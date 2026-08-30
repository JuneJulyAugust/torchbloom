# Power Series Solutions of Differential Equations

Source: https://www.mathacademy.com/topics/2543?courseId=61
Topic ID: 2543

## Prerequisites

- [Differentiating Taylor Series](../../../ap-courses/lessons/ap-calculus-bc/36-differentiating-taylor-series.md)
- [Verifying Solutions of Differential Equations](../../../ap-courses/lessons/ap-calculus-ab/1181-verifying-solutions-of-differential-equations.md)
- [Introduction to Recurrence Relations](./1989-introduction-to-recurrence-relations.md)

## Lesson

### Introduction

Another technique for solving *homogeneous* differential equations is to write the solution as a general power series and find a **recurrence relation** between the coefficients of the series. This technique involves the following steps:

- **Step 1:** Write the solution as a general power series $y =\displaystyle{\sum_{n=0}^\infty a_n x^n}.$

- **Step 2:** Compute any derivatives ($y',$ $y'',$ etc.) so that we can substitute the general series solution into the differential equation.

- **Step 3:** Rewrite all the series in the equation so that they use the same index of summation, the powers of $x$ are the same, and the indices start at the same value.

- **Step 4:** Consolidate all the series into a single series that is equal to $0.$

- **Step 5:** Set the coefficients of the series equal to $0$ and solve for the recurrence relation.

In the following, we'll illustrate this process in a concrete example.

### Finding the Recurrence Relation for the Coefficients of the Power Series Solution

Let's apply the general algorithm to find the power series solution for the following equation:

$$


y' - y =0


$$

- **Step 1:** First, we write the solution as a general power series $y =\displaystyle{\sum_{n=0}^\infty a_n x^n}.$

- **Step 2:** Next, we compute $y'$ so that we can substitute the general series solution into the differential equation. Computing $y',$ we get and substituting in the differential equation, we get

- **Step 3:** Then, we rewrite all the series in the equation so that they use the same index of summation, the powers of $x$ are the same, and the indices start at the same value. In the first sum, we change the index of the summation by writing $m = n-1.$ This gives Replacing $m$ with $n$ in the first summation (since it does not matter which letter we use) gives

- **Step 4:** We consolidate all the series into a single series that is equal to $0.$ Since both sums now start with $n=0,$ we can combine them as follows:

- **Step 5:** Setting the coefficients of the series equal to $0,$ we get the following recurrence relation:

$$


\begin{aligned}(𝑛+1)𝑎_{𝑛+1}−𝑎_{𝑛} & =0 \\ 𝑎_{𝑛+1} & =\frac{𝑎_{𝑛}}{𝑛+1},\,𝑛=0,1,2…\end{aligned}


$$

In the following, we'll see how to apply this recurrence relation to find the final power series solution of the differential equation.

### Finding the Power Series Solution Using the Recurrence Relation

The general power series solution of the differential equation $y' - y =0$ is

$$


y =\sum_{n=0}^\infty a_n x^n.


$$

As we determined previously, the coefficients of this series satisfy the recurrence relation

$$


a_{n+1} =\dfrac{a_n }{n+1 }, \qquad n= 0,1,2, \ldots


$$

Since we are looking for the general solution of the differential equation, we can set the first term of its power series solution to an arbitrary number. So, we can set $a_0=C,$ where $C$ is an arbitrary constant.

Now, using the recurrence relation, we get

$$


\begin{aligned}𝑎_{1} & =\frac{𝑎_{0}}{0+1}=\frac{𝐶}{1}, \\ 𝑎_{2} & =\frac{𝑎_{1}}{1+1}=\frac{𝐶}{1⋅2}, \\ 𝑎_{3} & =\frac{𝑎_{2}}{2+1}=\frac{𝐶}{1⋅2⋅3}, \\ & \,\,⋮ \\ 𝑎_{𝑛} & =\frac{𝐶}{𝑛!}.\end{aligned}


$$

So, we have

$$


\begin{aligned}𝑦 & =𝐶+\frac{𝐶}{1}\,𝑥+\frac{𝐶}{1⋅2}\,𝑥^{2}+\frac{𝐶}{1⋅2⋅3}\,𝑥^{3}+⋯+\frac{𝐶}{𝑛!}\,𝑥^{𝑛}+⋯ \\ & =𝐶(1+𝑥+\frac{1}{2!}𝑥^{2}+⋯+\frac{𝑥^{𝑛}}{𝑛!}+⋯) \\ & =𝐶(\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}\frac{𝑥^{𝑛}}{𝑛!}).\end{aligned}


$$

