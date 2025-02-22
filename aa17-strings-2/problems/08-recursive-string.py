# Create a function that reverses the string using recursion.

# Write your function here.
def recursive_string(string):
    # recursively reverses a string
    if len(string) == 0:
        return string
    else:
        return recursive_string(string[1:]) + string[0]


print(recursive_string("civic")) # civic
print(recursive_string("refer")) # refer
print(recursive_string("string")) # gnirts
print(recursive_string("avocado")) # odacova
print(recursive_string("application")) # noitacilppa
