# Fractions in Arbitrary Bases

Source: https://www.mathacademy.com/topics/2888?courseId=109
Topic ID: 2888

## Prerequisites

- [Converting Decimals From Standard to Expanded Form](../../../elementary-school/lessons/grade-5/2285-converting-decimals-from-standard-to-expanded-form.md)
- [Integers in Arbitrary Bases](./2889-integers-in-arbitrary-bases.md)

## Lesson

### Introduction

In a previous lesson, we learned how to convert between decimal integers and integers in base $b,$ where $b= 2,\, 3\, \ldots, \, 9.$ Let's now learn how we can write a fractional number in any base.

For example, consider the following floating point fractional number in base $4{:}$

$$



\boxed{\color{SandyBrown}1}\,.\,\boxed{\color{Purple}2}\,\boxed{\color{SteelBlue}3}



$$

To interpret this number, we use the place value system as usual. But now, instead of *decimal* place values (that correspond to powers of *ten*), we will use a base-$4$ place values (that correspond to the powers of *four*):

In the place-value chart above:

- The digit $\boxed{\color{SandyBrown}1}$ is in the $4^0$s place.

- The digit $\boxed{\color{Purple}2}$ is in the $4^{-1}$s place.

- The digit $\boxed{\color{SteelBlue}3}$ is in the $4^{-2}$s place.

Notice that place values to the right of the dot $(\,.)$ correspond to negative powers of $4$ in descending order.

Therefore, our number can be written in base $10$ as follows:

$$



\begin{aligned}(1.23)_{4} & =\overset{\overset{1⋅4^{0}}{}}{whole}+\,\overset{\overset{2⋅4^{−1}+3⋅4^{−2}}{}}{fraction} \\ & =1+0.5+0.1875 \\ & =(1.6875)_{10}\end{aligned}



$$

Any base $b$ number can be converted into a decimal number, and any decimal number can be written as a base $b$ number.

### Example: Converting Fractions in Bases 4, 5, and 8 to Decimal

#### Question

What is $(56.6)_8$ written in base $10?$

#### Explanation

We can write down the number using a place value chart:

Therefore, our number can be written in base $10$ as follows:

$$



\begin{aligned}(56.6)_{8} & =\overset{\overset{5⋅8^{1}+6⋅8^{0}}{}}{whole}+\,\overset{\overset{6⋅8^{−1}}{}}{fraction} \\ & =40+6+0.75 \\ & =(46.75)_{10}\end{aligned}



$$

### Fractions in Bases 3, 6, 7, and 9

Notice that finite floating-point fractions base $3, 6, 7, 9$ give infinite decimal representations.

Consider, for example, the number $(0.1)_3$, which is written in base $10$ as follows:

$$



\begin{aligned}(0.1)_{3} & =\overset{\overset{\,0^{1}}{}}{whole}+\,\overset{\overset{1⋅3^{−1}}{}}{fraction} \\ & =0+\frac{1}{3} \\ & =(\frac{1}{3})_{10} \\ & =(0.333\,333…)_{10}\end{aligned}



$$

### Example: Converting Fractions in Bases 3, 6, 7, and 9 to Decimal

#### Question

What is $(4.31)_7$ written as a fraction in base $10?$

#### Explanation

We can write down the number using a place value chart:

Therefore, our number can be written in base $10$ as follows:

$$



\begin{aligned}(4.31)_{7} & =\overset{\overset{4⋅7^{0}}{}}{whole}+\,\overset{\overset{3⋅7^{−1}+1⋅7^{−2}}{}}{fraction} \\ & =4+\frac{3}{7}+\frac{1}{49} \\ & =\frac{218}{49}\end{aligned}



$$

### Example: Converting a Decimal Fraction to a Fraction in Another Base

#### Question

What is $\left(74 + \dfrac{4}{5} + \dfrac{18}{25}\right)_{10}$ written in base $5?$

#### Explanation

First, we rewrite our decimal in descending powers of $5,$ as follows:

$$



\begin{aligned}74+\frac{4}{5}+\frac{18}{25} & =2⋅25+4⋅5+4+\frac{4}{5}+\frac{18}{25} \\ & =2⋅25+4⋅5+4+\frac{4}{5}+\frac{15+3}{25} \\ & =2⋅25+4⋅5+4+\frac{4}{5}+\frac{3}{5}+\frac{3}{25} \\ & =2⋅25+4⋅5+4+1+\frac{2}{5}+\frac{3}{25} \\ & =3⋅25+\frac{2}{5}+\frac{3}{25} \\ & =3⋅5^{2}+0⋅5^{1}+0⋅5^{0}+2⋅5^{−1}+3⋅5^{−2}\end{aligned}



$$

The corresponding place value chart is given below:

Therefore, $\left(74 + \dfrac{4}{5} + \dfrac{18}{25}\right)_{10} = (300.23)_5$

### Finite and Infinite Representations in Different Bases

Some rational numbers give a finite floating-point representation in some base and an infinite floating-point representation in another base.

For example, earlier, we saw that

$$



(0.1)_3 = \left(\dfrac{1}{3}\right)_{10} = (0.333\,333\ldots)_{10}.



$$

Let's try to convert the base $3$ number $(0.1)_3,$ into a base-$4$ number.

We extract the powers of $4$ from the number (starting from the largest possible one):

$$



\begin{aligned}(0.1)_{3} & =(\frac{1}{3})_{10} \\ & =1⋅4^{−1}+\frac{1}{12} \\ & =1⋅4^{−1}+1⋅4^{−2}+\frac{1}{48} \\ & =1⋅4^{−1}+1⋅4^{−2}+1⋅4^{−3}+\frac{1}{192}\end{aligned}



$$

However, this process will never end (at each step the remainder fraction becomes one-fourth of the previous step). So,

$$



(0.1)_3 = (0.\,111\,111\,\ldots)_4.



$$
