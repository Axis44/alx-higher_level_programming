0x07. Python - Test-driven development

Resources
-https://intranet.alxswe.com/rltoken/96kLRRIOHzsn3VDDXT21HA

Python Test Cases
-test files are inside a folder tests, and test files should be text files (extension: .txt)
-tests are executed by using this command: python3 -m doctest ./tests/*
-  modules have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
-functions have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')


Tasks
0. Integers addition
function that adds 2 integers.
-Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b

1. Divide a matrix
 function that divides all elements of a matrix.
-Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix

2. Say my name
 function that prints My name is <first name> <last name>
-Prototype: def say_my_name(first_name, last_name=""):
first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a string

3. Print square
 function that prints a square with the character #.
-Prototype: def print_square(size):
size is the size length of the square
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
if size is a float and is less than 0, raise a TypeError exception with the message size must be an integer

4. Text indentation
 function that prints a text with 2 new lines after each of these characters: ., ? and :
-Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message text must be a string, no space at the beginning or at the end of each printed line

5. Max integer - Unittest
write unittests for the function def max_integer(list=[]):
-test file should be inside a folder tests AND use the unittest module
-test file executed by using this command: python3 -m unittest tests.6-max_integer_test
