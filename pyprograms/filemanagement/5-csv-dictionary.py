import csv

reader = csv.DictReader(open("writeData.csv"))
for raw in reader:
    print(raw)