0x06. Python - Classes and Objects

Resources
-https://intranet.alxswe.com/rltoken/Wy2djWXK5b4rnnYlAq_wlA
-https://intranet.alxswe.com/rltoken/MxIOanLf5vG5QeCWek2nqQ
-https://intranet.alxswe.com/rltoken/AoLH4xp5StrQST-Cu0Fg8w
-https://intranet.alxswe.com/rltoken/-vVnWzwR3a3X0H8Oia78Ug
-https://intranet.alxswe.com/rltoken/qz3KSn154ia4H2DPaabOzg


General
-All modules have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
-All classes have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
-All functions have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')


tasks
0. My first square
an empty class Square that defines a square

1. Square with size
a class Square that defines a square by: (based on 0-square.py)
Private instance attribute: size
Instantiation with size (no type/value verification)

2. Size validation
a class Square that defines a square by: (based on 1-square.py)
-Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0

3. Area of a square
a class Square that defines a square by: (based on 2-square.py)
-Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Public instance method: def area(self): that returns the current square area

4. Access and update private attribute
a class Square that defines a square by: (based on 3-square.py)
-Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area

5. Printing a square
 a class Square that defines a square by: (based on 4-square.py)
-Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line

6. Coordinates of a square
a class Square that defines a square by: (based on 5-square.py)
-Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space - Don’t fill lines by spaces when position[1] > 0
