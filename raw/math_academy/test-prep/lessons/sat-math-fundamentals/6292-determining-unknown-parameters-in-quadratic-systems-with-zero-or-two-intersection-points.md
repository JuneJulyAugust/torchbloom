# Determining Unknown Parameters in Quadratic Systems With Zero or Two Intersection Points

Source: https://www.mathacademy.com/topics/6292?courseId=120
Topic ID: 6292

## Prerequisites

- [Determining Unknown Parameters in Quadratic Equations With No Real Solutions](../../../high-school/traditional/lessons/precalculus/6289-determining-unknown-parameters-in-quadratic-equations-with-no-real-solutions.md)
- [Determining Unknown Parameters in Quadratic Systems With One Intersection Point](./6291-determining-unknown-parameters-in-quadratic-systems-with-one-intersection-point.md)

## Lesson

### Introduction

In this lesson, we’ll learn how to use the discriminant to determine the values of unknown parameters that make a quadratic system have either two solutions (two intersection points) or no solutions (no intersection points).

Let's consider the following quadratic system:

$$


\begin{aligned}𝑦=4𝑥^{2}−8𝑥+5 \\ 𝑦=𝑚\end{aligned}


$$

In the system above, $m$ is an integer constant. Let's find the least possible value of $m$ such that the graphs of these functions intersect at two distinct points in the $xy$-plane.

The line $y=m$ intersects the parabola $y=4x^2 - 8x + 5$ where

$$


4x^2 - 8x + 5 = m.


$$

A quadratic equation has two distinct real roots if the discriminant is positive: $\mathcal{D} > 0.$

First, rewrite the equation in standard quadratic form:

$$


\begin{aligned}4𝑥^{2}−8𝑥+5 & =𝑚 \\ 4𝑥^{2}−8𝑥+5−𝑚 & =0 \\ 4𝑥^{2}−8𝑥+(5−𝑚) & =0\end{aligned}


$$

The coefficients of our quadratic equation are the following:

$$


a = 4, \qquad b = -8, \qquad c = 5-m


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−8)^{2}−4(4)(5−𝑚) \\ & =64−80+16𝑚 \\ & =−16+16𝑚.\end{aligned}


$$

For two distinct real solutions, we need $\mathcal{D} > 0{:}$

$$


\begin{aligned}−16+16𝑚 & >0 \\ 16𝑚 & >16 \\ 𝑚 & >1\end{aligned}


$$

Since $m$ must be an integer, we conclude that the least possible value is $2.$

### Example: Quadratic Systems With Horizontal Lines and Two Intersection Points

#### Question

$$


\begin{aligned}𝑦=4𝑥^{2}−8𝑥+7 \\ 𝑦=𝑚\end{aligned}


$$

The graphs of the equations given in the system of equations above, where $m$ is an **** constant, intersect at two distinct points in the $xy$-plane. What is the least possible value of $m?$

#### Explanation

The line $y = m$ intersects the parabola $y = 4x^2 - 8x + 7$ where

$$


4x^2 - 8x + 7 = m.


$$

A quadratic equation has two distinct real roots if the discriminant is positive: $\mathcal{D} > 0.$

First, rewrite the equation in standard quadratic form:

$$


\begin{aligned}4𝑥^{2}−8𝑥+7 & =𝑚 \\ 4𝑥^{2}−8𝑥+7−𝑚 & =0 \\ 4𝑥^{2}−8𝑥+(7−𝑚) & =0\end{aligned}


$$

The coefficients of our quadratic equation are the following:

$$


a = 4, \qquad b = -8, \qquad c = 7 - m


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−8)^{2}−4(4)(7−𝑚) \\ & =64−112+16𝑚 \\ & =−48+16𝑚.\end{aligned}


$$

For two distinct real solutions, we need $\mathcal{D} > 0{:}$

$$


\begin{aligned}−48+16𝑚 & >0 \\ 16𝑚 & >48 \\ 𝑚 & >3\end{aligned}


$$

Since $m$ must be an integer, we conclude that the least possible value is $4.$

### Example: Quadratic Systems With Sloped Lines and Two Intersection Points

#### Question

If the graph of the equation $y=3x^2 - 12x + 8$ intersects the line $y=k-3x,$ where $k$ is an **** constant, at two distinct points in the $xy$-plane, what is the least possible value of $k?$

#### Explanation

The line $y=k-3x$ intersects the parabola $y=3x^2 - 12x + 8$ where

$$


3x^2 - 12x + 8 = k - 3x.


$$

A quadratic equation has two distinct real roots if the discriminant is positive: $\mathcal{D} > 0.$

First, rewrite the equation in standard quadratic form:

$$


\begin{aligned}3𝑥^{2}−12𝑥+8 & =𝑘−3𝑥 \\ 3𝑥^{2}−12𝑥+8+3𝑥−𝑘 & =0 \\ 3𝑥^{2}−9𝑥+(8−𝑘) & =0\end{aligned}


$$

The coefficients of our quadratic equation are the following:

$$


a = 3, \qquad b = -9, \qquad c = 8-k


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−9)^{2}−4(3)(8−𝑘) \\ & =81−96+12𝑘 \\ & =−15+12𝑘.\end{aligned}


