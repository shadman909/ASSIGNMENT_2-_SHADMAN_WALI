# Question 1:  Assignment Operators
x = 50
print("Initial x =", x)
x += 6
print("After then x += 6:", x)
x -= 2
print("After then x -= 2:", x)
x *= 4
print("After then x *= 4:", x)
x /= 2
print("After then x /= 2:", x)
x %= 4
print("After then x %= 4:", x)
print("\n")

# Question 3: Simple Savings Balance Calculator with Interest
balance = 1000
interest_rate = 1.05

print(" balance:", balance)

early_balance = balance
balance *= interest_rate
interest_earned = balance - early_balance
print(" Balance =", balance )
print ("interest earned ",interest_earned)
print("\n")
