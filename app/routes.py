from app import app
from flask import render_template, redirect, request, url_for, send_file, Response, session, jsonify
from app.forms import Form
from app.download import Down
from app.tables import Tables
import pytube
import os

@app.route("/", methods = ["GET", "POST"])
def index():
    form = Form()
    if request.method == "POST":
        link = form.link.data
        metadata = []
        if request.form.get("metadata") == "y":
            metadata = [form.title.data, form.artist.data, form.album.data]
        convert = form.convert.data

        if "dl_button" in request.form:
            itag = request.form.get("itag")
            file_type = request.form.get('file_type')
            d = Down(link=link, itag=int(itag))
            d.clear_folder()
            if(len(metadata) > 0 or convert):
                print("first if")
                print("Downloading...")
                d.dl()
                if convert:
                    print("Converting to mp3...")
                    d.convert(file_type)
                    file_type='mp3'
                if len(metadata) > 0:
                    print("Changing Metadata...")
                    d.change_metadata(title=metadata[0], artist=metadata[1], album=metadata[2], file_type=file_type)
                return send_file(f"tmp/{d.title}.{file_type}", as_attachment=True)
            else:
                print("second if")
                filename = f"{d.title}.{file_type}"
                filename = filename.replace(" ", "_")
                response = Response(pytube.request.stream(d.dl_link()), mimetype=f'video/{file_type}', headers={"Content-Disposition":"attachment; filename=" + filename})
                return response
    else:
        return render_template("test.html", title="DOWNLOAD", form=form)

@app.route("/update", methods = ["POST"])
def update():
    form = Form()

    link = form.link.data
    if request.form.get("metadata") == "y":
        metadata = [form.title.data, form.artist.data, form.album.data]
    convert = form.convert.data    
    table = Tables(link, webm=False)
    d = Down(link)
    table.fill_table()
    table = table.return_table()
    return jsonify({'html' : table.__html__(), 'thumbnail' : d.thumbnail_url, 'title' : d.title})
