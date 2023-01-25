# Indentation and pass
# Need four spaces for indentation
# while True:
#     print('True')

# Function Definitions
# def fib(n):
#     if n <=1:
#         return n
#     else: return fib(n-1) + fib(n-3)
#
# fib()

#Default Value
# def fib(n=10):
#     if n <=1:
#         return n
#     else: return fib(n-1) + fib(n-3)
#
# fib()

# Lambda Expressions
# square = lambda x: x ** 2
# square(4)
#
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])

# PEP 8
# Checkstyle for Python it is automatically found in Pycharm
# Variables and function names and should be lowercase with underscores: x_position
# Class names are camel-case: MachineLearning, FeatureSelection
# Private fields in a class have a leading underscore self._not_for_you

# More on lists
# list.append(x)
# list.extend(iterable)
# list.insert(i, x)
# list.remove(x)
# list.pop([i])
# list.clear()
# list.index(x[, start[, end]])
# list.count(x)
# list.sort(key=None, reverse=False)
# list.reverse()
# list.copy()

# Queues
# from collections import deque
# queue = deque['Eric', 'Adam', 'James']
# queue.append('Terry')

# List Comprehensions
# squares = []
# for x in range[10]:
#     squares.append(x**2)
# squares
# # or
# squares = [x**2 for x in range(10)]
# squares

# Tuples
# t = 123, 456, 'hello'
# # These can not be changed or shuffled around once made (immutable)
# # Can be indexed like a list

# Sets
# basket = {'apple', 'orange', 'apple', 'pear'}
# 'orange' in basket
#
# 'banana' in basket
#
# a = {x for x in 'abracadabra' if x not in 'abc'}
# a

# Dictionaries
# tel = {'jack', 4098, 'sape', 4087}

# Writing To Files
# with open('file.txt', 'r') as fp:
#     s = fp.read()
#     print(s)
