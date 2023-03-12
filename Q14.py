
# Write a Python program to swap two variables.

num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
print("Before Swapping Num1 = {0},Num2 = {1}".format(num1,num2))

# # Using Temp variable
# temp = num1
# num1 = num2
# num2 = temp

# # Without Using 3rd variable
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2

# Using python function
num1,num2 = num2,num1

print("After Swapping Num1 = {0},Num2 = {1}".format(num1,num2))

