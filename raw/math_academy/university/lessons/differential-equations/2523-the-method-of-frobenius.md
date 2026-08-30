# The Method of Frobenius

Source: https://www.mathacademy.com/topics/2523?courseId=61
Topic ID: 2523

## Prerequisites

- [Regular Singular Points](./1880-regular-singular-points.md)

## Lesson

### Introduction

We now consider differential equations with **regular singular points** and how to find series solutions near them.

For simplicity, we will assume the regular singular point is at if a regular singular point occurs at then the change of variables translates it to the origin.

At an ordinary point, we often look for a solution as a usual power series, However, the coefficients in the differential equation are singular at a regular singular point, so a usual power series may fail to capture the behavior of a solution near the origin. Instead, we account for this by allowing the solution to start with a flexible exponent.

If is a regular singular point of a second-order homogeneous linear differential equation, then there is at least one solution of the form where and for are constants. This solution is valid in an interval for some number This is known as the **method of Frobenius**.

To evaluate the constants, we proceed as in the power series method. The derivatives of are and We substitute these into the differential equation, collect like terms, and set coefficients equal to zero:

- From the coefficient of the lowest power of (the term, with arbitrary), we obtain a quadratic equation in called the **indicial equation**.

- From the coefficients of the higher powers (), we obtain a **recurrence relation** for the coefficients

Let's demonstrate with a concrete example.

### A Worked Example

Consider the differential equation

$$


4xy'' + 2y' - y = 0.


$$

Let's find Frobenius series solutions about the regular singular point $x=0.$

**Step 1**: Write the solution $y$ as a Frobenius power series:

$$


y=x^\lambda\sum_{n=0}^\infty a_nx^n =\sum_{n=0}^\infty a_nx^{\lambda+n}.


$$

**Step 2**: Compute the derivatives $y'$ and $y''{:}$

$$


\begin{aligned}𝑦^{′} & =(\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝜆+𝑛})^{′}=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−1} \\ 𝑦^{″} & =(\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−1})^{′}=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛−1)(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−2}.\end{aligned}


$$

**Step 3**: Rewrite all the series in the equation so that they use the same index of summation, the powers of $x$ are the same, and the indices start at the same value.

The terms of the differential equation are

$$


\begin{aligned}4𝑥𝑦^{″} & =4𝑥⋅\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛−1)(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−2} \\ & =\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}4((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}𝑥^{𝜆+𝑛−1}, \\ 2𝑦^{′} & =2⋅\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−1} \\ & =\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}2(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−1}, \\ −𝑦 & =−\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝜆+𝑛}.\end{aligned}


$$

In the $y$ term, we change the index of the summation by writing $n=m-1.$ This gives

$$


-y=-\sum_{m=1}^\infty a_{m-1}x^{\lambda+m-1}.


$$

Then, replacing $m$ with $n$ gives

$$


-y=-\sum_{n=1}^\infty a_{n-1}x^{\lambda+n-1}.


$$

Now, isolating the $\color{blue}n=0$ terms for the other terms in the ODE, we have

$$


\begin{aligned}4𝑥𝑦^{″} & =4(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆−1}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}4((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}𝑥^{𝜆+𝑛−1}, \\ 2𝑦^{′} & =2𝜆𝑎_{0}𝑥^{𝜆−1}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}2(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−1}.\end{aligned}


$$

**Step 4**: Consolidate all the series into a single series that is equal to $0.$

Collecting the terms for ${\color{blue}n=0},$ we have

$$


\begin{aligned}4(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆−1}+2𝜆𝑎_{0}𝑥^{𝜆−1} & = \\ (4𝜆^{2}−4𝜆+2𝜆)𝑎_{0}𝑥^{𝜆−1} & = \\ (4𝜆^{2}−2𝜆)𝑎_{0}𝑥^{𝜆−1}. & \end{aligned}


$$

Similarly, collecting terms for $n\ge 1,$ we obtain an infinite series of the form

$$


\displaystyle x^{\lambda-1}\sum_{n=1}^\infty b_n(\lambda)x^n,


$$

for some $b_n(\lambda),$ $n\ge 1.$ Therefore, substituting into the homogeneous ODE, we have

$$


\begin{aligned}(4𝜆^{2}−2𝜆)𝑎_{0}𝑥^{𝜆−1}+𝑥^{𝜆−1}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛}(𝜆)𝑥^{𝑛} & =0 \\ 2(2𝜆^{2}−𝜆)𝑎_{0}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛}(𝜆)𝑥^{𝑛} & =0.\end{aligned}


$$

**Step 5**: Set the coefficients of the series equal to $0.$

