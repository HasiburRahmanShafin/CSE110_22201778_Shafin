
---

## lab1.py (LAB-1)
```python
# LAB-1: Basic Input/Output and Arithmetic

# Task: Print "hello world"
print('hello world')

# Task: Print the sum of 54 and 56
print(54+56)

# Task: Assign and print variables
season = 'Fall'
year = 2022
print(season)
print(year)

# Task: Take user input and print it
name1 = input("Enter your name :")
print("Your name is", name1)

# Task: Compute power (m^n)
m = int(input("Enter 1st number="))
n = int(input("Enter 2nd number="))
print(str(m) + "^" + str(n) + ":", m**n)

# Task: Find the largest multiple of 4 ≤ weight
x = int(input("Enter the weight :"))
print(4*(x//4))

# Task: Evaluate a^c + b*a - d/3 (integer result)
a = int(input("Enter 1st number ="))
b = int(input("Enter 2nd number ="))
c = int(input("Enter 3rd number ="))
d = float(input("Enter 4th number ="))
print(int(a**c + b*a - d/3))

# Task: Divide chocolates among 3 friends
a = int(input("Number of chocolates"))
print("Each friend will receive", a//3, "chocolates")
print("The number of remaining chocolates is", a%3)

# Task: Concatenate two strings (M and N)
m = input("M=")
n = input("N=")
print(n+m)

# Task: Print first character of a line
a = input("Enter a line:")
print(a[0])

# Task: Check if a number is even
x = int(input("Enter a number="))
if x % 2 == 0:
    print("True")
else:
    print("False")
