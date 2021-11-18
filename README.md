# Introductory Python Course - UiT

Welcome to this introductory programming course. We will use the programming language [Python](https://www.python.org/).

## Areas of Competence

### Basic Topics
- Variables
- Conditions
- Chained Conditionals
- Operators
- Control Flow (If/Else)
- Loops and Iterables
- Basic Data Structures
- Functions
- Mutable vs. Immutable
- Common Methods
- File IO

### Intermediate Topics
- Object Oriented Programming
- Data Structures
- Comprehensions 
- Lambda Functions
- Map, Filter
- Collections
- *args & **kwargs
- Inheritance
- Dunder Methods
- PIP
- Environments
- Modules
- Async IO

### Advanced Topics
- Decorators
- Generators 
- Context Managers
- Metaclasses
- Concurrency 
- Parallelism 
- Testing
- Packages

## Iterators and Generators

### The Iterator Protocol
```python
x = iter([1, 2, 3])
>>> x
<listiterator object at 0x1004ca850>
>>> next(x)
1
>>> next(x)
2
>>> next(x)
3
>>> next(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### Example Implementations
```python
class Range:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
```

```python
class ReverseRange:
	def __init__(self, count):
		self.i = count
		self.count = count
	def __iter__(self):
		return self
	def __next__(self):
		if self.i > 0:
			i = self.i
			self.i -= 1
			return i
		else:
			raise StopIteration()
```

### Generators
```python
def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1
```

```python
def even_generator(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield int(number)
```

### Generator Comprehension
#### Template
```my_gen = (<expression> for <item> in <iterable> if <condition>)```

#### Example
```python
eg = (int(number) for number in my_list if number % 2 == 0)
```

## Comprehensions

### List Comprehension
#### Template
```python
my_list = [<expression> for <item> in <iterable> if <condition>]
```

#### Example
```python
squares = [i * i for i in range(10)]
```

### Dictionary Comprehension
#### Template
```python
my_dict = {<key>:<value> for <item> in <iterable> if <condition>}
```

#### Example
```python
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}  
```

### Set Comprehension
#### Template
```my_set = {<expression> for <item> in <iterable> if <condition>}```

#### Example
```python
>>> {s for s in [1, 2, 1, 0]}
set([0, 1, 2])
>>> {s**2 for s in [1, 2, 1, 0]}
set([0, 1, 4])
>>> {s**2 for s in range(10)}
set([0, 1, 4, 9, 16, 25, 36, 49, 64, 81])
```