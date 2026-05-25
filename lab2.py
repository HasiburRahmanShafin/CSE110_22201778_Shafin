# LAB-2: Conditionals and Basic Calculations

import math

# Task: Sum, product, difference
a = int(input("1st number : "))
b = int(input("2nd number : "))
sum_ab = a+b
pro = a*b
dif = a-b
print("Sum=", sum_ab)
print("Product=", pro)
print("Difference=", dif)

# Task: Area and circumference of a circle
r = float(input("Radius of the circle = "))
area = math.pi * math.pow(r, 2)
circ = 2 * math.pi * r
print("Area is", area)
print("Circumference is", circ)

# Task: Compare two numbers
a = int(input("1st number : "))
b = int(input("2nd number : "))
if a > b:
    print("First is greater")
elif a < b:
    print("Second is greater")
else:
    print("The number is equal")

# Task: Absolute difference
a = int(input("1st number : "))
b = int(input("2nd number : "))
if a >= b:
    print(a-b)
else:
    print(b-a)

# Task: Odd or even
n = int(input("Enter number : "))
if n % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Task: Multiple of 2 or 5
num = int(input("Enter number : "))
if num % 2 == 0 or num % 5 == 0:
    print(num)
else:
    print("Not a multiple of 2 OR 5")

# Task: Multiple of both 2 and 5, or just one
n = int(input("Enter number : "))
if n % 2 == 0 and n % 5 == 0:
    print("Multiple of 2 and 5 both")
elif n % 2 == 0 or n % 5 == 0:
    print(n)
else:
    print("Not a multiple we want")

# Task: Multiple of both 2 and 5
n = int(input("Enter number : "))
if n % 2 == 0 and n % 5 == 0:
    print(n)
else:
    print("Not a multiple of 2 and 5 both")

# Task: Convert seconds to hours, minutes, seconds
s = int(input("Number of seconds : "))
hour = s // 3600
minute = (s % 3600) // 60
sec = (s % 3600) % 60
print("Hour:", hour, "Minutes:", minute, "Seconds:", sec)

# Task: Weekly salary calculation
t = int(input("Total hour : "))
if 0 < t <= 40:
    print(t*200)
elif 40 < t < 168:
    print(8000 + (t-40)*300)
elif t > 168:
    print("Impossible to work more than 168 hours weekly")
elif t < 0:
    print("Hour cannot be negative")

# Task: Compute L based on S
S = int(input("Enter a number : "))
if S < 100:
    L = 3000 - 125 * S**2
    print(L)
else:
    L = 12000 / (4 + (S**2)/14900)
    print(L)

# Task: Meal time message
h = int(input("Enter the hour : "))
if 4 <= h <= 6:
    print("Breakfast")
elif 12 <= h <= 13:
    print("Lunch")
elif 16 <= h <= 17:
    print("Snacks")
elif 19 <= h <= 20:
    print("Dinner")
elif 0 <= h < 24:
    print("Patience is a virtue")
else:
    print("Wrong time")

# Task: Grade from marks
x = int(input("Enter your mark :"))
if 90 <= x <= 100:
    print("A")
elif 80 <= x <= 89:
    print("B")
elif 70 <= x <= 79:
    print("C")
elif 60 <= x <= 69:
    print("D")
elif 50 <= x <= 59:
    print("E")
else:
    print("F")

# Task: Car speed check (km/h)
d = int(input("Enter the distance :"))
t = int(input("Enter the time :"))
v = (d/t)*3.6
print(v, "km/h")
if v < 60:
    print("Too slow. Needs more changes.")
elif 60 <= v <= 90:
    print("Velocity is okay. The car is ready!")
else:
    print("Too fast. Only a few changes should suffice.")

# Same as above but with explicit conversion
d = int(input("Enter the distance :"))
t = int(input("Enter the time :"))
v = (d/1000) / (t/3600)
print(v, "km/h")
if v < 60:
    print("Too slow. Needs more changes.")
elif 60 <= v <= 90:
    print("Velocity is okay. The car is ready!")
else:
    print("Too fast. Only a few changes should suffice.")

# Task: Waiver eligibility based on CGPA and credits
cg = float(input("Enter your CGPA :"))
c = int(input("Completed credit :"))
if c >= 30:
    if 3.80 <= cg <= 3.89:
        print("The student is eligible for a waiver of 25 percent.")
    elif 3.90 <= cg <= 3.94:
        print("The student is eligible for a waiver of 50 percent.")
    elif 3.95 <= cg <= 3.99:
        print("The student is eligible for a waiver of 75 percent.")
    elif cg == 4.00:
        print("The student is eligible for a waiver of 100 percent.")
    else:
        print("The student is not eligible for a waiver")
