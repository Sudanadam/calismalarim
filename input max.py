n = int(input("gir : "))
arr = list(map(int, input().split()))
print(arr)
print(max([x for x in arr if x != max(arr)]))
