# LAB-7: Functions

# Even/odd checker
def even_checker(a):
    if a % 2 == 0:
        print("Even!!")
    else:
        print("Odd!!")
even_checker(5)

# Fibonacci sequence up to a limit
def fibonacci(limit):
    n1, n2 = 0, 1
    print(n1, end=" ")
    while n1 + n2 <= limit:
        print(n1+n2, end=" ")
        n1, n2 = n2, n1+n2
fibonacci(10)
print()

# FooMoo function
def foo_moo(n):
    result = ""
    if n % 2 == 0:
        result += "Foo"
    if n % 3 == 0:
        result += "Moo"
    return result if result else "Boo"
print(foo_moo(6))

# Count uppercase and lowercase
def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    print("No. of Uppercase characters :", upper)
    print("No. of Lowercase Characters :", lower)
count_case('The quick Sand Man')

# Calculate tax based on age, salary, job
def calculate_tax(age, salary, job):
    if age > 18 and job != "president" and salary >= 10000:
        if salary <= 20000:
            return salary * 0.05
        else:
            return salary * 0.10
    return 0
a = int(input())
b = int(input())
c = input().lower()
print(calculate_tax(a, b, c))

# Convert days to years, months, days
def convert_days(days):
    years = days // 365
    months = (days % 365) // 30
    days_left = (days % 365) % 30
    print(f"{years} years, {months} months and {days_left} days")
num = int(input())
convert_days(num)

# Palindrome pattern
def show_palindrome(n):
    s = "".join(str(i) for i in range(1, n)) + "".join(str(i) for i in range(n, 0, -1))
    return s
print(show_palindrome(5))

# Palindrome triangle
def print_palindrome_triangle(height):
    for k in range(1, height+1):
        print("  " * (height - k), end="")
        print(" ".join(str(i) for i in range(1, k)) + " " + " ".join(str(i) for i in range(k, 0, -1)))
print_palindrome_triangle(5)

# Area and circumference generator
import math
def area_circumference_generator(radius):
    area = math.pi * radius**2
    circ = 2 * math.pi * radius
    return (area, circ)
c = area_circumference_generator(1)
print(c)
print(f"Area of the circle is {c[0]} and circumference is {c[1]}")

# Dictionary of squares in a range
def make_square(range_tuple):
    start, end = range_tuple
    return {i: i**2 for i in range(start, end+1)}
print(make_square((1, 3)))

# Remove duplicates from tuple
def rem_duplicate(t):
    return tuple(dict.fromkeys(t))
print(rem_duplicate((1,1,1,2,3,4,5,6,6,6,6,4,0,0,0)))

# Remove elements that appear more than twice
def remove_excess(lst):
    result = []
    removed = 0
    for x in lst:
        if result.count(x) < 2:
            result.append(x)
        else:
            removed += 1
    print("Removed:", removed)
    return result
print(remove_excess([1, 2, 3, 3, 3, 3, 4, 5, 8, 8]))

# Simple calculator
def simple_calc(op, a, b):
    ops = {"+": a+b, "-": a-b, "*": a*b, "/": a/b}
    return ops[op]
op = input().strip('"')
n1 = float(input())
n2 = float(input())
print(simple_calc(op, n1, n2))

# Split string by positions
def split_string(s, step):
    first = s[0]
    rest = ""
    for i in range(1, len(s)):
        if i % step == 0:
            rest += s[i]
        else:
            first += s[i]
    return first + rest
sentence = input().strip('"')
pos = int(input())
print(split_string(sentence, pos))

# Delivery cost with default location
def delivery_cost(items, location="Dhanmondi"):
    prices = {"Rice": 105, "Potato": 20, "Chicken": 250, "Beef": 510, "Oil": 85}
    total = sum(prices[item] for item in items)
    delivery_fee = 30 if location == "Dhanmondi" else 70
    return total + delivery_fee
order = input().strip('[""]').split('", "')
print(delivery_cost(order, "Mohakhali"))

# Note counter
def count_notes(amount):
    notes = [500, 100, 50, 20, 10, 5, 2, 1]
    for note in notes:
        if amount // note > 0:
            print(f"{note} Taka: {amount // note} note(s)")
            amount %= note
count_notes(1234)

# Remove odd numbers
def remove_odd(lst):
    return [x for x in lst if x % 2 == 0]
print(remove_odd([21, 33, 44, 66, 11, 1, 88, 45, 10, 9]))

# Sum of numbers divisible by c or d (but not both)
def sum_divisible(a, b, c, d):
    total = 0
    for i in range(a, b):
        if (i % c == 0 or i % d == 0) and not (i % c == 0 and i % d == 0):
            total += i
    return total
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(sum_divisible(a, b, c, d))

# Check for letters a-j in string
def check_letters(s):
    s_lower = s.lower()
    for i in range(97, 107):
        if chr(i) not in s_lower:
            return 6
    return 5
s = input().strip('"')
res = check_letters(s)
print("PSG will win the Champions League this season\n" * res)

# Individual bonus calculation
def individual_bonus(name, salary, goals, percent):
    bonus = goals * (percent/100 * salary)
    if 20 <= goals <= 30:
        bonus += 5000
    elif goals > 30:
        bonus += 10000
    print(f"{name} earned a bonus of {int(bonus)} Taka for {goals} goals.")

# Variable arguments for multiple players
def cal_bonus(*args):
    for i in range(0, len(args), 4):
        individual_bonus(args[i], args[i+1], args[i+2], args[i+3])
cal_bonus("Neymar", 1200000, 35, 5, 'Jamal', 700000, 19, 8, 'Luis', 80000, 25, 10)
