# Reasoning About Coefficients of Quadratics Using Standard and Factored Forms

Source: https://www.mathacademy.com/topics/6286?courseId=120
Topic ID: 6286

## Prerequisites

- [Splitting Rational Expressions Into Separate Terms](../algebra-ii/355-splitting-rational-expressions-into-separate-terms.md)
- [Roots of Quadratic Functions](../algebra-i/661-roots-of-quadratic-functions.md)
- [Equating Polynomial Coefficients](../algebra-i/6092-equating-polynomial-coefficients.md)
- [Rational Numbers as Finite or Repeating Decimals](../grade-7/7011-rational-numbers-as-finite-or-repeating-decimals.md)

## Lesson

### Introduction

In this lesson, we'll learn how to connect the factorized form of a quadratic expression with its standard form by expanding the factors and identifying the coefficients.

This skill is important because it enables us to quickly interpret or manipulate quadratic functions, whether working with equations, graphs, or applied problems.

For example, suppose the expression

$$


ax^{2} + bx + c,


$$

where $a,$ $b,$ and $c$ are constants, can be rewritten as

$$


(x+4)(x+2).


$$

What are the values of the constants?

First, we expand the factorization:

$$


\begin{aligned}(𝑥+4)(𝑥+2) & =𝑥(𝑥+2)+4(𝑥+2) \\ & =𝑥^{2}+2𝑥+4𝑥+8 \\ & =𝑥^{2}+6𝑥+8\end{aligned}


$$

Now, comparing $x^{2} + 6x + 8$ with the given quadratic $ax^{2} + bx + c,$ we have the following:

$$


\begin{aligned}𝑎𝑥^{2} & + & 𝑏𝑥 & + & 𝑐 \\ ↕𝑥 & & ↕𝑥\, & & ↕ \\ 1𝑥^{2} & + & 6𝑥 & + & 8\end{aligned}


$$

Therefore, the unknown coefficients are as follows:

- The leading coefficient gives $a = 1.$

- The middle coefficient gives $b = 6.$

- The constant term gives $c = 8.$

### Example: Expressing the Coefficients of Quadratic Through One of Them

#### Question

The expression $ax^{2} + bx + c$, where $a,$ $b,$ and $c$ are constants, can be rewritten as $(4x+2)(x+5).$ What are the values of the constants?

#### Explanation

First, expand the factorization:

$$


\begin{aligned}(4𝑥+2)(𝑥+5) & =4𝑥(𝑥+5)+2(𝑥+5) \\ & =4𝑥^{2}+20𝑥+2𝑥+10 \\ & =4𝑥^{2}+22𝑥+10\end{aligned}


$$

Now, comparing this with the general quadratic $ax^{2} + bx + c,$ we identify the following:

- The leading coefficient gives $a = 4.$

- The middle coefficient gives $b = 22.$

- The constant term gives $c = 10.$

### Example: Identifying a Possible Value of the Sum of Coefficients

#### Question

The function $h$ is defined by $h(x) = a x^{2} + b x + c,$ where $a, b,$ and $c$ are constants. The graph of $y = h(x)$ in the $xy$-plane passes through the points $(2, 0)$ and $(-3, 0).$ If $a$ is an integer greater than $1,$ which of the following could be the value of $a + b?$

1. $2$

2. $10$

3. $15$

#### Explanation

Note that the graph passes through $(2,0)$ and $(-3,0),$ so the function $h$ has roots $2$ and $-3$. Therefore, $(x-2)$ and $(x+3)$ are factors of $h(x).$

Since $h$ is quadratic with leading coefficient $a,$ we can write

$$


h(x) = a(x - 2)(x + 3).


$$

Next, we expand:

$$


\begin{aligned}ℎ(𝑥) & =𝑎(𝑥^{2}+𝑥−6) \\ & =𝑎𝑥^{2}+𝑎𝑥−6𝑎\end{aligned}


$$

So, comparing the coefficient of $x$ in the above expression with the given form

$$


h(x) = a x^2 + b x + c,


$$

we get

$$


b = a.


$$

Thus,

$$


a + b = a + a = 2a.


$$

Now, we're told that $a$ is ** This means that the possible values of $2a$ are all the even integers greater than $2{:}$

$$


4, 6, 8, 10,\ldots


$$

With that in mind, let's examine each option:

- $2$ is NOT an even integer greater than $2.\:\:{\color{red}{\times}}$

- $10$ is an even integer greater than $2.\:\:{\color{green}{\checkmark}}$

- $15$ is NOT an even integer greater than $2.\:\:{\color{red}{\times}}$

Therefore, the correct answer is "II only."

### Example: Identifying True Statements About Coefficients With Additional Constraints

#### Question

The expression $6x^{2} + bx - 35$, where $b$ is a constant, can be rewritten as $(px + q)(x + r)$, where $p, q,$ and $r$ are integer constants. Which of the following must be an integer?

1. $\dfrac{35}{q}$

2. $\dfrac{35}{p}$

3. $\dfrac{b}{p}$

4. $\dfrac{b}{q}$

#### Explanation

First, we expand the factorization:

$$


\begin{aligned}(𝑝𝑥+𝑞)(𝑥+𝑟) & =𝑝𝑥(𝑥+𝑟)+𝑞(𝑥+𝑟) \\ & =𝑝𝑥^{2}+𝑝𝑟𝑥+𝑞𝑥+𝑞𝑟 \\ & =𝑝𝑥^{2}+(𝑝𝑟+𝑞)𝑥+𝑞𝑟\end{aligned}


$$

Now, comparing this with the given quadratic, $6x^{2} + bx - 35,$ we have the following:

- The leading coefficient gives $p = 6.$

- The middle coefficient gives $pr + q = b.$

- The constant term gives $qr = -35.$

Next, since $q$ and $r$ are integers and $qr = -35,$ it follows that $q$ and $r$ must be factors of $-35.$ With that in mind, let's check the given options in turn.

- Option I is valid. Indeed, $\dfrac{35}{q}$ is an integer since $q$ must be a factor of $-35.$

- Option II is not valid. Notice that which is not an integer.

- Option III is not valid. Notice that can be non-integer, for example, when $q = 1.$

- Option IV is not valid. Notice that can be non-integer, for example, when $r = 1.$

Therefore, the correct answer is "I only."
