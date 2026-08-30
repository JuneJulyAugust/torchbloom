# The Column Space of a Matrix

Source: https://www.mathacademy.com/topics/1850?courseId=154
Topic ID: 1850

## Prerequisites

- [Representing 3x3 Systems of Equations Using a Matrix Product](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/155-representing-3x3-systems-of-equations-using-a-matrix-product.md)
- [Linear Span of Vectors in N-Dimensional Euclidean Space](./1852-linear-span-of-vectors-in-n-dimensional-euclidean-space.md)
- [Subspaces of N-Dimensional Space: Geometric Interpretation](./4077-subspaces-of-n-dimensional-space-geometric-interpretation.md)

## Lesson

### Introduction

The **column space** of a matrix $A$ is denoted $\text{Col}(A)$ and is the span of the columns of $A$ (i.e., the set of all possible linear combinations of columns of $A$). For example, consider the matrix

$$


[\begin{aligned}1 & 3 \\ 2 & −1\end{aligned}]


$$

where we denote its columns by $\color{red}\mathbf{a}_1$ and ${\color{blue}\mathbf{a}_2},$ respectively. The column space of this matrix is given by

$$


[\begin{aligned}1 \\ 2\end{aligned}]


$$

Now, suppose we would like to determine whether the vector $[\begin{aligned}2 \\ −3\end{aligned}]$ lies in $\textrm{Col}(A).$ In other words, we need to check if $\mathbf{b} \in \textrm{Span}\{{\color{red}\mathbf{a}_1}, {\color{blue}\mathbf{a}_2} \}.$ So, we need to determine whether $\mathbf{b}$ can be written as some linear combination of $\color{red}\mathbf{a}_1$ and ${\color{blue}\mathbf{a}_2}\mathbin{:}$

$$


\begin{aligned}𝑥_{1}𝐚_{1}+𝑥_{2}𝐚_{2}=𝐛\end{aligned}


$$

Notice that the equation above can be written as follows:

$$


