#******************** Conditional Statements*********************/


# 1. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

salary=int(input('Enter Your salary: '))
service=int(input('Enter your years of service:'))

if(service > 5):
    net_bonus = salary * (5/100)
    print(net_bonus)
else:
    print('Your years of service is less than 5 years')

# 2. Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible.

age=int(input('Enter your age: '))

if(age > 17):
    print('You are eligible to vote.')
else:
    print("You are NOT eligible to vote.")

# 3. Write a program to check whether a number entered by user is even or odd.

num=int(input('Enter any number: '))

if(num % 2==0):
    print('The number is even.')
else:
    print('The number is odd.')

# 4. Write a program to check whether a number is divisible by 7 or not. Show Answer

divisible=int(input('Enter a number: '))

if(divisible % 7==0):
    divisible/=7
    print(f'Yes it is divisible by 7. The Answer is {divisible}')
else:
    print('No, the number is not divisible by 7')

# 5. Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".

prompt=int(input('Enter a number: '))

if(prompt % 5==0):
    print('Hello')
else:
    print('Bye')

# 6. Write a program to display the last digit of a number.

digit= int(input("Enter a number: "))
last_digit = digit % 10
print("The last digit is:", last_digit)

# 7. Take values of length and breadth of a rectangle from user and print if it is square or rectangle.

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

if length == breadth:
    print("It is a Square.")
else:
    print("It is a Rectangle.")

# 8. Take two int values from user and print greatest among them.

value1=int(input('Enter first value: '))
value2=int(input('Enter second value: '))

if value1 > value2:
    print('First value is greater')
else:
    print('Second value is greater')

# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.

cost=100
quantity=int(input('Enter quantity: '))

total_cost= cost * quantity
print('Total cost is: ',total_cost)

if total_cost > 1000:
    discount = total_cost*(10/100)
    total_cost-=discount
    print('After 10 % Discount: ',total_cost)
else:
    print('No discount!')

# 10. A school has following rules for grading system:
#     a. Below 25 - F
#     b. 25 to 45 - E
#     c. 45 to 50 - D
#     d. 50 to 60 - C
#     e. 60 to 80 - B
#     f. Above 80 - A
#     Ask user to enter marks and print the corresponding grade.

marks=int(input('Enter your marks: '))

if marks < 25:
    print('F')
elif marks>=25 and marks<=45:
    print('E')
elif marks>=45 and marks<=50:
    print('D')
elif marks>=50 and marks<=60:
    print('C')
elif marks>=60 and marks<=80:
    print('B')
elif marks>80:
    print('A')

# 11. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#     Take following input from user
#     Number of classes held
#     Number of classes attended.
#     And print
#     percentage of class attended
#     Is student is allowed to sit in exam or not.

classes_held=int(input('Number of classes held: '))
classes_attended=int(input('Number of classes attended: '))

attendance=(classes_attended/classes_held) * 100
print(f"Attendance Percentage: {attendance:.1f}%")

if attendance >=75:
    print('You are allowed to sit in exam.')
else:
    print('You are NOT allowed to sit in exam.')

# 12. Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

classes_held=int(input('Number of classes held: '))
classes_attended=int(input('Number of classes attended: '))
med_cause=input('Do you have any medical cause. (Y/N): ').upper()

attendance=(classes_attended/classes_held) * 100
print(f"Attendance Percentage: {attendance:.1f}%")

if attendance >=75 or med_cause=='Y':
    print('You are allowed to sit in exam.')
else:
    print('You are NOT allowed to sit in exam.')

# 13. Write a program to check if a year is leap year or not. If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")

# 14. Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.

#     if employee is female, then she will work only in urban areas.
#     if employee is a male and age is in between 20 to 40 then he may work in anywhere
#     if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#     And any other input of age should print "ERROR"

age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
marital_status = input("Enter marital status (Y/N): ").upper()

if gender == 'F':
    print("She will work only in urban areas.")
elif gender == 'M':
    if 20 <= age <= 40:
        print("He may work anywhere.")
    elif 40 < age <= 60:
        print("He will work only in urban areas.")
    else:
        print("ERROR")
else:
    print("Invalid gender input!")

# 15. Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price upto 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750

units = int(input("Enter the number of units consumed: "))

bill = 0

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + ((units - 300) * 10)

print("Total electricity bill amount: Rs.", bill)

# 16. Take input of age of 3 people by user and determine oldest and youngest among them.

user1=int(input("Enter first user's age: "))
user2=int(input("Enter second user's age: "))
user3=int(input("Enter third user's age: "))

if user1 > user2 and user1 > user3:
    oldest = user1
elif user2 > user1 and user2 > user3:
    oldest = user2
else:
    oldest = user3

if user1 < user2 and user1 < user3:
    youngest = user1
elif user2 < user1 and user2 < user3:
    youngest = user2
else:
    youngest = user3

print("The oldest user is:", oldest)
print("The youngest user is:", youngest)
