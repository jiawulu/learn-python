import shelve

store = shelve.open('shelve')

store["list"] = [1,2,3,4,5]
store.close()

store2 = shelve.open('shelve')
print(store2.get("list"))
store2.close()