thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print("--------")


print(thisdict["year"])
print("--------")


print(len(thisdict))

print("--------")
print(type(thisdict))

print("--------")
x = thisdict["model"]
print(x)
print("--------")


y = thisdict.get("year")
print(y)
print("--------")


z = thisdict.keys()
k = thisdict.values()
p = thisdict.items()
print(k)
print(z)
print(p)

print("--------")


thisdict["color"] = "white"
print(thisdict)

print("--------")


thisdict.pop("model")
print(thisdict)

print("--------")


thisdict.popitem()
print(thisdict)

print("--------")


del thisdict["brand"]
print(thisdict)

print("--------")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])

for x, y in thisdict.items():
  print(x, y)


print("--------")


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
mydict = dict(thisdict)
print(mydict)

print("--------")


myfamily = {  "child1" : {    "name" : "Emil",    "year" : 2004  },
              "child2" : {    "name" : "Tobias",    "year" : 2007  },
              "child3" : {    "name" : "Linus",    "year" : 2011  }}
