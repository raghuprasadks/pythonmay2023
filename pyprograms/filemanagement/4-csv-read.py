import csv

with open('writeData.csv', 'rt') as f:
    data = csv.reader(f)
    for row in data:
        print(row)
