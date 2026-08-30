# General Solutions of First-Order Linear ODEs

Source: https://www.mathacademy.com/topics/6678?courseId=154
Topic ID: 6678

## Prerequisites

- [Introduction to First-Order Linear ODEs](./906-introduction-to-first-order-linear-odes.md)
- [Solving Systems of Equations Using Back Substitution](./1047-solving-systems-of-equations-using-back-substitution.md)
- [Solving First-Order IVPs Using Separation of Variables](./1179-solving-first-order-ivps-using-separation-of-variables.md)
- [Equating Polynomial Coefficients](../algebra-i/6092-equating-polynomial-coefficients.md)

## Lesson

### Introduction

Recall that a linear first-order homogeneous differential equation in the variable $y = y(x)$ takes the form

$$


a(x)y'(x)+b(x)y(x)= 0.


$$

For example, the equation

$$


\frac{\textrm{d} y}{\textrm{d} x} + 6xy = 0


$$

is a linear first-order homogeneous ODE with $a(x) = 1$ and $b(x) = 6x.$ Notice that the right-hand side is identical to zero.

A linear first-order *inhomogeneous* differential equation is similar, except the right-hand side is *not* identical to zero. So, a linear first-order inhomogeneous differential equation can be written as

$$


a(x)y'(x)+b(x)y(x)= f(x).


$$

The function $f(x)$ is often called the **forcing function.** We say that a first-order ODE has **polynomial forcing** if $f(x)$ is a polynomial.

For example, the equation

$$


\frac{\textrm{d} y}{\textrm{d} x} + 6xy = 2x


$$

is a linear first-order inhomogeneous ODE with polynomial forcing because the right-hand side, $f(x) = 2x,$ is a nonzero polynomial.

In this lesson, we will learn how to find general solutions to linear first-order ODEs with polynomial forcing.

### A Three-Step Process for Solving First-Order Inhomogeneous ODEs

We wish to construct the general solution to the first-order linear inhomogeneous ODE

$$


a(x)y'(x) + b(x)y(x) = f(x).


$$

There are several ways to find the general solution to a first-order inhomogeneous ODE. The method we'll discuss here is a three-step process that involves finding the sum of the so-called complementary and particular solutions.

The three steps are as follows:

- **Step 1:** Find the **complementary solution** (or the **homogeneous solution**) $y_c(x)$ that satisfies the associated homogeneous ODE

- **Step 2:** Find a **particular solution** $y_p(x)$ of the inhomogeneous ODE. This is a single function that satisfies the inhomogeneous equation.

- **Step 3:** Write the general solution as the sum of the complementary solution and the particular solution:

As we'll see, this method generalizes to higher-order linear ODEs, so it's well worth understanding how it works for first-order ODEs.

Let's begin by practicing finding the complementary solution to an equation.

### Finding a Complementary Solution

Let's find the complementary solution to the following inhomogeneous ODE:

$$


y' + 10y = x - 8.


$$

To find the complementary solution $y_c,$ we solve the corresponding homogeneous ODE. We start by setting the right-hand side equal to zero:

$$


y'_c + 10y_c = 0.


$$

Notice that this differential equation is separable since we can write it as

$$


\dfrac{\textrm{d}y_c}{\textrm{d}x} = -10y_c.


$$

We separate the variables as follows:

$$


\dfrac{1}{y_c}\,\textrm{d}y_c = -10\,\textrm{d}x.


$$

Then, we integrate both sides with respect to $x{:}$

$$


\begin{aligned}∫\frac{1}{𝑦_{𝑐}}\,d𝑦_{𝑐} & =∫−10\,d𝑥 \\ ln⁡|𝑦_{𝑐}| & =−10𝑥+𝐶.\end{aligned}


$$

Next, we make $y_c$ the subject by exponentiating both sides:

$$


\begin{aligned}|𝑦_{𝑐}| & =𝑒^{−10𝑥+𝐶} \\ & =𝑒^{−10𝑥}𝑒^{𝐶} \\ & =𝐾𝑒^{−10𝑥},\end{aligned}


$$

where $K=e^{C}.$

Finally, we can drop the absolute value by allowing the constant to be positive or negative (absorbing the sign into the constant). Therefore, the complementary solution is

$$


y_c(x)=Ae^{-10x},


$$

where $A$ is an arbitrary constant.

### Example: Finding the Complementary Solution to a First-Order Inhomogeneous ODE

#### Question

Consider the differential equation

$$


y' + y = -10.


$$

Find the complementary solution $y_c(x)$ to this equation.

#### Explanation

To find the complementary solution, we solve the corresponding homogeneous equation, given by

$$


y'_c + y_c = 0.


$$

Notice that this differential equation is separable since we can write it as

$$


\dfrac{\textrm{d}y_c}{\textrm{d}x} = -y_c.


