
# Write a Python program to calculate the area of a triangle.

a = int(input("Enter the first side:"))
b = int(input("Enter the second side:"))
c = int(input("Enter the third side:"))

# calculate the perimeter
p = a+b+c;

# calulate the semi_perimeter
s = p/2

# calculate the area_of_tringle
area = (s*(s-a)*(s-b)*(s-c))**0.5

print("Perimeter of tringle:",p)
print("Semi_Perimeter of tringle:",s)
print("Area of tringle:",area)
