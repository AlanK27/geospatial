from start.parse.jfiles import jfiles
from start.parse.parsing_j import json_to_csv
import pandas as pd



def analyze_resturants(name):

    x = jfiles()
    path = x.data_path()

    arcadia = x.json_load(name)

    j2c = json_to_csv()

    for result in arcadia['results']:
        plist = j2c.json_2_list_resturant(result)
        j2c.to_csv(plist, 'arcadia_resturants.csv', path)
        