$$

Therefore, we separate the variables as follows:

$$


\dfrac{1}{y_c} \cdot \dfrac {\textrm{d}y_c} {\textrm{d}x} = -1


$$

Then, we integrate both sides with respect to $x{:}$

$$


\begin{aligned}∫\frac{1}{𝑦_{𝑐}}\,\frac{d𝑦_{𝑐}}{d𝑥}\,d𝑥 & =∫−1\,d𝑥 \\ ∫\frac{1}{𝑦_{𝑐}}\,d𝑦_{𝑐} & =∫−1\,d𝑥 \\ ln⁡|𝑦_{𝑐}| & =−𝑥+𝐶\end{aligned}


$$

Next, we make $y_c$ the subject by exponentiating both sides:

$$


\begin{aligned}|𝑦_{𝑐}| & =𝑒^{−𝑥+𝐶} \\ & =𝑒^{−𝑥}𝑒^{𝐶} \\ & =𝐾𝑒^{−𝑥}\end{aligned}


$$

where $K= e^{C}.$

Finally, we can drop the absolute value by allowing the arbitrary constant to be either positive or negative, i.e., setting $A = \pm K.$ Therefore, the complementary solution is

$$


y_c = A e^{-x},


$$

where $A$ is an arbitrary constant.

### Finding a Particular Solution

We've discussed how to find the complementary solution $y_c(x)$ of a first-order inhomogeneous ODE

$$


a(x)y'(x)+b(x)y(x)= f(x).


$$

We will now turn our attention to finding a **particular solution.**

The particular solution $y_p(x)$ of a linear ODE captures the part of the solution that arises directly from the forcing term $f(x).$ In other words, if we substitute $y_p(x)$ into the left-hand side of the equation, it should produce the forcing function $f(x).$

For equations with constant coefficients, we can often find $y_p(x)$ by looking at the type of function appearing on the right-hand side and then guessing a form that matches it. This is sometimes called **the method of undetermined coefficients.**

For example, if the forcing function $f(x)$ is a polynomial of degree $n,$ we guess a particular solution that is also a polynomial of degree $n.$ After making this guess, we substitute it into the differential equation and solve for the unknown constants.

Next, we'll work through a concrete example where $f(x)$ is a linear polynomial.

### A Worked Example

Consider the inhomogeneous differential equation

$$


\frac{\textrm{d} y}{\textrm{d} x} - 5 y = 5x-16.


$$

Here, the forcing term

$$


f(x) = 5x - 16


$$

is a polynomial of degree $1.$ Therefore, we assume that the particular solution is also a polynomial of degree $1,$ so we guess

$$


y_p(x)=\alpha x + \beta,


$$

where $\alpha$ and $\beta$ are constants to be determined.

Calculating the derivative gives

$$


\frac{\textrm{d}y_p}{\textrm{d}x} = \alpha.


$$

Now substitute $y_p$ and $\dfrac{\textrm{d}y_p}{\textrm{d}x}$ into the differential equation:

$$


\alpha - 5(\alpha x + \beta ) = 5x-16.


$$

Next, group the terms proportional to $x$ and the constants:

$$


-5\alpha x + (\alpha - 5\beta) = 5x-16.


$$

Equating coefficients on both sides gives

$$


\begin{aligned}\begin{aligned}−5𝛼=5\, & (equating the coefficients of\,\,𝑥) \\ 𝛼−5𝛽=−16\, & (equating the constants)\end{aligned}\end{aligned}


$$

Solving this system gives $\alpha=-1$ and $\beta=3.$ Therefore,

$$


y_p(x) = -x+3.


$$

Let's see another example where the forcing function is a quadratic polynomial.

### Example: Finding a Particular Solution to a First-Order Inhomogeneous ODE With Polynomial Forcing

#### Question

Consider the differential equation

$$


\frac{\textrm{d} y}{\textrm{d} x} + y = x ^ 2 + 2x - 3.


$$

Find the particular solution $y_p(x)$ to this equation.

#### Explanation

The right-hand side of the inhomogeneous equation is a polynomial of degree $2.$ Therefore, we assume that the particular solution is also a polynomial of degree $2,$ i.e.,

$$


y_p(x)=\alpha x^2 + \beta x + \gamma


$$

where $\alpha,$ $\beta,$ and $\gamma$ are constants to be determined.

Calculating the first derivative of $y_p$ gives

$$


\frac{\textrm{d}y_p}{\textrm{d}x} = 2\alpha x+\beta.


$$

To find the values of $\alpha,$ $\beta$ and $\gamma,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


(2\alpha x+\beta) + (\alpha x^2 + \beta x + \gamma) = x ^ 2 + 2x - 3


$$

Grouping the terms on the left-hand side gives

$$


