# example file I/O
from pprint import pprint
import csv

# read CSV with header
with open("../data/people.csv","r") as f:
    reader = csv.DictReader(f)
    i = 0
    rows = []
    for row in reader:
        i = i + 1
        rows.append(row)
#        if i > 10:
#            break
#        print(row)
    print(len(rows), rows[0:4])