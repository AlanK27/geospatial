import googlemaps
import os

class gmap:


    def __init__(self):
        self.key = []
        self.gmapu = []

    def kay(self):
        with open(os.path.abspath('..')+'\\key.txt', 'r') as rf:
            api_key = rf.read()
        self.key = str(api_key)

    def start_key(self):
        self.kay()
        self.gmapu = googlemaps.Client(key=self.key)
        return self.gmapu
