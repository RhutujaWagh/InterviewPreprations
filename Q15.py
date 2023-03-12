
# Write a Python program to check if a given number is a Fibonacci number or not.

number = int(input("Enter the number which you want to print Fibonacci number:"))
feb_starts = [0,1]

while feb_starts[-1] <= number:
    feb_starts.append(feb_starts[-1] + feb_starts[-2])

if number in feb_starts:
    print(f'Yes.{number} is a Fibonacci number.')
else:
    print(f'No.{number} is not a Fibonacci number.')