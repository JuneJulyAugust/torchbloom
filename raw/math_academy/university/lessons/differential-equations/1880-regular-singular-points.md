# Regular Singular Points

Source: https://www.mathacademy.com/topics/1880?courseId=61
Topic ID: 1880

## Prerequisites

- [Power Series Solutions of Differential Equations](./2543-power-series-solutions-of-differential-equations.md)
- [Introduction to Second-Order Linear ODEs](./2548-introduction-to-second-order-linear-odes.md)
- [Radius of Convergence of Power Series](../../../ap-courses/lessons/ap-calculus-bc/3560-radius-of-convergence-of-power-series.md)

## Lesson

### Introduction

Consider a second-order linear differential equation in the standard form

$$


y'' + P(x)y' + Q(x)y = g(x).


$$

The point $x=a$ is an **ordinary point** of the differential equation if both $P(x)$ and $Q(x)$ are analytic about $x=a.$ Otherwise, $x=a$ is a **singular point** of the differential equation.

In this lesson, we'll use an operational rule for analyticity:

- Polynomials are analytic everywhere.

- Functions such as $e^x,$ $\sin x,$ and $\cos x$ are analytic everywhere.

- A rational function $\dfrac{p(x)}{q(x)}$ is analytic about $x=a$ as long as $q(a)\neq 0.$

To demonstrate, consider the differential equation

$$


y'' + \dfrac{3}{(x-2)(x+1)}y' + \dfrac{x+4}{x-2}y = 0.


$$

Among the points $x=-1,$ $x=0,$ and $x=2,$ which are singular points?

In this case, we have

$$


P(x)=\dfrac{3}{(x-2)(x+1)} \quad\text{and}\quad Q(x)=\dfrac{x+4}{x-2}.


$$

Let's now check the analyticity of these functions at the given points.

- The function $P(x)$ is *not* analytic about $x=-1,$ since its denominator at $x=-1$ equals zero. So, $x=-1$ is a singular point of the differential equation.

- *Both* functions are analytic about $x=0.$ So, $x=0$ is an ordinary point of the differential equation.

- *Neither* function is analytic about $x=2,$ since both denominators at $x=2$ equal zero. So, $x=2$ is a singular point of the differential equation.

Therefore, among the points listed, the singular points are $x=-1$ and $x=2.$

### Example: Identifying Ordinary and Singular Points

#### Question

$$


(x-2)(x+3)y'' + (x+1)y' + xy = 0


$$

Which of the following is a **** point of the differential equation above?

1. $x=-3$

2. $x=0$

3. $x=2$

#### Explanation

The point $x=a$ is an ordinary point of the differential equation

$$


y'' + P(x)y' + Q(x)y = f(x)


$$

if both coefficients $P(x)$ and $Q(x)$ are analytic about $x=a.$ Otherwise, $x=a$ is a singular point of the differential equation.

First, we rewrite the differential equation in standard form by dividing by $(x-2)(x+3){:}$

$$


\begin{aligned}(𝑥−2)(𝑥+3)𝑦^{″}+(𝑥+1)𝑦^{′}+𝑥𝑦 & =0 \\ 𝑦^{″}+\frac{𝑥+1}{(𝑥−2)(𝑥+3)}𝑦^{′}+\frac{𝑥}{(𝑥−2)(𝑥+3)}𝑦 & =0\end{aligned}


$$

So, we have

$$


P(x) = \dfrac{x+1}{(x-2)(x+3)} \quad\text{and}\quad Q(x) = \dfrac{x}{(x-2)(x+3)}.


$$

Let's now check the analyticity of these functions at the given points.

- ** function is analytic about $x=-3,$ since both denominators at $x=-3$ equal zero. So, $x=-3$ is a singular point of the differential equation.

- ** functions are analytic about $x=0.$ So, $x=0$ is an ordinary point of the differential equation.

- ** function is analytic about $x=2,$ since both denominators at $x=2$ equal zero. So, $x=2$ is a singular point of the differential equation.

Therefore, the correct answer is "I and III only."

### Regular Singular Points

A singular point $x=a$ of the differential equation

$$


y'' + P(x)y' + Q(x)y = g(x)


$$

is said to be **regular** if both $(x-a)P(x)$ and $(x-a)^2Q(x)$ are analytic about $x=a.$ Otherwise, the singular point is **irregular**.

In other words, at a regular singular point, the coefficients are allowed to have limited singular behavior:

- The function $P(x)$ is allowed to have (at worst) a $\dfrac{1}{x-a}$-type blow-up at $x=a.$

- The function $Q(x)$ is allowed to have (at worst) a $\dfrac{1}{(x-a)^2}$-type blow-up at $x=a.$

If the singularity is worse than this, then the point is an irregular singular point.

To demonstrate, consider the differential equation

$$


y'' + \dfrac{x+2}{(x-3)^2}y' + \dfrac{1}{(x-3)^4}y = 0.


$$

Is the point $x=3$ a regular singular point or an irregular singular point?

In this case, we have

$$


P(x)=\dfrac{x+2}{(x-3)^2} \quad\text{and}\quad Q(x)=\dfrac{1}{(x-3)^4}.


$$

First, we check that $x=3$ is a singular point. Since the denominators of both $P(x)$ and $Q(x)$ vanish at $x=3,$ neither $P(x)$ nor $Q(x)$ is analytic about $x=3.$ So, $x=3$ is a singular point of the differential equation.

