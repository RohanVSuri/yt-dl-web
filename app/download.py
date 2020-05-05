from pytube import YouTube

class Down():
    def __init__(self, link):
        self.link = link

    def dl(self):
        yt = YouTube(self.link)
        abs_link = yt.streams.filter(file_extension='mp4').first().url
        # print(abs_link)
        print("we be downloading" + self.link)
        return abs_link
