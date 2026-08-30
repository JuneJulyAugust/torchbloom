# Determining Unknown Parameters in Quadratic Equations With One Real Solution

Source: https://www.mathacademy.com/topics/6266?courseId=44
Topic ID: 6266

## Prerequisites

- [Solving Quadratic Equations with No Constant Term](./393-solving-quadratic-equations-with-no-constant-term.md)
- [The Discriminant of a Quadratic Equation](./425-the-discriminant-of-a-quadratic-equation.md)

## Lesson

### Introduction

Recall that for a quadratic equation $ax^2+bx+c=0,$ the discriminant $\mathcal{D} = b^2 - 4ac$ tells us about the number of distinct real solutions:

- If $\mathcal{D} > 0,$ then there are $2$ distinct real solutions.

- If $\mathcal{D} = 0,$ then there is $1$ distinct real solution.

- If $\mathcal{D} < 0,$ then there are no real solutions.

If we are given a quadratic equation with an unknown coefficient, then we can use the above criteria to determine the values of the unknown such that the quadratic has a desired number of distinct real solutions.

For example, suppose we have the quadratic equation

$$


9x^2 - 6x + k = 0,


$$

where $k$ is a constant. If this quadratic has exactly one real solution, then the discriminant must equal zero

$$


\mathcal{D} = 0.


$$

The coefficients of our quadratic equation are the following:

$$


a = 9, \qquad b = -6, \qquad c = k


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−6)^{2}−4(9)(𝑘) \\ & =36−36𝑘.\end{aligned}


$$

To have exactly one real solution, we need $\mathcal{D} = 0.$ Therefore, we can determine the values of $k$ that give one distinct solution as follows:

$$


\begin{aligned}D & =0 \\ 36−36𝑘 & =0 \\ 36 & =36𝑘 \\ 𝑘 & =\frac{36}{36} \\ 𝑘 & =1\end{aligned}


$$

### Example: Cases Reducing to Solving a Linear Equation

#### Question

Given that $kx^2 + 14x + k = 0,$ where $k$ is a **** constant, has exactly one real solution, what is the value of $k?$

#### Explanation

A quadratic equation has exactly one real root if the discriminant is equal to zero: $\mathcal{D} = 0.$

The coefficients of our quadratic equation are the following:

$$


a = k, \qquad b = 14, \qquad c = k


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(14)^{2}−4(𝑘)(𝑘) \\ & =196−4𝑘^{2}.\end{aligned}


$$

To have exactly one real solution, we need $\mathcal{D} = 0{:}$

$$


\begin{aligned}196−4𝑘^{2} & =0 \\ 196 & =4𝑘^{2} \\ 𝑘^{2} & =49 \\ |𝑘| & =7\end{aligned}


$$

Since $k$ must be positive, we conclude that $k=7.$

### Worked Example: Reducing to Solving a Quadratic by Factoring

Sometimes, when determining the value of a parameter $k$ that yields one distinct solution to a quadratic equation, we need to solve *another* quadratic equation in the variable $k.$

To demonstrate, suppose we have the equation

$$


4x^2 + 2kx + 8k = 0


$$

has exactly one real solution, where $k$ is a *positive* constant. Let's use this information to find the value of $k$.

A quadratic equation has exactly one real root if the discriminant is equal to zero:

$$


\mathcal{D} = 0.


$$

The coefficients of our quadratic equation are the following:

$$


a = 4, \qquad b = 2k, \qquad c = 8k


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(2𝑘)^{2}−4(4)(8𝑘) \\ & =4𝑘^{2}−128𝑘.\end{aligned}


$$

To have exactly one real solution, we need $\mathcal{D} = 0.$ This gives the following equation:

$$


4k^2 - 128k = 0


$$

Notice that the terms on the left-hand side of this equation have a common factor of $k.$ Thus, we can factor the equation and solve it as follows:

$$


\begin{aligned}4𝑘^{2}−128𝑘 & =0 \\ 4𝑘(𝑘−32) & =0 \\ 𝑘 & =0,32\end{aligned}


$$

Since $k$ must be positive, we conclude that $k=32.$

### Example: Cases Reducing to Solving a Quadratic by Factoring

#### Question

Given that $-3kx^2 - 2kx - 5 = 0,$ where $k$ is a **** constant, has exactly one real solution, what is the value of $k?$

#### Explanation

A quadratic equation has exactly one real root if the discriminant is equal to zero: $\mathcal{D} = 0.$

The coefficients of our quadratic equation are the following:

$$


a = -3k, \qquad b = -2k, \qquad c = -5


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−2𝑘)^{2}−4(−3𝑘)(−5) \\ & =4𝑘^{2}−60𝑘.\end{aligned}


$$

To have exactly one real solution, we need $\mathcal{D} = 0{:}$

$$


\begin{aligned}4𝑘^{2}−60𝑘 & =0 \\ 4𝑘(𝑘−15) & =0 \\ 𝑘 & =0,15\end{aligned}


$$

Since $k$ must be positive, we conclude that $k=15.$
