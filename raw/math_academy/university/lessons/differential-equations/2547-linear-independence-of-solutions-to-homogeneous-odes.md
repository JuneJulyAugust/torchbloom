# Linear Independence of Solutions to Homogeneous ODEs

Source: https://www.mathacademy.com/topics/2547?courseId=61
Topic ID: 2547

## Prerequisites

- [Verifying Solutions of Differential Equations](../../../ap-courses/lessons/ap-calculus-ab/1181-verifying-solutions-of-differential-equations.md)
- [Linear Independence in Abstract Vector Spaces](../linear-algebra/1908-linear-independence-in-abstract-vector-spaces.md)
- [Introduction to Second-Order Linear ODEs](./2548-introduction-to-second-order-linear-odes.md)

## Lesson

### Introduction

Suppose $\{f_1(x), f_2(x), \ldots, f_n(x) \}$ is a set of functions defined on an interval $I\subseteq R.$

- The set is called **linearly dependent** on $I$ if there exist real numbers $k_1, k_2, \ldots, k_n,$ *not all zero*, such that for all $x \in I.$ Intuitively, at least one of the functions can be written as a linear combination of the others.

- The set is called **linearly independent** on $I$ if the *only* way the linear combination can equal $0$ for all $x \in I$ is by taking

Notice that these definitions closely parallel the notions of linear dependence and independence for vectors in a vector space.

For example, let's consider the set of functions

$$


\{ \sin x, \, \cos x, \, 2\sin x \}


$$

defined on $x \in \mathbb{R}.$

Notice that for all $x \in \mathbb{R},$ we have that

$$


2 \cdot \sin x + 0 \cdot \cos x + (-1) \cdot 2\sin x = 0.


$$

Therefore, since not all the scalar coefficients in the linear combination are zero, the given set of functions is linearly dependent.

Let's see another example.

### Example: Identifying Pairs of Linearly Dependent and Linearly Independent Functions

#### Question

Given the set of functions $\{e^x, \, \sin x \}$ defined on $x \in \mathbb{R},$ explain why they are linearly independent.

#### Explanation

Recall that the set of functions $\{f_1(x), f_2(x), \ldots, f_n(x) \},$ which are defined on some interval $I,$ is ** if there exist real scalars $k_1,k_2,\ldots,k_n$ not all zero such that the linear combination $k_1 \cdot f_1 + k_2 \cdot f_2 + \ldots + k_2 \cdot f_2$ is identically zero, i.e,

$$


k_1 \cdot f_1(x) + k_2 \cdot f_2(x) + \ldots + k_2 \cdot f_2(x) = 0


$$

for all $x \in I.$ Otherwise, if $k_1 = k_2 = \cdots = k_n = 0$ is the only solution, the set is **.

Now, suppose for all $x \in \mathbb{R},$ we have that

$$


k_1 e^x + k_2 \sin x = 0.


$$

For example:

- If $x=0,$ we get

- If $x=1,$ we get

Thus, we obtain the following system of linear equations:

$$


\begin{aligned}𝑘_{1}=0 \\ 𝑒𝑘_{1}+(sin⁡1)\,𝑘_{2}=0\end{aligned}


$$

The only solution for this system is $\boxed{k_1=k_2=0}.$

Therefore, since $\boxed{\text{all}}$ the scalar coefficients in the linear combination must be zero, the given set of functions is linearly $\boxed{\text{independent}}.$

### The Wronskian

Suppose $y_1(x)$ and $y_2(x)$ are differentiable functions defined on some interval $I.$ Then, the **Wronskian** is defined as

$$


\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned}


$$

and it has the following important properties:

If $W \neq 0$ for at least one $x \in I,$ then $y_1$ and $y_2$ are linearly independent.

If $W = 0$ and it’s known that $y_1$ and $y_2$ are solutions to the same second-order linear differential equation, then $y_1$ and $y_2$ are linearly dependent.

**Watch out!** We cannot deduce any information from $W = 0$ in cases where $y_1$ and $y_2$ are not known to be solutions to the same second-order linear differential equation.

### Example: Calculating the Wronskian of Two Functions

#### Question

Compute the Wronskian $W(y_1, y_2)$ for $y_1(x) =2x$ and $y_2(x) = x^2.$

#### Explanation

The Wronskian $W(y_1,y_2)$ of two functions $y_1(x)$ and $y_2(x)$ is defined as

$$


\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned}


$$

In our case, we have $y_1(x) = 2x$ and $y_2(x) = x^2.$ Therefore,

$$


\begin{aligned}𝑊(𝑦_{1},𝑦_{2}) & =2𝑥(𝑥^{2})^{′}−𝑥^{2}(2𝑥)^{′} \\ & =4𝑥^{2}−2𝑥^{2} \\ & =2𝑥^{2}.\end{aligned}


$$

### Example: Identifying Pairs of Linearly Independent Functions Using the Wronskian

#### Question

$$


y_1(x) = x^2 + 1, \qquad y_2(x) = 2x, \qquad x \in \mathbb R


