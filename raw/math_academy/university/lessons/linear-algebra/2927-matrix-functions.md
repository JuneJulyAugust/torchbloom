# Matrix Functions

Source: https://www.mathacademy.com/topics/2927?courseId=55
Topic ID: 2927

## Prerequisites

- [Maclaurin Series](../../../ap-courses/lessons/ap-calculus-bc/340-maclaurin-series.md)
- [Jordan Canonical Decomposition of a 2x2 Matrix](./3652-jordan-canonical-decomposition-of-a-2x2-matrix.md)

## Lesson

### Introduction

We can extend a scalar function $f(x)$ to a square matrix argument $A.$ This function $f(A)$ is called a **matrix function**, and maps a square matrix to another square matrix of the same size.

Given a square matrix $A$ and a scalar function $f$ with Maclaurin series

$$


f(x) = \sum_{k=0}^\infty c_k x^k,


$$

we can define $f(A)$ by replacing $x$ with $A,$ with addition and multiplication performed in the matrix sense:

$$


f(A) = \sum_{k=0}^\infty c_k A^k


$$

For example, recall that the Maclaurin series of $f(x) = e^x$ is

$$


e^x = \sum_{k=0}^\infty \dfrac{x^k}{k!}.


$$

Then, for a square matrix $A,$ we define the matrix exponential as

$$


e^A = \sum_{k=0}^\infty \dfrac{1}{k!}A^k.


$$

In the next slide, we'll see how to apply matrix functions to square matrices.

### Function of a Diagonal Matrix

Suppose $D$ is a diagonal matrix with diagonal entries $\lambda_1, \ldots, \lambda_n{:}$

$$


\begin{aligned}𝜆_{1} & 0 & ⋯ & 0 \\ 0 & 𝜆_{2} & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & ⋯ & 𝜆_{𝑛}\end{aligned}


$$

For a scalar function $f$ with a Maclaurin series expansion, $f(D)$ is the diagonal matrix with diagonal entries $f(\lambda_1), \ldots, f(\lambda_n){:}$

$$


\begin{aligned}𝑓(𝜆_{1}) & 0 & ⋯ & 0 \\ 0 & 𝑓(𝜆_{2}) & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & ⋯ & 𝑓(𝜆_{𝑛})\end{aligned}


$$

For example, given the matrix $[\begin{aligned}2 & 0 \\ 0 & 1\end{aligned}]$ and the function $f(x) = e^x,$ we have

$$


[\begin{aligned}𝑓(2) & 0 \\ 0 & 𝑓(1)\end{aligned}]


$$

This rule works because raising a diagonal matrix to a power is equivalent to raising each diagonal entry to the same power.

Indeed, if $\displaystyle f(x) = \sum_{k=0}^\infty c_k x^k$ is the Maclaurin series of $f,$ then, by the definition of $f(D),$ we have

$$


\begin{aligned}𝑓(𝐷) & =\underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}𝑐_{𝑘}𝐷^{𝑘} \\ & =\underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}𝑐_{𝑘}\begin{aligned}𝜆_{1} & 0 & ⋯ & 0 \\ 0 & 𝜆_{2} & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & ⋯ & 𝜆_{𝑛}\end{aligned}^{𝑘} \\ & =\underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}𝑐_{𝑘}\begin{aligned}𝜆_{𝑘1}^{} & 0 & ⋯ & 0 \\ 0 & 𝜆_{𝑘2}^{} & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & ⋯ & 𝜆_{𝑘𝑛}^{}\end{aligned} \\ & =\begin{aligned}\underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}𝑐_{𝑘}𝜆_{𝑘1}^{} & 0 & ⋯ & 0 \\ 0 & \underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}𝑐_{𝑘}𝜆_{𝑘2}^{} & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & ⋯ & \underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}𝑐_{𝑘}𝜆_{𝑘𝑛}^{}\end{aligned} \\ & =\begin{aligned}𝑓(𝜆_{1}) & 0 & ⋯ & 0 \\ 0 & 𝑓(𝜆_{2}) & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & ⋯ & 𝑓(𝜆_{𝑛})\end{aligned}.\end{aligned}


$$

### Example: Computing the Value of a Function of a Diagonal Matrix

#### Question

Given that $\begin{aligned}100 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 10\end{aligned}$ find $\log D.$

#### Explanation

Given a function $f$ and a diagonal matrix $D$ with diagonal entries $\lambda_1, \ldots, \lambda_n,$ we have