Recall the definition of the standard Maclaurin series of the exponential function:

$$


e^{x} = 1+x+\frac{1}{2!}x^2+\cdots + \dfrac{x^n}{n!} + \cdots = \sum_{n=0}^\infty \dfrac{x^n}{n!}


$$

So, finally, we can write the general solution of our differential equation as

$$


y = C e^x.


$$

The solution of a differential equation is not always a recognizable standard series. But if we are able to find the recurrence relation for the coefficients, we can always present the solution as a general power series.

### Example: Calculating the Recurrence Relation For an Exponential Growth or Decay Equation

#### Question

Let $y = \displaystyle{\sum_{n=0}^\infty a_n x^n}$ be a series solution to the equation $y'-3y=0$. What is the recurrence relation for the coefficients $a_n$, where $n=0,1,2, \ldots$?

#### Explanation

First, we find $y'(x){:}$

$$


\begin{aligned}𝑦^{′}(𝑥) & =(\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛})^{′} \\ & =(𝑎_{0}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛})^{′} \\ & =0+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}𝑥^{𝑛−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}𝑥^{𝑛−1}\end{aligned}


$$

Now, we substitute the expressions for $y(x)$ and $y'(x)$ into the given differential equation:

$$


\sum_{n=1}^\infty n a_n x^{n-1}-3\sum_{n=0}^\infty a_n x^n = 0


$$

We want to make the powers of $x$ the same. Therefore, in the first sum, we change the index of the summation by writing $m = n-1$. This gives

$$


\sum_{m=0}^\infty (m+1) a_{m+1} x^{m} -3 \sum_{n=0}^\infty a_n x^n =0.


$$

Replacing $m$ with $n$ in the first summation (since it does not matter which letter we use) gives

$$


\sum_{n=0}^\infty (n+1) a_{n+1} x^{n} -3 \sum_{n=0}^\infty a_n x^n =0.


$$

Since both sums now start with $n=0$, we can combine them as follows:

$$


\begin{aligned}\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(𝑛+1)𝑎_{𝑛+1}𝑥^{𝑛}−\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}3𝑎_{𝑛}𝑥^{𝑛} & =0 \\ \underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}[(𝑛+1)𝑎_{𝑛+1}𝑥^{𝑛}−3𝑎_{𝑛}𝑥^{𝑛}] & =0 \\ \underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}[(𝑛+1)𝑎_{𝑛+1}−3𝑎_{𝑛}]𝑥^{𝑛} & =0\end{aligned}


$$

Setting each coefficient of $x$ equal to zero, we obtain

$$


(n+1) a_{n+1} -3 a_n = 0.


$$

Finally then, the recursion formula is

$$


a_{n+1} =\dfrac{3 a_n }{n+1}, \qquad n= 0,1,2, \ldots


$$

### Example: Calculating the Recurrence Relation For a First-Order Differential Equation

#### Question

Let $y =\displaystyle{\sum_{n=0}^\infty a_n x^n}$ be a series solution to the equation $y' +4xy = 0.$

What is the recurrence relation for the coefficients $a_n,$ where $n=1, 2, 3, \dots$?

#### Explanation

First, we find $y'(x){:}$

$$


\begin{aligned}𝑦^{′}(𝑥) & =(\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛})^{′} \\ & =(𝑎_{0}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛})^{′} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}𝑥^{𝑛−1}\end{aligned}


$$

Now, we substitute the expressions for $y(x)$ and $y'(x)$ into the given differential equation:

$$


\begin{aligned}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}𝑥^{𝑛−1}+4𝑥\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛} & =0 \\ \underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}𝑥^{𝑛−1}+\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}4𝑎_{𝑛}𝑥^{𝑛+1} & =0\end{aligned}


$$

We want to make the powers of $x$ the same. Therefore, in the first sum, we change the index of the summation by writing $m = n-1.$ This gives

$$


\sum_{m=0}^\infty (m+1) a_{m+1} x^{m} + \sum_{n=0}^\infty 4a_n x^{n+1} =0.


$$

Now, in the second series, we change the index of the summation by writing $m = n+1.$ This gives

$$


\sum_{m=0}^\infty (m+1) a_{m+1} x^{m} + \sum_{m=1}^\infty 4a_{m-1} x^{m} =0.


$$

Replacing $m$ with $n$ in both summations (since it does not matter which letter we use) gives

$$


\sum_{n=0}^\infty (n+1) a_{n+1} x^{n} + \sum_{n=1}^\infty 4 a_{n-1} x^{n} =0.


$$

Next, we need to get two series starting with the same value of $n.$ So, we take out the term $n = 0$ from the left-hand side:

