# QR Factorization

Source: https://www.mathacademy.com/topics/2129?courseId=155
Topic ID: 2129

## Prerequisites

- [The Gram-Schmidt Process in the General Case](./2128-the-gram-schmidt-process-in-the-general-case.md)
- [Orthogonal Linear Transformations](./4319-orthogonal-linear-transformations.md)

## Lesson

### Introduction

The **QR factorization** of an $m\times n$ matrix $A$ with linearly independent columns is the matrix product

$$


\underset{{\large m} \times {\large n}}{A} = \underset{{\large m} \times {\large n}}{Q} \times \underset{{\large n} \times {\large n}}{R},


$$

where

- $Q$ is an $m \times n$ matrix whose columns form an orthonormal basis of $\text{Col}(A),$ and

- $R$ is an $n \times n$ upper triangular matrix with positive entries on its diagonal.

For example, the $3\times 2$ matrix

$$


\begin{aligned}2 & −3 \\ −4 & 3 \\ 4 & 0\end{aligned}


$$

has the QR factorization

$$


\begin{aligned}2 & −3 \\ −4 & 3 \\ 4 & 0\end{aligned}


$$

### Example: Identifying Dimensions of Factors in a QR Factorization

#### Question

Given that $A=QR$ is a QR factorization of a $3 \times 2$ matrix $A$ with linearly independent columns, which of the following statements are true?

1. $Q$ is a $3 \times 3$ matrix

2. The columns of $Q$ form an orthonormal basis of $\text{Col}(A)$

3. $R$ is an upper triangular matrix

#### Explanation

Recall that if $A=QR$ is a QR factorization of an $m \times n$ matrix $A,$ then

$$


\underset{{\large m} \times {\large n}}{A} = \underset{{\large m} \times {\large n}}{Q} \times \underset{{\large n} \times {\large n}}{R},


$$

where

- $Q$ is an $m \times n$ matrix whose columns form an orthonormal basis of $\text{Col}(A)$

- $R$ is an $n \times n$ upper triangular matrix

With that in mind, let's examine our statements.

- Statement I is false. $Q$ should be a $3\times 2$ matrix.

- Statement II is true. Indeed, the columns of $Q$ form an orthonormal basis of $\text{Col}(A).$

- Statement III is true. Indeed, $R$ must be a $2 \times 2$ upper triangular matrix.

Therefore, the correct answer is "II and III only."

### Computing the Matrix R Given the Matrix Q in a QR Factorization

Given the matrix $Q$ in the QR factorization of an $m\times n$ matrix $A,$ how do we find $R?$

Recall that $Q$ has orthonormal columns, so pre-multiplying both sides of $A=QR$ by $Q^T,$ we obtain

$$


\begin{aligned}𝑄^{𝑇}⋅𝐴 & =𝑄^{𝑇}⋅𝑄𝑅 \\ 𝑄^{𝑇}𝐴 & =𝑄^{𝑇}𝑄𝑅.\end{aligned}


$$

Now, note that since the columns of $Q$ are orthonormal we have $Q^TQ = I_n.$ Therefore,

$$


\begin{aligned}𝑄^{𝑇}𝐴 & =(𝑄^{𝑇}𝑄)𝑅 \\ 𝑄^{𝑇}𝐴 & =𝐼_{𝑛}𝑅 \\ 𝑅 & =𝑄^{𝑇}𝐴.\end{aligned}


$$

So, we can find $R$ by pre-multiplying $A$ by the transpose of $Q.$

### Example: Finding the Triangular Factor of a QR Factorization Given the Orthogonal Factor

#### Question

$$


\begin{aligned}0 & 1 \\ 1 & 0 \\ −1 & 2\end{aligned}


$$

Consider the matrices $A$ and $Q$ shown above. Find the matrix $R$ such that $A=QR$ is a QR factorization of $A.$

#### Explanation

Since $Q$ has orthonormal columns, pre-multiplying both sides of $A=QR$ by $Q^T,$ we obtain

$$


\begin{aligned}𝑄^{𝑇}⋅𝐴 & =𝑄^{𝑇}⋅𝑄𝑅 \\ 𝑄^{𝑇}\,𝐴 & =(𝑄^{𝑇}\,𝑄)𝑅 \\ 𝑄^{𝑇}\,𝐴 & =𝐼_{2}𝑅 \\ 𝑅 & =𝑄^{𝑇}\,𝐴\end{aligned}


