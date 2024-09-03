# example file I/O

# f = open("example-foods.csv","r")
# # print([f])
# # print(f.name, f.mode)
# lines = f.readlines()
# print([lines])
# ....
# f.close()

with open("example-foods.csv","r") as f:
    lines = f.readlines()
    print([lines])
    lines = [line.strip() for line in lines]
    print([lines])
    print("in context", f.closed)

print("after context", f.closed)

t = [2,3,4]
print(t)
v = [r*2 for r in t]
print(v)