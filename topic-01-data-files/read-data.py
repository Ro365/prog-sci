# example file I/O
from pprint import pprint


with open("example-foods.csv","r") as f:
    lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    print(lines)
    items = [line.split(",") for line in lines]
    pprint(items)
    print("fruits")
    for item in items:
        item[1] = int(item[1])
        item[3] = item[3] == "yes"
        print(item)
    print("fruits")
    for item in items:
        print("name:",item[0], "  quantity:",item[1])