$$

Note that $Q^TQ = I_2$ since the columns of $Q$ are orthonormal.

Now, we calculate the matrix $R\mathbin{:}$

$$


\begin{aligned}𝑅 & =𝑄^{𝑇}𝐴 \\ & =\begin{matrix}0 & \frac{1}{\sqrt{2}} & −\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}}\end{matrix}\begin{matrix}0 & 1 \\ 1 & 0 \\ −1 & 2\end{matrix} \\ & =[\begin{matrix}\sqrt{2} & −\sqrt{2} \\ 0 & \sqrt{3}\end{matrix}].\end{aligned}


$$

### Interpreting Relations Between Two Bases as Matrix Multiplication

Let's consider the QR factorization of the matrix $A$ shown below:

$$


\begin{aligned}| & | & | \\ 𝐚_{1} & 𝐚_{2} & 𝐚_{3} \\ | & | & |\end{aligned}


$$

Suppose also that we are given the following system of equations that connects the columns of $Q$ and the columns of $A{:}$

$$


\begin{aligned}𝐪_{1}=\frac{1}{2}𝐚_{1} \\ 𝐪_{2}=\frac{1}{3}𝐚_{2}+3𝐪_{1} \\ 𝐪_{3}=\frac{1}{4}𝐚_{3}−2𝐪_{1}+𝐪_{2}\end{aligned}


$$

How do we find $R?$ First, let's rewrite the vectors $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ as a linear combination of the vectors $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3 \mathbin{:}$

$$


\begin{aligned}𝐪_{1}=\frac{1}{2}𝐚_{1} \\ 𝐪_{2}=\frac{1}{3}𝐚_{2}+3𝐪_{1} \\ 𝐪_{3}=\frac{1}{4}𝐚_{3}−2𝐪_{1}+𝐪_{2}\end{aligned}


$$

In this new system, the coefficients of $\mathbf{q}_1$ correspond to the first-row entries of $R,$ the coefficients of $\mathbf{q}_2$ correspond to the second-row entries of $R,$ and the coefficients of $\mathbf{q}_3$ correspond to the third-row entries of $R.$ Therefore,

$$


\begin{aligned}| & | & | \\ 𝐚_{1} & 𝐚_{2} & 𝐚_{3} \\ | & | & |\end{aligned}


$$

To see why this is, we can take the transpose of both sides of $A=QR{:}$

$$


\begin{aligned}𝐴 & =𝑄𝑅 \\ 𝐴^{𝑇} & =(𝑄𝑅)^{𝑇} \\ 𝐴^{𝑇} & =𝑅^{𝑇}𝑄^{𝑇} \\ \overset{\begin{matrix}−\,\,\,\, & 𝐚_{1} & \,\,\,\,− \\ −\,\,\,\, & 𝐚_{2} & \,\,\,\,− \\ −\,\,\,\, & 𝐚_{3} & \,\,\,\,−\end{matrix}}{𝐴^{𝑇}} & =\overset{\begin{matrix}2 & 0 & 0 \\ −9 & 3 & 0 \\ 8 & −4 & 4\end{matrix}}{𝑅^{𝑇}}\overset{\begin{matrix}−\,\,\,\, & 𝐪_{1} & \,\,\,\,− \\ −\,\,\,\, & 𝐪_{2} & \,\,\,\,− \\ −\,\,\,\, & 𝐪_{3} & \,\,\,\,−\end{matrix}}{𝑄^{𝑇}}\end{aligned}


$$

If we were to expand this matrix product, we would obtain our system of equations.

### Example: Finding a QR Factorization of a Matrix Given an Orthogonal Basis in Terms of the Columns of a Matrix

#### Question

$$


\begin{aligned}| & | & | \\ 𝐚_{1} & 𝐚_{2} & 𝐚_{3} \\ | & | & |\end{aligned}


$$

Consider the QR factorization of the matrix $A$ shown above, where $\big\{\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3 \big\}$ is an orthogonal set of vectors. You're given that $\Vert\mathbf{v}_1\Vert =2,$ $\Vert\mathbf{v}_2\Vert =3,$ $\Vert\mathbf{v}_3\Vert =4,$ and that the system of equations below describes the relationship between the columns of $Q$ and the columns of $A.$

