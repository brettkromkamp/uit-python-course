# Introductory Python Course - UiT

Welcome to this introductory programming course. We will use the programming language [Python](https://www.python.org/).

## Recommended Python Learning Path

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

## Truthy and Falsy in Python

### Falsy Values

#### Sequences and Collections
- Empty lists []
- Empty tuples ()
- Empty dictionaries {}
- Empty sets set()
- Empty strings ""
- Empty ranges range(0)

#### Numbers
- Zero of any numeric type
- Integer: 0
- Float: 0.0
- Complex: 0j

#### Constants
- None
- False

### Truthy Values

By default, an object is considered true.

#### Truthy Values
- Non-empty sequences or collections (lists, tuples, strings, dictionaries, sets).
- Numeric values that are not zero.
- True

## Resources
- [Structural pattern matching in Python 3.10](https://benhoyt.com/writings/python-pattern-matching/)
- [Time complexity in CPython](https://wiki.python.org/moin/TimeComplexity)
- [Pass by reference in Python](https://realpython.com/python-pass-by-reference/)
- [Variables in Python](https://realpython.com/python-variables/)
- [Variables and scope - Global, nonlocal and local](https://medium.com/swlh/variables-and-scopes-in-python-global-nonlocal-and-local-923a71cb57d4)
- [Truthy and Falsy in Python](https://www.freecodecamp.org/news/truthy-and-falsy-values-in-python/)
- [What every programmer needs to know about encodings](https://kunststube.net/encoding/)
- [How Python does Unicode](https://www.b-list.org/weblog/2017/sep/05/how-python-does-unicode/)
- [Dictionary comprehension tutorial](https://www.datacamp.com/community/tutorials/python-dictionary-comprehension)
- [How to use Python lambda functions](https://realpython.com/python-lambda/)
- [Destructuring in Python](https://blog.teclado.com/destructuring-in-python/)
- [Listening to sorting algorithms](https://www.youtube.com/watch?v=GIvjJwzrHBU)
- [Tkinter 8.5 reference](https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html)
- [Iterators and generators](https://anandology.com/python-practice-book/iterators.html)
- [Four types of comprehensions](https://towardsdatascience.com/4-types-of-comprehensions-in-python-2fbeafdf2fda)
- [When to use a list comprehension](https://realpython.com/list-comprehension-python/)
- [Context managers and Python's ```with``` statement](https://realpython.com/python-with-statement/)
- [Primer on Python decorators](https://realpython.com/primer-on-python-decorators/)
- [Introduction to Python generators](https://realpython.com/introduction-to-python-generators/)
