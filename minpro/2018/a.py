import sys
import itertools

x = input()

if x[:3] == "yah":
    if x[3] == x[4:]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
