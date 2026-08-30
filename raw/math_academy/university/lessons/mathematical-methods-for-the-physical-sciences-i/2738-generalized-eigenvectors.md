# Generalized Eigenvectors

Source: https://www.mathacademy.com/topics/2738?courseId=154
Topic ID: 2738

## Prerequisites

- [Calculating the Eigenvectors of a 3x3 Matrix in the General Case](./1965-calculating-the-eigenvectors-of-a-3x3-matrix-in-the-general-case.md)
- [Nilpotent and Idempotent Matrices](./3776-nilpotent-and-idempotent-matrices.md)

## Lesson

### Introduction

Let $A$ be an $m \times m$ matrix. Recall that a nonzero vector $\mathbf{v}_1$ is an eigenvector of $A$ corresponding to the eigenvalue $\lambda$ if

$$


A\mathbf{v}_1 = \lambda \mathbf{v}_1.


$$

We can write this equation as

$$


(A - \lambda I) \mathbf{v}_1 = \mathbf{0}.


$$

Therefore, the matrix $A-\lambda I$ maps the vector $\mathbf{v}_1$ to the zero vector $\mathbf{0}{:}$

$$


\mathbf{v}_1 \xrightarrow{A- \lambda I} \mathbf{0}


$$

Now suppose that there exists a nonzero vector $\mathbf v_2$ that is mapped to the zero vector in *two* steps by the matrix $A-\lambda I.$ That is,

$$


(A-\lambda I)\mathbf v_2 = \mathbf v_1 \qquad \text{and}\qquad (A-\lambda I)\mathbf v_1 = \mathbf 0,


$$

where $\mathbf v_1$ is an eigenvector of $A$ corresponding to the eigenvalue $\lambda.$

We can represent this schematically as a chain of mappings, as follows:

$$


\mathbf{v}_2 \xrightarrow{A- \lambda I} \mathbf{v}_{1} \xrightarrow{A- \lambda I} \mathbf{0}


$$

We call $\mathbf v_2$ a **generalized eigenvector of rank** $2$ because it is mapped to the zero vector in two steps.

By the same idea, an eigenvector of $A$ is a generalized eigenvector of rank $1$ because it is mapped to the zero vector in one step.

### An Example of a Generalized Eigenvector of Rank Two for a 2x2 Matrix

Consider the matrix $A$ and the vector $\mathbf v,$ given by

$$


[\begin{aligned}1 & 4 \\ −1 & 5\end{aligned}]


$$

The matrix $A$ has only one eigenvalue, namely $\lambda = 3.$ Let's show that $\mathbf v$ is a generalized eigenvector of rank $2$ corresponding to this eigenvalue.

- First, we compute $A-3I{:}$

- Next, we find the image of $\mathbf{v}$ under the action of $A-3I{:}$

- Since we got a nonzero vector in the last step, we now compute the image of $\mathbf{w}$ under the action of $A-3I{:}$

So, we obtain the following chain of maps:

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

As we can see, $A-3I$ maps $\mathbf{v}$ to $\mathbf{0}$ in $2$ steps.

Therefore, we conclude that $\mathbf{v}$ is a generalized eigenvector of rank $2$ corresponding to the eigenvalue $\lambda=3$ of $A.$

### Example: Identifying Generalized Eigenvectors of a 2x2 Matrix

#### Question

$$


[\begin{aligned}6 & −1 \\ 4 & 2\end{aligned}]


$$

Consider the matrix $A$ and vector $\mathbf v$ shown above. Which of the following statements are true?

1. $\mathbf{v}$ is an eigenvector corresponding to the eigenvalue $\lambda=4$ of $A$

2. $\mathbf{v}$ is a generalized eigenvector of rank $2$ corresponding to the eigenvalue $\lambda=4$ of $A$

3. $\mathbf{v}$ is a generalized eigenvector of rank $1$ corresponding to the eigenvalue $\lambda=4$ of $A$

#### Explanation

A ** $\mathbf{v_2}$ of rank $2$ corresponding to the eigenvalue $\lambda$ of a matrix $A$ is a nonzero vector such that

$$


\mathbf{v}_2 \xrightarrow{A- \lambda I} \mathbf{v}_1 \xrightarrow{A- \lambda I} \mathbf{0},


$$

where $\mathbf{v}_1 \neq \mathbf{0}.$ Recall that an ** is simply a generalized eigenvector of rank $1.$

With this in mind, let's examine our statements.

First, we compute $A-4I{:}$

$$


[\begin{aligned}6 & −1 \\ 4 & 2\end{aligned}]


$$

- Next, we find the image of $\mathbf{v}$ under the action of $A-4I{:}$

- Since we got a nonzero vector in the last step, we now compute the image of $\mathbf{w}$ under the action of $A-4I{:}$

So, we obtain the following chain of maps:

$$


[\begin{aligned}2 \\ 3\end{aligned}]


$$

Here, we see that $A-4I$ maps $\mathbf{v}$ to $\mathbf{0}$ in $2$ steps.

Therefore:

$\qquad$ **

So, the correct answer is "II only."

### Generalized Eigenvectors of Rank N

Let $A$ be an $m \times m$ matrix. A **generalized eigenvector of rank $n$** corresponding to the eigenvalue $\lambda$ of $A$ is a nonzero vector $\mathbf{v}_n$ such that

$$


