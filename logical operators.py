# Task 1: Check if a number
number =  int( input("check if the number  is positive and even:"))
positive_and_even = number > 0 and number % 2 == 0
print("1. Number is positive and even:", positive_and_even)


# f person is eligible to vote (age >= 18) and is a citizen

age = int (input("enter the age :"))
citizen = input("are you a citizen (yes/no:)")
print((age >= 18 and citizen == "yes/no" and "You are eligible to vote.")
     or   "You are not eligible to vote.")

# Task 3: Check if number is less than 0 or greater than 100
value = -1
value  = value < 0 or value > 100
print("3. Number is < 0 or > 100:", value)

# Task 4: Check if student passed (marks ≥ 40) and did not cheat
marks = int(input("Enter marks: "))
cheated = input("Did the student cheat? (yes/no): ")

print((marks >= 40 and cheated == "no" and "Student passed.") or "Student failed.")


# Task 5: Use `not` to reverse a boolean condition
hungry = input("are you hungry (yes/no): ")

# Reverse the condition using not
eat_food = not (hungry == "yes")

print("eat food:", eat_food)

