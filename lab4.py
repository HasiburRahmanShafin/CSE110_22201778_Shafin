# LAB-4: String Manipulation

# Reverse string (method 1)
a = input()
for i in range(-1, -len(a)-1, -1):
    print(a[i], end="")
print()

# Reverse string (method 2)
var = input()
for i in range(len(var)-1, -1, -1):
    print(var[i], end="")
print()

# Reverse using slicing
var = input()
print(var[::-1])

# Reverse part of string until index
var = input()
ind = int(input())
for i in range(ind, -1, -1):
    print(var[i], end="")
for j in range(ind+1, len(var)):
    print(var[j], end="")
print()

# Using slicing after reverse part
var = input()
ind = int(input())
for i in range(ind, -1, -1):
    print(var[i], end="")
print(var[ind+1:])

# Check if binary
num = input()
is_binary = True
for ch in num:
    if ch not in '01':
        is_binary = False
        break
print("Binary Number" if is_binary else "Not a Binary Number")

# Another binary check
num = input()
has_non_binary = 0
for ch in num:
    if ch not in '01':
        has_non_binary = 1
        break
print("Binary Number" if has_non_binary == 0 else "Not a Binary Number")

# Adjective to comparative/superlative
text = input()
if len(text) >= 3:
    if text[-3:] == "est":
        print(text)
    elif text[-2:] == "er":
        print(text[:-2] + "est")
    else:
        print(text + "er")
else:
    print(text)

# Alternative version
text = input()
if len(text) < 4:
    print(text)
elif len(text) > 3:
    if text.endswith('er'):
        print(text[:-2] + 'est')
    elif text.endswith('est'):
        print(text)
    else:
        print(text + 'er')

# Print progressive substrings
var = input()
for i in range(1, len(var)+1):
    print(var[:i])

# Print ASCII values of characters
text = input()
for ch in text:
    print(ch, ":", ord(ch))

# Shift letters forward by 1
text = input()
for ch in text:
    a = ord(ch)
    if a == 122:
        print("a", end="")
    else:
        print(chr(a+1), end="")
print()

# Convert every second character to uppercase
text = input()
for i in range(len(text)):
    if i % 2 != 0:
        a = ord(text[i])
        print(chr(a-32), end="")
print()

# Remove consecutive duplicates
text = input()
print(text[0], end="")
for i in range(len(text)-1):
    if text[i] != text[i+1]:
        print(text[i+1], end="")
print()

# Interleave two strings separated by comma
text = input()
comma_pos = text.find(',')
up = text[:comma_pos]
low = text[comma_pos+2:]   # skip comma and space
if len(up) >= len(low):
    for j in range(len(low)):
        print(up[j], low[j], sep="", end="")
    print(up[len(low):])
else:
    for k in range(len(up)):
        print(up[k], low[k], sep="", end="")
    print(low[len(up):])

# Loop tracing with string formatting
i = 10
while i >= -20:
    if i < 0:
        test = " != "
        test = str(i//2) + test + str(int(i/2))
    else:
        test = " == "
        test = str(i//2) + test + str(int(i/2))
    print(test)
    i -= 5

# Another loop tracing with concatenation
test = "-->"
i = 0
j = 0
k = 15
while i < 5:
    j = k - 1
    k -= 1
    while j > 10:
        test = str(i + j) + "--> " + test
        print(test)
        j -= 1
    i += 1

# More complex tracing
test = ""
i = 5
j = 0
k = 15
while i < 10:
    k -= 1
    j = k
    while j > 10:
        if j % 2 == 0:
            test = "<--"
            test = test + str(i) + str(2) + "-->" + str(int(j/2))
        else:
            test = "-->"
            test = "--> " + str(int(i/2)) + test + str(j)
        print(test)
        j -= 1
    i += 1

# Variant with 3
test = ""
i = 5
j = 0
k = 15
while i < 10:
    k -= 1
    j = k
    while j > 10:
        if j % 2 == 0:
            test = "<--"
            test = test + str(i) + '3' + "-->" + str(j//3)
        else:
            test = "-->"
            test = "--> " + str(i//3) + test + str(j)
        print(test)
        j -= 1
    i += 1

# String accumulation with 'cat'
i = 0
j = 0
k = 15
test = '<--cat'
while i < 5:
    k -= 1
    j = k
    while j > 10:
        if j % 2 == 0:
            test += '-->'
            test = test + str(i) + str(j//2)
        else:
            test += '<--'
            test = test + str(i//2) + str(j)
        print(test)
        j -= 1
    i += 1

# Remove character from string
txt = input("Enter text: ")
c = input("character: ")
if c in txt:
    for ch in txt:
        if ch != c:
            print(ch, end="")
elif len(txt) > 3 and c not in txt:
    print(txt[1:-1])
else:
    print(txt)
print()

# Another removal (just skip char)
txt = input("Enter text: ")
s = input("character: ")
for ch in txt:
    if ch != s:
        print(ch, end="")
print()

# Repeat string based on parity
txt = input("Enter text: ")
num = int(input("Number: "))
if num % 2 == 0:
    print(txt * (num*2))
else:
    print(txt * (num*3))

# Alternating case
txt = input()
res = 'a'
for i in range(len(txt)):
    v = ord(txt[i])
    if 65 <= v <= 90 or 97 <= v <= 122:
        if 65 <= ord(res) <= 90:
            if 65 <= v <= 90:
                res = chr(v+32)
                print(res, end="")
            else:
                res = chr(v)
                print(res, end="")
        elif 97 <= ord(res) <= 122:
            if 97 <= v <= 122:
                res = chr(v-32)
                print(res, end="")
            else:
                res = chr(v)
                print(res, end="")
    else:
        print(txt[i], end="")
print()

# Count letters, digits, symbols
text = input()
letters = digits = symbols = 0
for ch in text:
    val = ord(ch)
    if 65 <= val <= 90 or 97 <= val <= 122:
        letters += 1
    elif 48 <= val <= 57:
        digits += 1
    else:
        symbols += 1
print("Letters : ", letters)
print("Number : ", digits)
print("Symbols : ", symbols)
