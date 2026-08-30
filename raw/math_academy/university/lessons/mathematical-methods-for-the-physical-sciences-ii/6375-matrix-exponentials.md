# Matrix Exponentials

Source: https://www.mathacademy.com/topics/6375?courseId=155
Topic ID: 6375

## Prerequisites

- [Differentiating Taylor Series](../../../ap-courses/lessons/ap-calculus-bc/36-differentiating-taylor-series.md)
- [The Cayley-Hamilton Theorem](../linear-algebra/1972-the-cayley-hamilton-theorem.md)
- [Finding Complex Eigenvalues of Real 2x2 Matrices](../linear-algebra/2016-finding-complex-eigenvalues-of-real-2x2-matrices.md)

## Lesson

### Introduction

In this topic, we'll learn how to compute the **matrix exponential**.

Recall that the scalar exponential function $e^t$ can be written as the power series

$$


e^t = \sum_{k=0}^{\infty}\dfrac{t^k}{k!} = 1 + t + \dfrac{t^2}{2} + \cdots + \dfrac{t^k}{k!} + \cdots.


$$

Now, let $A$ be an $n\times n$ matrix. By definition, the matrix exponential $e^{At}$ is given by the analogous series

$$


e^{At} = \sum_{k=0}^{\infty}\frac{A^k t^k}{k!} = I + tA + \dfrac{t^2}{2}A^2 + \cdots + \dfrac{t^k}{k!}A^k + \cdots.


$$

There are several approaches for computing matrix exponentials:

- The most direct approach is to use the definition above, but this is typically impractical.

- Another method, often covered in linear algebra courses, is to use the Jordan canonical form of $A$. This works, but it can also be tedious, especially for larger matrices.

Here, we will introduce a different method.

By the Cayley–Hamilton theorem, every power $A^n, A^{n+1}, \ldots$ can be rewritten as a linear combination of

$$


I, \: A, \: A^2, \: \ldots, \: A^{n-1}.


$$

As a result, $e^{At}$ can be written in the form

$$


e^{At}=\alpha_{n-1}A^{n-1} t^{n-1}+\alpha_{n-2} A^{n-2}t^{n-2}+\cdots+\alpha_1 At+\alpha_0 I,


$$

where $\alpha_0, \alpha_1, \ldots, \alpha_{n-1}$ are functions of $t$ and $I$ is the $n \times n$ identity matrix.

Now, we define the polynomial

$$


r(\lambda)=\alpha_{n-1}\lambda^{n-1}+\alpha_{n-2}\lambda^{n-2}+\cdots+\alpha_1\lambda+\alpha_0.


$$

Then we have the following key fact:

For any eigenvalue $\lambda$ of $At$, we have $r(\lambda) = e^{\lambda}.$

Let’s now see how this method works in practice.

### 2x2 Matrices With Distinct Real Eigenvalues

Let's find $e^{At}$ for $[\begin{aligned}2 & 0 \\ −7 & 7\end{aligned}]$

By solving the characteristic polynomial $|A-\lambda I|=0,$ we can find that the eigenvalues of $A$ are

$$


\lambda_1=2, \qquad \lambda_2=7.


$$

We have a square matrix of dimension $n=2.$ Thus,

$$


\begin{aligned}𝑒^{𝐴𝑡} & =𝛼_{1}𝐴𝑡+𝛼_{0}𝐼 \\ & =𝛼_{1}[\begin{aligned}2 & 0 \\ −7 & 7\end{aligned}]𝑡+𝛼_{0}[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}2𝛼_{1}𝑡+𝛼_{0} & 0 \\ −7𝛼_{1}𝑡 & 7𝛼_{1}𝑡+𝛼_{0}\end{aligned}],\end{aligned}


$$

where $\alpha_1$ and $\alpha_0$ are functions to be determined.

Consider the polynomial $r(\lambda) = \alpha_1 \lambda + \alpha_0.$ The eigenvalues of $At$ are

$$


\lambda_1=2t, \qquad \lambda_2=7t,


$$

both of multiplicity one. Thus, we have the following:

$$


\begin{aligned}\begin{aligned}𝑟(2𝑡)=𝑒^{2𝑡} \\ 𝑟(7𝑡)=𝑒^{7𝑡}\end{aligned}\,⇒\,\begin{aligned}2𝑡𝛼_{1}+𝛼_{0}=𝑒^{2𝑡} \\ 7𝑡𝛼_{1}+𝛼_{0}=𝑒^{7𝑡}\end{aligned}\end{aligned}


$$

Now, we solve the system for $\alpha_1$ and $\alpha_0{:}$

