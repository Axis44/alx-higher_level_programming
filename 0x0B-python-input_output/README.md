0x0B. Python - Input/Output

Resources
-https://intranet.alxswe.com/rltoken/ZvtAdnUzjnEVu1sjg3m_tQ

Python Test Cases
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Tasks
0. Read file
-function that reads a text file (UTF8) and prints it to stdout:
Prototype: def read_file(filename=""):
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.

1. Write to a file
- function that writes a string to a text file (UTF8) and returns the number of characters written:
Prototype: def write_file(filename="", text=""):
-use the with statement and function should create the file if doesn’t exist
-function should overwrite the content of the file if it already exists.

2. Append to a file
-function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
Prototype: def append_write(filename="", text=""):
-If the file doesn’t exist, it should be created and using the with statement
-don’t need to manage file permission or file doesn't exist exceptions.

3. To JSON string
- function that returns the JSON representation of an object (string):
Prototype: def to_json_string(my_obj):

4. From JSON string to Object
- function that returns an object (Python data structure) represented by a JSON string:
Prototype: def from_json_string(my_str):

5. Save Object to a file
- function that writes an Object to a text file, using a JSON representation:
Prototype: def save_to_json_file(my_obj, filename):
 use the with statement and no need to manage exceptions if the object can’t be serialized.

6. Create object from a JSON file
- function that creates an Object from a “JSON file”:
Prototype: def load_from_json_file(filename):
-use the with statement and no need to manage exceptions if the JSON string doesn’t represent an object.

7. Load, add, save
script that adds all arguments to a Python list, and then save them to a file:
use your function save_to_json_file from 5-save_to_json_file.py, also with load_from_json_file from 6-load_from_json_file.py
-The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created

8. Class to JSON
-function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
Prototype: def class_to_json(obj):
-obj is an instance of a Class
All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean

9. Student to JSON
class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)

10. Student to JSON with filter
- A  class Student that defines a student by: (based on 9-student.py)
Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved

11. Student to disk and reload
 a class Student that defines a student by: (based on 10-student.py)
-Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attributes name contain in this list must be retrieved.
Otherwise, all attributes must be retrieved
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
You can assume json will always be a dictionary
A dictionary key will be the public attribute name
A dictionary value will be the value of the public attribute

12. Pascal's Triangle
 function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
-Returns an empty list if n <= 0 and n will be always an integer
