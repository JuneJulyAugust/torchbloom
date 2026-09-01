# Finding the Canonical Form of a Quadratic Form Using Lagrange's Method

Source: https://www.mathacademy.com/topics/3124?courseId=55
Topic ID: 3124

## Prerequisites

- [Change of Variables in Quadratic Forms](./3122-change-of-variables-in-quadratic-forms.md)
- [Completing the Square With Leading Coefficients](../../../high-school/traditional/lessons/algebra-i/3824-completing-the-square-with-leading-coefficients.md)

## Lesson

### Introduction

A quadratic form is said to be in its **canonical form** if it does not contain any cross-product terms ($x_i x_j$ where $i \neq j$).

With that in mind, which of the following quadratic forms are given in their canonical forms?

1. $P(\mathbf{x})=x_1^2-2x_2^2$

2. $Q(\mathbf{x})=x_1^2+2x_1x_3+x_2^2$

Let's examine our quadratic forms in turn.

- $P(\mathbf{x})$ is in canonical form. Indeed, the form does not contain any cross-product terms (it contains only squares).

- $Q(\mathbf{x})$ is *not* in canonical form since it contains the cross-product term $2x_1x_3.$

In terms of matrix representation

$$


\mathbf{x}^T \! A \mathbf{x},


$$

we have a canonical form if the corresponding matrix $A$ is diagonal.

For example, which of the following quadratic forms are given in their canonical forms?

1. $R(\mathbf{x})=\mathbf{x}^T \! A \mathbf{x},$ where $[\begin{aligned}0 & 0 \\ 0 & 1\end{aligned}]$

2. $S(\mathbf{x})=\mathbf{x}^T \! A \mathbf{x},$ where $[\begin{aligned}1 & 0 \\ −1 & 1\end{aligned}]$

Examining our quadratic forms, we obtain the following.

- $R(\mathbf{x})$ is in canonical form. Indeed, its corresponding matrix is diagonal.

- $S(\mathbf{x})$ is *not* in canonical form since its corresponding matrix is not diagonal.

### Example: Identifying the Canonical Form of a Quadratic Form

#### Question

Which of the following quadratic forms are given in their canonical forms?

1. $P(\mathbf{x})=x_1^2-2x_2x_3+x_3^2$

2. $Q(\mathbf{x})=\mathbf{x}^T \! A \mathbf{x},$ where $[\begin{aligned}2 & 0 \\ 0 & −2\end{aligned}]$

3. $R(\mathbf{x})=x_3^2-2x_1^2$

#### Explanation

A quadratic form in its canonical form shouldn't contain any cross-product terms ($x_i x_j$ where $i \neq j$). In terms of its matrix representation, this means that the corresponding matrix is diagonal.

With that in mind, let's examine our quadratic forms in turn.

- $P(\mathbf{x})$ is ** in canonical form since it contains the cross-product term $2x_2x_3.$

- $Q(\mathbf{x})$ is in canonical form. Indeed, its corresponding matrix is diagonal.

- $R(\mathbf{x})$ is in canonical form. Indeed, the form does not contain any cross-product terms (it contains only squares).

Therefore, the correct answer is "$Q(\mathbf{x})$ and $R(\mathbf{x})$ only."

### Lagrange's Method

**Lagrange's method** can be used to reduce any quadratic form to a canonical form by completing the squares and applying changes of variables.

To see how it works, let's reduce

$$


Q(\mathbf{x})=x_1^2 +5x_2^2 + 4x_1x_2-2x_1x_3-4x_2x_3


$$

to its canonical form.

First, we group $x_1^2$-term with all cross-product terms that contain $x_1$ and complete the square inside the parentheses:

$$


