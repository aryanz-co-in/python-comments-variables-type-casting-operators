"""
Python Assignment Operators
Assignment operators are used to assign values to variables:
---------------------------------------------------------
|   Operator        |   Example     |       Similar to  |
|-------------------|---------------|-------------------|
|       =           |   x = 5       |       x = 5       |   Assign value from right to left side
|       +=          |   x += 5      |       x = x + 5   |   It adds right & left operand and assign to left side
|       -=          |   x -= 5      |       x = x - 5   |   It subtracts right & left operand and assign to left side
|       *=          |   x *= 5      |       x = x * 5   |   It multiplies right & left operand and assign to left side
|       /=          |   x /= 5      |       x = x / 5   |   It divides left with right operand and assign to left side
|       %=          |   x %= 5      |       x = x % 5   |   It takes modulo using two operand and assign to left
|       //=         |   x //= 5     |       x = x // 5  |   It performs floor division on operands and assign to left
|       **=         |   x **= 5     |       x = x ** 5  |   It performs exponential (power) calc on operands & assign to left
|       &=          |   x &= 5      |       x = x & 5   |   Bitwise AND
|       |=          |   x |= 5      |       x = x | 5   |   Bitwise OR
|       ^=          |   x ^= 5      |       x = x ^ 5   |   Bitwise XOR
|       >>=         |   x >>= 5     |       x = x >> 5  |   Bitwise right shift
|       <<=         |   x <<= 5     |       x = x << 5  |   Bitwise left shift
----------------------------------------------------------
"""
x = 10
x = ~4
print(~x)
