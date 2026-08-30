# First-Order Recurrence Relations With Exponential Forcing

Source: https://www.mathacademy.com/topics/5375?courseId=109
Topic ID: 5375

## Prerequisites

- [First-Order Recurrence Relations With Polynomial Forcing](./5374-first-order-recurrence-relations-with-polynomial-forcing.md)

## Lesson

### Introduction

Let's consider the following first-order recurrence relation:

$$



a_n = 4a_{n-1} + 2^n, \qquad n \geq 2



$$

This relation is *inhomogeneous* because the right-hand side contains $f(n) = 2^n,$ which is different from zero.

We say that the recurrence relation is subject to **exponential forcing** because $f(n)$ is an exponential function in this case.

Recall that to find the general solution to a linear inhomogeneous recurrence relation, we perform the following steps:

- **Step 1**: Find the complementary solution $a_n^{(h)}$ of the associated homogeneous equation.

- **Step 2**: Find a particular solution $a_n^{(p)}$ that satisfies the inhomogeneous equation.

- **Step 3**: Write the general solution as the sum of the complementary and particular solutions:

To find the general solution of the given recurrence relation, we proceed as follows:

**Step 1**: Find the complementary solution $a_n^{(h)}$ of the associated homogeneous equation.

The associated homogeneous recurrence relation is

$$



a_n = 4a_{n-1} , \qquad n \geq 2



$$

and this has the general solution

$$



a_n^{(h)} = A \cdot 4^n, \qquad n \geq 1.



$$

**Step 2**: Find a particular solution $a_n^{(p)}$ that satisfies the inhomogeneous equation.

Since the inhomogeneous function $g(n)=2^n$ is an exponential with base $2$ (which is not the base of the exponential in the complementary solution), we assume the particular solution is of the same form, i.e.

$$



a_n^{(p)} = \alpha \cdot 2^n,



$$

where $\alpha$ is a constant. Then, we have

$$



\begin{aligned}𝑎_{(𝑝)𝑛−1}^{} & =𝛼⋅2^{𝑛−1}.\end{aligned}



$$

Substituting the above into the original relation, we obtain

$$



\begin{aligned}𝑎_{(𝑝)𝑛}^{} & =4𝑎_{(𝑝)𝑛−1}^{}+2^{𝑛} \\ 𝛼⋅2^{𝑛} & =4𝛼⋅2^{𝑛−1}+2^{𝑛} \\ 𝛼⋅2^{𝑛} & =2𝛼⋅2⋅2^{𝑛−1}+2^{𝑛} \\ 𝛼⋅2^{𝑛} & =2𝛼⋅2^{𝑛}+2^{𝑛} \\ 𝛼⋅2^{𝑛} & =2𝛼⋅2^{𝑛}+1⋅2^{𝑛} \\ 𝛼 & =2𝛼+1 \\ 𝛼 & =−1\end{aligned}



$$

Therefore, the particular solution is

$$



a_n^{(p)} = - 2^n.



$$

**Step 3**: Find the general solution.

To find the general solution, we simply sum $a_n^{(h)}$ and $a_n^{(p)}.$ Therefore, our general solution is

$$



a_n = A \cdot 4^n - 2^n, \qquad n \geq 1



$$

Finally, note that if we're also given the first term of the recurrence relation, we can use this information to find the constant $A.$ We'll see an example of this later in the lesson.

### Example: Solving First-Order Recurrence Relations With Exponential Forcing

#### Question

Consider the recurrence relation

$$



a_n = 6a_{n-1} + 7\cdot 3^n, \qquad n \geq 2.



$$

Find the general solution to this relation for $n \geq 1.$

#### Explanation

To find the general solution to a linear inhomogeneous recurrence relation, we perform the following steps:

- ****: Find the complementary solution $a_n^{(h)}$ of the associated homogeneous equation.

- ****: Find a particular solution $a_n^{(p)}$ of the inhomogeneous equation.

- ****: Write the general solution as the sum of the complementary and particular solutions:

We find the associated homogeneous equation by removing the inhomogeneous function from the relation:

$$



a_n = 6a_{n-1} + 7\cdot 3^n \qquad\Rightarrow\qquad a_n^{(h)} = 6a_{n-1}^{(h)}.



$$

The general solution of a linear homogeneous recurrence relation $a_n = \lambda a_{n-1}$ is given by

$$



a_n = A \cdot \lambda^n,



$$

where $A$ is a constant.

So, the complementary solution of the associated homogeneous equation is

$$



a_n^{(h)} = A \cdot 6^n.



$$

Next, we find a particular solution to the inhomogeneous equation. Since the inhomogeneous function $g(n)=7\cdot3^n$ is exponential with base $3,$ which is not the base of the exponent in the complementary solution, we assume the particular solution is of the same form, i.e.

$$



