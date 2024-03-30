import json

class TorrentData:
    def init(self):
        self.guid = ""
        self.name = ""

    def __str__(self):
        return f'{self.guid}: {self.name}'
    
    def __repr__(self):
        return self.__str__()
    
    def compareWith(self, item):
        if(self.guid == item.guid and self.name == item.name):
            return
        print(f"{self.guid} already exist, probobly changed, TODO: comparator TorrentData::compareWith")        

    def to_json(self, path):
        item = {
            'guid': self.guid,
            'name': self.name
        }
        with open(path, 'w') as file:
            json.dump(item, file)

    def from_json(self, path):
        with open('data.json', 'r') as file:
            data = json.load(file)
        if(data != None):
            self.guid = data.guid
            self.name = data.name