- Subtracting the first equation from the second one, we get

$$


5t\alpha_1 = e^{7t} - e^{2t} \qquad\Rightarrow\qquad \alpha_1 = \dfrac{1}{5t}\bigl(e^{7t}-e^{2t}\bigr).


$$

- Multiplying the first equation by $7$ and subtracting twice the second one, we get

$$


5\alpha_0 = 7e^{2t} - 2e^{7t} \qquad\Rightarrow\qquad \alpha_0 = \dfrac{1}{5}\bigl(7e^{2t}-2e^{7t}\bigr).


$$

Substituting $\alpha_1$ and $\alpha_0$ into the expressions for the entries of $e^{At},$ we get the following:

$$


\begin{aligned}2𝛼_{1}𝑡+𝛼_{0} & =2(\frac{1}{5𝑡}(𝑒^{7𝑡}−𝑒^{2𝑡}))𝑡+\frac{1}{5}(7𝑒^{2𝑡}−2𝑒^{7𝑡}) \\ & =\frac{1}{5}((2𝑒^{7𝑡}−2𝑒^{2𝑡})+(7𝑒^{2𝑡}−2𝑒^{7𝑡})) \\ & =𝑒^{2𝑡} \\ −7𝛼_{1}𝑡 & =−7(\frac{1}{5𝑡}(𝑒^{7𝑡}−𝑒^{2𝑡}))𝑡 \\ & =−\frac{7}{5}(𝑒^{7𝑡}−𝑒^{2𝑡}) \\ & =\frac{7}{5}(𝑒^{2𝑡}−𝑒^{7𝑡}) \\ 7𝛼_{1}𝑡+𝛼_{0} & =7(\frac{1}{5𝑡}(𝑒^{7𝑡}−𝑒^{2𝑡}))𝑡+\frac{1}{5}(7𝑒^{2𝑡}−2𝑒^{7𝑡}) \\ & =\frac{1}{5}((7𝑒^{7𝑡}−7𝑒^{2𝑡})+(7𝑒^{2𝑡}−2𝑒^{7𝑡})) \\ & =𝑒^{7𝑡}\end{aligned}


$$

Therefore,

$$


[\begin{aligned}5𝑒^{2𝑡} & 0 \\ 7(𝑒^{2𝑡}−𝑒^{7𝑡}) & 5𝑒^{7𝑡}\end{aligned}]


$$

### Example: Finding the Matrix Exponent for a Matrix With Distinct Real Eigenvalues

#### Question

Find $e^{At}$ for $[\begin{aligned}1 & 0 \\ −3 & 4\end{aligned}]$

**

#### Explanation

We have a square matrix of dimension $n=2.$ Thus,

$$


\begin{aligned}𝑒^{𝐴𝑡} & =𝛼_{1}𝐴𝑡+𝛼_{0}𝐼 \\ & =𝛼_{1}[\begin{aligned}1 & 0 \\ −3 & 4\end{aligned}]𝑡+𝛼_{0}[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}𝛼_{1}𝑡+𝛼_{0} & 0 \\ −3𝛼_{1}𝑡 & 4𝛼_{1}𝑡+𝛼_{0}\end{aligned}],\end{aligned}


$$

where $\alpha_1$ and $\alpha_0$ are functions to be determined.

Consider the polynomial $r(\lambda) = \alpha_1 \lambda + \alpha_0.$ The eigenvalues of $At$ are

$$


\lambda_1=t, \qquad \lambda_2=4t,


$$

both of multiplicity one. Thus, we have the following:

$$


\begin{aligned}\begin{aligned}𝑟(𝑡)=𝑒^{𝑡} \\ 𝑟(4𝑡)=𝑒^{4𝑡}\end{aligned}\,⇒\,\begin{aligned}𝑡𝛼_{1}+𝛼_{0}=𝑒^{𝑡} \\ 4𝑡𝛼_{1}+𝛼_{0}=𝑒^{4𝑡}\end{aligned}\end{aligned}


$$

Now, we solve the system for $\alpha_1$ and $\alpha_0{:}$

- Subtracting the first equation from the second one, we get

$$


3t\alpha_1 = e^{4t} - e^{t} \qquad\Rightarrow\qquad \alpha_1 = \dfrac{1}{3t}\bigl(e^{4t}-e^{t}\bigr).


$$

- Multiplying the first equation by $4$ and subtracting the second one, we get

$$


3\alpha_0 = 4e^{t} - e^{4t} \qquad\Rightarrow\qquad \alpha_0 = \dfrac{1}{3}\bigl(4e^{t}-e^{4t}\bigr).


$$

