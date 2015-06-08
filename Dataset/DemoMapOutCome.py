__author__ = 'Alessandro'

import Dataset.MapOutCome
from Dataset.MapOutCome import *



moc = MapOutCome('Fiori.csv')
print('File path: ', moc.get_path_file())
moc.run()

print(moc.get_map())
