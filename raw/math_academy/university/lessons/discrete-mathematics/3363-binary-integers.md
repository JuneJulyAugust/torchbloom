# Binary Integers

Source: https://www.mathacademy.com/topics/3363?courseId=109
Topic ID: 3363

## Prerequisites

- [The Zeroth Power](../../../middle-school/lessons/grade-8/322-the-zeroth-power.md)
- [Evaluating Whole Number Expressions Containing Exponents](../../../elementary-school/lessons/grade-5/2475-evaluating-whole-number-expressions-containing-exponents.md)

## Lesson

### Introduction

The number system we're most familiar with is the decimal system, which comprises the following ten digits:

$$



0, \, 1, \, 2, \, 3, \, 4, \, 5, \, 6, \, 7, \, 8, \, 9



$$

We can express any integer using these digits.

Now, imagine a system where we're only allowed to use two digits, namely

$$



0 \quad\textrm{and}\quad 1.



$$

Can we encode any integer using only these two digits? The answer is yes! The system that we use to do this is called the **binary system**.

Consider the following binary integer:

$$



\boxed{\color{black}1}\,\boxed{\color{Purple}0}\,\boxed{\color{SteelBlue}1}



$$

It's common to write numbers like these as $(101)_2$ to show that we're working in **base-2** (binary) as opposed to **base-10** (decimal).

We use a place value chart to interpret this number. But now, instead of *decimal* place values (corresponding to powers of *ten*), we will use *binary* place values that correspond to the powers of *two*:

We can interpret this number in a similar way to decimal digits:

- The digit $\boxed{\color{black}1}$ is in the $2^2$s place.

- The digit $\boxed{\color{Purple}0}$ is in the $2^1$s place.

- The digit $\boxed{\color{SteelBlue}1}$ is in the $2^0$s place.

We express this number in base ten by writing it in expanded form and evaluating it as follows:

$$



\begin{aligned}(101)_{2} & =1⋅2^{2}+0⋅2^{1}+1⋅2^{0} \\ & =4+0+1 \\ & =(5)_{10}\end{aligned}



$$

In other words, $(101)_2$ is equivalent to $5$ (in base-10). They represent the same number!

### Example: Converting a Binary Integer to Decimal

#### Question

What is $(1\,110)_2$ written in base $10?$

#### Explanation

We can write down the binary integer using a place value chart:

Therefore, our number in base $10$ can be written as follows:

$$



\begin{aligned}(1\,110)_{2} & =1⋅2^{3}+1⋅2^{2}+1⋅2^{1}+0⋅2^{0} \\ & =8+4+2+0 \\ & =(14)_{10}\end{aligned}



$$

### Example: Converting Expanded Decimal Integer to Binary

#### Question

What is $(2^{3}+1)_{10}$ written in base $2?$

#### Explanation

First, we rewrite our decimal integer as follows:

$$



\begin{aligned}2^{3}+2^{0}=1⋅2^{3}+0⋅2^{2}+0⋅2^{1}+1⋅2^{0}\end{aligned}



$$

The corresponding place value chart is given below:

Therefore, $(2^{3}+1)_{10} = (1\,001)_2.$

### Example: Converting a Decimal Integer to Binary

#### Question

What is $(53)_{10}$ written in base $2?$

#### Explanation

We extract the powers of $2$ from the integer (starting from the largest possible one):

$$



\begin{aligned}53 & =32+21 \\ & =32+16+5 \\ & =32+16+4+1 \\ & =1⋅2^{5}+1⋅2^{4}+0⋅2^{3}+1⋅2^{2}+0⋅2^{1}+1⋅2^{0}\end{aligned}



$$

So, the corresponding place value chart is as follows:

Therefore, $(53)_{10} = (110\,101)_2.$