Substituting $\alpha_1$ and $\alpha_0$ into the expressions for the entries of $e^{At},$ we get the following:

$$


\begin{aligned}𝛼_{1}𝑡+𝛼_{0} & =(\frac{1}{3𝑡}(𝑒^{4𝑡}−𝑒^{𝑡}))𝑡+\frac{1}{3}(4𝑒^{𝑡}−𝑒^{4𝑡}) \\ & =\frac{1}{3}(𝑒^{4𝑡}−𝑒^{𝑡}+4𝑒^{𝑡}−𝑒^{4𝑡}) \\ & =𝑒^{𝑡} \\ −3𝛼_{1}𝑡 & =−3(\frac{1}{3𝑡}(𝑒^{4𝑡}−𝑒^{𝑡}))𝑡 \\ & =𝑒^{𝑡}−𝑒^{4𝑡} \\ 4𝛼_{1}𝑡+𝛼_{0} & =4(\frac{1}{3𝑡}(𝑒^{4𝑡}−𝑒^{𝑡}))𝑡+\frac{1}{3}(4𝑒^{𝑡}−𝑒^{4𝑡}) \\ & =\frac{1}{3}((4𝑒^{4𝑡}−4𝑒^{𝑡})+(4𝑒^{𝑡}−𝑒^{4𝑡})) \\ & =𝑒^{4𝑡}\end{aligned}


$$

Therefore,

$$


[\begin{aligned}𝑒^{𝑡} & 0 \\ 𝑒^{𝑡}−𝑒^{4𝑡} & 𝑒^{4𝑡}\end{aligned}]


$$

### Example: Finding the Matrix Exponent for a Matrix With Distinct Complex Eigenvalues

#### Question

Find $e^{At}$ for $[\begin{aligned}7 & 4 \\ −5 & −1\end{aligned}]$

**

#### Explanation

We have a square matrix of dimension $n=2.$ Thus,

$$


\begin{aligned}𝑒^{𝐴𝑡} & =𝛼_{1}𝐴𝑡+𝛼_{0}𝐼 \\ & =𝛼_{1}[\begin{aligned}7 & 4 \\ −5 & −1\end{aligned}]𝑡+𝛼_{0}[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}7𝛼_{1}𝑡+𝛼_{0} & 4𝛼_{1}𝑡 \\ −5𝛼_{1}𝑡 & −𝛼_{1}𝑡+𝛼_{0}\end{aligned}].\end{aligned}


$$

where $\alpha_1$ and $\alpha_0$ are functions to be determined.

Consider the polynomial $r(\lambda) = \alpha_1 \lambda + \alpha_0.$ The eigenvalues or $At$ are

$$


\lambda_1= (3+2\textrm{i}) t, \qquad \lambda_2= (3-2\textrm{i}) t,


$$

which are complex conjugates. Thus, we have the following:

$$


\begin{aligned}𝑟((3+2i)𝑡) & =𝑒^{(3+2i)𝑡} \\ 𝛼_{1}(3+2i)𝑡+𝛼_{0} & =𝑒^{3𝑡}(cos⁡(2𝑡)+isin⁡(2𝑡)) \\ (3𝛼_{1}𝑡+𝛼_{0})+2𝛼_{1}i𝑡 & =𝑒^{3𝑡}cos⁡(2𝑡)+i\,𝑒^{3𝑡}sin⁡(2𝑡)\end{aligned}


$$

Now, we equate the real and imaginary parts, and solve for $\alpha_1$ and $\alpha_0{:}$

$$


\begin{aligned}\begin{aligned}3𝛼_{1}𝑡+𝛼_{0}=𝑒^{3𝑡}cos⁡(2𝑡) \\ 2𝑡𝛼_{1}=𝑒^{3𝑡}sin⁡(2𝑡)\end{aligned}\,⇒\,\begin{aligned}𝛼_{1}=\frac{1}{2𝑡}𝑒^{3𝑡}sin⁡(2𝑡) \\ 𝛼_{0}=𝑒^{3𝑡}(cos⁡(2𝑡)−\frac{3}{2}sin⁡(2𝑡))\end{aligned}\end{aligned}


$$

Substituting $\alpha_1$ and $\alpha_0$ into the expressions for the entries of $e^{At},$ we get the following:

$$


