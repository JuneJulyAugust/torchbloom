# Converting Between Binary and Hexadecimal Integers

Source: https://www.mathacademy.com/topics/2891?courseId=109
Topic ID: 2891

## Prerequisites

- [Hexadecimal Integers](./2984-hexadecimal-integers.md)
- [Binary Integers](./3363-binary-integers.md)

## Lesson

### Introduction

Hexadecimal integers can be converted into binary and vice versa without converting to decimal first.

To write a hexadecimal integer as the corresponding binary number, we convert each digit of the hexadecimal number into a $4$-digit binary (with leading zeros if necessary) and **concatenate** the results.

For example, consider the following hexadecimal integer:

$$



{\color{SandyBrown}3}\,{\color{Purple}\textrm{B}}\,{\color{SteelBlue}7}.



$$

First, we convert each digit into binary.

Then, we combine (concatenate) the results:

$$



({\color{SandyBrown}0011} \: {\color{Purple}1011} \: {\color{SteelBlue}0111} )_2



$$

Therefore,

$$



(3\textrm{B}7)_{16} = (0011 \: 1011 \: 0111 )_2 = (11 \: 1011 \: 0111 )_2.



$$

Similarly, to write a binary number as the corresponding hexadecimal integer, we split it into groups of $4$ digits (starting from the right) and convert each group separately.

For example, consider the following binary number:

$$



({\color{SandyBrown}11} \: {\color{Purple}1011} \: {\color{SteelBlue}0111} )_2



$$

To convert this to hexadecimal, we first split it into groups of four digits with leading zeroes.

Thus, by concatenating these hexadecimal digits, we get

$$



({\color{SandyBrown}3}\,{\color{Purple}\textrm{B}}\,{\color{SteelBlue}7})_{16}.



$$

Therefore,

$$



(11 \: 1011 \: 0111 )_2 = (3\textrm{B}7)_{16}.



$$

### Conversion Table

The table below gives the conversions between binary and hexadecimal for the decimal integers from zero to fifteen.

### Example: Converting a Hexadecimal Integer to Binary

#### Question

What is $(\textrm{FE}9)_{16}$ written in base $2?$

#### Explanation

Recall that the hexadecimal integers $\textrm{A}-\textrm{F}$ correspond to decimal integers $10-15{:}$

To write a hexadecimal integer as the corresponding binary number, we convert each digit of the hexadecimal number into a $4$-digit binary (with leading zeros if necessary) and concatenate the results.

- Converting each digit of $(\textrm{FE}9)_{16}$ into binary, we obtain:

- Concatenating the results, we get

### Example: Converting a Binary Integer to Hexadecimal

#### Question

What is $(100 \: 1101)_2$ written in base $16?$

#### Explanation

Recall that the hexadecimal integers $\textrm{A}-\textrm{F}$ correspond to decimal integers $10-15{:}$

To write a binary integer as the corresponding hexadecimal number, we split it from right to left into blocks containing precisely four digits. Then, we write each block using the corresponding hexadecimal digit.

First, let's add the leading zero to get four-digit blocks:

$$



(100 \: 1101)_2 = (0100 \: 1101)_2



$$

Converting each four-digit block into a hexadecimal integer, we obtain:

$$



\begin{aligned}(0100)_{2} & =2^{2}=4 \\ (1101)_{2} & =2^{3}+2^{2}+2^{0}=13=D\end{aligned}



$$

Therefore, we get

$$



(100 \: 1101 )_2 = (4\textrm{D})_{16}.



$$
