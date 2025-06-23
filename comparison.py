# 1. Check if two numbers are equal.
a = 10
b = 20
print(" Are two numbers are equal?", a == b)  # False

# 2. Compare the ages of two people and print who is older.
age1 = 25
age2 = 30
if age1 > age2:
    print(" Person 1 is older.")
elif age1 < age2:
    print(" Person 2 is older.")

# 3. Determine if a year is before or after 2000.
year = 1999
if year < 2000:
    print(" Year is before 2000.")
elif year > 2000:
    print(" Year is after 2000.")
else:
    print(" Year is exactly 2000.")

# 4. Take two numbers from the user and check which one is greater.
num1 = int(input(" Enter first number: "))
num2 = int(input("   Enter second number: "))
if num1 > num2:
    print(" First number is greater.")
elif num2 > num1:
    print("Second number is greater.")
else:
    print(" Both numbers are equal.")

# 5. Compare marks of two students to check if both got the same score.
marks1 = 45
marks2 = 85
print(" Do both students have the same marks?", marks1 == marks2)

# 6. Check if a number is not equal to zero before dividing.
dividend = 100
divisor = 0
if divisor != 0:
    result = dividend / divisor
    print("result:", result)
else:
    print("6. Cannot divide by zero!")
