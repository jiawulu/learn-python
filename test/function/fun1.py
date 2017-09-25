# print(">>>")
#
#
# def hello(arg):
#     print(arg)
#
#
# hello(123)
#
#
# def world():
#     print('world')
#
#
# world()


def withargs(*args, **kwargs):
    print(args)
    print(kwargs)


withargs(1,2,3, a=123)