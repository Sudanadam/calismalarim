mylist = []
n = int(input())
for a in range(n):
    list1 = input().split()
    if list1[0] == "insert":
            mylist.insert(int(list1[1]), int(list1[2]))
    elif list1[0] == "print":
           print(mylist)
    elif list1[0] == "remove":
        mylist.remove(int(list1[1]))
    elif list1[0] == "append":
        for i in list1[1:]:
            mylist.append(int(i))
    elif list1[0] == "sort":
        mylist.sort()
    elif list1[0] == "pop":
        mylist.pop(-1)
    elif list1[0] == "reverse":
        mylist.reverse()

