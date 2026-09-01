# Further Modeling With First-Order ODEs

Source: https://www.mathacademy.com/topics/3860?courseId=154
Topic ID: 3860

## Prerequisites

- [Calculating Related Rates With Circles and Spheres](../../../ap-courses/lessons/ap-calculus-ab/287-calculating-related-rates-with-circles-and-spheres.md)
- [Calculating Related Rates With Rectangular Solids](../../../ap-courses/lessons/ap-calculus-ab/365-calculating-related-rates-with-rectangular-solids.md)
- [The Distance Formula](../../../high-school/traditional/lessons/geometry/459-the-distance-formula.md)
- [Modeling With First-Order ODEs](./2023-modeling-with-first-order-odes.md)

## Lesson

### Introduction

When constructing a differential equation to model a particular phenomenon, we sometimes combine several pieces of information to create the correct model.

Consider the following situation:

*The common cold virus spreads through a particular country. The rate at which the number of infected people increases is **** to the **** $t$ (in days) since the outbreak started. Additionally, $100$ infected people ****.*

We want to find a differential equation that models $P(t),$ the number of infected people. We note the following:

- The statement describes the *rate* at which the *number of infected people* varies. Therefore, this is a statement about the quantity

- The rate at which the number of infected people increases is **proportional** to the **square of the time** $t.$ Therefore, if $I(t)$ represents the rate at which infections increase, then where $k$ is a positive constant.

- Additionally, $100$ infected people **recover from the virus each day**. Therefore, if $D(t)$ represents the rate at which infections decrease, then

Therefore, the differential equation that describes this phenomenon is as follows:

$$


\begin{aligned}\frac{d𝑃}{d𝑡} & =\underset{𝐼(𝑡)−𝐷(𝑡)}{\underset{}{𝑘𝑡^{2}−100}}\end{aligned}


$$

Although we introduced the functions $I(t)$ and $D(t)$ here, we can usually write down the appropriate differential equation straight away. Let's see an example.

### Example: Translating Contextual Problems Into Differential Equations

#### Question

Since the year $2000$, a herd of antelopes multiplies at a rate proportional to their population. Also, the number of antelopes in the herd decreases by $20$ antelopes per year due to predators. What differential equation describes the rate of change in the population of antelopes at time $t,$ where $t$ is the time (in years) since the year $2000?$

#### Explanation

The rate of change in the number of antelopes per year increases in proportion to $P$ and decreases by $20.$ The differential equation that describes this is

$$


\dfrac{\text{d}P}{\text{d}t}=kP - 20,


$$

where $k$ is a (positive) constant of proportionality.

### Recalling Some Facts From Elementary Geometry

Let's recall some basic facts from geometry in the $xy$-plane:

- The distance between the point $(x,y)$ and the origin $(0,0)$ equals $\sqrt{x^2+y^2}.$

- The (smallest) distance between the point $(x,y)$ and the $x$-axis equals $|y|.$

- Similarly, the (smallest) distance between the point $(x,y)$ and the $y$-axis equals $|x|.$

- The slope of the line that passes through $(x,y)$ and the origin equals $\dfrac{y}{x}.$

We sometimes need to use these basic facts when constructing differential equations described in a geometric context.

Let's see an example.

### Example: Translating Coordinate Plane Problems Into Differential Equations

#### Question

At each point $P$ on a particular curve, the derivative $y'(x)$ is **** proportional to the square of the distance from $P$ to the origin. The derivative at the point $(-1,2)$ equals $2.$ What differential equation describes this curve?

#### Explanation

Let's highlight the important words in the given statement:

**

We note the following:

- The ** is given by $x^2+y^2.$

- Since the ** is ** the square of the distance from $P$ to the origin, we have where $k$ is a constant.

So, our differential equation is

$$


y'(x) = \dfrac{k}{x^2+y^2}.


$$

