
# Write a Python program to check leap year.

year = int(input("Enter the year:"))

if ((year % 400 == 0) or
    (year % 100 != 0) and
    (year % 4 == 0)):
    print("{0} is the leap year.".format(year))
else:
    print("{0} is not a the leap year.".format(year))

