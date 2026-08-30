# Scalar Multiplication of Matrices

Source: https://www.mathacademy.com/topics/146?courseId=101
Topic ID: 146

## Prerequisites

- [Adding and Subtracting Matrices](./29-adding-and-subtracting-matrices.md)
- [Solving One-Step Multiplication and Division Equations](../grade-7/40-solving-one-step-multiplication-and-division-equations.md)
- [Index Notation for Matrices](./1167-index-notation-for-matrices.md)

## Lesson

### Introduction

We can multiply matrices by numbers. This type of multiplication is known as **scalar multiplication**. Here, a **scalar** is just a number.

For example, consider the matrix

$$


[\begin{aligned}1 & 3 \\ 2 & 4\end{aligned}]


$$

To multiply ${A}$ by the scalar $2,$ we just multiply each entry of ${A}$ by $2\mathbin{:}$

$$


\begin{aligned}2𝐴 & =2[\begin{aligned}1 & 3 \\ 2 & 4\end{aligned}] \\ & =[\begin{aligned}2⋅1 & 2⋅3 \\ 2⋅2 & 2⋅4\end{aligned}] \\ & =[\begin{aligned}2 & 6 \\ 4 & 8\end{aligned}]\end{aligned}


$$

In general, to multiply a $m \times n$ matrix $A$ by a scalar $c,$ we multiply each entry of $A$ by $c$ as follows:

$$


\begin{aligned}𝑎_{11} & 𝑎_{12} & … & 𝑎_{1𝑛} \\ 𝑎_{21} & 𝑎_{22} & … & 𝑎_{2𝑛} \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 𝑎_{𝑚1} & 𝑎_{𝑚2} & … & 𝑎_{𝑚𝑛}\end{aligned}


$$

### Example: Multiplying a Matrix by a Scalar

#### Question

Calculate $-2A$, if $A=\left\lbrack \matrix {2 & -1 \ 4 & 7} \right\rbrack.$

#### Explanation

We multiply each entry of $A$ by $-2,$ as follows:

$$


\begin{aligned}−2𝐴 & =−2[\begin{aligned}2 & −1 \\ 4 & 7\end{aligned}] \\ & =[\begin{aligned}−2⋅2 & −2⋅(−1) \\ −2⋅4 & −2⋅7\end{aligned}] \\ & =[\begin{aligned}−4 & 2 \\ −8 & −14\end{aligned}]\end{aligned}


$$

### Example: Calculating the Value of a Scalar

#### Question

If $k {A} = \left\lbrack \matrix {1 & 3 & 4 \ 6 & 0 & -2} \right\rbrack,$ where ${A} = \left\lbrack \matrix {2 & 6 & 8 \ 12 & 0 & -4} \right\rbrack$ and $k$ is a scalar, calculate the value of $k.$

#### Explanation

To express $kA,$ we multiply each entry of $A$ by $k,$ as follows:

$$


\begin{aligned}𝑘𝐴 & =𝑘⋅[\begin{aligned}2 & 6 & 8 \\ 12 & 0 & −4\end{aligned}] \\ & =[\begin{aligned}2𝑘 & 6𝑘 & 8𝑘 \\ 12𝑘 & 0 & −4𝑘\end{aligned}]\end{aligned}


$$

Now, we set the above result equal to the matrix given for $kA$ in the problem statement:

$$


\left\lbrack \matrix { 2k & 6k & 8k \ 12k & 0 & -4k } \right\rbrack = \left\lbrack \matrix { 1 & 3 & 4 \ 6 & 0 & -2 } \right\rbrack


$$

We can solve for $k$ by equating any two corresponding (nonzero) elements. Let's choose the top-left elements, $2k$ and $1.$ Equating these elements, we get

$$


\begin{aligned}2𝑘 & =1 \\ 𝑘 & =\frac{1}{2}.\end{aligned}


$$

**** We would still get the same result if we chose any other two corresponding (nonzero) elements.

### Properties of Scalar Multiplication of Matrices

Since scalar multiplication is done entry-wise, it obeys the same kind of rules as multiplication of real numbers.

For example, for any numbers $c_1, c_2$ and any matrix $A,$ we can perform scalar multiplication in any order:

$$


c_1 (c_2 A) = (c_1 c_2) A = c_2 (c_1 A)


$$

Moreover, we can distribute a matrix over the sum or difference of scalars:

$$


(c_1 \pm c_2)A = c_1A \pm c_2A


$$

We can also distribute scalar multiplication over the sum or difference of two matrices:

$$


c (A \pm B) = c A \pm c B


$$

### Example: Calculating a Linear Combination of Two Matrices

#### Question

Calculate $2 {A} + \dfrac{1}{2} {B}$, where $[\begin{aligned}1 & 5 \\ 1 & 2\end{aligned}]$ and ${B}= \left\lbrack \matrix {0 & 2 \ 4 & 2} \right\rbrack.$

#### Explanation

We multiply each entry of $A$ by $2$ and each entry of $B$ by $\dfrac{1}{2},$ and then add the resulting matrices, as follows:

$$


\begin{aligned}2𝐴+\frac{1}{2}𝐵 & =2[\begin{aligned}1 & 5 \\ 1 & 2\end{aligned}]+\frac{1}{2}[\begin{aligned}0 & 2 \\ 4 & 2\end{aligned}] \\ & =[\begin{aligned}2⋅1 & 2⋅5 \\ 2⋅1 & 2⋅2\end{aligned}]+\begin{aligned}\frac{1}{2}⋅0 & \frac{1}{2}⋅2 \\ \frac{1}{2}⋅4 & \frac{1}{2}⋅2\end{aligned} \\ & =[\begin{aligned}2 & 10 \\ 2 & 4\end{aligned}]+[\begin{aligned}0 & 1 \\ 2 & 1\end{aligned}] \\ & =[\begin{aligned}2+0 & 10+1 \\ 2+2 & 4+1\end{aligned}] \\ & =[\begin{aligned}2 & 11 \\ 4 & 5\end{aligned}]\end{aligned}


$$
