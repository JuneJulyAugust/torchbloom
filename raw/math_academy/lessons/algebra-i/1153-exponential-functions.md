# Exponential Functions

Source: https://www.mathacademy.com/topics/1153?courseId=44
Topic ID: 1153

## Prerequisites

- [Solving Exponential Equations](./391-solving-exponential-equations.md)
- [Introduction to Functions](./470-introduction-to-functions.md)
- [The Power of Quotient Rule for Exponents](../prealgebra/1289-the-power-of-quotient-rule-for-exponents.md)

## Lesson

### Introduction

An **exponential function** is a function where a variable is contained within an exponent. For example, the function below is an exponential function:

$$


f(x) = 3^x


$$

Just like any other function, we can evaluate it for some particular value of $x,$ say at $x={\color{blue}{4}},$ by substituting this value of $x$ into the function:

$$


f(4) = 3^{\color{blue}{4}} = 81


$$

Another example of an exponential function is $g(x)$ below:

$$


g(x) = 16\cdot \left(\dfrac 1 2\right)^x


$$

We can evaluate this function at $x={\color{blue}{4}}$ using the power of quotient rule, as follows:

$$


\begin{aligned}𝑔(4) & =16⋅(\frac{1}{2})^{4} \\ & =16⋅\frac{1^{4}}{2^{4}} \\ & =16⋅\frac{1}{16} \\ & =1\end{aligned}


$$

Exponential functions are of huge practical importance in science, engineering, economics, and many other disciplines. Let's practice evaluating them.

### Example: Evaluating an Exponential Function

#### Question

If $f(x) = 12 \cdot 2^{x},$ then $f(-4)=$

#### Explanation

To calculate $f(-4),$ we substitute $x=-4$ into the expression for $f(x).$ This gives

$$


\begin{aligned}𝑓(−4) & =12⋅2^{−4} \\ & =12⋅\frac{1}{2^{4}} \\ & =12⋅\frac{1}{16} \\ & =\frac{12}{16} \\ & =\frac{3}{4}.\end{aligned}


$$

### Example: Evaluating a Function in a Modeling Problem

#### Question

The formula $M(t)=128 \cdot \left(\dfrac{1}{4} \right)^{t}$ gives the mass (in grams) of a radioactive calcium isotope after $t$ years. What mass of isotope remains after $3$ years?

#### Explanation

To get the mass of the isotope after $3$ years, we evaluate the function at $t=3.$ Substituting $t=3$ into the function $M(t)$ gives

$$


\begin{aligned}𝑀 & =128(\frac{1}{4})^{𝑡} \\ & =128(\frac{1}{4})^{3} \\ & =128⋅\frac{1^{3}}{4^{3}} \\ & =128⋅\frac{1}{64} \\ & =\frac{128}{64} \\ & =2.\end{aligned}


$$

Therefore, after $3$ years, there will be $2$ grams of isotope remaining.

### Solving for an Unknown Constant

Suppose that we're given the following exponential function:

$$


f(t) = C\cdot 4^t


$$

In addition, we're told that $f(3) = 128.$ Can we use this information to find the unknown constant $C?$

To solve this problem, we substitute $t=3$ and $f(t) = 128$ and solve for $C,$ as follows:

$$


\begin{aligned}128 & =𝐶⋅4^{3} \\ 128 & =𝐶⋅64 \\ \frac{128}{64} & =𝐶 \\ 2 & =𝐶\end{aligned}


$$

Therefore, $C=2.$ So our function expressed in full is

$$


f(t) = 2\cdot 4^t.


$$

We sometimes say that the **initial value** of the function is $2,$ because if we evaluate $f$ at $t=0,$ we get

$$


f(0) = 2\cdot 4^0 = 2\cdot 1 = 2.


$$

### Example: Finding an Initial Value

#### Question

Solve for $C$ given that $y(t) = C \cdot \left(\dfrac{1}{2}\right)^{t}$ and $y(5)=1.$

#### Explanation

We substitute $t=5$ and $y(t)=1$ into the expression for $y(t),$ and get

$$


\begin{aligned}1 & =𝐶⋅(\frac{1}{2})^{5} \\ 1 & =𝐶⋅\frac{1^{5}}{2^{5}} \\ 1 & =𝐶⋅\frac{1}{32} \\ 1⋅32 & =𝐶 \\ 32 & =𝐶.\end{aligned}


$$

Therefore, $C=32.$

### Solving for an Unknown Input Value

Let's consider the following exponential function:

$$


h(x) = 2^x


$$

Can we find the value of $x$ that gives $h(x)=64?$ Indeed, we can. To do this, we'll need to use our knowledge of exponential equations.

First, we use the fact that $h(x)=64$ to write our equation as

$$


2^x = 64.


$$

This is an exponential equation. Since we know that $64$ is a power of $2,$ we can solve this equation as follows:

$$


\begin{aligned}2^{𝑥} & =64 \\ 2^{𝑥} & =2^{6} \\ 𝑥 & =6\end{aligned}


$$

### Example: Solving for an Unknown Input Value

#### Question

Given that $P(x) = 2 \cdot 5^{3x},$ find $x$ such that $P(x)=250.$

#### Explanation

First we substitute $P(x)=250$ into the equation:

$$


2 \cdot 5^{3x}= 250


$$

We can divide both sides of the equation by the constant factor of $2\mathbin{:}$

$$


\begin{aligned}\frac{2⋅5^{3𝑥}}{2} & =\frac{250}{2} \\ \frac{2⋅5^{3𝑥}}{2} & =125 \\ 5^{3𝑥} & =125\end{aligned}


$$

Finally, we solve for $x,$ using the fact that $125$ is a power of $5\mathbin{:}$

$$


\begin{aligned}5^{3𝑥} & =5^{3} \\ 3𝑥 & =3 \\ 𝑥 & =1\end{aligned}


$$
