from app import app
from flask import render_template, redirect, request, url_for, send_file, Response, send_from_directory
from app.forms import LoginForm
from app.download import Down
from io import BytesIO
import os
@app.route("/", methods=["POST","GET"])
def index():
    form = LoginForm()
    if request.method == "POST":
        link=form.link.data
        d=Down(link)
        d.dl()
        d.clear_folder()
        # return send_from_directory('download', d.title+'.mp4', as_attachment=True)
        # return send_file(d.title+".mp4", as_attachment=True)
        return send_file(f"download/{d.title}.mp4", as_attachment=True)
        # return redirect(url_for("download", title=d.title+'.mp4'))
        # return render_template('test.html', title=d.title)
    else:
        return render_template("dl.html", title="DOWNLOAD", form=form)

@app.route("/download/<title>")
def download(title):
    # return send_file(title+".mp4", as_attachment=True)
    # return send_from_directory('download', title)
    # return render_template("test.html")
    # return send_from_directory(app.config["DOWNLOAD"], filename=title, as_attachment=True)
    print(title)
    return send_from_directory("/download", filename=title, as_attachment=True)
    # return send_file("KW.mp3", as_attachment=True)
