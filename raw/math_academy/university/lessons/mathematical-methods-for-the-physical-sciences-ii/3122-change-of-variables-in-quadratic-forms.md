# Change of Variables in Quadratic Forms

Source: https://www.mathacademy.com/topics/3122?courseId=155
Topic ID: 3122

## Prerequisites

- [Changing a Basis Using the Change-of-Coordinates Matrix](../linear-algebra/1910-changing-a-basis-using-the-change-of-coordinates-matrix.md)
- [Quadratic Forms](./3123-quadratic-forms.md)

## Lesson

### Introduction

Suppose we are given the quadratic form

$$


Q(\mathbf{x})= x_1^2-8x_1x_2 + x_2^2


$$

and the matrix $[\begin{aligned}2 & −1 \\ 0 & −1\end{aligned}]$ that defines the **change of variable**

$$


\mathbf{x} =P \mathbf{y} ,


$$

where $[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]$ and $[\begin{aligned}𝑦_{1} \\ 𝑦_{2}\end{aligned}]$

How do we express $Q(\mathbf{x})$ in terms of the components of $\mathbf{y}?$

First, notice that

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

gives the following expressions for $x_1$ and $x_2\mathbin{:}$

$$


\begin{aligned}𝑥_{1} & =2𝑦_{1}−𝑦_{2} \\ 𝑥_{2} & =−𝑦_{2}\end{aligned}


$$

So, if we substitute these into our quadratic form expression, we get:

$$


\begin{aligned}𝑄(𝐱) & =𝑥_{21}−8𝑥_{1}𝑥_{2}+𝑥_{22} \\ & =(2𝑦_{1}−𝑦_{2})^{2}+8(2𝑦_{1}−𝑦_{2})𝑦_{2}+(−𝑦_{2})^{2} \\ & =4𝑦_{21}−4𝑦_{1}𝑦_{2}+𝑦_{22}+16𝑦_{1}𝑦_{2}−8𝑦_{22}+𝑦_{22} \\ & =4𝑦_{21}+12𝑦_{1}𝑦_{2}−6𝑦_{22}\end{aligned}


$$

### Example: Changing Variables in a Quadratic Form Given Old Variables Through New Variables

#### Question

Given that

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

express the quadratic form $Q(\mathbf{x})= x_1^2-x_2^2\,$ in terms of the components of $\mathbf{y}.$

#### Explanation

First, notice that

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

gives the following expressions for $x_1$ and $x_2\mathbin{:}$

$$


\begin{aligned}𝑥_{1} & =𝑦_{1}−𝑦_{2} \\ 𝑥_{2} & =2𝑦_{2}\end{aligned}


$$

Now, we substitute these into our quadratic form expression:

$$


\begin{aligned}𝑄(𝐱) & =𝑥_{21}−𝑥_{22} \\ & =(𝑦_{1}−𝑦_{2})^{2}−(2𝑦_{2})^{2} \\ & =𝑦_{21}−2𝑦_{1}𝑦_{2}+𝑦_{22}−4𝑦_{22} \\ & =𝑦_{21}−2𝑦_{1}𝑦_{2}−3𝑦_{22}\end{aligned}


$$

### Example: Changing Variables in a Quadratic Form Given New Variables Through Old Variables

#### Question

Given that

$$


[\begin{aligned}𝑦_{1} \\ 𝑦_{2}\end{aligned}]


$$

express the quadratic form $Q(\mathbf{x})= x_1x_2+2x_2^2$ in terms of the components of $\mathbf{y}.$

#### Explanation

First, notice that

$$


[\begin{aligned}𝑦_{1} \\ 𝑦_{2}\end{aligned}]


$$

gives the following expressions for $y_1$ and $y_2\mathbin{:}$

$$


\begin{aligned}𝑦_{1} & =2𝑥_{1}−𝑥_{2} \\ 𝑦_{2} & =−𝑥_{1}\end{aligned}


$$

By solving the second equation for $x_1$ and substituting it into the first equation, we obtain the following expressions for $x_1$ and $x_2\mathbin{:}$

$$


\begin{aligned}𝑥_{1} & =−𝑦_{2} \\ 𝑥_{2} & =−𝑦_{1}−2𝑦_{2}\end{aligned}


$$

