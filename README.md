# Learn Python
Learn Python in Tamil - https://www.youtube.com/channel/UCXFGGATa3Q2UF-6vKyLB2Zg/

Description
-------------------------------------------
This project contains demo code and example for the following topics.

1. Python Comments
   1. Single line comment
   2. End of the line comment
   3. Multi line comment using #
   4. Multi line comment using """ (3 double quotes)
2. Variables 
   1. Assign multiple values to variable
   2. Local & Global variables 
   3. Assign None - nullify variable
3. Type cast
   1. Casting to int
   2. Casting to float
   3. Casting to str
4. Operators
   1. Arithmetic Operators
   2. Comparison (Relational) Operators
   3. Assignment Operators
   4. Logical Operators
   5. Bitwise Operators
   6. Membership Operators
   7. Identity Operators

---------------------------------------------

## Python Comments

### Comments where and how is it used?

Well to answer for it, Comments are used for many reasons, lets see what are those below.


1. Documentation using comments - It helps anyone who is reading the code along with the comments can easily understand what is the code used for and how it works. (Logical and Functional explanation).
2. Skip code execution while debugging - Certain times you might want partial code not to be executed. mostly this will be used for debugging your code, if the code is not working as expected and to find the line which cause the bug.

### How to comment and what are all the ways we can comment in Python?

we can comment in Python using the following ways.

1. Single line comments
2. End of the line comments 
3. Multi line comments using #(Pound or Sharp)
4. Multi line comments using """ (3 double quotes a.k.a Multi line string)


## Single line comments

Single line comments are nothing but writing your comment in one single line.

These lines are prefixed using #(Pound or Sharp).


```
# This is Single line comment 
# Sample program to print hello world.
print("Hello, World") 

# End of my python program
```

## End of the line comments

End of line comments, as name says it is written at end of the line along with the Python code.

**_Lets see an example below_**

```
amt1 = 4
amt2 = 5 
final_amt = amt1 + amt2 # Adding amt1 and amt2.
```
In the above example, we perform some logic and by writing end of the line comment, we tell what is happening in that line.



## Multi line comments using \#

Multi line comments using #, it is same as Single line comment but it is written in multiple lines prefixed with the #(Pound or Sharp). symbol.
Mostly this multi line comments is used for documentation, and it is written on top of class file or above the function.

**_Lets see an example below_**

```
#  Author: aryanz.co.in
#  Class name: calculator
#  Description: This class is used for performing add, sub, multiply and divide. each action requires two parameters.


#  Add operation
#  Two parameters x and y
#  prints the result on the screen 

def add(x, y)
   print(x + y)
```

## Multi line comments using """

Multi line comments using """, it is same as Multi line comment using # but it is prefixed with the """(3 double quotes).

This multi line comments is also used for documentation, and it is written on top of class file or above the function.

Lets see an example below

```
"""       
Author: aryanz.co.in  
Class name: calculator  
Description:  This class is used for performing add, sub, multiply and divide. each action requires two parameters.
"""
  
"""
Add operation  
Two parameters x and y  prints the result on the screen 
"""

def add(x, y)
   print(x + y)
```

-------------------------------------------------------
End of Comments
-------------------------------------------------------

# What is a variable?

Variables, a placeholder or container or a memory location to store values of any type, such as string, int, float, list and etc.,

1. Variable is a container for storing data/values.
2. Values are assigned at the beginning of the program.
3. It does not need to be declared with any particular type.
4. Type can be changed at any time, after they have been initialised at the beginning. (x = 5, after few line of code assign x = “Hello”, it is possible in Python)
5. Before assigning values to variables, it can be type cast to specific type. (x = str(4))
6. Most importantly variables are case-sensitive.(Msg = “Hello” and msg = “Hello” both are different variables)


---------------------------------------------
``` 
Powered by www.aryanz.co.in
```