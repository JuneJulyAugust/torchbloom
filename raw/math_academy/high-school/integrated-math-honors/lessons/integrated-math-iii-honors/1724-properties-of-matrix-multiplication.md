# Properties of Matrix Multiplication

Source: https://www.mathacademy.com/topics/1724?courseId=101
Topic ID: 1724

## Prerequisites

- [Multiplying a Matrix by the Identity Matrix](./1171-multiplying-a-matrix-by-the-identity-matrix.md)
- [Multiplying Matrices](./1196-multiplying-matrices.md)

## Lesson

### Introduction

We have already seen some properties of matrix multiplication. For example, multiplying any $n \times n$ square matrix $A$ by the identity matrix $I_n$ will leave it unchanged:

$$


A I_n = I_n A = A.


$$

Also, matrix multiplication follows the **distributive laws**:

$$


\begin{aligned}(𝐴+𝐵)𝐶 & =𝐴𝐶+𝐵𝐶, \\ 𝐶(𝐴+𝐵) & =𝐶𝐴+𝐶𝐵.\end{aligned}


$$

### Example: Calculating a Matrix Product Using the Distributive Law

#### Question

Find $AB-CB,$ where

$$


\begin{aligned}2 & 4 & −3 \\ −1 & −5 & 3 \\ −2 & 0 & 7\end{aligned}


$$

#### Explanation

We can apply the distributive law

$$


AB-CB=(A-C)B.


$$

So, we calculate $A-C$ first:

$$


\begin{aligned}𝐴−𝐶 & =\begin{aligned}2 & 4 & −3 \\ −1 & −5 & 3 \\ −2 & 0 & 7\end{aligned}−\begin{aligned}3 & 4 & −3 \\ −1 & −4 & 3 \\ −2 & 0 & 8\end{aligned} \\ & =\begin{aligned}−1 & 0 & 0 \\ 0 & −1 & 0 \\ 0 & 0 & −1\end{aligned} \\ & =−𝐼_{3}\end{aligned}


$$

Finally, we obtain

$$


\begin{aligned}𝐴𝐵−𝐶𝐵 & =(𝐴−𝐶)𝐵 \\ & =−𝐼_{3}𝐵 \\ & =−𝐵 \\ & =\begin{aligned}−\sqrt{√2} & −\sqrt{√3} & 45 \\ −81 & \sqrt{√5} & 2 \\ −2 & −1 & −\sqrt{√3}\end{aligned}.\end{aligned}


$$

### The Associative Law for Matrix Multiplication

If $A,$ $B,$ and $C$ are three matrices that are conformable for multiplication, then they follow the **associative law**:

$$


\left( AB\right) C = A\left( BC\right)


$$

So, when we wish to compute a product $ABC,$ we don't always have to start by multiplying $AB.$ Alternatively, we can start by multiplying $BC,$ and then multiply $A$ by the result.

Sometimes rearranging the parentheses might make the computations slightly easier.

### Example: Calculating a Matrix Product Using the Associative Law

#### Question

Calculate $ABC,$ where

$$


\begin{aligned}1 & −1 & 0 \\ 4 & 3 & 1 \\ 1 & 2 & 1\end{aligned}


$$

#### Explanation

First, recall the associative law

$$


ABC = (AB)C = A(BC).


$$

Notice that $A$ is a $3 \times 3$ matrix, $B$ is a $3 \times 3$ matrix, and $C$ is a $3 \times 1$ matrix. Therefore,

- multiplying $A$ by $B$, we will obtain a $3 \times 3$ matrix that will require finding $9$ entries, while

- multiplying $B$ by $C$, we will obtain a $3 \times 1$ matrix that will require finding only $3$ entries.

So, we find the product $BC$ first:

$$


\begin{aligned}𝐵𝐶 & =\begin{aligned}−2 & 5 & −4 \\ 2 & 1 & 1 \\ −4 & 3 & −1\end{aligned}⋅\begin{aligned}−2 \\ 1 \\ 3\end{aligned} \\ & =\begin{aligned}−3 \\ 0 \\ 8\end{aligned}\end{aligned}


$$

Now, we multiply $A$ by $BC\mathbin{:}$

$$


\begin{aligned}𝐴𝐵𝐶 & =𝐴(𝐵𝐶) \\ & =\begin{aligned}1 & −1 & 0 \\ 4 & 3 & 1 \\ 1 & 2 & 1\end{aligned}⋅\begin{aligned}−3 \\ 0 \\ 8\end{aligned} \\ & =\begin{aligned}−3 \\ −4 \\ 5\end{aligned}\end{aligned}


$$

### Matrix Multiplication Is Not Commutative in General

In general, matrix multiplication is **not** commutative. In other words, given two general matrices $A$ and $B$ that are conformable for multiplication, we have

$$


AB \neq BA.


$$

However, some particular matrices may satisfy this property. For instance, $AI = IA$ (where $I$ is the identity matrix).

### Example: Identifying True Statements Regarding Matrix Multiplication

#### Question

Given that $A, B,$ and $C$ are $6 \times 6$ matrices, which of the following statements are always true?

1. $A(BC) = (AB)C$

2. $A(B+C) = BA+CA$

3. $A(B+C) = AB+AC$

#### Explanation

Let's consider the statements one by one.

- Statement I is true. Matrix multiplication is associative, so $(AB)C = A(BC)$ in general.

- Statement II is false. Matrix multiplication is distributive, so $A(B+C) = AB + AC$ in general. However, since matrix multiplication is not commutative, we have

- Statement III is true. Matrix multiplication is distributive, so $(A+B)C = AC+BC,$ and $A(B+C) = AB+AC$ in general.

Therefore, only statements I and III are true.
