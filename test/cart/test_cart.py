shopping = [["iphone",5000],["s8",4000],["nokia",100]]

print(shopping)

print(shopping[0])

salary = int(input("input your salary : "))
print(salary)
# print(type(salary))

cart = []
money = 0

while True :

    for i in range(len(shopping)) :
        print("{} {} {}".format(i,shopping[i][0], shopping[i][1]))

    index = input(">>>>> please input your index , q to exit : ")

    if "q" == index :
        break

    intdex = int(index)
    if  money + shopping[intdex][1] > salary :
        print(" >>>>>  over your salary,please select cheaper")
        continue
    else:
        print(" >>>>>> select " + shopping[intdex][0])

    money += shopping[intdex][1]
    cart.append(shopping[intdex])

print(money)
print(cart)