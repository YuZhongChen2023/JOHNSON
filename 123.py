from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A 411147055 陳昱中的求職相關資訊</h1>"
    homepage += "<a href=/about>我的個人簡介</a><br>"
    homepage += "<a href=/work>資管相關工作介紹</a><br>"
    homepage += "<a href=/welcome?johnson=陳昱中>職涯測驗結果</a><br>"
    homepage += "<a href=/proflie>求職履歷</a><br>"
    return homepage

@app.route("/about")
def about():
    return "<h1>陳昱中(YU-ZHONG  CHEN)<h1>"
    "<h1>靜宜大學 / 資訊管理學系</h1>"
    <img src="IMG_20231113_214016_1""img-fluid rounded-circle" width="50%" id="pic" onmouseover="change1()" onmouseout="change2()"></img>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

<nav class="navbar navbar-expand-md bg-primary navbar-dark">
    <a class="navbar-brand" href="#">MENU</a>
                    
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="collapsibleNavbar">
        <ul class="navbar-nav">
            <li class="nav-item"><a class="nav-link" href="#aboutme">關於我</a></li>
            <li class="nav-item"><a class="nav-link" href="#motto">座右銘</a></li>
            <li class="nav-item"><a class="nav-link" href="#youtube">推薦影片</a></li>
        </ul>
    </div>
</nav>
     <table width="70%" border="1">
  <tr>
   <td>
   <h1 id="aboutme">關於我</h1>
   <table width="70%" border="1">
  系級：資管二A
   學號: 411147055
   E-Mail: <a href="s1114705@pu.edu.tw">s1114705@pu.edu.tw</a><br>
   <td>
   


@app.route("/work")
def work():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("johnson")
    return render_template("welcome.html", name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")  

#if __name__ == "__main__":
    #app.debug = True
    #app.run()
    
