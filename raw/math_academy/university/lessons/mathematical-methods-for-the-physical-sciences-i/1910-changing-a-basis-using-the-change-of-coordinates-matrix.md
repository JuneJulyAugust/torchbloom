# Changing a Basis Using the Change-of-Coordinates Matrix

Source: https://www.mathacademy.com/topics/1910?courseId=154
Topic ID: 1910

## Prerequisites

- [The Change-of-Coordinates Matrix](./1928-the-change-of-coordinates-matrix.md)

## Lesson

### Introduction

Suppose that $\mathbf x \in V$ for some vector space $V,$ and that $\mathcal B$ and $\mathcal C$ are two bases of $V.$

To find the coordinates of $\mathbf{x}$ relative to $\mathcal{C}$ given its coordinates relative to $\mathcal B,$ we can use the **change-of-basis formula**

$$


\begin{aligned}[\,𝐱\,]_{C}=𝑃_{B→C}⋅[\,𝐱\,]_{B},\end{aligned}


$$

where we recall that

- $[\,\mathbf x\,]_{\color{blue}\mathcal{B}}$ and $[\,\mathbf x\,]_{\color{red}\mathcal{C}}$ are the coordinates of $\mathbf{x}$ relative to the bases $\color{blue}\mathcal{B}$ and ${\color{red}\mathcal{C}},$ respectively, and

- $P_{\small{\color{blue}\mathcal{B}}\to{\color{red}\mathcal{C}}}$ is the change-of-coordinates matrix from $\color{blue}\mathcal{B}$ to ${\color{red}\mathcal{C}},$ whose columns are the coordinates of vectors of the basis $\color{blue}\mathcal{B}$ relative to the basis ${\color{red}\mathcal{C}}.$

As an example, suppose we are given two bases $\mathcal{B}=\left\{\mathbf{b}_1, \mathbf{b}_2 \right\}$ and $\mathcal{C}=\left\{\mathbf{c}_1, \mathbf{c}_2 \right\}$ of a vector space $V,$ and we already know that the change-of-coordinates matrix from $\mathcal{B}$ to $\mathcal{C}$ is given by

$$


[\begin{aligned}−1 & 2 \\ 2 & 1\end{aligned}]


$$

Let $\mathbf{v} \in V$ and $[\begin{aligned}2 \\ 2\end{aligned}]$ Then we can easily find $[\,\mathbf{v}\,]_{\mathcal{C}},$ as follows:

$$


\begin{aligned}[\,𝐯\,]_{C} & =\overset{\overset{[\begin{aligned}−1 & 2 \\ 2 & 1\end{aligned}]}{}}{𝑃_{B→C}}⋅\overset{\overset{[\begin{aligned}2 \\ 2\end{aligned}]}{}}{[𝐯]_{B}} \\ & =[\begin{aligned}2 \\ 6\end{aligned}]\end{aligned}


$$

### The Change-of-Basis Formula in Expanded Form

We've seen that to find the coordinates of a vector $\mathbf{x}$ relative to a basis $\mathcal{C}$ given its coordinates relative to a basis $\mathcal B,$ we can use the formula

$$


\begin{aligned}[\,𝐱\,]_{C}=𝑃_{B→C}⋅[\,𝐱\,]_{B}.\end{aligned}


$$

In expanded form, the formula looks as follows:

$$


\begin{aligned}| \\ [𝐱]_{C} \\ |\end{aligned}


$$

Also, remember that the change-of-coordinates matrix from $\color{blue}\mathcal{B}$ to $\color{red}\mathcal{C}$ and from $\color{red}\mathcal{C}$ to $\color{blue}\mathcal{B}$ are the inverses of each other:

$$


P_{\small{\color{red}\mathcal{C}}\to{\color{blue}\mathcal{B}}} = P_{\small{\color{blue}\mathcal{B}}\to{\color{red}\mathcal{C}}}^{-1} \quad\textrm{and}\quad P_{\small{\color{blue}\mathcal{B}}\to{\color{red}\mathcal{C}}} = P_{\small{\color{red}\mathcal{C}}\to{\color{blue}\mathcal{B}}}^{-1}


$$

### Example: Finding the Coordinates of a Vector in a New Basis Given the Change-of-Coordinates Matrix

#### Question

The change-of-coordinates matrix from the basis $\mathcal{B}$ to the basis $\mathcal{C}$ and the coordinates of the vector $\mathbf{x}$ relative to the basis $\mathcal{B}$ are given below. What is $[\mathbf{x}]_{\mathcal{C}}?$

$$


[\begin{aligned}−3 & 6 \\ 5 & −8\end{aligned}]


