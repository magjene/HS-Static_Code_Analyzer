"""
Project: Static Code Analyzer
Stage 1/5: Search for long lines


Description
To make sure your Python code is beautiful and consistently formatted, you should follow the PEP8 specification and best practices recommended by the Python community. This is not always easy, especially for beginners. Luckily, there are special tools called static code analyzers (pylint, flake8, and others) that automatically check that your code meets all the standards and recommendations. These tools don't execute your code but just analyze it and output all the issues they find.

In this project, you will create a small static analyzer tool that finds some common stylistic mistakes in Python code. This way, you will familiarize yourself with the concept of static code analysis and improve your Python skills along the way.

PEP8 requires that we should "limit all lines to a maximum of 79 characters", which is designed to make your code more readable. So let's first make a program that checks that code lines are not too long.

Objectives
In this stage, your program should read Python code from a specified file and perform a single check: the length of code lines should not exceed 79 characters.

Note that:

The path to the file is obtained from standard input.
The general output format is:
Line X: Code Message
In the format:

X is the number of the line where the issue was found. The count starts from one.

Code is the code of the discovered stylistic issue (like S001).

Message is a human-readable description of the issue (optional).

For example:

Line 3: S001 Too long
This format will be used throughout the project with some minor changes.

The order of the lines should always be first to last.
Your program can output another message instead of Too long. The rest of the output must exactly match the provided example. In the code S001, S means a stylistic issue, and 001 is the internal number of the issue.
Examples
Here is an example of the file's contents:

print('What\'s your name?')
name = input()
print(f'Hello, {name}')  # here is an obvious comment: this prints a greeting with a name

very_big_number = 11_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
print(very_big_number)
This code contains two long lines (>79 characters): lines 3 and 5.

Here is the expected output for the given example:

Line 3: S001 Too long
Line 5: S001 Too long
"""


def too_long(i, r):
    if len(r) > 79:
        print(f'Line {i}: S001 Too long')


def indentation(i, r):
    if (len(r) - len(r.lstrip(' '))) % 4 != 0:
        print(f'Line {i}: S002 Indentation is not a multiple of four')


def unnecessary_semicolon(i, r):
    if ';' in r:
        if ('#' not in r and "'" not in r) or \
                ('#' not in r and r.find("'") < r.find(';') and not(r.find("'") < r.find(';') < r.rfind("'"))) or \
                ('#' in r and r.find(';') < r.find('#')):
            print(f'Line {i}: S003 Unnecessary semicolon')


def two_spaces_comments(i, r):
    if '#' in r:
        if r.find('#') == 1 or (r.find('#') > 1 and (r[r.find('#') - 1] != ' ' or r[r.find('#') - 2] != ' ')):
            print(f'Line {i}: S004 At least two spaces required before inline comments')


def todo(i, r):
    if '# todo' in r.lower():
        if '# TODO' not in r or r.count('#') > 1 or r.find('#') == 0 or r.find('# TODO') + 5 == len(r) - 1:
            print(f'Line {i}: S005 TODO found')


funcs = [too_long, indentation, unnecessary_semicolon, two_spaces_comments, todo]
# with open(f'{input()}', 'r', encoding='utf-8') as file:
with open(r'D:\pythonProject\Static Code Analyzer\Static Code Analyzer\task\test\test_6.py', 'r', encoding='utf-8') as file:
    count = 0
    for j, row in enumerate(file.read().split('\n'), start=1):
        if row == '':
            count += 1
            continue
        else:
            for fun in funcs:
                fun(j, row)
            if count > 2:
                print(f'Line {j}: S006 More than two blank lines used before this line')
            count = 0
