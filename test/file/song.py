f = open('song.txt','r+');

# read one line
line = f.readline()

print(line.center(100,'-'))

# read all lines
other = f.read()

print(other)


f.close()


with open('song.txt') as f :
    print(f.read())
# print(f.readline())
# # print(f.readlines(4))
# print(f.writable())

# f.write("hello world \n")