\begin{aligned}𝑄(𝐱) & =𝑥_{21}+5𝑥_{22}+4𝑥_{1}𝑥_{2}−2𝑥_{1}𝑥_{3}−4𝑥_{2}𝑥_{3} \\ & =(𝑥_{21}+4𝑥_{1}𝑥_{2}−2𝑥_{1}𝑥_{3})−4𝑥_{2}𝑥_{3}+5𝑥_{22} \\ & =(𝑥_{21}+2𝑥_{1}(2𝑥_{2}−𝑥_{3}))−4𝑥_{2}𝑥_{3}+5𝑥_{22} \\ & =(𝑥_{21}+2𝑥_{1}(2𝑥_{2}−𝑥_{3})+(2𝑥_{2}−𝑥_{3})^{2}−(2𝑥_{2}−𝑥_{3})^{2})−4𝑥_{2}𝑥_{3}+5𝑥_{22} \\ & =(𝑥_{1}+2𝑥_{2}−𝑥_{3})^{2}−(2𝑥_{2}−𝑥_{3})^{2}−4𝑥_{2}𝑥_{3}+5𝑥_{22} \\ & =(𝑥_{1}+2𝑥_{2}−𝑥_{3})^{2}−4𝑥_{22}+4𝑥_{2}𝑥_{3}−𝑥_{23}−4𝑥_{2}𝑥_{3}+5𝑥_{22} \\ & =(𝑥_{1}+2𝑥_{2}−𝑥_{3})^{2}+𝑥_{22}−𝑥_{23}\end{aligned}


$$

Finally, the canonical form is

$$


y_1^2 + y_2^2 - y_3^2,


$$

where we performed the following substitution:

$$


\begin{aligned}𝑦_{1}=𝑥_{1}+2𝑥_{2}−𝑥_{3} \\ 𝑦_{2}=𝑥_{2} \\ 𝑦_{3}=𝑥_{3}\end{aligned}


$$

### Example: Reducing a Quadratic Form to Canonical Form Using Lagrange's Method: 2D-Case

#### Question

Lagrange's method can be used to reduce the quadratic form $Q(\mathbf{x})=9x_1^2-18x_1x_2+5x_2^2$ to the canonical form given below.

$$


\,4\,


$$

From left to right, what is missing from the blank spaces?

#### Explanation

We apply Lagrange's method as follows:

First, we group $x_1^2$-term with all cross-product terms that contain $x_1$ and factor out the coefficient of $x_1^2\mathbin{:}$

$$


\begin{aligned}𝑄(𝐱) & =9𝑥_{21}−18𝑥_{1}𝑥_{2}+5𝑥_{22} \\ & =(9𝑥_{21}−18𝑥_{1}𝑥_{2})+5𝑥_{22} \\ & =9(𝑥_{21}−2𝑥_{1}𝑥_{2})+5𝑥_{22}\end{aligned}


$$

Next, we complete the square inside the parentheses:

$$


\begin{aligned}9(𝑥_{21}−2𝑥_{1}𝑥_{2})+5𝑥_{22} & =9([𝑥_{21}−2𝑥_{1}𝑥_{2}+𝑥_{22}]−𝑥_{22})+5𝑥_{22} \\ & =9((𝑥_{1}−𝑥_{2})^{2}−𝑥_{22})+5𝑥_{22}\end{aligned}


$$

Then, we simplify the expression:

$$


\begin{aligned}9((𝑥_{1}−𝑥_{2})^{2}−𝑥_{22})+5𝑥_{22} & =9(𝑥_{1}−𝑥_{2})^{2}−9𝑥_{22}+5𝑥_{22} \\ & =9(𝑥_{1}−𝑥_{2})^{2}−4𝑥_{22}\end{aligned}


$$

Finally, the canonical form is

$$


\begin{aligned}𝑦_{1}=𝑥_{1}−𝑥_{2} \\ 𝑦_{2}=𝑥_{2}.\end{aligned}


$$

Therefore, from left to right, the missing parts are as follows:

$\qquad$ $4 \quad$ and $\quad x_1-x_2.$

### Example: Reducing a Quadratic Form to Canonical Form Using Lagrange's Method: 3D-Case

#### Question

Lagrange's method can be used to reduce the quadratic form $Q(\mathbf{x})=x_1^2-4x_3^2+2x_1x_2-4x_1x_3+2x_2x_3$ to the canonical form given below.

$$


\begin{aligned}𝑦_{1}=\phantom{x_1+x_2-2x_3} \\ 𝑦_{2}=\phantom{x_2-3x_3} \\ 𝑦_{3}=𝑥_{3}\end{aligned}


$$

From top to bottom, what is missing from the blank spaces?

#### Explanation

We apply Lagrange's method as follows:

First, we group $x_1^2$-term with all cross-product terms that contain $x_1$ and complete the square inside the parentheses:

$$


