
# Write a Python Program to Find Vowels From a String.

strings = input("Enter the string:")
for char in strings:
    if char.lower() in 'aeiou':
        print(char,"is vowel")
    elif char.lower() in ' ':
        pass
    else:
        print(char,"is Consonant")
