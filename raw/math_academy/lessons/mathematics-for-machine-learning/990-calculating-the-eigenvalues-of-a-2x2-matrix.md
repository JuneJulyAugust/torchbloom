# Calculating the Eigenvalues of a 2x2 Matrix

Source: https://www.mathacademy.com/topics/990?courseId=145
Topic ID: 990

## Prerequisites

- [The Eigenvalues and Eigenvectors of a 2x2 Matrix](./1375-the-eigenvalues-and-eigenvectors-of-a-2x2-matrix.md)
- [The Invertible Matrix Theorem in Terms of Dimension, Rank and Nullity](./1869-the-invertible-matrix-theorem-in-terms-of-dimension-rank-and-nullity.md)

## Lesson

### Introduction

Consider the matrix $[\begin{aligned}2 & 5 \\ −1 & −4\end{aligned}]$ How can we find its eigenvalues?

By definition, we need to find the value(s) of $\,\lambda\,$ such that $\,A\mathbf{\color{blue}v} = \lambda \mathbf{\color{blue}v}\,$ is true for some *non-zero* vector $\mathbf{\color{blue}v}.$ Let's re-write this equation as follows:

$$


\begin{aligned}𝐴𝐯 & =𝜆𝐯 \\ 𝐴𝐯−𝜆𝐯 & =𝟎 \\ 𝐴𝐯−𝜆𝐼𝐯 & =𝟎 \\ (𝐴−𝜆𝐼)𝐯 & =𝟎\end{aligned}


$$

The final equation above tells us that there should be at least one non-zero vector $\mathbf{\color{blue}v}$ that lies in $\textrm{Null}(A-\lambda I)$, the null space of the matrix $A-\lambda I.$ As a result, the invertible matrix theorem tells us that the matrix $\, A-\lambda I \,$ must be singular, meaning $\det(A-\lambda I) = 0.$

We've reduced the problem to finding the values of $\lambda$ that satisfy the equation

$$


\det(A-\lambda I) = 0,


$$

which is called the **characteristic equation** of the matrix $A$. So, let's solve it!

First, we write down the matrix $A-\lambda I\mathbin{:}$

$$


\begin{aligned}𝐴\,−\,𝜆𝐼 & =[\begin{aligned}2 & 5 \\ −1 & −4\end{aligned}]\,−\,𝜆[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}2\,−\,𝜆 & 5 \\ −1 & −4\,−\,𝜆\end{aligned}]\end{aligned}


$$

Then, we solve the characteristic equation $\det(A-\lambda I) = 0\mathbin{:}$

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{aligned}2−𝜆 & 5 \\ −1 & −4−𝜆\end{aligned} & =0 \\ (2−𝜆)(−4−𝜆)−5⋅(−1) & =0 \\ −8−2𝜆+4𝜆+𝜆^{2}+5 & =0 \\ 𝜆^{2}+2𝜆−3 & =0 \\ (𝜆+3)(𝜆−1) & =0\end{aligned}


$$

Therefore, the eigenvalues of $A$ are $\lambda=-3$ and $\lambda=1.$

### Example: Finding the Characteristic Equation of a Matrix

#### Question

Find the characteristic equation of the matrix $[\begin{aligned}2 & 4 \\ 3 & 2\end{aligned}]$

#### Explanation

First, we find the matrix $\, A-\lambda I\mathbin{:}$

$$


[\begin{aligned}2−𝜆 & 4 \\ 3 & 2−𝜆\end{aligned}]


$$

Then, the characteristic equation is

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{aligned}2−𝜆 & 4 \\ 3 & 2−𝜆\end{aligned} & =0 \\ (2−𝜆)(2−𝜆)−4⋅3 & =0 \\ 4−4𝜆+𝜆^{2}−12 & =0 \\ 𝜆^{2}−4𝜆−8 & =0.\end{aligned}


$$

### The Number of Real Eigenvalues of a 2x2 Matrix

The characteristic equation of any $2 \!\times\! 2$ matrix $A$ is always a quadratic equation, which implies that $A$ has at most $2$ eigenvalues. Here are the all possible cases:

