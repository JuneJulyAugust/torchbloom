# Finding Recurrence Relations for the Coefficients of a Frobenius Solution

Source: https://www.mathacademy.com/topics/6727?courseId=61
Topic ID: 6727

## Prerequisites

- [The Method of Frobenius](./2523-the-method-of-frobenius.md)

## Lesson

### Introduction

Previously, we considered the differential equation

$$


4xy'' + 2y' - y = 0,


$$

and, using the Frobenius trial solution

$$


y=\sum_{n=0}^\infty a_nx^{\lambda+n},


$$

we found that the possible values of $\lambda$ are $\lambda=0$ and $\lambda=\dfrac12.$ Since $\lambda\in(0,1),$ we take $\lambda=\dfrac12.$

Let's now determine a **recurrence relation** for the coefficients of a Frobenius series solution of our previous example, for the case $\lambda \in (0,1).$

Rewriting each term of the ODE as a power series (with the $\color{blue}n=0$ term isolated), we obtained

$$


\begin{aligned}4𝑥𝑦^{″} & =4(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆−1}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}4((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}𝑥^{𝜆+𝑛−1}, \\ 2𝑦^{′} & =2𝜆𝑎_{0}𝑥^{𝜆−1}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}2(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−1}, \\ −𝑦 & =−\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛−1}𝑥^{𝜆+𝑛−1}.\end{aligned}


$$

We continue from this point.

**Step 4**: Consolidate all the series into a single series that is equal to $0.$

Since we already handled the ${\color{blue}n=0}$ terms in the previous slide to obtain the indicial equation, we focus only on the coefficients of the $n\geq 1$ terms here.

For $n\geq 1,$ collecting like powers of $x$ gives

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[4((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}+2(𝜆+𝑛)𝑎_{𝑛}−𝑎_{𝑛−1}]𝑥^{𝜆+𝑛−1} & = \\ 𝑥^{𝜆−1}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[4((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}+2(𝜆+𝑛)𝑎_{𝑛}−𝑎_{𝑛−1}]𝑥^{𝑛} & = \\ 𝑥^{𝜆−1}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(4(𝜆+𝑛)^{2}−2(𝜆+𝑛))𝑎_{𝑛}−𝑎_{𝑛−1}]𝑥^{𝑛} & .\end{aligned}


$$

**Step 5**: Set the coefficients of the series equal to $0.$

For each $n\geq 1,$ the coefficient of $x^n$ must be $0,$ so

$$


\begin{aligned}(4(𝜆+𝑛)^{2}−2(𝜆+𝑛))𝑎_{𝑛}−𝑎_{𝑛−1} & =0 \\ (𝜆+𝑛)(4(𝜆+𝑛)−2)𝑎_{𝑛}−𝑎_{𝑛−1} & =0.\end{aligned}


$$

Finally, since we are working in the case $\lambda\in(0,1),$ we substitute $\lambda=\dfrac12$ and solve for $a_n{:}$

$$


\begin{aligned}(\frac{1}{2}+𝑛)(4(\frac{1}{2}+𝑛)−2)𝑎_{𝑛} & =𝑎_{𝑛−1} \\ 4𝑛(𝑛+\frac{1}{2})𝑎_{𝑛} & =𝑎_{𝑛−1} \\ 2𝑛(2𝑛+1)𝑎_{𝑛} & =𝑎_{𝑛−1} \\ 𝑎_{𝑛} & =\frac{𝑎_{𝑛−1}}{2𝑛(2𝑛+1)},\,𝑛≥1.\end{aligned}


$$

### Example: Determining a Recurrence Formula for the Coefficients of a Frobenius Series Solution: Constant Coefficients of y and y'

#### Question

$$


10x^2y'' + 7xy' + (3x-1)y = 0


$$

Let $\displaystyle y = x^\lambda \sum_{n=0}^\infty a_nx^n$ be a Frobenius series solution about the regular singular point $x=0$ of the differential equation above. Find $f(n),$ given that $\lambda\in(0,1)$ and the recurrence relation for $a_n$ can be written as

$$


a_n = -\dfrac{3a_{n-1}}{f(n)}, \qquad n \geq 1.


$$

**

#### Explanation

If $x=0$ is a regular singular point of a second-order homogeneous linear differential equation, then the method of Frobenius states that there is at least one solution of the form

$$


y = x^\lambda \sum_{n=0}^\infty a_nx^n,


$$

where $\lambda$ and $a_n$ for $n=0,1,2,\ldots$ are constants.

Substituting this solution and its derivatives into the ODE, collecting like terms, and setting coefficients equal to zero, we obtain:

- the indicial equation from the coefficients of the $n=0$ term for arbitrary $a_0,$ and

- a recurrence formula from the coefficients of the $n \geq 1$ terms.

We are given the three terms of the ODE as power series with the $\color{blue}n=0$ term isolated in each.

$$


\begin{aligned}10𝑥^{2}𝑦^{″} & =10(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}10((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}𝑥^{𝜆+𝑛}, \\ 7𝑥𝑦^{′} & =7𝜆𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}7(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛}, \\ (3𝑥−1)𝑦 & =−𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(3𝑎_{𝑛−1}−𝑎_{𝑛})𝑥^{𝜆+𝑛}.\end{aligned}


$$

Now, we continue from this point.

****: Consolidate all the series into a single series that is equal to $0.$

Collecting the terms for ${\color{blue}n=0},$ we have

$$


\begin{aligned}10(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆}+7𝜆𝑎_{0}𝑥^{𝜆}−𝑎_{0}𝑥^{𝜆} & = \\ (10𝜆^{2}−10𝜆+7𝜆−1)𝑎_{0}𝑥^{𝜆} & = \\ (10𝜆^{2}−3𝜆−1)𝑎_{0}𝑥^{𝜆}. & \end{aligned}


$$

Similarly, collecting terms for $n\geq 1,$ we have

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[10((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}+7(𝜆+𝑛)𝑎_{𝑛}+(3𝑎_{𝑛−1}−𝑎_{𝑛})]𝑥^{𝜆+𝑛} & = \\ \underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[10(𝜆+𝑛)^{2}𝑎_{𝑛}−3(𝜆+𝑛)𝑎_{𝑛}−𝑎_{𝑛}+3𝑎_{𝑛−1}]𝑥^{𝜆+𝑛} & = \\ 𝑥^{𝜆}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(10(𝜆+𝑛)^{2}−3(𝜆+𝑛)−1)𝑎_{𝑛}+3𝑎_{𝑛−1}]𝑥^{𝑛} & .\end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}(10𝜆^{2}−3𝜆−1)𝑎_{0}𝑥^{𝜆}+𝑥^{𝜆}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(10(𝜆+𝑛)^{2}−3(𝜆+𝑛)−1)𝑎_{𝑛}+3𝑎_{𝑛−1}]𝑥^{𝑛} & =0 \\ (10𝜆^{2}−3𝜆−1)𝑎_{0}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(10(𝜆+𝑛)^{2}−3(𝜆+𝑛)−1)𝑎_{𝑛}+3𝑎_{𝑛−1}]𝑥^{𝑛} & =0.\end{aligned}