$$

#### Explanation

Given the coordinates of $\mathbf{x}$ relative to $\mathcal{B}$ and the change-of-coordinates matrix from $\mathcal{B}$ to $\mathcal{C},$ we find the coordinates of $\mathbf{x}$ relative to $\mathcal{C}$ as follows:

$$


\begin{aligned}[\,𝐱\,]_{C} & =𝑃_{B→C}[\,𝐱\,]_{B} \\ & =[\begin{aligned}−3 & 6 \\ 5 & −8\end{aligned}][\begin{aligned}5 \\ 3\end{aligned}] \\ & =[\begin{aligned}3 \\ 1\end{aligned}]\end{aligned}


$$

### Example: Finding the Coordinates of a Vector in a New Basis Given the Inverse Change-of-Coordinates Matrix

#### Question

The change-of-coordinates matrix from $\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2 \}$ to $\mathcal{C} = \{\mathbf{c}_1,\mathbf{c}_2 \}$ is given below. Find $[\mathbf{x}]_{\mathcal{B}}$ given that $\mathbf{x} =2\mathbf{c}_1-6\mathbf{c}_2.$

$$


[\begin{aligned}−4 & 3 \\ 6 & −4\end{aligned}]


$$

#### Explanation

We will use the change-of-coordinates formula in the form

$$


[\,\mathbf{x}\,]_{\mathcal{B}} = P_{\small\mathcal{C}\to\mathcal{B}} [\,\mathbf{x}\,]_{\mathcal{C}} .


$$

First, we need to find the change-of-coordinates matrix $P_{\small\mathcal{C}\to\mathcal{B}}$ from $\mathcal{C}$ to $\mathcal{B}.$ To do that, we compute the inverse of $P_{\small\mathcal{B}\to\mathcal{C}}\mathbin{:}$

$$


\begin{aligned}𝑃_{C→B} & =𝑃_{−1B→C}^{} \\ & =[\begin{aligned}−4 & 3 \\ 6 & −4\end{aligned}]^{−1} \\ & =\frac{1}{(−4)(−4)−6⋅3}[\begin{aligned}−4 & −3 \\ −6 & −4\end{aligned}] \\ & =\begin{aligned}2 & \frac{3}{2} \\ 3 & 2\end{aligned}\end{aligned}


$$

Notice that since $\mathbf{x} = 2 \mathbf{c}_1-6\mathbf{c}_2,$ we obtain

$$


[\begin{aligned}2 \\ −6\end{aligned}]


$$

Now, we compute $[\,\mathbf{x}\,]_{\mathcal{B}}\mathbin{:}$

$$


\begin{aligned}[\,𝐱\,]_{B} & =𝑃_{C→B}[\,𝐱\,]_{C} \\ & =\begin{aligned}2 & \frac{3}{2} \\ 3 & 2\end{aligned}[\begin{aligned}2 \\ −6\end{aligned}] \\ & =[\begin{aligned}−5 \\ −6\end{aligned}]\end{aligned}


$$

### Example: Finding the Coordinates of a Vector in a New Basis Given Its Coordinates in the Standard Basis

#### Question

The basis $\mathcal{B}$ of $\mathbb{R}^2$ and the coordinates of the vector $\mathbf{x}$ relative to the standard basis $\mathcal{S}$ are given below. Find $[\mathbf{x}]_{\mathcal{B}}.$

$$


[\begin{aligned}1 \\ 3\end{aligned}]


$$

#### Explanation

We will use the change-of-coordinates formula in the form

$$


[\,\mathbf{x}\,]_{\mathcal{B}} = P_{\small\mathcal{S}\to\mathcal{B}} [\,\mathbf{x}\,]_{\mathcal{S}} .


$$

First, recall that the change-of-coordinates matrix from $\mathcal{B}$ to $\mathcal{S}$ is the matrix whose columns are the vectors of $\mathcal{B}$ relative to the standard basis $\mathcal{S}.$ As a result, we have

$$


[\begin{aligned}1 & 3 \\ 3 & 10\end{aligned}]


$$

Now, we need to find the change-of-coordinates matrix $P_{\small\mathcal{S}\to\mathcal{B}}$ from $\mathcal{S}$ to $\mathcal{B}.$ To do that, we compute the inverse of $P_{\small\mathcal{B}\to\mathcal{S}}\mathbin{:}$

$$


\begin{aligned}𝑃_{S→B} & =𝑃_{−1B→S}^{} \\ & =[\begin{aligned}1 & 3 \\ 3 & 10\end{aligned}]^{−1} \\ & =\frac{1}{1⋅10−3⋅3}[\begin{aligned}10 & −3 \\ −3 & 1\end{aligned}] \\ & =[\begin{aligned}10 & −3 \\ −3 & 1\end{aligned}]\end{aligned}