- Two distinct real eigenvalues

- One repeated real eigenvalue (or, equivalently, two real eigenvalues that are the same)

- No real eigenvalues (or, equivalently, two complex eigenvalues)

### Example: Computing the Eigenvalues of a Matrix With Two Distinct Eigenvalues

#### Question

Find all real eigenvalues of the matrix $[\begin{aligned}10 & 3 \\ 6 & 7\end{aligned}]$

#### Explanation

Let's start by writing the matrix $A - \lambda I\mathbin{:}$

$$


[\begin{aligned}10−𝜆 & 3 \\ 6 & 7−𝜆\end{aligned}]


$$

Now, let's find and solve the characteristic equation $\det(A-\lambda I) = 0\mathbin{:}$

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{aligned}10−𝜆 & 3 \\ 6 & 7−𝜆\end{aligned} & =0 \\ (10−𝜆)(7−𝜆)−3⋅6 & =0 \\ 70−7𝜆−10𝜆+𝜆^{2}−18 & =0 \\ 𝜆^{2}−17𝜆+52 & =0\end{aligned}


$$

Using the quadratic formula, we obtain

$$


\begin{aligned}𝜆 & =\frac{17±\sqrt{√(−17)^{2}−4⋅1⋅52}}{2⋅1} \\ & =\frac{17±\sqrt{√81}}{2} \\ & =\frac{17±9}{2} \\ & =13,4.\end{aligned}


$$

Therefore, the eigenvalues are $\lambda=13$ and $\lambda=4.$

### Example: Computing the Eigenvalues of a Matrix With At Most One Distinct Eigenvalue

#### Question

Find all real eigenvalues of the matrix $[\begin{aligned}4 & 0 \\ 0 & 4\end{aligned}]$

#### Explanation

Let's start by writing the matrix $B-\lambda I\mathbin{:}$

$$


[\begin{aligned}4−𝜆 & 0 \\ 0 & 4−𝜆\end{aligned}]


$$

Now, let's find and solve the characteristic equation $\det(B-\lambda I) = 0\mathbin{:}$

$$


\begin{aligned}det(𝐵−𝜆𝐼) & =0 \\ \begin{aligned}4−𝜆 & 0 \\ 0 & 4−𝜆\end{aligned} & =0 \\ (4−𝜆)(4−𝜆)−0⋅0 & =0 \\ (𝜆−4)^{2} & =0\end{aligned}


$$

Therefore, the matrix $B$ has only one eigenvalue $\lambda=4,$ which is a double root of the characteristic equation.

**** We also say that $\lambda=4$ has an **** of $2.$

### Example: Calculating the Eigenvalues of a Triangular/Diagonal Matrix

#### Question

Find all real eigenvalues of the matrix $[\begin{aligned}3 & 0 \\ 9 & −2\sqrt{√3}\end{aligned}]$

#### Explanation

Let's start by writing the matrix $A - \lambda I \mathbin{:}$

$$


[\begin{aligned}3−𝜆 & 0 \\ 9 & −2\sqrt{√3}−𝜆\end{aligned}]


$$

Now, let's find and solve the characteristic equation $\det (A - \lambda I) = 0\mathbin{:}$

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{aligned}3−𝜆 & 0 \\ 9 & −2\sqrt{√3}−𝜆\end{aligned} & =0 \\ (3−𝜆)(−2\sqrt{√3}−𝜆)−9⋅0 & =0 \\ (𝜆−3)(𝜆+2\sqrt{√3}) & =0\end{aligned}


$$

So, we get the eigenvalues $\lambda={\color{red}3}$ and $\lambda={\color{blue}-2\sqrt{3}}.$

If we look again at the matrix

$$


[\begin{aligned}3 & 0 \\ 9 & −2\sqrt{√3}\end{aligned}]


$$

we see that the eigenvalues are the entries on the main diagonal. This is true in general: the eigenvalues of a ** or ** matrix are ** given by the entries on the main diagonal!

**** For a general matrix (which is neither triangular nor diagonal), this might not be the case!