\alpha x^2 + (2\alpha+ \beta)x + (\beta+ \gamma) = x ^ 2 + 2x - 3.


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{aligned}𝛼=1\, & (equating the coefficients of\,\,𝑥^{2}) \\ 2𝛼+𝛽=2\, & (equating the coefficients of\,\,𝑥) \\ 𝛽+𝛾=−3\, & (equating the constants)\end{aligned}\end{aligned}


$$

Solving this system gives $\alpha=1, \beta=0, \gamma=-3.$

Therefore, the particular integral $y_p(x)$ is

$$


y_p(x) = x ^ 2 - 3.


$$

### Constructing the General Solution

Now that we've practiced finding both the complementary and particular solutions, let's put them together to find the **general solution**.

Recall that the complementary solution $y_c(x)$ comes from solving the associated homogeneous equation. It contains an arbitrary constant, so it represents all homogeneous solutions.

The particular solution $y_p(x)$ is one specific function that satisfies the full inhomogeneous equation.

To find the general solution, we add these two pieces:

$$


y(x) = y_c(x) + y_p(x).


$$

The particular solution already satisfies the full equation. Adding any complementary solution preserves this property while introducing the arbitrary constant needed to match different initial conditions.

In this way, the formula above describes *every possible solution* of a linear inhomogeneous equation.

Let's consider an example.

### A Worked Example

Consider the differential equation

$$


3\frac{\textrm{d} y}{\textrm{d} x} + 2y = 16.


$$

We will find its general solution by computing the complementary and particular solutions.

First, we find the complementary solution by solving the associated homogeneous equation:

$$


3 \frac{\textrm{d} y_c}{\textrm{d} x} + 2y_c = 0.


$$

Solving this equation using separation of variables gives

$$


y_c(x) = Ae^{-2/3x},


$$

where $A$ is an arbitrary constant.

Next, we will find a particular solution. To find a particular solution of

$$


3\frac{\textrm{d} y}{\textrm{d} x} + 2y = 16,


$$

note that the forcing term is a polynomial of degree $0.$

Therefore, we assume the particular solution is also a constant:

$$


y_p(x)=\beta.


$$

Its derivative is

$$


\frac{\textrm{d}y_p}{\textrm{d}x} = 0.


$$

Substituting $y_p$ and its derivative into the differential equation gives

$$


3\cdot 0 + 2\beta = 16.


$$

Solving yields $\beta = 8,$ so

$$


y_p(x) = 8.


$$

Finally, the general solution is

$$


y(x) = y_c(x) + y_p(x) = Ae^{-2/3x} + 8.


$$

### Example: Finding the General Solution to a First-Order Inhomogeneous ODE With Polynomial Forcing

#### Question

Consider the differential equation

$$


\frac{\textrm{d} y}{\textrm{d} x} + 2y = -2x + 5.


$$

Find the general solution to this equation given that the complementary solution is $y_c(x) = Ae^{-2x},$ where $A$ is an arbitrary constant.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c,$ we solve the corresponding homogeneous equation, given by

$$


\frac{\textrm{d} y_c}{\textrm{d} x} + 2y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{-2x}


$$

where $A$ is an arbitrary constant.

We now need to find the particular solution $y_p(x).$

The right-hand side of the inhomogeneous equation is a polynomial of degree $1.$ Therefore, we assume that the particular solution is also a polynomial of degree $1,$ i.e.,

$$


y_p(x)=\alpha x + \beta


$$

where $\alpha$ and $\beta$ are constants to be determined.

Calculating the first derivative of $y_p$ gives

$$


\frac{\textrm{d}y_p}{\textrm{d}x} = \alpha.


$$

To find the values of $\alpha$ and $\beta,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


\alpha +2(\alpha x + \beta) = -2x + 5.


$$

We then group the terms on the left-hand side, as follows:

$$


2\alpha x + (\alpha +2\beta) = -2x + 5.


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{aligned}2𝛼=−2\, & (equating the coefficients of\,\,𝑥) \\ 𝛼+2𝛽=5\, & (equating the constants)\end{aligned}\end{aligned}


$$

Solving this system gives $\alpha=-1, \,\beta=3.$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x) = -x + 3.


$$

Now, since the general solution is given by

$$


y(x) = y_c(x)+y_p(x),


$$

the general solution in our case is

$$


y = Ae^{-2x} - x + 3.


$$

### Example: Solving an Initial Value Problem

#### Question

Consider the following initial value problem:

$$


y' + 4y = -8x + 6, \qquad y(0) = 1


$$

Given that the differential equation

$$


y' + 4y = -8x + 6


$$

has the complementary solution $y_c = Ae^{-4x},$ solve the initial value problem.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c,$ we solve the corresponding homogeneous equation, given by

$$


y_c' + 4y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{-4x}


$$

where $A$ is an arbitrary constant.

