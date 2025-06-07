# 1. Task Description: Uses conditional statements (if-elif-else)
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)

# 2. Compress the String



from itertools import groupby

s = input().strip()
compressed = []

for key, group in groupby(s):
    count = len(list(group))
    compressed.append(f"({count}, {key})")

print(' '.join(compressed))

# 3. The Minion Game
def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i
    
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

s = input().strip()
minion_game(s)

# 4. Write a Function
def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

year = int(input())
print(is_leap(year))
# 5. Word Order
from collections import OrderedDict

n = int(input())
word_counts = OrderedDict()

for _ in range(n):
    word = input().strip()
    word_counts[word] = word_counts.get(word, 0) + 1

print(len(word_counts))
print(' '.join(map(str, word_counts.values())))

# 6. Iterables and Iterators
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

all_combinations = list(combinations(letters, k))
a_combinations = [c for c in all_combinations if 'a' in c]

probability = len(a_combinations) / len(all_combinations)
print(f"{probability:.3f}")
# 7. Python Tuples
n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))
# 8. Finding the Percentage
n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
marks = student_marks[query_name]
average = sum(marks) / len(marks)
print("{:.2f}".format(average))
# 9. Python String Formatting
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        dec = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{dec.rjust(width)} {octal.rjust(width)} {hexa.rjust(width)} {binary.rjust(width)}")

n = int(input())
print_formatted(n)