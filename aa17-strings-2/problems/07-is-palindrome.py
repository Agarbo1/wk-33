# Create a function that returns whether or not the string is a Palindrome.

# Write your function here.
def is_palindrome(string):
    reverse_string = ""
    for i in range(len(string)-1, -1, -1):
        reverse_string += string[i]
    return reverse_string == string

print(is_palindrome("kayak")) # True
print(is_palindrome("app"))  # False
print(is_palindrome("racecar")) # True
print(is_palindrome("valid")) # False
