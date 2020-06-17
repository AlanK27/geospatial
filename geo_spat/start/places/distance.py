from start.gmapu import gmap
from start.parse.parse_csv import parse_csv
from start.parse.jfiles import jfiles
import pandas as pd

class distance(jfiles, parse_csv):


    def __init__(self, gmap, parse_csv):
        self.gmap = gmap
        self.parse_csv = parse_csv
        self.resturants_coord = []
        self.school_coord = []
        self.data_2_csvdir = []


    def distance_calc(self, transportation='walking'):
        self.data_2_csvdir = self.data_path()
        df = self.get_csv_data(self.parse_csv, self.data_2_csvdir)
        self.df_to_dict(df)
        self.school_list()


        for resturant in self.resturants_coord.keys():
            result = self.gmap.distance_matrix(origins=self.school_coord['Arcadia High School'], destinations=self.resturants_coord[resturant], mode=transportation)

            header = ['dest', 'origin', 'distance km', 'duration s']
            p_list = []

            try: 
                p_list.append(result["destination_addresses"][0])

            except: 
                p_list.append(None)

            try: 
                p_list.append(result["origin_addresses"][0])

            except: 
                p_list.append(None)

            try: 
                p_list.append(result['rows'][0]['elements'][0]['distance']['value'])

            except: 
                p_list.append(None)

            try: 
                p_list.append(result['rows'][0]['elements'][0]['duration']['value'])

            except: 
                p_list.append(None)

            self.data_2_csv(p_list, f'{transportation}_distance_from_Arcadia_HS.csv', self.data_2_csvdir, header)




    def df_to_dict(self, df):

        data_file = self.data_2_csvdir + "\\arcadia_resturants.csv"

        df = pd.read_csv(data_file)
        names = df['name'].tolist()
        latitudes = df['latitude'].tolist()
        # longitudes = df['longitude'].tolist()
        longitudes = df['formatted_address'].tolist()
        coordinates = list(zip(longitudes,latitudes))
        self.resturants_coord = {name: coordinates[i] for i, name in enumerate(names)}
        return self.resturants_coord


    def school_list(self):
        data_file = self.data_2_csvdir + "\\school.csv"
        df = pd.read_csv(data_file)
        df.reset_index(inplace=True)
        names = df['school_name'].tolist()
        latitudes = df['latitude'].tolist()
        longitudes = df['longitude'].tolist()
        coordinates = list(zip(latitudes, longitudes))
        longitudes = df['longitude'].tolist()
        self.school_coord = {name: coordinates[i] for i, name in enumerate(names)}


