# LAB-3: Loops (while, for) and Patterns

# a) Print decreasing multiples of 6
a = 24
print("a)", end="")
while a >= -6:
    if a == -6:
        print(a)
    else:
        print(a, end=",")
    a -= 6

# b) Print increments of 5 from -10 to 20
b = -10
print("b)", end="")
while b <= 20:
    if b == 20:
        print(b)
    else:
        print(b, end=",")
    b += 5

# c) Print multiples of 9 from 18 to 63
c = 18
print("c)", end="")
while c <= 63:
    if c == 63:
        print(c)
    else:
        print(c, end=",")
    c += 9

# d) Alternating signs for multiples of 9
d = 18
print("d)", end="")
while d <= 63:
    if d % 2 == 0:
        print(d, end=",")
    elif d == 63:
        print(d*(-1))
    else:
        print(d*(-1), end=",")
    d += 9

# Task: Print favourite car N times
car = input("Favourite car : ")
num = int(input("Enter number : "))
for i in range(num):
    print(car)

# Task: Sum of numbers divisible by both 7 and 9 up to 600
sum_val = 0
for i in range(601):
    if i % 7 == 0 and i % 9 == 0:
        sum_val += i
print(sum_val)

# Task: Sum of numbers divisible by 7 or 9 (excluding double count)
sum_val = 0
for i in range(601):
    if i % 7 == 0 or i % 9 == 0:
        sum_val += i
    if i % 7 == 0 and i % 9 == 0:
        sum_val -= i
print(sum_val)

# Task: Print odd numbers from 11 to 50 using while
count = 10
while count <= 50:
    if count % 2 != 0:
        print(count, end=" ")
    count += 1
print()

# Task: Print last odd number from 11 to 50 using for
for i in range(11, 50, 2):
    last = i
print(last, end=" ")
print()

# Task: Sum of squares with alternating signs
n = int(input())
sum_val = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum_val -= i**2
    else:
        sum_val += i**2
print(sum_val)

# Task: Average of odd numbers among 10 inputs
sum_odd = 0
count_odd = 0
for i in range(10):
    n = int(input("Enter number : "))
    if n % 2 != 0:
        sum_odd += n
        count_odd += 1
print("The total of the odd numbers is", sum_odd, "and their average is", sum_odd/count_odd)

# Task: Sum of multiples of 7 up to N (for loop)
N = int(input("Enter N : "))
sum_val = 0
for i in range(N+1):
    if i % 7 == 0:
        sum_val += i
print(sum_val)

# Same using while loop
N = int(input("Enter N : "))
sum_val = 0
i = 0
while i < N+1:
    if i % 7 == 0:
        sum_val += i
    i += 1
print(sum_val)

# Task: Cumulative sum of 5 numbers
sum_val = 0
for i in range(5):
    n = int(input("Enter number : "))
    sum_val += n
    print(sum_val)

# Task: Print digits of a number in reverse
n = int(input("Enter number : "))
for i in range(n):
    res = n % 10
    print(res, end=",")
    n = n // 10
    if n == 0:
        break
print()

