# First-Order Recurrence Relations With Polynomial Forcing

Source: https://www.mathacademy.com/topics/5374?courseId=109
Topic ID: 5374

## Prerequisites

- [Solving Systems of Equations Using Back Substitution](./1047-solving-systems-of-equations-using-back-substitution.md)
- [First-Order Recurrence Relations](./1915-first-order-recurrence-relations.md)

## Lesson

### Introduction

Recall that a linear recurrence relation (with constant coefficients) is **homogeneous** if the recurrence involves only previous terms of the sequence.

In other words, the linear recurrence relation

$$



a_n = s_1a_{n-1} + s_2a_{n-2} + \ldots + s_ka_{n-k} + g(n)



$$

(where $s_i$ are constants) is homogeneous if $g(n) =0$ for all $n\geq 1.$

A **first-order linear inhomogeneous recurrence relation** is a recurrence relation that can be written as

$$



a_n + \lambda a_{n-1} = f(n)



$$

where the function $f(n)$ is often called a **forcing function.**

For example, let's consider the following first-order recurrence relation:

$$



a_n -3a_{n-1} = 4n+6



$$

The equation is inhomogeneous because the right-hand side $f(n)=4n+6$ is different from zero.

In this case, the recurrence relation is subject to **polynomial forcing** because the forcing function $f(n)$ is a polynomial.

In this lesson, we'll learn how to construct general solutions to first-order linear inhomogeneous recurrence relations subject to polynomial forcing.

### Solving First-Order Inhomogeneous Recurrence Relations

To find the general solution to an inhomogeneous recurrence relation, we perform the following steps:

- **Step 1:** Find the general solution $a_n^{(h)}$ of the associated homogeneous recurrence relation.

- **Step 2:** Find a particular solution $a_n^{(p)}$ to the inhomogeneous recurrence relation.

- **Step 3:** Find the general solution of the inhomogeneous recurrence relation by adding the general solution of the homogeneous equation and the particular solution to the inhomogeneous equation:

To illustrate, let's find the general solution to the following recurrence relation:

$$



a_n = -2a_{n-1} + 6, \qquad n\geq 2



$$

We proceed as follows:

- **Step 1:** Find the general solution $a_n^{(h)}$ of the associated homogeneous recurrence relation. The associated homogeneous recurrence relation is and this has the general solution The general solution of the homogeneous equation is called the **complementary solution** or **complementary function.**

- **Step 2:** Find the particular solution $a_n^{(p)}$ that satisfies the inhomogeneous recurrence relation. Since the inhomogeneous function $g(n)=6$ is a polynomial of degree $0,$ we assume the particular solution is also a polynomial of degree $0,$ i.e. where $\alpha$ is a constant. Since $a_n^{(p)}$ does not depend on $n,$ we also have $a_{n-1}^{(p)} = \alpha.$ Substituting the above into the original relation, we obtain Therefore, the particular solution is

- **Step 3:** Find the general solution. To find the general solution, we simply sum $a_n^{(h)}$ and $a_n^{(p)}.$ Therefore, our general solution is

Finally, note that if we're also given the first term of the recurrence relation, we can use this information to find the constant $A.$ We'll see an example of this later in the lesson.

### Example: Solving First-Order Recurrence Relations With Constant Forcing

#### Question

Consider the recurrence relation

$$



a_n = -4a_{n-1}+10, \qquad n\geq 2.



$$

Find the general solution to this equation for $n\geq 1$.

#### Explanation

To find the general solution to a linear inhomogeneous recurrence relation, we perform the following steps:

- ****: Find the complementary solution $a_n^{(h)}$ of the associated homogeneous equation.

- ****: Find a particular solution $a_n^{(p)}$ of the inhomogeneous equation.

- ****: Write the general solution as the sum of the complementary and particular solutions:

We find the associated homogeneous equation by removing the inhomogeneous function from the relation:

$$



a_n =-4a_{n-1} + 10 \qquad\Rightarrow\qquad a_n^{(h)} = -4a_{n-1}^{(h)}.



$$

The general solution of a linear homogeneous recurrence relation $a_n = \lambda a_{n-1}$ is given by

$$



a_n = A\cdot\lambda^n,



$$

where $A$ is a constant.

So, the complementary solution of the associated homogeneous equation is

$$



a_n^{(h)} = A \cdot (-4)^n.



$$

Next, we find a particular solution to the inhomogeneous equation. Since the inhomogeneous function $g(n)=10$ is a polynomial of degree $0,$ we will try guessing that there is a particular solution which is also a polynomial of degree $0,$ i.e.