\mathbf{v}_n \xrightarrow{A- \lambda I} \mathbf{v}_{n-1} \xrightarrow{A- \lambda I} \ldots \xrightarrow{A- \lambda I} \mathbf{v}_1 \xrightarrow{A- \lambda I} \mathbf{0},


$$

where $\mathbf{v}_{n-1}, \mathbf{v}_{n-2},\ldots, \mathbf{v}_{1} \neq \mathbf{0}.$ In other words, $A-\lambda I$ maps $\mathbf{v}$ to $\mathbf{0}$ in $n$ steps.

### Example: Identifying Generalized Eigenvectors Using Definition

#### Question

$$


\begin{aligned}𝐮\overset{}{𝐴+3𝐼\,}𝐯\overset{}{𝐴+3𝐼\,}𝐰\overset{}{𝐴+3𝐼\,}𝟎 \\ 𝐱\overset{}{𝐴−5𝐼\,}𝐲\overset{}{𝐴−5𝐼\,}𝟎\end{aligned}


$$

Given the action of the matrices $A+3I$ and $A-5I$ on the nonzero vectors $\mathbf{u},\mathbf{v},\mathbf{w},\mathbf{x}$ and $\mathbf y$ as depicted above, which of the following statements are true?

1. $\mathbf{v}$ is an eigenvector corresponding to the eigenvalue $\lambda=-3$ of $A$

2. $\mathbf{u}$ is a generalized eigenvector of rank $3$ corresponding to the eigenvalue $\lambda=-3$ of $A$

3. $\mathbf{y}$ is a generalized eigenvector of rank $2$ corresponding to the eigenvalue $\lambda=5$ of $A$

#### Explanation

A ** $\mathbf{v}_n$ of rank $n$ corresponding to the eigenvalue $\lambda$ of a matrix $A$ is a nonzero vector such that

$$


\mathbf{v}_n \xrightarrow{A- \lambda I} \mathbf{v}_{n-1} \xrightarrow{A- \lambda I} \ldots \xrightarrow{A- \lambda I} \mathbf{v}_1 \xrightarrow{A- \lambda I} \mathbf{0},


$$

where $\mathbf{v}_{n-1}, \mathbf{v}_{n-2},\ldots, \mathbf{v}_{1} \neq \mathbf{0}.$ An ** is simply a generalized eigenvector of rank $1.$

With that in mind, let's examine our statements in turn.

- Statement I is false. Since i.e. $A+3I$ maps $\mathbf{v}$ to $\mathbf{0}$ in $\color{red}2$ steps, the vector $\mathbf{v}$ is a generalized eigenvector of rank ${\color{red}2},$ not $1.$

- Statement II is true. Indeed, since i.e. $A+{\color{blue}3}I$ maps $\mathbf{u}$ to $\mathbf{0}$ in $\color{red}3$ steps, the vector $\mathbf{u}$ is a generalized eigenvector of rank $\color{red}3$ corresponding to the eigenvalue $\lambda={\color{blue}-3}$ of $A.$

- Statement III is false. Since i.e. $A-{\color{black}5}I$ maps $\mathbf{y}$ to $\mathbf{0}$ in $\color{red}1$ step, the vector $\mathbf{y}$ is a generalized eigenvector of rank $\color{red}1,$ not $2.$

Therefore, the correct answer is "II only."

### Example: Identifying Generalized Eigenvectors of a 3x3 Matrix

#### Question

$$


\begin{aligned}−1 & 2 & 0 \\ −2 & 3 & 0 \\ 1 & 0 & 1\end{aligned}


$$

Consider the matrix $A$ and vector $\mathbf v$ shown above. Which of the following statements are true?

1. $\mathbf{v}$ is an eigenvector corresponding to the eigenvalue $\lambda=1$ of $A$

2. $\mathbf{v}$ is a generalized eigenvector of rank $2$ corresponding to the eigenvalue $\lambda=1$ of $A$

3. $\mathbf{v}$ is a generalized eigenvector of rank $3$ corresponding to the eigenvalue $\lambda=1$ of $A$

#### Explanation

A ** $\mathbf{v_n}$ of rank $n$ corresponding to the eigenvalue $\lambda$ of a matrix $A$ is a nonzero vector such that

$$


\mathbf{v}_n \xrightarrow{A- \lambda I} \mathbf{v}_{n-1} \xrightarrow{A- \lambda I} \ldots \xrightarrow{A- \lambda I} \mathbf{v}_1 \xrightarrow{A- \lambda I} \mathbf{0},


$$

where $\mathbf{v}_{n-1}, \mathbf{v}_{n-2},\ldots, \mathbf{v}_{1} \neq \mathbf{0}.$ An ** is simply a generalized eigenvector of rank $1.$

- First, we compute $A-I{:}$

$$


\begin{aligned}−1 & 2 & 0 \\ −2 & 3 & 0 \\ 1 & 0 & 1\end{aligned}


$$

- Next, we find the image of $\mathbf{v}$ under the action of $A-I{:}$

- Since we got a nonzero vector, we now compute the image of $\mathbf{w}$ under the action of $A-I{:}$

- Again, since we got a nonzero vector in the last step, we now compute the image of $\mathbf{x}$ under the action of $A-I{:}$

So, we obtain the following chain of maps:

$$


\begin{aligned}1 \\ 2 \\ 1\end{aligned}


$$

Here, we see that $A-I$ maps $\mathbf{v}$ to $\mathbf{0}$ in $3$ steps.

Therefore:

$\qquad$ **

So, the correct answer is "III only."
