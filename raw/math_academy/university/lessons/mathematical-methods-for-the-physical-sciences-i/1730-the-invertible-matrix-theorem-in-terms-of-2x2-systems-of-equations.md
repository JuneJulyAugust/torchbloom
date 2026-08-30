# The Invertible Matrix Theorem in Terms of 2x2 Systems of Equations

Source: https://www.mathacademy.com/topics/1730?courseId=154
Topic ID: 1730

## Prerequisites

- [Solving 2x2 Systems of Equations Using Inverse Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/934-solving-2x2-systems-of-equations-using-inverse-matrices.md)

## Lesson

### Introduction

Consider a system of two linear equations with two variables

$$


\begin{aligned}𝑎_{11}𝑥+𝑎_{12}𝑦=𝑏_{1} \\ 𝑎_{21}𝑥+𝑎_{22}𝑦=𝑏_{2},\end{aligned}


$$

and let

$$


[\begin{aligned}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{aligned}]


$$

Recall that we can write the system as $A \mathbf{x} = \mathbf{b}.$ The **invertible matrix theorem** says the following statements are equivalent:

1. $A$ is invertible (that is, $A^{-1}$ exists).

2. The system $A\mathbf{x}=\mathbf{b}$ has exactly one solution for any $2 \times 1$ column vector $\mathbf{b}$ (we call such systems consistent independent).

3. The system $A\mathbf{x}=\mathbf{0}$ has the unique solution $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$

4. The lines ${\color{red}{a_{11}}}x+{\color{red}{a_{12}}}y={\color{blue}{b_1}}$ and ${\color{red}{a_{21}}}x+{\color{red}{a_{22}}}y={\color{blue}{b_2}}$ intersect at one point.

5. The determinant of $A$ is nonzero (that is, $\det(A) \neq 0$).

### Example: Identifying a True Statement Concerning a 2x2 System of Equations

#### Question

Consider a system of two linear equations in two variables, represented by the matrix equation $A\mathbf{x}=\mathbf{b}$ in the usual way. Given that the system has exactly one solution, which of the following statements are true?

1. $\det(A) =0$

2. The system $[\begin{aligned}2 \\ 2\end{aligned}]$ has exactly one solution

3. $A^{-1}$ does not exist

#### Explanation

Recall that given $[\begin{aligned}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{aligned}]$, then according to the invertible matrix theorem the following statements are equivalent:

1. $A$ is invertible.

2. The system $A\mathbf{x}=\mathbf{b}$ has exactly one solution for any $2 \times 1$ column vector $\mathbf{b}.$

3. The system $A\mathbf{x}=\mathbf{0}$ has the unique zero solution.

4. The lines $a_{11}x+a_{12}y=b_1$ and $a_{21}x+a_{22}y=b_2$ intersect at exactly one point.

5. $\det(A) \neq 0.$

Also, we are told that the second part of the invertible matrix theorem is true. So, all the other parts of the theorem are true too. Therefore, according to the theorem:

- Statement I is false by the fifth part of the invertible matrix theorem.

- Statement II is true by the second part of the invertible matrix theorem.

- Statement III is false by the first part of the invertible matrix theorem.

Therefore, only statement II is true.

### Example: Identifying a True Statement Given a 2x2 Matrix

#### Question

Let $[\begin{aligned}1 & −2 \\ −2 & 𝑘\end{aligned}]$ and $[\begin{aligned}1 \\ −3\end{aligned}]$ where $k\neq 4$ is a constant. Which of the following statements are true?

1. $\det(A) = 0$

2. $A\mathbf{x}=\mathbf{b}$ has no solutions

3. The lines $x-2y=1$ and $-2x+ky=-3$ intersect at exactly one point

#### Explanation

Recall that given $[\begin{aligned}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{aligned}]$, then according to the invertible matrix theorem the following statements are equivalent:

1. $A$ is invertible.

2. The system $A\mathbf{x}=\mathbf{b}$ has exactly one solution for any $2 \times 1$ column vector $\mathbf{b}.$

3. The system $A\mathbf{x}=\mathbf{0}$ has the unique zero solution.

4. The lines $a_{11}x+a_{12}y=b_1$ and $a_{21}x+a_{22}y=b_2$ intersect at exactly one point.

5. $\det(A) \neq 0.$

With that in mind, let's now check our statements.

- Statement I is false. We have where $k - 4 \neq 0$ if $k \neq 4.$ So, since the fifth part in the invertible matrix theorem is true, all the other parts of the theorem are true too. Therefore, according to the theorem:

- Statement II is false. According to the second part of the invertible matrix theorem, there must be exactly one solution to $A\mathbf{x}=\mathbf{b}.$

- Statement III is true by the fourth part of the invertible matrix theorem.

Therefore, only statement III is true.

### Example: Completing a True Statement

#### Question

Which of the following completes the statement so that it is true:

**

1. $A\mathbf{x}=\mathbf{0}$ has infinitely many solutions

2. $A\mathbf{x}=\mathbf{0}$ has exactly one solution

3. $\det(A) = 0$

#### Explanation

Recall that given $[\begin{aligned}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{aligned}]$, then according to the invertible matrix theorem the following statements are equivalent:

1. $A$ is invertible.

2. The system $A\mathbf{x}=\mathbf{b}$ has exactly one solution for any $2 \times 1$ column vector $\mathbf{b}.$

3. The system $A\mathbf{x}=\mathbf{0}$ has the unique zero solution.

4. The lines $a_{11}x+a_{12}y=b_1$ and $a_{21}x+a_{22}y=b_2$ intersect at exactly one point.

5. $\det(A) \neq 0.$

With that in mind, let's now check our statements.

Notice that since the first part of the invertible matrix theorem is true ($A$ is invertible), all the other parts of the theorem are true too. Therefore, according to the theorem, only option II gives us a true statement:

- ** $\quad \color{green}\checkmark$
