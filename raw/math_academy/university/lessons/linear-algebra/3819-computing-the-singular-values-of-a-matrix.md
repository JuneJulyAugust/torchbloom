# Computing the Singular Values of a Matrix

Source: https://www.mathacademy.com/topics/3819?courseId=55
Topic ID: 3819

## Prerequisites

- [The Singular Values of a Matrix](./3131-the-singular-values-of-a-matrix.md)

## Lesson

### Introduction

Recall that the singular values of a real matrix $A$ are the square roots of the eigenvalues of the matrix $A^T \! A.$

Also, since $A^T \! A$ is a positive semi-definite matrix, the eigenvalues of $A^T \! A$ must be always non-negative real numbers.

Let's compute the singular values of the matrix $A,$ given by

$$


\begin{aligned}\,0 & \,2 \\ \,\,−2 & \,0 \\ 2 & 1\end{aligned}


$$

Now, since

- $A$ is a $3 \times 2$ matrix, and

- $A^T$ is a $2 \times 3$ matrix,

then $A^T \! A$ must be a $2 \times 2$ matrix:

$$


\underset{\boxed{\large 2} \times {\large 3}}{A^T} \times \underset{{\large 3} \times \boxed{\large 2}}{A} = \underset{\boxed{\large 2} \times \boxed{\large 2}}{A^T \! A}


$$

Let's now compute our singular values. First, we calculate $A^T \! A\mathbin{:}$

$$


\begin{aligned}𝐴^{𝑇}\,𝐴 & =\begin{matrix}\,0 & \,2 \\ \,\,−2 & \,0 \\ 2 & 1\end{matrix}^{𝑇}\begin{matrix}\,0 & \,2 \\ \,\,−2 & \,0 \\ 2 & 1\end{matrix} \\ & =[\begin{matrix}0 & −2 & 2 \\ 2 & 0 & 1\end{matrix}]\begin{matrix}\,0 & \,2 \\ \,\,−2 & \,0 \\ 2 & 1\end{matrix} \\ & =[\begin{matrix}8 & 2 \\ 2 & 5\end{matrix}]\end{aligned}


$$

Next, we compute the eigenvalues of $A^T \! A\mathbin{:}$

$$


\begin{aligned}|𝐴^{𝑇}\,𝐴−𝜆𝐼| & =0 \\ \begin{matrix}8−𝜆 & 2 \\ 2 & 5−𝜆\end{matrix} & =0 \\ (8−𝜆)(5−𝜆)−4 & =0 \\ 𝜆^{2}−13𝜆+36 & =0 \\ (𝜆−9)(𝜆−4) & =0 \\ 𝜆 & =9,\,4\end{aligned}


$$

Therefore, the singular values of $A$ are as follows:

$$


\begin{aligned}𝜎_{1} & =\sqrt{𝜆_{1}}=\sqrt{9}=3 \\ 𝜎_{2} & =\sqrt{𝜆_{2}}=\sqrt{4}=2\end{aligned}


$$

Note the following:

- When listing the singular values of a matrix, we usually write them in descending order.

- If $A$ is a $m\times n$ matrix, then $A^T A$ is a $n\times n$ positive semi-definite matrix. This means that $A$ has *at most* $n$ distinct singular values.

### Example: Identifying True Statements Regarding the Singular Values of a Matrix

#### Question

Which of the following statements are true?

1. Any $1\times4$ matrix $A$ has at most $1$ singular value.

2. Any $4\times2$ matrix $A$ has at most $2$ distinct singular values.

3. The matrix $[\begin{aligned}−1 & 0 \\ 0 & 1\end{aligned}]$ has one negative singular value.

#### Explanation

The singular values of the matrix $A$ are the square roots of the eigenvalues of the matrix $A^T \! A.$

With that in mind, let's examine our statements.

- Statement I is false. Since $A$ is a $1 \times 4$ matrix and $A^T$ is a $4\times 1$ matrix, $A^T \! A$ must be a $4 \times 4$ matrix: Hence, $A$ has at most $4$ distinct singular values.

- Statement II is true. Since $A$ is a $4 \times 2$ matrix and $A^T$ is a $2\times 4$ matrix, $A^T \! A$ must be a $2 \times 2$ matrix: Hence, $A$ has at most $2$ distinct singular values.

