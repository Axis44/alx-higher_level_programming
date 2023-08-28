0x05. Python - Exceptions

Resources
https://intranet.alxswe.com/rltoken/Yj7sDOzmKwICSHr7WEAW3A
https://intranet.alxswe.com/rltoken/xASzXarhF1sBhzYkJ14LvQ

Tasks
0. Safe list printing
-function that prints x elements of a list.
Prototype: def safe_print_list(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my_list
Returns the real number of elements printed, using  try: / except:
-no importing of any module and or use of  len()

1. Safe printing of an integers list
- function that prints an integer with "{:d}".format().
Prototype: def safe_print_integer(value):
value can be any type (integer, string, etc.)
The integer should be printed followed by a new line
Returns True if value has been correctly printed (it means the value is an integer)
Otherwise, returns False
-using try: / except: and "{:d}".format() to print as integer
-not importing amy module or use type()

2. Print and count integers
function that prints the first x elements of a list and only integers.
Prototype: def safe_print_list_integers(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
x represents the number of elements to access in my_list
x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
Returns the real number of integers printed
-using  try: / except: and  "{:d}".format() to print an integer
- not importing any module or use len()


3. Integers division with debug
a function that divides 2 integers and prints the result.
Prototype: def safe_print_division(a, b):
You can assume that a and b are integers
The result of the division should print on the finally: section preceded by Inside result:
Returns the value of the division, otherwise: None
-using  try: / except: / finally: and "{}".format() to print the result
-not importing any any module

4. Divide a list
 function that divides element by element 2 lists.
Prototype: def list_division(my_list_1, my_list_2, list_length):
my_list_1 and my_list_2 can contain any type (integer, string, etc.)
list_length can be bigger than the length of both lists
Returns a new list (length = list_length) with all divisions
If 2 elements can’t be divided, the division result should be equal to 0
If an element is not an integer or float:
print: wrong type
If the division can’t be done (/0):
print: division by 0
If my_list_1 or my_list_2 is too short
print: out of range
-using try: / except: / finally: andnot import any module

5. Raise exception
 function that raises a type exception.
Prototype: def raise_exception(): and not importing any module

6. Raise a message
function that raises a name exception with a message.
Prototype: def raise_exception_msg(message=""):
