import copy

names = [1,2,3,[1,2,3]]
print(names)

print(names[1:2])

print(names[1])

print(names[::2])

print(copy.deepcopy(names))

print(names.pop(2))

print(names)

names.append("123")

names.insert(1,"1234")

print(names)

print(names[-1])

for n in names :
    print(n)

for i in range(0,20,2) :
    print(i)

print(123)