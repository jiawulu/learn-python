f = open('gbk', encoding='gbk');

print(f.encoding)

line = f.read()

line2 = line.encode().decode("utf-8");

print(line)

f2 = open('utf','w');
f2.write(line2)
f2.close()

print("read utf")

f2 = open('utf');
print(f2.read())
print(f2.encoding)

print(line2)