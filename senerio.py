#  Student 1
print("\n Enter Details for Student 1 ")
name1 = input("Enter student name: ")
sub1_1 = float(input("Enter the marks for Subject 1: "))
sub1_2 = float(input("Enter  the marks for Subject 2: "))
sub1_3 = float(input("Enter the marks for Subject 3: "))

# Calculate
total1 = sub1_1 + sub1_2 + sub1_3
average1 = total1 / 3
percentage1 = (total1 / 300) * 100

if average1 >= 80:
    grade1 = "A good"

elif average1 >= 70:
    grade1 = "B average"

elif average1 >= 50:
    grade1 = "C below average"

else:
    grade1 = "F failed"


# Pass & Scholarship check
passed1 = sub1_1 >= 40 and sub1_2 >= 40 and sub1_3 >= 40
scholarship1 = average1 >= 85 and sub1_1 >= 80 and sub1_2 >= 80 and sub1_3 >= 80

# printing the out put before bonus
print("\n--- Student 1 Report (Before Bonus) ---")
print("Name:", name1)
print("Total Marks:", total1)
print("Average:", average1)
print("Percentage:", percentage1, "%")
print("Grade:", grade1)
print("Passed:", "Yes" if passed1 else "No")
print("Scholarship Eligible:", "Yes" if scholarship1 else "No")

# Add Bonus
sub1_1 += 5
sub1_2 += 5
sub1_3 += 5

# Recalculate
total1 = sub1_1 + sub1_2 + sub1_3
average1 = total1 / 3
percentage1 = (total1 / 300) * 100
#  After Bonus
print("\n--- Student 1 Report After Bonus---")
print("Update Marks:", sub1_1, sub1_2, sub1_3)
print("New Total Marks:", total1)
print("New Average:", average1)
print("New Percentage:", percentage1, "%")


# Student 2
print("\n Enter  for Student 2")
name2 = input("Enter student name: ")
sub2_1 = float(input("Enter marks for Subject 1: "))
sub2_2 = float(input("Enter marks for Subject 2: "))
sub2_3 = float(input("Enter marks for Subject 3: "))

total2 = sub2_1 + sub2_2 + sub2_3
average2 = total2 / 3
percentage2 = (total2 / 300) * 100

if average2 >= 80:
    grade2 = "A good"
elif average2 >= 70:
    grade2 = "B average"
elif average2 >= 50:
    grade2 = "C  below average"
else:
    grade2 = "F    failed"

passed2 = sub2_1 >= 40 and sub2_2 >= 40 and sub2_3 >= 40
scholarship2 = average2 >= 85 and sub2_1 >= 80 and sub2_2 >= 80 and sub2_3 >= 80


print("\n--- Student 2 Report (Before Bonus) ---")
print("Name:", name2)
print("Total Marks:", total2)
print("Average:", average2)
print("Percentage:", percentage2, "%")
print("Grade:", grade2)
print("Passed:", "Yes" if passed2 else "No")
print("Scholarship Eligible:", "Yes" if scholarship2 else "No")

# Add Bonus
sub2_1 += 5
sub2_2 += 5
sub2_3 += 5


# Recalculate
total2 = sub2_1 + sub2_2 + sub2_3
average2 = total2 / 3
percentage2 = (total2 / 300) * 100

# Output After Bonus
print("\n--- Student 2 Report (After Bonus) ---")
print("Updated Marks:", sub2_1, sub2_2, sub2_3)
print("New Total Marks:", total2)
print("New Average:", average2)
print("New Percentage:", percentage2, "%")
