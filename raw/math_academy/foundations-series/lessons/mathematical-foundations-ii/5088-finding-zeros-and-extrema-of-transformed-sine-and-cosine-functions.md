# Finding Zeros and Extrema of Transformed Sine and Cosine Functions

Source: https://www.mathacademy.com/topics/5088?courseId=111
Topic ID: 5088

## Prerequisites

- [Properties of Transformed Sine and Cosine Functions](./2062-properties-of-transformed-sine-and-cosine-functions.md)

## Lesson

### Introduction

In this lesson, we'll learn how to construct expressions that describe the zeros, maxima, and minima of transformed sine and cosine functions.

First, let's recall the following facts:

- The zeros of the sine function $y = \sin x$ are given by where $n$ is any integer.

- The zeros of the cosine function $y = \cos x$ are given by where $n$ is any integer.

Let's use these facts to find the zeros of a transformed sine or cosine function.

### A Worked Example

Let's find a general expression that describes all of the zeros of

$$


y = 5\cos \left( 2x - \dfrac{\pi}{3} \right).


$$

First, let's start by defining a new variable $X$ as

$$


X = 2x - \dfrac{\pi}{3}.


$$

So, we now need to calculate the zeros of

$$


y = 5\cos X.


$$

As we saw previously, the zeros of this function are given by the expression

$$


X = \dfrac{\pi}{2} + n\pi,


$$

where $n$ is any integer.

So, to find the zeros of our original function $y = 5\cos \left(2x - \dfrac{\pi}{3} \right),$ we rewrite $X$ in terms of the original variable $x$ and solve the resulting equation for $x{:}$

$$


\begin{aligned}𝑋 & =\frac{𝜋}{2}+𝑛𝜋 \\ 2𝑥−\frac{𝜋}{3} & =\frac{𝜋}{2}+𝑛𝜋 \\ 2𝑥 & =\frac{𝜋}{2}+𝑛𝜋+\frac{𝜋}{3} \\ 2𝑥 & =\frac{5𝜋}{6}+𝑛𝜋 \\ 𝑥 & =\frac{5𝜋}{12}+\frac{𝑛𝜋}{2}\end{aligned}


$$

Therefore, we conclude that the zeros of $y = 5\cos \left(2x - \dfrac{\pi}{3} \right)$ are given by

$$


x = \dfrac{5\pi}{12} + \dfrac{n\pi}{2}


$$

where $n$ is any integer.

Let's look at an example involving the sine function.

### Example: Finding the Zeros of a Transformed Sine or Cosine Function

#### Question

Find a general expression describing all of the zeros of $y = \sin\left(\dfrac x 2\right).$

#### Explanation

First, let's start by defining a new variable $X$ as

$$


X = \dfrac x 2.


$$

So, we need to calculate the zeros of

$$


y=\sin X.


$$

The zeros of this function are given by the following expression:

$$


X =n\pi


$$

where $n$ is an integer.

To find the zeros of our original function, we rewrite $X$ in terms of the original variable $x$ and solve the resulting equation for $x{:}$

$$


\begin{aligned}𝑋 & =𝑛𝜋 \\ \frac{𝑥}{2} & =𝑛𝜋 \\ 𝑥 & =2𝑛𝜋\end{aligned}


$$

Therefore, we conclude that the zeros are $x =2n\pi,$ where $n$ is any integer.

### Extreme Values of the Sine Function

We'll now turn our attention to the minima and maxima of transformed sine and cosine functions.

First, recall the graph of $y=\sin{x}$ once again.

![Instructional graphic](../../../lesson-assets/mathematical-foundations-ii/topic-5088/a3fe7870ea24e47e.png)

Recall that:

- The function has a maximum when $x=\dfrac\pi 2$ and the function is periodic with period $2\pi.$ Therefore, a general expression for the $x$-values that maximize sine is

- The function has a minimum when $x=-\dfrac\pi 2$ and the function is periodic with period $2\pi.$ Therefore, a general expression for the $x$-values that minimize sine is

$$


x = -\dfrac{\pi}{2} + 2n\pi.


$$

### Extreme Values of the Cosine Function

Now, recall the graph of $y=\cos x{:}$

![Instructional graphic](../../../lesson-assets/mathematical-foundations-ii/topic-5088/e5daab1276c6cb6d.png)

- The function has a maximum when $x=0$ and is periodic with period $2\pi.$ Therefore, a general expression for the $x$-values that maximize cosine is

- The function has a minimum when $x=\pi$ and is periodic with period $2\pi.$ Therefore, a general expression for the $x$-values that minimize cosine is

$$


x = \pi + 2n\pi.


$$

Let's now apply these results to transformed sine and cosine functions.

### Example: Maxima of Transformed Sine or Cosine Functions

#### Question

Consider the function $f(x) = 5\cos \left(2x + \dfrac{\pi}{3} \right).$ Find an expression that gives the $x$-values at which $f(x)$ attains its maximum value. Assume that $n$ is an integer.

#### Explanation

First, let's start by defining a new variable $X$ as

$$


X =2x + \dfrac{\pi}{3}.


$$

So, we need to calculate $X$-values at the maxima of

$$


y = 5\cos X.


$$

The $X$-values at the maxima are given by the following expression:

$$


X = 2n\pi


$$

where $n$ is an integer.

To find the $x$-values at the maxima of our original function, we rewrite $X$ in terms of the original variable $x$ and solve the resulting equation for $x{:}$

$$


\begin{aligned}𝑋 & =2𝑛𝜋 \\ 2𝑥+\frac{𝜋}{3} & =2𝑛𝜋 \\ 2𝑥 & =−\frac{𝜋}{3}+2𝑛𝜋 \\ 𝑥 & =−\frac{𝜋}{6}+𝑛𝜋\end{aligned}


$$

We conclude that the values of $x$ that maximize $f(x)$ are given by $x= -\dfrac{\pi}{6} + n\pi,$ where $n$ is any integer.

### Example: Minima of Transformed Sine or Cosine Functions

#### Question

Consider the function $f(x) =\sin \left(3x + 45^{\circ} \right).$ Find an expression that gives the $x$-values at which $f(x)$ attains its minimum value.

#### Explanation

First, let's start by defining a new variable $X$ as

$$


X = 3x + 45^{\circ}.


$$

So, we need to calculate $X$-values at the minima of

$$


f(x) = \sin X.


$$

The $X$-values at the minima are given by the following expression:

$$


X = -90^\circ+360^\circ\cdot n


$$

where $n$ is an integer.

To find the $x$-values at the minima of our original function, we rewrite $X$ in terms of the original variable $x$ and solve the resulting equation for $x{:}$

$$


\begin{aligned}𝑋 & =−90^{∘}+360^{∘}⋅𝑛 \\ 3𝑥+45^{∘} & =−90^{∘}+360^{∘}⋅𝑛 \\ 3𝑥 & =−45^{∘}−90^{∘}+360^{∘}⋅𝑛 \\ 3𝑥 & =−135^{∘}+360^{∘}⋅𝑛 \\ 𝑥 & =−45^{∘}+120^{∘}⋅𝑛\end{aligned}


$$

We conclude that the values of $x$ that minimize $f(x)$ are given by $x=-45^\circ + 120^\circ \cdot n,$ where $n$ is any integer.
