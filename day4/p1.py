with open("input.txt") as input:
    data = input.read()

def palindrome(string):
    new_string = ""
    for i in reversed(string):
        new_string += i
    if new_string == string:
        print("This word is a palindrome!")
    else:
        print("This word is not a palindrome!")

palindrome("racecar")