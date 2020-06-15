from app import app
from flask import render_template, redirect, request, url_for, send_file, Response, send_from_directory
from app.forms import Form
from app.download import Down

import pytube

from io import BytesIO
import os
@app.route("/", methods=["POST","GET"])
def index():
    form = Form()
    if request.method == "POST":
        link=form.link.data
        d=Down(link=link, extension=form.ext.data)

        print(f'Link: {d.dl_link()}')

        response = Response(pytube.request.stream(d.dl_link()), mimetype='video/mp4')
        response.headers['Content-Disposition'] = 'attachment'
        return response
        # return render_template('test.html', title=d.title)
    else:
        # print(request.form.get("metadata"))
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
