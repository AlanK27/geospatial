import os
import pandas as pd
from start.parse.jfiles import jfiles
from start.places.places import places
from start.analysis.analysis import analyze_resturants
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
        1: 'initate',
        2: 'analyze_resturants'

    }
    sf = pd.Series(lis)
    print(sf)
    in_u = input('what is the input')

    if in_u == '1':
        x = initiate()
        x.starting()

    if in_u == '2':
        analyze_resturants('arcadia_0.json')




    print('end')


