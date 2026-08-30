# Differentials

Source: https://www.mathacademy.com/topics/1950?courseId=54
Topic ID: 1950

## Prerequisites

- [The Multivariable Chain Rule](./3173-the-multivariable-chain-rule.md)

## Lesson

### Introduction

The **differential** of a multivariable function $f(x,y)$ is denoted $\textrm df(x,y)$ and represents the infinitesimal change in the function value that occurs when the inputs $x$ and $y$ are changed by infinitesimal amounts $\textrm dx$ and $\textrm dy.$

The formula for the differential comes from the multivariable chain rule, which can be expressed as

$$


\begin{aligned}d𝑓(𝑥,𝑦) & =(\frac{𝜕𝑓}{𝜕𝑥})\,d𝑥+(\frac{𝜕𝑓}{𝜕𝑦})\,d𝑦.\end{aligned}


$$

Note that the differential can be extended to any number of variables. For example, for a three-variable function $f(x,y,z),$ we have

$$


\begin{aligned}d𝑓(𝑥,𝑦,𝑧) & =(\frac{𝜕𝑓}{𝜕𝑥})\,d𝑥+(\frac{𝜕𝑓}{𝜕𝑦})\,d𝑦+(\frac{𝜕𝑓}{𝜕𝑧})\,d𝑧.\end{aligned}


$$

### Example: Computing the Differential of a Multivariable Function

#### Question

Find the differential for $f(x,y) = x^2 \sin y.$

#### Explanation

We compute the differential using the formula:

$$


\begin{aligned}d𝑓(𝑥,𝑦) & =(\frac{𝜕𝑓}{𝜕𝑥})\,d𝑥+(\frac{𝜕𝑓}{𝜕𝑦})\,d𝑦 \\ & =(2𝑥sin⁡𝑦)\,d𝑥+(𝑥^{2}cos⁡𝑦)\,d𝑦 \\ & =2𝑥sin⁡𝑦\,d𝑥+𝑥^{2}cos⁡𝑦\,d𝑦\end{aligned}


$$

### Example: Computing a Differential in a Geometrical Context

#### Question

Given a cone, find the differential $\textrm d V$ for the volume $V$ of the cone if the radius is $r=6$ and the height is $h = 3.$

#### Explanation

The volume of the cone is $V = \dfrac{1}{3} \pi r^2h.$ Let's find the differential:

$$


\begin{aligned}d𝑉(𝑟,ℎ) & =(\frac{𝜕𝑉}{𝜕𝑟})\,d𝑟+(\frac{𝜕𝑉}{𝜕ℎ})\,dℎ \\ & =\frac{2}{3}𝜋𝑟ℎ\,d𝑟+\frac{1}{3}𝜋𝑟^{2}\,dℎ.\end{aligned}


$$

For $r=6$ and $h=3,$ the differential is

$$


\begin{aligned}d𝑉(6,3) & =\frac{2}{3}𝜋⋅6⋅3\,d𝑟+\frac{1}{3}𝜋⋅6^{2}\,dℎ \\ & =12𝜋\,d𝑟+12𝜋\,dℎ.\end{aligned}


$$

### Approximating Change Using Differentials

Given a multivariable function $f(x,y),$ the differential

$$


\begin{aligned}d𝑓(𝑥,𝑦) & =(\frac{𝜕𝑓}{𝜕𝑥})\,d𝑥+(\frac{𝜕𝑓}{𝜕𝑦})\,d𝑦\end{aligned}


$$

tells us how infinitesimal changes in $x$ and $y,$ denoted $\textrm dx$ and $\textrm dy,$ result in an infinitesimal change in $f,$ denoted $\textrm df.$

Consequently, we can use the differential to *approximate* the change in $f$ as we move from one point to another. If we move from a point $(x,y)$ to a point $(x + \Delta x, y + \Delta y),$ then the approximate change in $f$ is given by

$$


\begin{aligned}Δ𝑓(𝑥,𝑦) & ≈(\frac{𝜕𝑓}{𝜕𝑥})\,Δ𝑥+(\frac{𝜕𝑓}{𝜕𝑦})\,Δ𝑦.\end{aligned}


