"""
Project: Static Code Analyzer
Stage 4/5: Check names according to PEP8


Description
As many coders say, naming is one of the hardest things in programming. Good naming makes your code more readable and uniform. Names should also follow style guides. In Python, the basic requirement is using snake_case for function names and CamelCase for class names. Also, there should be only one space between the construction name and the object name. Checking these rules is the next feature that we need to implement.

Check out the Python tutorial about regular expressions: they will help you implement the checks.

Objectives
In this stage, we need to add three new checks to the program:

[S007] Too many spaces after construction_name (def or class);

[S008] Class name class_name should be written in CamelCase;

[S009] Function name function_name should be written in snake_case.

Note that:

Functions names may start or end with underscores (__fun, __init__).

To simplify the task, we will assume that classes are always written as in the following examples:

# a simple class
class MyClass:
    pass

# a class based on inheritance
class MyClass(AnotherClass):
    pass
In reality, it's possible to declare a class this way:

class \
        S:
    pass
However, since it is not a common way to declare classes, you can ignore it.

Another assumption is that functions are always declared like this:

def do_magic():
    pass
As before:

The program obtains the path to the file or directory via command-line arguments:

> python code_analyzer.py directory-or-file
All the previously implemented checks should continue to work properly.

Examples
Here is an input example:

class  Person:
    pass

class user:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def _print1():
        print('q')

    @staticmethod
    def Print2():
        print('q')
The expected output for this code is:

/path/to/file/script.py: Line 1: S007 Too many spaces after 'class'
/path/to/file/script.py: Line 4: S008 Class name 'user' should use CamelCase
/path/to/file/script.py: Line 15: S009 Function name 'Print2' should use snake_case
"""


import os
import sys
import re


def too_long(i, r, e):
    if len(r) > 79:
        print(f'{e}: Line {i}: S001 Too long')


def indentation(i, r, e):
    if (len(r) - len(r.lstrip(' '))) % 4 != 0:
        print(f'{e}: Line {i}: S002 Indentation is not a multiple of four')


def unnecessary_semicolon(i, r, e):
    if (r[:r.find('#')] if '#' in r else r).strip().endswith(';'):
        print(f'{e}: Line {i}: S003 Unnecessary semicolon')


def two_spaces_comments(i, r, e):
    if '#' in r and not r.startswith('#') and '  #' not in r:
        print(f'{e}: Line {i}: S004 At least two spaces required before inline comments')


def todo(i, r, e):
    if '#' in r and r.find('#') < r.lower().find('todo'):
        print(f'{e}: Line {i}: S005 TODO found')


def spaces_def_class(i, r, e):
    if re.match(' *def  ', r) or re.match('class  ', r):
        print(f"{e}: Line {i}: S007 Too many spaces after '{'def' if re.match('def', r) else 'class'}'")


def class_name(i, r, e):
    if re.match('class [a-z]', r) or re.match('class .*_.*', r):
        print(f"{e}: Line {i}: S008 Class name 'user' should use CamelCase")


def def_name(i, r, e):
    ...
        # print(f'{e}: Line {i}: S009 Function name 'Print2' should use snake_case')


def open_file(f_path, f_name):
    with open(f_path + f_name, 'r', encoding='utf-8') as file:
        count = 0
        for j, row in enumerate(file.read().splitlines(), start=1):
            if row == '':
                count += 1
            else:
                for fun in funcs:
                    fun(j, row, f'{f_path}{f_name}')
                if count > 2:
                    print(f'{f_path}{f_name}: Line {j}: S006 More than two blank lines used before this line')
                count = 0


funcs = [too_long, indentation, unnecessary_semicolon, two_spaces_comments, todo,
         spaces_def_class, class_name, def_name]
path = ' '.join(sys.argv[1:])
if os.path.isdir(path):
    with os.scandir(path) as entr:
        for entry in entr:
            if entry.is_file() and entry.name.endswith('.py'):
                open_file(path + '\\', entry.name)
else:
    open_file('', path)