$$


\begin{aligned}𝑓(𝜆_{1}) & ⋯ & 0 \\ ⋮ & ⋱ & ⋮ \\ 0 & ⋯ & 𝑓(𝜆_{𝑛})\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}log⁡𝐷 & =\begin{aligned}log⁡(100) & 0 & 0 \\ 0 & log⁡(1) & 0 \\ 0 & 0 & log⁡(10)\end{aligned}=\begin{aligned}2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1\end{aligned}.\end{aligned}


$$

### Function of a Jordan Block

Suppose $J_n(\lambda)$ is an $n\times n$ Jordan block where the main diagonal entries are all $\lambda{:}$

$$


\begin{aligned}𝜆 & 1 & 0 & ⋯ & 0 \\ 0 & 𝜆 & 1 & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋱ & ⋮ \\ 0 & ⋯ & 0 & 𝜆 & 1 \\ 0 & ⋯ & ⋯ & 0 & 𝜆\end{aligned}


$$

For a scalar function $f$ analytic at $\lambda$ (i.e., has a Taylor series expansion at $\lambda$), $f(J_n(\lambda))$ is the matrix

$$


\begin{aligned}𝑓(𝜆) & 𝑓^{′}(𝜆) & \frac{𝑓^{″}(𝜆)}{2!} & ⋯ & \frac{𝑓^{(𝑛−1)}(𝜆)}{(𝑛−1)!} \\ 0 & 𝑓(𝜆) & 𝑓^{′}(𝜆) & ⋯ & \frac{𝑓^{(𝑛−2)}(𝜆)}{(𝑛−2)!} \\ ⋮ & ⋱ & ⋱ & ⋱ & ⋮ \\ 0 & ⋯ & 0 & 𝑓(𝜆) & 𝑓^{′}(𝜆) \\ 0 & ⋯ & ⋯ & 0 & 𝑓(𝜆)\end{aligned}


$$

To demonstrate, let's find $f(J_3(2))$ for $f(x) = \ln x.$

Since $J_3(2)$ is a $3\times 3$ matrix, we will need the first $3-1=2$ derivatives of $f{:}$

$$


\begin{aligned}𝑓(𝑥) & =ln⁡𝑥 \\ 𝑓^{′}(𝑥) & =\frac{1}{𝑥} \\ 𝑓^{″}(𝑥) & =−\frac{1}{𝑥^{2}}\end{aligned}


$$

Therefore, we have

Now that we can compute the value of a function of a Jordan block, we can also find the value of a function of a Jordan matrix.

### Function of a Jordan Matrix

Consider a Jordan matrix formed by the direct sum of blocks $J_{n_1}(\lambda_1) {\textstyle\:\oplus\:} \cdots {\textstyle\:\oplus\:} J_{n_k}(\lambda_k)$ and a function $f.$ By applying the rule for diagonal matrices to this block diagonal matrix, we get

$$


\begin{aligned}𝑓(𝐽_{𝑛_{1}}(𝜆_{1})\,⊕\,⋯\,⊕\,𝐽_{𝑛_{𝑘}}(𝜆_{𝑘})) & =𝑓\begin{aligned}𝐽_{𝑛_{1}}(𝜆_{1}) & ⋯ & 0 \\ ⋮ & ⋱ & ⋮ \\ 0 & ⋯ & 𝐽_{𝑛_{𝑘}}(𝜆_{𝑘})\end{aligned} \\ & =\begin{aligned}𝑓(𝐽_{𝑛_{1}}(𝜆_{1})) & ⋯ & 0 \\ ⋮ & ⋱ & ⋮ \\ 0 & ⋯ & 𝑓(𝐽_{𝑛_{𝑘}}(𝜆_{𝑘}))\end{aligned} \\ & =𝑓(𝐽_{𝑛_{1}}(𝜆_{1}))\,⊕\,⋯\,⊕\,𝑓(𝐽_{𝑛_{𝑘}}(𝜆_{𝑘})).\end{aligned}


$$

This allows us to compute functions of any matrix in Jordan Normal Form by applying the function to each Jordan block individually.

For example, suppose $J = J_2(2) \oplus J_1(3).$ Then, applying a function $f,$ we have

$$


[\begin{aligned}𝑓(𝐽_{2}(2)) & 0 \\ 0 & 𝑓(𝐽_{1}(3))\end{aligned}]


$$

### Example: Computing the Value of a Function of a Jordan Block

#### Question