$$

****: Set the coefficients of the series equal to $0.$

Setting the coefficients of the $n=0$ term equal to $0$ with arbitrary $a_0\neq0,$ we obtain the indicial equation:

$$


\begin{aligned}(10𝜆^{2}−3𝜆−1)𝑎_{0} & =0 \\ 10𝜆^{2}−3𝜆−1 & =0 \\ (2𝜆−1)(5𝜆+1) & =0 \\ 𝜆 & =−\frac{1}{5},\frac{1}{2}\end{aligned}


$$

Since we're interested in $\lambda\in(0,1),$ we take $\lambda=\dfrac12.$

Similarly, setting the coefficients of $x^n$ for $n \geq 1$ equal to $0,$ we obtain the following recurrence relation:

$$


\begin{aligned}(10(𝜆+𝑛)^{2}−3(𝜆+𝑛)−1)𝑎_{𝑛}+3𝑎_{𝑛−1} & =0 \\ (2(𝜆+𝑛)−1)(5(𝜆+𝑛)+1)𝑎_{𝑛}+3𝑎_{𝑛−1} & =0\end{aligned}


$$

Finally, we substitute $\lambda=\dfrac12$ into the above and solve for $a_n{:}$

$$


\begin{aligned}(2(\frac{1}{2}+𝑛)−1)(5(\frac{1}{2}+𝑛)+1)𝑎_{𝑛} & =−3𝑎_{𝑛−1} \\ 2𝑛(5𝑛+\frac{7}{2})𝑎_{𝑛} & =−3𝑎_{𝑛−1} \\ 𝑛(10𝑛+7)𝑎_{𝑛} & =−3𝑎_{𝑛−1} \\ 𝑎_{𝑛} & =−\frac{3𝑎_{𝑛−1}}{𝑛(10𝑛+7)}\end{aligned}


$$

Therefore, $f(n)=n(10n+7).$

### Example: Determining a Recurrence Formula for the Coefficients of a Frobenius Series Solution: Binomial Coefficient of y or y'

#### Question

$$


4x^2y'' + 3x(x+2)y' - 2y = 0


$$

Let $\displaystyle y = x^\lambda \sum_{n=0}^\infty a_nx^n$ be a Frobenius series solution about the regular singular point $x=0$ of the differential equation above. Find $f(n),$ given that $\lambda\in(0,1)$ and the recurrence relation for $a_n$ can be written as

$$


a_n = \dfrac{3(1-2n)}{f(n)}\,a_{n-1}, \qquad n \geq 1.


$$

**

#### Explanation

If $x=0$ is a regular singular point of a second-order homogeneous linear differential equation, then the method of Frobenius states that there is at least one solution of the form

$$


y = x^\lambda \sum_{n=0}^\infty a_nx^n,


$$

where $\lambda$ and $a_n$ for $n=0,1,2,\ldots$ are constants.

Substituting this solution and its derivatives into the ODE, collecting like terms, and setting coefficients equal to zero, we obtain:

