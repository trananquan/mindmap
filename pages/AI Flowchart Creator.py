import streamlit as st
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.warning("Please login first.")
    st.stop()

from groq import Groq
import streamlit.components.v1 as components
import json

# Setup Groq API
API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=API_KEY)

def get_flowchart_data_from_groq(description):
    prompt = f"""
    Given the description below, generate ONLY flowchart data in strict JSON format.  If requirement is in Vietnamese, keep structure of built diagram 
    and show result in diagram in Vietnamese language.
    
    Output example:

    {{
      "nodes": [
        {{"id": "A", "text": "Start"}},
        {{"id": "B", "text": "Process"}},
        {{"id": "C", "text": "Decision"}},
        {{"id": "D", "text": "End"}}
      ],
      "edges": [
        {{"from": "A", "to": "B"}},
        {{"from": "B", "to": "C"}},
        {{"from": "C", "to": "D", "condition": "Yes"}},
        {{"from": "C", "to": "B", "condition": "No"}}
      ]
    }}

    Rules:
    - 'id' must be a single letter like A, B, C, etc.
    - 'condition' is optional, only for decisions.
    - No extra explanations.

    Description: {description}
    """
    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"system",
                "content":"Return only valid JSON."
            },
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.2,

        max_tokens=4096
    )

    text = response.choices[0].message.content.strip()

    start = text.find('{')
    end = text.rfind('}')
    json_text = text[start:end+1]
    flowchart_data = json.loads(json_text)
    return flowchart_data

def build_mermaid_flowchart(title, data, flow_direction='TD'):
    nodes = data['nodes']
    edges = data['edges']
    
    mermaid = f"flowchart {flow_direction}\n"
    mermaid += f"    %% {title}\n"
    
    special_nodes = {"Start": "startend", "End": "startend"}
    
    # Node Definitions
    for node in nodes:
        shape = ""
        if node['text'].lower() in ["start", "end", "bắt đầu", "kết thúc"]:
            shape = f"(({node['text']}))"  # Circle double parentheses
        elif "decision" in node['text'].lower():
            shape = f"{{{node['text']}}}"  # Diamond for decision
        else:
            shape = f"[{node['text']}]"  # Normal rectangular node
        mermaid += f"    {node['id']}{shape}\n"
    
    # Edge Definitions
    for edge in edges:
        if 'condition' in edge:
            mermaid += f"    {edge['from']} -- \"{edge['condition']}\" --> {edge['to']}\n"
        else:
            mermaid += f"    {edge['from']} --> {edge['to']}\n"

    # Class Definitions for styling
    mermaid += """
    classDef startend fill:#4CAF50,stroke:#333,stroke-width:2px;
    classDef decision fill:#FF9800,stroke:#333,stroke-width:2px;
    classDef process fill:#2196F3,stroke:#333,stroke-width:2px;
    """

    # Assign classes
    for node in nodes:
        if node['text'].lower() in ["start", "end", "bắt đầu", "kết thúc"]:
            mermaid += f"    class {node['id']} startend;\n"
        elif "decision" in node['text'].lower():
            mermaid += f"    class {node['id']} decision;\n"
        else:
            mermaid += f"    class {node['id']} process;\n"
    
    return mermaid


def render_mermaid(mermaid_code):
    components.html(
        f"""
        <script type="module">
          import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
          mermaid.initialize({{ startOnLoad: true }});
        </script>
        <div class="mermaid">
        {mermaid_code}
        </div>
        """,
        height=800,
        scrolling=True,
    )

# Streamlit UI
st.set_page_config(page_title="AI Flowchart Builder", page_icon="🧠", layout="wide")
st.title("📊 AI-Powered Flowchart Creator")
st.markdown(
        """
        <style>
        h1 {
            text-align: center;
            color: darkblue;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

title = st.text_input("Flowchart Title/ Tên biểu đồ", placeholder="Input Flowchart title.....")
description = st.text_area("Enter a description for the flowchart/ Nhập mô tả cho biểu đồ", placeholder="Input Flowchart description here.....", height=150)
flow_direction = st.selectbox("Flow Direction/ Hướng biểu đồ", options=["TD (Top-Down)", "LR (Left-Right)", "BT (Bottom-Top)", "RL (Right-Left)"])

# Mapping for short code
flow_direction_short = {
    "TD (Top-Down)": "TD",
    "LR (Left-Right)": "LR",
    "BT (Bottom-Top)": "BT",
    "RL (Right-Left)": "RL"
}[flow_direction]

if st.button("Create Flowchart"):
    if description:
        with st.spinner('AI is building Flowchart...'):
            try:
                flowchart_data = get_flowchart_data_from_groq(description)
                mermaid_code = build_mermaid_flowchart(title, flowchart_data, flow_direction_short)
                st.subheader("Generated Flowchart Diagram")
                render_mermaid(mermaid_code)
                st.code(mermaid_code, language='markdown')
            except Exception as e:
                st.error(f"Error generating Flowchart: {e}")
    else:
        st.warning("Please enter a description first.")

st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: blue;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
        }
        div.stButton > button:hover {
            background-color: #002244;
        }
        </style>
        """,
        unsafe_allow_html=True
)

