# Additional Problems from the Notebook

# Product of ASCII values per key
def product_of_list(d):
    result = []
    for lst in d.values():
        prod = 1
        for ch in lst:
            prod *= ord(ch)
        result.append(prod)
    return tuple(result)
b = {'A': ['a', 'c'], 'B': ['b', 'z'], 'C': ['g', 'm']}
print(product_of_list(b))

# Column-wise sum of tuple of tuples
tup = ((1, 2, 3, 4), (3, 5, 2, 1), (2, 2, 3, 1))
col_sums = [sum(col) for col in zip(*tup)]
print(tuple(col_sums))

# Sum of elements in each inner tuple
org = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
sums = [sum(inner) for inner in org]
print(sums)

# Sort list of tuples by float value
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
price_sorted = sorted(price, key=lambda x: float(x[1]))
print(price_sorted)

# Check if color exists in nested tuple
given = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
color = input()
found = any(color in inner for inner in given)
print(found)

# Categorize characters
txt = input("Input : ")
upper = lower = digits = special = ''
for ch in txt:
    if ch.isupper():
        upper += ch
    elif ch.islower():
        lower += ch
    elif ch.isdigit():
        digits += ch
    elif not ch.isspace():
        special += ch
print("Upper-Case:", upper)
print("Lower-Case:", lower)
print("Digits:", digits)
print("Special:", special)
new_word = ''
for i in range(min(len(upper), len(lower), len(digits), len(special))):
    new_word += upper[i] + lower[i] + digits[i] + special[i]
print("New word:", new_word)

# Caesar cipher decode
encoded = input()
decoded = ''
for ch in encoded:
    if ch.isalpha():
        base = ord('a') if ch.islower() else ord('A')
        decoded += chr((ord(ch) - base + 21) % 26 + base)
    else:
        decoded += chr(ord(ch) - 3)
print("Decoded message:", decoded)
imposter = ''.join(c for c in decoded if c.isalpha())
print("Imposter name:", imposter)

# Convert list-like string to uppercase each word
a = input()
words = ''.join(c for c in a if c.isalpha() or c == ',').split(',')
for w in words:
    print(w.capitalize())

# Validate ID (sum of first 8 digits mod 10 equals last digit)
var = input()
total = sum(int(var[i]) for i in range(8))
if total % 10 == int(var[-1]):
    print("Match")
else:
    print("No")

# Boolean logic with input (always prints DORMAMMU LEAVES)
dormammu_gives_up = bool(input('please enter if the statement is TRUE OR FALSE: '))
if True:
    print("DORMAMMU LEAVES THE EARTH ALONE")
if False:
    number_of_stones_dr_strange_has = 1
    while number_of_stones_dr_strange_has > 0:
        print("DORMAMMU ! I HAVE COME TO BARGAIN")

# Prime numbers in range
start = int(input())
end = int(input())
primes = []
for num in range(start, end+1):
    if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5)+1)):
        primes.append(num)
print("Found", len(primes), "prime numbers")
print("Prime numbers:", ", ".join(map(str, primes)))

# Perfect numbers in range
for num in range(start, end+1):
    if num > 0 and sum(i for i in range(1, num) if num % i == 0) == num:
        print(num)

# Hexadecimal addition
chk1 = {chr(ord('A')+i): 10+i for i in range(6)}
chk2 = {v: k for k, v in chk1.items()}
a = input().upper()
b = input().upper()
def hex_to_dec(s):
    val = 0
    for ch in s:
        val = val*16 + (int(ch) if ch.isdigit() else chk1[ch])
    return val
dec_sum = hex_to_dec(a) + hex_to_dec(b)
print(hex(dec_sum)[2:].upper())

# More cipher (same as earlier)
encoded = input()
decoded = ''
for ch in encoded:
    if 'a' <= ch <= 'z':
        decoded += chr((ord(ch) - ord('a') + 21) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        decoded += chr((ord(ch) - ord('A') + 21) % 26 + ord('A'))
    else:
        decoded += chr(ord(ch) - 3)
print(decoded)
name = ''.join(c for c in decoded if c.isalpha())
print(name)

# Convert bracketed list to proper list and capitalize each word
a = input()
clean = ''.join(c for c in a if c.isalpha() or c == ',').split(',')
for w in clean:
    print(w.capitalize())

# Diamond pattern
char = input()
n = int(input())
# Upper half
for i in range(n):
    print(" "*(n-1-i) + char + (" " + char)*i)
# Lower half
for i in range(n-2, -1, -1):
    print(" "*(n-1-i) + char + (" " + char)*i)

# Hollow diamond
char = input()
n = int(input())
print(" "*(n-1) + char)
for i in range(1, n):
    print(" "*(n-1-i) + char + " "*(2*i-1) + char)
for i in range(n-2, 0, -1):
    print(" "*(n-1-i) + char + " "*(2*i-1) + char)
print(" "*(n-1) + char)

# Pyramid with spaces
char = input()
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) + (char + " ")*(i))