- the indicial equation from the coefficients of the $n=0$ term for arbitrary $a_0,$ and

- a recurrence formula from the coefficients of the $n \geq 1$ terms.

We are given the three terms of the ODE as a power series with the $\color{blue}n=0$ term isolated in each.

$$


\begin{aligned}4𝑥^{2}𝑦^{″} & =4(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}4((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}𝑥^{𝜆+𝑛}, \\ 3𝑥(𝑥+2)𝑦^{′} & =6𝜆𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[3(𝜆+𝑛−1)𝑎_{𝑛−1}+6(𝜆+𝑛)𝑎_{𝑛}]𝑥^{𝜆+𝑛}, \\ −2𝑦 & =−2𝑎_{0}𝑥^{𝜆}−\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}2𝑎_{𝑛}𝑥^{𝜆+𝑛}.\end{aligned}


$$

Now, we continue from this point.

****: Consolidate all the series into a single series that is equal to $0.$

Collecting the terms for ${\color{blue}n=0},$ we have

$$


\begin{aligned}4(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆}+6𝜆𝑎_{0}𝑥^{𝜆}−2𝑎_{0}𝑥^{𝜆} & = \\ (4𝜆^{2}−4𝜆+6𝜆−2)𝑎_{0}𝑥^{𝜆} & = \\ 2(2𝜆^{2}+𝜆−1)𝑎_{0}𝑥^{𝜆}. & \end{aligned}


$$

Similarly, collecting terms for $n\geq 1,$ we obtain

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[4((𝜆+𝑛)^{2}−(𝜆+𝑛))+3(𝜆+𝑛−1)𝑎_{𝑛−1}+6(𝜆+𝑛)𝑎_{𝑛}−2𝑎_{𝑛}]𝑥^{𝜆+𝑛} & = \\ \underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[4(𝜆+𝑛)^{2}+2(𝜆+𝑛)𝑎_{𝑛}−2𝑎_{𝑛}+3(𝜆+𝑛−1)𝑎_{𝑛−1}]𝑥^{𝜆+𝑛} & = \\ 2𝑥^{𝜆}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(2(𝜆+𝑛)^{2}+(𝜆+𝑛)−1)𝑎_{𝑛}+\frac{3}{2}(𝜆+𝑛−1)𝑎_{𝑛−1}]𝑥^{𝑛} & .\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,2(2𝜆^{2}+𝜆−1)𝑎_{0}𝑥^{𝜆}+2𝑥^{𝜆}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(2(𝜆+𝑛)^{2}+(𝜆+𝑛)−1)𝑎_{𝑛}+\frac{3}{2}(𝜆+𝑛−1)𝑎_{𝑛−1}]𝑥^{𝑛} & =0 \\ (2𝜆^{2}+𝜆−1)𝑎_{0}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(2(𝜆+𝑛)^{2}+(𝜆+𝑛)−1)𝑎_{𝑛}+\frac{3}{2}(𝜆+𝑛−1)𝑎_{𝑛−1}]𝑥^{𝑛} & =0.\end{aligned}


$$

****: Set the coefficients of the series equal to $0.$

Setting the coefficient of the $n=0$ term equal to $0$ with arbitrary $a_0\neq0,$ we obtain the indicial equation:

$$


\begin{aligned}2𝜆^{2}+𝜆−1 & =0 \\ (𝜆+1)(2𝜆−1) & =0 \\ 𝜆 & =−1,\frac{1}{2}.\end{aligned}


$$

Since we're interested in $\lambda\in(0,1),$ we take $\lambda=\dfrac12.$

Similarly, setting the coefficients of $x^n$ for $n\geq1$ equal to $0,$ we obtain the following recurrence relation:

$$


\begin{aligned}(2(𝜆+𝑛)^{2}+(𝜆+𝑛)−1)𝑎_{𝑛}+\frac{3}{2}(𝜆+𝑛−1)𝑎_{𝑛−1} & =0 \\ ((𝜆+𝑛)+1)(2(𝜆+𝑛)−1)𝑎_{𝑛} & =−\frac{3}{2}(𝜆+𝑛−1)𝑎_{𝑛−1}\end{aligned}


$$

Substituting $\lambda=\dfrac12$ and solving for $a_n,$ we have

$$


\begin{aligned}((\frac{1}{2}+𝑛)+1)(2(\frac{1}{2}+𝑛)−1)𝑎_{𝑛} & =−\frac{3}{2}(\frac{1}{2}+𝑛−1)𝑎_{𝑛−1} \\ (𝑛+\frac{3}{2})(2𝑛)𝑎_{𝑛} & =−\frac{3}{2}(𝑛−\frac{1}{2})𝑎_{𝑛−1} \\ 𝑛(2𝑛+3)𝑎_{𝑛} & =\frac{3}{4}(1−2𝑛)𝑎_{𝑛−1} \\ 𝑎_{𝑛} & =\frac{3(1−2𝑛)}{4𝑛(2𝑛+3)}\,𝑎_{𝑛−1}.\end{aligned}


$$

Therefore, $f(n) = 4n(2n+3).$
