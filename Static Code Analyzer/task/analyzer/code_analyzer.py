"""
Project: Static Code Analyzer
Stage 3/5: Analyze multi-file projects


Description
As a rule, real projects contain more than a single file. Also, project directories often contain not only Python files, and we don't need to check if an HTML file follows PEP8.

We recommend that you check out a tutorial on realpython.com that can help you to work with files and directories.

Objectives
In this stage, you need to improve your program so that it can analyze all Python files inside a specified directory.

Please note that:

You also need to change the input format. Instead of reading the path from the standard input, the program must obtain it as a command-line argument:

> python code_analyzer.py directory-or-file
The output format also needs to be changed slightly. It should include the path to the analyzed file:

Path: Line X: Code Message 
All output lines must be sorted in ascending order according to the file name, line number, and issue code.

Non-Python files must be skipped.

Once again:

It is important that all the checks implemented in the previous stages continue to work properly.

If a line contains the same stylistic issue several times, your program must print the information only once. If a line has several issues with different types of error codes, they should be printed in ascending order.

To simplify the solution, we consider it acceptable if your program finds some false-positive stylistic issues in strings, especially in multi-lines ('''...''' and ).

We recommend that you break your program code into a set of functions and classes to avoid confusion.

Examples
Only a single file is specified as the input:

> python code_analyzer.py /path/to/file/script.py
/path/to/file/script.py: Line 1: S004 At least two spaces required before inline comments
/path/to/file/script.py: Line 2: S003 Unnecessary semicolon
/path/to/file/script.py: Line 3: S001 Too long line
/path/to/file/script.py: Line 3: S003 Unnecessary semicolon
/path/to/file/script.py: Line 6: S001 Too long line
/path/to/file/script.py: Line 11: S006 More than two blank lines used before this line
/path/to/file/script.py: Line 13: S003 Unnecessary semicolon
/path/to/file/script.py: Line 13: S004 At least two spaces required before inline comments
/path/to/file/script.py: Line 13: S005 TODO found
The input path is a directory; the output should contain all Python files from it:

> python code_analyzer.py /path/to/project
/path/to/project/__init__.py: Line 1: S001 Too long line
/path/to/project/script1.py: Line 1: S004 At least two spaces required before inline comments
/path/to/project/script1.py: Line 2: S003 Unnecessary semicolon
/path/to/project/script2.py: Line 1: S004 At least two spaces required before inline comments
/path/to/project/script2.py: Line 3: S001 Too long line
/path/to/project/somedir/script.py: Line 3: S001 Too long line
/path/to/project/test.py: Line 3: Line 13: S003 Unnecessary semicolon
"""


import os
import sys


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


funcs = [too_long, indentation, unnecessary_semicolon, two_spaces_comments, todo]
path = ' '.join(sys.argv[1:])
if os.path.isdir(path):
    with os.scandir(path) as entr:
        for entry in entr:
            if entry.is_file() and entry.name.endswith('.py'):
                open_file(path + '\\', entry.name)
else:
    open_file('', path)
