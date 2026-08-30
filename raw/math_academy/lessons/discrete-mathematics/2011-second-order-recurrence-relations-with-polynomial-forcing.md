# Second-Order Recurrence Relations with Polynomial Forcing

Source: https://www.mathacademy.com/topics/2011?courseId=109
Topic ID: 2011

## Prerequisites

- [Second-Order Homogeneous Recurrence Relations: Characteristic Equations with Repeated Roots](./1916-second-order-homogeneous-recurrence-relations-characteristic-equations-with-repeated-roots.md)
- [Second-Order Homogeneous Recurrence Relations: Characteristic Equations with Complex Roots](./2008-second-order-homogeneous-recurrence-relations-characteristic-equations-with-complex-roots.md)

## Lesson

### Introduction

Recall that a second-order linear homogeneous recurrence relation takes the form

$$



a_n + P \cdot a_{n-1} + Q\cdot a_{n-2} = 0



$$

where $P$ and $Q$ are constants.

A **second-order linear inhomogeneous recurrence relation** is a recurrence relation that can be written as

$$



a_n + P \cdot a_{n-1} + Q \cdot a_{n-2} = f(n).



$$

The function $f(n)$ is sometimes called a **forcing function.**

For example, let's consider the following second-order recurrence relation:

$$



a_n + 5 a_{n-1} + 6 a_{n-2} = n^2+n+1



$$

This equation is inhomogeneous because the right-hand side $f(n) = n^2+n+1,$ which is different from zero.

In this case, we say that the recurrence relation is subject to **polynomial forcing** because $f(n)$ is a polynomial.

### Solving Second-Order Inhomogeneous Recurrence Relations With Polynomial Forcing

To find the general solution to a linear inhomogeneous recurrence relation, we perform the following steps:

- **Step 1:** Find the **complementary solution** $a^{(h)}_n$ of the associated homogeneous equation.

- **Step 2:** Find a **particular solution** $a^{(p)}_n$ of the inhomogeneous equation.

- **Step 3:** Write the general solution as the sum of the complementary and particular solutions:

To illustrate, let's find the general solution to the following inhomogeneous recurrence relation:

$$



a_n + 5 a_{n-1} + 6 a_{n-2} = 2



$$

**Step 1:** Find the complementary solution.

First, we find the solution $a^{(h)}_n$ of the associated homogeneous recurrence relation:

$$



a_n + 5 a_{n-1} + 6 a_{n-2} = 0



$$

The characteristic equation is

$$



\begin{aligned}𝜆^{2}+5𝜆+6 & =0 \\ (𝜆+3)(𝜆+2) & =0,\end{aligned}



$$

so $\lambda=-3$ or $\lambda=-2.$ Consequently, the complementary solution is

$$



a_n^{(h)} = A \cdot (-3)^n + B \cdot (-2)^n.



$$

**Step 2:** Find a particular solution that satisfies the recurrence relation.

Since the right-hand side is given by the constant polynomial $f(n)=2,$ the particular solution will also be a constant polynomial. So, we assume

$$



a^{(p)}_n=\alpha,



$$

where $\alpha$ is to be determined. Since $a_n^{(p)}$ does not depend on $n,$ we also have

$$



a_{n-1}^{(p)} = a_{n-2}^{(p)} = \alpha.



$$

To find the value of $\alpha,$ we substitute the particular solution into the recurrence relation:

$$



\alpha + 5\alpha + 6\alpha = 2 \qquad \Longrightarrow \qquad \alpha = \dfrac{1}{6}.



$$

Therefore, the particular solution is

$$



a_n^{(p)} = \dfrac{1}{6}.



$$

**Step 3:** Write down the general solution.

The general solution is the sum of the complementary and particular solutions:

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}^{}+𝑎_{(𝑝)𝑛}^{} \\ & =𝐴⋅(−3)^{𝑛}+𝐵⋅(−2)^{𝑛}+\frac{1}{6}.\end{aligned}



$$

### Example: Solving a Second-Order Recurrence Relation With Constant Forcing

#### Question

Find the general solution to the difference equation

$$



a_n - 6a_{n-1} + 9a_{n-2} = 8.



$$

#### Explanation

First, we need to find the general solution $a_n^{(h)}$ of the associated homogeneous difference equation, given by

$$



a_n - 6a_{n-1} + 9a_{n-2} = 0.



$$

Writing down and solving the characteristic equation gives

$$



\begin{aligned}𝜆^{2}−6𝜆+9 & =0 \\ (𝜆−3)^{2} & =0.\end{aligned}



$$

So $\lambda = 3$ is a repeated root, and therefore

$$



a_n^{(h)} = A \cdot 3^n + B n \cdot 3^n.



$$

We now need to find the particular solution $a_n^{(p)}$ of the original difference equation.

The right-hand side of the inhomogeneous equation is a polynomial of degree $0.$ Therefore, we assume that the particular solution is also a polynomial of degree $0,$ i.e.