# Task: Count number of digits
n = int(input("Enter number : "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print(count)

# Task: Print digits in forward order
n = int(input("Enter number : "))
m = n
count = 0
while n > 0:
    n = n // 10
    count += 1
pow10 = count - 1
for j in range(count):
    res = m // (10**pow10)
    print(res, end=",")
    m = m % (10**pow10)
    pow10 -= 1
print()

# Task: Find all divisors
n = int(input("Enter a number : "))
div_count = 0
for i in range(1, n+1):
    if n % i == 0:
        print(i)
        div_count += 1
print(f"Total {div_count} divisors.")

# Task: Perfect number check
n = int(input("Enter a number : "))
sum_div = 0
for i in range(1, n):
    if n % i == 0:
        sum_div += i
if sum_div == n:
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")

# Task: Prime number check
n = int(input("Enter a number : "))
div_count = 0
for i in range(1, n+1):
    if n % i == 0:
        div_count += 1
if div_count > 2:
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")

# Task: Find max, min, average of N numbers
import math
q = int(input("Quantity : "))
max_val = -math.inf
min_val = math.inf
sum_val = 0
for i in range(q):
    n = int(input("Enter number : "))
    sum_val += n
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n
print("Maximum", max_val)
print("Minimum", min_val)
print("Average is", sum_val/q)

# Pattern: N x N plus signs
N = int(input("N= "))
for row in range(N):
    for col in range(N):
        print("+", end="")
    print()

# Pattern: M rows, columns 1..N
M = int(input("M = "))
N = int(input("N = "))
for row in range(M):
    for col in range(1, N+1):
        print(col, end="")
    print()

# Pattern: Right-angled triangle of numbers
N = int(input("N = "))
for row in range(1, N+1):
    for col in range(1, row+1):
        print(col, end="")
    print()

# Tracing loop (original)
x = 0
p = 0
sum_val = 0
p = 1
x = 2
q = 0.0
sum_val = 0
while p < 10:
    q = x + p - (sum_val + int(5/3)) / 3.0 % 2
    sum_val = sum_val + x + int(q)
    x += 1
    print(sum_val)
    if x > 5:
        p += int(4/2)
    else:
        p += 3 % 1
sum_val = sum_val + p
print(sum_val)

# Another tracing loop
x = y = 0
sum_val = 0
while x < 10:
    y = x - 3
    while y < 3:
        sum_val = x - y * 2
        print(sum_val)
        y = y + 1
    if x > 7:
        x += 1
    else:
        x += 3
sum_val = x - y * 2
print(sum_val)

# Another tracing loop
x = 0
y = 0
sum_val = 0
p = 0.0
while x < 10:
    y = x // 2
    while y < x:
        p = (x + 10.0) / 2
        sum_val = (sum_val % 2) + x - y * 2 + int(p)
        print(sum_val)
        y = y + 2
    if x > 5:
        x += 1
    else:
        x += 2

# Loop tracing
test = 1
j = 0
k = 100
while k > 0:
    while j < k:
        test = k + j - 21
        print(str(1 + int(test/2)))
        j += 10
    k -= 10
test = 1
j = 0
k = 100

# Fibonacci up to N
N = int(input("N = "))
n1, n2 = 0, 1
print("0", end=" ")
while n1 + n2 <= N:
    print(n2, end=" ")
    n1, n2 = n2, n1+n2
print()

# Decimal to binary
n = int(input("Enter decimal number : "))
bin_str = ""
while n > 0:
    res = n % 2
    n = n // 2
    bin_str += str(res)
print(bin_str[::-1])

# Binary to decimal
n = input()
dec = 0
for i in range(len(n)):
    x = int(n[-1-i])
    dec += 2**i * x
print(dec)

# Prime and perfect numbers in range
start = int(input())
stop = int(input())
prime = []
perfect = []
cprime = 0
cperfect = 0
for i in range(start, stop+1):
    count = 0
    sum_div = 0
    for j in range(1, i):
        if i % j == 0:
            count += 1
            sum_div += j
    if count == 1:
        cprime += 1
        prime.append(i)
    if sum_div == i:
        cperfect += 1
        perfect.append(i)
print(f"Between {start} and {stop} end,")
print(f"Found {cprime} prime numbers")
print(f"Found {cperfect} perfect numbers")
print("Prime numbers:", prime)
print("Perfect number:", perfect)

# Same but formatted output
start = int(input())
stop = int(input())
prime_str = ""
perfect_str = ""
cprime = 0
cperfect = 0
for i in range(start, stop+1):
    count = 0
    sum_div = 0
    for j in range(1, i):
        if i % j == 0:
            count += 1
            sum_div += j
    if count == 1:
        cprime += 1
        prime_str += str(i) + ","
    if sum_div == i:
        cperfect += 1
        perfect_str += str(i) + ","
prime_str = prime_str[:-1]
perfect_str = perfect_str[:-1]
print(f"Between {start} and {stop},")
print(f"Found {cprime} prime numbers")
print(f"Found {cperfect} perfect numbers")
print("Prime numbers:", prime_str)
print("Perfect number:", perfect_str)

# Product of digits divisible by c
a = int(input())
b = int(input())
c = int(input())
for i in range(a, b+1):
    prod = 1
    for ch in str(i):
        prod *= int(ch)
    if prod % c == 0:
        print(prod, end=" ")
print()
