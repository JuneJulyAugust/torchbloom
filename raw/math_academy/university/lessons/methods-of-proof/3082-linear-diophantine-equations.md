# Linear Diophantine Equations

Source: https://www.mathacademy.com/topics/3082?courseId=76
Topic ID: 3082

## Prerequisites

- [The Extended Euclidean Algorithm](./2677-the-extended-euclidean-algorithm.md)

## Lesson

### Introduction

A **linear Diophantine equation** with two variables $x$ and $y$ takes the form

$$


ax+by=c,


$$

where $a,$ $b,$ and $c$ are integer constants. A **solution of a Diophantine equation** is any integer pair

$$


(x,y)


$$

that satisfies the equation.

For example, the Diophantine equation

$$


2x+3y=9


$$

has an infinite number of integer solutions:

$$


(3, 1), \quad (6, -1), \quad (15, -7), \quad \ldots


$$

### Example: Identifying a Solution of a Linear Diophantine Equation

#### Question

Which of the following pairs $(x,y)$ are solutions of the Diophantine equation $3x+8y=5?$

1. $(7,-2)$

2. $(22,-8)$

3. $(15,-5)$

#### Explanation

Let's check each pair in turn.

- $(7,-2)$ is a solution of our equation. Indeed, substituting $x=7$ and $y=-2,$ we obtain

- $(22,-8)$ is ** a solution of our equation. Substituting $x=22$ and $y=-8,$ we obtain

- $(15,-5)$ is a solution of our equation. Indeed, substituting $x=15$ and $y=-5,$ we obtain

Therefore, the correct answer is "I and III only."

### When a Linear Diophantine Equation Has No Solutions

The linear Diophantine equation

$$


ax+by=c


$$

has a solution if and only if $d \: | \: c,$ where $d = \text{gcd}(a,b).$

Let's use the theorem to test some Diophantine equations.

- Consider the equation Here, we have $a=2,$ $b=10,$ and $c=17.$ Notice that and $2 \!\not{|}\: 17.$ Therefore, according to the theorem, our equation has no solution.

Indeed, notice that the expression on the left-hand side ($2x+10y$) is always an even number, while the right-hand side of the equation ($17$) is an odd number. As a result, there is no solution.

- Consider the equation Here, we have $a=4,$ $b=5,$ and $c=7.$ Since and $1 \:{|}\: 7,$ our equation has solutions.

Indeed, one of the solutions for $4x+5y=7$ is the pair $(3,-1).$

### Example: Identifying Whether a Linear Diophantine Equation Has a Solution

#### Question

Which of the following Diophantine equations have solutions?

1. $18x+15y=24$

2. $7x-28y=10$

3. $9x+27y=16$

#### Explanation

Recall that a linear Diophantine equation

$$


ax+by=c


$$

has a solution if and only if $d \: | \: c,$ where $d = \text{gcd}(a,b).$

With that in mind, let's examine each equation in turn.

- Equation I has solutions. We have $a=18,$ $b=15,$ and $c=24.$ Since and $3 \: | \: 24,$ our equation has solutions.

- Equation II has no solution. We have $a=7,$ $b=-28,$ and $c=10.$ Since and $7 \!\not{|}\: 10,$ our equation has no solution.

- Equation III has no solution. We have $a=9,$ $b=27,$ and $c=16.$ Since and $9 \!\not{|}\: 16,$ our equation has no solution.

Therefore, the correct answer is "I only."

### The General Solution of a Linear Diophantine Equation

If $(x_0,y_0)$ is any particular solution of the equation, then the set of all solutions consists of integer pairs

$$


\left( x_0 + \dfrac{b}{d}t, \: y_0 - \dfrac{a}{d}t \right), \qquad t = 0, \pm 1, \pm2, \ldots \: .


$$

In particular, if $d=1,$ we obtain

$$


\left( x_0 + bt, \: y_0 - at \right), \qquad t = 0, \pm 1, \pm2, \ldots \: .


$$

