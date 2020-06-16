import json
import os


class jfiles:


    def __init__(self):
        self.data_paths = os.path.abspath('..') + "\\data"

    def data_path(self):
        self.data_paths = os.path.abspath('..') + "\\data"
        return self.data_paths

    def json_dump(self, jfile, name):
        with open(self.data_paths + f'\\{name}.json', 'w') as wf:
            json.dump(jfile, wf, indent = 5)

    def json_dumps(self, jfile):
        return json.dumps(jfile, indent = 5)

    def json_load(self, name):
        with open(self.data_paths + f'\\{name}', 'r') as rf:
            j = json.load(rf)
        return j

