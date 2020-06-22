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
        d.clear_folder()
        # print(f'Link: {d.dl_link()}')
        d.dl()
        if(form.ext.data=="mp3"):
            d.convert()
        d.change_metadata(title=form.title.data, artist=form.artist.data, album=form.album.data)
        return send_file(f"tmp/{d.title}.{form.ext.data}", as_attachment=True)
        # response = Response(pytube.request.stream(d.dl_link()), mimetype='video/mp4')
        # response.headers['Content-Disposition'] = 'attachment'
        # return response

    else:
        return render_template("dl.html", title="DOWNLOAD", form=form)