Now we check whether the singular point is regular by testing $(x-3)P(x)$ and $(x-3)^2Q(x).$

- The function is *not* analytic about $x=3,$ since its denominator at $x=3$ equals zero. (**Note:** This failure alone is sufficient to classify the point as irregular, but we will check the second term for completeness.)

- The function is also *not* analytic about $x=3,$ since its denominator at $x=3$ equals zero.

Therefore, since $x=3$ is a singular point and neither $(x-3)P(x)$ nor $(x-3)^2Q(x)$ is analytic about $x=3,$ it follows that $x=3$ is an **irregular** singular point of the differential equation.

### Example: Identifying Regular and Irregular Singular Points

#### Question

$$


(x-5)y'' + \dfrac{x+5}{x-5}y' + \dfrac{3}{(x-5)^3}y = 0


$$

Consider the differential equation given above. Which of the following statements are true?

1. The functions $P(x)=\dfrac{x+5}{(x-5)^2}$ and $Q(x)=\dfrac{3}{(x-5)^4}$ are analytic about $x=5.$

2. The functions $(x-5)P(x)$ and $(x-5)^2Q(x)$ are analytic about $x=5.$

3. The point $x=5$ is an **** singular point of the differential equation.

#### Explanation

A singular point $a$ of the differential equation

$$


y'' + P(x)y' + Q(x)y = f(x)


$$

is regular if both $(x-a)P(x)$ and $(x-a)^2Q(x)$ are analytic about $x=a.$ Otherwise, the singular point is irregular.

First, we rewrite the differential equation in standard form by dividing by $(x-5){:}$

$$


\begin{aligned}(𝑥−5)𝑦^{″}+\frac{𝑥+5}{𝑥−5}𝑦^{′}+\frac{3}{(𝑥−5)^{3}}𝑦 & =0 \\ 𝑦^{″}+\frac{𝑥+5}{(𝑥−5)^{2}}𝑦^{′}+\frac{3}{(𝑥−5)^{4}}𝑦 & =0\end{aligned}


$$

So, we have

$$


P(x) = \dfrac{x+5}{(x-5)^2} \quad\text{and}\quad Q(x) = \dfrac{3}{(x-5)^4}.


$$

Let's now check each statement in turn.

- Since the denominators of both $P(x)$ and $Q(x)$ vanish at $x=5,$ they are ** analytic about $x=5.$ So, statement I is false.

- The function is ** analytic about $x=5$ since its denominator vanishes at $x=5.$ Therefore, statement II is false.

- Since statement I is false, $x=5$ is a singular point. Also, since statement II is false, it follows that $x=5$ is an **** singular point. Thus, statement III is true.

Therefore, the correct answer is "III only."

### Example: Classifying Points for a Differential Equation

#### Question

$$


x(x-2)(x+1)y'' + x(x-2)y' + \dfrac{\sin x}{(x-2)^2}\, y = 0


$$

Given the points $x = -1,$ $x = 0,$ $x = 1,$ and $x = 2,$ indicate whether they are ordinary or singular points of the differential equation above. If they are singular points, indicate whether they are regular or irregular.

#### Explanation

The point $x=a$ is an ordinary point of the differential equation

$$


y'' + P(x)y' + Q(x)y = f(x)


$$

if both $P(x)$ and $Q(x)$ are analytic about $x=a.$ Otherwise, $x=a$ is a singular point of the differential equation.

A singular point $x=a$ is regular if both $(x-a)P(x)$ and $(x-a)^2Q(x)$ are analytic about $x=a.$ Otherwise, the singular point is irregular.

First, we rewrite the differential equation in standard form by dividing by $x(x-2)(x+1){:}$

$$


\begin{aligned}𝑥(𝑥−2)(𝑥+1)𝑦^{″}+𝑥(𝑥−2)𝑦^{′}+\frac{sin⁡𝑥}{(𝑥−2)^{2}}𝑦 & =0 \\ 𝑦^{″}+\frac{1}{𝑥+1}𝑦^{′}+\frac{sin⁡𝑥}{𝑥(𝑥+1)(𝑥−2)^{3}}𝑦 & =0\end{aligned}


$$

So, we have

$$


P(x)=\dfrac{1}{x+1} \quad\text{and}\quad Q(x)=\dfrac{\sin x}{x(x+1)(x-2)^3}.


$$

The function $P(x)$ is ** analytic about points where $x+1 = 0,$ which occurs at $x = -1.$

The function $Q(x)$ is ** analytic about points where $x(x+1)(x-2)^3 = 0,$ which occurs at $x=-1,$ $x=0,$ and $x=2.$

Therefore, $x=1$ is a ** of the differential equation, and the ** are

$$


x=-1, \quad x=0, \quad x=2.


$$

Now, let's classify each singular point.

- For $x=-1,$ the function is analytic about $x=-1,$ and the function is also analytic about $x=-1.$ Thus, $x=-1$ is a ** of the differential equation.

- For $x=0,$ the function is analytic about $x=0,$ and the function is also analytic about $x=0.$ Thus, $x=0$ is a ** of the differential equation.

- For $x=2,$ the function is analytic about $x=2,$ but the function is ** analytic about $x=2.$ Therefore, $x=2$ is an ** of the differential equation.
