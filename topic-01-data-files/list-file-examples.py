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
    # comprehension mapping and filtering
    lines = [line.strip() for line in lines if 'a' in line]
    # # traditional mapping
    # for i in range(0,len(lines)):
    #     lines[i] = lines[i].strip()
    # # traditional filtering
    # result = []
    # for i in range(0,len(lines)):
    #     if 'a' in lines[i]:
    #         result.append(lines[i])
    # print([result])
    print([lines])
    print("in context", f.closed)

print("after context", f.closed)

# t = [2,3,4,4,5,2,4,6,2,1,4,5,7,4,2,2]
# print(t)
# v = [r*2 for r in t if r > 4]  # list comprehension
# print(v)
