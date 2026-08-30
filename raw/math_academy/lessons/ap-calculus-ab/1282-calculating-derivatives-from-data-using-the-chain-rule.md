# Calculating Derivatives From Data Using the Chain Rule

Source: https://www.mathacademy.com/topics/1282?courseId=24
Topic ID: 1282

## Prerequisites

- [The Chain Rule With Trigonometric Functions](./305-the-chain-rule-with-trigonometric-functions.md)
- [The Chain Rule With Exponential Functions](./1007-the-chain-rule-with-exponential-functions.md)
- [The Chain Rule With Logarithmic Functions](./1036-the-chain-rule-with-logarithmic-functions.md)
- [Calculating Derivatives From Data and Tables](./1249-calculating-derivatives-from-data-and-tables.md)

## Lesson

### Introduction

In this lesson, we'll learn how to compute derivatives of composite functions when given function data at specific points.

For example, suppose we know the values of two functions, $f(x), g(x),$ and their derivatives at the points $x=1$ and $x=2.$ This data is given in the table below.

Now, let's define a new function $h(x)$ as

$$


h(x)=f(g(x)).


$$

By the chain rule, we have that

$$


h'(x) = f'(g(x)) \cdot g'(x).


$$

To compute, for example, $h'(1),$ we substitute $x=1$ into the expression for $h'(x)$ above.

$$


h'(1) = f'(g(1)) \cdot g'(1)


$$

We can now evaluate this derivative by substituting some values from the table above:

$$


\begin{aligned}ℎ^{′}(1) & =𝑓^{′}(𝑔(1))⋅𝑔^{′}(1) \\ & =𝑓^{′}(2)⋅𝑔^{′}(1) \\ & =5⋅(−4) \\ & =−20\end{aligned}


$$

So, we conclude that $h'(1) = -20.$

### Example: Applying the Chain Rule Given Data For Two Functions

#### Question

The table below shows the values of functions $f,$ $g,$ $f',$ and $g'$ at $x=1$ and $x=2.$ Find $h'(2),$ if $h(x)=g(f(x)).$

#### Explanation

The chain rule gives

$$


h'(x) = g'(f(x)) \cdot f'(x).


$$

Evaluating at $x=2$ and using the values given in the table, we have

$$


\begin{aligned}ℎ^{′}(2) & =𝑔^{′}(𝑓(2))⋅𝑓^{′}(2) \\ & =𝑔^{′}(1)⋅𝑓^{′}(2) \\ & =4⋅2 \\ & =8.\end{aligned}


$$

### Using the Chain Rule With the Power Rule

Let's now suppose we have the following data regarding the function $f(x)$ and its derivative $f'(x){:}$

$$


f(-1)={\color{blue}2}, \qquad\qquad f'(-1)={\color{red}-8}


$$

Let's use this data to evaluate the following derivative:

$$


\dfrac{\textrm{d}}{\textrm{d}x}\left.\left(\dfrac{1}{f(x)}\right)\right|_{x=-1}


$$

First, we find an expression for the derivative using the chain rule:

$$


\begin{aligned}\frac{d}{d𝑥}(\frac{1}{𝑓(𝑥)}) & =\frac{d}{d𝑥}(𝑓(𝑥))^{−1} \\ & =−(𝑓(𝑥))^{−2}⋅𝑓^{′}(𝑥) \\ & =−\frac{1}{(𝑓(𝑥))^{2}}⋅𝑓^{′}(𝑥) \\ & =−\frac{𝑓^{′}(𝑥)}{(𝑓(𝑥))^{2}}\end{aligned}


$$

Now, evaluating this expression at $x = -1$, we get

$$


\begin{aligned}\frac{d}{d𝑥}(\frac{1}{𝑓(𝑥)})_{𝑥=−1} & =−\frac{𝑓^{′}(−1)}{(𝑓(−1))^{2}} \\ & =−\frac{(−8)}{2^{2}} \\ & =\frac{8}{4} \\ & =2.\end{aligned}


$$

### Example: Applying the Chain Rule With the Power Rule

#### Question

The values of the function $f(x)$ and its derivative at $x=-1$ are given in the table below.

Find $g'\left(-1\right)$, if $g(x)=\sqrt[3]{f(x)}.$

#### Explanation

Using the chain rule, we get

$$


\begin{aligned}𝑔^{′}(𝑥) & =\frac{d}{d𝑥}(\sqrt[√𝑓(𝑥)]{3}) \\ & =\frac{d}{d𝑥}(𝑓(𝑥))^{1/3} \\ & =\frac{1}{3}(𝑓(𝑥))^{−2/3}⋅𝑓^{′}(𝑥) \\ & =\frac{1}{3(\sqrt[√𝑓(𝑥)]{3})^{2}}⋅𝑓^{′}(𝑥).\end{aligned}


$$

Evaluating at $x = -1$ and using the values given in the table, we have

$$


\begin{aligned}𝑔^{′}(−1) & =\frac{1}{3(\sqrt[√𝑓(−1)]{3})^{2}}⋅𝑓^{′}(−1) \\ & =\frac{1}{3(\sqrt[√8]{3})^{2}}⋅(−2) \\ & =\frac{1}{3⋅4}⋅(−2) \\ & =−\frac{1}{6}\end{aligned}


$$

### Example: Applying the Chain Rule With Trigonometric Functions

#### Question

Given that $f(1)=\dfrac{\pi}{2}$ and $f'(1)=-\dfrac{3\pi}{4},$ compute $\dfrac{\textrm{d}}{\textrm{d}x}\big(\cos{\left(f(x)\right)}\big)$ at $x=1.$

#### Explanation

Using the chain rule, we get

$$


\begin{aligned}\frac{d}{d𝑥}\,(cos⁡(𝑓(𝑥))) & =−sin⁡(𝑓(𝑥))⋅𝑓^{′}(𝑥).\end{aligned}


$$

Evaluating at $x=1$ and using the values given in the table, we have

$$


\begin{aligned}\frac{d}{d𝑥}\,(cos⁡(𝑓(𝑥)))_{𝑥=1} & =−sin⁡(𝑓(1))⋅𝑓^{′}(1) \\ & =−sin⁡(\frac{𝜋}{2})⋅(−\frac{3𝜋}{4}) \\ & =−1⋅(−\frac{3𝜋}{4}) \\ & =\frac{3𝜋}{4}.\end{aligned}


$$

### Example: Applying the Chain Rule With Exponential and Logarithmic Functions

#### Question

The values of the function $f(x)$ and its derivative at $x = -3$ are given in the table below.

Find $w'(-3),$ if $w(x) = e^{f(x)}.$

#### Explanation

Using the chain rule, we get

$$


w'(x) = e^{f(x)} \cdot f'(x).


$$

Evaluating at $x = -3$ and using the values given in the table, we have

$$


\begin{aligned}𝑤^{′}(−3) & =𝑒^{𝑓(−3)}⋅𝑓^{′}(−3) \\ & =𝑒^{−2}⋅𝑒^{4} \\ & =𝑒^{−2+4} \\ & =𝑒^{2}.\end{aligned}


$$
