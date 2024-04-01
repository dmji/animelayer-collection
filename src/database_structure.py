import json

class TorrentData:
    def __init__(self):
        self.guid = ""
        self.name = ""
        self.descriptions = []
        self.ref_image = "" 

    def __str__(self):
        return f'{self.guid}: {self.name}\n{self.descriptions}\n{self.ref_image}'
    
    def __repr__(self):
        return self.__str__()
    
    def compareWith(self, item):
        if(self.guid == item.guid and self.name == item.name):
            return
        print(f"{self.guid} already exist, probobly changed, TODO: comparator TorrentData::compareWith")        

    def to_json(self, path):
        item = {
            'guid': self.guid,
            'name': self.name,
            'descriptions': self.descriptions,
            'ref_image': self.ref_image
        }
        with open(path, 'w') as file:
            json.dump(item, file)

    def from_json(path:str):
        item = TorrentData()
        with open(path, 'r') as file:
            data = json.load(file)
        if(data != None):
            temp = data.get('guid')
            if(temp != None):
               item.guid = temp

            temp = data.get('name')
            if(temp != None):
                item.name = temp

            temp = data.get('descriptions')
            if(temp != None):
                item.descriptions = temp

            temp = data.get('ref_image')
            if(temp != None):
                item.ref_image = temp
        return item