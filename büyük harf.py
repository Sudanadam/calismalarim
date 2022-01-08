import os

s = input()
def solve(s):
    return " ".join([word.capitalize() for word in s.split(" ")])
