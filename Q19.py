
# Write a Python program to print all prime numbers in an interval.

starting_Num = int(input('Enter the starting range: '))
ending_Num = int(input('Enter the ending range: '))

print("Prime numbers between", starting_Num, "and", ending_Num, "are:")

for num in range(starting_Num, ending_Num + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
