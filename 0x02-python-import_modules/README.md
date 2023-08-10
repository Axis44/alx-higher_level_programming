0x02. Python - import & modules TASKS


0. Import a simple function from a simple file
program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
-print function with string format to display integers used.
- assign:
the value 1 to a variable called a
the value 2 to a variable called b
two variables used as arguments when calling the functions add and print
a and b must be defined in 2 different lines: a = 1 and another b = 2
-program to print: <a value> + <b value> = <add(a, b) value> followed with a new line
- word add_0 used once
- not allowed to use * for importing or __import__
-code should not be executed when imported - by using __import__


1. My first toolbox!
-program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
-function print (with string format to display integers) more than 4 times not used
- define:
the value 10 to a variable a
the value 5 to a variable b
and use those two variables only, as arguments when calling functions (including print)
-a and b must be defined in 2 different lines: a = 10 and another b = 5
-program should call each of the imported functions
-he word calculator_1 should be used only once 
-not allowed to use * for importing or __import__
-code should not be executed when imported


2. How to make a script dynamic!
 program that prints the number of and the list of its arguments.
-output should be:
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
-code should not be executed when imported
-The number of elements of argv can be retrieved by using: len(argv)


3. Infinite addition
program that prints the result of the addition of all arguments
-The output should be the result of the addition of all arguments, followed by a new line
-cast arguments into integers by using int()
-code should not be executed when imported
-program should also handle big numbers.



4. Who are you?
program that prints all the names defined by the compiled module hidden_4.pyc
- print one name per line, in alpha order
- print only names that do not start with __
- code should not be executed when imported




5. Everything can be imported
-program that imports the variable a from the file variable_load_5.py and prints its value.
-not allowed to use * for importing or __import__
code should not be executed when imported
