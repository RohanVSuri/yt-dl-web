from app import app
from flask import render_template, redirect, request, url_for, send_file, Response
from app.forms import LoginForm
from app.download import Down
from io import BytesIO
import os
@app.route("/", methods=["POST","GET"])
def index():
    form = LoginForm()
    if request.method == "POST":
        # return redirect(url_for("tes"))
        link=form.link.data
        d=Down(link)
        d.dl()
        # return(redirect(d.dl()))
        return send_file(d.title+".mp4", as_attachment=True)
        os.remove(d.title+".mp4")
        # return send_file("KW.mp3",attachment_filename="hello.mp4", as_attachment=True)
        # return redirect(url_for("test"))
        #
        # return result
        # return redirect("https://www.google.com")
    else:
        return render_template("dl.html", title="DOWNLOAD", form=form)

@app.route("/test")
def test():
    # return render_template("test.html")
    return send_file("KW.mp3", as_attachment=True)
