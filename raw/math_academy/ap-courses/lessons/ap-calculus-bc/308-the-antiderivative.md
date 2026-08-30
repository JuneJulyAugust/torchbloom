# The Antiderivative

Source: https://www.mathacademy.com/topics/308?courseId=21
Topic ID: 308

## Prerequisites

- [The Power Rule for Differentiation](../ap-calculus-ab/35-the-power-rule-for-differentiation.md)

## Lesson

### Introduction

An **antiderivative** is the *opposite* of a derivative. For example:

- Using the power rule, we know that the *derivative* of $\color{blue}x^2$ is ${\color{red}2x}.$

- Going in the *opposite* direction, we say that an **antiderivative** of $\color{red}2x$ is ${\color{blue}x^2}.$

For any given function, there are infinitely many antiderivatives. For example:

- The derivative of $\color{blue}x^2$ is ${\color{red}2x},$ so an *antiderivative* of $\color{red}2x$ is ${\color{blue}x^2}.$

- The derivative of $\color{blue}x^2+1$ is ${\color{red}2x},$ so another *antiderivative* of $\color{red}2x$ is ${\color{blue}x^2+1}.$

- The derivative of $\color{blue}x^2+2$ is ${\color{red}2x},$ so another *antiderivative* of $\color{red}2x$ is ${\color{blue}x^2+2}.$

- ...

In general, all the antiderivatives of $\color{red}2x$ can be written in the form ${\color{blue}x^2+C},$ where $C$ is a constant.

To represent the antiderivative symbolically, we use a special symbol $\displaystyle \int$ called the **integral** symbol. So, using **integral notation**, we can write

$$


\int 2x \, \textrm d x = x^2 + C


$$

where $C$ represents an arbitrary constant and is called the **constant of integration**.

In words, $\displaystyle \int 2x \, \textrm d x$ is said as “the integral of $2x$ with respect to $x$” or “the antiderivative of $2x$.” Integrals like this are called **indefinite integrals**, and the function being **integrated** ($2x$ in this case) is called the **integrand**.

### The Power Rule for Integration

To compute the integral of any power function $x^n,$ where $n \neq -1,$ we can use the **power rule for integration**. The power rule for integration states that

$$


\int x^n\, \text{d}x = \dfrac {x^{n + 1}}{n + 1} + C,


$$

where $C$ is any constant and $n\neq -1.$ For example, in the case of $n=3,$ we have

$$


\begin{aligned}∫𝑥^{3}\,d𝑥 & =\frac{𝑥^{3+1}}{3+1}+𝐶 \\ & =\frac{𝑥^{4}}{4}+𝐶.\end{aligned}


$$

So the **antiderivative** of $f'(x) = x^3$ is $f(x) = \dfrac {x^{4}}{4}+C.$

We can check that this is the correct answer by taking the derivative of $f(x)$ and seeing that it is indeed equal to $x^3\mathbin{:}$

$$


\begin{aligned}\frac{d}{d𝑥}(\frac{𝑥^{4}}{4}+𝐶) & = \\ \frac{d}{d𝑥}(\frac{𝑥^{4}}{4})+\frac{d}{d𝑥}(𝐶) & = \\ \frac{1}{4}(\frac{d}{d𝑥}𝑥^{4})+0 & = \\ \frac{1}{4}⋅4𝑥^{4−1} & = \\ 𝑥^{3}\,✓ & \end{aligned}


$$

Notice that the constant $C$ disappeared when we differentiated because the derivative of any constant is zero. We always add $+C$ whenever we find the antiderivative of a function because we know that it will disappear when we differentiate.

**Note:** The power rule for integration is just the power rule for differentiation in reverse!

$$


\dfrac{\text{d}}{\text{d}x} \left( x^{n+1} \right) = (n+1)x^n \quad \Leftrightarrow \quad \displaystyle \int x^n \, \textrm dx = \dfrac{x^{n+1}}{n+1}


$$

### Example: Finding the Antiderivative of a Monomial

#### Question

