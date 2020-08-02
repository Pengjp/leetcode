# Reference https://realpython.com/python-coding-interview-tips/

# Decrementing with range() and enumerate()
for i in range(10, 0, -2): # negative steps work
    print(i)
for i in reversed(range(5)): # use built-in reversed()
    print(i)

def enumerate2(xs, start=0, step=1):
    for x in xs:
        yield (start, x)
        start += step

assert list(enumerate2([1,2,3], 5, -1)) == [(5, 1), (4, 2), (3, 3)]

# Iterate With enumerate() Instead of range()

numbers = [45, 22, 14, 65, 97, 72]

for i, num in enumerate(numbers):
	if num % 3 == 0 and num % 5 == 0:
		numbers[i] = 'fizzbuzz'
	elif num % 3 == 0:
		numbers[i] = 'fizz'
	elif num % 5 == 0:
		numbers[i] = 'buzz'

assert numbers == ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']

# customize start value
for i, num in enumerate(numbers, start=52):
	print(i,num)

# Use List Comprehensions Instead of map() and filter()
numbers = [4, 2, 1, 6, 9, 7]
def square(x):
	return x * x

assert list(map(square, numbers)) == [square(x) for x in numbers]

def is_odd(x):
	return bool(x % 2)

assert list(filter(is_odd, numbers)) == [x for x in numbers if is_odd(x)]

# Save Memory With Generators
# this approach will consume lots of memory
sum([i * i for i in range(1, 1001)])
#use generators instead
sum((i * i for i in range(1, 1001)))

# Define Default Values in Dictionaries With .get() and .setdefault()

cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
# wish to get cowboy's name, in an naive way:
''' 
if 'name' in cowboy:
	print(cowboy['name'])
else:
	print('The Man with No Name')
'''
# a better way
name = cowboy.get('name', 'The Man with No Name')
# if I want to update the dictionary with a default value
name = cowboy.setdefault('name', 'The Man with No Name')

# Handle Missing Dictionary Keys With collections.defaultdict()
grades = [
     ('elliot', 91),
     ('neelam', 98),
     ('bianca', 81),
     ('elliot', 88),
]

from collections import defaultdict
student_grades = defaultdict(list) # defaultdict calls list() if the name doesn’t exist and then allows the grade to be appended.
for name, grade in grades:
	student_grades[name].append(grade)

# Count Hashable Objects With collections.Counter
from collections import Counter
words = "if there was there was but if there was not there was not".split()
counts = Counter(words)
print(dict(counts))
print('two most common works:',counts.most_common(2))

#Generate Permutations and Combinations With itertools
import itertools
friends = ['Monique', 'Ashish', 'Devon', 'Bernie']
list(itertools.permutations(friends, r=2))
list(itertools.combinations(friends, r=2))