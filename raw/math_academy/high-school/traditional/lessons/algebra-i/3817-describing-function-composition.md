# Describing Function Composition

Source: https://www.mathacademy.com/topics/3817?courseId=44
Topic ID: 3817

## Prerequisites

- [Squaring Binomials](./360-squaring-binomials.md)
- [Function Composition](./1985-function-composition.md)

## Lesson

### Introduction

Suppose that we wish to find an algebraic expression for $(f \circ g)(x),$ where $f(x) = 2x + 3$ and $g(x) = x - 1.$

The composite function can be calculated by taking the expression for the inner function ${\color{blue}g(x)}$ and passing it as input to the outer function $f({\color{blue}x})\mathbin{:}$

$$


\begin{aligned}(𝑓∘𝑔)(𝑥) & =𝑓(𝑔(𝑥)) \\ & =2(𝑔(𝑥))+3 \\ & =2(𝑥−1)+3 \\ & =2𝑥−2+3 \\ & =2𝑥+1\end{aligned}


$$

So, we just take the expression for $f$ and replace every occurrence of $x$ with the expression for $g(x).$

### Example: Finding a Composite Function

#### Question

Find $(f \circ g)(x)$ for $f(x) = 3x^2 - 2x$ and $g(x) = x + 4.$

#### Explanation

Note that $(f \circ g)(x)$ is equivalent to $f(g(x)).$

To find $f(g(x)),$ we write down the function $f$ and replace every occurrence of $x$ with $g(x)\mathbin{:}$

$$


\begin{aligned}𝑓(𝑥) & =3𝑥^{2}−2𝑥 \\ 𝑓(𝑔(𝑥)) & =3(𝑔(𝑥))^{2}−2(𝑔(𝑥))\end{aligned}


$$

Then, we substitute ${\color{blue}g(x)} = {\color{red}x+4}$ into the right-hand side of the above and simplify, as follows:

$$


\begin{aligned}𝑓(𝑔(𝑥)) & =3(𝑔(𝑥))^{2}−2(𝑔(𝑥)) \\ & =3(𝑥+4)^{2}−2(𝑥+4) \\ & =3(𝑥+4)(𝑥+4)−2𝑥−8 \\ & =3(𝑥^{2}+4𝑥+4𝑥+16)−2𝑥−8 \\ & =3(𝑥^{2}+8𝑥+16)−2𝑥−8 \\ & =3𝑥^{2}+24𝑥+48−2𝑥−8 \\ & =3𝑥^{2}+22𝑥+40\end{aligned}


$$

### Example: Composing a Function With Itself

#### Question

If $g(x)=x^2+x,$ then find $(g\circ g)(x).$

#### Explanation

First, we note that $(g\circ g)(x)$ is equivalent to $g(g(x)).$

To find $g(g(x)),$ we write down the function $g$ and replace every occurrence of $x$ with $g(x)\mathbin{:}$

$$


\begin{aligned}𝑔(𝑥) & =𝑥^{2}+𝑥 \\ 𝑔(𝑔(𝑥)) & =(𝑔(𝑥))^{2}+𝑔(𝑥)\end{aligned}


$$

Then, we substitute ${\color{blue}g(x)} = {\color{red}x^2+x}$ into the right-hand side of the above and simplify, as follows:

$$


\begin{aligned}𝑔(𝑔(𝑥)) & =(𝑔(𝑥))^{2}+𝑔(𝑥) \\ & =(𝑥^{2}+𝑥)^{2}+(𝑥^{2}+𝑥) \\ & =(𝑥^{2}+𝑥)(𝑥^{2}+𝑥)+𝑥^{2}+𝑥 \\ & =(𝑥^{4}+𝑥^{3}+𝑥^{3}+𝑥^{2})+𝑥^{2}+𝑥 \\ & =𝑥^{4}+2𝑥^{3}+2𝑥^{2}+𝑥\end{aligned}


$$

Therefore, $g(g(x)) = x^4+2x^3+2x^2+x.$

### Example: Evaluating a Function With a Variable Input

#### Question

If $f(x) = x^2-1$, then find $f(a+1).$

#### Explanation

To find $f(a+1),$ we write down the function $f$ and replace every occurrence of $x$ with $(a+1)\mathbin{:}$

$$


\begin{aligned}𝑓(𝑥) & =𝑥^{2}−1 \\ 𝑓(𝑎+1) & =(𝑎+1)^{2}−1\end{aligned}


$$

Then, we simplify as follows:

$$


\begin{aligned}𝑓(𝑎+1) & =(𝑎+1)^{2}−1 \\ & =(𝑎+1)(𝑎+1)−1 \\ & =𝑎^{2}+𝑎+𝑎+1−1 \\ & =𝑎^{2}+2𝑎\end{aligned}


$$

Therefore, $f(a+1)=a^2+2a.$

### Example: Solving Equations Involving Composite Function

#### Question

If $f(x) = r + 4x$ and $f(5a+1) = 22a,$ where $a$ and $r$ are constants, find an expression for $r$ in terms of $a.$

#### Explanation

We are given the linear function

$$


f(x) = r + 4x,


$$

and are told that

$$


f(5a+1) = 22a.


$$

To find $f(5a+1)$ in terms of $r,$ we write down the function $f$ and replace every occurence of $x$ with $5a+1{:}$

$$


\begin{aligned}𝑓(𝑥) & =𝑟+4𝑥 \\ 𝑓(5𝑎+1) & =𝑟+4(5𝑎+1)\end{aligned}


$$

Therefore, we simplify $f(5a+1) = 22a$ as follows:

$$


\begin{aligned}𝑓(5𝑎+1) & =22𝑎 \\ 𝑟+4(5𝑎+1) & =22𝑎 \\ 𝑟+20𝑎+4 & =22𝑎\end{aligned}


$$

Finally, we solve for $r{:}$

$$


\begin{aligned}𝑟+20𝑎+4 & =22𝑎 \\ 𝑟 & =22𝑎−20𝑎−4 \\ 𝑟 & =2𝑎−4\end{aligned}


$$