$$

Finally, we compute $[\,\mathbf{x}\,]_{\mathcal{B}}\mathbin{:}$

$$


\begin{aligned}[\,𝐱\,]_{B} & =𝑃_{S→B}[\,𝐱\,]_{S} \\ & =[\begin{aligned}10 & −3 \\ −3 & 1\end{aligned}][\begin{aligned}1 \\ 5\end{aligned}] \\ & =[\begin{aligned}−5 \\ 2\end{aligned}]\end{aligned}


$$

### Using Gaussian Elimination to Find the Coordinates of a Vector in a New Basis

Let $\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2 \}$ and $\mathcal{C}=\{\mathbf{c}_1,\mathbf{c}_2 \}$ be bases of $\mathbb{R}^2.$ Now, suppose we would like to find the coordinates of $\mathbf{b}_1$ and $\mathbf{b}_2$ relative to the basis $\mathcal{C}.$

- We first need to find $x_1$ and $x_2$ such that which is equivalent to solving the system with the augmented matrix

- Similarly, we need to find $y_1$ and $y_2$ such that which is equivalent to solving the system with the augmented matrix

We can solve both systems using Gaussian elimination. However, we can do that simultaneously by considering the matrix

$$


\begin{aligned}| & | & | & | \\ 𝐜_{1} & 𝐜_{2} & 𝐛_{1} & 𝐛_{2} \\ | & | & | & |\end{aligned}


$$

Reducing the left-hand side to reduced row-echelon form using Gaussian elimination, we get a matrix of the form

$$


\begin{aligned}𝑀 & ∼[\begin{aligned}1 & 0 & 𝑥_{1} & 𝑦_{1} \\ 0 & 1 & 𝑥_{2} & 𝑦_{2}\end{aligned}],\end{aligned}


$$

where the required coefficients will be stored in the columns on the right-hand side.

### Example: Finding the Coordinates of a Vector in a New Basis Given Its Coordinates in Another Basis

#### Question

The bases $\mathcal{B}$ and $\mathcal{C}$ of $\mathbb{R}^2$ and the coordinates of the vector $\mathbf{x}$ relative to the basis $\mathcal{B}$ are given below. Find $[\mathbf{x}]_{\mathcal{C}}.$

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

#### Explanation

Let's denote the vectors of $\mathcal{B}$ and $\mathcal{C}$ as $\{\mathbf{b}_1,\mathbf{b}_2 \}$ and $\{\mathbf{c}_1,\mathbf{c}_2 \},$ respectively.

The change-of-coordinates matrix from $\mathcal{B}$ to $\mathcal{C}$ is a matrix whose columns are the vectors of $\mathcal{B}$ relative to the basis $\mathcal{C}.$

So, we need to find the coordinates of $\mathbf{b}_1$ and $\mathbf{b}_2$ relative to the basis $\mathcal{C}.$ We can do this simultaneously by considering the matrix

$$


\begin{aligned}| & | & | & | \\ 𝐜_{1} & 𝐜_{2} & 𝐛_{1} & 𝐛_{2} \\ | & | & | & |\end{aligned}


$$

Reducing the left-hand side to reduced row-echelon form using Gaussian elimination, we get

$$


\begin{aligned}𝑀 & =[\begin{aligned}1 & 2 & 1 & 1 \\ 6 & 13 & 1 & −1\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+(−6)𝑅_{1} \\ & ∼[\begin{aligned}1 & 2 & 1 & 1 \\ 0 & 1 & −5 & −7\end{aligned}] & 𝑅_{1} & :=𝑅_{1}+(−2)𝑅_{2} \\ & ∼[\begin{aligned}1 & 0 & 11 & 15 \\ 0 & 1 & −5 & −7\end{aligned}]. & & \end{aligned}


$$

Therefore, the change-of-coordinates matrix $P_{\small\mathcal{B}\to\mathcal{C}}$ is

$$


[\begin{aligned}11 & 15 \\ −5 & −7\end{aligned}]


$$

Finally, we compute $[\,\mathbf{x}\,]_{\mathcal{C}}\mathbin{:}$

$$


\begin{aligned}[\,𝐱\,]_{C} & =𝑃_{B→C}[\,𝐱\,]_{B} \\ & =[\begin{aligned}11 & 15 \\ −5 & −7\end{aligned}][\begin{aligned}−2 \\ 1\end{aligned}] \\ & =[\begin{aligned}−7 \\ 3\end{aligned}]\end{aligned}


$$