else:
    print("The student is not eligible for a waiver")

# Tracing code blocks (original logic preserved)
p, q, r = 5, 6, 9
sum_val = 0
if p < 12:
    print(r + 2)
else:
    print(r + p)
if q > 20:
    print(r + 19)
elif q <= 6:
    print(q + 3)
else:
    print(p + q + r)
if r > 15:
    print(r)
elif r == 0:
    print(p + q)
else:
    print(p)
if sum_val != 0:
    print(3)
else:
    print(sum_val + 32)
if p > 0 and r < 10:
    print(p + r)
else:
    print(p - r)

# More boolean tracing
var1 = 4 > 3 - 1
var2 = var1 and False
var3 = True
var4 = False
var5 = True
var6 = var3 and False
result1 = (var1 or var2) and (8 * 10 > 45)
result2 = (var1 or var2) and (result1 and False)
result3 = (var1 and result1) or result2
result4 = (var1 or var2) or ((var3 and var1) and False)
result5 = (var1 and var2) and (result3 or var1)
result6 = ((var3 or var2) and not(result5)) or True
result7 = (var4 and result1) and ((result1 and False) or True)
result8 = ((var1 and result3) and (var5 or var6)) and True
result9 = ((result2 and var2) or (result7 and var1)) and False
result10 = not(var1 and True)
print(result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, sep='\n')

# Another boolean tracing block
var1 = ((not True) or True) and False
var2 = var1 and False
var3 = True and not False
var4 = False
var5 = True
var6 = var3 and False
result1 = (var1 and var2) and (40 % 3) > 45 or (var5 and var6)
result2 = (var1 or var2) or (result1 and False)
result3 = (var1 and result1) or result2 or var5
result4 = (var1 or var2) or ((var3 and var1) and False)
result5 = (var1 and var2) and (result3 or var1)
result6 = ((var3 or (not var2)) and (result5)) or True
result7 = (var4 and result1) and ((result1 and False) or True)
result8 = ((var1 and result3) and ((not var5) or var6)) and True
result9 = ((result2 and var2) or ((not result7) and var1)) and not False
result10 = not(var1 and True)
print(result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, sep='\n')

# Third boolean tracing block
var1 = (not False or False) and True
var2 = var1 and True
var3 = False and not True
var4 = True
var5 = False
var6 = var3 and True
result1 = (var1 and var2) and (40 % 3 > 45) or (var5 and var6)
result2 = (var1 or var2) or (result1 and False)
result3 = (var1 and result1) or result2 or var5
result4 = (var1 or var2) or ((var3 and var1) and False)
result5 = (var1 and var2) and (result3 or var1)
result6 = ((var3 or not var2) and (result5)) or True
result7 = (var4 and result1) and ((result1 and False) or True)
result8 = ((var1 and result3) and (not var5 or var6)) and True
result9 = ((result2 and var2) or (not result7 and var1)) and not False
result10 = not (var1 and True)
print(result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, sep='\n')

# Task: Print number if NOT multiple of 2 AND NOT multiple of 5
num = int(input("Enter number : "))
if num % 2 != 0 and num % 5 != 0:
    print(num)
else:
    print("no")

# Task: Print number if NOT multiple of 2 OR NOT multiple of 5
num = int(input("Enter number : "))
if num % 2 != 0 or num % 5 != 0:
    print(num)
else:
    print("No")

# Task: Apply discount based on total purchase
c = int(input("10X10 sized canvas : "))
p = int(input("25 ml paint tube : "))
t = c*120 + p*75
print("Previous total:", t)
if 300 <= t <= 499:
    t -= 10
elif 500 <= t <= 749:
    t -= 20
elif 750 <= t <= 999:
    t -= 50
elif t >= 1000:
    t -= 150
print("New total after discount:", t)

# Task: Convert Fahrenheit to Celsius and print season
fahrenheit = int(input("Enter temperature: "))
celsius = int((fahrenheit-32)*0.56)
print(celsius, "degrees C")
if celsius < 20:
    print("Winter")
elif 20 <= celsius <= 25:
    print("Autumn")
elif 25 < celsius < 30:
    print("Spring")
else:
    print("Summer")
