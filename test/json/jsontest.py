import json

list = [2,2,3,[1],(4)]

txt = json.dumps(list)
print(txt)

with open('list.txt','w+') as f:
    f.write(txt)


with open('list.txt','r') as f:
    txt = f.read()
    print(txt)
    list = json.loads(txt)
    print(list)
    print(type(list))

json.dumps(list,'test2.txt')

