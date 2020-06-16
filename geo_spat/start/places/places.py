from start.gmapu import gmap
from start.parse.jfiles import jfiles
import os
import pandas as pd


class places(gmap, jfiles):


    def __init__(self):
        super().__init__()
        self.next_token = []
        self.data_pathed = []
        self.coord_dict = []
        
    def get_data(self):
        self.data_pathed = self.data_path()

        data_file = self.data_pathed + "\\school.csv"
        df = pd.read_csv(data_file)

        school_names = df['school_name'].tolist()
        latitudes = df['latitude'].tolist()
        longitudes = df['longitude'].tolist()
        coordinates = list(zip(latitudes, longitudes))
        self.coord_dict = {school: coordinates[i] for i, school in enumerate(school_names)}

        result = self.start_key().places('restaurants', location = self.coord_dict['Arcadia High School'], open_now = False)
        self.next_token = result['next_page_token']
        return result

    def get_next_data(self):
        print(self.next_token)
        result = self.start_key().places('restaurants', page_token = self.next_token)
        self.next_token = result['next_page_token']
        return result




