# Create a function that takes two strings as arguments and return either `True`
# or `False` depending on whether the total number of characters in the first
# string is equal to the total number of characters in the second string.

# Write your function, here.
def compare(a, b):
    return len(a) == len(b)

print(compare("AB", "CD"))              #> True
print(compare("ABC", "DE"))             #> False
print(compare("hello", "App Academy"))  #> False
