# Integers in Arbitrary Bases

Source: https://www.mathacademy.com/topics/2889?courseId=109
Topic ID: 2889

## Prerequisites

- [The Division Algorithm](../methods-of-proof/2689-the-division-algorithm.md)
- [Binary Integers](./3363-binary-integers.md)

## Lesson

### Introduction

In a previous lesson, we learned how to express integers using the *binary system* of numbers, where each integer is represented as a string containing only the digits $0$ and $1.$

Each binary integer has an equivalent decimal representation and vice-versa. We can find an equivalent decimal representation of a binary integer by expanding the digits as powers of $2.$

For example, we can express the binary integer $(101)_2$ as a decimal number as follows:

$$



\begin{aligned}(101)_{2} & =1⋅2^{2}+0⋅2^{1}+1⋅2^{0} \\ & =4+0+1 \\ & =5\end{aligned}



$$

Thus,

$$



(101)_2 = (5)_{10}.



$$

More generally, we can represent integers in any base $b \geq 2,$ where $b$ is an integer. These are called **base $\boldsymbol b$ representations**.

For example, suppose we take a number $b$ among the following numbers:

$$



2, \, 3, \, 4, \, 5, \, 6, \, 7, \, 8, \, 9



$$

Then, we can uniquely express any integer using only the digits

$$



0, \, 1, \, \cdots, \, b-1.



$$

For example, consider the following integer written in base $b=8$ (octal integer):

$$



\boxed{\color{SandyBrown}1}\,\boxed{\color{Purple}5}\,\boxed{\color{SteelBlue}7}



$$

It's common to write numbers like these as $(157)_8$ to show that we are working in **base-8** (octal) rather than **base-10** (decimal).

We use a place value chart to interpret this number. Instead of decimal place values (corresponding to powers of ten), we will use octal place values corresponding to powers of eight:

In the place-value chart above:

- The digit $\boxed{\color{SandyBrown}1}$ is in the $8^2$s place.

- The digit $\boxed{\color{Purple}5}$ is in the $8^1$s place.

- The digit $\boxed{\color{SteelBlue}7}$ is in the $8^0$s place.

Therefore, we can express our octal number as a base $10$ integer as follows:

$$



\begin{aligned}(157)_{8} & =1⋅8^{2}+5⋅8^{1}+7⋅8^{0} \\ & =64+40+7 \\ & =(111)_{10}\end{aligned}



$$

In other words, $(157)_8$ is the same as $(111)_{10}.$ They represent the same number!

### Example: Converting From Another Base to Decimal

#### Question

What is $(113)_4$ written in base $10?$

#### Explanation

We can interpret the base $4$ representation of this integer using a place value chart:

Therefore, our number in base $10$ can be written as follows:

$$



\begin{aligned}(113)_{4} & =1⋅4^{2}+1⋅4^{1}+3⋅4^{0} \\ & =16+4+3 \\ & =(23)_{10}\end{aligned}



$$

### Converting From Decimal Base to Another Base

To convert a decimal integer $N$ to an integer in base $b,$ we must expand $N$ in powers of $b{:}$

$$



N=a_k \cdot b^k+a_{k-1} \cdot b^{k-1}+...+a_1 \cdot b^1 + a_0 \cdot b^0



$$

where $a_i \in \{0,1,2,\ldots b-1\}.$ Then, our base $b$ representation of $N$ is the string of digits

$$



N = (a_k a_{k-1} a_{k-2}\ldots a_1 a_0)_{b}



$$

For example, let's write the following decimal integer in base $8{:}$

$$



(102)_{10}



$$

First, we must write this number as a sum of powers of $8.$ Note that in base $10,$ we have

$$



8^3 > 102 \quad \text{and}\quad 8^2 < 102.



$$

Moreover, the quotient when $8^2$ divides $102$ equals $1,$ and the remainder is $38.$ Thus

$$



102 = 1 \cdot 8^2 + 38.



$$

We must now expand the remainder $38$ similarly.

The quotient when $8^1$ divides $38$ equals $4,$ and the remainder is $6.$ Thus, we can write

$$



102 = 1 \cdot 8^2 + 4 \cdot 8^1 + 6



$$

So, the full expansion of $(102)_{10}$ is powers of $8$ is

$$



(102)_{10} = {\color{SandyBrown}1} \cdot 8^2 + {\color{Purple}4} \cdot 8^1 + {\color{SteelBlue}6} \cdot 8^0.



$$

Finally, write the coefficients above using base-8 digits as follows:

Therefore, we conclude that

$$



(102)_{10} = (146)_{8}.



$$

### Example: Converting an Expanded Decimal Integer to Another Base

#### Question

What is $(5\cdot 6^{2}+3)_{10}$ written in base $6?$

#### Explanation

First, we rewrite our decimal integer as follows:

$$



\begin{aligned}5⋅6^{2}+3=5⋅6^{2}+0⋅6^{1}+3⋅6^{0}\end{aligned}



$$

The corresponding place value chart is given below:

Therefore, $(5\cdot 6^{2}+3)_{10} = (503)_6$

### Example: Converting a Decimal Integer to Another Base

#### Question

What is $(125)_{10}$ written in base $6?$

#### Explanation

We extract the powers of $6$ from the integer (starting from the largest possible one):

$$



\begin{aligned}125 & =3⋅6^{2}+17 \\ & =3⋅6^{2}+2⋅6^{1}+5 \\ & =3⋅6^{2}+2⋅6^{1}+5⋅6^{0}\end{aligned}



$$

So, the corresponding place value chart is as follows:

Therefore, $(125)_{10} = (325)_6$
