import pandas as pd
import csv

class parse_csv:


    def __init__(self):
        pass

    def get_csv_data(self, name, dir):

        files = dir + f'\\{name}'
        df = pd.read_csv(files)
        df.reset_index(inplace=True)
        # df = df.rename(columns = {'formatted_address':'longitude'})
        dffs = df[['name','latitude', 'formatted_address']]
        return dffs

    def data_2_csv(self, file_line, name, dir, header = None):

        with open(dir + f'\\{name}', 'a+') as af:
            data_parser = csv.writer(af, delimiter=',')
            if af.tell() == 0:
                data_parser.writerow(header)
            data_parser.writerow(file_line)











