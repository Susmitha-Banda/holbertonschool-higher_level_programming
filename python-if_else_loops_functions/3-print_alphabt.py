#!/usr/bin/python3
for letter in range(ord("a"), ord("z") + 1):
    current_letter = chr(letter)
    if current_letter != 'q' and current_letter != 'e':
        print("{}".format(current_letter), end="")
        