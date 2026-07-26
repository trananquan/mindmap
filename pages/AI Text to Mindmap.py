import streamlit as st
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

from groq import Groq
import streamlit.components.v1 as components
import re


def configure_groq():
    try:
        global client
        client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )
        return True
    except Exception as e:
        st.error(f"Error configuring Groq API: {str(e)}")
        return False

def extract_final_nodes(markdown_content):
    """Extract the leaf nodes (lines with no deeper child lines) from the markdown."""
    lines = markdown_content.strip().splitlines()
    levels = []
    final_nodes = []

    for i, line in enumerate(lines):
        if not line.strip():
            continue
        level = line.count('#')
        if level == 0:
            continue
        is_final = True
        for j in range(i + 1, len(lines)):
            next_line = lines[j]
            next_level = next_line.count('#')
            if next_level > level:
                is_final = False
                break
            if next_level <= level and next_line.count('#') > 0:
                break
        if is_final:
            final_nodes.append(line.strip('# ').strip())

    return final_nodes

def explain_terms_with_groq(terms):
    """Generate explanations for a list of terms using Groq AI."""
    try:

        explanations = {}
        for term in terms:

            prompt = f"Explain the following term in a simple and concise way:\n\nTerm: {term}"
            response = client.chat.completions.create(

                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert teacher. Explain concepts clearly, simply, and concisely."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.3,
                max_tokens=512

            )

            explanation = response.choices[0].message.content.strip()

            if not explanation:
                explanation = "No explanation available."

            explanations[term] = explanation
        return explanations

    except Exception as e:

        st.error(f"Error generating explanations: {str(e)}")

        return {}

def generate_mindmap_from_prompt(prompt_text):
    """Generate a mindmap markdown from a user-provided prompt text."""
    try:

        prompt = f"""
        Create a hierarchical markdown mindmap from the following text.
        Use proper markdown heading syntax (# for main topics, ## for subtopics, ### for details).
        Focus on the main concepts and their relationships.
        Include relevant details and connections between ideas.
        Keep the structure clean and organized.

        Format the output exactly like this example:
        # Main Topic
        ## Subtopic 1
        ### Detail 1
        - Key point 1
        - Key point 2
        ### Detail 2
        ## Subtopic 2
        ### Detail 3
        ### Detail 4

        Text to analyze: {prompt_text}
        Respond only with the markdown mindmap, no additional text.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",

            messages=[
                {
                    "role": "system",
                    "content": "You are an expert at creating hierarchical markdown mindmaps. Always return only the markdown mindmap without any explanation."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3,
            max_tokens=4096

        )

        markdown = response.choices[0].message.content.strip()

        # Xóa markdown code fence nếu Groq trả về
        markdown = re.sub(r"^```(?:markdown|md)?\s*", "", markdown)
        markdown = re.sub(r"\s*```$", "", markdown)
        markdown = markdown.strip()

        if not markdown:
            st.error("Received empty response from Groq")
            return None

        return markdown

        return markdown

    except Exception as e:
        st.error(f"Error generating mindmap: {str(e)}")
        return None

def create_markmap_html(markdown_content):
    """Create HTML for Markmap visualization."""

    markdown_content = (
        markdown_content
        .replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("${", "\\${")
    )

    html_content = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>
html, body {{
    margin:0;
    padding:0;
    width:100%;
    height:100%;
}}

#mindmap {{
    width:100%;
    height:650px;
}}
</style>

<script src="https://cdn.jsdelivr.net/npm/d3@6"></script>
<script src="https://cdn.jsdelivr.net/npm/markmap-view"></script>
<script src="https://cdn.jsdelivr.net/npm/markmap-lib@0.15.4/dist/browser/index.min.js"></script>

</head>
<body>
<svg id="mindmap"></svg>

<script>

window.onload = () => {{

    try {{

        const markdown = `{markdown_content}`;
        const transformer = new markmap.Transformer();
        const result = transformer.transform(markdown);
        const root = result.root;
        const mm = new markmap.Markmap(
            document.querySelector("#mindmap"),
            {{
                autoFit:true,
                duration:500,
                initialExpandLevel:2,
                maxWidth:300,
                paddingX:16
            }}
        );

        mm.setData(root);
        mm.fit();

    }}
    catch(err){{
        document.body.innerHTML =
        "<h3 style='color:red'>"+err+"</h3>";

        console.error(err);
    }}

}}

</script>

</body>
</html>
"""

    return html_content

def main():
    st.set_page_config(page_title="Text to Mindmap", page_icon="🧠", layout="wide")
    st.title("📚 AI Text to MindMap Creator")

    if not configure_groq():
        return

    st.subheader("📓 Create Mindmap from Prompt")
    prompt_text = st.text_area("Input your text prompt:", height=200)

    if st.button("Create Mindmap"):
        if prompt_text.strip():
            with st.spinner("🔄 Generating mindmap..."):
                markdown_content = generate_mindmap_from_prompt(prompt_text)

                if markdown_content:
                    tab1, tab2, tab3 = st.tabs(["📊 Mindmap", "📝 Markdown", "🔍 Explanations"])

                    with tab1:
                        st.subheader("Interactive Mindmap")
                        html_content = create_markmap_html(markdown_content)
                        components.html(html_content, height=700, scrolling=True)

                    with tab2:
                        st.subheader("Markdown")
                        st.text_area("Markdown Content", markdown_content, height=400)
                        st.download_button(
                            label="⬇️ Download Markdown",
                            data=markdown_content,
                            file_name="mindmap_from_prompt.md",
                            mime="text/markdown"
                        )

                    with tab3:
                        st.subheader("Explanations for Final Nodes")
                        final_terms = extract_final_nodes(markdown_content)
                        if final_terms:
                            explanations = explain_terms_with_groq(final_terms)
                            for term, explanation in explanations.items():
                                st.markdown(f"**{term}**: {explanation}")
                        else:
                            st.info("No final nodes found to explain.")

if __name__ == "__main__":
    main()

st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: blue;
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: bold;
    padding: 0.5rem 1rem;
}

div.stButton > button:first-child:hover {
    background-color: #002244;
    color: white;
}

div.stButton > button:first-child:active {
    background-color: #0D47A1;
}
</style>
""", unsafe_allow_html=True)