Setting the coefficients of the $n=0$ term equal to $0$ with arbitrary $a_0\ne 0,$ we obtain the indicial equation:

$$


\begin{aligned}2(2𝜆^{2}−𝜆)𝑎_{0} & =0 \\ 2𝜆^{2}−𝜆 & =0.\end{aligned}


$$

Now, we can determine the possible values of $\lambda.$ Solving the indicial equation for the roots, we get

$$


\begin{aligned}2𝜆^{2}−𝜆 & =0 \\ 𝜆(2𝜆−1) & =0 \\ 𝜆 & =0,\frac{1}{2}.\end{aligned}


$$

Therefore, the Frobenius series solutions have the forms

$$


y_1(x)=\sum_{n=0}^\infty a_nx^n \qquad\text{and}\qquad y_2(x)=\sum_{n=0}^\infty a_nx^{n+1/2},


$$

where the constants $a_n$ are to be determined separately in each case from the recurrence relation.

### Example: Determining the Indicial Equation of an ODE

#### Question

$$


x^2y'' + x(x-3)y' - 6y = 0


$$

Find the indicial equation for a Frobenius series solution about the regular singular point $x=0$ of the differential equation above.

#### Explanation

If $x=0$ is a regular singular point of a second-order homogeneous linear differential equation, then the method of Frobenius states that there is at least one solution of the form

$$


y = x^\lambda \sum_{n=0}^\infty a_nx^n,


$$

where $\lambda$ and $a_n$ for $n=0,1,2,\ldots$ are constants.

Substituting this solution and its derivatives into the ODE, collecting like terms, and setting coefficients equal to zero, we obtain:

- the indicial equation from the coefficients of the $n=0$ term for arbitrary $a_0,$ and

- a recurrence formula from the coefficients of the $n \geq 1$ terms.

****: Write the solution $y$ as a Frobenius power series:

$$


y = x^\lambda \sum_{n=0}^\infty a_nx^n = \sum_{n=0}^\infty a_nx^{\lambda+n}


$$

****: Compute the derivatives $y'$ and $y''{:}$

$$


\begin{aligned}𝑦^{′} & =(\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝜆+𝑛})^{′}=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−1} \\ 𝑦^{″} & =(\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−1})^{′}=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛−1)(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−2}\end{aligned}


$$

****: Rewrite all the series in the equation so that they use the same index of summation, the powers of $x$ are the same, and the indices start at the same value.

The terms of the differential equation are

$$


\begin{aligned}𝑥^{2}𝑦^{″} & =𝑥^{2}⋅\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛−1)(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−2} \\ & =\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}𝑥^{𝜆+𝑛}, \\ 𝑥(𝑥−3)𝑦^{′} & =(𝑥^{2}−3𝑥)⋅\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛−1} \\ & =\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛+1}−\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}3(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛}, \\ −6𝑦 & =−\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}6𝑎_{𝑛}𝑥^{𝜆+𝑛}.\end{aligned}


$$

In the first sum of the $y'$ term, we change the index of the summation by writing $m=n+1.$ This gives

$$


x(x-3)y' = \sum_{m=1}^\infty (\lambda+m-1)a_{m-1}x^{\lambda+m} - \sum_{n=0}^\infty 3(\lambda+n)a_nx^{\lambda+n}.


$$

Then, replacing $m$ with $n$ (since it does not matter which letter we use) and isolating the ${\color{blue}n=0}$ term gives

$$


\begin{aligned}𝑥(𝑥−3)𝑦^{′} & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(𝜆+𝑛−1)𝑎_{𝑛−1}𝑥^{𝜆+𝑛}−\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}3(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(𝜆+𝑛−1)𝑎_{𝑛−1}𝑥^{𝜆+𝑛}−3𝜆𝑎_{0}𝑥^{𝜆}−\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}3(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛} \\ & =−3𝜆𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(𝜆+𝑛−1)𝑎_{𝑛−1}−3(𝜆+𝑛)𝑎_{𝑛}]𝑥^{𝜆+𝑛}.\end{aligned}


$$

Similarly, isolating the ${\color{blue}n=0}$ terms for the other terms in the ODE, we have

$$


\begin{aligned}𝑥^{2}𝑦^{″} & =(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}𝑥^{𝜆+𝑛}, \\ −6𝑦 & =−6𝑎_{0}𝑥^{𝜆}−\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}6𝑎_{𝑛}𝑥^{𝜆+𝑛}.\end{aligned}


$$

****: Consolidate all the series into a single series that is equal to $0.$

Collecting the terms for ${\color{blue}n=0},$ we have

$$


