# The Multinomial Theorem

Source: https://www.mathacademy.com/topics/1407?courseId=109
Topic ID: 1407

## Prerequisites

- [The Special Case of the Binomial Theorem](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/3764-the-special-case-of-the-binomial-theorem.md)

## Lesson

### Introduction

Recall that the binomial theorem allows us to quickly expand powers of binomials. It states that if $n$ is a positive integer, then we can expand $(a+b)^n$ using the following formula:

$$



{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \cdots + {n \choose n}{a^0}{b^n}.



$$

The general formula for the binomial coefficient is

$$



{n \choose k} = \dfrac{n!}{k!\, (n-k)! }.



$$

We can restate the binomial theorem more concisely as follows:

*For any positive integer $n,$ the terms of $(a+b)^n$ can be written as*

$$



{n \choose k} a^{n-k} b^{k}.



$$

### The Multinomial Theorem

The binomial theorem can be generalized to the **multinomial theorem**, which allows us to quickly expand powers of multinomial expressions. The multinomial theorem for the case of a trinomial is as follows:

- *For any positive integer $n,$ the terms of $(a+b+c)^n$ can be written as* *where $k_1 + k_2 + k_3 = n,$ and the general formula for the **** is*

For example, using the multinomial theorem, we have

$$



\begin{aligned}(𝑎+𝑏+𝑐)^{2} & =(\frac{2}{2,\,0,\,0})𝑎^{2}𝑏^{0}𝑐^{0}+(\frac{2}{0,\,2,\,0})𝑎^{0}𝑏^{2}𝑐^{0}+(\frac{2}{0,\,0,\,2})𝑎^{0}𝑏^{0}𝑐^{2} \\ & ==+(\frac{2}{1,\,1,\,0})𝑎^{1}𝑏^{1}𝑐^{0}+(\frac{2}{1,\,0,\,1})𝑎^{1}𝑏^{0}𝑐^{1}+(\frac{2}{0,\,1,\,1})𝑎^{0}𝑏^{1}𝑐^{1} \\ & =\frac{2!}{2!\,0!\,0!}𝑎^{2}+\frac{2!}{0!\,2!\,0!}𝑏^{2}+\frac{2!}{0!\,0!\,2!}𝑐^{2}+\frac{2!}{1!\,1!\,0!}𝑎𝑏+\frac{2!}{1!\,0!\,1!}𝑎𝑐+\frac{2!}{0!\,1!\,1!}𝑏𝑐 \\ & =𝑎^{2}+𝑏^{2}+𝑐^{2}+2𝑎𝑏+2𝑎𝑐+2𝑏𝑐.\end{aligned}



$$

The multinomial theorem applies to powers of expressions with an arbitrary number of terms. But first, let's focus on understanding and applying the theorem in the case of a trinomial.

### Example: Computing the Coefficient of a Term in the Expansion of a Trinomial

#### Question

What is the coefficient of $a^2bc$ in the expansion of $(3a + b - 5c)^4?$

#### Explanation

According to the multinomial theorem, a general term in the expansion of $(3a + b - 5c)^4$ will have the form

$$



\binom{4}{k_1,\,k_2,\,k_3}(3a)^{k_1} (b)^{k_2} (-5c)^{k_3}



$$

with $k_1 + k_2 + k_3=4.$

The **** of $(3a)^2 (b)^{1} (-5c)^{1}$ is $a^2bc,$ so we have $k_1 = 2,$ $k_2 = 1,$ and $k_3 = 1.$

Therefore, the monomial that has literal part $a^2bc$ is

$$



\begin{aligned}(\frac{4}{2,\,1,\,1})(3𝑎)^{2}(𝑏)^{1}(−5𝑐)^{1} & =\frac{4!}{2!\,1!\,1!}⋅9𝑎^{2}⋅𝑏⋅(−5𝑐) \\ & =−\frac{4⋅3⋅2⋅1}{2}⋅45𝑎^{2}𝑏𝑐 \\ & =−12⋅45𝑎^{2}𝑏𝑐 \\ & =−540𝑎^{2}𝑏𝑐\,.\end{aligned}



$$

We see that the coefficient is $-540.$

### Example: Expanding a Trinomial Using the Multinomial Theorem

#### Question

Expand $(1+x+y)^3.$

#### Explanation

We apply the multinomial theorem as follows:

$$



\begin{aligned}(1+𝑥+𝑦)^{3} & =(\frac{3}{3,\,0,\,0})(1)^{3}+(\frac{3}{0,\,3,\,0})(𝑥)^{3}+(\frac{3}{0,\,0,\,3})(𝑦)^{3} \\ & ==+(\frac{3}{2,\,1,\,0})(1)^{2}(𝑥)+(\frac{3}{2,\,0,\,1})(1)^{2}(𝑦)+(\frac{3}{1,\,2,\,0})(1)(𝑥)^{2} \\ & ==+(\frac{3}{1,\,0,\,2})(1)(𝑦)^{2}+(\frac{3}{0,\,2,\,1})(𝑥)^{2}(𝑦)+(\frac{3}{0,\,1,\,2})(𝑥)(𝑦)^{2} \\ & ==+(\frac{3}{1,\,1,\,1})(1)(𝑥)(𝑦) \\ & =1+𝑥^{3}+𝑦^{3}+3𝑥+3𝑦+3𝑥^{2}+3𝑦^{2}+3𝑥^{2}𝑦+3𝑥𝑦^{2}+6𝑥𝑦\end{aligned}



$$

### The Multinomial Theorem in the General Case

The multinomial theorem applies to powers of expressions with any number of terms. Let's state the general form of the multinomial theorem below:

*For any positive integer $n,$ the terms of $(a_1 + a_2 + \ldots + a_m)^n$ can be written as*

$$



\binom{n}{k_1,\,k_2,\, \ldots \, k_m} {a_1}^{k_1} {a_2}^{k_2} \cdots {a_m}^{k_m},



$$

*where $k_1 + k_2 + \ldots + k_m = n$ and the general formula for the multinomial coefficient is*

$$



\binom{n}{k_1,\,k_2,\, \ldots \, k_m} = \dfrac{n!}{k_1!\, k_2! \, \cdots \, k_m! }.



$$

### Example: Computing the Coefficient of a Term in the Expansion of a Polynomial

#### Question

What is the coefficient of $x^3y^2$ in the expansion of $(-x-3y+z+2t)^5?$

#### Explanation

According to the multinomial theorem, a general term in the expansion of $(-x-3y+z+2t)^5$ will have the form

$$



\binom{5}{k_1,\,k_2,\,k_3,\,k_4}(x)^{k_1} (3y)^{k_2} (z)^{k_3} (2t)^{k_4}



$$

with $k_1 + k_2 + k_3 + k_4 = 5.$

The literal part of $(-x)^{3} (-3y)^{2} (z)^{0} (2t)^{0}$ is $x^3y^2,$ so we have $k_1 = 3,$ $k_2 = 2,$ $k_3 = 0,$ and $k_4 = 0.$

Therefore, the monomial that has literal part $x^3y^2$ is

$$



\begin{aligned}(\frac{5}{3,\,2,\,0,\,0})(−𝑥)^{3}(−3𝑦)^{2}(𝑧)^{0}(2𝑡)^{0} & =\frac{5!}{3!\,2!}⋅(−𝑥^{3})⋅9𝑦^{2} \\ & =−\frac{5⋅4⋅3!}{3!⋅2}⋅9𝑥^{3}𝑦^{2} \\ & =−10⋅9𝑥^{3}𝑦^{2} \\ & =−90𝑥^{3}𝑦^{2}\,.\end{aligned}



$$

We see that the coefficient is $-90.$
