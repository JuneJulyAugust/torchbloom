# Powers of Matrices

Source: https://www.mathacademy.com/topics/1725?courseId=136
Topic ID: 1725

## Prerequisites

- [Properties of Matrix Multiplication](./1724-properties-of-matrix-multiplication.md)

## Lesson

### Introduction

Powers of matrices are similar to powers of numbers. If $A$ is a matrix, then $A^n$ is $A$ multiplied by itself $n$ times:

$$


A^n = \underbrace{A\:\cdot\: A\:\cdot\: \ldots \:\cdot\: A}_{\Large{n\text{ times}}}


$$

For $A$ to be conformable with itself, $A$ needs to be a square matrix. So we can only take powers of square matrices.

To demonstrate, suppose that

$$


[\begin{aligned}3 & −1 \\ 2 & 1\end{aligned}]


$$

Then we can calculate $A^2$ as follows:

$$


\begin{aligned}𝐴^{2} & =𝐴⋅𝐴 \\ & =[\begin{aligned}3 & −1 \\ 2 & 1\end{aligned}]⋅[\begin{aligned}3 & −1 \\ 2 & 1\end{aligned}] \\ & =[\begin{aligned}3⋅3+(−1)⋅2 & 3⋅(−1)+(−1)⋅1 \\ 2⋅3+1⋅2 & 2⋅(−1)+1⋅1\end{aligned}] \\ & =[\begin{aligned}7 & −4 \\ 8 & −1\end{aligned}]\end{aligned}


$$

We say that $A^0 = I,$ the identity matrix of the same dimension as $A.$

### Example: Finding a Power of a Matrix

#### Question

Find $A^4$ given that $[\begin{aligned}3 & 0 \\ 5 & −1\end{aligned}]$

#### Explanation

First, to find $A^2,$ we multiply $A$ by itself:

$$


\begin{aligned}𝐴^{2} & =𝐴⋅𝐴 \\ & =[\begin{aligned}3 & 0 \\ 5 & −1\end{aligned}]⋅[\begin{aligned}3 & 0 \\ 5 & −1\end{aligned}] \\ & =[\begin{aligned}9 & 0 \\ 10 & 1\end{aligned}]\end{aligned}


$$

Now, since $A^4 = A^2 \cdot A^2,$ we get

$$


\begin{aligned}𝐴^{4} & =𝐴^{2}⋅𝐴^{2} \\ & =[\begin{aligned}9 & 0 \\ 10 & 1\end{aligned}]⋅[\begin{aligned}9 & 0 \\ 10 & 1\end{aligned}] \\ & =[\begin{aligned}81 & 0 \\ 100 & 1\end{aligned}].\end{aligned}


$$

### Matrix Polynomials

Now that we know how to compute powers of matrices, we can evaluate polynomials where the input is a square matrix.

For example, consider the polynomial

$$


f(X) = X^2 + 4X + 3.


$$

Note that, in order to evaluate this polynomial for an input matrix $X,$ we need to interpret any constants as multiples of the identity matrix. So, we interpret the polynomial as

$$


f(X) = X^2 + 4X + 3I.


$$

For example, if $[\begin{aligned}1 & 1 \\ 0 & 2\end{aligned}]$ then

$$


\begin{aligned}𝐴^{2} & =[\begin{aligned}1 & 1 \\ 0 & 2\end{aligned}][\begin{aligned}1 & 1 \\ 0 & 2\end{aligned}] \\ & =[\begin{aligned}1 & 3 \\ 0 & 4\end{aligned}],\end{aligned}


$$

and we can evaluate $f(A)$ as follows:

$$


\begin{aligned}𝑓(𝐴) & =𝐴^{2}+4𝐴+3𝐼 \\ & =[\begin{aligned}1 & 3 \\ 0 & 4\end{aligned}]+4[\begin{aligned}1 & 1 \\ 0 & 2\end{aligned}]+3[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}1 & 3 \\ 0 & 4\end{aligned}]+[\begin{aligned}4 & 4 \\ 0 & 8\end{aligned}]+[\begin{aligned}3 & 0 \\ 0 & 3\end{aligned}] \\ & =[\begin{aligned}1+4+3 & 3+4+0 \\ 0+0+0 & 4+8+3\end{aligned}] \\ & =[\begin{aligned}8 & 7 \\ 0 & 15\end{aligned}]\end{aligned}


$$

### Example: Evaluating a Matrix Polynomial

#### Question

Consider the matrix

$$


[\begin{aligned}1 & 5 \\ 0 & −3\end{aligned}]


$$

Find $f(D)$ if $f(X)=-X^2+3X+2.$

#### Explanation

First, we rewrite the polynomial, interpreting any constants as multiples of the identity matrix:

$$


\begin{aligned}𝑓(𝑋) & =−𝑋^{2}+3𝑋+2 \\ & =−𝑋^{2}+3𝑋+2𝐼\end{aligned}


$$

So, we want to find $f(D)=-D^2+3D+2I.$

Let's calculate $D^2$ as follows:

$$


\begin{aligned}𝐷^{2} & =𝐷⋅𝐷 \\ & =[\begin{aligned}1 & 5 \\ 0 & −3\end{aligned}]⋅[\begin{aligned}1 & 5 \\ 0 & −3\end{aligned}] \\ & =[\begin{aligned}1 & −10 \\ 0 & 9\end{aligned}]\end{aligned}


$$

Now, we can evaluate $f(D)\mathbin{:}$

$$


\begin{aligned}𝑓(𝐷) & =−𝐷^{2}+3𝐷+2𝐼 \\ & =−[\begin{aligned}1 & −10 \\ 0 & 9\end{aligned}]+3[\begin{aligned}1 & 5 \\ 0 & −3\end{aligned}]+2[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}−1 & 10 \\ 0 & −9\end{aligned}]+[\begin{aligned}3 & 15 \\ 0 & −9\end{aligned}]+[\begin{aligned}2 & 0 \\ 0 & 2\end{aligned}] \\ & =[\begin{aligned}−1+3+2 & 10+15+0 \\ 0 & −9−9+2\end{aligned}] \\ & =[\begin{aligned}4 & 25 \\ 0 & −16\end{aligned}]\end{aligned}


$$
