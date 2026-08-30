# Expanding Binomials Using Pascal's Triangle

Source: https://www.mathacademy.com/topics/1157?courseId=113
Topic ID: 1157

## Prerequisites

- [Squaring Binomials](./360-squaring-binomials.md)
- [The Power of Product Rule With Algebraic Expressions](./1331-the-power-of-product-rule-with-algebraic-expressions.md)

## Lesson

### Introduction

One interesting number pattern is **Pascal's triangle**, named after Blaise Pascal, a famous French mathematician.

Pascal's triangle is made by rows of numbers that form a triangle. Each row has one more number than the row above. The first two rows are made of three $1$s in a triangle:

$$


\begin{aligned} & & 1 & & \\ & 1 & & 1 & \\ ⋮ & & ⋮ & & ⋮\end{aligned}


$$

Let's construct the next row. The first and last number in each row is always $1.$

$$


\begin{aligned} & & & 1 & & & \\ & & 1 & & 1 & & \\ & 1 & & ◻ & & 1 & \\ ⋮ & & ⋮ & & ⋮ & & ⋮\end{aligned}


$$

The other numbers are always greater than $1$ and can be found by adding the two closest numbers located in the previous row.

In our case, the numbers closest to the unknown number and located in the previous row are ${\color{blue}1}$ and ${\color{blue}1}.$ Therefore, the unknown number is the sum of $\color{blue}1$ and ${\color{blue}1}\mathbin{:}$

$$


{\large\square} = {\color{blue}1} + {\color{blue}1} = 2


$$

Now, we have the first three rows of Pascal's triangle.

$$


\begin{aligned} & & & 1 & & & \\ & & 1 & & 1 & & \\ & 1 & & 2 & & 1 & \\ ⋮ & & ⋮ & & ⋮ & & ⋮\end{aligned}


$$

If we continue repeating this process for each row, we will get the following results for the first six rows of Pascal's triangle:

$$


\begin{aligned} & & & & & & 1 & & & & & & \\ & & & & & 1 & & 1 & & & & & \\ & & & & 1 & & 2 & & 1 & & & & \\ & & & 1 & & 3 & & 3 & & 1 & & & \\ & & 1 & & 4 & & 6 & & 4 & & 1 & & \\ & 1 & & 5 & & 10 & & 10 & & 5 & & 1 & \\ ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮\end{aligned}


$$

### Example: Finding the Missing Number in a Pascal's Triangle

#### Question

What is the missing number?

$$


\begin{aligned} & & & & & & 1 & & & & & \\ & & & & & 1 & & 1 & & & & \\ & & & & 1 & & 2 & & 1 & & & \\ & & & 1 & & 3 & & 3 & & 1 & & \\ & & 1 & & ◻ & & 6 & & 4 & & 1 & \\ & ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮\end{aligned}


$$

#### Explanation

In Pascal's triangle, the first and last number in each row is $1.$ The other numbers are always greater than $1$ and can be found by adding the two closest numbers located in the previous row.

In our case, the numbers closest to the unknown number and located in the previous row are $1$ and $3.$

$$


\begin{aligned} & & & & & & 1 & & & & & \\ & & & & & 1 & & 1 & & & & \\ & & & & 1 & & 2 & & 1 & & & \\ & & & 𝟏 & & 𝟑 & & 3 & & 1 & & \\ & & 1 & & ◻ & & 6 & & 4 & & 1 & \\ & ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮\end{aligned}


$$

Therefore, the unknown number is the sum of $1$ and $3\mathbin{:}$

$$


{\large\square} = 1 + 3 = 4


$$

### Expanding Binomials Using Pascal’s Triangle

Multiplying a binomial by itself $n$ times is known as a **binomial expansion**. For instance, multiplying the binomial $(a + b)$ by itself gives

$$


(a + b)^2 = a^2 + 2ab + b^2.


$$

Let's consider the binomial expansion of

$$


(a+b)^n,


$$

where $n$ is a positive integer.

To write out the expansion, we use two patterns to simplify most of the hard work: the **exponent pattern** and the **coefficient pattern**.

- The **exponent pattern** is The exponents of $a$ start at $n$ and go down ($n, n-1, \cdots, 1, 0$) while the exponents of $b$ increase from $0$ to $n.$ In every term, the two exponents always add up to $n.$

- The **coefficient pattern** can be found using Pascal's Triangle: We take the top row to be the $0$th row. Then, the $n$th row of Pascal's Triangle are the coefficients of $(a+b)^n.$

Let's use this to expand the binomial

$$


(a+b)^3.


$$

The exponent pattern is

$$


a^{\color{red}3}b^{\color{blue}0},\quad a^{\color{red}2}b^{\color{blue}1}, \quad a^{\color{red}1}b^{\color{blue}2}, \quad a^{\color{red}0}b^{\color{blue}3}.


