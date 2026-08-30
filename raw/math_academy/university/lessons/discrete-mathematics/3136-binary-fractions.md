# Binary Fractions

Source: https://www.mathacademy.com/topics/3136?courseId=109
Topic ID: 3136

## Prerequisites

- [Evaluating Expressions With Integer Exponents](../../../middle-school/lessons/grade-8/1987-evaluating-expressions-with-integer-exponents.md)
- [Converting Decimals From Standard to Expanded Form](../../../elementary-school/lessons/grade-5/2285-converting-decimals-from-standard-to-expanded-form.md)
- [Writing Repeating Decimals as Fractions](../../../high-school/traditional/lessons/algebra-ii/2564-writing-repeating-decimals-as-fractions.md)
- [Binary Integers](./3363-binary-integers.md)

## Lesson

### Introduction

In decimal notation, any fraction can be represented as a decimal number.

To represent a fraction as a decimal in decimal notation, we use the digits

$$



0, \, 1, \, 2, \, 3, \, 4, \, 5, \, 6, \, 7, \, 8, \, 9



$$

and a **decimal point** to separate the integer part from its proper fractional part. For example,

$$



\dfrac54=1\dfrac14=1.25.



$$

We can also represent fractions in binary notation, using only the digits $0$ and $1.$ Similar to decimal notation, we use a decimal point to separate the whole number and fractional parts.

For example, consider the following binary fraction:

$$



\boxed{\color{black}1} \mathbf{ .} \boxed{\color{Purple}0}\,\boxed{\color{SteelBlue}1}



$$

It's common to write numbers like these as $(1.01)_2$ to show that we're working in **base-2** (binary) as opposed to **base-10** (decimal).

We use a place value chart to interpret this number. But now, instead of *decimal* place values (corresponding to powers of *ten*), we will use *binary* place values that correspond to the powers of *two*:

We can interpret this number in a similar way to decimal digits:

- The digit $\boxed{\color{black}1}$ is in the $2^0$s place.

- The digit $\boxed{\color{Purple}0}$ is in the $2^{-1}$s place.

- The digit $\boxed{\color{SteelBlue}1}$ is in the $2^{-2}$s place.

We express this number in base ten by writing it in expanded form and evaluating it as follows:

$$



\begin{aligned}(1.01)_{2} & =1⋅2^{0}+0⋅2^{−1}+1⋅2^{−2} \\ & =1+0+0.25 \\ & =(1.25)_{10}\end{aligned}



$$

In other words, $(1.01)_2$ is equivalent to $1.25$ (in base $10$). They represent the same number!

### Example: Converting Binary Representations of Fractions to Decimal

#### Question

$(11.1101)_2 =$

#### Explanation

We can write down the binary fraction using a place value chart:

Therefore, our number in base $10$ can be written as follows:

$$



\begin{aligned}(10.0101)_{2} & =\overset{1⋅2^{1}+1⋅2^{0}}{}}{whole}+\,\overset{1⋅2^{−1}+1⋅2^{−2}+0⋅2^{−3}+1⋅2^{−4}}{}}{fraction} \\ & =2+1+0.5+0.25+0+0.0625 \\ & =(3.8125)_{10}\end{aligned}



$$

### Finite and Infinite Binary Representations

We are familiar with the fact some fractions require an infinite number of digits to represent them when expressed in decimal notation.

For example:

$$



\dfrac13=0.333\ldots =0.\overline{3}



$$

The notation $\overline{3}$ indicates that the digit $3$ repeats indefinitely.

In binary notation, it can be shown that *most* fractions require an infinite binary representation. For example:

$$



\begin{aligned}\frac{1}{10} & =(0.1)_{10}=(0.000110011…)_{2}=(0.0\overset{0011}{})_{2} \\ \frac{2}{10} & =(0.2)_{10}=(0.00110011…)_{2}=(0.\overset{0011}{})_{2} \\ \frac{3}{10} & =(0.3)_{10}=(0.0100110011…)_{2}=(0.01\overset{0011}{})_{2} \\ \frac{4}{10} & =(0.4)_{10}=(0.01100110…)_{2}=(0.0\overset{1100}{})_{2}\end{aligned}



$$

We have the following result:

*A number has a finite binary representation in base 2 if and only if it can be written as a fraction whose denominator is a power of $2.$*

For example:

$$



\begin{aligned}\frac{1}{2} & =(0.5)_{10}=(0.1)_{2} \\ \frac{1}{4} & =(0.25)_{10}=(0.01)_{2} \\ \frac{1}{8} & =(0.125)_{10}=(0.001)_{2} \\ \frac{5}{32} & =(0.15625)_{10}=(0.00101)_{2}\end{aligned}



$$

### Example: Converting Decimal Representations of Fractions to Finite Binary

#### Question

$(3.25)_{10} =$

#### Explanation

We express the number $(3.25)_{10}$ in base $10$ as follows:

- For the whole number part ($3$), we extract the powers of $2$ from the number, starting from the largest possible one.

- For the fractional part, we extract the ** powers of $2$ from the number, starting from the largest possible one.

Therefore, we get:

$$



\begin{aligned}3.25 & =\overset{3}{whole}+\overset{0.25}{fraction} \\ & =2^{1}+2^{0}+2^{−2} \\ & =\underset{whole}{\underset{}{1⋅2^{1}+1⋅2^{0}}}+\underset{fraction}{\underset{}{0⋅2^{−1}+1⋅2^{−2}}}\end{aligned}



$$

So, the corresponding place value chart is as follows:

Therefore, $(3.25)_{10} = (11.01)_2.$

### Example: Converting Decimal Representations of Fractions to Infinite Binary

#### Question

Find the first six digits of $(0.9)_{10}$ in base $2.$

#### Explanation

We extract the negative powers of $2$ from the number, starting from the largest possible one:

$$



\begin{aligned}0.9 & =\underset{1/2}{\underset{}{0.5}}+0.4 \\ & =\underset{1/2}{\underset{}{0.5}}+\underset{1/4}{\underset{}{0.25}}+0.15 \\ & =\underset{1/2}{\underset{}{0.5}}+\underset{1/4}{\underset{}{0.25}}+\underset{1/8}{\underset{}{0.125}}+0.025 \\ & =\underset{1/2}{\underset{}{0.5}}+\underset{1/4}{\underset{}{0.25}}+\underset{1/8}{\underset{}{0.125}}+\underset{1/64}{\underset{}{0.015625}}+0.009375 \\ & =1⋅2^{−1}+1⋅2^{−2}+1⋅2^{−3}+0⋅2^{−4}+0⋅2^{−5}+1⋅2^{−6}+⋯\end{aligned}



$$

So, the corresponding place value chart is as follows:

Therefore, $(0.9)_{10} = (0.\,111\:001 \ldots)_2.$