$$



a_n^{(p)} = \alpha,



$$

where $\alpha$ is a constant. Then, since $a_n^{(p)}$ does not depend on $n,$ we also have $a_{n-1}^{(p)} = \alpha.$

Substituting the above into the original relation, we obtain

$$



\begin{aligned}𝑎_{(𝑝)𝑛} & =−4𝑎_{(𝑝)𝑛−1}+10 \\ 𝑎_{(𝑝)𝑛}+4𝑎_{(𝑝)𝑛−1} & =10 \\ 𝛼+4𝛼 & =10 \\ 5𝛼 & =10 \\ 𝛼 & =2.\end{aligned}



$$

Therefore, a particular solution is

$$



a_n^{(p)} = 2.



$$

Finally, we write the general solution as the sum of the complementary and particular solutions. Therefore,

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}+𝑎_{(𝑝)𝑛} \\ & =𝐴⋅(−4)^{𝑛}+2.\end{aligned}



$$

### Example: Solving First-Order Recurrence Relations With Linear Forcing

#### Question

Consider the recurrence relation

$$



a_n = 2a_{n-1} +3n+1, \qquad n\geq 2.



$$

Given that the associated homogeneous recurrence relation has the general solution

$$



a_n^{(h)} = A \cdot 2^n, \qquad n\geq 1



$$

find the particular solution $a_n^{(p)}$ of the inhomogeneous equation.

#### Explanation

Since the inhomogeneous function $g(n)=3n+1$ is a polynomial of degree $1,$ we assume the particular solution is also a polynomial of degree $1,$ i.e.

$$



a_n^{(p)} = \alpha n+ \beta,



$$

where $\alpha$ and $\beta$ are constants. Then, we have

$$



\begin{aligned}𝑎_{(𝑝)𝑛−1} & =𝛼(𝑛−1)+𝛽 \\ & =𝛼𝑛−𝛼+𝛽.\end{aligned}



$$

Substituting the above into the original relation, we obtain

$$



\begin{aligned}𝑎_{(𝑝)𝑛} & =2𝑎_{(𝑝)𝑛−1}+3𝑛+1 \\ 𝑎_{(𝑝)𝑛}−2𝑎_{(𝑝)𝑛−1} & =3𝑛+1 \\ (𝛼𝑛+𝛽)−2(𝛼𝑛−𝛼+𝛽) & =3𝑛+1 \\ −𝛼𝑛+(2𝛼−𝛽) & =3𝑛+1.\end{aligned}



$$

Now, equating the coefficients of $n$ and constant terms, respectively, on both sides of the equation, we obtain the following system of equations:

$$



\begin{aligned}−𝛼=3 \\ 2𝛼−𝛽=1\end{aligned}



$$

Solving this system gives $\alpha=-3$ and $\beta=-7.$

Therefore, the particular solution is

$$



a_n^{(p)} = -3n - 7.



$$

### Example: Solving First-Order Recurrence Relations With Quadratic Forcing

#### Question

Consider the recurrence relation

$$



a_n = -6a_{n-1} -7n^2+19n, \qquad n\geq 2.



$$

Given that the associated homogeneous recurrence relation has the general solution

$$



a_n^{(h)} = A \cdot (-6)^n, \qquad n\geq 1



$$

find the particular solution $a_n^{(p)}$ of the inhomogeneous equation.

#### Explanation

Since the inhomogeneous function $g(n)= -7n^2+19n$ is a polynomial of degree $2,$ we assume the particular solution is also a polynomial of degree $2,$ i.e.

$$



a_n^{(p)} = \alpha n^2 + \beta n + \gamma,



$$

where $\alpha, \beta,$ and $\gamma$ are constants. Then, we have

$$



\begin{aligned}𝑎_{(𝑝)𝑛−1} & =𝛼(𝑛−1)^{2}+𝛽(𝑛−1)+𝛾 \\ & =𝛼𝑛^{2}−2𝛼𝑛+𝛼+𝛽𝑛−𝛽+𝛾 \\ & =𝛼𝑛^{2}+(𝛽−2𝛼)𝑛+(𝛼−𝛽+𝛾).\end{aligned}



$$

Substituting the above into the original relation, we obtain

$$