Find $f\left(J_4(1) \right)$ for $f(x)=2^x.$

#### Explanation

Given a function $f$ and a Jordan block $J_n(\lambda),$ we have

$$


\begin{aligned}𝑓(𝜆) & 𝑓^{′}(𝜆) & \frac{𝑓^{″}(𝜆)}{2!} & ⋯ & \frac{𝑓^{(𝑛−1)}(𝜆)}{(𝑛−1)!} \\ 0 & 𝑓(𝜆) & 𝑓^{′}(𝜆) & ⋯ & \frac{𝑓^{(𝑛−2)}(𝜆)}{(𝑛−2)!} \\ ⋮ & ⋱ & ⋱ & ⋱ & ⋮ \\ 0 & ⋯ & 0 & 𝑓(𝜆) & 𝑓^{′}(𝜆) \\ 0 & ⋯ & ⋯ & 0 & 𝑓(𝜆)\end{aligned}


$$

In this case, we have $f(x) = 2^{x},$ $n=4,$ and $\lambda=1.$

Since $n=4,$ we need to compute the first $4-1=3$ derivatives of $f{:}$

$$


\begin{aligned}𝑓(𝑥) & =2^{𝑥} \\ 𝑓^{′}(𝑥) & =2^{𝑥}ln⁡2 \\ 𝑓^{″}(𝑥) & =2^{𝑥}(ln⁡2)^{2} \\ 𝑓^{‴}(𝑥) & =2^{𝑥}(ln⁡2)^{3}\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}𝑓(𝐽_{4}(1)) & =\begin{aligned}𝑓(1) & 𝑓^{′}(1) & \frac{1}{2!}𝑓^{″}(1) & \frac{1}{3!}𝑓^{‴}(1) \\ 0 & 𝑓(1) & 𝑓^{′}(1) & \frac{1}{2!}𝑓^{″}(1) \\ 0 & 0 & 𝑓(1) & 𝑓^{′}(1) \\ 0 & 0 & 0 & 𝑓(1)\end{aligned} \\ & =\begin{aligned}2^{1} & 2^{1}(ln⁡2) & \frac{1}{2}⋅2^{1}(ln⁡2)^{2} & \frac{1}{6}⋅2^{1}(ln⁡2)^{3} \\ 0 & 2^{1} & 2^{1}(ln⁡2) & \frac{1}{2}⋅2^{1}(ln⁡2)^{2} \\ 0 & 0 & 2^{1} & 2^{1}(ln⁡2) \\ 0 & 0 & 0 & 2^{1}\end{aligned} \\ & =\begin{aligned}2 & 2ln⁡2 & (ln⁡2)^{2} & \frac{1}{3}(ln⁡2)^{3} \\ 0 & 2 & 2ln⁡2 & (ln⁡2)^{2} \\ 0 & 0 & 2 & 2ln⁡2 \\ 0 & 0 & 0 & 2\end{aligned}\end{aligned}


$$

### Example: Computing the Value of a Function of a Jordan Matrix

#### Question

Let $J_n\left(\lambda\right)$ denote the $n \times n$ Jordan block matrix with $\lambda$ on the main diagonal. Then, find $e^{2\left(J_2(1) {\textstyle\:\oplus\:} J_2(3)\right)}.$

#### Explanation

Given a function $f$ and a Jordan block $J_n(\lambda),$ we have

$$


\begin{aligned}𝑓(𝜆) & 𝑓^{′}(𝜆) & \frac{𝑓^{″}(𝜆)}{2!} & ⋯ & \frac{𝑓^{(𝑛−1)}(𝜆)}{(𝑛−1)!} \\ 0 & 𝑓(𝜆) & 𝑓^{′}(𝜆) & ⋯ & \frac{𝑓^{(𝑛−2)}(𝜆)}{(𝑛−2)!} \\ ⋮ & ⋱ & ⋱ & ⋱ & ⋮ \\ 0 & ⋯ & 0 & 𝑓(𝜆) & 𝑓^{′}(𝜆) \\ 0 & ⋯ & ⋯ & 0 & 𝑓(𝜆)\end{aligned}


$$

First, note that

$$


