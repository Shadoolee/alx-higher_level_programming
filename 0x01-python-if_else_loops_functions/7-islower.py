#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')

character = 'a'
result = islower(character)

if result:
    print(f"{character} is lowercase")
else:
    print(f"{character} is not lowercase")
