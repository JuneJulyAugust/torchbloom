# Further Solving First-Order ODEs by Substitution

Source: https://www.mathacademy.com/topics/3628?courseId=61
Topic ID: 3628

## Prerequisites

- [Integrating Functions Using Polynomial Division](../../../ap-courses/lessons/ap-calculus-ab/338-integrating-functions-using-polynomial-division.md)
- [Integrating Rational Functions Using Partial Fractions](../../../ap-courses/lessons/ap-calculus-bc/445-integrating-rational-functions-using-partial-fractions.md)
- [Solving First-Order ODEs by Substitution](./3179-solving-first-order-odes-by-substitution.md)

## Lesson

### Introduction

Suppose that we're given a differential equation of the form

$$


y' = F(x,y).


$$

By factoring the function $F(x,y),$ we can often convert this differential equation to one that is of the form

$$


y' = f ( a x + b y ),


$$

where $a$ and $b$ are real constants. Then, using the substitution $z= ax+by,$ we can convert the equation to a separable differential equation.

To illustrate, let's consider the differential equation

$$


y' = 9x^2 - 6xy + y^2.


$$

Notice that the right-hand side is a perfect square. So, we factor it as follows:

$$


\begin{aligned}𝑦^{′}=(3𝑥−𝑦)^{2}\end{aligned}


$$

Then, we make the substitution

$$


z = 3x - y.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = 3 - \,\dfrac{\text{d}y}{\text{d}x} \quad \Rightarrow\quad \dfrac{\text{d}y}{\text{d}x} = 3 - \,\dfrac{\text{d}z}{\text{d}x}


$$

Therefore, we can write our equation in terms of $z$ as

$$


3 - \,\dfrac{\text{d}z}{\text{d}x} = z^2,


$$

which simplifies to

$$


\dfrac{\text{d}z}{\text{d}x} = 3-z^2.


$$

We now have a separable differential equation.

### Example: Reducing a First-Order ODE to a Separable Form by Factoring and Using a Linear Substitution

#### Question

Consider the differential equation

$$


\dfrac{\text{d}y}{\text{d}x} = 2xy - x^2 - y^2.


$$

Using a substitution of the form $z= x - y,$ transform the differential equation into an equation of the form $z'(x) = f(z).$ What is the function $f(z)?$

#### Explanation

First, we factor the right-hand side of the given equation, and we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =−(𝑥−𝑦)^{2}.\end{aligned}


$$

Then, we make the substitution

$$


z = x - y.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = 1 - \dfrac{\text{d}y}{\text{d}x} \quad \Longrightarrow\quad \dfrac{\text{d}y}{\text{d}x} = 1 - \dfrac{\text{d}z}{\text{d}x}.


$$

Therefore, the original equation can be written in terms of $z$ as follows:

$$


\begin{aligned}1−\frac{d𝑧}{d𝑥} & =−𝑧^{2}\end{aligned}


$$

Expressing this equation in the form $z'(x) = f(z),$ we get

$$


\dfrac{\text{d}z}{\text{d}x} = z^2 + 1.


$$

Therefore, $f(z) = z^2 + 1.$

### Example: Solving a First-Order ODE by Factoring and Using a Linear Substitution

#### Question

Consider the differential equation

$$


\dfrac{\text{d}y}{\text{d}x} = \dfrac{1 - x - y}{x + y}.


$$

The general solution to this equation can be expressed in the form

$$


g(x,y) = 2x + C,


$$

where $C$ is a constant. What is $g(x,y)?$

#### Explanation

First, we factor the right-hand side of the given equation.

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{1−(𝑥+𝑦)}{𝑥+𝑦}\end{aligned}


$$

Then, we make the substitution

$$


z = x+y.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = 1 + \dfrac{\text{d}y}{\text{d}x} \quad\Longrightarrow\quad \dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{d}z}{\text{d}x} - 1.


$$

Therefore, the original equation can be written in terms of $z$ as follows:

$$


\begin{aligned}\frac{d𝑧}{d𝑥}−1 & =\frac{1−𝑧}{𝑧}\end{aligned}


$$

Expressing this equation in the form $z'(x) = f(z)$ gives

$$


\dfrac{\text{d}z}{\text{d}x} = \dfrac{1}{z}.


$$

This differential equation is separable. So, we separate the variables and integrate both sides with respect to $x\mathbin{:}$

$$


\begin{aligned}𝑧\,\frac{d𝑧}{d𝑥} & =1 \\ ∫𝑧\,d𝑧 & =∫d𝑥 \\ \frac{𝑧^{2}}{2} & =𝑥+𝐾 \\ 𝑧^{2} & =2𝑥+𝐶\end{aligned}


$$

where $C = 2K.$

Finally, we write the equation in terms of $y$ and $x$ using our original substitution, as follows:

$$


(x+y)^2 = 2x + C


$$

Therefore,

$$


g(x,y) = (x+y)^2.


$$
