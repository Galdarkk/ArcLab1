import csv
import os

table = {}

with open(os.path.join(os.getcwd(), 'parser', 'data', 'ua-list.csv')) as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='\n')
    table = {row[2].lower(): 0 for row in reader}
