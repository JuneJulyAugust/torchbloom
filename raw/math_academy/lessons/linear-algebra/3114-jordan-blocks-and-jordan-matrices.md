# Jordan Blocks and Jordan Matrices

Source: https://www.mathacademy.com/topics/3114?courseId=55
Topic ID: 3114

## Prerequisites

- [Partitioned and Block Matrices](./1735-partitioned-and-block-matrices.md)

## Lesson

### Introduction

A **Jordan block** is a square matrix that has the following properties:

- the same value ${\color{blue}\lambda}$ on the main diagonal,

- ${\color{violet}1}$'s on the superdiagonal (the diagonal above the main one),

- zeros everywhere else.

A general Jordan block is shown below.

$$


\begin{aligned}𝜆 & 1 & 0 & 0 & ⋯ & 0 \\ 0 & 𝜆 & 1 & 0 & ⋯ & 0 \\ 0 & 0 & 𝜆 & 1 & ⋯ & 0 \\ ⋮ & ⋮ & ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & 0 & 0 & ⋯ & 1 \\ 0 & 0 & 0 & 0 & ⋯ & 𝜆\end{aligned}


$$

For example,

$$


\begin{aligned}9 & 1 & 0 \\ 0 & 9 & 1 \\ 0 & 0 & 9\end{aligned}


$$

is a Jordan block. Indeed, it has

- the same value $({\color{blue}9})$ on the main diagonal,

- ${\color{violet}1}$'s on the superdiagonal,

- zeros everywhere else.

On the other hand, the matrices

$$


\begin{aligned}−2 & 1 & 0 \\ 0 & −2 & 0 \\ 0 & 0 & −2\end{aligned}


$$

are *not* Jordan blocks. The matrix $B$ does not have all $1$'s on the superdiagonal, while $C$ has a nonzero entry below the main diagonal.

### Example: Identifying Jordan Blocks

#### Question

Which of the following matrices are Jordan blocks?

$$


[\begin{aligned}−3 & 1 \\ 1 & −3\end{aligned}]


$$

#### Explanation

$$


\begin{aligned}𝜆 & 1 & 0 & 0 & ⋯ & 0 \\ 0 & 𝜆 & 1 & 0 & ⋯ & 0 \\ 0 & 0 & 𝜆 & 1 & ⋯ & 0 \\ ⋮ & ⋮ & ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & 0 & 0 & ⋯ & 1 \\ 0 & 0 & 0 & 0 & ⋯ & 𝜆\end{aligned}


$$

A ** is a square matrix that has the following properties:

- the same value ${\color{blue}\lambda}$ on the main diagonal,

- ${\color{violet}1}$'s on the superdiagonal (the diagonal above the main one),

- zeros everywhere else.

With that in mind, let's examine our matrices.

- $A$ is ** a Jordan block since it has nonzero entries outside the main diagonal and superdiagonal:

- $B$ is ** a Jordan block since it does not have all ones on the superdiagonal:

- $C$ is a Jordan block. Indeed, it has: the same value $({\color{blue}8})$ on the main diagonal, ${\color{violet}1}$'s on the superdiagonal, zeros everywhere else.

Therefore, the correct answer is "$C$ only."

### Notation for Jordan Blocks

Consider the following Jordan block:

$$


\begin{aligned}9 & 1 & 0 \\ 0 & 9 & 1 \\ 0 & 0 & 9\end{aligned}


$$

We can denote this Jordan block compactly using the notation $J_{\color{red}3}({\color{blue}{9}}).$

- The index ${\color{red}3}$ in $J_{\color{red}3}({\color{blue}{9}})$ means that we have a ${\color{red}3} \times {\color{red}3}$ matrix.

- The value ${\color{blue}9}$ in $J_{3}({\color{blue}9})$ means that we have ${\color{blue}9}$'s on the main diagonal.

- Also, since $J_{\color{red}3}({\color{blue}{9}})$ denotes a Jordan block, we know that we must have ${\color{violet}1}$'s on the superdiagonal, and zeros everywhere outside the main diagonal and superdiagonal.

### Example: Constructing Jordan Blocks

#### Question

Construct the matrix $J_4(-7).$

#### Explanation

Let's construct our matrix:

- The index ${\color{red}4}$ in $J_{\color{red}4}(-7)$ means that we have a ${\color{red}4} \times {\color{red}4}$ matrix.

- The value ${\color{blue}-7}$ in $J_{4}({\color{blue}-7})$ means that we have ${\color{blue}-7}$'s on the main diagonal.

- Also, we must have ${\color{violet}1}$'s on the superdiagonal (the diagonal above the main one).

Given that all the other entries must be zero, our Jordan block is

$$


\begin{aligned}−7 & 1 & 0 & 0 \\ 0 & −7 & 1 & 0 \\ 0 & 0 & −7 & 1 \\ 0 & 0 & 0 & −7\end{aligned}


$$

### Compositions of Jordan Blocks

We can generate new matrices by composing Jordan blocks.

For instance, suppose we have the following Jordan blocks:

$$


[\begin{aligned}3 & 1 \\ 0 & 3\end{aligned}]


$$

Their composition is a block diagonal matrix that can be written as follows:

$$


\begin{aligned}3 & 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & −5\end{aligned}


$$

We can compose more than two Jordan blocks. For example, if

$$


[\begin{aligned}−1\end{aligned}]


$$

then the composition of these Jordan blocks is given by

$$


\begin{aligned}−1 & 0 & 0 & 0 \\ 0 & 4 & 1 & 0 \\ 0 & 0 & 4 & 0 \\ 0 & 0 & 0 & 2\end{aligned}


$$

Matrices that are formed by composing Jordan blocks are called **Jordan matrices**.

### Example: Identifying Matrices Corresponding to a Composition of Jordan Blocks

#### Question

Calculate the matrix $J_2(3) {\textstyle\:\oplus\:} J_1(1).$

#### Explanation

First, recall the following:

- $J_2(3)$ represents a $2\times 2$ Jordan block with $3$'s on the leading diagonal.

- $J_1(1)$ represents a $1\times 1$ Jordan block with $1$'s on the leading diagonal.

Therefore, our Jordan blocks are given by

$$


[\begin{aligned}3 & 1 \\ 0 & 3\end{aligned}]


$$

The composition of our Jordan blocks gives the following block diagonal matrix:

$$


\begin{aligned}3 & 1 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1\end{aligned}


$$

### Example: Writing a Matrix as a Composition of Jordan Blocks

#### Question

$$


\begin{aligned}7 & 1 & 0 & 0 \\ 0 & 7 & 0 & 0 \\ 0 & 0 & −4 & 0 \\ 0 & 0 & 0 & −3\end{aligned}


$$

Consider the matrix above. Find its decomposition using Jordan blocks.

#### Explanation

Our matrix can be represented as the composition of three Jordan blocks (one $2 \times 2$ block and two $1 \times 1$ blocks), as follows:

$$


\begin{aligned}7 & 1 & 0 & 0 \\ 0 & 7 & 0 & 0 \\ 0 & 0 & −4 & 0 \\ 0 & 0 & 0 & −3\end{aligned}


$$
