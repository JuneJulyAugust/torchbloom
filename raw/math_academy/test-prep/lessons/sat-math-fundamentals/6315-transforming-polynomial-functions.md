# Transforming Polynomial Functions

Source: https://www.mathacademy.com/topics/6315?courseId=120
Topic ID: 6315

## Prerequisites

- [Multiplicities of the Roots of Polynomials](../../../high-school/traditional/lessons/algebra-ii/88-multiplicities-of-the-roots-of-polynomials.md)
- [The Average of the Roots Formula](../../../high-school/traditional/lessons/algebra-i/1451-the-average-of-the-roots-formula.md)
- [Describing Function Composition](../../../high-school/traditional/lessons/algebra-i/3817-describing-function-composition.md)
- [Finding Equations of Translated Functions](./6085-finding-equations-of-translated-functions.md)

## Lesson

### Introduction

In this lesson, we will learn how to transform polynomial functions by shifting their graphs and determining how these shifts affect their properties.

Suppose a curve is defined by $y = f(x),$ where

$$


f(x) = (x-7)(x+4).


$$

If $y = g(x)$ is a horizontal translation of $y = f(x)$ by $2$ units right, how can we find $g(x)?$

We're given the curve

$$


y = (x-7)(x+4)


$$

and we wish to translate this curve by $2$ units to the right.

Recall that to shift the curve $y = f(x)$ by $2$ units to the *right*, we *add* $2$ to each $x$-coordinate to get the corresponding point on the new curve $y = g(x)$. So, the $x$-coordinates of the points on the new curve are given by

$$


x_{\text{new}} = x + 2.


$$

This equation is equivalent to

$$


x = x_{\text{new}} - 2.


$$

To get the equation of the new curve, we substitute this into the equation of the first curve. Doing this, we get

$$


\begin{aligned}𝑦 & =(𝑥−7)(𝑥+4) \\ 𝑦 & =((𝑥_{new}−2)−7)((𝑥_{new}−2)+4).\end{aligned}


$$

Dropping the $\text{new}$ suffix, we get

$$


y = ((x - 2) - 7)((x - 2) + 4).


$$

Finally, simplifying the expression, we have

$$


\begin{aligned}𝑦 & =((𝑥−2)−7)((𝑥−2)+4) \\ 𝑦 & =(𝑥−2−7)(𝑥−2+4) \\ 𝑦 & =(𝑥−9)(𝑥+2).\end{aligned}


$$

Therefore, we conclude that

$$


g(x) = (x-9)(x+2).


$$

We can check that this answer makes sense by examining the roots of both functions:

- From the equation we can see that the roots are $x=7$ and $x=-4.$

- From the equation we can see that the roots are $x=9$ and $x=-2.$

- Thus, we can see that the roots have shifted two units *right* under the transformation.

### Example: Horizontal Translations of Quadratic Functions

#### Question

A curve is defined by $y = f(x),$ where $f(x) = -x^2 + x + 2.$ If $y = g(x)$ is a horizontal translation of $y = f(x)$ by $2$ units left, what is the function $g(x)?$

#### Explanation

We're given the curve

$$


y = -x^2 + x + 2


$$

and we wish to translate this curve by $2$ units left.

For each point on the curve $y = f(x),$ we must subtract $2$ from each $x$-coordinate to get the corresponding point on the new curve $y = g(x).$ So, the $x$-coordinates of the points on the new curve are given by

$$


x_{\text{new}} = x - 2.


$$

This equation is equivalent to

$$


x = x_{\text{new}} + 2.


$$

To get the equation of the new curve, we substitute this into the equation of the first curve. Doing this, we get

$$


\begin{aligned}𝑦 & =−𝑥^{2}+𝑥+2 \\ 𝑦 & =−(𝑥_{new}+2)^{2}+(𝑥_{new}+2)+2.\end{aligned}


$$

Dropping the $\text{new}$ suffix, we get

$$


y = -(x + 2)^2 + (x + 2) + 2.


$$

Finally, simplifying the expression, we have

$$


