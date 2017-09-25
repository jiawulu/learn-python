import datetime
import json

user_login = False

# 账户信息
# account = {
#     'admin': ['admin', 0, [], 0, 1]
# }
with open('account.json', 'r') as file:
    account = json.load(file)


def login(name, pwd):
    if account.get(name):
        return pwd == account.get(name)[0]
    return False


def login_aop(fun):
    def inner(*args, **kwargs):
        global user_login
        if not user_login:
            name = args[0]
            pwd = input("password for {} :".format(name))
            user_login = login(name, pwd)
        if user_login:
            value = fun(*args, **kwargs);
            with open('account.json', 'w') as file:
                json.dump(account, file)
            return value
        else:
            print("user login failed")

    return inner


@login_aop
def addAccount(name, pwd, amount):
    account[name] = [pwd, amount, [], 0, 0]


def calOverDraw(money, name):
    overdraw = money
    for i in account[name][2]:
        overdraw += i[0]
    return overdraw


# 使用默认参数
@login_aop
def takeoutmoney(name, money, type='takout'):
    # 判断是否可以继续消费
    overdraw = calOverDraw(money, name)
    if overdraw > account[name][1]:
        return False
    account[name][2].append((money, type, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return True


def creditPay(name, money):
    takeoutmoney(name, money, 'shopping')


@login_aop
def refund(name, money):
    account[name][3] += money


@login_aop
def transfer(name, toname, money):
    if takeoutmoney(name, money, "transfer"):
        account[toname][3] += money
        return True
    return False


def autorefound(name):
    overdraw = calOverDraw(0, name)
    if overdraw <= account[name][3]:
        account[name][2].clear()
        account[name][3] -= overdraw
        return True
    return False


def manager():
    name = input("input your admin account : ")
    pwd = input("input your admin pwd : ")
    if login(name, pwd):

        global user_login
        user_login = True

        while True:
            print("1. add account ")
            print("2. remove account ")
            print("3. forbid account ")

            type = int(input("select :"))

            if 1 == type:
                subname = input('user');
                subpwd = input('pwd')
                addAccount(subname, subpwd, 10000)
                print(account)

    else:
        print("pwd is wrong")


# manager()

# name = input("input user name : ")


#
#
# print(login(1, 1))
print(login('admin', 'admin'))
# print(login('admin', 'admin2'))
# addAccount( 'admin', 'test', 'test', 150000)
# takeoutmoney('test', 1000)
# print("take out too much")
# print(takeoutmoney('test', 1000000))
#
# creditPay('test', 20000)
# refund('test', 100)
# refund('test', 10000)
#
# print(account)
# store_dir
# print(account)
#
# {
#     name : [ pwd, amount, [消费记录], cash， type]
# }
#
# login
#
# takeoutmoney
#
# transfer
#
# refund
#
# manager
#
# log
#
# checkAccount
#
#
# creditPay
#
#
# 自动扣款
