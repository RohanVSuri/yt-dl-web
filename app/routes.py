from app import app
from flask import render_template, redirect, request, url_for, send_file, Response
from app.forms import LoginForm
from app.download import Down
from io import BytesIO

@app.route("/", methods=["POST","GET"])
def index():
    form = LoginForm()
    if request.method == "POST":
        # return redirect(url_for("tes"))
        link=form.link.data
        d=Down(link)
        # d.dl()
        # return redirect(url_for("test"))
        # return(redirect(d.dl()))
        result= send_file(d.dl(), as_attachment=True, attachment_filename="downlaoded.mp4")
        return result
        # return redirect("https://www.google.com")
    else:
        return render_template("dl.html", title="DOWNLOAD", form=form)

@app.route("/test")
def test():
    return render_template("test.html")
