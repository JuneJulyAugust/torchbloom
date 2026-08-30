# Factoring Expressions Containing Hidden Factors

Source: https://www.mathacademy.com/topics/6172?courseId=120
Topic ID: 6172

## Prerequisites

- [Factoring Expressions Containing Binomials](./6091-factoring-expressions-containing-binomials.md)

## Lesson

### Introduction

Suppose we wish to factor the expression

$$


(8x+3){\color{blue}{(4-x)}} + {\color{red}{(x-4)}}(5x-7)


$$

At first glance, it seems as though there are no common factors.

However, upon closer inspection, we notice that

- the first term contains a factor of ${\color{blue}{(4-x)}},$ and

- the second term contains a factor of ${\color{red}{(x-4)}}.$

These factors differ only by their sign:

$$


{\color{red}{(x-4)}} = -{\color{blue}{(4-x)}}.


$$

So, we first make the factors the same by factoring out $-1$ in the second term, as follows:

$$


(8x+3){\color{blue}{(4-x)}} - {\color{blue}{(4-x)}}(5x-7)


$$

Notice that the plus $(+)$ symbol in front of the second term of our original expression has flipped to a minus symbol $(-).$

Now that our terms contain a common factor, we can factor the expression. This gives

$$


{\color{blue}{(4-x)}}\left[(8x+3) - (5x-7)\right].


$$

Finally, we simplify the expression inside the square brackets:

$$


(8x+3) - (5x-7) = 3x + 10


$$

So, our fully factored form is

$$


(4-x)(3x+10).


$$

### Example: Factoring Expressions

#### Question

Factor the following expression:

$$


(4y+1)(8y-7) - (7-8y)(6y-5)


$$

#### Explanation

We're asked to factor the expression

$$


(4y+1)(8y-7) - (7-8y)(6y-5).


$$

Notice that

- the first term in this expression contains a factor of $(8y-7),$ and

- the second term contains a factor of $(7-8y).$

These factors differ only by the sign:

$$


7-8y = -(8y-7).


$$

So, we first make the factors the same by factoring out $-1$ in the second term:

$$


(4y+1)(8y-7) + (8y-7)(6y-5)


$$

Now, we can factor the expression as follows:

$$


(8y-7)\left[(4y+1) + (6y-5)\right]


$$

Finally, we simplify the expression inside the square brackets:

$$


(4y+1) + (6y-5) = 10y - 4


$$

So the factored form is

$$


(8y-7)(10y-4).


$$

### Example: Factoring Expressions Containing Squared Binomials

#### Question

Factor the following expression:

$$


(z-12)(z+3) + 4(12-z)^2


$$

#### Explanation

We're asked to factor the expression

$$


(z-12)(z+3) + 4(12-z)^2.


$$

Notice that

- the first term in this expression contains a factor of $(z-12),$ and

- the second term contains a factor of $(12-z).$

These factors differ only by the sign:

$$


12-z = -(z-12)


$$

However, the squaring eliminates the minus sign:

$$


(12-z)^2 = (z-12)^2


$$

So, we can simply rewrite the second term:

$$


(z-12)(z+3) + 4(z-12)^2


$$

Now, we can factor the expression as follows:

$$


(z-12)\left[(z+3) + 4(z-12)\right]


$$

Finally, we simplify the expression inside the square brackets. This gives

$$


\begin{aligned}(𝑧−12)[(𝑧+3)+4(𝑧−12)] & = \\ (𝑧−12)[𝑧+3+4𝑧−48] & = \\ (𝑧−12)(5𝑧−45). & \end{aligned}


$$

### Example: Factoring Expressions Containing Cubic Binomials

#### Question

Consider the expression

$$


(2a-7)^3(a+2) + (3a+4)(7-2a)^2.


$$

This expression can be written in the form

$$


(2a-7)^2\cdot g(a).


$$

Find the polynomial $g(a).$

#### Explanation

We're asked to factor the expression

$$


(2a-7)^3(a+2) + (3a+4)(7-2a)^2.


$$

Notice that

- the first term in this expression contains a factor of $(2a-7)^2,$ and

- the second term contains a factor of $(7-2a)^2.$

These factors differ only by the sign:

$$


7-2a = -(2a-7)


$$

However, the squaring eliminates the minus sign:

$$


(7-2a)^2 = (2a-7)^2


$$

So, we can simply rewrite the second term:

$$


(2a-7)^3(a+2) + (3a+4)(2a-7)^2


$$

Now, we can factor the expression as follows:

$$


(2a-7)^2 \left[(2a-7)(a+2) + (3a+4)\right]


$$

Finally, we simplify the expression inside the square brackets. This gives

$$


\begin{aligned}(2𝑎−7)^{2}[(2𝑎−7)(𝑎+2)+(3𝑎+4)] & = \\ (2𝑎−7)^{2}[\,2𝑎^{2}+4𝑎−7𝑎−14+3𝑎+4\,] & = \\ (2𝑎−7)^{2}\underset{𝑔(𝑎)}{\underset{}{(2𝑎^{2}−10)}}. & \end{aligned}


$$

Therefore, we have

$$


g(a) = 2a^2 - 10.


$$