$$

Consider the functions $y_1(x)$ and $y_2(x)$ above. Given that $y_1$ and $y_2$ are solutions of the same second-order linear differential equation, use the Wronskian to explain why the set $\{y_1(x), y_2(x) \}$ is linearly independent.

#### Explanation

Suppose the functions $y_1(x)$ and $y_2(x)$ are defined on some interval $I.$ The Wronskian $W(y_1,y_2)$ of these functions is defined as

$$


\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned}


$$

Recall the following:

- If $W \neq 0$ for at least one $x \in I,$ then $y_1$ and $y_2$ are linearly independent.

- If $W = 0$ and it’s known that $y_1$ and $y_2$ are solutions to the same second-order linear differential equation, then $y_1$ and $y_2$ are linearly dependent.

In our case, the Wronskian is given by

$$


\begin{aligned}𝑊(𝑦_{1},𝑦_{2}) & =\begin{aligned}𝑥^{2}+1 & 2𝑥 \\ (𝑥^{2}+1)^{′} & (2𝑥)^{′}\end{aligned} \\ & =\begin{aligned}𝑥^{2}+1 & 2𝑥 \\ 2𝑥 & 2\end{aligned} \\ & =(𝑥^{2}+1)⋅2−(2𝑥)⋅(2𝑥) \\ & =2(𝑥^{2}+1)−4𝑥^{2} \\ & =2𝑥^{2}+2−4𝑥^{2} \\ & =2−2𝑥^{2}\end{aligned}


$$

which is nonzero for at least one $x \in \mathbb{R}.$

Therefore, the set $\left\{y_1(x), y_2(x) \right\}$ is linearly independent on $\mathbb R.$

### Sets of Fundamental Solutions

A **fundamental set of solutions** to a homogeneous, linear differential equation of degree $n$ is a set of precisely $n$ linearly independent solutions.

For example, consider the second-order homogeneous differential equation

$$


y''(x) - 4y(x) = 0.


$$

Using direct substitution, it's straightforward to show that $y_1(x) = e^{2x}$ and $y_2(x) = e^{-2x}$ are the solutions to the equation.

Let's keep track of our solutions by putting them into a set $S,$ as follows:

$$


S = \left\{e^{2x}, e^{-2x}\right\}


$$

Computing the Wronskian of our solutions, we get

$$


\begin{aligned}𝑊(𝑦_{1},𝑦_{2}) & =\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned} \\ & =𝑦_{1}𝑦_{′2}^{}−𝑦_{′1}^{}𝑦_{2} \\ & =(𝑒^{2𝑥})(𝑒^{−2𝑥})^{′}−(𝑒^{2𝑥})^{′}(𝑒^{−2𝑥}) \\ & =(𝑒^{2𝑥})(−2𝑒^{−2𝑥})−(2𝑒^{2𝑥})(𝑒^{−2𝑥}) \\ & =−2−2 \\ & =−4\end{aligned}


$$

Since the Wronskian is not zero, the solutions $y_1$ and $y_2$ are linearly independent.

Because the original equation is of degree two, and since the set $S$ contains *precisely* two linearly independent functions, we say that the set $S$ is a fundamental set of solutions to the differential equation.

**Important:** The fundamental set of solutions is not unique. For example, the set $S',$ given by

$$


S' = \left\{4e^{2x}, e^{-2x}\right\}


$$

is also a fundamental set of solutions.

As a general rule, we tend to pick the simplest set of linearly independent functions when constructing our fundamental set of solutions.

### Example: Identifying Fundamental Sets of Solutions

#### Question

Consider the differential equation $x^2y'' - 5x y' + 9y=0.$ Which of the following statements are true?

1. $y_1(x) = x^3$ is a solution to the equation for $x\in \mathbb R.$

2. $y_2(x) = x^3 \ln x$ is a solution to the equation for $x > 0.$

3. The functions $y_1(x)$ and $y_2(x)$ form a set of fundamental solutions to the equation on $(0, \infty).$

#### Explanation

Recall that to determine whether $y(x)$ is a solution to the differential equation, we substitute $y$ and its derivatives into the equation.

Let's check each statement in turn.

- Statement I is true. First, we find the first and second derivatives of $y_1(x){:}$ Now, let's substitute $y_1(x)$ and its derivatives into the equation: So, $y_1(x)$ is a solution to the equation.

- Statement II is true. First, we find the first and second derivatives of $y_2(x){:}$ Now, let's substitute $y_2(x)$ and its derivatives into the equation: So, $y_2(x)$ is a solution to the equation.

- Statement III is true. Both $y_1$ and $y_2$ are solutions of the equation. To check if these functions are linearly independent, we compute the Wronskian: Since the Wronskian is not identically $0$ on $(0, \infty),$ the functions are linearly independent. Hence, $y_1(x)$ and $y_2(x)$ form a set of fundamental solutions to the equation on $(0, \infty)$.

Therefore, the correct answer is "I, II, and III".
