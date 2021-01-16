#  Python Relational/Comparison Operators
#  These operators compare the values on either sides of them and decide the relation among them.

"""
--------------------------------------------------------------------------------------------
|    Operator    |    Description                                                       |
|       ==       | equals operator check if both sides are same.                        |
|       !=       | not equals operator check if both sides are not same.                |
|       <>       | not equals operator check if both sides are not same. same as !=     | Python3 Does not Support <>
|       >        | if left side value is greater than right.                            |
|       <        | if left side value is lesser than right.                             |
|       >=       | if left side value is greater and equal to the right.                |
|       <=       | if left side value is lesser and equal to the right.                 |
------------------------------------------------------------------------------------------
Lets see some examples below
Assume variable x holds 3 and variable y holds 6,
"""

x = 6
y = 6


print(f"is x equals y ? (x == y)                      {x == y}")
print()
print(f"is x not equals y ? (x != y)                  {x != y}")
print()
#  print(f"is x not equal to y ? (x <> y)             {x <> y}")  # This is not supported by Python3
print(f"is x greater than y ? (x > y)                 {x > y}")
print()
print(f"is x lesser than y ? (x < y)                  {x < y}")
print()
print(f"is x greater and equals to y ? (x >= y)       {x >= y}")
print()
print(f"is x lesser and equals to y ? (x <= y)        {x <= y}")



