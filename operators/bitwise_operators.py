"""
Python Bitwise Operators
-----------------------------------------------------------------
|   Operator        |   Example     |   Operator name           |
|-------------------|---------------|---------------------------|
|       &           |   x = x & y   |  Bitwise AND              |
|       |           |   x = x | y   |  Bitwise OR               |
|       ~           |   x = x ~ y   |  Binary Ones Complement   |
|       ^           |   x = x ^ y   |  Bitwise XOR              |
|       >>          |   x = x>>y    |  Bitwise right shift      |
|       <<          |   x = x<<y    |  Bitwise left shift       |
-----------------------------------------------------------------
"""

print(bin(90))  # To find the binary value use bin(value)

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
#  print(bin(z))
print("Bitwise AND - Value of z is ", z)

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
#  print(bin(z))
print("Bitwise OR -                  Value of z is ", z)

# x = 90 = 0101 1010
# ~x = -91 = 0101 1011
z = ~x           # -91 = 0101 1011
#  print(bin(z))
print("Binary Ones Complement -      Value of z is ", z)

z = x ^ y        # 86 = 0101 0110
#  print(bin(z))
print("Bitwise XOR -                 Value of z is ", z)

z = x >> 2       # 22 = 0001 0110
#  print(bin(z))
print("Bitwise right shift           Value of z is ", z)

z = x << 2       # 360 = 0001 0110 1000
#  print(bin(z))
print("Bitwise Left shift            Value of z is ", z)