$$


\begin{aligned}𝐯_{1}=𝐚_{1} \\ 𝐯_{2}=𝐚_{2}−𝐯_{1} \\ 𝐯_{3}=𝐚_{3}−3𝐯_{1}+2𝐯_{2}.\end{aligned}


$$

What is the value of $r_{13}+r_{23}+r_{33}?$

#### Explanation

First, we normalize the vectors $\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3 \mathbin{:}$

$$


\begin{aligned}𝐪_{1} & =\frac{𝐯_{1}}{‖𝐯_{1}‖}=\frac{𝐯_{1}}{2}\,⟹\,𝐯_{1}=2𝐪_{1} \\ 𝐪_{2} & =\frac{𝐯_{2}}{‖𝐯_{2}‖}=\frac{𝐯_{2}}{3}\,⟹\,𝐯_{2}=3𝐪_{2} \\ 𝐪_{3} & =\frac{𝐯_{3}}{‖𝐯_{3}‖}=\frac{𝐯_{3}}{4}\,⟹\,𝐯_{3}=4𝐪_{3}.\end{aligned}


$$

Now, the set $\big\{\mathbf{q}_1,\mathbf{q}_2,\mathbf{q}_3 \big\}$ will be both orthogonal and normalized.

Next, let's rewrite the vectors $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ as a linear combination of the vectors $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3 \mathbin{:}$

$$


\begin{aligned}𝐯_{1}=𝐚_{1} \\ 𝐯_{2}=𝐚_{2}−𝐯_{1} \\ 𝐯_{3}=𝐚_{3}−3𝐯_{1}+2𝐯_{2}\end{aligned}


$$

The final system can be written in matrix form as follows:

$$


\begin{aligned}| & | & | \\ 𝐚_{1} & 𝐚_{2} & 𝐚_{3} \\ | & | & |\end{aligned}


$$

Therefore,

$$


r_{13}+r_{23}+r_{33} = 6+(-6)+4 = 4.


$$

### The QR Factorization Algorithm

Let's now go through the QR factorization algorithm to find the factorization of the matrix

$$


\begin{aligned}2 & 1 \\ 4 & 3 \\ −4 & −1\end{aligned}


$$

**Step 1**. Orthogonalize the columns of $A$ to get the columns of $Q.$ Using the Gram-Schmidt process, we obtain

$$


\begin{aligned}𝐪_{1}=\frac{1}{3}\begin{matrix}1 \\ 2 \\ −2\end{matrix},\,𝐪_{2}=\frac{1}{\sqrt{2}}\begin{matrix}0 \\ 1 \\ 1\end{matrix}.\end{aligned}


$$

**Step 2**. Compute $R=Q^TA.$ We get

$$


\begin{aligned}𝑅=[\begin{matrix}6 & 3 \\ 0 & \sqrt{2}\end{matrix}].\end{aligned}


$$

Therefore, the QR factorization of $A$ is

$$


\begin{aligned}2 & 1 \\ 4 & 3 \\ −4 & −1\end{aligned}


$$

### Example: Finding a QR Factorization of a Matrix Given a Matrix With Orthogonal Columns

#### Question

$$


\begin{aligned}1 & −2 \\ 0 & 1 \\ 1 & 2\end{aligned}


$$

Consider the QR factorization of the matrix $A$ shown above. Given that the columns $\mathbf{a}_1,\mathbf{a}_2$ of $A$ are orthogonal, and that the columns $\mathbf{q}_1,\mathbf{q}_2$ of $Q$ were obtained by normalizing the columns of $A,$ what is the value of $q_{12} \cdot r_{22}?$

#### Explanation

Since the columns of $A$ are already orthogonal, to construct a matrix $Q,$ we simply normalize $\mathbf{a}_1$ and $\mathbf{a}_2\mathbf{:}$

$$


\begin{aligned}𝐪_{1} & =\frac{𝐚_{1}}{‖𝐚_{1}‖}=\frac{1}{\sqrt{2}}\begin{matrix}1 \\ 0 \\ 1\end{matrix} \\ 𝐪_{2} & =\frac{𝐚_{2}}{‖𝐚_{2}‖}=\frac{1}{3}\begin{matrix}−2 \\ 1 \\ 2\end{matrix}\end{aligned}


