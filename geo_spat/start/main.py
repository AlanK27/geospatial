import os
import pandas as pd
from start.analysis.analysis import analyze_resturants
from start.parse.jfiles import jfiles
from start.places.places import places
from start.places.distance import distance
from start.gmapu import gmap
import sys



class initiate(places):


    def __init__(self):
        super().__init__()
        pass

    def starting(self, page = 1):

        self.start_key()
        j_file = self.get_data()
        self.json_dump(j_file, 'arcadia_0')

        if page > 0:
            for n in range(page):
                j_file = self.get_next_data()
                self.json_dump(j_file, f'arcadia_{n+1}')




def starts():
    lis = {
        1: 'initate (create json)',
        2: 'analyze_resturants (create csv)',
        3: 'distance from school (create csv)'

    }
    sf = pd.Series(lis)
    print(sf)
    in_u = input('what is the input')

    if in_u == '1':
        x = initiate()
        x.start_key()
        x.starting()

    if in_u == '2':
        analyze_resturants('arcadia_0.json')

    if in_u == '3':
        gp = gmap()
        key = gp.start_key()
        x = distance(key,'arcadia_resturants.csv')
        x.distance_calc()



    print('end')