\begin{aligned}(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆}−3𝜆𝑎_{0}𝑥^{𝜆}−6𝑎_{0}𝑥^{𝜆} & = \\ (𝜆^{2}−𝜆−3𝜆−6)𝑎_{0}𝑥^{𝜆} & = \\ (𝜆^{2}−4𝜆−6)𝑎_{0}𝑥^{𝜆}. & \end{aligned}


$$

Similarly, collecting terms for $n\geq 1,$ we obtain an infinite series of the form $\displaystyle x^{\lambda}\sum_{n=1}^\infty b_n(\lambda)x^n,$ for some $b_n(\lambda),$ $n\geq 1.$ Therefore, substituting into the homogeneous ODE, we have

$$


\begin{aligned}(𝜆^{2}−4𝜆−6)𝑎_{0}𝑥^{𝜆}+𝑥^{𝜆}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛}(𝜆)𝑥^{𝑛} & =0 \\ (𝜆^{2}−4𝜆−6)𝑎_{0}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛}(𝜆)𝑥^{𝑛} & =0.\end{aligned}


$$

****: Set the coefficients of the series equal to $0.$

Setting the coefficient of the $n=0$ term equal to $0$ with arbitrary $a_0\neq0,$ we obtain the indicial equation:

$$


\begin{aligned}(𝜆^{2}−4𝜆−6)𝑎_{0} & =0 \\ 𝜆^{2}−4𝜆−6 & =0\end{aligned}


$$

### Example: Determining a Frobenius Series Solution

#### Question

$$


12x^2y'' + 7xy' + (2x-3)y = 0


$$

Find the possible values of $\lambda$ for a Frobenius series solution about the regular singular point $x=0$ of the differential equation above, and write the corresponding Frobenius series forms.

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


\begin{aligned}12𝑥^{2}𝑦^{″} & =12(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}12((𝜆+𝑛)^{2}−(𝜆+𝑛))𝑎_{𝑛}𝑥^{𝜆+𝑛}, \\ 7𝑥𝑦^{′} & =7𝜆𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}7(𝜆+𝑛)𝑎_{𝑛}𝑥^{𝜆+𝑛}, \\ (2𝑥−3)𝑦 & =−3𝑎_{0}𝑥^{𝜆}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(2𝑎_{𝑛−1}−3𝑎_{𝑛})𝑥^{𝜆+𝑛}.\end{aligned}


$$

Now, we continue from this point.

****: Consolidate all the series into a single series that is equal to $0.$

Collecting the terms for ${\color{blue}n=0},$ we have

$$


\begin{aligned}12(𝜆^{2}−𝜆)𝑎_{0}𝑥^{𝜆}+7𝜆𝑎_{0}𝑥^{𝜆}−3𝑎_{0}𝑥^{𝜆} & = \\ (12𝜆^{2}−12𝜆+7𝜆−3)𝑎_{0}𝑥^{𝜆} & = \\ (12𝜆^{2}−5𝜆−3)𝑎_{0}𝑥^{𝜆}. & \end{aligned}


$$

Similarly, collecting terms for $n\geq 1,$ we obtain an infinite series of the form $\displaystyle x^{\lambda}\sum_{n=1}^\infty b_n(\lambda)x^n,$ for some $b_n(\lambda),$ $n \geq 1.$ Therefore, substituting into the homogeneous ODE, we have

$$


\begin{aligned}(12𝜆^{2}−5𝜆−3)𝑎_{0}𝑥^{𝜆}+𝑥^{𝜆}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛}(𝜆)𝑥^{𝑛} & =0 \\ (12𝜆^{2}−5𝜆−3)𝑎_{0}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛}(𝜆)𝑥^{𝑛} & =0.\end{aligned}


$$

****: Set the coefficients of the series equal to $0.$

Setting the coefficient of the $n=0$ term equal to $0$ with arbitrary $a_0\neq0,$ we obtain the indicial equation:

$$


\begin{aligned}(12𝜆^{2}−5𝜆−3)𝑎_{0} & =0 \\ 12𝜆^{2}−5𝜆−3 & =0\end{aligned}


$$

Now, we can determine the possible values of $\lambda.$ Solving the indicial equation for the roots, we get

$$


\begin{aligned}12𝜆^{2}−5𝜆−3 & =0 \\ (4𝜆−3)(3𝜆+1) & =0 \\ 𝜆 & =−\frac{1}{3},\frac{3}{4}\end{aligned}


$$

Therefore, the two Frobenius series solutions have the forms

$$


\begin{aligned}𝑦(𝑥)=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛−1/3}\,and\,𝑦(𝑥)=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛+3/4},\end{aligned}


$$

where the constants $a_n$ are to be determined separately in each of the two cases.