$$

The above formula is very similar to the differential formula, except the $\textrm d$'s are replaced with $\Delta$'s. The $\textrm d$'s refer to infinitesimal changes, while the $\Delta$'s refer to changes that can actually be measured.

### Example: Using Differentials to Approximate the Change in a Multivariable Function

#### Question

If $f (x, y) = xe^y,$ use the differential $\textrm d f$ to estimate the change $\Delta f$ in the value of $f(x, y)$ from $(5,0)$ to $(2,1).$

#### Explanation

First, let's find the differential:

$$


\begin{aligned}d𝑓(𝑥,𝑦) & =(\frac{𝜕𝑓}{𝜕𝑥})\,d𝑥+(\frac{𝜕𝑓}{𝜕𝑦})\,d𝑦 \\ & =𝑒^{𝑦}\,d𝑥+𝑥𝑒^{𝑦}\,d𝑦\end{aligned}


$$

At the point $(5,0),$ the differential is

$$


\begin{aligned}d𝑓(5,0) & =𝑒^{0}\,d𝑥+5𝑒^{0}\,d𝑦 \\ & =1\,d𝑥+5\,d𝑦.\end{aligned}


$$

So, if we move to the point $(5 + \Delta x, 0 + \Delta y),$ then we can approximate the change in $f$ as

$$


\Delta f \approx 1 \, \Delta x + 5 \, \Delta y.


$$

Moving from $(5,0)$ to $(2,1),$ we have

$$


\begin{aligned}Δ𝑥 & =2−5=−3, \\ Δ𝑦 & =1−0=1.\end{aligned}


$$

So, we have

$$


\begin{aligned}Δ𝑓 & ≈1\,Δ𝑥+5\,Δ𝑦 \\ & ≈1⋅(−3)+5⋅(1) \\ & ≈2.\end{aligned}


$$

Therefore, the value of $f(x,y)$ increases by approximately $2.$

### Example: Using Differentials to Approximate the Value of a Function

#### Question

Estimate $\sin (3) + \cos (0.2)$ using a differential of the function $f(x,y) = \sin x + \cos y$ at the point $\left(\pi, 0 \right).$

#### Explanation

First, let's find the differential:

$$


\begin{aligned}d𝑓(𝑥,𝑦) & =(\frac{𝜕𝑓}{𝜕𝑥})\,d𝑥+(\frac{𝜕𝑓}{𝜕𝑦})\,d𝑦 \\ & =cos⁡𝑥\,d𝑥−sin⁡𝑦\,d𝑦\end{aligned}


$$

At the point $\left(\pi, 0 \right),$ the differential is

$$


\begin{aligned}d𝑓(𝑥,𝑦) & =cos⁡𝜋\,d𝑥−sin⁡0\,d𝑦 \\ & =−1\,d𝑥+0\,d𝑦.\end{aligned}


$$

So, if we move to the point $(\pi + \Delta x, 0 + \Delta y),$ then we can approximate the change in $f$ as

$$


\Delta f \approx -1 \, \Delta x + 0 \, \Delta y


$$

Note that

$$


\sin (3) + \cos (0.2)= f(3,0.2),


$$

so we want to move to the point $(3,0.2).$

Moving from $(\pi, 0)$ to $(3,0.2),$ we have

$$


\begin{aligned}Δ𝑥 & =3−𝜋≈−0.141, \\ Δ𝑦 & =0.2−0=0.2.\end{aligned}


$$

So, we have

$$


\begin{aligned}Δ𝑓 & ≈−1(−0.141)+0(0.2) \\ & ≈0.141.\end{aligned}


$$

This means that the value of $f$ increases by about $0.141.$ Consequently, we have

$$


\begin{aligned}𝑓(3,0.2) & ≈𝑓(𝜋,0)+0.141 \\ sin⁡(3)+cos⁡(0.2) & ≈sin⁡(𝜋)+cos⁡(0)+0.141 \\ & ≈0+1+0.141 \\ & ≈1.141.\end{aligned}


$$
