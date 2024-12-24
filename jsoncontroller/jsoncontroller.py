import json

class JsonController():
    def __init__(self, file_path):
        self._filepath = file_path
        self._jsondata = None

    def read_json(self):
        with open(self._filepath, "r") as file:
            json_data = json.load(file)
        return json_data

    def write_json(self, data = {}):
        with open(self._filepath, "w") as file:
            json.dump(data, file, indent=4)
    
    def load(self):
        self._jsondata = self.read_json()
        return self._jsondata
    
    def save(self, data = None):
        if data is None:
            self.write_json(self._jsondata)
        else:
            self.write_json(data)