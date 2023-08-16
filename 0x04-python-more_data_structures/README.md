0x04. Python - More Data Structures: Set, Dictionary

0. Squared simple
function that computes the square value of all integers of a matrix
-matrix is a 2 dimensional array which returns a new matrix: Same size as matrix and each value is square of the value of the input
-Initial matrix is not modified, not allowed to import any module
-no regular loops used

1. Search and replace
function that replaces all occurrences of an element by another in a new list
-my_list is the initial list, search is the element to replace in the list and replace is the new element
-not allowed to import any module

2. Unique addition
function that adds all unique integers in a list (only once for each integer).
- not allowed to import any module

3. Present in both
function that returns a set of common elements in two sets.
- not allowed to import any module

4. Only differents
function that returns a set of all elements present in only one set.
-not allowed to import any module

5. Number of keys
function that returns the number of keys in a dictionary.
-not allowed to import any module

6. Print sorted dictionary
function that prints a dictionary by ordered keys.
- all keys are strings and keys are sorted by alphabetic order
-Only sort keys of the first level, Dictionary values have any type
 not allowed to import any module

7. Update dictionary
 function that replaces or adds key/value in a dictionary.
-key argument will be always a string and value argument will be any type
- key exists in the dictionary, the value will be replaced and If a key doesn’t exist in the dictionary, it will be created
-not allowed to import any module

8. Simple delete by key
 function that deletes a key in a dictionary.
-key argument will be always a string and if a key doesn’t exist, the dictionary won’t change
-not allowed to import any module

9. Multiply by 2
 function that returns a new dictionary with all values multiplied by 2
- assume that all values are only integers and returns a new dictionary
-not allowed to import any module

10. Best score
function that returns a key with the biggest integer value.
- assume that all values are only integers and if no score found, return None
-all students have a different score, not allowed to import any module

11. Multiply by using map
function that returns a list with all values multiplied by a number without using any loops.
-Returns a new list: same length as my_list and each value should be multiplied by number
-nitial list should not be modified, not allowed to import any module
- used map,

12. Roman to Integer
function def roman_to_int(roman_string): that converts a Roman numeral to an integer.
-You can assume the number will be between 1 to 3999.
def roman_to_int(roman_string) must return an integer
If the roman_string is not a string or None, return 0




                            TASKS: PROTOTYPES


| File                           | Prototype                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `0-square_matrix_simple.py`    | `def square_matrix_simple(matrix=[]):`                                                                    |
| `1-search_replace.py`          | `def search_replace(my_list, search, replace):`                                                           |
| `2-uniq_add.py`                | `def uniq_add(my_list=[]):`                                                                               |
| `3-common_elements.py`         | `def common_elements(set_1, set_2):`                                                                      |
| `4-only_diff_elements.py`      | `def only_diff_elements(set_1, set_2):`                                                                   |
| `5-number_keys.py`             | `def number_keys(a_dictionary):`                                                                          |
| `6-print_sorted_dictionary.py` | `def print_sorted_dictionary(a_dictionary):`                                                              |
| `7-update_dictionary.py`       | `def update_dictionary(a_dictionary, key, value):`                                                        |
| `8-simple_delete.py`           | `def simple_delete(a_dictionary, key=""):`                                                                |
| `9-multiply_by_2.py`           | `def multiply_by_2(a_dictionary):`                                                                        |
| `10-best_score.py`             | `def best_score(a_dictionary):`                                                                           |
| `11-mutiply_list_map.py`       | `def mutiply_list_map(my_list=[], number=0):`                                                             |
| `12-roman_to_int.py`           | `def roman_to_int(roman_string):`                                                                         |
| `100-weight_average.py`        | `def weight_average(my_list=[]):`                                                                         |
| `101-square_matrix_map.py`     | `def square_matrix_map(matrix=[]):`                                                                       |