- Statement III is false. All singular values of any matrix are non-negative. So, $A$ cannot have a negative singular value.

Therefore, the correct answer is "II only."

### Example: Finding the Singular Values of a Square Matrix

#### Question

What are the singular values of the matrix $[\begin{aligned}1 & 2 \\ 2 & 1\end{aligned}]$

#### Explanation

The singular values of the matrix $A$ are the square roots of the eigenvalues of the matrix $A^T \! A.$

First, we calculate $A^T \! A\mathbin{:}$

$$


\begin{aligned}𝐴^{𝑇}\,𝐴 & =[\begin{matrix}1 & 2 \\ 2 & 1\end{matrix}]^{𝑇}[\begin{matrix}1 & 2 \\ 2 & 1\end{matrix}] \\ & =[\begin{matrix}1 & 2 \\ 2 & 1\end{matrix}][\begin{matrix}1 & 2 \\ 2 & 1\end{matrix}] \\ & =[\begin{matrix}5 & 4 \\ 4 & 5\end{matrix}]\end{aligned}


$$

Now, we solve the characteristic equation of $A^T \! A\mathbin{:}$

$$


\begin{aligned}|𝐴^{𝑇}\,𝐴−𝜆𝐼| & =0 \\ \begin{matrix}5−𝜆 & 4 \\ 4 & 5−𝜆\end{matrix} & =0 \\ (5−𝜆)^{2}−16 & =0 \\ 𝜆^{2}−10𝜆+9 & =0 \\ (𝜆−1)(𝜆−9) & =0 \\ 𝜆 & =9,\,1\end{aligned}


$$

Therefore, the singular values of $A$ are as follows:

$$


\begin{aligned}𝜎_{1} & =\sqrt{𝜆_{1}}=\sqrt{9}=3 \\ 𝜎_{2} & =\sqrt{𝜆_{2}}=\sqrt{1}=1\end{aligned}


$$

### Example: Finding the Singular Values of a Rectangular Matrix

#### Question

What are the singular values of the matrix $[\begin{aligned}1 & 0 & 1 \\ 0 & 1 & 0\end{aligned}]$

#### Explanation

The singular values of the matrix $A$ are the square roots of the eigenvalues of the matrix $A^T \! A.$

First, we calculate $A^T \! A\mathbin{:}$

$$


\begin{aligned}𝐴^{𝑇}\,𝐴 & =[\begin{matrix}1 & 0 & 1 \\ 0 & 1 & 0\end{matrix}]^{𝑇}[\begin{matrix}1 & 0 & 1 \\ 0 & 1 & 0\end{matrix}] \\ & =\begin{matrix}1 & 0 \\ 0 & 1 \\ 1 & 0\end{matrix}[\begin{matrix}1 & 0 & 1 \\ 0 & 1 & 0\end{matrix}] \\ & =\begin{matrix}1 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 1\end{matrix}\end{aligned}


$$

Now, we solve the characteristic equation of $A^T \! A\mathbin{:}$

$$


\begin{aligned}|𝐴^{𝑇}\,𝐴−𝜆𝐼| & =0 \\ \begin{matrix}1−𝜆 & 0 & 1 \\ 0 & 1−𝜆 & 0 \\ 1 & 0 & 1−𝜆\end{matrix} & =0 \\ (1−𝜆)\begin{matrix}1−𝜆 & 0 \\ 0 & 1−𝜆\end{matrix}+\begin{matrix}0 & 1−𝜆 \\ 1 & 0\end{matrix} & =0 \\ (1−𝜆)(1−𝜆)^{2}−(1−𝜆) & =0 \\ (1−𝜆)((1−𝜆)^{2}−1) & =0 \\ (1−𝜆)(𝜆^{2}−2𝜆) & =0 \\ −𝜆(𝜆−1)(𝜆−2) & =0 \\ 𝜆 & =2,\,1,\,0\end{aligned}


$$

Therefore, the singular values of $A$ are as follows:

$$


\begin{aligned}𝜎_{1} & =\sqrt{𝜆_{1}}=\sqrt{2} \\ 𝜎_{2} & =\sqrt{𝜆_{2}}=\sqrt{1}=1 \\ 𝜎_{3} & =\sqrt{𝜆_{3}}=\sqrt{0}=0\end{aligned}


$$
