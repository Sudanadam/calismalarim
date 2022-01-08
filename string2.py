for x in "banana":
  print(x)

txt = "The best things in life are free!"
print("free" in txt)

b = "Hello, World!"
print(b[2:5])

a = " Hello, Worldaaaaaaaaaaaaaaaaaaaaaaaaa! "
print(a.strip()) # returns "Hello, Worldaaaaaaaaaaaaaaaa!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

string = "abracadabra"
print(string[5])


string = "abracadabra"
l = list(string)
print(l)
l[5] = 'k'
string = ''.join(l)
print(string)

string = string[:5] + "yyy" + string[6:]
print (string)
