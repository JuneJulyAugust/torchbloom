# The Cayley-Hamilton Theorem

Source: https://www.mathacademy.com/topics/1972?courseId=154
Topic ID: 1972

## Prerequisites

- [Dividing Polynomials Using Long Division](../algebra-ii/427-dividing-polynomials-using-long-division.md)
- [Vieta's Formulas](../algebra-i/729-vieta-s-formulas.md)
- [Powers of Matrices](../integrated-math-iii-honors/1725-powers-of-matrices.md)
- [The Characteristic Equation of a Matrix](./1964-the-characteristic-equation-of-a-matrix.md)

## Lesson

### Introduction

The characteristic equation of a square matrix $A$ is given by

$$


\det(A-\lambda I)=0.


$$

On the left-hand side of this equation, we have the expression

$$


\det(A-\lambda I),


$$

which we call the **characteristic polynomial** of the matrix $A.$

For instance, let's find the characteristic polynomial of the matrix $[\begin{aligned}−8 & −9 \\ 6 & 7\end{aligned}]$

$$


\begin{aligned}𝑝(𝜆) & =det(𝐶−𝜆𝐼) \\ & =\begin{aligned}−8−𝜆 & −9 \\ 6 & 7−𝜆\end{aligned} \\ & =(−8−𝜆)⋅(7−𝜆)−(−9)⋅6 \\ & =𝜆^{2}+𝜆−2\end{aligned}


$$

### The Characteristic Polynomial for 2x2 Matrices

What conclusions can we make regarding the characteristic polynomial of the general $2\times 2$ matrix $A,$ given by

$$


[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]


$$

First, let's find the characteristic equation:

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{aligned}𝑎−𝜆 & 𝑏 \\ 𝑐 & 𝑑−𝜆\end{aligned} & =0 \\ (𝑎−𝜆)(𝑑−𝜆)−𝑏𝑐 & =0 \\ 𝜆^{2}−(𝑎+𝑑)𝜆+(𝑎𝑑−𝑏𝑐) & =0\end{aligned}


$$

Notice that the constant term is the determinant of the matrix:

$$


\det(A) = ad-bc


$$

The coefficient of $\lambda$ is the sum of the diagonal entries of $A$ taken with a negative sign. The sum of the diagonal entries of a matrix $A$ is called the **trace** of $A,$ and we denote it as

$$


\mathrm{tr}(A) = a+d.


$$

So, for any $2\times 2$ matrix $A$, the characteristic polynomial is

$$


p(\lambda) = \lambda^2 -\mathrm{tr}(A)\lambda + \det(A).


$$

**Note:** This result can be extended to the general case of $n \times n$ matrices. If $A$ is an $n \times n$ matrix, then its characteristic polynomial takes the form

$$


\begin{aligned}𝑝(𝜆) & =det(𝐴−𝜆𝐼) \\ & =(−1)^{𝑛}𝜆^{𝑛}+𝑐_{𝑛−1}𝜆^{𝑛−1}+⋯+𝑐_{1}𝜆+𝑐_{0} \\ & =(−1)^{𝑛}𝜆^{𝑛}+\underset{𝑐_{𝑛−1}}{\underset{}{(−1)^{𝑛−1}tr(𝐴)}}𝜆^{𝑛−1}+⋯+𝑐_{1}𝜆+\underset{𝑐_{0}}{\underset{}{det(𝐴)}},\end{aligned}


$$

where

$$


\begin{aligned}𝑐_{𝑛−1}=(−1)^{𝑛−1}tr(𝐴)\,and\,𝑐_{0}=det(𝐴).\end{aligned}


$$

### Example: Calculating the Sum and Product of Eigenvalues of a 2x2 Matrix

#### Question

Given that $[\begin{aligned}9 & 1 \\ 2 & −6\end{aligned}]$ find the sum of the eigenvalues of $A.$

#### Explanation

The characteristic polynomial of $A$ is given by

$$


\begin{aligned}𝑝(𝜆) & =𝜆^{2}−tr(𝐴)𝜆+det(𝐴).\end{aligned}


$$

Now, using Vieta's formulas, we have that the roots of $p(\lambda),$ i.e., the eigenvalues of $A,$ satisfy

$$


\begin{aligned}𝜆_{1}+𝜆_{2}=tr(𝐴) \\ 𝜆_{1}⋅𝜆_{2}=det(𝐴).\end{aligned}


$$

So, the sum of the eigenvalues of $A$ is equal to the trace of $A.$

Therefore,

$$


\lambda_1+\lambda_2 = \textrm{tr}(A)= 9+(-6)=3.


$$

### The Cayley-Hamilton Theorem

The **Cayley-Hamilton theorem** states the following:

*Let $A$ be an $\,n \!\times\! n$ matrix whose characteristic polynomial is*

$$


p(\lambda) = \textrm{det}(A-\lambda I) = (-1)^n\lambda^n + c_{n-1}\lambda^{n-1}+\cdots+c_1\lambda + c_0.


$$

*Then, the matrix $A$ is a solution of the characteristic equation $p(\lambda) = 0$.*

That is to say, if we substitute $A$ into the characteristic polynomial $p(\lambda)$, taking $A^0 = I,$ then we have

$$


p(A) = (-1)^nA^n + c_{n-1}A^{n-1}+\cdots+c_1A + c_0I = O,


$$

where $O$ is the zero-matrix.

For example, according to this theorem, for the matrix

$$


[\begin{aligned}−8 & −9 \\ 6 & 7\end{aligned}]


$$

whose characteristic polynomial is

$$


p(\lambda)=\lambda^2 +\lambda -2,


$$

we have

$$


p(A) = A^2 +A -2I =O.


$$

### Example: Expressing a Power of a Matrix as a Linear Combination of Smaller Powers

#### Question

Let $A$ be a $2\times 2$ matrix such that $\textrm{tr}(A)=-4$ and $\textrm{det}(A)=-18.$ If $A^2 = xA + yI$ for constants $x$ and $y,$ then find the value of $x+y.$

#### Explanation

The characteristic polynomial of $A$ is given by

$$


p(\lambda)=\lambda^2-\textrm{tr}(A)\lambda+\textrm{det}(A).


$$

Therefore, using the Cayley-Hamilton theorem, we obtain

$$


\begin{aligned}𝑝(𝐴) & =𝑂 \\ 𝐴^{2}−tr(𝐴)𝐴+det(𝐴)𝐼 & =𝑂 \\ 𝐴^{2} & =tr(𝐴)𝐴−det(𝐴)𝐼 \\ 𝐴^{2} & =−4𝐴+18𝐼.\end{aligned}


$$

Therefore, $x+y = -4+18 = 14.$

### Example: Expressing the Inverse of a Matrix as a Linear Combination of Its Powers

#### Question

Given that $[\begin{aligned}−8 & −9 \\ 6 & 7\end{aligned}]$ and $A^{-1}=pI+qA$, find the value of $p+q.$

#### Explanation

Let's find the characteristic equation $\textrm{det}(A-\lambda I)=0\mathbin{:}$

$$


\begin{aligned}det(𝐴−𝜆𝐼) & =0 \\ \begin{aligned}−8−𝜆 & −9 \\ 6 & 7−𝜆\end{aligned} & =0 \\ (−8−𝜆)(7−𝜆)+54 & =0 \\ 𝜆^{2}+𝜆−2 & =0\end{aligned}


$$

Using the Cayley-Hamilton theorem, we have that

$$


\begin{aligned}𝐴^{2}+𝐴−2𝐼 & =𝑂.\end{aligned}


$$

Since $A$ is invertible, we can multiply this equation by $A^{-1}\mathbin{:}$

$$


\begin{aligned}𝐴^{−1}(𝐴^{2}+𝐴−2𝐼) & =𝑂 \\ 𝐴+𝐼−2𝐴^{−1} & =𝑂 \\ 𝐴^{−1} & =\frac{1}{2}𝐴+\frac{1}{2}𝐼\end{aligned}


$$

Therefore, $p=\dfrac{1}{2},$ $q=\dfrac{1}{2},$ and

$$


p+q=\dfrac{1}{2}+\dfrac{1}{2}=1.


$$

### Using the Cayley-Hamilton Theorem to Quickly Evaluate a Matrix Polynomial

If we want to evaluate a high-degree polynomial for a given matrix input, it can take a lot of time. For example, suppose we wanted to evaluate the polynomial

$$


f(x) = x^{10} - 5x^9 - 2x^8 + x + 2


$$

for the input $[\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}]$ Computing the $10$th power of this matrix would be a lot of work!

