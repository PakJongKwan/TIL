Binary Number
=============

Negative Binary Number
----------------------

In Digital System, how **Binary Number** express **Negative Number** is using **most significant bit(MSB)** by sign bit to distinguish between positive and negative numbers.  
 Here is **three ways** to how **Binary Number** express **Negative Number** .

● Sign-Magnitude

● 1's Complement

● 2's Complement

---

### Sign-Magnitude

> Using **most significant bit(MSB)** by sign bit to distinguish between positive and negative numbers.

| Binary Number | Integers |
|---------------|----------|
| 0000          | +0       |
| 0001          | +1       |
| 1000          | -0       |
| 1001          | -1       |

**Sign-Magnitude** is a most simple method to divide positive and negative numbers . If MSB is **0**, number is positive, If MSB is **1**, number is negative. and remaining values are expressed as **absolute values**.

### Weakness

---

**Sign-Magnitude** is the simplest way, but it has some big problems.

● -0 and +0 occur

● Errors in arithmetic calculations

**Sign-Magnitude** has to divide sign and absolute values to calculation. If you want to addtion negative numbers, it cant implements Subtraction calculator, So **Errors in arithmetic calculations** is occur.

**0000 0010** = **+2**  
 **1000 0010** = **-2**  
\---------------------  
 **1000 0100** = **-4**

---

### 1's Complement

> To express negative numbers, reversal **Sign-Magnitude**'s positive numbers.

| Binary Number | Integers |
|---------------|----------|
| 0000          | +0       |
| 0001          | +1       |
| 1111          | -0       |
| 1110          | -1       |

**1's Complement** is a method that invert a bit, its sign is reversed

**2 = 0010 >> 1101 = -2**

This **"bit reversal"** resolves errors in previous arithmetic calculations.

**0000 0010** = **+2**  
**1111 1101** = **-2**  
\---------------------  
 **1111 1111** = **-0**

Carry Occur) Adds the generated carry to the least significant bit.

**0000 1001** = **+9**  
 **1111 1010** = **-5**  
 \------------------------  
 **(1)0000 0011** = **+3**  
 \------------------------  
 **0000 0100** = **+4**

### Weakness

---

**1's Complement** resolves errors in arithmetic calculations, but it cant resolves occur error in -0 and +0.

● Occur +0 and -0

● Occur carry, uncomfortable calculations

**2 – 2** = **0010** + **1101** = **1111** >> **0000** = **-0** = **+0**

---

### 2's Complement

> resolves all problems. Invert the bit and add 1 to the least significant bit

resolves **1's Complement**'s problems that exist -0 and +0.

**0000 -> 0**  
**1111 -> 8**

Also resolves problems that carry is occur, uncomfortable calculations by add 1 to the least significant bit.

**2 + 3 = 0010 + 001 = 0101 = 5**  
**(-2) + (-3) = 1110 + 1101 = 1011 = -5**