\begin{aligned}𝑎_{(𝑝)𝑛} & =−6𝑎_{(𝑝)𝑛−1}−7𝑛^{2}+19𝑛 \\ 𝑎_{(𝑝)𝑛}+6𝑎_{(𝑝)𝑛−1} & =−7𝑛^{2}+19𝑛 \\ (𝛼𝑛^{2}+𝛽𝑛+𝛾)+6(𝛼𝑛^{2}+(𝛽−2𝛼)𝑛+(𝛼−𝛽+𝛾)) & =−7𝑛^{2}+19𝑛 \\ 𝛼𝑛^{2}+𝛽𝑛+𝛾+6𝛼𝑛^{2}+6(𝛽−2𝛼)𝑛+6(𝛼−𝛽+𝛾) & =−7𝑛^{2}+19𝑛 \\ 7𝛼𝑛^{2}+(7𝛽−12𝛼)𝑛+(6𝛼−6𝛽+7𝛾) & =−7𝑛^{2}+19𝑛.\end{aligned}



$$

Now, equating the coefficients of $n^2, n,$ and constant terms, respectively, on both sides of the equation, we obtain the following system of equations:

$$



\begin{aligned}7𝛼=−7 \\ 7𝛽−12𝛼=19 \\ 6𝛼−6𝛽+7𝛾=0\end{aligned}



$$

Solving this system gives $\alpha=-1,$ $\beta=1,$ and $\gamma=\dfrac{12}7.$

Therefore, the particular solution is

$$



a_n^{(p)} = -n^2 + n+\dfrac{12}7.



$$

### Example: Solving First-Order Recurrence Relations Given Initial Values

#### Question

Consider the recurrence relation

$$



a_n = 2a_{n-1} + n + 1, \qquad a_1=0, \quad n \geq 2.



$$

Find the solution of this recurrence relation for $n \geq 1.$

#### Explanation

To find the general solution to a linear inhomogeneous recurrence relation, we perform the following steps:

- ****: Find the complementary solution $a_n^{(h)}$ of the associated homogeneous equation.

- ****: Find a particular solution $a_n^{(p)}$ of the inhomogeneous equation.

- ****: Write the general solution as the sum of the complementary and particular solutions:

We find the associated homogeneous equation by removing the inhomogeneous function from the relation:

$$



a_n = 2a_{n-1} + n+1 \qquad\Rightarrow\qquad a_n^{(h)} = 2a_{n-1}^{(h)}.



$$

The general solution of a linear homogeneous recurrence relation $a_n = \lambda a_{n-1}$ is given by

$$



a_n = A\cdot\lambda^n,



$$

where $A$ is a constant.

So, the complementary solution of the associated homogeneous equation is

$$



a_n^{(h)} = A \cdot 2^n.



$$

Next, we find a particular solution to the inhomogeneous equation. Since the inhomogeneous function $g(n)=n+1$ is a polynomial of order $1,$ we assume that the particular solution is also a polynomial of degree $1,$ i.e.

$$



a_n^{(p)} = \alpha n + \beta,



$$

where $\alpha$ and $\beta$ are constants. Then, we have

$$



\begin{aligned}𝑎_{(𝑝)𝑛−1} & =𝛼(𝑛−1)+𝛽 \\ & =𝛼𝑛−𝛼+𝛽.\end{aligned}



$$

Substituting the above into the original relation, we obtain

$$



\begin{aligned}𝑎_{(𝑝)𝑛} & =2𝑎_{(𝑝)𝑛−1}+𝑛+1 \\ 𝑎_{(𝑝)𝑛}−2𝑎_{(𝑝)𝑛−1} & =𝑛+1 \\ (𝛼𝑛+𝛽)−2(𝛼𝑛−𝛼+𝛽) & =𝑛+1 \\ 𝛼𝑛+𝛽−2𝛼𝑛+2𝛼−2𝛽 & =𝑛+1 \\ −𝛼𝑛+(2𝛼−𝛽) & =𝑛+1.\end{aligned}



$$

Now, equating the coefficients, we obtain the following system of equations:

$$



\begin{aligned}−𝛼=1 \\ 2𝛼−𝛽=1\end{aligned}



$$

Solving this system gives $\alpha=-1$ and $\beta=-3.$

Therefore, the particular solution is

$$



a_n^{(p)} = -n-3.



$$

Next, we write the general solution as the sum of the complementary and particular solutions. Therefore,

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}+𝑎_{(𝑝)𝑛} \\ & =𝐴⋅2^{𝑛}−𝑛−3.\end{aligned}



$$

Finally, we find the constant $A$ by substituting the initial condition $a_1=0$ into the general solution:

$$



\begin{aligned}0 & =𝐴⋅2^{1}−1−3 \\ 0 & =2𝐴−4 \\ 𝐴 & =2\end{aligned}



$$

Therefore, the solution is

$$



a_n = \boxed{\color{blue}2(2)^n - n - 3}.



$$
