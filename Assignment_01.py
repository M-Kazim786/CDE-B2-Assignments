# 1. Print Your Name with your Father name and Date of birth using suitable escape sequence charactor.
print("Muhammad Kazim\nFather's Name: Muhammad Naveed\nDate of Birth: 06-12-2004\n")

# 2. Write your small bio using variables and print it using print function.

name = "Muhammad Kazim"
father_name = "Muhammad Naveed"
dob = "01-01-2000"
city = "Karachi"
hobby = "Coding"

print(f"My name is {name}. My father's name is {father_name}. I was born on {dob}. I live in {city} and my hobby is {hobby}.\n")

# 3. Write a program in which use all the operators we can use in Python

# Arithmetic Operators
a, b = 10, 5

# Arithmetic Operators
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# Comparison Operators
print(a == b)
print(a != b)
print(a > b)
print(a < b)

# Logical Operators
x, y = True, False
print(x and y)
print(x or y)
print(not x)

# Bitwise Operators
print(a & b)
print(a | b)
print(a << 1)
print(a >> 1)

# Assignment Operators
c = 10
c += 5
print(c)
print('\n')

#  4. Completes the following steps of small task:
# Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
# Mention Variable of Total Marks and assign 300 to it
# Calculate Percentage

english = 85
islamiat = 90
maths = 95

total_marks = 300

obtained_marks = english + islamiat + maths
percentage = (obtained_marks / total_marks) * 100

print("Obtained Marks:", obtained_marks)
print("Percentage:", percentage, "%\n")
