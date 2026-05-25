# LAB-5: Lists

# Task: Build a list of 5 numbers
lis = []
for i in range(5):
    a = int(input())
    lis.append(a)
    print(lis)

# Task: Extract middle part of list (after splitting comma-separated input)
a = input()
b = []
a = a.split(",")
if len(a) > 3:
    for x in a:
        b.append(int(x))
    print(b[2:len(b)-2])
else:
    print("Not possible")

# Alternate parsing
a = input()
a += ","
lis = []
tmp = ""
for ch in a:
    if ch == ",":
        lis.append(int(tmp))
        tmp = ""
    else:
        tmp += ch
if len(lis) > 3:
    print(lis[2:len(lis)-2])
else:
    print("Not possible")

# Reverse print
lis = []
for i in range(5):
    a = int(input())
    lis.append(a)
print("Printing values from the list in reverse order:")
for j in range(1, len(lis)+1):
    print(lis[-j])

# Square each element
lis1 = [1, 2, 3, 4, 5, 6, 7]
lis2 = []
for x in lis1:
    lis2.append(x**2)
print(lis2)

# Remove empty strings
lis = ["hey", "there", "", "what's", "", "up", "", "?"]
mod = []
for item in lis:
    if item != "":
        mod.append(item)
print("Original List:", lis)
print("Modified List:", mod)

# Find largest number and its index
a = input()
a += ","
tmp = ""
lis = []
for ch in a:
    if ch == ",":
        lis.append(int(tmp))
        tmp = ""
    else:
        tmp += ch
print("My list:", lis)
max_val = lis[0]
idx = 0
for j in range(len(lis)):
    if lis[j] >= max_val:
        max_val = lis[j]
        idx = j
print(f"Largest number in the list is {max_val} which was found at index {idx}")

# Same using split
a = input()
a = a.split(",")
lis = [int(x) for x in a]
print(lis)
max_val = lis[0]
idx = 0
for j in range(len(lis)):
    if lis[j] > max_val:
        max_val = lis[j]
        idx = j
print(max_val, idx)

# Merge two lists (replace last element)
List_one = [1, 3, 5, 7, 9, 10]
List_two = [2, 4, 6, 8]
List_one = List_one[:len(List_one)-1] + List_two
print(List_one)

# Alternative merge
List_one = [1, 3, 5, 7, 9, 10]
List_two = [2, 4, 6, 8]
for x in List_one:
    if x == List_one[-1]:
        List_one = List_one[:-1]
        for y in List_two:
            List_one.append(y)
print(List_one)

# Another alternative
List_one = [1, 3, 5, 7, 9, 10]
List_two = [2, 4, 6, 8]
merged = []
for i in range(len(List_one)-1):
    merged.append(List_one[i])
for j in List_two:
    merged.append(j)
print(merged)

# Even numbers from two lists
list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = [10, 11, 12, -13, -14, -15, -16]
evens = []
for x in list_one:
    if x % 2 == 0:
        evens.append(x)
for x in list_two:
    if x % 2 == 0:
        evens.append(x)
print(evens)

# Filter odd numbers
a = input()
a = a.split(" ")
lis = [int(x) for x in a]
print("Original list:", lis)
odd_list = [x for x in lis if x % 2 != 0]
print("Modified list:", odd_list)

# Same with manual parsing
a = input()
a += " "
tmp = ""
lis = []
for ch in a:
    if ch == " ":
        lis.append(int(tmp))
        tmp = ""
    else:
        tmp += ch
print("Original list:", lis)
odd_list = [x for x in lis if x % 2 != 0]
print("Modified list:", odd_list)

# Remove duplicates
a = input()
a += ","
tmp = ""
lis = []
for ch in a:
    if ch == ",":
        lis.append(int(tmp))
        tmp = ""
    else:
        tmp += ch
print("Input list:", lis)
unique = []
for x in lis:
    if x not in unique:
        unique.append(x)
