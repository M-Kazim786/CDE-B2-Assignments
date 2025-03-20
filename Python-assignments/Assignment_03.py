#/........................Strings Assignment....................../


# 1. Write a program that accepts a string from user. Your program should count and display number of vowels in that string.

str=input("Enter a string: ")
vowels='aeiouAeiou'
count=0

for char in str:
    if char in vowels:
        count+=1

print(f'Number of count in string "{str}" is: {count}')


# 2. Write a program that reads a string from keyboard and display:

    #  The number of uppercase letters in the string
    #  The number of lowercase letters in the string
    #  The number of digits in the string
    #  The number of whitespace characters in the string

str=input('Enter a string: ')
upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

for char in str:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
print("Digits:", digit_count)
print("Whitespace characters:", space_count)

# 3. Write a Python program that accepts a string from user. Your program should create and display a new string where the first and last characters have been exchanged.
#    For example if the user enters the string 'HELLO' then new string would be 'OELLH'

str=input('Enter a string: ')
if len(str) > 1:
    newStr= str[-1] + str[1:-1] + str[0]
else:
    newStr=str

print('New String: ',newStr)


# 4. Write a Python program that accepts a string from user. Your program should create a new string in reverse of first string and display it.
#    For example if the user enters the string 'EXAM' then new string would be 'MAXE

string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed string:", reversed_string)


# 5. Write a Python program that accepts a string from user. Your program should create a new string by shifting one position to left.
#    For example if the user enters the string 'examination 2021' then new string would be 'xamination 2021e'

string = input("Enter a string: ")

if len(string) > 1:
    shifted_string = string[1:] + string[0]
else:
    shifted_string = string

print("New string:", shifted_string)


# 6.  Write a program that asks the user to input his name and print its initials. Assuming that the user always types first name, middle name, and last name and does not include any unnecessary spaces.
#     For example, if the user enters Ajay Kumar Garg, the program should display A. K. G.
#     Note: Don't use the split() method.

name = input("Enter your full name: ")
initials = ""

for i in range(len(name)):
    if i == 0 or name[i-1] == " ":
        initials += name[i].upper() + ". "

print(initials)


# 7. A palindrome is a string that reads the same backward as forward. For example, the words dad, madam, and radar are all palindromes. Write a program that determines whether the string is a palindrome.
# Note: Do not use the reverse() method.

string = input("Enter a string: ").lower()
is_palindrome = True

for i in range(len(string) // 2):
    if string[i] != string[-(i+1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")


# 8. Write a program that displays the following output:

# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT

word = "SHIFT"

for i in range(len(word) + 1):
    print(word)
    word = word[1:] + word[0]


# 9. Write a program in Python that accepts a string to set up a password. Your entered password must meet the following requirements:

# The password must be at least eight characters long.
# It must contain at least one uppercase letter.
# It must contain at least one lowercase letter.
# It must contain at least one numeric digit.
# Your program should validate these conditions.

password = input("Enter your password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long.")
else:
    has_upper = has_lower = has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    if not has_upper:
        print("Password must contain at least one uppercase letter.")
    elif not has_lower:
        print("Password must contain at least one lowercase letter.")
    elif not has_digit:
        print("Password must contain at least one numeric digit.")
    else:
        print("Password is valid.")