Luckily, there is a way to speed up the process. The trick is to use Cayley-Hamilton theorem, which tells us that every matrix is a solution to its characteristic equation.

For the given matrix $[\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}]$ the characteristic polynomial is

$$


\begin{aligned}𝑝(𝜆) & =det(𝐴−𝜆𝐼) \\ & =\begin{aligned}1−𝜆 & 2 \\ 3 & 4−𝜆\end{aligned} \\ & =(1−𝜆)(4−𝜆)−6 \\ & =𝜆^{2}−5𝜆−2,\end{aligned}


$$

so the Cayley-Hamilton theorem tells us that

$$


p(A) = A^2 - 5A - 2I = 0.


$$

Now, observe that the polynomial $f(x)$ can be written as

$$


\begin{aligned}𝑓(𝑥) & =𝑥^{10}−5𝑥^{9}−2𝑥^{8}+𝑥+2 \\ & =𝑥^{8}(𝑥^{2}−5𝑥−2)+𝑥+2 \\ & =𝑥^{8}𝑝(𝑥)+𝑥+2.\end{aligned}


$$

Then we have

$$


f(A) = A^8 p(A) + A + 2I,


$$

and because $p(A) = 0,$ we conclude that

$$


\begin{aligned}𝑓(𝐴) & =𝐴^{8}⋅0+𝐴+2𝐼 \\ & =0+𝐴+2𝐼 \\ & =𝐴+2𝐼.\end{aligned}


