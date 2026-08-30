# Homogeneous Functions

Source: https://www.mathacademy.com/topics/2536?courseId=61
Topic ID: 2536

## Prerequisites

- [The Domain of a Multivariable Function](../multivariable-calculus/1899-the-domain-of-a-multivariable-function.md)

## Lesson

### Introduction

We say that a function $f(x,y)$ is **homogeneous of degree $\boldsymbol n$** if it satisfies

$$


f(tx,ty) = t^n f(x,y).


$$

In other words, if we scale the function's arguments by some scale factor $t,$ then the output of the function scales by the $n$th power of that scale factor.

- For example, the function $g(x,y)=2x+y$ is homogeneous of degree $1$ because it satisfies

- Likewise, the function $h(x,y) = x^2-y^2$ is homogeneous of degree $2$ because it satisfies

The definition of a homogeneous function of degree $n$ extends to functions of any number of variables. For example, a function of $3$ variables $F(x,y,z)$ is homogeneous of degree $n$ if it satisfies

$$


F(tx,ty,tz) = t^nF(x,y,z).


$$

Knowledge of homogeneous functions can help us to solve certain types of differential equations. So let's explore them a little more.

### Example: Determining the Degree of a Homogeneous Polynomial

#### Question

Is the function $f(x,y,z) = x^3+2y^3+z^3$ homogeneous? If so, what is its degree?

#### Explanation

A function $f(x,y,z)$ is homogeneous of degree $n$ if it satisfies the property

$$


f(tx,ty, tz) = t^nf(x,y, z).


$$

So first, we compute $f(tx,ty,tz),$ and then we simplify by writing it as $t^n f(x,y,z)$ for some $n\mathbin{:}$

$$


\begin{aligned}𝑓(𝑡𝑥,𝑡𝑦,𝑡𝑧) & =(𝑡𝑥)^{3}+2(𝑡𝑦)^{3}+(𝑡𝑧)^{3} \\ & =𝑡^{3}𝑥^{3}+2𝑡^{3}𝑦^{3}+𝑡^{3}𝑧^{3} \\ & =𝑡^{3}(𝑥^{3}+2𝑦^{3}+𝑧^{3}) \\ & =𝑡^{3}𝑓(𝑥,𝑦,𝑧)\end{aligned}


$$

Therefore, we conclude that

$$


f(tx,ty,tz) = t^3 f(x,y,z)


$$

and so the function $f(x,y,z)$ is homogeneous of degree $3.$

### Determining the Degree of a Homogeneous Polynomial Using the Fast Method

There is a quick way to determine whether a polynomial function is homogeneous:

Given a polynomial function $p,$ if the degree of each of the polynomial terms is $n,$ then $p$ is homogeneous of degree $n.$

For example, the function $f(x,y,z) = x^3+2xy^2+z^3$ is homogeneous of degree $3$ because it is a polynomial and each of the terms has degree $3.$

On the other hand, the function $g(x,y,z) = x^3 + xy + yz^2$ is *not* homogeneous. It is a polynomial, but not all the terms have the same degree. Here, the middle term has degree $2$ while the other terms have degree $3.$

### Example: Determining the Degree of a Homogeneous Polynomial Using the Fast Method

#### Question

Which of the following polynomials are homogeneous?

1. $f(x,y) = x^2+x+y$

2. $g(x,y) = x^6-2x^3y^3 + y^6$

3. $h(x,y) = 6$

#### Explanation

Let's go through each of the options.

- The function $f(x,y)$ is not homogeneous. It is a polynomial of degree $2,$ but not all the terms have the same degree. The first term has degree $2,$ while the other terms have degree $1.$

- The function $g(x,y)$ is homogeneous of degree $6$. It is a polynomial of degree $6,$ and all of its terms are of degree $6.$

- The function $h(x,y)$ is homogeneous of degree $0$. It is a polynomial of degree $0,$ and all of its terms are of degree $0.$ (There is only one term, and it has degree $0.$)

Therefore, the correct answer is "II and III only.

### The Degree of a Homogeneous Rational Function

