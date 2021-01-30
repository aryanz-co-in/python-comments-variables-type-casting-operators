#  Logical Operators
#  It used on combine conditional statements

"""
------------------------------------------------------------------------------------------
|   Operator    |                    Description                    |   Example            |
|---------------|---------------------------------------------------|----------------------|
|     and       | Returns True if both statements are true          |  x < 5 and  x < 10   |
|     or        | Returns True if one statements is true            |  x < 5 or  x < 10    |
|     not       | Returns False if the result is true or vice-versa |not(x < 5 and x < 10) |
|------------------------------------------------------------------------------------------|
"""


x = 2
y = 5
z = 10

value_and = ((x < y) and (x < z))      # and logical operator

value_or = ((x < y) or (x < z))        # or logical operator

value_not = not((x < y) and (x < z))   # not logical operator

print(f"value_and = ({x} < {y} and {x} < {z}) = {value_and}")

print(f"value_or = ({x} < {y} or {x} < {z}) = {value_or}")

print(f"value_not = not({x} < {y} and {x} < {z}) = {value_not}")
