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
def course():
    return "<h1></h1>"

@app.route("/today")
def today():
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
    
