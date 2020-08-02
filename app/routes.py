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
        session["METADATA"] = [form.title.data, form.artist.data, form.album.data]
        session["CONVERT"] = form.convert.data
        return redirect(url_for("download"))
    else:
        return render_template("dl.html", title="DOWNLOAD", form=form)

@app.route('/download', methods=["POST","GET"])
def download():
    itag = request.form.get("itag")
    file_type = request.form.get('file_type')

    link=session["LINK"]
    metadata = session["METADATA"]
    convert = session["CONVERT"]

    form=Form()
    
    if request.method == "POST":
        d = Down(link=link, itag=int(itag))

        if(metadata[0] or convert):
            print("first if")
            print("Downloading...")
            d.dl()
            if convert:
                print("Converting...")
                d.convert()
                file_type='mp3'
            if metadata[0]:
                print("Changing Metadata...")
                # d.change_metadata(title=metadata[0], artist=metadata[1], album=metadata[2])
            return send_file(f"tmp/{d.title}.{file_type}", as_attachment=True)
        else:
            print("second if")
            filename = f"{d.title}.{file_type}"
            filename = filename.replace(" ", "_")
            print(filename)
            response = Response(pytube.request.stream(d.dl_link()), mimetype=f'video/{file_type}', headers={"Content-Disposition":"attachment; filename=" + filename})
            return response
            
    elif request.method == "GET":
        table = Tables(link)
        table.fill_table()
        table = table.return_table()
        return render_template("dl.html", title="Download", form=form, table=table)
