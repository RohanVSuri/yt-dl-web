from app import app
from flask import render_template, redirect, request, url_for, send_file, Response, send_from_directory
from app.forms import Form
from app.download import Down
from app.tables import Tables
import pytube
import os

@app.route("/", methods=["POST","GET"])
def index():
    form = Form()
    if request.method == "POST":
        link=form.link.data
        metadata=[form.title.data, form.artist.data, form.album.data]
        return redirect(url_for("download", link=link, metadata=metadata))
    else:
        return render_template("dl.html", title="DOWNLOAD", form=form)

@app.route('/download', methods=["POST","GET"])
def download():
    link=request.args.get("link")
    itag = request.form.get("itag")
    metadata = request.args.getlist('metadata')
    # print(request.form['metadata'], "woop")
    print(metadata)
    form=Form()
    print(link)
    if request.method == "POST":
        d = Down(link=link, itag=int(itag))
        if(metadata[0]):
            print("first if")
            print("Downloading...")
            d.dl()
            print("Converting...")
            d.convert()
            print("Changing Metadata...")
            # d.change_metadata(title=metadata[0], artist=metadata[1], album=metadata[2])
            return send_file(f"tmp/{d.title}.mp3", as_attachment=True)
        else:
            print("second if")
            filename = f"{d.title}.mp4"
            filename = filename.replace(" ", "_")
            print(filename)
            response = Response(pytube.request.stream(d.dl_link()), mimetype='video/mp4', headers={"Content-Disposition":"attachment; filename=" + filename})
            return response
    elif request.method == "GET":
        table = Tables(link)
        table.fill_table()
        table = table.return_table()
        return render_template("dl.html", title="Download", form=form, table=table)
