__author__ = 'Alessandro'

import Dataset.MapOutCome
from Dataset.MapOutCome import *

#https://docs.python.org/2/library/csv.html#csv-fmt-params

# moc = MapOutCome('Fiori.csv')
# print('File path: ', moc.get_path_file())
# moc.run()
#
# print(moc.get_map())

import csv

with open('Fiori.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(row)