$$

Now, the computation is much faster:

$$


\begin{aligned}𝑓(𝐴) & =𝐴+2𝐼 \\ & =[\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}]+2[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}3 & 2 \\ 3 & 6\end{aligned}]\end{aligned}


$$

**Note:** Other times, it may not be so obvious how to group the terms of $f(x)$ to reveal $p(x).$ In the general case, it's best to divide $f(x)$ by $p(x)$ using long division, and use the result

$$


f(x) = q(x) p(x) + r(x)


$$

where $q(x)$ is the quotient and $r(x)$ is the remainder. Let's see an example of this.

### Example: Evaluating a Matrix Polynomial Using the Cayley-Hamilton Theorem

#### Question

Given that $[\begin{aligned}4 & −5 \\ 3 & −4\end{aligned}]$ and $f(x) = x^{12} -x^{10} +2x-1,$ find $f(A).$

#### Explanation

Let's start by finding the characteristic polynomial $p(\lambda)\mathbin{:}$

$$


\begin{aligned}𝑝(𝜆) & =det(𝐴−𝜆𝐼) \\ & =\begin{aligned}4−𝜆 & −5 \\ 3 & −4−𝜆\end{aligned} \\ & =(4−𝜆)(−4−𝜆)+15 \\ & =𝜆^{2}−1\end{aligned}


$$

Now, let's divide $f(x)$ by $p(x)$ using long division:

Therefore, we can write $f(x)$ as

$$


\begin{aligned}𝑓(𝑥) & =𝑞(𝑥)𝑝(𝑥)+𝑟(𝑥) \\ & =𝑥^{10}(𝑥^{2}−1)+(2𝑥−1),\end{aligned}


$$

where $q(x) = x^{10}.$ Replacing $x$ with $A,$ we have

$$


f(A) = q(A)p(A)+(2A-I).


$$

According to the Cayley-Hamilton theorem, we have $p(A)=O.$ Therefore,

$$


\begin{aligned}𝑓(𝐴) & =𝑞(𝐴)𝑝(𝐴)+(2𝐴−𝐼) \\ & =𝑞(𝐴)⋅𝑂+(2𝐴−𝐼) \\ & =2𝐴−𝐼 \\ & =2[\begin{aligned}4 & −5 \\ 3 & −4\end{aligned}]−[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}8 & −10 \\ 6 & −8\end{aligned}]−[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}] \\ & =[\begin{aligned}7 & −10 \\ 6 & −9\end{aligned}].\end{aligned}


$$
