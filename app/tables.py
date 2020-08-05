from flask_table import Table, Col, ButtonCol
from pytube import YouTube, itags, streams
import urllib.request
class ItemTable(Table):
    classes = ["table"]
    itag = Col('itag')
    res = Col('Resolution')
    bitrate = Col('bitrate')
    file_type = Col('Filetype')
    size = Col('size')
    button = ButtonCol('Download', endpoint="download",
    button_attrs={'id': 'dl_button','onclick':'update_form_info(this)'}, form_attrs={'action': ''},
    form_hidden_fields={'itag':'temp_itag', 'file_type': 'temp_file_type'})

class Item(object):
    def __init__(self, itag, res, bitrate, file_type, size):
        self.itag = itag
        self.res = res
        self.bitrate = bitrate
        self.file_type = file_type
        self.size = size

class Tables():
    def __init__(self, link, webm):
        self.link=link
        self.yt = YouTube(self.link)
        self.items = []
        self.webm = webm

    def fill_table(self):
        self.itag_list = self.yt.get_itag_list()
        self.itag_list.sort()
        print(self.itag_list, "before")
        for x in self.itag_list:
            try:
                urllib.request.urlopen(self.yt.streams.get_by_itag(x).url)
                # pytube for sometimes gives streams that dont exist, this doesn't allow them through
            except:
                # self.itag_list.remove(x) - for some reason this doesnt work
                print(x, "FAILED!")
                continue
            else:
                if (not (self.yt.streams.get_by_itag(x).parse_codecs()[0] and self.yt.streams.get_by_itag(x).parse_codecs()[0][0:4] == "av01")):
                    # gets rid of av01 codec bc it sucks
                    print(x,"continuing")
                    if not (itags.get_format_profile(x)['file_type'] == "webm" and self.webm == True):
                        #currently not able to change metadata of webm files, so this gets rid of them
                        self.items.append(
                            Item(
                                x,
                                itags.get_format_profile(x)['resolution'],
                                itags.get_format_profile(x)['abr'],
                                itags.get_format_profile(x)['file_type'],
                                str(self.yt.streams.get_by_itag(x).filesize_approx/1000000) + " MB" # sizes are NOT accurate, only estimates
                            )
                        )
        print(self.itag_list, "after")
    def return_table(self):
        table = ItemTable(self.items)
        return table
