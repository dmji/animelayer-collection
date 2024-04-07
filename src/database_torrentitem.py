class TorrentItem:
    def __init__(self):
        self.guid = ""
        self.name_original = ""
        self.name_translated = ""
        self.status = "" 
        self.update_date = "" 
        self.update_created = "" 
        self.country = "" 
        self.type = "" 
        self.director = "" 
        self.serie_duration = "" 
        self.descriptions = ""
        self.resolution = ""
        self.subtitles = ""
        self.language = ""
        self.update_reason = ""
        self.poster_image_ref = "" 
        self.poster_image_blob = "" 

    def __str__(self):
        return f'{self.guid}: {self.name}\n{self.descriptions}\n{self.ref_image}'
    
    def __repr__(self):
        return self.__str__()
    
    def compareWith(self, item):
        if(self.guid == item.guid and self.name == item.name):
            return
        print(f"{self.guid} already exist, probobly changed, TODO: comparator TorrentItem::compareWith")