$$

Now, pre-multiplying both sides of $A=QR$ by $Q^T,$ we obtain

$$


\begin{aligned}𝑅 & =𝑄^{𝑇}\,𝐴 \\ & =\begin{matrix}\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{2}} \\ −\frac{2}{3} & \frac{1}{3} & \frac{2}{3}\end{matrix}\begin{matrix}1 & −2 \\ 0 & 1 \\ 1 & 2\end{matrix} \\ & =[\begin{matrix}\sqrt{2} & 0 \\ 0 & 3\end{matrix}].\end{aligned}


$$

Therefore, we have the following QR factorization of $A\mathbin{:}$

$$


\begin{aligned}1 & −2 \\ 0 & 1 \\ 1 & 2\end{aligned}


$$

Finally, $q_{12} \cdot r_{22} = -\dfrac{2}{3} \cdot 3 = -2.$

### Example: Finding the QR Factorization of a Matrix

#### Question

$$


\begin{aligned}1 & 3 \\ 2 & 3 \\ 1 & 3\end{aligned}


$$

Consider the QR factorization of the matrix $A$ shown above. Given that the columns $\mathbf{q}_1,\mathbf{q}_2$ of $Q$ were obtained from the columns of $A$ using the Gram-Schmidt process, find the value of $q_{11} \cdot r_{12}.$

#### Explanation

Let $\mathbf{a}_1,\mathbf{a}_2$ be the columns of $A.$

First, we find an orthonormal basis of $\text{Col}(A)=\text{Span}\{\mathbf{a}_1,\mathbf{a}_2\}$ using the Gram-Schmidt process.

****. We set $\begin{aligned}1 \\ 2 \\ 1\end{aligned}$

****. We find the vector $\mathbf{v}_2$ orthogonal to $\text{Span}\{\mathbf{v}_1\}$ using the formula

$$


\begin{aligned}𝐯_{2} & =𝐚_{2}−proj_{𝐯_{1}}𝐚_{2} \\ & =𝐚_{2}−\frac{𝐚_{2}⋅𝐯_{1}}{𝐯_{1}⋅𝐯_{1}}𝐯_{1} \\ & =\begin{matrix}3 \\ 3 \\ 3\end{matrix}−\frac{12}{6}\begin{matrix}1 \\ 2 \\ 1\end{matrix} \\ & =\begin{matrix}3 \\ 3 \\ 3\end{matrix}−2\begin{matrix}1 \\ 2 \\ 1\end{matrix} \\ & =\begin{matrix}1 \\ −1 \\ 1\end{matrix}.\end{aligned}


$$

Next, we normalize $\mathbf{v}_1$ and $\mathbf{v}_2\mathbin{:}$

$$


\begin{aligned}𝐪_{1} & =\frac{𝐯_{1}}{‖𝐯_{1}‖}=\frac{1}{\sqrt{6}}\begin{matrix}1 \\ 2 \\ 1\end{matrix} \\ 𝐪_{2} & =\frac{𝐯_{2}}{‖𝐯_{2}‖}=\frac{1}{\sqrt{3}}\begin{matrix}1 \\ −1 \\ 1\end{matrix}\end{aligned}


$$

Next, we compute $R\mathbin{:}$

$$


\begin{aligned}𝑅 & =𝑄^{𝑇}\,𝐴 \\ & =\begin{matrix}\frac{1}{\sqrt{6}} & \frac{2}{\sqrt{6}} & \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{3}} & −\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{3}}\end{matrix}\begin{matrix}1 & 3 \\ 2 & 3 \\ 1 & 3\end{matrix} \\ & =[\begin{matrix}\sqrt{6} & 2\sqrt{6} \\ 0 & \sqrt{3}\end{matrix}].\end{aligned}


$$

Therefore, we obtain the following QR factorization of $A\mathbin{:}$

$$


\begin{aligned}1 & 3 \\ 2 & 3 \\ 1 & 3\end{aligned}


$$

Finally, $q_{11} \cdot r_{12} = \left(\dfrac{1}{\sqrt{6}}\right) \cdot \left({2\sqrt6}\right) = 2.$
