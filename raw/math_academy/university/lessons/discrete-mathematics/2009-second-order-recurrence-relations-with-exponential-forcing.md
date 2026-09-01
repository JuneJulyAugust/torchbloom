# Second-Order Recurrence Relations with Exponential Forcing

Source: https://www.mathacademy.com/topics/2009?courseId=109
Topic ID: 2009

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

A second-order linear**inhomogeneous** recurrence relation is a recurrence relation that can be written as

$$



a_n + P \cdot a_{n-1} + Q \cdot a_{n-2} = f(n).



$$

The function $f(n)$ is sometimes called a **forcing function.**

For example, let's consider the following second-order recurrence relation:

$$



a_n + 5 a_{n-1} + 6 a_{n-2} = 15 \cdot 2^n



$$

This equation is inhomogeneous because the right-hand side is $f(n) = 15 \cdot 2^n,$ which is different from zero.

We say that the recurrence relation is subject to **exponential forcing** because $f(n)$ is an exponential function in this case.

### Solving Second-Order Inhomogeneous Recurrence Relations With Exponential Forcing

To find the general solution to a linear inhomogeneous recurrence relation, we perform the following steps:

- **Step 1:** Find the **complementary solution** $a^{(h)}_n$ of the associated homogeneous equation.

- **Step 2:** Find a **particular solution** $a^{(p)}_n$ of the inhomogeneous equation.

- **Step 3:** Write the general solution as the sum of the complementary and particular solutions:

To illustrate, let's find the general solution to the following inhomogeneous recurrence relation:

$$



a_n + 5a_{n-1} + 6a_{n-2} = 15 \cdot 2^n



$$

**Step 1:** Find the complementary solution.

First, we find the solution $a^{(h)}_n$ of the associated homogeneous recurrence relation:

$$



a_n + 5 a_{n-1} + 6 a_{n-2} = 0



$$

The characteristic equation is

$$



\begin{aligned}𝜆^{2}+5𝜆+6 & =0 \\ (𝜆+3)(𝜆+2) & =0.\end{aligned}



$$

So, we have $\lambda=-3$ or $\lambda=-2.$ Consequently, the complementary solution is

$$



a_n^{(h)} = A \cdot (-3)^n + B \cdot (-2)^n.



$$

**Step 2:** Find a particular solution that satisfies the recurrence relation.

The right-hand side of our recurrence relation is $15 \cdot 2^n.$ The base of the exponential part is $2.$ Therefore, we assume a particular solution of the form

$$



a_n^{(p)} = \alpha \cdot 2^n,



$$

where $\alpha$ is a constant to be determined. As a result,

$$



a_{n-1}^{(p)} = \alpha \cdot 2^{n-1}, \qquad a_{n-2}^{(p)} = \alpha \cdot 2^{n-2}.



$$

To find the value of $\alpha,$ we substitute the particular solution into the recurrence relation and solve for $\alpha{:}$

$$



\begin{aligned}𝛼⋅2^{𝑛}+5⋅𝛼⋅2^{𝑛−1}+6⋅𝛼⋅2^{𝑛−2} & =15⋅2^{𝑛} \\ 𝛼⋅2^{𝑛}+5𝛼⋅\frac{1}{2}⋅2^{𝑛}+6⋅𝛼⋅\frac{1}{2^{2}}⋅2^{𝑛} & =15⋅2^{𝑛} \\ 𝛼⋅2^{𝑛}+5𝛼⋅\frac{1}{2}⋅2^{𝑛}+6⋅𝛼⋅\frac{1}{2^{2}}⋅2^{𝑛} & =15⋅2^{𝑛} \\ 𝛼+\frac{5𝛼}{2}+\frac{3𝛼}{2} & =15 \\ 5𝛼 & =15 \\ 𝛼 & =3\end{aligned}



$$

Therefore, the particular solution is

$$



a_n^{(p)} = 3 \cdot 2^n.



$$

**Step 3:** Write down the general solution.

The general solution is the sum of the complementary and particular solutions:

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}+𝑎_{(𝑝)𝑛} \\ & =𝐴⋅(−3)^{𝑛}+𝐵⋅(−2)^{𝑛}+3⋅2^{𝑛}\end{aligned}



$$

### Example: Solving a Second-Order Recurrence Relation With Exponential Forcing

#### Question

Find the general solution to the difference equation

$$



a_n + 2a_{n-1} + a_{n-2} = 16\cdot 3^n.



$$

#### Explanation

First, we need to find the general solution $a_n^{(h)}$ of the associated homogeneous difference equation

$$



a_n + 2a_{n-1} + a_{n-2} = 0.



$$

Writing down and solving the characteristic equation gives

$$



\begin{aligned}𝜆^{2}+2𝜆+1 & =0 \\ (𝜆+1)^{2} & =0.\end{aligned}



$$

So $\lambda = -1.$ Therefore,

$$



a_n^{(h)} = A \cdot (-1)^n + Bn \cdot (-1)^n.



$$

We now need to find the particular solution $a_n^{(p)}$ of the original difference equation.

