# LAB-6: Tuples and Dictionaries

# Access nested tuple element
a_tuple = ("The Institute", ("Best Mystery & Thriller", "The Silent Patient", 68821), 75717,
           [1, 2, 3, 400, 5, 6, 7], ("Best Fiction", "The Testaments", 98291))
print(a_tuple[3][3])

# Extract middle part of tuple
a = input()
a = a[1:-1]  # remove parentheses
a = a.split(",")
tup = tuple(int(x) for x in a)
if len(tup) > 3:
    print(tup[2:len(tup)-2])

# Another tuple slicing
tup = (10, 20, 24, 25, 26, 35, 70)
if len(tup) > 3:
    print(tup[2:len(tup)-2])

# Book info tuple of tuples
book_info = (
    ("Best Mystery & Thriller", "The Silent Patient", 68, 821),
    ("Best Horror", "The Institute", 75, 717),
    ("Best History & Biography", "The five", 31, 783),
    ("Best Fiction", "The Testaments", 98, 291)
)
print("Size of the tuple is:", len(book_info))
for book in book_info:
    print(book)

# Format book info with votes
book_info = (
    ("Best Mystery & Thriller", "The Silent Patient", 68821),
    ("Best Horror", "The Institute", 75717),
    ("Best History & Biography", "The five", 31783),
    ("Best Fiction", "The Testaments", 98291)
)
for award, book, votes in book_info:
    print(f"{book} won the '{award}' category with {votes} votes")

# Count occurrences in tuple
tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
target = int(input())
count = tup.count(target)
print(f"{target} appears {count} times in the tuple")

# Reverse tuple
tup = (10, 20, 30, 40, 50, 60)
rev = tuple(reversed(tup))
print(rev)

# Merge dictionaries
a = {'Harry': 15, 'Draco': 8, 'Nevil': 19}
b = {'Ginie': 18, 'Luna': 14}
merged = {**a, **b}
print(merged)

# Compute average from dictionary input
z = input()
# Remove braces and quotes
cleaned = z.strip('{}').replace('"', '').replace("'", "")
pairs = cleaned.split(', ')
dic = {}
for pair in pairs:
    key, val = pair.split(':')
    dic[key] = int(val)
total = sum(dic.values())
avg = total // len(dic)
print("Average is", avg)

# Same using simpler parsing
a = input()
a = a.split(', ')
dic = {}
for item in a:
    k, v = item.split(':')
    dic[k] = int(v)
total = sum(dic.values())
print("Average is", total // len(dic))

# Filter dictionary by value threshold
exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
threshold = int(input())
filtered = {k: v for k, v in exam_marks.items() if v >= threshold}
print(filtered)

# Highest selling genre
sales = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure': 14}
max_sales = max(sales.values())
best_genre = [g for g, s in sales.items() if s == max_sales][0]
print(f"The highest selling book genre is '{best_genre}' and the number of books sold are {max_sales}.")

# Count characters in string (case-insensitive)
a = input()
# Remove surrounding quotes
a = a[1:-1].lower()
char_count = {}
for ch in a:
    if ch == ' ':
        continue
    char_count[ch] = char_count.get(ch, 0) + 1
print(char_count)

# Count total elements in dictionary of lists
dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
total_elements = sum(len(v) for v in dict_1.values())
print(total_elements)

# Convert list of tuples to dictionary of lists
list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
grouped = {}
for key, val in list_1:
    grouped.setdefault(key, []).append(val)
print(grouped)

# Tracing with dictionary update
dict1 = {'a': 59, 'b': -82, 'c': 5, 'd': -81, 'e': 53}
for key in dict1:
    j = 0
    k = 22
    while j < 5:
        if j % 2 == 0:
            k = dict1[key] + j - (8 + k % 6) / 3
            dict1[key] = dict1[key] + int(k)
        else:
            k = dict1[key] + j - (6 - k % 8) * 3
            dict1[key] = dict1[key] - int(k)
        j += 1
    print(int(k))
    print(key + " -> " + str(dict1[key]))

# Multiply tuple pairs
lis1 = [(11, 22), (33, 55), (55, 77), (11, 44)]
products = [a*b for a, b in lis1]
print(products)

# Modify tuple of lists
a_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
new_val = input()
new_tuple = []
for lst in a_tuple:
    lst.pop()
    lst.append(new_val)
    new_tuple.append(lst)
print(tuple(new_tuple))

# Remove None values from dict
my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue', 'a5': None}
cleaned_dict = {k: v for k, v in my_dictionary.items() if v is not None}
print(cleaned_dict)

# Filter dict by range
dict_1 = {'a': 6, 'b': 7, 'c': 9, 'd': 8, 'e': 11, 'f': 12, 'g': 13}
limits = input().split(",")
low, high = int(limits[0]), int(limits[1])
filtered_dict = {k: v for k, v in dict_1.items() if low <= v < high}
print(filtered_dict)

# Group by second element
a = [(20, 'Sad'), (31, 'Sad'), (88, 'NotSad'), (27, 'NotSad')]
grouped = {}
for val, key in a:
    grouped.setdefault(key, []).append((val, key))
print(grouped)

# Advanced string processing (hash mapping words)
var1 = input().strip("[]'")
words = var1.split()
var2 = input().strip("[]'")
hash_list = var2.split()
dic = {}
print("Words in the given String:", words)
for w in words:
    total_ord = sum(ord(ch) for ch in w)
    idx = total_ord % len(hash_list)
    key = hash_list[idx]
    if key not in dic:
        dic[key] = []
    if w not in dic[key]:
        dic[key].append(w)
print(dic)