print("Modified list:", unique)

# Using split for duplicates
a = input()
a = a.split(", ")
lis = [int(x) for x in a]
print("Input list:", lis)
unique = []
for x in lis:
    if x not in unique:
        unique.append(x)
print("Modified list:", unique)

# Check common elements
List_one = [1, 4, 3, 2, 6]
List_two = [5, 6, 9, 8, 7]
common = False
for x in List_two:
    if x in List_one:
        common = True
        break
print(common)

# Loop tracing with list
myList = [0]*10
index1 = 1
while index1 < 10:
    myList[index1] = index1 + 4
    index2 = 1
    while index2 < index1:
        myList[index1] = myList[index1] + myList[index2] - index1
        index2 += 1
    print(myList[index1])
    index1 += 1

# Another tracing
myList = [0]*10
index1 = 1
while index1 < 10:
    myList[index1] = index1 + 4
    index2 = 1
    while index2 < index1:
        myList[index1] = myList[index1-1] - myList[index2-1] - index1
        index2 += 1
    print(myList[index1])
    index1 += 1

# Tracing with b list copy
myList = [0]*10
b = myList.copy()
index1 = 1
while index1 < 10:
    myList[index1] = index1 + 2
    index2 = 1
    while index2 < index1:
        myList[index1] = b[index1] + myList[index2] - index1
        index2 += 1
    print(myList[index1])
    index1 += 1

# More tracing
myList = [0]*10
b = myList.copy()
index1 = 1
while index1 < 10:
    myList[index1] = index1 + 1
    index2 = 1
    while index2 < index1:
        myList[index1] = b[index2-1] + myList[index2] - index1
        index2 += 1
    print(myList[index1])
    index1 += 1

# Second largest number
a = input()
a += ","
tmp = ""
lis = []
for ch in a:
    if ch == ",":
        lis.append(int(tmp))
        tmp = ""
    else:
        tmp += ch
print("My list:", lis)
max1 = max(lis)
max2 = min(lis)
idx2 = 0
for k in range(len(lis)):
    if lis[k] != max1 and lis[k] > max2:
        max2 = lis[k]
        idx2 = k
print(f"Second largest number in the list is {max2} which was found at index {idx2}.")

# Min and max with indices
a = input()
a += ","
tmp = ""
lis = []
for ch in a:
    if ch == ",":
        lis.append(int(tmp))
        tmp = ""
    else:
        tmp += ch
print("My list:", lis)
max_val = lis[0]
min_val = lis[0]
imax = imin = 0
for j in range(len(lis)):
    if lis[j] > max_val:
        max_val = lis[j]
        imax = j
    if lis[j] < min_val:
        min_val = lis[j]
        imin = j
print(f"Smallest number in the list is {min_val} which was found at index {imin}")
print(f"Largest number in the list is {max_val} which was found at index {imax}")

# Intersection of two lists
lis1 = input().split(", ")
lis2 = input().split(", ")
intersection = [x for x in lis2 if x in lis1]
print(intersection)

# Union without duplicates
list_one = [1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]
union = []
for x in list_one:
    if x not in union:
        union.append(x)
for x in list_two:
    if x not in union:
        union.append(x)
print(union)

# Parse string representation of list
a = input()
original = a.strip()
print("Original data:", original)
inside = original[1:-1].strip()
print("After removing square brackets:", inside)
# split by commas but keep spaces
parts = inside.split(',')
print("Numbers in string format with extra white spaces:", parts)
final = [int(p.strip()) for p in parts]
print("Final data (numbers in list format):", final)

# Duplicate removal from list input
a = input()
a += ","
tmp = ""
lis = []
for ch in a:
    if ch == ",":
        lis.append(int(tmp))
        tmp = ""
    else:
        tmp += ch
print("Given numbers in list:", lis)
unique = []
for x in lis:
    if x not in unique:
        unique.append(x)
print("List without any duplicate values:", unique)
