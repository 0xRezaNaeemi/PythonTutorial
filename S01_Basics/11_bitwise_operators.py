"""
Operator   Name    Descriptions
&          AND     Sets each bit to 1 if both bits are 1
|          OR      Sets each bit to 1 if one of two bits is 1
^          XOR     Sets each bit to 1 if only one of two bits is 1
~          NOT     Inverts all the bits
<<   Zero fill left shift.
                   Shift left by pushing zeros in from of the right
                    and left the leftmost bits fall off
>>   Signed right shift.
                   Shift right by pushing copies of the leftmost bit in
                    from the left, and let the rightmost bits fall off
"""

x, y = 16, 4
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x >> 1)  # x // 2 ** 1
print(x // 2 ** 1)
print(x << 3)  # x * 2 **3
print(x * 2 ** 3)
