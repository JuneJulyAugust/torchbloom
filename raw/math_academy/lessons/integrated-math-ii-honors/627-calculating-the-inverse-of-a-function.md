# Calculating the Inverse of a Function

Source: https://www.mathacademy.com/topics/627?courseId=128
Topic ID: 627

## Prerequisites

- [Solving Many-Variable Equations](../algebra-i/354-solving-many-variable-equations.md)
- [Invertible Functions](../algebra-ii/1889-invertible-functions.md)

## Lesson

### Introduction

Suppose that we have the function $f(x) = 3x-9,$ and we wish to find the inverse function $f^{-1}(x).$ There's a simple technique that often works. The technique is described below in four steps.

**Step 1:** Replace $f(x)$ with $y.$

$$


y = 3x-9


$$

**Step 2:** Swap $x$ and $y.$

$$


x = 3y-9


$$

**Step 3:** Solve for $y.$

$$


\begin{aligned}𝑥 & =3𝑦−9 \\ 𝑥+9 & =3𝑦 \\ \frac{𝑥+9}{3} & =𝑦\end{aligned}


$$

**Step 4:** Replace $y$ with $f^{-1}(x).$

$$


f^{-1}(x) = \frac{x+9}{3}


$$

To verify that this is really the inverse of $f,$ we can check that

$$


(f\circ f^{-1})(x) = (f^{-1}\circ f)(x) = x.


$$

First, we check that $(f^{-1}\circ f)(x)=x\mathbin{:}$

$$


\begin{aligned}(𝑓^{−1}∘𝑓)(𝑥) & =𝑓^{−1}(𝑓(𝑥)) \\ & =\frac{𝑓(𝑥)+9}{3} \\ & =\frac{(3𝑥−9)+9}{3} \\ & =\frac{3𝑥}{3} \\ & =𝑥\end{aligned}


$$

So we've shown that $(f^{-1}\circ f)(x) = x.$ Using the same technique, we can verify that $(f \circ f^{-1})(x)=x\mathbin{:}$

$$


\begin{aligned}(𝑓∘𝑓^{−1})(𝑥) & =𝑓(𝑓^{−1}(𝑥)) \\ & =3𝑓^{−1}(𝑥)−9 \\ & =3(\frac{𝑥+9}{3})−9 \\ & =𝑥+9−9 \\ & =𝑥\end{aligned}


$$

Therefore, since $(f\circ f^{-1})(x) = (f^{-1}\circ f)(x) = x,$ we can be sure that we've found the correct inverse function.

### Example: Finding the Inverse of a Linear Function

#### Question

Find the inverse of $f(x) = 3x - 4.$

#### Explanation

To find the inverse of a function, we follow the four steps below.

**** Replace $f(x)$ with $y.$

$$


y = 3x-4


$$

**** Swap $x$ and $y.$

$$


x = 3y-4


$$

**** Solve for $y.$

$$


\begin{aligned}𝑥 & =3𝑦−4 \\ 𝑥+4 & =3𝑦 \\ \frac{𝑥+4}{3} & =𝑦\end{aligned}


$$

**** Replace $y$ with $f^{-1}(x).$

$$


f^{-1}(x) = \dfrac {x + 4} {3}


$$

### Example: Finding the Inverse of a Function With a Parameter

#### Question

Find the inverse of the function $f(x) = bx-5,$ where $b$ is a constant.

#### Explanation

To find the inverse of a function, we follow the four steps below.

**** Replace $f(x)$ with $y.$

$$


y = bx- 5


$$

**** Swap $x$ and $y.$

$$


x = by- 5


$$

**** Solve for $y.$

$$


\begin{aligned}𝑥 & =𝑏𝑦−5 \\ 𝑥+5 & =𝑏𝑦 \\ \frac{𝑥+5}{𝑏} & =𝑦\end{aligned}


$$

**** Replace $y$ with $f^{-1}(x).$

$$


f^{-1}(x) = \dfrac{x + 5}{b}


$$