$$

Since $n=3,$ the coefficient pattern is found using the $3$rd row in Pascal's Triangle: $(1,3,3,1).$

Therefore,

$$


(a + b)^3 = \mathbf{1}a^{\color{red}3}b^{\color{blue}0} + \mathbf{3}a^{\color{red}2}b^{\color{blue}1} + \mathbf{3}a^{\color{red}1}b^{\color{blue}2} + \mathbf{1}a^{\color{red}0}b^{\color{blue}3}.


$$

Finally, simplifying the above gives

$$


(a + b)^3= a^{3} + 3a^{2}b + 3ab^{2} + b^{3} ,


$$

and we're done!

### Table of Results

The following table shows the first six binomial expansions.

### Example: Expanding a Binomial With One Variable

#### Question

Expand the binomial $(2z + 1)^4.$

#### Explanation

First, let's compare our expression with the binomial

$$


(a+b)^n.


$$

We have that $n=4,$ $a = 2z,$ and $b= 1.$ So, the exponents of the binomial expansion must follow the pattern

$$


a^4b^0,\quad a^{3}b^1,\quad a^{2}b^2,\quad a^1b^3,\quad a^0b^4.


$$

The $4$th row in Pascal's Triangle is $(1,4,6,4,1).$ Therefore,

$$


\begin{aligned} (2z + 1)^4 &=\mathbf{1}a^4 + \mathbf{4}a^3b + \mathbf{6}a^2b^2 + \mathbf{4}ab^3 + \mathbf{1}b^4\\\[5pt] &=\mathbf{1}(2z)^4(1)^0 + \mathbf{4}(2z)^3(1)^1 + \mathbf{6}(2z)^2(1)^2 + \mathbf{4}(2z)^1(1)^3 + \mathbf{1}(2z)^0(1)^4\\\[5pt] &=(2z)^4 + 4(2z)^3 + 6(2z)^2 + 4(2z) +1\\\[5pt] &=16z^4 + 32z^3 + 24z^2 + 8z + 1 \end{aligned}


$$

### Example: Expanding a Binomial With More Than One Variable

#### Question

Expand the binomial $(3x-y)^4.$

#### Explanation

First, let's compare our expression with the binomial

$$


(a+b)^n.


$$

Here we have that $n=4,$ $a = 3x,$ and $b= -y.$ So, the exponents of the binomial expansion must follow the pattern

$$


a^4b^0,\quad a^{3}b^1,\quad a^{2}b^2,\quad a^1b^3,\quad a^0b^4.


$$

The $4$th row in Pascal's Triangle is $(1,4,6,4,1).$ Therefore,

$$


\begin{aligned} (3x - y)^4 &=\mathbf{1}a^4 + \mathbf{4}a^3b + \mathbf{6}a^2b^2 + \mathbf{4}ab^3 + \mathbf{1}b^4\\\[5pt] &= \mathbf{1}(3x)^4(-y)^0 + \mathbf{4}(3x)^3(-y)^1 + \mathbf{6}(3x)^2(-y)^2 + \mathbf{4}(3x)^1(-y)^3 + \mathbf{1}(3x)^0(-y)^4\\\[5pt] &= \mathbf{1}\left(81x^4\right)(1) + \mathbf{4}\left(27x^3\right)(-y) + \mathbf{6}\left(9x^2\right)(y^2) + \mathbf{4}(3x)(-y^3) + \mathbf{1}(1)(y^4) \\\[5pt] &= 81x^4 - 108x^3y + 54x^2y^2 - 12xy^3 + y^4. \end{aligned}


$$

### Example: Finding the Coefficient of a Particular Term in a Binomial Expansion

#### Question

Find the coefficient of $x^4y$ in the expansion of ${(2x^2+y)}^3.$

#### Explanation

Since the exponent of the binomial expression is $n=3,$ we see that the exponents of the binomial expansion must follow the pattern

$$


\left(2x^2\right)^3y^0, \qquad {\color{blue}{\left(2x^2\right)^2 y^1}},\qquad \left(2x^2\right)^1 y^2,\qquad \left(2x^2\right)^0 y^3.


$$

Of these, the term that returns $x^4y$ is the second. So, we are looking for the second term in the binomial expansion.

The $3$rd row in Pascal's Triangle is $(1,{\color{red}3},3,1).$ Therefore, the second term in the binomial expansion is

$$


\begin{aligned}3(2𝑥^{2})^{2}(𝑦)^{1} & =3(4𝑥^{4})(𝑦) \\ & =12𝑥^{4}𝑦.\end{aligned}


$$

So, the coefficient of $x^4y$ in the expansion of ${(2x^2+y)}^3$ is $12.$