\begin{aligned}7𝛼_{1}𝑡+𝛼_{0} & =7⋅\frac{1}{2𝑡}𝑒^{3𝑡}sin⁡(2𝑡)⋅𝑡+𝑒^{3𝑡}(cos⁡(2𝑡)−\frac{3}{2}sin⁡(2𝑡)) \\ & =\frac{7}{2}𝑒^{3𝑡}sin⁡(2𝑡)+𝑒^{3𝑡}cos⁡(2𝑡)−\frac{3}{2}𝑒^{3𝑡}sin⁡(2𝑡) \\ & =𝑒^{3𝑡}(cos⁡(2𝑡)+2sin⁡(2𝑡)), \\ 4𝛼_{1}𝑡 & =4⋅\frac{1}{2𝑡}𝑒^{3𝑡}sin⁡(2𝑡)⋅𝑡 \\ & =2𝑒^{3𝑡}sin⁡(2𝑡), \\ −5𝛼_{1}𝑡 & =−5⋅\frac{1}{2𝑡}𝑒^{3𝑡}sin⁡(2𝑡)⋅𝑡 \\ & =−\frac{5}{2}𝑒^{3𝑡}sin⁡(2𝑡), \\ −𝛼_{1}𝑡+𝛼_{0} & =−\frac{1}{2𝑡}𝑒^{3𝑡}sin⁡(2𝑡)⋅𝑡+𝑒^{3𝑡}(cos⁡(2𝑡)−\frac{3}{2}sin⁡(2𝑡)) \\ & =−\frac{1}{2}𝑒^{3𝑡}sin⁡(2𝑡)+𝑒^{3𝑡}cos⁡(2𝑡)−\frac{3}{2}𝑒^{3𝑡}sin⁡(2𝑡) \\ & =𝑒^{3𝑡}(cos⁡(2𝑡)−2sin⁡(2𝑡))\end{aligned}


$$

Therefore,

$$


\begin{aligned}cos⁡(2𝑡)+2sin⁡(2𝑡) & 2sin⁡(2𝑡) \\ −\frac{5}{2}sin⁡(2𝑡) & cos⁡(2𝑡)−2sin⁡(2𝑡)\end{aligned}


$$

### 2x2 Matrices With Repeated Eigenvalues

Recall that the matrix exponential $e^{At}$ can be written as

$$


e^{At}=\alpha_{n-1} A^{n-1}t^{n-1}+\alpha_{n-2} A^{n-2}t^{n-2}+\cdots+\alpha_1 At+\alpha_0 I.


$$

If we define the polynomial

$$


r(\lambda)=\alpha_{n-1}\lambda^{n-1}+\alpha_{n-2}\lambda^{n-2}+\cdots+\alpha_1\lambda+\alpha_0,


$$

then for any eigenvalue $\lambda_i$ of $At,$ we have

$$


r(\lambda_i) = e^{\lambda_i}.


$$

However, for *repeated eigenvalues*, we have the following additional fact:

If $\lambda_i$ is an eigenvalue of multiplicity $k$ with $k>1,$ then

$$


\begin{aligned}\frac{d}{d𝜆}𝑟(𝜆)_{𝜆=𝜆_{𝑖}}=𝑒^{𝜆_{𝑖}},\,\frac{d^{2}}{d𝜆^{2}}𝑟(𝜆)_{𝜆=𝜆_{𝑖}}=𝑒^{𝜆_{𝑖}},\,…,\,\frac{d^{𝑘−1}}{d𝜆^{𝑘−1}}𝑟(𝜆)_{𝜆=𝜆_{𝑖}}=𝑒^{𝜆_{𝑖}}\end{aligned}


$$

Let's apply these facts to a concrete example.

### Example: Finding the Matrix Exponent for a Matrix With Repeated Eigenvalues

#### Question

Find $e^{At}$ for $[\begin{aligned}8 & −2 \\ 2 & 4\end{aligned}]$

**

#### Explanation

We have a square matrix of dimension $n=2.$ Thus,

$$


\begin{aligned}𝑒^{𝐴𝑡} & =𝛼_{1}𝐴𝑡+𝛼_{0}𝐼 \\ & =𝛼_{1}[\begin{aligned}8 & −2 \\ 2 & 4\end{aligned}]𝑡+𝛼_{0}[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}8𝛼_{1}𝑡+𝛼_{0} & −2𝛼_{1}𝑡 \\ 2𝛼_{1}𝑡 & 4𝛼_{1}𝑡+𝛼_{0}\end{aligned}],\end{aligned}


$$

where $\alpha_1$ and $\alpha_0$ are constants to be determined.

Consider the polynomial $r(\lambda) = \alpha_1 \lambda + \alpha_0.$ The only eigenvalue of $At$ is

$$


\lambda_1 = 6t


$$

of multiplicity two. Thus, we have the following:

$$