For example, given that $(x,y)=(4,-1)$ is a solution of the Diophantine equation

$$


4x+5y=11,


$$

find its general solution.

Here, we have $a=4,$ $b=5,$ and $c=11.$ Since $(4,-1)$ is a solution of $4x+5y=11,$ the general solution must be

$$


\begin{aligned}(4+\frac{5}{1}𝑡,\,−1−\frac{4}{1}𝑡) & =(4+5𝑡,\,−1−4𝑡),\end{aligned}


$$

where $t=0, \pm1, \pm2, \ldots \,.$

### Example: Finding the General Solution of a Linear Diophantine Equation Given One of Its Solutions

#### Question

Given that $(x,y)=(15,14)$ is a solution of the Diophantine equation $11x-13y=-17,$ and that $(\overset{\sim}{x},\overset{\sim}{y})$ is the solution with the smallest possible positive value of $x,$ what is the value of $\overset{\sim}{x}?$

#### Explanation

First, recall that a linear Diophantine equation

$$


ax+by=c


$$

has a solution if and only if $d \: | \: c,$ where $d = \text{gcd}(a,b).$ Moreover, if $(x_0,y_0)$ is a solution to the equation, then the general solution is given by

$$


\left(x_0+\dfrac{b}{d}t, \, y_0-\dfrac{a}{d}t\right), \qquad t=0, \pm1, \pm2, \ldots


$$

Here, we have $a=11,$ $b=-13,$ $c=-17,$ and

$$


d=\text{gcd}(11,-13)=1.


$$

Since $(15,14)$ is a solution of $11x-13y=-17,$ the general solution must be

$$


\left(15+\dfrac{(-13)}{1}t, \, 14-\dfrac{11}{1}t\right) = (15-13t, \, 14-11t),


$$

where $t=0, \pm1, \pm2, \ldots \,.$

The smallest possible positive value of $x=15-13t$ is attained when $t=1.$ Therefore,

$$


\overset{\sim}{x} = 15-13 \cdot 1 = 2.


$$

### Example: Solving a Linear Diophantine Equation

#### Question

Consider the Diophantine equation $2x+7y=10.$ The integer pair $(\overset{\sim}{x},\overset{\sim}{y})$ is the solution with the smallest possible positive value of $x.$ What is the value of $\overset{\sim}{x}?$

#### Explanation

We have the linear Diophantine equation

$$


ax+by=c


$$

where $a=2,$ $b=7,$ and $c=10.$ We're given that the equation has solutions.

Notice that our equation can't be solved for either of the two variables using integer coefficients. So, let's find the linear representation of $\text{gcd}(2,7)$ using the extended Euclidean algorithm. First, we apply the forward reduction:

$$


\begin{aligned}\begin{matrix}7 & = & 2⋅3 & + & 1 \\ & ↙ & & ↙ & \\ 2 & = & 1⋅2 & + & 0\end{matrix}\end{aligned}


$$

Solving for the remainders (the rightmost terms) in the equations above, we get

$$


\begin{aligned}1 & =7−2⋅3.\end{aligned}


$$

As a result, we obtain that $d=\text{gcd}(a,b) = 1$ and

$$


2 \cdot (-3) + 7 = 1.


$$

Multiplying this equation by $10,$ we get

$$


\begin{aligned}2⋅(−3)+7 & =1 \\ 2⋅(−3)⋅10+7⋅10 & =10 \\ 2⋅(−30)+7⋅10 & =10,\end{aligned}


$$

which means that $(x,y)=(-30,10)$ is a solution to our Diophantine equation.

Now, the general solution is

$$


\left(-30+\dfrac{b}{d}t, \, 10-\dfrac{a}{d}t\right) = (-30+7t, \, 10-2t),


$$

where $t=0, \pm1, \pm2, \ldots \,.$

The smallest possible positive value of $x=-30+7t$ is attained when $t=5.$ Therefore,

$$


\overset{\sim}{x} = -30+7 \cdot 5 = 5.


$$
