from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二A 411147055 陳昱中的求職網頁</h1>"
    homepage += "<a href=/about>我的個人簡介</a><br>"
    homepage += "<a href=/work>資管相關工作介紹</a><br>"
    homepage += "<a href=/ucantest>職涯測驗結果</a><br>"
    homepage += "<a href=/autobiographyprofile>求職履歷</a><br>"
    return homepage

@app.route("/about")
def johnson():
    return render_template("johnson.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/ucantest")
def ucantest():
	return render_template("ucantest.html")

@app.route("/autobiographyprofile")
def autobiographyprofile():
    return render_template("autobiographyprofile.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
    