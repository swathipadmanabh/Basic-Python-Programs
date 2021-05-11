# Isogram/Heterogram is word which does not have repetative letters. Ex: Python
# Palindrome is word which reads same even when read in reverse direction. Ex: Madam


def check_isogram(string):
    return len(string) == len(set(string))

# When we use set function for a string, it separates the string to different unique characters.
# So when the set string has length less than the actual length, then it means string has duplicates.

def check_palindrome(string):
    if string.lower() == string.lower()[::-1]:
# string slicer function --> [start: stop: step function (after which it will slice the string)}]
# [::-1] --> this will consider full string and -1 will reverse the string
        return "String is a palindrome"
    else:
        return "string is not a palindrome"

print(check_isogram("Python"))
print(check_palindrome("Mom"))
print(check_isogram("Sleep"))
print(check_palindrome("Travel"))
