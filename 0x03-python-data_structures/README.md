Python - Data Structures: Lists, Tuples

0. Print a list of integers
function that prints all integers of a list
-Prototype: def print_list_integer(my_list=[]):
-Format: one integer per line
-not allowed to import any module and assume that the list only contains integers
-not allowed to cast integers into strings, and to use str.format() to print integers


1. Secure access to an element in a list
function that retrieves an element from a list like in C
-Prototype: def element_at(my_list, idx)
-If idx is negative, the function should return None and idx is out of range (> of number of element in my_list), the function should return None
-not allowed to import any module, and not allowed to use try/except


2. Replace element
function that replaces an element of a list at a specific position
-Prototype: def replace_in_list(my_list, idx, element)
-If idx is negative, the function should not modify anything, and returns the original list and idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
-not allowed to import any module and not allowed to use try/except


3. Print a list of integers... in reverse!
function that prints all integers of a list, in reverse order
-Prototype: def print_reversed_list_integer(my_list=[]):
-Format: one integer per line and not allowed to import any module
- list only contains integers and not allowed to cast integers into strings
-to  use str.format() to print integers


4. Replace in a copy
function that replaces an element in a list at a specific position without modifying the original list
-Prototype: def new_in_list(my_list, idx, element):
-If idx is negative, the function should return a copy of the original list and idx is out of range (> of number of element in my_list), the function should return a copy of the original list
-not allowed to import any module and use try/except


5. Can you C me now?
function that removes all characters c and C from a string
-Prototype: def no_c(my_string):
-function should return the new string
-not allowed to import any module and use str.replace()


6. Lists of lists = Matrix
function that prints a matrix of integers
-Prototype: def print_matrix_integer(matrix=[[]]):
-not allowed to import any module and to assume that the list only contains integers
-not allowed to cast integers into strings also to use str.format() to print integers


7. Tuples addition
function that adds 2 tuples.
-Prototype: def add_tuple(tuple_a=(), tuple_b=()):
-Returns a tuple with 2 integers:the first element should be the addition of the first element of each argument and  second element should be the addition of the second element of each argument
-not allowed to import any module and the two tuples will only contain integers
-If a tuple is smaller than 2, the value 0 used for each missing integers or if tuple is bigger than 2, only the first 2 integers used


8. More returns!
function that returns a tuple with the length of a string and its first character.
-Prototype: def multiple_returns(sentence):
-If the sentence is empty, the first character is equal to None
-not allowed to import any module


9. Find the max
function that finds the biggest integer of a list.
-Prototype: def max_integer(my_list=[]):
-If the list is empty, return None and list only contains integers
-not allowed to import any module and not allowed to use the builtin max()


10. Only by 2
function that finds all multiples of 2 in a list.
-Prototype: def divisible_by_2(my_list=[]):
-Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
-new list should have the same size as the original list and not allowed to import any module


11. Delete at
 function that deletes the item at a specific position in a list.
-Prototype: def delete_at(my_list=[], idx=0):
If idx is negative or out of range, nothing change (returns the same list) and  not allowed to use pop(), not importing any module code


12. Switch
source code to switch value of a and b
- program should be exactly 5 lines long


13. Linked list palindrome
function in C that checks if a singly linked list is a palindrome.
-Prototype: int is_palindrome(listint_t **head);
Return: 0 if it is not a palindrome, 1 if it is a palindrome
An empty list is considered a palindrome





                                    TASKS:
              Prototypes for functions written in this project:

| File                               | Prototype                                      |
| ---------------------------------- | ---------------------------------------------- |
| `0-print_list_integer.py`          | `def print_list_integer(my_list=[]):`          |
| `1-element_at.py`                  | `def element_at(my_list, idx):`                |
| `2-replace_in_list.py`             | `def replace_in_list(my_list, idx, element):`  |
| `3-print_reversed_list_integer.py` | `def print_reversed_list_integer(my_list=[]):` |
| `4-new_in_list.py`                 | `def new_in_list(my_list, idx, element):`      |
| `5-no_c.py`                        | `def no_c(my_string):`                         |
| `6-print_matrix_integer.py`        | `def print_matrix_integer(matrix=[[]]):`       |
| `7-add_tuple.py`                   | `def add_tuple(tuple_a=(), tuple_b=()):`       |
| `8-multiple_returns.py`            | `def multiple_returns(sentence):`              |
| `9-max_integer.py`                 | `def max_integer(my_list=[]):`                 |
| `10-divisible_by_2.py`             | `def divisible_by_2(my_list=[]):`              |
| `11-delete_at.py`                  | `def delete_at(my_list=[], idx=0):`            |
| `100-print_python_list_info.c`     | `void print_python_list_info(PyObject *p);`    |