a_n^{(p)} = \alpha \cdot 3^n,



$$

where $\alpha$ is a constant. Then, we have

$$



a_{n-1}^{(p)} = \alpha \cdot 3^{n-1}.



$$

Substituting the above into the original relation, we obtain

$$



\begin{aligned}𝑎_{(𝑝)𝑛}^{} & =6𝑎_{(𝑝)𝑛−1}^{}+7⋅3^{𝑛} \\ 𝛼⋅3^{𝑛} & =6⋅𝛼⋅3^{𝑛−1}+7⋅3^{𝑛} \\ 𝛼⋅3^{𝑛} & =6𝛼⋅3^{−1}⋅3^{𝑛}+7⋅3^{𝑛} \\ 𝛼⋅3^{𝑛} & =2𝛼⋅3^{𝑛}+7⋅3^{𝑛} \\ 𝛼 & =2𝛼+7 \\ 𝛼 & =−7.\end{aligned}



$$

Therefore, the particular solution is

$$



a_n^{(p)} = -7\cdot 3^n.



$$

Finally, we write the general solution as the sum of the complementary and particular solutions. Therefore,

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}^{}+𝑎_{(𝑝)𝑛}^{} \\ & =𝐴⋅6^{𝑛}−7⋅3^{𝑛}.\end{aligned}



$$

### Cases With Linear Dependence

Consider the recurrence relation

$$



a_n = 4a_{n-1} + 5\cdot 4^n, \qquad n \geq 2.



$$

Let's apply our three-step process to find the general solution of this recurrence relation.

**Step 1**: Find the complementary solution $a_n^{(h)}$ of the associated homogeneous relation.

The associated homogeneous recurrence relation is

$$



a_n = 4a_{n-1}, \qquad n \geq 2,



$$

and this has the general solution

$$



a_n^{(h)} = A \cdot 4^n, \qquad n \geq 1.



$$

**Step 2**: Find a particular solution $a_n^{(p)}$ that satisfies the inhomogeneous equation.

We now have a slight problem. The forcing function of the inhomogeneous equation

$$



f(n) = 5\cdot 4^n



$$

is a constant multiple of the complementary solution $a_n^{(h)}.$ So, we *cannot* choose the particular solution $a_n^{(p)} = \alpha \cdot 4^n$ because solutions of this type are already incorporated into the complementary solution. We say that $f(n)$ and $a_n^{(h)}$ are **linearly dependent.**

In cases such as this, we need to choose the particular solution $a_n^{(p)}$ as follows:

$$



a_n^{(p)} = \alpha n \cdot 4^n



$$

Then, we have

$$



a_{n-1}^{(p)} = \alpha (n-1) \cdot 4^{n-1}.



$$

Substituting the above into the original relation, we obtain

$$



\begin{aligned}𝑎_{(𝑝)𝑛}^{} & =4𝑎_{(𝑝)𝑛−1}^{}+5⋅4^{𝑛}, \\ 𝛼𝑛⋅4^{𝑛} & =4𝛼(𝑛−1)⋅4^{𝑛−1}+5⋅4^{𝑛}, \\ 𝛼𝑛⋅4^{𝑛} & =𝛼(𝑛−1)⋅4^{𝑛}+5⋅4^{𝑛}, \\ 𝛼𝑛⋅4^{𝑛} & =𝛼(𝑛−1)⋅4^{𝑛}+5⋅4^{𝑛}, \\ 𝛼𝑛 & =𝛼(𝑛−1)+5, \\ 𝛼𝑛 & =𝛼𝑛−𝛼+5, \\ 0 & =−𝛼+5, \\ 𝛼 & =5.\end{aligned}



$$

Therefore, the particular solution is

$$



a_n^{(p)} = 5n \cdot 4^n.



$$

**Step 3**: Find the general solution.

To find the general solution, we simply sum $a_n^{(h)}$ and $a_n^{(p)}.$ Therefore, our general solution is

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}^{}+𝑎_{(𝑝)𝑛}^{} \\ & =𝐴⋅4^{𝑛}+5𝑛⋅4^{𝑛}.\end{aligned}



$$

### Example: Solving Recurrence Relations In Cases With Linear Dependence

#### Question

Consider the recurrence relation

$$



a_n = 5a_{n-1} + 3\cdot 5^n, \qquad n \geq 2.



$$

Given that the associated homogeneous recurrence relation has the general solution

$$



a_n^{(h)} = A \cdot 5^n, \qquad n \geq 1



$$

find the particular solution $a_n^{(p)}$ of the inhomogeneous equation.

#### Explanation

Since the inhomogeneous function $g(n)=3\cdot 5^n$ is exponential with base $5,$ which coincides with the base of the exponent in the complementary solution, we assume a particular solution of the form

$$



a_n^{(p)} = \alpha\, n \cdot 5^n,



