import re


def password(x):

    if x == "\n" or x == " ":
        return "Password cannot be empty"

    
    if 7 <= len(x) <= 20:
        # Check for reptitive charracter occurence
        if re.search(r'(.)\1\1', x):
            return "Weak Password! Password has repeating characters more than three times."
        # Check for repetitive string occurence
        if re.search(r'(..)(.*?)\1\1', x):
            return "Weak Password! Password has strings repeating more than twice."
        else:
            return "Strong Password!"
    else:
        return "Password length should be between 7 - 20 characters."


def main():
    print(password(input()))