The right-hand side of the inhomogeneous difference equation is $16\cdot 3^n.$ The base of the exponential part is $3,$ which is not the root of the characteristic equation. Therefore, we assume a particular solution of the form

$$



a_n^{(p)} = \alpha \cdot 3^n,



$$

where $\alpha$ is a constant to be determined. As a result,

$$



a_{n-1}^{(p)} = \alpha \cdot 3^{n-1}, \qquad a_{n-2}^{(p)} = \alpha \cdot 3^{n-2}.



$$

To find the value of $\alpha,$ we substitute the particular solution into the difference equation and solve for $\alpha{:}$

$$



\begin{aligned}𝛼⋅3^{𝑛}+2⋅𝛼⋅3^{𝑛−1}+𝛼⋅3^{𝑛−2} & =16⋅3^{𝑛} \\ 𝛼⋅3^{𝑛}+2𝛼⋅\frac{1}{3}⋅3^{𝑛}+𝛼⋅\frac{1}{3^{2}}⋅3^{𝑛} & =16⋅3^{𝑛} \\ 𝛼⋅3^{𝑛}+2𝛼⋅\frac{1}{3}⋅3^{𝑛}+𝛼⋅\frac{1}{3^{2}}⋅3^{𝑛} & =16⋅3^{𝑛} \\ 𝛼+\frac{2𝛼}{3}+\frac{𝛼}{9} & =16 \\ \frac{16𝛼}{9} & =16 \\ 𝛼 & =9\end{aligned}



$$

Therefore, the particular solution is

$$



a_n^{(p)} = 9 \cdot 3^n.



$$

Finally, the general solution is given by

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}+𝑎_{(𝑝)𝑛} \\ & =𝐴⋅(−1)^{𝑛}+𝐵𝑛⋅(−1)^{𝑛}+9⋅3^{𝑛}.\end{aligned}



$$

### When the Forcing and Complementary Functions are Linearly Dependent

Consider the following recurrence relation:

$$



a_{n} - 3a_{n-1} + 2a_{n-2} = 2^n



$$

It's easy to show that the complementary solution is

$$



a_{n}^{(h)} = A + B\cdot 2^n.



$$

When it comes to selecting a form for a particular solution, we *cannot* pick

$$



a_n^{(p)} = \alpha \cdot 2^n.



$$

This solution is already associated with the complementary solution. Therefore, the left-hand side of the recurrence relation evaluates to zero when this is form substituted into it.

Indeed, we can check that if $a_n = \alpha \cdot 2^n$, then we have

$$



\begin{aligned}𝑎_{𝑛}−3𝑎_{𝑛−1}+2𝑎_{𝑛−2} & =𝛼⋅2^{𝑛}−3𝛼⋅2^{𝑛−1}+2𝛼⋅2^{𝑛−2} \\ & =𝛼⋅2^{𝑛}−\frac{3}{2}𝛼⋅2^{𝑛}+\frac{2}{4}𝛼⋅2^{𝑛} \\ & =(1−\frac{3}{2}+\frac{1}{2})⋅𝛼⋅2^{𝑛} \\ & =0.\end{aligned}



$$

In this case, the correct form for a particular solution is

$$



a_n^{(p)} = \alpha n\cdot 2^n.



$$

### When the Forcing and Complementary Functions are Linearly Dependent: Double Root Case

Now consider the following recurrence relation:

$$



a_{n} - 4a_{n-1} + 4a_{n-2} = 2^n



$$

In this case, the characteristic equation has the double root $\lambda = 2.$ Therefore, the complementary solution is

$$



a_{n}^{(h)} = A\cdot 2^n + Bn\cdot 2^n.



$$

Now, when it comes to selecting a form for a particular solution, *neither* of the following will work!

$$



\alpha \cdot 2^n, \qquad \alpha n \cdot 2^n



$$

This is because both of these solutions are associated with the complementary solution.

In this case, the correct form for a particular solution is

$$



a_n^{(p)} = \alpha n^2\cdot 2^n.



$$

### Example: Solving a Recurrence Relation When the Forcing and Complementary Functions are Linearly Dependent

#### Question

Find the general solution to the difference equation

$$



a_n - 8a_{n-1} + 7a_{n-2} = 6\cdot 7^n.



$$

#### Explanation

First, we need to find the general solution $a_n^{(h)}$ of the associated homogeneous difference equation

$$



a_n - 8a_{n-1} + 7a_{n-2} = 0.



$$

Writing down and solving the characteristic equation gives

$$



\begin{aligned}𝜆^{2}−8𝜆+7 & =0 \\ (𝜆−7)(𝜆−1) & =0.\end{aligned}



$$

So $\lambda = 1$ or $\lambda = 7.$ Therefore,

$$



a_n^{(h)} = A + B \cdot 7^n.



$$

We now need to find the particular solution $a_n^{(p)}$ of the original difference equation.

The right-hand side of the inhomogeneous difference equation is $6\cdot 7^n.$ The base of the exponential part is $7,$ which coincides with one of the roots of the characteristic equation. Therefore, we assume a particular solution of the form

$$



a_n^{(p)} = \alpha n \cdot 7^n,



$$

