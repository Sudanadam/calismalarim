mylist = [1, 2, 3, 4]
mylist2 = [6, 4, 9, 1]
#print(list(map(lambda x: x + 10, mylist)))

def kucuk(x,y):
    if x < y:
        return x
    else:
        return y

print(list(map(kucuk, mylist,mylist2)))

