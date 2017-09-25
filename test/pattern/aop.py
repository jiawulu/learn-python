def aop(fun):
    print("enter aop")
    def wrapper(*args,**kwargs) :
        print("aop invoked")
        return fun(*args,**kwargs)
    return wrapper

@aop
def test() :
    print(123)

@aop
def test2(arg):
    print(arg)


test()
print(">>>>>>>>>>>>>>>")
test2(111)