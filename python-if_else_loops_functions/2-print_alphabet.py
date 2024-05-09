#!/usr/bin/python3
ascii_code = ord('a')
alphabet = ""
for i in range(26):
    alphabet += chr(ascii_code + i)
print(alphabet)