\begin{aligned}𝑦 & =−(𝑥+2)^{2}+(𝑥+2)+2 \\ 𝑦 & =−𝑥^{2}−4𝑥−4+𝑥+2+2 \\ 𝑦 & =−𝑥^{2}−3𝑥.\end{aligned}


$$

Therefore, $g(x) = -x^2 - 3x.$

### Properties of Transformed Functions

When we transform a function, every point on its graph is transformed in the same way. We can use this fact to quickly determine properties of transformed functions.

For example, suppose we have the parabola $y = f(x),$ where the function $f$ is given by

$$


f(x) = (x - 7)(x + 3)


$$

and we want to determine the vertex of $y = g(x),$ where the function $g$ is defined by

$$


g(x) = f(x + 2).


$$

To find the vertex, we could transform $f$ to find $g$ and then find the vertex of $g.$ However, it's faster and easier to translate the vertex of $f.$

We start by noting the following:

- Since $g(x) = f(x + 2),$ the graph of $y = g(x)$ is obtained by shifting the graph of $y = f(x)$ by $2$ units to the *left.*

- Therefore, to obtain the corresponding points on $y = g(x),$ we *subtract* $2$ from each $x$-coordinate of $y = f(x)$ while keeping the $y$-coordinate unchanged.

Notice that $f$ is expressed in factored form. Therefore, the roots of $f$ are

$$


x_1=7\quad\text{and}\quad x_2=-3.


$$

To find the $x$-coordinate of the vertex of $y = f(x),$ we take the average of the roots, as follows:

$$


\begin{aligned}𝑥 & =\frac{𝑥_{1}+𝑥_{2}}{2} \\ & =\frac{7+(−3)}{2} \\ & =\frac{4}{2} \\ & =2\end{aligned}


$$

Next, to find the $y$-coordinate of the vertex of $y = f(x),$ we substitute $x = 2$ into $f(x){:}$

$$


\begin{aligned}𝑓(2) & =(2−7)(2+3) \\ & =(−5)(5) \\ & =−25\end{aligned}


$$

So, the vertex of $y = f(x)$ is $(2,-25).$

Therefore, *subtracting* $2$ from the $x$-coordinate, the vertex of $y = g(x)$ is

$$


(2-2, -25)


$$

which simplifies as

$$


(0,-25).


$$

Therefore, we conclude that the vertex of $y = g(x)$ is at the point $(0,-25).$

### Example: Determining Properties of Translated Quadratic Functions

#### Question

A parabola is given by $y=f(x),$ where

$$


f(x) = x^2 + 8x + 5.


$$

The function $g$ is defined by $g(x) = f(x - 5).$ What is the vertex of $y = g(x)?$

#### Explanation

We start by noting the following:

- Since $g(x) = f(x - 5),$ the graph of $y = g(x)$ is obtained by shifting the graph of $y = f(x)$ by $5$ units to the **

- Therefore, to obtain the corresponding points on $y = g(x),$ we ** $5$ to each $x$-coordinate of $y = f(x)$ while keeping the $y$-coordinate unchanged.

Now, recall that the $x$-coordinate of the vertex of a quadratic function $y = ax^2 + bx + c$ is

$$


x = -\dfrac{b}{2a}.


$$

Here, $a = 1$ and $b = 8$, so the $x$-coordinate of the vertex of $y = f(x)$ is

$$


\begin{aligned}𝑥 & =−\frac{8}{2(1)} \\ & =−4.\end{aligned}


$$

Next, to find the $y$-coordinate of the vertex of $y = f(x),$ we substitute $x = -4$ into $f(x){:}$

$$


\begin{aligned}𝑓(𝑥) & =𝑥^{2}+8𝑥+5 \\ 𝑓(−4) & =(−4)^{2}+8(−4)+5 \\ & =16−32+5 \\ & =−11\end{aligned}


$$

So, the vertex of $y = f(x)$ is $(-4,-11).$

Therefore, ** $5$ to the $x$-coordinate, the vertex of $y = g(x)$ is

$$


(-4+5, -11) = \left(1, -11\right).


$$

### Example: Determining Properties of the Preimage

#### Question

A parabola is given by $y = g(x),$ where

$$


g(x) = (x-7)(x+5).


$$