$$



a_n^{(p)}=\alpha



$$

where $\alpha$ is a constant to be determined. Since $a_n^{(p)}$ does not depend on $n,$ we also have

$$



a_{n-1}^{(p)} = a_{n-2}^{(p)} = \alpha.



$$

To find the value of $\alpha,$ we substitute the particular solution into the difference equation:

$$



\alpha - 6\alpha + 9\alpha = 8 \qquad \Longrightarrow \qquad \alpha = 2



$$

Therefore,

$$



a_n^{(p)} = 2.



$$

Finally, the general solution is given by

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}^{}+𝑎_{(𝑝)𝑛}^{} \\ & =𝐴⋅3^{𝑛}+𝐵𝑛⋅3^{𝑛}+2.\end{aligned}



$$

### Example: Solving a Second-Order Recurrence Relation With Linear Forcing

#### Question

Consider the difference equation

$$



a_n - 2a_{n-1} - 8a_{n-2} = 9n .



$$

Given that the associated homogeneous difference equation has the general solution

$$



a_n^{(h)} = A \cdot (-2)^n + B \cdot 4^n,



$$

find the particular solution $a_n^{(p)}$ of the inhomogeneous equation.

#### Explanation

The right-hand side of the inhomogeneous difference equation is a polynomial of degree $1.$ Therefore, we assume that the particular solution is also a polynomial of degree $1,$ i.e.

$$



a_{n}^{(p)} = \alpha n + \beta



$$

where $\alpha$ and $\beta$ are constants to be determined. As a result,

$$



a_{n-1}^{(p)} = \alpha(n-1) + \beta, \qquad a_{n-2}^{(p)} = \alpha(n-2) + \beta.



$$

To find the values of $\alpha$ and $\beta,$ we substitute the particular solution into the difference equation:

$$



\big[ \alpha n + \beta \big] - 2\big[ \alpha (n-1) + \beta \big] - 8\big[ \alpha (n-2) + \beta \big] = 9n



$$

Grouping the terms on the left-hand side gives:

$$



-9\alpha n + (18\alpha - 9\beta) = 9n



$$

Equating the coefficients, we get the following system of equations:

$$



\begin{aligned}\begin{aligned}−9𝛼=9\, & (equating the coefficients of\,\,𝑛) \\ 18𝛼−9𝛽=0\, & (equating the constants)\end{aligned}\end{aligned}



$$

Solving this system gives $\alpha = -1, \,\beta=-2.$

Therefore, the particular solution is

$$



a_n^{(p)} = - n - 2.



$$

### Example: Solving a Second-Order Recurrence Relation With Polynomial Forcing Given Some Initial Values

#### Question

Solve the difference equation

$$



a_n + 4a_{n-1} + 4a_{n-2} = 18, \quad a_0 = 1, \quad a_1 = -2.



$$

#### Explanation

First, we need to find the general solution $a_n^{(h)}$ of the associated homogeneous difference equation

$$



a_n + 4a_{n-1} + 4a_{n-2} = 0.



$$

Writing down and solving the characteristic equation gives

$$



\begin{aligned}𝜆^{2}+4𝜆+4 & =0 \\ (𝜆+2)^{2} & =0.\end{aligned}



$$

So $\lambda = -2$ is a repeated root, and therefore

$$



a_n^{(h)} = A \cdot (-2)^n + B n \cdot (-2)^n.



$$

We now need to find the particular solution $a_n^{(p)}$ of the original difference equation.

The right-hand side of the inhomogeneous equation is a polynomial of degree $0.$ Therefore, we assume that the particular solution is also a polynomial of degree $0,$ i.e.

$$



a_n^{(p)} = \alpha



$$

where $\alpha$ is a constant to be determined. Since $a_n^{(p)}$ does not depend on $n,$ we also have

$$



a_{n-1}^{(p)} = a_{n-2}^{(p)} = \alpha.



$$

To find the value of $\alpha,$ we substitute the particular solution into the difference equation:

$$



\alpha + 4\alpha + 4\alpha = 18 \qquad \Longrightarrow \qquad \alpha = 2



$$

Therefore, $a_n^{(p)} = 2$ and

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}^{}+𝑎_{(𝑝)𝑛}^{} \\ & =𝐴⋅(−2)^{𝑛}+𝐵𝑛⋅(−2)^{𝑛}+2.\end{aligned}



$$

Finally, we find the constants $A$ and $B$ by substituting the initial values.

- Substituting $a_0 = 1$ into the general solution gives

- Substituting $a_1 = -2$ and $A = -1$ into the general solution gives

Therefore, the solution to the difference equation is

$$



\begin{aligned}𝑎_{𝑛} & =(−1)⋅(−2)^{𝑛}+3𝑛⋅(−2)^{𝑛}+2 \\ & =(−2)^{𝑛}(3𝑛−1)+2.\end{aligned}



$$