$$


a_1 + \sum_{n=1}^\infty (n+1) a_{n+1} x^{n} + \sum_{n=1}^\infty 4a_{n-1} x^{n} = 0


$$

We now combine the series as follows:

$$


\begin{aligned}𝑎_{1}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(𝑛+1)𝑎_{𝑛+1}𝑥^{𝑛}+4𝑎_{𝑛−1}𝑥^{𝑛}] & =0 \\ 𝑎_{1}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}[(𝑛+1)𝑎_{𝑛+1}+4𝑎_{𝑛−1}]𝑥^{𝑛} & =0\end{aligned}


$$

Finally, by equating coefficients of $x^n,$ we obtain

$$


a_1 = 0, \qquad (n+1) a_{n+1} = -4a_{n-1}.


$$

Solving for $a_{n+1}$ gives

$$


a_{n+1} = -\dfrac{ 4a_{n-1}}{n+1 }, \quad n=1, 2, 3, \dots


$$

Therefore, the recurrence relation is

$$


a_{n+1} = -\dfrac{ 4a_{n-1}}{n+1 }, \quad a_1=0, \quad n=1, 2, 3, \dots


$$

Note that every coefficient with an odd index equals $0,$ since $a_1=0.$

### Example: Calculating the Recurrence Relation For a Second-Order Differential Equation

#### Question

Let $y =\displaystyle{\sum_{n=0}^\infty a_n x^n}$ be a series solution to the equation $2y''+y=0.$ Find $f(n),$ given that the recurrence relation for $a_n$ can be written as

$$


a_{n+2} = \dfrac{ a_n }{ f(n) }, \qquad n= 0,1,2\ldots


$$

#### Explanation

First, we find $y'(x)\mathbin{:}$

$$


\begin{aligned}𝑦^{′}(𝑥) & =(\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛})^{′} \\ & =(𝑎_{0}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛})^{′} \\ & =0+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}𝑥^{𝑛−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}𝑥^{𝑛−1}\end{aligned}


$$

Similarly, we find $y''(x)\mathbin{:}$

$$


\begin{aligned}𝑦^{″}(𝑥) & =(\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}𝑥^{𝑛−1})^{′} \\ & =(𝑎_{1}+\underset{\underset{𝑛=2}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}𝑥^{𝑛−1})^{′} \\ & =0+\underset{\underset{𝑛=2}{∑}}{\overset{}{∞}}𝑛(𝑛−1)𝑎_{𝑛}𝑥^{𝑛−2} \\ & =\underset{\underset{𝑛=2}{∑}}{\overset{}{∞}}𝑛(𝑛−1)𝑎_{𝑛}𝑥^{𝑛−2}\end{aligned}


$$

Now, we substitute the expressions for $y(x)$ and $y''(x)$ into the given differential equation:

$$


2\sum_{n=2}^\infty n (n-1) a_{n} x^{n-2} +\sum_{n=0}^\infty a_n x^{n} = 0


$$

We want to make the powers of $x$ the same. Therefore, in the first sum, we change the index of the summation by writing $m = n-2.$ This gives

$$


2\sum_{m=0}^\infty (m+2) (m+1) a_{m+2} x^{m} +\sum_{n=0}^\infty a_n x^{n} = 0.


$$

Replacing $m$ with $n$ in the first summation (since it does not matter which letter we use) gives

$$


2\sum_{n=0}^\infty (n+2) (n+1) a_{n+2} x^{n} +\sum_{n=0}^\infty a_n x^{n} = 0.


$$

Since both sums now start with $n=0,$ we can combine them as follows:

$$


\begin{aligned}\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}2(𝑛+2)(𝑛+1)𝑎_{𝑛+2}𝑥^{𝑛}+\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}𝑥^{𝑛} & =0 \\ \underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}[2(𝑛+2)(𝑛+1)𝑎_{𝑛+2}𝑥^{𝑛}+𝑎_{𝑛}𝑥^{𝑛}] & =0 \\ \underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}[2(𝑛+2)(𝑛+1)𝑎_{𝑛+2}+𝑎_{𝑛}]𝑥^{𝑛} & =0\end{aligned}


$$

Setting each coefficient of $x$ equal to zero, we obtain

$$


2(n+2)(n+1) a_{n+2} +a_n = 0.


$$

Finally then, the recursion formula is

$$


a_{n+2} = -\dfrac{ a_n }{ 2(n+1)(n+2) }, \qquad n= 0,1,2 \ldots


$$

Therefore,

$$


f(n)=-2(n+1)(n+2).


$$