# Combine keys and values into dictionary and tuple
keys = ['key1','key2','key3','key1','key2']
values = [10, [20], 30, [40,50], 10]
merged = {}
for k, v in zip(keys, values):
    merged.setdefault(k, []).append(v)
print(merged)
flat = []
for k, v in merged.items():
    flat.append(k)
    flat.append(v)
print(tuple(flat))

# Missing letters in sequence
def missing_numbers(start, lst):
    start_ord = ord(start)
    present = set(lst)
    missing = []
    for i in range(len(lst)):
        ch = chr(start_ord + i)
        if ch not in present:
            missing.append(ch)
    return missing
l = ['g','f','e','j','k','f','e','d']
left = 'd'
print(missing_numbers(left, l))

# Find actor from nested dict
cast = {
    'Friends': [('Joey', 'Matt'), ('Chandler', 'Matthew')],
    'BBT': [('Penny', 'Kaley'), ('Sheldon', 'Jim')],
    'Breaking Bad': [('Jesse', 'Aaron'), ('Walter', 'Bryan')]
}
name = input()
for show, actors in cast.items():
    for actor, real in actors:
        if name == actor:
            print(f"{name} was played by {real} in {show}")
            break

# Pattern with # and A
def print_pattern(n):
    for i in range(n, 1, -1):
        print("#"*(i-1) + "A"*i)
    print("A"*n)
b = int(input())
print_pattern(b)

# Index mapping for characters in string (positive and negative)
def index_mapping(s):
    n = len(s)
    d = {}
    for i, ch in enumerate(s):
        if ch not in d:
            d[ch] = [i, i-n]
        else:
            d[ch].extend([i, i-n])
    return d
print(index_mapping("pythonbook"))

# Reconstruct string from tuple values
d1 = {"0": (3,4), "1": (2,3), "2": (1,2), "3": (1,0), "5": (1,6), "6": (1,5), "7": (2,1)}
length = max(v[1] for v in d1.values()) + 1
result = [''] * length
for ch, (count, pos) in d1.items():
    result[pos] = ch * count
print(''.join(result))

# Process dimensions string
def shipping_info(dim_str):
    unit = dim_str[-2:]
    dims = dim_str[:-2].split('x')
    print("Length:", dims[0])
    print("height:", dims[1])
    print("width:", dims[2])
    print("Unit:", unit)
b = input()
shipping_info(b)

# Compute cumulative sums/products based on parity
a = input()
nums = [int(x) for x in a.split('#')]
result = {}
for idx, val in enumerate(nums):
    if val % 2 == 0:
        result[idx] = sum(nums[:idx+1])
    else:
        prod = 1
        for k in range(idx+1):
            prod *= nums[k]
        result[idx] = prod
print(nums)
print(result)

# Separate even/odd digits from list of strings
def checker(lst):
    evens = []
    odds = []
    for item in lst:
        if item.isdigit():
            d = int(item)
            if d % 2 == 0:
                evens.append(d)
            else:
                odds.append(d)
    print("EvenList:", evens)
    print("OddList:", odds)
checker(["1","2","c","3","4","Z"])

# Join dictionary keys' tuples as string and map sum to value
dic = {(1,2,3): "Shafin", (10,): "uwu", (1,12,4,7): "hahah"}
concatenated = ''.join(dic.values())
new_dict = {sum(k): v for k, v in dic.items()}
print(concatenated)
print(new_dict)

# Convert mixed list to string
def list_to_string(lst):
    return ''.join(str(x) for x in lst)
print(list_to_string(["Hello",1,"2",3.3,True]))

# Separate vowels and consonants, print alternately
vowels = "aeiouAEIOU"
word = input("word= ")
vow = ''.join(ch for ch in word if ch in vowels)
con = ''.join(ch for ch in word if ch not in vowels)
for i in range(len(word)):
    if i % 2 == 0:
        print(vow)
    else:
        print(con)

# Count spaces in a long paragraph
text = input()
print(text.count(' '))
