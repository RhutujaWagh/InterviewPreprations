
# Write a Python program to check prime numbers.

num = int(input("Enter the number:"))
if num > 1:
    for i in range(2,num//2+1):
        if num % i == 0:
            print(("{0} is not a prime number.".format(num)))
            break
    else:
        print(("{0} is a prime number.".format(num)))
else:
    print(("{0} is a invalid number.".format(num)))
