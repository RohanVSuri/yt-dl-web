from pytube import YouTube, streams
import os
from os import listdir
from mutagen.mp4 import MP4, MP4Tags
from mutagen.easyid3 import EasyID3
class Down():
    def __init__(self, link, itag, title = "YouTube"):
        self.link = link
        self.yt = YouTube(self.link)
        self.title = self.yt.title.replace(".","")
        self.path = os.getcwd()+"/app/tmp/"
        self.itag = itag

    def dl(self):
        self.yt.streams.get_by_itag(self.itag).download(filename=self.title, output_path=self.path)

    def dl_link(self):
        # print(self.yt.streams.get_by_itag(self.itag).url)
        return self.yt.streams.get_by_itag(self.itag).url

    def convert(self, file_type):
        import moviepy.editor as mp
        if self.yt.streams.get_by_itag(self.itag).parse_codecs()[0]:
            clip = mp.VideoFileClip(f'app/tmp/{self.title}.{file_type}')
            clip.audio.write_audiofile(f'app/tmp/{self.title}.mp3')
            clip.close()
        else:
            clip = mp.AudioFileClip(f'app/tmp/{self.title}.{file_type}')
            clip.write_audiofile(f'app/tmp/{self.title}.mp3')
            clip.close()

    def change_metadata(self, title, artist, album, file_type):
        if file_type == "mp3":
            audio = EasyID3(f'app/tmp/{self.title}.mp3')
            audio["title"] = title
            audio["album"] = album
            audio["artist"] = artist
            audio.save()
        elif file_type == "mp4":
            audio = MP4(f'app/tmp/{self.title}.mp4')
            audio['\xa9nam'] = title
            audio['\xa9alb'] = album
            audio['\xa9ART'] = artist
            audio.save()

    def clear_folder(self):
        for file_name in listdir(self.path):
            os.remove(self.path + file_name)