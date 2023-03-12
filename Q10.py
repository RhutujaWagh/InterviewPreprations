
# Write a Python program to check Armstrong’s number.

num = int(input("Enter the number:"))
sum = 0
original = num
lenth = len(str(num))
while original > 0:
    digit = original % 10
    sum += digit ** lenth
    original = original // 10

if sum == num:
    print("{0} is the armstrong number.".format(num))
else:
    print("{0} is a not a armstrong number.".format(num))