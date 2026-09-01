# The Determinant of a 3x3 Matrix

Source: https://www.mathacademy.com/topics/153?courseId=136
Topic ID: 153

## Prerequisites

- [The Minors of a 3x3 Matrix](./233-the-minors-of-a-3x3-matrix.md)
- [Introduction to the Inverse of a Matrix](./863-introduction-to-the-inverse-of-a-matrix.md)

## Lesson

### Introduction

How do we find the determinant of a $3\times3$ matrix such as

$$


\begin{aligned}7 & 1 & −3 \\ 3 & 2 & 4 \\ 5 & 0 & −1\end{aligned}


$$

One way to do this is to take the alternating sum of the entries in the top row of the matrix, multiplied by their respective minors, as shown below:

$$


\begin{aligned}\begin{matrix}7 & 1 & −3 \\ 3 & 2 & 4 \\ 5 & 0 & −1\end{matrix} & =\underset{𝑎_{11}}{\underset{}{(\,7\,)}}⋅\overset{\begin{matrix}2 & 4 \\ 0 & −1\end{matrix}}{𝑀_{11}}−\underset{𝑎_{12}}{\underset{}{(\,1\,)}}⋅\overset{\begin{matrix}3 & 4 \\ 5 & −1\end{matrix}}{𝑀_{12}}+\underset{𝑎_{13}}{\underset{}{(−3)}}⋅\overset{\begin{matrix}3 & 2 \\ 5 & 0\end{matrix}}{𝑀_{13}} \\ & =7(−2−0)−1(−3−20)−3(0−10) \\ & =−14+23+30 \\ & =39\end{aligned}


$$

In the above, we have denoted $\color{blue}M_{1j}$ as the minor of the entry ${\color{red}a_{1j}}.$

In general, the determinant of a $3\times 3$ matrix $A$ is given by

$$


\det(A) = {\color{red}a_{11}}{\color{blue}M_{11}} - {\color{red}a_{12}}{\color{blue}M_{12}} + {\color{red}a_{13}}{\color{blue}M_{13}}.


$$

That is, if $\begin{aligned}𝑎 & 𝑏 & 𝑐 \\ 𝑑 & 𝑒 & 𝑓 \\ 𝑔 & ℎ & 𝑖\end{aligned}$ then

$$


\begin{aligned}\begin{matrix}𝑎 & 𝑏 & 𝑐 \\ 𝑑 & 𝑒 & 𝑓 \\ 𝑔 & ℎ & 𝑖\end{matrix} & =𝑎\begin{matrix}𝑒 & 𝑓 \\ ℎ & 𝑖\end{matrix}−𝑏\begin{matrix}𝑑 & 𝑓 \\ 𝑔 & 𝑖\end{matrix}+𝑐\begin{matrix}𝑑 & 𝑒 \\ 𝑔 & ℎ\end{matrix} \\ & =𝑎(𝑒𝑖−𝑓ℎ)−𝑏(𝑑𝑖−𝑓𝑔)+𝑐(𝑑ℎ−𝑒𝑔).\end{aligned}


$$

**Important:** Do not forget about the *minus sign* in front of the *second term* in the formula!

### Example: Calculating the Determinant of a 3x3 Matrix

#### Question

Find the value of $\begin{aligned}0 & −3 & 6 \\ 8 & 8 & 8 \\ −6 & −12 & 1\end{aligned}$

#### Explanation

Using the formula, we take the alternating sum of the entries in the top row of the matrix, multiplied by their respective minors, as follows:

$$


\begin{aligned}\begin{matrix}0 & −3 & 6 \\ 8 & 8 & 8 \\ −6 & −12 & 1\end{matrix} & =0\begin{matrix}8 & 8 \\ −12 & 1\end{matrix}−(−3)\begin{matrix}8 & 8 \\ −6 & 1\end{matrix}+6\begin{matrix}8 & 8 \\ −6 & −12\end{matrix} \\ & =0(8+96)+3(8+48)+6(−96+48) \\ & =0+3⋅56+6⋅(−48) \\ & =168−288 \\ & =−120\end{aligned}


$$

### Singular Matrices

If the determinant of a square matrix $A$ is equal to zero, then we say that $A$ is a **singular** matrix.

If a matrix is singular, then it does not have a multiplicative inverse.

