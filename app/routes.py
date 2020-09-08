from app import app, socketio
from flask import render_template, redirect, request, url_for, send_file, Response, session, jsonify
from app.forms import DownloadForm, SubmitForm
from app.download import Down
from app.tables import Tables
import pytube
import os

# @app.route("/", methods = ["GET", "POST"])
@app.route("/")
def index():
    form = DownloadForm()
    # if request.method == "POST":
    #     pass
        # link = form.link.data
        # metadata = []
        # if request.form.get("metadata") == "y":
        #     metadata = [form.title.data, form.artist.data, form.album.data]
        # convert = form.convert.data

        # if "dl_button" in request.form:
        #     itag = request.form.get("itag")
        #     file_type = request.form.get('file_type')
        #     d = Down(link=link, itag=int(itag))
        #     d.clear_folder()
        #     if(len(metadata) > 0 or convert):
        #         print("first if")
        #         print("Downloading...")
        #         socketio.emit('message', {'text' : 'Downloading'}, namespace= '/test')
        #         d.dl()
        #         if convert:
        #             print("Converting to mp3...")
        #             socketio.emit('message', {'text' : 'Converting to mp3'}, namespace= '/test')
        #             d.convert(file_type)
        #             file_type='mp3'
        #         if len(metadata) > 0:
        #             print("Changing Metadata...")
        #             socketio.emit('message', {'text' : 'Changing Metadata'}, namespace= '/test')
        #             d.change_metadata(title=metadata[0], artist=metadata[1], album=metadata[2], file_type=file_type)
        #         socketio.emit('message', {'text' : 'Done'}, namespace= '/test')
        #         return send_file(f"tmp/{d.title}.{file_type}", as_attachment=True)
        #     else:
        #         print("second if")
        #         filename = f"{d.title}.{file_type}"
        #         filename = filename.replace(" ", "_")
        #         response = Response(pytube.request.stream(d.dl_link()), mimetype=f'video/{file_type}', headers={"Content-Disposition":"attachment; filename=" + filename})
        #         return response
    # else:
    return render_template("test.html", title="DOWNLOAD", form=form)

    

@app.route("/update", methods = ["POST"])
def update():
    form = DownloadForm()

    link = form.link.data
    metadata=[]
    if request.form.get("metadata") == "y":
        metadata = [form.title.data, form.artist.data, form.album.data]
    table = Tables(link, webm=(metadata!=[]))
    d = Down(link)
    table.fill_table()
    table = table.return_table()
    # socketio.emit('message', {'text' : 'hello what is up '}, namespace= '/test')
    return jsonify({'html' : table.__html__(), 'thumbnail' : d.thumbnail_url, 'title' : d.title})

@app.route('/download', methods = ["POST"])
def download():
    form = DownloadForm()
    print(form.data)
    link = form.link.data
    itag = form.itag.data
    file_type = form.file_type.data
    metadata = []
    if form.data.get('metadata'):
        metadata = [form.title.data, form.artist.data, form.album.data]
    convert = form.convert.data
    socketio.emit('message', {'text' : 'HELLOOOO'}, namespace= '/test')
    d = Down(link=link, itag=int(itag))
    d.clear_folder()
    if(len(metadata) > 0 or convert):
        print("first if")
        print("Downloading...")
        socketio.emit('message', {'text' : 'Downloading'}, namespace= '/test')
        d.dl()
        if convert:
            print("Converting to mp3...")
            socketio.emit('message', {'text' : 'Converting to mp3'}, namespace= '/test')
            d.convert(file_type)
            file_type='mp3'
        if len(metadata) > 0:
            print("Changing Metadata...")
            socketio.emit('message', {'text' : 'Changing Metadata'}, namespace= '/test')
            d.change_metadata(title=metadata[0], artist=metadata[1], album=metadata[2], file_type=file_type)
        socketio.emit('message', {'text' : 'Done'}, namespace= '/test')
        return send_file(f"tmp/{d.title}.{file_type}", as_attachment=True)
    else:
        print("second if")
        filename = f"{d.title}.{file_type}"
        filename = filename.replace(" ", "_")
        response = Response(pytube.request.stream(d.dl_link()), mimetype=f'video/{file_type}', headers={"Content-Disposition":"attachment; Access-Control-Expose-Headers: Content-Disposition; filename=" + filename})
        return response
        # return d.dl_link()


    # return jsonify(success=True)