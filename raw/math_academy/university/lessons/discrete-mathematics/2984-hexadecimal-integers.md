# Hexadecimal Integers

Source: https://www.mathacademy.com/topics/2984?courseId=109
Topic ID: 2984

## Prerequisites

- [The Division Algorithm](../methods-of-proof/2689-the-division-algorithm.md)

## Lesson

### Introduction

The **hexadecimal number system** represents numbers using a base of $16.$ In other words, it uses sixteen separate digits to write numbers.

The first ten digits are the same as those in the decimal number system, while the values from $10$ to $15$ are represented by the first six letters of the English alphabet.

The decimal numbers $0$ to $15$ and their hexadecimal equivalents are shown in the table below.

To avoid ambiguity, we usually use subscripts to denote the bases when writing numbers in different bases. For example:

$$



(9)_{16} = (9)_{10}, \qquad (\textrm B)_{16} = (11)_{10}



$$

When counting numbers in a hexadecimal system, we use the same place value rules as in a decimal system. However, instead of having place values of $10^0$ (ones), $10^1$ (tens), $10^2$ (hundreds), etc, we have $16^0$ (ones), $16^1$ (sixteens), $16^2, \ldots.$

For example, when we reach $\text{F}\ (=15),$ writing the next number in the sequence involves placing a $0$ in the ones place and $1$ in the sixteens place. Therefore,

$$



(16)_{10} = (10)_{16}



$$

The next sixteen numbers after $\textrm F$ are written as follows:

The integers from $0$ to $100$ are written in the hexadecimal system as follows:

$$



\begin{aligned}0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & A & B & C & D & E & F \\ 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 1A & 1B & 1C & 1D & 1E & 1F \\ 20 & 21 & 22 & 23 & 24 & 25 & 26 & 27 & 28 & 29 & 2A & 2B & 2C & 2D & 2E & 2F \\ 30 & 31 & 32 & 33 & 34 & 35 & 36 & 37 & 38 & 39 & 3A & 3B & 3C & 3D & 3E & 3F \\ 40 & 41 & 42 & 43 & 44 & 45 & 46 & 47 & 48 & 49 & 4A & 4B & 4C & 4D & 4E & 4F \\ 50 & 51 & 52 & 53 & 54 & 55 & 56 & 57 & 58 & 59 & 5A & 5B & 5C & 5D & 5E & 5F \\ 60 & 61 & 62 & 63 & 64 & & & & & & & & & & & \end{aligned}



$$

Notice that the hexadecimal number $(64)_{16}$ is *not* equal to $(64)_{10}$, even though it is composed of the same digits. Instead, $(64)_{16}$=$(100)_{10}.$

Due to their compact representation of binary data, hexadecimal numbers are widely used in computing and digital systems. They are commonly used in programming, memory addressing in computer architecture, and encoding error messages in debugging. Additionally, hexadecimal numbers are essential in cryptography, where encryption keys and hash values are often represented in hexadecimal for efficiency and readability.

### Converting From Hexadecimal to Decimal

To convert a hexadecimal number to a decimal number, we expand it using the same method as decimal numbers. However, instead of using powers of $10,$ we use powers of $16.$

For example, consider the following hexadecimal integer:

$$



{\color{SandyBrown}1}\,{\color{Purple}\text{C}}\,{\color{SteelBlue}\text{A}}



$$

The powers of $16$ that correspond to the digits of this number are:

Hence, $(1\textrm C \textrm A)_{16}$ expands as follows:

$$



\begin{aligned}(1CA)_{16} & =1⋅16^{2}+\overset{12}{C}⋅16^{1}+\overset{10}{A}⋅16^{0} \\ & =256+192+10 \\ & =(458)_{10}\end{aligned}



$$

Therefore, $1\textrm C \textrm A$ base $16$ is equal to $458$ base $10.$

Converting decimal integers to hexadecimal integers will be discussed in the next section.

### Example: Converting a Hexadecimal Integer to a Decimal Integer

#### Question

What is $(27\text{F})_{16}$ written in base $10?$

#### Explanation

Recall that the hexadecimal integers $\text{A}-\text{F}$ correspond to decimal integers $10-15{:}$

We can write down the given hexadecimal integer using a place value chart:

Therefore, our number in base $10$ can be written as follows:

$$



\begin{aligned}(27F)_{16} & =2⋅16^{2}+7⋅16^{1}+15⋅16^{0} \\ & =512+112+15 \\ & =(639)_{10}\end{aligned}



$$

### Converting From Decimal to Hexadecimal

To convert a decimal integer $N$ to a hexadecimal integer, we follow two steps:

- First, we expand $N$ using powers of $16{:}$

- Then, we write all the coefficients $a_i$ using hexadecimal digits $0,1,...,9,\text{A},...,\text{F}.$

Let's write the following decimal integer in base $16{:}$

$$



(1000)_{10}



$$

First, we must write this number as a sum of powers of $16.$ Note that in base $10,$ we have

$$



16^3 > 1000 \quad \text{and}\quad 16^2 < 1000.



$$

Moreover, the quotient when $16^2$ divides $1000$ equals $3,$ and the remainder is $232.$ Thus

$$



1000 = 3 \cdot 16^2 + 232.



$$

We must now expand the remainder $232$ similarly.

The quotient when $16^1$ divides $232$ equals $14,$ and the remainder is $8.$ Thus, we can write

$$



1000 = 3 \cdot 16^2 + 14 \cdot 16^1 + 8



$$

So, the full expansion of $(1000)_{10}$ is powers of $16$ is

$$



(1000)_{10} = {\color{SandyBrown}3} \cdot 16^2 + {\color{Purple}14} \cdot 16^1 + {\color{SteelBlue}8} \cdot 16^0.



$$

Finally, write the coefficients above using hexadecimal digits as follows:

Therefore, we conclude that

$$



(1000)_{10} = (3\text{E}8)_{16}.



$$

### Example: Converting an Expanded Decimal Integer to a Hexadecimal Integer

#### Question

What is $(15 \cdot 16^{4} + 2 \cdot 16^{1} + 1)_{10}$ written in base $16?$

#### Explanation

Recall that the hexadecimal integers $\text{A}-\text{F}$ correspond to decimal integers $10-15{:}$

First, we rewrite our decimal integer as follows:

$$



\begin{aligned}15⋅16^{4}+2⋅16^{1}+1=15⋅16^{4}+0⋅16^{3}+0⋅16^{2}+2⋅16^{1}+1⋅16^{0}\end{aligned}



$$

The corresponding place value chart is given below:

Therefore, $(15 \cdot 16^{4} + 2 \cdot 16^{1} + 1)_{10} = (\text{F}0021)_{16}.$

### Example: Converting a Decimal Integer to a Hexadecimal Integer

#### Question

What is $(1\,500)_{10}$ written in base $16?$

#### Explanation

Recall that the hexadecimal integers $\text{A}-\text{F}$ correspond to decimal integers $10-15{:}$

We extract the powers of $16$ from the integer (starting from the largest possible one):

$$



\begin{aligned}1\,500 & =5⋅16^{2}+220 \\ & =5⋅16^{2}+13⋅16^{1}+12 \\ & =5⋅16^{2}+13⋅16^{1}+12⋅16^{0}\end{aligned}



$$

The corresponding place value chart is given below:

Therefore, $(1\,500)_{10} = (5\text{DC})_{16}.$