Now, we substitute these into our quadratic form expression:

$$


\begin{aligned}𝑄(𝐱) & =𝑥_{1}𝑥_{2}+2𝑥_{22} \\ & =(−𝑦_{2})(−𝑦_{1}−2𝑦_{2})+2(−𝑦_{1}−2𝑦_{2})^{2} \\ & =𝑦_{2}𝑦_{1}+2𝑦_{22}+2𝑦_{21}+8𝑦_{1}𝑦_{2}+8𝑦_{22} \\ & =2𝑦_{21}+9𝑦_{1}𝑦_{2}+10𝑦_{22}\end{aligned}


$$

### The Connection Between Matrices of Quadratic Forms in Different Bases

Suppose we are given a quadratic form

$$


Q(\mathbf{x})= \mathbf{x}^T \! A\mathbf{x}


$$

and an invertible matrix $P$ that defines the change of variable

$$


\mathbf{x} =P \mathbf{y}.


$$

If this change of variable is applied to the quadratic form $Q(\mathbf{x}),$ what will be the new matrix of $Q$?

By making the necessary substitutions, we obtain the following:

$$


\begin{aligned}𝑄(𝐱) & =𝐱^{𝑇}\,𝐴𝐱 \\ & =(𝑃𝐲)^{𝑇}\,𝐴\,(𝑃𝐲) \\ & =𝐲^{𝑇}𝑃^{𝑇}\,𝐴𝑃\,𝐲 \\ & =𝐲^{𝑇}(𝑃^{𝑇}𝐴𝑃)𝐲\end{aligned}


$$

Therefore, the new matrix of our quadratic form is

$$


B= P^T \! A P.


$$

### Example: Finding the Matrix of a Quadratic Form Given a Change-of-Coordinates Matrix

#### Question

Consider the matrices $A$ and $P$ below. Find the matrix of the quadratic form $\mathbf{x}^T \! A \mathbf{x}$ in the basis that consists of the columns of $P.$

$$


[\begin{aligned}1 & −2 \\ −2 & 0\end{aligned}]


$$

#### Explanation

Recall that if $\mathbf{x}=[x_1, x_2]^T$ is a vector given by its coordinates in the standard basis and $\mathbf{y}=[y_1, y_2]^T$ is the same vector but given in the coordinates relative to the basis that consists of the columns of $P,$ then

$$


\mathbf{x} = P\mathbf{y}.


$$

As a result, we have

$$


\begin{aligned}𝐱^{𝑇}\,𝐴𝐱 & =(𝑃𝐲)^{𝑇}\,𝐴\,(𝑃𝐲) \\ & =(𝐲^{𝑇}𝑃^{𝑇})\,𝐴\,(𝑃𝐲) \\ & =𝐲^{𝑇}(𝑃^{𝑇}\,𝐴𝑃)\,𝐲,\end{aligned}


$$

which means that the matrix of our form in the new basis is

$$


\begin{aligned}𝑃^{𝑇}\,𝐴𝑃 & =[\begin{matrix}−1 & 2 \\ −1 & 1\end{matrix}]^{𝑇}[\begin{matrix}1 & −2 \\ −2 & 0\end{matrix}][\begin{matrix}−1 & 2 \\ −1 & 1\end{matrix}] \\ & =[\begin{matrix}−1 & −1 \\ 2 & 1\end{matrix}][\begin{matrix}1 & −2 \\ −2 & 0\end{matrix}][\begin{matrix}−1 & 2 \\ −1 & 1\end{matrix}] \\ & =[\begin{matrix}1 & 2 \\ 0 & −4\end{matrix}][\begin{matrix}−1 & 2 \\ −1 & 1\end{matrix}] \\ & =[\begin{matrix}−3 & 4 \\ 4 & −4\end{matrix}]\end{aligned}


$$

### Equivalent Quadratic Forms

Two quadratic forms $Q_1$ and $Q_2$ on $\Bbb R^n$ are said to be **equivalent** if they can be obtained from each other through a change of variable.

*The two quadratic forms with matrices $A$ and $B$ are equivalent if and only if there exists an invertible matrix $P$ such that*

$$


B = P^T \! A \, P.


$$

**Note:** Equivalent quadratic forms represent the same function from $\Bbb R^n$ to $\Bbb R.$