Suppose that we have the rational function $h(x,y),$ defined as follows:

$$


h(x,y) = \dfrac{x^2-y^2}{x^2+y^2}


$$

Is this function homogeneous? If so, what is its degree?

To answer this question, we have two methods available to us. The second is much shorter than the first, but let's go through both.

**Method 1**

We note that

- the numerator of $h(x,y)$ is a homogeneous polynomial of degree $2,$ and

- the denominator of $h(x,y)$ is a homogeneous polynomial of degree $2.$

Therefore, the function $h(x,y)$ is homogeneous of degree $2-2 = 0.$

So, we conclude that

$$


h(tx,ty) = t^0h(x,y) = h(x,y).


$$

**Method 2**

A function $h(x,y)$ is homogeneous of degree $n$ if it satisfies the property

$$


h(tx,ty) = t^nh(x,y).


$$

So first, we compute $h(tx,ty),$ and then we simplify by writing it as $t^n h(x,y)$ for some $n\mathbin{:}$

$$


\begin{aligned}ℎ(𝑡𝑥,𝑡𝑦) & =\frac{(𝑡𝑥)^{2}−(𝑡𝑦)^{2}}{(𝑡𝑥)^{2}+(𝑡𝑦)^{2}} \\ & =\frac{𝑡^{2}𝑥^{2}−𝑡^{2}𝑦^{2}}{𝑡^{2}𝑥^{2}+𝑡^{2}𝑦^{2}} \\ & =\frac{𝑡^{2}(𝑥^{2}−𝑦^{2})}{𝑡^{2}(𝑥^{2}+𝑦^{2})} \\ & =\frac{𝑥^{2}−𝑦^{2}}{𝑥^{2}+𝑦^{2}} \\ & =ℎ(𝑥,𝑦)\end{aligned}


$$

Therefore, we conclude that

$$


h(tx,ty) = h(x,y) = t^0h(x,y)


$$

and so the degree of the homogeneous function $h(x,y)$ is $0.$

**Note:** Functions that are homogeneous of degree $0$ satisfy $f(tx,ty) = f(x,y).$ In general, rational functions where all terms have the same polynomial order (like $h(x,y)$ above) are homogeneous of degree $0.$

### Example: Determining the Degree of a Homogeneous Rational Function

#### Question

What is the degree of the homogeneous function defined as

#### Explanation

****

We note that

- the numerator of is a homogeneous polynomial of degree and

- the denominator of is a homogeneous polynomial of degree

Therefore, the function is homogeneous of degree

****

A function is homogeneous of degree if it satisfies the property

So first, we compute and then we simplify by writing it as for some:

Therefore, we conclude that

and so the degree of the homogeneous function is

### Example: Determining the Degree of a Homogeneous Function

#### Question

Find the degree of the homogeneous function $g(x,y) = \dfrac{1}{x}\cos\left(\dfrac{y}{x}\right).$

#### Explanation

A function $g(x,y)$ is homogeneous of degree $n$ if it satisfies the property

$$


g(tx,ty) = t^ng(x,y).


$$

So first, we compute $g(tx,ty),$ and then we simplify by writing it as $t^n g(x,y)$ for some $n\mathbin{:}$

$$


\begin{aligned}𝑔(𝑡𝑥,𝑡𝑦) & =\frac{1}{𝑡𝑥}cos⁡(\frac{𝑡𝑦}{𝑡𝑥}) \\ & =\frac{1}{𝑡𝑥}cos⁡(\frac{𝑦}{𝑥}) \\ & =\frac{1}{𝑡}⋅\frac{1}{𝑥}cos⁡(\frac{𝑦}{𝑥}) \\ & =𝑡^{−1}⋅\frac{1}{𝑥}cos⁡(\frac{𝑦}{𝑥}) \\ & =𝑡^{−1}𝑔(𝑥,𝑦)\end{aligned}


$$

Therefore, we conclude that

$$


g(tx,ty) = t^{-1} g(x,y)


$$

and so the degree of the homogeneous function $g(x,y)$ is $-1.$