$$

where $\alpha$ is a constant. We include the factor $n$ to ensure linear independence of $a_n^{(h)}$ and $a_n^{(p)}.$ Then, we have

$$



a_{n-1}^{(p)} = \alpha \left(n-1\right) \cdot 5^{n-1}.



$$

Substituting the above into the original relation, we obtain

$$



\begin{aligned}𝑎_{(𝑝)𝑛}^{} & =5𝑎_{(𝑝)𝑛−1}^{}+3⋅5^{𝑛}, \\ 𝛼𝑛⋅5^{𝑛} & =5𝛼(𝑛−1)⋅5^{𝑛−1}+3⋅5^{𝑛}, \\ 𝛼𝑛⋅5^{𝑛} & =𝛼(𝑛−1)⋅5^{𝑛}+3⋅5^{𝑛}, \\ 𝛼𝑛⋅5^{𝑛} & =𝛼(𝑛−1)⋅5^{𝑛}+3⋅5^{𝑛}, \\ 𝛼𝑛 & =𝛼(𝑛−1)+3, \\ 𝛼𝑛 & =𝛼𝑛−𝛼+3, \\ 0 & =−𝛼+3, \\ 𝛼 & =3.\end{aligned}



$$

Therefore, the particular solution is

$$



a_n^{(p)} = 3n \cdot 5^n.



$$

### Example: Solving First-Order Recurrence Relations Given Initial Values

#### Question

Consider the recurrence relation

$$



a_n = 6a_{n-1} - 6^n, \qquad a_1=12, \quad n \geq 2.



$$

Find the solution of this recurrence relation for $n\geq1$.

#### Explanation

To find the general solution to a linear inhomogeneous recurrence relation, we perform the following steps:

- ****: Find the complementary solution $a_n^{(h)}$ of the associated homogeneous equation.

- ****: Find a particular solution $a_n^{(p)}$ to the inhomogeneous equation.

- ****: Write the general solution as the sum of the complementary and particular solutions:

We find the associated homogeneous equation by removing the inhomogeneous function from the relation:

$$



a_n = 6a_{n-1} - 6^n \qquad\Rightarrow\qquad a_n^{(h)} = 6a_{n-1}^{(h)}.



$$

The general solution of a linear homogeneous recurrence relation $a_n = \lambda a_{n-1}$ is given by

$$



a_n = A\cdot\lambda^n,



$$

where $A$ is a constant.

So, the general solution of the associated homogeneous recurrence relation is

$$



a_n^{(h)} = A \cdot 6^n.



$$

Next, we find a particular solution to the inhomogeneous recurrence relation. Since the inhomogeneous function $g(n) = - 6^n$ is an exponential with base $6,$ which coincides with the base of the exponential in the complementary solution, we assume a particular solution of the form

$$



a_n^{(p)} = \alpha\, n \cdot 6^n,



$$

where $\alpha$ is a constant. We include the factor $n$ to ensure linear independence of $a_n^{(h)}$ and $a_n^{(p)}.$ Then, we have

$$



a_{n-1}^{(p)} = \alpha\left(n-1\right) \cdot 6^{n-1}.



$$

Substituting the above into the original relation, we obtain

$$



\begin{aligned}𝑎_{(𝑝)𝑛}^{} & =6𝑎_{(𝑝)𝑛−1}^{}−6^{𝑛} \\ 𝛼𝑛⋅6^{𝑛} & =6⋅𝛼(𝑛−1)⋅6^{𝑛−1}−6^{𝑛} \\ 𝛼𝑛⋅6^{𝑛} & =𝛼(𝑛−1)⋅6^{𝑛}−6^{𝑛} \\ 𝛼𝑛⋅6^{𝑛} & =𝛼(𝑛−1)⋅6^{𝑛}−1⋅6^{𝑛} \\ 𝛼𝑛 & =𝛼𝑛−𝛼−1 \\ 𝛼 & =−1.\end{aligned}



$$

Therefore, the particular solution is

$$



a_n^{(p)} = -n \cdot 6^n.



$$

Next, we write the general solution as the sum of the complementary and particular solutions. Therefore,

$$



\begin{aligned}𝑎_{𝑛} & =𝑎_{(ℎ)𝑛}^{}+𝑎_{(𝑝)𝑛}^{} \\ & =𝐴⋅6^{𝑛}−𝑛⋅6^{𝑛} \\ & =(𝐴−𝑛)⋅6^{𝑛}.\end{aligned}



$$

Finally, we find the constant $A$ by substituting the initial condition $a_1=12$ into the general solution:

$$



\begin{aligned}12 & =(𝐴−1)⋅6^{1} \\ 2 & =𝐴−1 \\ 𝐴 & =3\end{aligned}



$$

Therefore, the solution is

$$



a_n = (3-n) 6^n.



$$
