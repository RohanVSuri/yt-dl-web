from app import app
from flask import render_template, redirect, request, url_for, send_file, Response, session
from app.forms import Form
from app.download import Down
from app.tables import Tables
import pytube
import os

@app.route("/", methods=["POST","GET"])
def index():
    form = Form()
    if request.method == "POST":
        session["LINK"] = form.link.data
        print(request.form.get('metadata'), 'CHECKBOX METADATA')
        session["METADATA"] = []
        if request.form.get("metadata") == "y":
            session["METADATA"] = [form.title.data, form.artist.data, form.album.data]
        session["CONVERT"] = form.convert.data
        print(session["METADATA"])
        return redirect(url_for("download"))
    else:
        session.clear()
        return render_template("home.html", title="DOWNLOAD", form=form)

@app.route('/download', methods=["POST","GET"])
def download():
    itag = request.form.get("itag")
    file_type = request.form.get('file_type')

    link=session["LINK"]
    metadata = session["METADATA"]
    convert = session["CONVERT"]

    form=Form()
    d = Down(link=link)

    if request.method == "POST":
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
            
    elif request.method == "GET":
        table = Tables(link, webm=(metadata!=[]))
        table.fill_table()
        table = table.return_table()
        video_title = d.title
        return render_template("download.html", title="Download", table=table, video_title=d.title, thumbnail=d.thumbnail_url, link=link)
