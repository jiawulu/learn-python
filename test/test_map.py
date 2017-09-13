map = {'a':1,'b':2}
map['c'] = 3

print(map)

map['c'] = 4

for i in map.keys() :
    print(i)

for i in map.values() :
    print(i)

# for i,j in map:
#     print(i,j)

for i in map.items() :
    print(i)