where $\alpha$ is a constant to be determined. As a result,

$$



a_{n-1}^{(p)} = \alpha (n-1) 7^{n-1}, \qquad a_{n-2}^{(p)} = \alpha (n-2) 7^{n-2}.



$$

To find the value of $\alpha,$ we substitute the particular solution into the difference equation and solve for $\alpha{:}$

$$



\begin{aligned}𝛼𝑛⋅7^{𝑛}−8⋅𝛼(𝑛−1)7^{𝑛−1}+7⋅𝛼(𝑛−2)7^{𝑛−2} & =6⋅7^{𝑛} \\ 𝛼𝑛⋅7^{𝑛}−8𝛼(𝑛−1)⋅\frac{1}{7}⋅7^{𝑛}+7𝛼(𝑛−2)⋅\frac{1}{7^{2}}⋅7^{𝑛} & =6⋅7^{𝑛} \\ 𝛼𝑛⋅7^{𝑛}−8𝛼(𝑛−1)⋅\frac{1}{7}⋅7^{𝑛}+7𝛼(𝑛−2)⋅\frac{1}{7^{2}}⋅7^{𝑛} & =6⋅7^{𝑛} \\ 𝛼𝑛−\frac{8𝛼𝑛}{7}+\frac{8𝛼}{7}+\frac{𝛼𝑛}{7}−\frac{2𝛼}{7} & =6 \\ \frac{6𝛼}{7} & =6 \\ 𝛼 & =7\end{aligned}



$$

Therefore, the particular solution is

$$



a_n^{(p)} = 7n \cdot 7^n.



$$

Finally, the general solution is given by

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}+𝑎_{(𝑝)𝑛} \\ & =𝐴+𝐵⋅7^{𝑛}+7𝑛⋅7^{𝑛} \\ & =𝐴+𝐵⋅7^{𝑛}+𝑛⋅7^{𝑛+1}.\end{aligned}



$$

### Example: Solving a Second-Order Recurrence Relation With Exponential Forcing Given Some Initial Values

#### Question

Solve the difference equation

$$



a_n - 16 a_{n-2} = 9\cdot 5^n, \quad a_0 = 15, \quad a_1 = 85.



$$

#### Explanation

First, we need to find the general solution $a_n^{(h)}$ of the associated homogeneous difference equation

$$



a_n - 16a_{n-2} = 0.



$$

Writing down and solving the characteristic equation gives

$$



\begin{aligned}𝜆^{2}−16 & =0 \\ (𝜆+4)(𝜆−4) & =0.\end{aligned}



$$

So $\lambda = -4$ or $\lambda = 4.$ Therefore,

$$



a_n^{(h)} = A \cdot (-4)^n + B \cdot 4^n.



$$

We now need to find the particular solution $a_n^{(p)}$ of the original difference equation.

The right-hand side of the inhomogeneous difference equation is $9\cdot 5^n.$ The base of the exponential part is $5,$ which is not a root of the characteristic equation. Therefore, we assume a particular solution of the form

$$



a_n^{(p)} = \alpha \cdot 5^n,



$$

where $\alpha$ is a constant that is to be determined. As a result,

$$



a_{n-1}^{(p)} = \alpha \cdot 5^{n-1}, \qquad a_{n-2}^{(p)} = \alpha \cdot 5^{n-2}.



$$

To find the value of $\alpha,$ we substitute the particular solution into the difference equation and solve for $\alpha{:}$

$$



\begin{aligned}𝛼⋅5^{𝑛}−16⋅𝛼⋅5^{𝑛−2} & =9⋅5^{𝑛} \\ 𝛼⋅5^{𝑛}−16𝛼⋅\frac{1}{5^{2}}⋅5^{𝑛} & =9⋅5^{𝑛} \\ 𝛼⋅5^{𝑛}−16𝛼⋅\frac{1}{5^{2}}⋅5^{𝑛} & =9⋅5^{𝑛} \\ 𝛼−\frac{16𝛼}{25} & =9 \\ \frac{9𝛼}{25} & =9 \\ 𝛼 & =25\end{aligned}



$$

Therefore, the particular solution is

$$



a_n^{(p)} = 25 \cdot 5^n = 5^{n+2}.



$$

So, the general solution is given by

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}+𝑎_{(𝑝)𝑛} \\ & =𝐴⋅(−4)^{𝑛}+𝐵⋅4^{𝑛}+5^{𝑛+2}.\end{aligned}



$$

Finally, we find the constants $A$ and $B$ by substituting the initial values.

- Substituting $a_0 = 15$ into the general solution gives

- Substituting $a_1 = 85$ into the general solution gives

Therefore, we have the following system of equations for $A$ and $B{:}$

$$



\begin{aligned}𝐴+𝐵=−10 \\ 𝐴−𝐵=10\end{aligned}



$$

Solving this system gives $A=0,$ $B=-10.$

Therefore, the solution to the recurrence relation is

$$



\begin{aligned}𝑎_{𝑛} & =−10⋅4^{𝑛}+5^{𝑛+2} \\ & =5^{𝑛+2}−10⋅4^{𝑛}.\end{aligned}



$$
