import re

# Define function
def password(x):

# Check it's not a space or blank line
    if x == "\n" or x == " ":
        return "Password cannot be empty"

    # Check the password length
    if 7 <= len(x) <= 20:
        # Check for reptitive charracter occurence
        if re.search(r'(.)\1\1', x):
            return "Weak Password! Password has repeating characters more than three times."
        # Check for repetitive string occurence
        if re.search(r'(..)(.*?)\1', x):
            return "Weak Password! Password has strings repeating more than once."
        else:
            return "Strong Password!"
    else:
        return "Password length should be between 7 - 20 characters."
# Main method
def main():
    print(password(input()))
# Driver Code
if __name__ == "__main__":
    main()