Suppose the function $g$ is defined by $g(x) = f(x-6).$ What is the vertex of $y = f(x)?$

#### Explanation

We start by noting the following:

- Since $g(x) = f(x - 6),$ the graph of $y = g(x)$ is obtained by shifting the graph of $y = f(x)$ by $6$ units to the right.

- Therefore, the graph of $y = f(x)$ is obtained by shifting the graph of $y = g(x)$ by $6$ units to the **

- So, to obtain the corresponding points on $y = f(x),$ we ** $6$ from each $x$-coordinate of $y = g(x)$ while keeping the $y$-coordinate unchanged.

From the equation $g(x) = (x-7)(x+5),$ we find that the roots of the parabola are $x_1=7$ and $x_2=-5.$

To find the $x$-coordinate of the vertex of $y = g(x),$ we take the average of the roots, as follows:

$$


\begin{aligned}𝑥 & =\frac{𝑥_{1}+𝑥_{2}}{2} \\ & =\frac{7+(−5)}{2} \\ & =\frac{2}{2} \\ & =1\end{aligned}


$$

Next, to find the $y$-coordinate of the vertex of $y = g(x),$ we substitute $x = 1$ into $g(x){:}$

$$


\begin{aligned}𝑔(𝑥) & =(𝑥−7)(𝑥+5) \\ 𝑔(1) & =(1−7)(1+5) \\ & =(−6)(6) \\ & =−36\end{aligned}


$$

So, the vertex of $y = g(x)$ is $(1,-36).$

Therefore, ** $6$ from the $x$-coordinate, the vertex of $y = f(x)$ is

$$


(1-6, -36) = \left(-5, -36\right).


$$

### Higher-Order Polynomials

Let's now consider cases where we transform higher-order polynomials.

Suppose we have the function

$$


f(x) = (x+4)(x-6)^2


$$

and we are told that $f(12-k) = 0,$ where $k$ is a constant. What are the possible values of $k?$

The function $f(x)$ is written in factored form, so we can immediately deduce its zeros:

- From the factor $(x+4),$ we get $x=-4.$

- From the factor $(x-6)^2,$ we get $x=6.$

Notice that $x=6$ is a *double root* because the factor $(x-6)$ is squared. So the zeros of $f$ are $x=-4$ and $x=6.$

The equation $f(12-k)=0$ means that the input $12-k$ must be equal to one of the zeros of $f.$

Therefore,

$$


\begin{aligned}12−𝑘=−4\, & ⇒\,𝑘=16, \\ 12−𝑘=6\, & ⇒\,𝑘=6.\end{aligned}


$$

So the possible values of $k$ are $6$ and $16.$

### Example: Determining Roots of Transformed Higher-Order Polynomials

#### Question

A function $f$ is defined by

$$


f(x)=(x+5)(x+1)(x-6).


$$

Define $k$ by $k(x)=f(x+2).$ The graph $y=k(x)$ has $x$-intercepts at $(s,0)$, $(t,0)$, and $(u,0),$ where $s> t > u$ are distinct constants. What is the value of $s+t+u?$

#### Explanation

We start by noting the following:

- Since $k(x) = f(x + 2),$ the graph of $k(x)$ is obtained by shifting the graph of $f(x)$ by $2$ units to the **

- Therefore, to obtain the corresponding points on $k(x),$ we ** $2$ from each $x$-coordinate of $f(x)$ while keeping the $y$-coordinate unchanged.

The $x$-intercepts of $y=k(x)$ occur where $k(x)=0$, i.e., where $f(x+2)=0.$ By the zero product property, the zeros of $f$ are

$$


x = -5,\qquad x = -1, \qquad x = 6.


$$

Therefore, ** $2$ from the $x$-coordinates, we get the roots of $k$:

$$


\begin{aligned}𝑠 & =6−2=4 \\ 𝑡 & =−1−2=−3 \\ 𝑢 & =−5−2=−7\end{aligned}


$$

Thus, the $x$-intercepts are $(4,0)$, $(-3,0)$, and $(-7,0)$, and their $x$-coordinates sum to

$$


s+t+u=4+(-3)+(-7)=-6.


$$

So, $s+t+u=-6.$
