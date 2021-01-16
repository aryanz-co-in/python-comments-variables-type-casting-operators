"""
Python Bitwise Operators
------------------------------------------------------------
|   Operator        |   Example     |   Operator name      |
|-------------------|---------------|----------------------|
|       &           |   x = x & y   |  Bitwise AND         |
|       |           |   x = x | y   |  Bitwise OR          |
|       ~           |   x = x ~ y   |  Bitwise NAND        |
|       ^           |   x = x ^ y   |  Bitwise XOR         |
|       >>          |   x = x>>y    |  Bitwise right shift |
|       <<          |   x = x<<y    |  Bitwise left shift  |
------------------------------------------------------------
"""

print(bin(0))  # To find the binary value use bin(value)

x = 90            # 90 = 0101 1010
y = 12            # 12 = 0000 1100
z = 0             # 0  = 0000 0000

# AND Table
# |--X---|---Y---|---Z---|
# |  0   |   0   |   0   |
# |  0   |   1   |   0   |
# |  1   |   0   |   0   |
# |  1   |   1   |   1   |
# ------------------------

# x = 90 = 0101 1010
# y = 12 = 0000 1100
# ------------------
# z =  8 = 0000 1000
z = x & y        # 8 = 0000 1000
print(bin(z))
print("Bitwise AND - Value of c is ", z)

# OR Table
# |--X---|---Y---|---Z---|
# |  0   |   0   |   0   |
# |  0   |   1   |   1   |
# |  1   |   0   |   1   |
# |  1   |   1   |   1   |
# ------------------------

# x = 90 = 0101 1010
# y = 12 = 0000 1100
# ------------------
# z = 94 = 0101 1110
z = x | y        # 94 = 0101 1110
print(bin(z))
print("Bitwise OR - Value of c is ", z)

z = ~x           # -61 = 1100 0011
print("Bitwise NAND - Value of c is ", z)

z = x ^ y        # 49 = 0011 0001
print("Bitwise XOR - Value of c is ", z)

z = x >> 2       # 15 = 0000 1111
print("Bitwise right shift Value of c is ", z)

z = x << 2       # 240 = 1111 0000
print("Bitwise Left shift Value of c is ", z)


