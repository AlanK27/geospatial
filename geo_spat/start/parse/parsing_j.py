import csv
import json


class json_to_csv:


    def __init__(self):
        pass
    
    def json_2_list_resturant(self, data_file):
        
        p_list = []

        try: p_list.append(data_file['formatted_address'])

        except:
            p_list.append(None)

        try: p_list.append(data_file["geometry"]["location"]['lat'])

        except:
            p_list.append(None)

        try: p_list.append(data_file["geometry"]["location"]['lng'])

        except:
            p_list.append(None)

        try: p_list.append(data_file['id'])

        except:
            p_list.append(None)

        try: p_list.append(data_file['name'])

        except:
            p_list.append(None)

        try: p_list.append(data_file['price_level'])

        except:
            p_list.append(None)

        try: p_list.append(data_file['raiting'])

        except:
            p_list.append(None)

        try: p_list.append(data_file["user_ratings_total"])

        except:
            p_list.append(None)

        try: p_list.append(data_file['types'])

        except:
            p_list.append(None)
        
        return p_list

    @staticmethod
    def resturant_header():
        
        return [
            'formatted_address,',
            'latitude',
            'longitude'
            'id',
            'name',
            'price_level',
            'rating',
            "user_ratings_total",
            'types'
        ]


    def to_csv(self, j_file, name, dir):

        with open(str(dir) + f'\\{str(name)}', 'a+') as af:
            data_parser = csv.writer(af, delimiter=',')
            if af.tell() == 0:
                data_parser.writerow(self.resturant_header())
            data_parser.writerow(j_file)
      
        return True