\begin{aligned}𝑒^{2(𝐽_{2}(1)\,⊕\,𝐽_{2}(3))} & =𝑒^{2([\begin{aligned}𝐽_{2}(1) & 0 \\ 0 & 𝐽_{2}(3)\end{aligned}])} \\ & =[\begin{aligned}𝑒^{2(𝐽_{2}(1))} & 0 \\ 0 & 𝑒^{2(𝐽_{2}(3))}\end{aligned}] \\ & =𝑒^{2(𝐽_{2}(1))}\,⊕\,𝑒^{2(𝐽_{2}(3))}.\end{aligned}


$$

So, we compute the function of each Jordan block separately.

- For $J_2(1),$ we have $n=2$ and $\lambda=1.$ Since $n=2,$ we need to compute the first derivative of $f$ only: So, we get

- For $J_2(3),$ we have $n=2$ and $\lambda=3.$ Since $n=2,$ we need the first derivative of $f$ only, which we have already computed. So, we get

Therefore, we conclude that

$$


\begin{aligned}𝑒^{2} & 2𝑒^{2} & 0 & 0 \\ 0 & 𝑒^{2} & 0 & 0 \\ 0 & 0 & 𝑒^{6} & 2𝑒^{6} \\ 0 & 0 & 0 & 𝑒^{6}\end{aligned}


$$

### Function of a Jordan Decomposition

Suppose $A$ and $S$ are matrices, where $S$ is invertible. For a scalar function $f$ with a Maclaurin series expansion, we have

$$


f(SAS^{-1}) = Sf(A)S^{-1}.


$$

Indeed, given the Maclaurin series $\displaystyle f(x) = \sum_{k=0}^\infty c_kx^k,$ we have

$$


\begin{aligned}𝑓(𝑆𝐴𝑆^{−1}) & =\underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}𝑐_{𝑘}(𝑆𝐴𝑆^{−1})^{𝑘} \\ & =\underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}𝑐_{𝑘}𝑆𝐴^{𝑘}𝑆^{−1} \\ & =𝑆(\underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}𝑐_{𝑘}𝐴^{𝑘})𝑆^{−1} \\ & =𝑆𝑓(𝐴)𝑆^{−1}.\end{aligned}


$$

So far, we have seen how to evaluate functions for diagonal matrices and Jordan blocks. With the formula above, we will now be able to

- evaluate $f(B)$ for diagonalizable $B$ using a diagonalization $B=PDP^{-1},$ and

- evaluate $f(B)$ for non-diagonalizable $B$ using a Jordan decomposition $B=PJP^{-1}.$

Let's see how with an example.

### Example: Computing the Value of a Function of a Jordan Decomposition

#### Question

Consider the following matrices:

$$


[\begin{aligned}−4 & 1 \\ −1 & −2\end{aligned}]


$$

Given that $V = PJP^{-1},$ find $\sin\left(\pi V\right).$

#### Explanation

Given a function $f$ and matrices $A$ and $S,$ where $S$ is invertible, we have

$$


f(SAS^{-1}) = S \cdot f(A) \cdot S^{-1}.


$$

For $f(x) = \sin(\pi x)$ and the given matrix $V,$ we have

$$


\sin(\pi V) = \sin\left(\pi{PJP^{-1}}\right) = P \cdot (\sin(\pi J)) \cdot P^{-1}.


$$

Now, since $J$ is a Jordan block with $-3$s on the main diagonal, we have

$$


[\begin{aligned}𝑓(−3) & 𝑓^{′}(−3) \\ 0 & 𝑓(−3)\end{aligned}]


$$

The derivative of $f$ is $f'(x) = \pi \cos \pi x.$ So, we get

$$


[\begin{aligned}𝑓(−3) & 𝑓^{′}(−3) \\ 0 & 𝑓(−3)\end{aligned}]


$$

Also, the inverse of $P$ is

$$


[\begin{aligned}1 & 0 \\ −1 & 1\end{aligned}]


$$

Therefore, we conclude that

$$


\begin{aligned}sin⁡(𝜋𝑉) & =𝑃⋅(sin⁡(𝜋𝐽))⋅𝑃^{−1} \\ & =[\begin{aligned}1 & 0 \\ 1 & 1\end{aligned}][\begin{aligned}0 & −𝜋 \\ 0 & 0\end{aligned}][\begin{aligned}1 & 0 \\ −1 & 1\end{aligned}] \\ & =[\begin{aligned}1 & 0 \\ 1 & 1\end{aligned}][\begin{aligned}𝜋 & −𝜋 \\ 0 & 0\end{aligned}] \\ & =[\begin{aligned}𝜋 & −𝜋 \\ 𝜋 & −𝜋\end{aligned}].\end{aligned}


$$