\begin{aligned}[\begin{aligned}𝐚_{1} & 𝐚_{2}\end{aligned}][\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =𝐛 \\ \underset{𝐴}{\underset{}{[\begin{aligned}1 & 3 \\ 2 & −1\end{aligned}]}}\underset{𝐱}{\underset{}{[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]}} & =\underset{𝐛}{\underset{}{[\begin{aligned}2 \\ −3\end{aligned}]}}\end{aligned}


$$

So, the equation is equivalent to $A\mathbf{x}=\mathbf{b}.$ To solve the equation, let's find the row echelon form of the augmented matrix $[A \,|\, \mathbf{b}]$ as follows:

$$


\begin{aligned}[𝐴\,|\,𝐛] & =[\begin{aligned}1 & 3 & 2 \\ 2 & −1 & −3\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+(−2)𝑅_{1} \\ & ∼[\begin{aligned}1 & 3 & 2 \\ 0 & −7 & −7\end{aligned}] & & \end{aligned}


$$

Now, we have the system

$$


\begin{aligned}𝑥_{1}+3𝑥_{2}=2 \\ −7𝑥_{2}=−7.\end{aligned}


$$

From the second equation, we get $x_2=1.$ Substituting into the first equation, we get $x_1=-1.$

Since we have a solution, the equation $A\mathbf{x}=\mathbf{b}$ is consistent, which implies that $\mathbf{b} \in \textrm{Col}(A).$

Moreover, there is exactly one solution, so we have exactly one way to write $\mathbf{b}$ as a linear combination of $\color{red}\mathbf{a}_1$ and ${\color{blue}\mathbf{a}_2}\mathbin{:}$

$$


[\begin{aligned}2 \\ −3\end{aligned}]


$$

### Example: Determining if a Vector is in the Column Space of a Matrix

#### Question

The matrix $B$ and the vector $\mathbf{b}$ are given below. Determine if $\mathbf{b} \in \textrm{Col}(B).$ In the affirmative case, find the values of $x_1$ and $x_2,$ where $x_1$ and $x_2$ are the real numbers such that $\mathbf{b}=x_1\mathbf{b}_1+x_2\mathbf{b}_2,$ and $\mathbf{b}_1,$ $\mathbf{b}_2$ are the respective columns of $B.$

$$


\begin{aligned}5 & −2 \\ 15 & −6 \\ 0 & 1\end{aligned}


$$

#### Explanation

In order to determine whether $\mathbf{b}$ lies in $\textrm{Col}(B),$ we need to check if the equation $B\mathbf{x}=\mathbf{b}$ is consistent. So, let's find the row echelon form of the augmented matrix $[B \,|\, \mathbf{b}]$ as follows:

$$


\begin{aligned}[𝐵\,|\,𝐛] & =\begin{aligned}5 & −2 & 7 \\ 15 & −6 & 21 \\ 0 & 1 & 0\end{aligned} & 𝑅_{2} & :=𝑅_{2}−3𝑅_{1} \\ & ∼\begin{aligned}5 & −2 & 7 \\ 0 & 0 & 0 \\ 0 & 1 & 0\end{aligned} & 𝑅_{2} & ↔𝑅_{3} \\ & ∼\begin{aligned}5 & −2 & 7 \\ 0 & 1 & 0 \\ 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

Now, we have the system

$$


\begin{aligned}5𝑥_{1}−2𝑥_{2}=7 \\ 𝑥_{2}=0 \\ 0=0.\end{aligned}


$$

From the third equation, we get the true statement $0=0.$ So the system is equivalent to the following:

$$


\begin{aligned}5𝑥_{1}−2𝑥_{2}=7 \\ 𝑥_{2}=0\end{aligned}


$$

From the second equation, we get $x_2=0.$ Substituting into the first equation gives $x_1=\dfrac 7 5.$

Since we have a solution, the equation $B\mathbf{x}=\mathbf{b}$ is consistent, which implies that $\mathbf{b}\in\textrm{Col}(B).$

Moreover, there is exactly one solution, so we have exactly one way to write $\mathbf{b}$ as a linear combination of $\mathbf{b}_1$ and $\mathbf{b}_2\mathbin{:}$

$$


\begin{aligned}7 \\ 21 \\ 0\end{aligned}


$$

### Example: Determining the Value of an Unknown Given a Vector That’s in the Column Space of a Matrix

#### Question

Consider the matrix given by $\begin{aligned}1 & 2 \\ 3 & −2 \\ 5 & −1\end{aligned}$ Determine the value of $k$ for which the vector $\begin{aligned}10 \\ −2 \\ 2+𝑘\end{aligned}$ belongs to $\textrm{Col}(A).$

#### Explanation

If $\mathbf{b}$ lies in $\textrm{Col}(A),$ then the equation $A\mathbf{x}=\mathbf{b}$ must be consistent. So, let's find the row echelon form of the augmented matrix $[A \,|\, \mathbf{b}]$ as follows:

$$


\begin{aligned}[𝐴\,|\,𝐛] & =\begin{aligned}1 & 2 & 10 \\ 3 & −2 & −2 \\ 5 & −1 & 2+𝑘\end{aligned} & 𝑅_{2} & :=𝑅_{2}−3𝑅_{1} \\ & ∼\begin{aligned}1 & 2 & 10 \\ 0 & −8 & −32 \\ 5 & −1 & 2+𝑘\end{aligned} & 𝑅_{3} & :=𝑅_{3}−5𝑅_{1} \\ & ∼\begin{aligned}1 & 2 & 10 \\ 0 & −8 & −32 \\ 0 & −11 & 𝑘−48\end{aligned} & 𝑅_{2} & :=\frac{1}{8}𝑅_{2} \\ & ∼\begin{aligned}1 & 2 & 10 \\ 0 & 1 & 4 \\ 0 & −11 & 𝑘−48\end{aligned} & 𝑅_{3} & :=𝑅_{3}+11𝑅_{2} \\ & ∼\begin{aligned}1 & 2 & 10 \\ 0 & 1 & 4 \\ 0 & 0 & 𝑘−4\end{aligned} & & \end{aligned}


$$

So, we have the system

$$


\begin{aligned}𝑥_{1}+2𝑥_{2}=10 \\ 𝑥_{2}=4 \\ 0=𝑘−4.\end{aligned}


$$

In order for this system to be consistent, we require $0=k-4,$ which means that $k=4.$

### Properties of the Column Space of a Matrix

The column space is defined for matrices of *any* dimensions. In general, if ${\color{black}\mathbf{a}_1}, {\color{black}\mathbf{a}_2}, \ldots, {\color{black}\mathbf{a}_n}$ are the columns of a matrix $A,$ that is to say,

$$


\begin{aligned}| & | & & | \\ 𝐚_{1} & 𝐚_{2} & … & 𝐚_{𝑛} \\ | & | & & |\end{aligned}


$$

then $\textrm{Col}(A) = \textrm{Span} \{{\color{black}\mathbf{a}_1}, {\color{black}\mathbf{a}_2}, \ldots, {\color{black}\mathbf{a}_n} \}.$

The column space satisfies the following properties:

- If $A$ is an ${\color{blue}m}\times n$ matrix, then $\textrm{Col}(A)$ is a subspace of $\mathbb{R}^{\color{blue}m}.$ This is because each column has ${\color{blue}m}$ entries.

- $\mathbf{b}\in\textrm{Col}(A)$ if and only if the equation $A\mathbf{x}=\mathbf{b}$ is consistent (has a solution).

- If the equation $A\mathbf{x}=\mathbf{b}$ is inconsistent (has no solution), then $\mathbf{b}\not\in\textrm{Col}(A).$

These hold for any $m\times n$ matrix, and the matrix does not necessarily have to be square.

### Example: Determining if a Vector Is in the Column Space of a Larger Matrix

#### Question

The matrix $C$ and the vector $\mathbf{b}$ are given below. Determine if $\mathbf{b} \in \textrm{Col}(C).$ In affirmative case, find the value of $x_1 \cdot x_2 \cdot x_3$, where $x_1$, $x_2$, and $x_3$ are real numbers such that $\mathbf{b}=x_1\mathbf{c}_1+x_2\mathbf{c}_3+x_3\mathbf{c}_3,$ and $\mathbf{c}_1,$ $\mathbf{c}_2,$ and $\mathbf{c}_3$ are the respective columns of $C.$

$$


\begin{aligned}1 & 1 & 4 \\ −1 & 2 & 0 \\ 0 & −3 & 1\end{aligned}


$$

#### Explanation

In order to determine whether $\mathbf{b}$ lies in $\textrm{Col}(C),$ we need to check if the equation $C\mathbf{x}=\mathbf{b}$ is consistent. So, let's find the row echelon form of the augmented matrix $[C \,|\, \mathbf{b}]$ as follows:

$$


\begin{aligned}[𝐶\,|\,𝐛] & =\begin{aligned}1 & 1 & 4 & 5 \\ −1 & 2 & 0 & −4 \\ 0 & −3 & 1 & 4\end{aligned} & 𝑅_{2} & :=𝑅_{2}+𝑅_{1} \\ & ∼\begin{aligned}1 & 1 & 4 & 5 \\ 0 & 3 & 4 & 1 \\ 0 & −3 & 1 & 4\end{aligned} & 𝑅_{3} & :=𝑅_{3}+𝑅_{2} \\ & ∼\begin{aligned}1 & 1 & 4 & 5 \\ 0 & 3 & 4 & 1 \\ 0 & 0 & 5 & 5\end{aligned} & & \end{aligned}


$$

Now, we have the system

$$


\begin{aligned}𝑥_{1}+𝑥_{2}+4𝑥_{3}=5 \\ 3𝑥_{2}+4𝑥_{3}=1 \\ 5𝑥_{3}=5.\end{aligned}


$$

From the third equation, we get $x_3=1$. Substituting into the second equation gives

$$


\begin{aligned}3𝑥_{2}+4(1) & =1 \\ 3𝑥_{2} & =−3 \\ 𝑥_{2} & =−1.\end{aligned}


$$

Finally, from the first equation, we get

$$


\begin{aligned}𝑥_{1} & =5−𝑥_{2}−4𝑥_{3} \\ & =5−(−1)−4(1) \\ & =2.\end{aligned}


$$

Since we have a solution, the equation $C\mathbf{x}=\mathbf{b}$ is consistent, which implies that $\mathbf{b}\in\textrm{Col}(C).$

Moreover, there is exactly one solution, so we have exactly one way to write $\mathbf{b}$ as a linear combination of $\mathbf{c}_1,$ $\mathbf{c}_2,$ and $\mathbf{c}_3\mathbin{:}$

$$


\begin{aligned}5 \\ −4 \\ 4\end{aligned}


$$

Finally, we get $x_1 \cdot x_2 \cdot x_3 = 2 \cdot (-1) \cdot 1 = -2$.
