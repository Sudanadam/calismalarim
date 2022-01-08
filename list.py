x = int(input())
y = int(input())
z = int(input())
n = int(input())
#list1 = list(range(0,n))
#list2 = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i + j + k != n :
                print([i,j,k])
#                list2.append([x,y,z])
#                print("[{}, {}, {}]".format(x,y,z))
            else:
                None
#print(list2)