Calculate $\displaystyle \int x^2 \,\textrm d x.$

#### Explanation

We apply the power rule with $n=2$, and we get

$$


\int x^2 \,\textrm d x = \dfrac{x^{2+1}}{2+1} + C = \dfrac{x^3}{3}+C.


$$

Let's check by differentiating:

$$


\begin{aligned}\frac{d}{d𝑥}(\frac{𝑥^{3}}{3}+𝐶) & = \\ \frac{d}{d𝑥}(\frac{𝑥^{3}}{3})+\frac{d}{d𝑥}(𝐶) & = \\ \frac{1}{3}\frac{d}{d𝑥}(𝑥^{3})+0 & = \\ \frac{1}{3}⋅3𝑥^{2} & = \\ 𝑥^{2}\,✓ & \end{aligned}


$$

### Example: Finding the Antiderivative of a Radical Function

#### Question

Find the antiderivative of $\sqrt x.$

#### Explanation

We start by writing the square root as a rational power, $\sqrt x= x^{1/2}.$ So, we can apply the power rule with $n=\dfrac{1}{2}$ and get

$$


\begin{aligned}∫\sqrt{𝑥}\,d𝑥 & =∫𝑥^{1/2}\,d𝑥 \\ & =\frac{𝑥^{1/2+1}}{(\frac{1}{2}+1)}+𝐶 \\ & =\frac{𝑥^{3/2}}{(\frac{3}{2})}+𝐶 \\ & =\frac{2𝑥^{3/2}}{3}+𝐶.\end{aligned}


$$

Again, let's check by differentiating:

$$


\begin{aligned}\frac{d}{d𝑥}(\frac{2𝑥^{3/2}}{3}+𝐶) & = \\ \frac{d}{d𝑥}(\frac{2𝑥^{3/2}}{3})+\frac{d}{d𝑥}(𝐶) & = \\ \frac{2}{3}\frac{d}{d𝑥}(𝑥^{3/2})+0 & = \\ \frac{2}{3}⋅\frac{3}{2}𝑥^{3/2−1} & = \\ 𝑥^{1/2}\,✓ & \end{aligned}


$$

### Example: Finding the Antiderivative of a Reciprocal Function

#### Question

Given that $f(x) = \dfrac 1 {x^3}$ and that $F'(x) = f(x)$, calculate $F(x).$

#### Explanation

Remember that integration is the opposite of differentiation. So, if $F'(x) = f(x),$ then integrating both sides of this equation gives

$$


\begin{aligned}𝐹^{′}(𝑥) & =𝑓(𝑥) \\ ∫𝐹^{′}(𝑥)\,d𝑥 & =∫𝑓(𝑥)\,d𝑥 \\ 𝐹(𝑥) & =∫𝑓(𝑥)\,d𝑥.\end{aligned}


$$

Note that $\dfrac 1 {x^3}= x^{-3}.$ So, we can use the power rule with $n=-3$ and get

$$


\begin{aligned}𝐹(𝑥) & =∫𝑓(𝑥)\,d𝑥 \\ & =∫\frac{1}{𝑥^{3}}\,d𝑥 \\ & =∫𝑥^{−3}\,d𝑥 \\ & =\frac{𝑥^{−3+1}}{−3+1}+𝐶 \\ & =−\frac{𝑥^{−2}}{2}+𝐶 \\ & =−\frac{1}{2𝑥^{2}}+𝐶.\end{aligned}


$$

### Some Final Notes on Indefinite Integrals and Constants

Let's recap the main points:

- Integrals like $\displaystyle \int x^3\,\textrm d x$ are called **indefinite integrals**.

- Whenever we calculate an indefinite integral, we must always remember to add an **arbitrary constant** $+C.$

- To integrate power functions, we can use the **power rule for integration**, which states that provided that $n \neq -1.$ To emphasize, the power rule does *not* work when $n=-1.$ So we cannot use the above formula to work out $\displaystyle \int \dfrac{1}{x}\,\textrm d x.$ Integrals like this need to be handled differently, and you'll find out how soon.