In addition, we're told that $y'(x) = 2$ when at the point $(-1, 2).$ We can use this to determine the value of the coefficient $k\mathbin{:}$

$$


\begin{aligned}2 & =\frac{𝑘}{(−1)^{2}+2^{2}} \\ 2 & =\frac{𝑘}{5} \\ 𝑘 & =10\end{aligned}


$$

Finally, the differential equation describing the curve is

$$


y'(x)= \dfrac{10}{x^2+y^2}.


$$

### Example: Expressing Two-Dimensional Related Rates Using Differential Equations

#### Question

The area of a circle decreases at a rate that's proportional to its radius. Write down a differential equation describing the rate of change of the radius, $r(t),$ in this process.

#### Explanation

Let's highlight the important words in the given statement:

**

We note the following:

- The question describes the ** at which the ** varies. Therefore, this is a statement about the quantity

- We're told that $\dfrac{\textrm d A}{\textrm d t}$ ** at a rate that's ** to its ** In other words, where $k > 0.$

We wish to use this information to find an expression for $\dfrac{\textrm d r}{\textrm d t}.$

The area of a circle is given by

$$


A=\pi r^2.


$$

Differentiating this equation with respect to $t,$ we get

$$


\begin{aligned}\frac{d𝐴}{d𝑡} & =\frac{d}{d𝑡}(𝜋𝑟^{2}) \\ \frac{d𝐴}{d𝑡} & =2𝜋𝑟\frac{d𝑟}{d𝑡}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}\frac{d𝐴}{d𝑡} & =−𝑘𝑟 \\ 2𝜋𝑟\frac{d𝑟}{d𝑡} & =−𝑘𝑟 \\ \frac{d𝑟}{d𝑡} & =−\frac{𝑘𝑟}{2𝜋𝑟} \\ \frac{d𝑟}{d𝑡} & =−\frac{𝑘}{2𝜋}.\end{aligned}


$$

We now introduce a new constant:

$$


K = \dfrac{k}{2\pi} > 0


$$

Therefore, our equation becomes

$$


\dfrac{\text{d}r}{\text{d}t} = -K.


$$

### Example: Expressing Three-Dimensional Related Rates Using Differential Equations

#### Question

The volume of a sphere increases at a rate inversely proportional to its radius. Write down a differential equation describing the rate of change of the radius, $r(t),$ in this process.

#### Explanation

Let's highlight the important words in the given statement:

**

We note the following:

- The question describes the ** at which the ** varies. Therefore, this is a statement about the quantity

- We're told that $\dfrac{\textrm d V}{\textrm d t}$ ** at a rate ** Therefore, where $k > 0.$

We wish to use this information to find an expression for $\dfrac{\textrm d r}{\textrm d t}.$

The volume $V$ of a sphere is given by

$$


V = \dfrac{4}{3}\pi r^3.


$$

Differentiating this equation with respect to $t,$ we get

$$


\begin{aligned}\frac{d𝑉}{d𝑡} & =\frac{d}{d𝑡}(\frac{4}{3}𝜋𝑟^{3}) \\ \frac{d𝑉}{d𝑡} & =4𝜋𝑟^{2}\frac{d𝑟}{d𝑡}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}\frac{d𝑉}{d𝑡} & =\frac{𝑘}{𝑟} \\ 4𝜋𝑟^{2}\frac{d𝑟}{d𝑡} & =\frac{𝑘}{𝑟} \\ \frac{d𝑟}{d𝑡} & =\frac{(\frac{𝑘}{𝑟})}{𝑟} \\ \frac{d𝑟}{d𝑡} & =\frac{𝑘}{4𝜋𝑟^{3}}.\end{aligned}


$$

We now introduce a new constant:

$$


K = \dfrac{k}{4\pi} > 0


$$

Therefore, our equation becomes

$$


\dfrac{\text{d}r}{\text{d}t} = \dfrac{K}{r^3}.


$$