### Example: Identifying Singular Matrices

#### Question

Which of the following statements are true regarding the matrix $A$ given below?

1. $\det(A) = 0$

2. $A$ is **** a singular matrix

3. $A$ is a singular matrix

$$


\begin{aligned}1 & 2 & 3 \\ 1 & 0 & 1 \\ 3 & 4 & 7\end{aligned}


$$

#### Explanation

Remember that a square matrix is singular if its determinant is equal to $0.$

Using the formula, we take the alternating sum of the entries in the top row of the matrix, multiplied by their respective minors, as follows:

$$


\begin{aligned}det(𝐴) & =\begin{matrix}1 & 2 & 3 \\ 1 & 0 & 1 \\ 3 & 4 & 7\end{matrix} \\ & =1\begin{matrix}0 & 1 \\ 4 & 7\end{matrix}−2\begin{matrix}1 & 1 \\ 3 & 7\end{matrix}+3\begin{matrix}1 & 0 \\ 3 & 4\end{matrix} \\ & =1(0−4)−2(7−3)+3(4−0) \\ & =−4−2⋅4+3⋅4 \\ & =−4−8+12 \\ & =0\end{aligned}


$$

Since $\det(A)=0$, the matrix is singular.

Therefore, only statements I and III are true.

### Solving for a Variable

Suppose we are given the $3\times 3$ matrix

$$


\begin{aligned}1 & 2 & 3 \\ 𝑘 & −1 & 1 \\ 0 & 2 & 1\end{aligned}


$$

that has an unknown constant $k$ as one of the entries, and we are given that $A$ is singular. How do we find all the possible values of $k?$

One way is to use the formula for the determinant of a $3 \times 3$ matrix to find an expression for the determinant in terms of $k,$ and then make an equation with the given determinant to solve for $k.$

So first, let's use the formula for the determinant on our matrix to get an expression in terms of $k\mathbin{:}$

$$


\begin{aligned}\begin{matrix}1 & 2 & 3 \\ 𝑘 & −1 & 1 \\ 0 & 2 & 1\end{matrix} & =1\begin{matrix}−1 & 1 \\ 2 & 1\end{matrix}−2\begin{matrix}𝑘 & 1 \\ 0 & 1\end{matrix}+3\begin{matrix}𝑘 & −1 \\ 0 & 2\end{matrix} \\ & =(−1−2)−2(𝑘−0)+3(2𝑘−0) \\ & =−3−2𝑘+6𝑘 \\ & =4𝑘−3\end{aligned}


$$

Now, since we are told that $\det(A) =0,$ let's equate the above expression to $0$ and solve for $k\mathbin{:}$

$$


\begin{aligned}\begin{matrix}1 & 2 & 3 \\ 𝑘 & −1 & 1 \\ 0 & 2 & 1\end{matrix} & =0 \\ 4𝑘−3 & =0 \\ 4𝑘 & =3 \\ 𝑘 & =\frac{3}{4}\end{aligned}


$$

Therefore, the only possible value for $k$ is $\dfrac{3}{4}.$

### Example: Solving for an Unknown Given the Determinant

#### Question

Given that the determinant of $\begin{aligned}3 & 1 & 2 \\ 𝑘 & 4 & 5 \\ 0 & 2 & 3\end{aligned}$ is $2,$ find the value of the constant $k.$

#### Explanation

Let's use our formula to find an expression for the determinant in terms of $k\mathbin{:}$

$$


\begin{aligned}\begin{matrix}3 & 1 & 2 \\ 𝑘 & 4 & 5 \\ 0 & 2 & 3\end{matrix} & =3\begin{matrix}4 & 5 \\ 2 & 3\end{matrix}−1\begin{matrix}𝑘 & 5 \\ 0 & 3\end{matrix}+2\begin{matrix}𝑘 & 4 \\ 0 & 2\end{matrix} \\ & =3(12−10)−1(3𝑘−0)+2(2𝑘−0) \\ & =3⋅2−1⋅3𝑘+2⋅2𝑘 \\ & =6−3𝑘+4𝑘 \\ & =𝑘+6\end{aligned}


$$

Since the determinant of the matrix is $2,$ we have:

$$


\begin{aligned}𝑘+6 & =2 \\ 𝑘 & =−4\end{aligned}


$$
