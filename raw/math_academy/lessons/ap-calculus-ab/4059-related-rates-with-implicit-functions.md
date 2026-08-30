# Related Rates With Implicit Functions

Source: https://www.mathacademy.com/topics/4059?courseId=24
Topic ID: 4059

## Prerequisites

- [Solving Equations Containing the Exponential Function](../algebra-ii/870-solving-equations-containing-the-exponential-function.md)
- [Introduction to Related Rates](./1044-introduction-to-related-rates.md)
- [Solving Logarithmic Equations Containing the Natural Logarithm](../algebra-ii/1551-solving-logarithmic-equations-containing-the-natural-logarithm.md)

## Lesson

### Introduction

Suppose we have a curve defined by the implicit equation

$$


x^2 + e^y=5,


$$

and a particle moves along this curve. If the coordinates of the particle at time $t$ are given by

$$


x=x(t),\qquad y=y(t)


$$

and $\dfrac{\textrm d y}{\textrm d t}=4$ at the point $(2,0),$ how can we use this information to calculate the horizontal velocity $\dfrac{\textrm d x}{\textrm d t}$ at this point?

We start by differentiating the equation of the curve with respect to $t{:}$

$$


\begin{aligned}𝑥^{2}+𝑒^{𝑦} & =5 \\ \frac{d}{d𝑡}(𝑥^{2}+𝑒^{𝑦}) & =\frac{d}{d𝑡}(5) \\ \frac{d}{d𝑡}(𝑥^{2})+\frac{d}{d𝑡}(𝑒^{𝑦}) & =0\end{aligned}


$$

Although the equation $x^2 + e^y = 0$ is written in terms of $x$ and $y,$ we can differentiate both sides with respect to $t$ by treating $x = x(t)$ and $y = y(t)$ as differentiable functions of $t.$

This allows us to apply implicit differentiation as follows:

$$


\begin{aligned}\frac{d}{d𝑡}(𝑥^{2})+\frac{d}{d𝑡}(𝑒^{𝑦}) & =0 \\ \frac{d𝑥}{d𝑡}⋅\frac{d}{d𝑥}(𝑥^{2})+\frac{d𝑦}{d𝑡}⋅\frac{d}{d𝑦}(𝑒^{𝑦}) & =0 \\ \frac{d𝑥}{d𝑡}⋅(2𝑥)+\frac{d𝑦}{d𝑡}⋅(𝑒^{𝑦}) & =0 \\ 2𝑥\frac{d𝑥}{d𝑡}+𝑒^{𝑦}\frac{d𝑦}{d𝑡} & =0\end{aligned}


$$

Now, we substitute the given information

$$


\dfrac{\textrm d y}{\textrm d t}=4,\qquad x=2,\qquad y=0,


$$

into our differentiated expression and solve for $\dfrac{\textrm{d}x}{\textrm{d}t}{:}$

$$


\begin{aligned}2⋅2⋅\frac{d𝑥}{d𝑡}+𝑒^{0}⋅4 & =0 \\ 4⋅\frac{d𝑥}{d𝑡}+4 & =0 \\ 4⋅\frac{d𝑥}{d𝑡} & =−4 \\ \frac{d𝑥}{d𝑡} & =−1\end{aligned}


$$

Therefore, we conclude that the horizontal velocity of the particle $\dfrac{\textrm dx}{\textrm dt} = -1$ at the point $(2,0).$

### Example: Calculating a Related Rate From an Implicitly Defined Curve

#### Question

Consider the following ellipse:

$$


\dfrac{x^2}{2}+\dfrac{y^2}{4}=1


$$

Given that $x=x(t),$ $y=y(t),$ and that $\dfrac{\textrm d y}{\textrm d t}=\sqrt{2}$ on the curve at the point $(1,\sqrt2),$ find the value of $\dfrac{\textrm d x}{\textrm d t}$ at that point.

#### Explanation

Differentiating the given relation with respect to $t$ using implicit differentiation, we get

$$


\begin{aligned}\frac{𝑥^{2}}{2}+\frac{𝑦^{2}}{4} & =1 \\ \frac{d}{d𝑡}(\frac{𝑥^{2}}{2}+\frac{𝑦^{2}}{4}) & =\frac{d}{d𝑡}(1) \\ \frac{d}{d𝑡}(\frac{𝑥^{2}}{2})+\frac{d}{d𝑡}(\frac{𝑦^{2}}{4}) & =0 \\ \frac{d𝑥}{d𝑡}⋅\frac{d}{d𝑥}(\frac{𝑥^{2}}{2})+\frac{d𝑦}{d𝑡}⋅\frac{d}{d𝑦}(\frac{𝑦^{2}}{4}) & =0 \\ \frac{d𝑥}{d𝑡}⋅(𝑥)+\frac{d𝑦}{d𝑡}⋅(\frac{𝑦}{2}) & =0.\end{aligned}


$$

Now, we substitute the given information $\dfrac{\textrm d y}{\textrm d t}=\sqrt{2},$ $x=1,$ and $y=\sqrt2,$ and solve $\dfrac{\textrm{d}x}{\textrm{d}t}.$ We get

$$


