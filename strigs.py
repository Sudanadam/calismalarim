a = "this is a string"
a = a.split(" ") # a is converted to a list of strings.
print(a)
print("-----------")
a = "-".join(a)
print(a)

print("-----------")
line = str(input())
def split_and_join(line):
    data = line.split(" ")
    return "-".join(data)

print(split_and_join(line))
print("-----------")