$$

For two distinct real solutions, we need $\mathcal{D} > 0{:}$

$$


\begin{aligned}−15+12𝑘 & >0 \\ 12𝑘 & >15 \\ 𝑘 & >\frac{15}{12} \\ 𝑘 & >1.25\end{aligned}


$$

Since $k$ must be an integer, we conclude that the least possible value is $2.$

### Determining Unknown Coefficients in Quadratic Systems With No Intersection Points

Now, let’s see an example where there are no intersection points.

If the graph of the equation $y = x^2 - 4x + 7$ doesn't intersect the line $y=k$ in the $xy$-plane, where $k$ is an integer constant, let's find the greatest possible value of $k.$

The line $y=k$ intersects the parabola $y = x^2 - 4x + 7$ where

$$


x^2 - 4x + 7 = k.


$$

A quadratic equation has no real roots if the discriminant is negative: $\mathcal{D} < 0.$

First, rewrite the equation in standard quadratic form:

$$


\begin{aligned}𝑥^{2}−4𝑥+7 & =𝑘 \\ 𝑥^{2}−4𝑥+7−𝑘 & =0 \\ 𝑥^{2}−4𝑥+(7−𝑘) & =0\end{aligned}


$$

The coefficients of our quadratic equation are the following:

$$


a = 1, \qquad b = -4, \qquad c = 7-k


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =(−4)^{2}−4(1)(7−𝑘) \\ & =16−4(7−𝑘) \\ & =16−28+4𝑘 \\ & =4𝑘−12.\end{aligned}


$$

For no real solutions, we need $\mathcal{D} < 0{:}$

$$


\begin{aligned}4𝑘−12 & <0 \\ 4𝑘 & <12 \\ 𝑘 & <\frac{12}{4} \\ 𝑘 & <3\end{aligned}


$$

Since $k$ must be an integer, we conclude that the greatest possible value is $2.$

### Example: Quadratic Systems With Horizontal Lines and No Intersection Points

#### Question

$$


\begin{aligned}𝑦=−3𝑥^{2}−6𝑥+9 \\ 𝑦=𝑘\end{aligned}


$$

The graphs of the equations given in the system of equations above, where $k$ is an **** constant, don't intersect in the $xy$-plane. What is the smallest possible value of $k?$

#### Explanation

The line $y=k$ intersects the parabola $y = -3x^2 - 6x + 9$ where

$$


-3x^2 - 6x + 9 = k.


$$

A quadratic equation has no real roots if the discriminant is negative: $\mathcal{D} < 0.$

First, rewrite the equation in standard quadratic form:

$$


\begin{aligned}−3𝑥^{2}−6𝑥+9 & =𝑘 \\ −3𝑥^{2}−6𝑥+9−𝑘 & =0 \\ −3𝑥^{2}−6𝑥+(9−𝑘) & =0\end{aligned}


$$

The coefficients of our quadratic equation are the following:

$$


a = -3, \qquad b = -6, \qquad c = 9-k


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−6)^{2}−4(−3)(9−𝑘) \\ & =36+12(9−𝑘) \\ & =36+108−12𝑘 \\ & =144−12𝑘.\end{aligned}


$$

For no real solutions, we need $\mathcal{D} < 0{:}$

$$


\begin{aligned}144−12𝑘 & <0 \\ −12𝑘 & <−144 \\ 12𝑘 & >144 \\ 𝑘 & >\frac{144}{12} \\ 𝑘 & >12\end{aligned}


$$

Since $k$ must be an integer, we conclude that the smallest possible value is $13.$

### Example: Quadratic Systems With Sloped Lines and No Intersection Points

#### Question

If the graph of the equation $y=2x^2-4x+8$ doesn't intersect the line $y=x+k$ in the $xy$-plane, where $k$ is an **** constant, what is the greatest possible value of $k?$

#### Explanation

The line $y=x+k$ intersects the parabola $y = 2x^2 - 4x + 8$ where

$$


2x^2 - 4x + 8 = x+k.


$$

A quadratic equation has no real roots if the discriminant is negative: $\mathcal{D} < 0.$

First, rewrite the equation in standard quadratic form:

$$


\begin{aligned}2𝑥^{2}−4𝑥+8 & =𝑥+𝑘 \\ 2𝑥^{2}−4𝑥+8−𝑥−𝑘 & =0 \\ 2𝑥^{2}−5𝑥+(8−𝑘) & =0\end{aligned}


$$

The coefficients of our quadratic equation are the following:

$$


a = 2, \qquad b = -5, \qquad c = 8-k


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−5)^{2}−4(2)(8−𝑘) \\ & =25−8(8−𝑘) \\ & =25−64+8𝑘 \\ & =8𝑘−39.\end{aligned}


$$

For no real solutions, we need $\mathcal{D} < 0{:}$

$$


\begin{aligned}8𝑘−39 & <0 \\ 8𝑘 & <39 \\ 𝑘 & <\frac{39}{8} \\ 𝑘 & <4.875\end{aligned}


$$

Since $k$ must be an integer, we conclude that the greatest possible value is $4.$
