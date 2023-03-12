
# Write a Python program to display a multiplication table using for loop.

num = int(input("Enter the table:"))
print("Table of {0} is below:".format(num))
for i in range(1,11):
    table = num * i
    print(num,"X",i,"=",num * i)