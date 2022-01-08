
sub_string = input().strip()
string = input().strip()
length = len(sub_string)
A = sum(element[index:index+length] == sub_string for element in string for index,char in enumerate(element))
print(A)