\begin{aligned}\frac{d𝑥}{d𝑡}⋅(1)+\sqrt{√2}⋅(\frac{\sqrt{√2}}{2}) & =0 \\ \frac{d𝑥}{d𝑡}+1 & =0 \\ \frac{d𝑥}{d𝑡} & =−1.\end{aligned}


$$

### Example: Using an Implicitly Defined Curve to Determine a Second Coordinate

#### Question

Consider the curve $x^3-\ln y=1.$ Given that $x=x(t),$ $y=y(t),$ and that $\dfrac{\textrm d x}{\textrm d t}=2$ on the curve at the point where $x=1,$ find the value of $\dfrac{\textrm d y}{\textrm d t}$ at that point.

#### Explanation

Differentiating the given relation with respect to $t$ using implicit differentiation, we get

$$


\begin{aligned}𝑥^{3}−ln⁡𝑦 & =1 \\ \frac{d}{d𝑡}(𝑥^{3}−ln⁡𝑦) & =\frac{d}{d𝑡}(1) \\ \frac{d}{d𝑡}(𝑥^{3})−\frac{d}{d𝑡}(ln⁡𝑦) & =0 \\ \frac{d𝑥}{d𝑡}⋅\frac{d}{d𝑥}(𝑥^{3})−\frac{d𝑦}{d𝑡}⋅\frac{d}{d𝑦}(ln⁡𝑦) & =0 \\ \frac{d𝑥}{d𝑡}⋅3𝑥^{2}−\frac{d𝑦}{d𝑡}⋅\frac{1}{𝑦} & =0.\end{aligned}


$$

Now, we substitute the given information $\dfrac{\textrm d x}{\textrm d t}=2$ and $x=1.$ We get

$$


\begin{aligned}6−\frac{d𝑦}{d𝑡}⋅\frac{1}{𝑦} & =0.\end{aligned}


$$

We also want to substitute for $y,$ but we are not given this value. However, we can find it by substituting $x=1$ into the equation of the curve.

At the point where $x=1,$ we have

$$


\begin{aligned}𝑥^{3}−ln⁡𝑦 & =1 \\ 1−ln⁡𝑦 & =1 \\ ln⁡𝑦 & =0 \\ 𝑦 & =1.\end{aligned}


$$

Finally, substituting $y=1,$ we get

$$


\begin{aligned}6−\frac{d𝑦}{d𝑡}⋅\frac{1}{1} & =0 \\ \frac{d𝑦}{d𝑡} & =6.\end{aligned}


$$

### Example: Using the Equation of a Conic Section to Determine a Second Coordinate

#### Question

Consider the section of the hyperbola

$$


\dfrac{x^2}{3}-\dfrac{y^2}{2}=1


$$

that lies in the first quadrant. Given that $x=x(t),$ $y=y(t),$ and that $\dfrac{\textrm d y}{\textrm d t}=-2$ on the hyperbola at the point where $x=3,$ find the value of $\dfrac{\textrm d x}{\textrm d t}$ at this point.

#### Explanation

Differentiating the given relation with respect to $t$ using implicit differentiation, we get

$$


\begin{aligned}\frac{𝑥^{2}}{3}−\frac{𝑦^{2}}{2} & =1 \\ \frac{d}{d𝑡}(\frac{𝑥^{2}}{3}−\frac{𝑦^{2}}{2}) & =\frac{d}{d𝑡}(1) \\ \frac{d}{d𝑡}(\frac{𝑥^{2}}{3})−\frac{d}{d𝑡}(\frac{𝑦^{2}}{2}) & =0 \\ \frac{d𝑥}{d𝑡}⋅\frac{d}{d𝑥}(\frac{𝑥^{2}}{3})−\frac{d𝑦}{d𝑡}⋅\frac{d}{d𝑦}(\frac{𝑦^{2}}{2}) & =0 \\ \frac{d𝑥}{d𝑡}⋅(\frac{2𝑥}{3})−\frac{d𝑦}{d𝑡}⋅𝑦 & =0.\end{aligned}


$$

Now, we substitute the given information $\dfrac{\textrm d y}{\textrm d t}=-2$ and $x=3.$ We get

$$


\begin{aligned}\frac{d𝑥}{d𝑡}⋅(\frac{2⋅3}{3})−(−2)⋅𝑦 & =0 \\ 2\frac{d𝑥}{d𝑡}+2𝑦 & =0 \\ \frac{d𝑥}{d𝑡} & =−𝑦.\end{aligned}


$$

We also want to substitute for $y$, but we are not given this value. However, we can find it by substituting $x=3$ into the equation of the hyperbola.

At the point where $x=3,$ we have

$$


\begin{aligned}\frac{𝑥^{2}}{3}−\frac{𝑦^{2}}{2} & =1 \\ \frac{3^{2}}{3}−\frac{𝑦^{2}}{2} & =1 \\ \frac{𝑦^{2}}{2} & =2 \\ 𝑦^{2} & =4 \\ 𝑦 & =2.\end{aligned}


$$

Note that we used $y > 0$ since we're only interested in the first quadrant.

Finally, substituting $y= 2,$ we get

$$


\begin{aligned}\frac{d𝑥}{d𝑡} & =−𝑦 \\ \frac{d𝑥}{d𝑡} & =−2.\end{aligned}


$$