We now need to find the particular solution $y_p(x).$

The right-hand side of the inhomogeneous equation is a polynomial of degree $1.$ Therefore, we assume that the particular integral is also a polynomial of degree $1,$ i.e.,

$$


y_p(x)=\alpha x + \beta


$$

where $\alpha$ and $\beta$ are constants to be determined.

Calculating the first derivative of $y_p$ gives

$$


\frac{\textrm{d}y_p}{\textrm{d}x} = \alpha.


$$

To find the values of $\alpha,$ and $\beta,$ we substitute $y_p$ and $y_p'$ into the differential equation:

$$


\alpha + 4(\alpha x + \beta) = -8x + 6


$$

We then group the terms on the left-hand side, as follows:

$$


4\alpha x + (\alpha + 4\beta) = -8x + 6


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{aligned}4𝛼=−8\, & (equating the coefficients of\,\,𝑥) \\ 𝛼+4𝛽=6\, & (equating the constants)\end{aligned}\end{aligned}


$$

Solving this system gives $\alpha=-2, \,\beta = 2.$

Therefore, the particular solution $y_p(x)$ is

$$


y_p(x)= -2x + 2.


$$

The general solution is given by

$$


y(x) = y_c(x)+y_p(x),


$$

and therefore, the general solution in our case is

$$


y = Ae^{-4x} -2x + 2.


$$

Now, we can find the constant $A$ using the initial conditions.

Substituting $y(0) = 1$ into the general solution gives

$$


\begin{aligned}𝐴𝑒^{−4(0)}−2(0)+2 & =1 \\ 𝐴+2 & =1 \\ 𝐴 & =−1.\end{aligned}


$$

Therefore, the solution to the initial value problem is

$$


y = -e^{-4x} - 2x + 2.


$$

### Proof of the Form of the General Solution

Consider the first-order linear differential equation

$$


a(x)y' + b(x)y = f(x).


$$

We'll now prove that the sum of the complementary and particular solutions gives a general solution to the equation.

First, we note that, by definition, the complementary solution $y_c$ satisfies

$$


a(x)y'_c + b(x)y_c = 0.


$$

This can be solved by separating the variables, and the solution is given by (for $a(x)\neq 0$)

$$


y_c = A\exp\left(-\int \dfrac{b(x)}{a(x)}\,\textrm d x\right).


$$

By definition, the particular solution satisfies

$$


a(x)y'_p + b(x)y_p = f(x).


$$

We claim that

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝}\end{aligned}


$$

is the most general solution to the equation.

- First, we show that $y_c + y_p$ satisfies the equation. Substituting this into the left-hand side of the differential equation gives

$$


\begin{aligned}𝑎(𝑥)𝑦^{′}+𝑏(𝑥)𝑦 & =𝑎(𝑥)(𝑦_{′𝑐}^{}+𝑦_{′𝑝}^{})+𝑏(𝑥)(𝑦_{𝑐}+𝑦_{𝑝}) \\ & =\underset{0}{\underset{}{[𝑎(𝑥)𝑦_{′𝑐}^{}+𝑏(𝑥)𝑦_{𝑐}]}}+[𝑎(𝑥)𝑦_{′𝑝}^{}+𝑏(𝑥)𝑦_{𝑝}] \\ & =𝑎(𝑥)𝑦_{′𝑝}^{}+𝑏(𝑥)𝑦_{𝑝} \\ & =𝑓(𝑥).\end{aligned}


$$

- Now, suppose that $y$ is *any* solution to the equation, and $y_p$ is a known, particular solution. Substituting $y - y_p$ into the left-hand side of the equation gives Since $y$ is a solution, we have $a(x)y' + b(x)y = f(x)$, and since $y_p$ is a particular solution, we have $a(x)y'_p + b(x)y_p = f(x)$. Therefore, So, $y - y_p$ satisfies the homogeneous equation, and hence $y - y_p = y_c$. This implies that any solution $y$ is the sum of $y_c$ and $y_p.$

### A Common Convention for “the” Particular Solution

Technically, a particular solution $y_p$ is *not unique*.

If $y_p$ solves

$$


y' + P(x)\,y = Q(x),


$$

and $y_c$ solves the homogeneous equation

$$


y' + P(x)\,y = 0,


$$

then

$$


y_c + y_p


$$

also solves the inhomogeneous equation, which means that $y_c + y_p$ is also a particular solution!

However, in practice, even though $y_p$ is not unique, it’s very common to use the phrase **“the particular solution”** to mean "a particular solution that *does not include* any terms from the complementary (homogeneous) solution".

So, we typically choose $y_p$ to avoid overlapping with $y_c$, since the full solution is written as

$$


y = y_c + y_p.


$$

This makes the roles of $y_c$ and $y_p$ clean and non-redundant.
