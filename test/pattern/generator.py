def fib(max):
    n,a,b = 0,0,1

    while n < max:
        #print(b)
        yield  b
        a,b = b,a+b

        n += 1

a = fib(10)

print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

print(">>>>")

b = fib(10)
for i in b :
    print(i)