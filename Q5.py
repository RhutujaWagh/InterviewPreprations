
# Write a Python program to find the maximum of two numbers?

num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))

# if num1 > num2:
#     print("{0} is Max.".format(num1))
# elif num2 > num1:
#     print("{0} is Max.".format(num2))
# else:
#     print("Invalid Number.")

maximum = max(num1,num2)

print("Maximum num is {0}".format(maximum))