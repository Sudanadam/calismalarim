def is_leap(year):
    leap = False
if year %4 ==0:
    if year %100 ==0:
        if year %400 ==0:
            True
        else:
            False
    else:
        True
else:
     False
year = int(input())
print(is_leap(year))