# The Remainder Theorem

Source: https://www.mathacademy.com/topics/847?courseId=111
Topic ID: 847

## Prerequisites

- [Dividing Polynomials Using Synthetic Division](./728-dividing-polynomials-using-synthetic-division.md)
- [Solving Systems of Linear Equations Using Elimination: One Transformation](../../../high-school/traditional/lessons/algebra-i/4026-solving-systems-of-linear-equations-using-elimination-one-transformation.md)

## Lesson

### Introduction

The **remainder** theorem states that for any polynomial $p(x)$ and number $c,$ when we divide $p(x)$ by $(x-c),$ the remainder is equal to $p(c).$

For example, consider the polynomial $p(x)=4x^3-5x^2-7x+3$ and the number $c={\color{red}{2}}.$ First, let's divide $p(x)$ by $(x-{\color{red}{2}})$ using synthetic division:

We get a remainder of ${\color{blue}1}.$ Indeed, when we work out $p({\color{red}2}),$ we also get a result of ${\color{blue}1},$ just like the remainder theorem guarantees:

$$


\begin{aligned}𝑝(2) & =4(2)^{3}−5(2)^{2}−7(2)+3 \\ & =32−20−14+3 \\ & =1\,✓\end{aligned}


$$

To understand why this happens, notice that we can use the result of the synthetic division to rewrite $p(x)$ as

$$


p(x) = (4x^2+3x-1)(x-2)+{\color{blue}{1}}.


$$

When we substitute $x={\color{red}{2}}$ into the above, we see that the $(x-2)$ factor turns to $0,$ thereby eliminating the quotient $(4x^2+3x-1)$ and leaving only the remainder of ${\color{blue}{1}}\mathbin{:}$

$$


\begin{aligned}𝑝(2) & =(4⋅2^{2}+3⋅2−1)(2−2)+1 \\ & =(4⋅2^{2}+3⋅2−1)(0)+1 \\ & =0+1 \\ & =1\,✓\end{aligned}


$$

The remainder theorem remains valid even if we substitute $(x-c)$ with $k(x-c),$ as long as $k$ is a non-zero real number. Let's look at an example.

### Example: Finding the Value of the Remainder When a Polynomial is Divided by a Linear Factor

#### Question

Find the remainder when $p(x)=3x^2 +7x - 4$ is divided by $(3x-2).$

#### Explanation

The remainder theorem states that when $p(x)$ is divided by $(3x-2)= 3\left(x-\dfrac23\right),$ the remainder equals $p\left(\dfrac23\right).$

Evaluating $p\left(\dfrac23\right)$ directly gives

$$


\begin{aligned} p\left(\dfrac23\right) & =3\cdot \left(\dfrac23\right)^2 +7\cdot \left(\dfrac23\right) - 4 \\[5pt] & =3\cdot \left(\dfrac49\right) +\dfrac{14}{3} - 4 \\[5pt] & =\dfrac{12}{9}+\dfrac{2}{3} \\[5pt] & = \dfrac{12+ 3\cdot 2}{9} \\[5pt] & = \dfrac{18}{9}\\[5pt] & = 2. \end{aligned}


$$

So, when $p(x)$ is divided by $3\left(x-\dfrac23\right),$ the remainder is $2.$

**** We can check the answer by carrying out synthetic division:

### Example: Finding the Value of a Single Unknown in a Polynomial Given a Remainder

#### Question

If $q(x)=2x^3+3x^2-5x+c$ has remainder $-5$ when divided by $(x+3),$ what is the value of $c?$

#### Explanation

The remainder theorem states that when $q(x)$ is divided by $(x+3),$ the remainder equals $q(-3).$ Since we're told that the remainder is $-5,$ then, we must have $q(-3)=-5.$

Evaluating $q(-3)$ directly gives

$$


\begin{aligned}𝑞(−3) & =2(−3)^{3}+3(−3)^{2}−5(−3)+𝑐 \\ & =−54+27+15+𝑐 \\ & =−12+𝑐,\end{aligned}


$$

which means that

$$


-5 = -12 + c.


$$

Solving for $c$ in the equation above, we find that $c=7.$

### Example: Finding the Values of Two Unknowns in a Polynomial Given Two Remainders

#### Question

Suppose $f(x) = ax^3 +bx^2 -11x -2$ has a factor of $(x-2)$ and remainder of $-8$ when divided by $(x-1).$ Find the values of $a$ and $b.$

#### Explanation

Since $(x-2)$ is a factor of $f(x)$, it must divide into $f(x)$ with no remainder. In other words, when $f(x)$ is divided by $(x-2),$ the remainder is $0.$ It follows from the remainder theorem that

$$


\begin{aligned}0 & =𝑓(2) \\ & =𝑎(2)^{3}+𝑏(2)^{2}−11(2)−2 \\ & =8𝑎+4𝑏−24.\end{aligned}


$$

Likewise, since we're told that the remainder is $-8$ when $f(x)$ is divided by $(x-1),$ it follows from the remainder theorem that

$$


\begin{aligned}−8 & =𝑓(1) \\ & =𝑎(1)^{3}+𝑏(1)^{2}−11(1)−2 \\ & =𝑎+𝑏−13.\end{aligned}


$$

We now have the system of equations

$$


\begin{aligned}0=8𝑎+4𝑏−24 \\ −8=𝑎+𝑏−13.\end{aligned}


$$

Simplifying each equation, we get

$$


\begin{aligned}2𝑎+𝑏=6 \\ 𝑎+𝑏=5.\end{aligned}


$$

To eliminate $b,$ we subtract the equations and get

$$


\begin{aligned}2 & 𝑎+𝑏 & & =6 \\ −\, & 𝑎+𝑏 & & =5 \\ & 𝑎 & & =1.\end{aligned}


$$

Finally, we substitute $a=1$ into $a+b=5$ to find $b=4.$

Therefore, our final solution is $(a,b) = (1,4).$
