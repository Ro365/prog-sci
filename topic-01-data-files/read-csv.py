# example file I/O
from pprint import pprint
import csv

# with open("example-foods-2.csv","r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# with open("example-foods-2.csv","r") as f:
#     reader = csv.DictReader(f,fieldnames=["name","quantity","color","circular","recipe"])
#     for row in reader:
#         row["quantity"] = int(row["quantity"])
#         print(row)

# read CSV with header
with open("example-foods-3.csv","r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["qty"] = int(row["qty"])
        print(row)
