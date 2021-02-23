#Níže máš slovník, který obsahuje kódy balíků s informací, zda již byl balík předán kurýrovi
# k doručení. Pokud byl předán, má hodnotu True, v opačném případě má hodnotu False.

#Napiš program pro operátora společnosti, který poskytuje informaci, zda byl balík předán kurýrovi.
# Nejprve se uživatele zeptej na kód balíku. Následně podle hodnoty ve slovníku vypiš větu
# Balík byl předán kurýrovi nebo Balík zatím nebyl předán kurýrovi.

"""
Boolean expressions
x < y
x == y
x > y
x <= y
x >= y
x != y
...
x = None
if x:
    print("this will never be reached")
"""


"""
Basic PL theory

Statements
Building blocks of programming language.
Executed by Python as instructions.
Example:
- Assignment
>>> x = 8
Statements don't return anything, and not evaluated. They are executed!


Expressions
Pieces of code that are evaluated into some value.
Example:
>>> 1
1
^ expression 1 was evaluated into number 1
when python "sees" 1 as text of your program, it needs to translate it into an internal representation of 1.
1 as text gets evaluated(!) into 1 inside the Python interpreter. Then CPU gets to work with 1 as bits.
Program text are not bits! It's text.
Example:
Assume x = 8 was already executed
Below is an expression - x is a variable. Pythoh evaluates a variable.
When Python evaluates an expression, the end result is alway some value.
>>> x
8  # x was evaluated to 8


List- open and can be chaged comapred to Tuple
>>> l = ['a', 'b', 'c']
>>> l[0]
'a'
>>> l[3]
IndexError: ...
>>> l[0] = 1  # this is an assignment statement, not an expression! It doesn't return anything
>>> l
[1, 'b', 'c']
>>> l.append(7)
>>> l
[1, 'b', 'c', 7]

Dictionary - collection of key value pairs
Like a table of contents - you know the chapter, you get the page number
>>> d = {'a': 1, 'b': 2}
>>> d['a']
1
>>> d.get('a')
1
>>> d['c']
KeyError: ...
>>> d.get('c')
None

Tuple- definitely defined/not possible to change
Collection of random objects
- Ordered
- Immutable: can't be modified
>>> t = ('a', 8, 9)
>>> t[0]
'a'
>>> t[1]
8
>>> t[3]
IndexError: ...
>>> len(t)
3
>>> t[0] = 'b'
TypeError: ... -- can't modify a tuple!
"""

baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
code = input("What is the package code?")
if code in baliky:
    if baliky[code] == True:
        print("The package is with curier")
    else:
        print("The package has not been delivered to currier yet")

"""
>>> baliky = {'a': 1}
>>> code = 'a'
What python interpreter does:
>>> baliky[code]
1. evaluate `baliky[code]`. This expression in turn has two internal exressions.
2. evaluate `baliky` -> evaluates to {'a': 1}
3. `code` is a second expression, evaluates to 'a'
4. now python can evaluate `{'a': 1}['a']` -> evaluates to 1
"""