\begin{aligned}𝑄(𝐱) & =𝑥_{21}−4𝑥_{23}+2𝑥_{1}𝑥_{2}−4𝑥_{1}𝑥_{3}+2𝑥_{2}𝑥_{3} \\ & =(𝑥_{21}+2𝑥_{1}𝑥_{2}−4𝑥_{1}𝑥_{3})+2𝑥_{2}𝑥_{3}−4𝑥_{23} \\ & =(𝑥_{21}+2𝑥_{1}(𝑥_{2}−2𝑥_{3}))+2𝑥_{2}𝑥_{3}−4𝑥_{23} \\ & =(𝑥_{21}+2𝑥_{1}(𝑥_{2}−2𝑥_{3})+(𝑥_{2}−2𝑥_{3})^{2}−(𝑥_{2}−2𝑥_{3})^{2})+2𝑥_{2}𝑥_{3}−4𝑥_{23} \\ & =(𝑥_{1}+𝑥_{2}−2𝑥_{3})^{2}−(𝑥_{2}−2𝑥_{3})^{2}+2𝑥_{2}𝑥_{3}−4𝑥_{23} \\ & =(𝑥_{1}+𝑥_{2}−2𝑥_{3})^{2}−𝑥_{22}+4𝑥_{2}𝑥_{3}−4𝑥_{23}+2𝑥_{2}𝑥_{3}−4𝑥_{23} \\ & =(𝑥_{1}+𝑥_{2}−2𝑥_{3})^{2}−𝑥_{22}+6𝑥_{2}𝑥_{3}−8𝑥_{23}\end{aligned}


$$

Next, we group $x_2^2$-term with all cross-product terms that contain $x_2,$ factor out the coefficient of $x_2^2,$ and complete the square inside the second parentheses:

$$


\begin{aligned}𝑄(𝐱) & =(𝑥_{1}+𝑥_{2}−2𝑥_{3})^{2}−𝑥_{22}+6𝑥_{2}𝑥_{3}−8𝑥_{23} \\ & =(𝑥_{1}+𝑥_{2}−2𝑥_{3})^{2}−(𝑥_{22}−6𝑥_{2}𝑥_{3})−8𝑥_{23} \\ & =(𝑥_{1}+𝑥_{2}−2𝑥_{3})^{2}−([𝑥_{22}−6𝑥_{2}𝑥_{3}+9𝑥_{23}]−9𝑥_{23})−8𝑥_{23} \\ & =(𝑥_{1}+𝑥_{2}−2𝑥_{3})^{2}−(𝑥_{2}−3𝑥_{3})^{2}+9𝑥_{23}−8𝑥_{23} \\ & =(𝑥_{1}+𝑥_{2}−2𝑥_{3})^{2}−(𝑥_{2}−3𝑥_{3})^{2}+𝑥_{23}\end{aligned}


$$

Finally, the canonical form is

$$


\begin{aligned}𝑦_{1}=𝑥_{1}+𝑥_{2}−2𝑥_{3} \\ 𝑦_{2}=𝑥_{2}−3𝑥_{3} \\ 𝑦_{3}=𝑥_{3}\end{aligned}


$$

Therefore, from top to bottom, the missing parts are as follows:

$\qquad$ $x_1+x_2-2x_3 \quad$ and $\quad x_2-3x_3.$

### Non-Uniqueness of a Canonical Form

Consider the quadratic function

$$


Q(\mathbf{x})=x_1^2-2x_2^2+2x_1x_2.


$$

Using Lagrange's method, we can find its canonical form

$$


y_1^2 - 3y_2^2,


$$

where $y_1 = x_1+x_2$ and $y_2 = x_2.$

**Watch out!** This is not the only possible canonical form! For example, substituting

$$


\begin{aligned}𝑧_{1}=𝑦_{1} \\ 𝑧_{2}=\sqrt{3}𝑦_{2}\end{aligned}


$$

we obtain

$$


z_1^2-z_2^2,


$$

which is another canonical form of $Q(\mathbf{x}).$ In conclusion, the canonical (diagonal) form is *not* unique.

On the other hand, among all the possibilities, there is one special canonical form.

The **normal form** of a quadratic function is a canonical form where all coefficients are either $1$ or $-1.$

The normal form is unique (up to the order of the terms) for each quadratic function.
