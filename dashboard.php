<?php
session_start();
if (!isset($_SESSION['username'])) {
    header("Location: login.php");
    exit();
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard | Mindmap AI</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
<?php include 'includes/navbar.php'; ?>
<h2 style="color:darkblue; text-align: left; font-style:italic">Xin chào, <?php echo $_SESSION['username']; ?></h2>
<h1 style="color:darkblue">Khám phá các loại Mindmap </h1>

<div class="app-grid">
    <div class="app-card">
        <img src="images/app.1.jpg" alt="App 1">
        <h3 style="color:darkgreen">Chuyển đổi file PDF thành biểu đồ Mindmap </h3>
        <p>App ứng dụng Gemini AI trích xuất các từ khóa từ file PDF và trực quan hóa 
            thành biểu đồ Mindmap.</p>
        <a href="https://ai-mindmap-2.streamlit.app"><button>Bắt đầu</button></a>
    </div>
    <div class="app-card">
        <img src="images/app.2.jpg" alt="App 2">
        <h3 style="color:darkgreen">Mindmap tích hợp AI </h3>
        <p>Xuất biểu đồ Mindmap dựa trên những câu mô tả đơn giản với Gemini AI
            </p>
        <a href="https://ai-mindmap-1.streamlit.app"><button>Bắt đầu</button></a>
    </div>
    <div class="app-card">
        <img src="images/app_3.jpg" alt="App 3">
        <h3 style="color:darkgreen">Timeline map tích hợp AI </h3>
        <p>Xuất biểu đồ Timeline trực quan về dòng thời gian dựa trên những câu mô tả đơn giản với AI.</p>
        <a href="https://ai-mindmap-3.streamlit.app"><button>Bắt đầu</button></a>
    </div>
    <div class="app-card">
        <img src="images/app_4.jpg" alt="App 4">
        <h3 style="color:darkgreen">Flowchart tích hợp AI</h3>
        <p>Xuất biểu đồ Flowchart trực quan hóa quy trình dựa trên những câu mô tả đơn giản với AI.</p>
        <a href="https://ai-mindmap-4.streamlit.app"><button>Bắt đầu</button></a>
    </div>
</div>


<?php include 'includes/footer.php'; ?>
</body>
</html>

<style>
.app-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 60px;
    justify-content: center;
    margin: 20px 20px 10px 10px;
    }
.app-card {
    width: 35%;
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 10px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
.app-card img {
    width: 100%;
    height: auto;
    border-radius: 8px;
        }
.app-card button {
    margin-top: 10px;
    padding: 10px 20px;
    background-color: darkblue;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    }
.app-card button:hover {
    background-color: navy;
    }
</style>