\begin{aligned}\begin{aligned}𝑟(6𝑡)=𝑒^{6𝑡} \\ \frac{d}{d𝜆}𝑟(6𝑡)=𝑒^{6𝑡}\end{aligned}\,⇒\,\begin{aligned}6𝑡𝛼_{1}+𝛼_{0}=𝑒^{6𝑡} \\ 𝛼_{1}=𝑒^{6𝑡}\end{aligned}\end{aligned}


$$

Now, we solve the system for $\alpha_1$ and $\alpha_0{:}$

- From the second equation, we get

- Substituting this into the first one, we get

Substituting $\alpha_1$ and $\alpha_0$ into the expressions for the required entries of $e^{At},$ we get the following:

$$


\begin{aligned}8𝛼_{1}𝑡+𝛼_{0} & =8𝑒^{6𝑡}𝑡+𝑒^{6𝑡}(1−6𝑡) \\ & =𝑒^{6𝑡}(1+2𝑡), \\ −2𝛼_{1}𝑡 & =−2𝑒^{6𝑡}𝑡 \\ & =𝑒^{6𝑡}(−2𝑡), \\ 2𝛼_{1}𝑡 & =2𝑒^{6𝑡}𝑡 \\ & =𝑒^{6𝑡}(2𝑡), \\ 4𝛼_{1}𝑡+𝛼_{0} & =4𝑒^{6𝑡}𝑡+𝑒^{6𝑡}(1−6𝑡) \\ & =𝑒^{6𝑡}(1−2𝑡).\end{aligned}


$$

Therefore,

$$


[\begin{aligned}1+2𝑡 & −2𝑡 \\ 2𝑡 & 1−2𝑡\end{aligned}]


$$

### Derivatives of Matrix Exponentials

Again, let $A$ be a constant $n\times n$ matrix. The matrix exponential satisfies

$$


\dfrac{\text{d}}{\text{d}t}\bigl(e^{At}\bigr)=A\,e^{At}.


$$

Indeed, recall that

$$


e^{At}=\sum_{k=0}^{\infty}\frac{(At)^k}{k!} =\sum_{k=0}^{\infty}\frac{A^k t^k}{k!}.


$$

To prove the formula, we differentiate the series above term-by-term:

$$


\begin{aligned}\frac{d}{d𝑡}(𝑒^{𝐴𝑡}) & =\underset{\underset{𝑘=1}{∑}}{\overset{}{∞}}\frac{𝐴^{𝑘}⋅𝑘𝑡^{𝑘−1}}{𝑘!} \\ & =\underset{\underset{𝑘=1}{∑}}{\overset{}{∞}}\frac{𝐴^{𝑘}𝑡^{𝑘−1}}{(𝑘−1)!} \\ & =𝐴\underset{\underset{𝑘=1}{∑}}{\overset{}{∞}}\frac{𝐴^{𝑘−1}𝑡^{𝑘−1}}{(𝑘−1)!} \\ & =𝐴\underset{\underset{𝑗=0}{∑}}{\overset{}{∞}}\frac{𝐴^{𝑗}𝑡^{𝑗}}{𝑗!} \\ & =𝐴\,𝑒^{𝐴𝑡}\end{aligned}


$$

### Example: Computing the Derivative of a Matrix Exponential

#### Question

$$


[\begin{aligned}1 & 1 \\ 0 & 1\end{aligned}]


$$

Given the matrices $A$ and $e^{At}$ above, compute $\dfrac{\text{d}}{\text{d}t} \big(e^{At}\big).$

#### Explanation

Recall that

$$


\dfrac{\text{d}}{\text{d}t} \big(e^{At}\big) = A \, e^{At}.


$$

Therefore, we have

$$


\begin{aligned}\frac{d}{d𝑡}(𝑒^{𝐴𝑡}) & =𝐴\,𝑒^{𝐴𝑡} \\ & =[\begin{aligned}1 & 1 \\ 0 & 1\end{aligned}][\begin{aligned}𝑒^{𝑡} & 𝑡𝑒^{𝑡} \\ 0 & 𝑒^{𝑡}\end{aligned}] \\ & =[\begin{aligned}𝑒^{𝑡} & (𝑡+1)𝑒^{𝑡} \\ 0 & 𝑒^{𝑡}\end{aligned}].\end{aligned}


$$

### Properties of the Matrix Exponential

Matrix exponentials have other properties. We list a few of them:

1. *Law of Exponents:* If $A$ is a constant square matrix, then

2. *Inverse:* For any $t,$ the matrix $e^{At}$ is invertible and

3. *Identity:* For any square matrix $A,$

4. *Product of exponentials:* If $A$ and $B$ commute (i.e., $AB = BA$), then **Watch out!** In general, this identity is *not true* unless $A$ and $B$ commute.
