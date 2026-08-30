# Second-Order Inhomogeneous Boundary Value Problems

Source: https://www.mathacademy.com/topics/6710?courseId=155
Topic ID: 6710

## Prerequisites

- [Second-Order Homogeneous Boundary Value Problems](./6711-second-order-homogeneous-boundary-value-problems.md)

## Lesson

### Introduction

When solving an inhomogeneous BVP, it is important to know whether the boundary conditions determine a unique solution. In this topic, we will learn how the solution behavior of an **inhomogeneous BVP** depends on the corresponding **homogeneous BVP**.

Suppose we have the second-order **inhomogeneous boundary value problem (BVP)**

$$


y''(x) + P(x)y'(x) + Q(x)y(x) = f(x), \qquad a \le x \le b


$$

with the Robin (mixed) boundary conditions

$$


\alpha_1 y(a) + \beta_1 y'(a) = \gamma_1, \qquad \alpha_2 y(b) + \beta_2 y'(b) = \gamma_2.


$$

Let the **associated homogeneous BVP** be

$$


y''(x) + P(x)y'(x) + Q(x)y(x) = 0, \qquad a \le x \le b


$$

with the boundary conditions

$$


\alpha_1 y(a) + \beta_1 y'(a) = 0, \qquad \alpha_2 y(b) + \beta_2 y'(b) = 0.


$$

Then we have the following:

The inhomogeneous BVP has a **unique solution** if and only if the associated homogeneous BVP has only the **trivial solution** $y \equiv 0.$

We interpret this as follows:

- If the homogeneous BVP has only the *trivial solution* $y \equiv 0,$ then the inhomogeneous BVP has a *unique solution*.

- If the homogeneous BVP has (infinitely many) *nontrivial solutions*, then the inhomogeneous BVP either has *infinitely many solutions* or *no solution*.

In particular, if the inhomogeneous BVP has one solution $y_p$ and the homogeneous BVP has a nontrivial solution $y_c,$ then

$$


y = c\,y_c + y_p


$$

is a solution for every $c\in\mathbb R.$ Therefore, the inhomogeneous BVP has infinitely many solutions.

In the next slide, we'll show how to use this criterion if the general solution of the homogeneous BVP is known.

### Using the Criteria if the Solution of the Homogeneous BVP Is Known

Suppose the second-order homogeneous BVP

with the homogeneous boundary conditions

$$


\alpha_1 y(a) + \beta_1 y'(a) = 0, \qquad \alpha_2 y(b) + \beta_2 y'(b) = 0


$$

has the fundamental solutions $y_1(x)$ and $y_2(x).$ Then, the general solution is given by $y_c(x) = c_1 y_1(x) + c_2 y_2(x).$

Substituting this into the boundary conditions yields a linear system for the constants $c_1, c_2$ with coefficient matrix $A$:

$$


[\begin{aligned}\,𝛼_{1}𝑦_{1}(𝑎)+𝛽_{1}𝑦_{′1}(𝑎) & 𝛼_{1}𝑦_{2}(𝑎)+𝛽_{1}𝑦_{′2}(𝑎) \\ 𝛼_{2}𝑦_{1}(𝑏)+𝛽_{2}𝑦_{′1}(𝑏) & 𝛼_{2}𝑦_{2}(𝑏)+𝛽_{2}𝑦_{′2}(𝑏)\end{aligned}]


$$

As we know, the homogeneous BVP has a **unique, trivial solution** $y \equiv 0$ if and only if $\det(A) \neq 0.$

Consequently, our inhomogeneous BVP

$$


y''(x) + P(x)y'(x) + Q(x)y(x) = f(x), \qquad a \le x \le b


$$

with the Robin boundary conditions

$$


\alpha_1 y(a) + \beta_1 y'(a) = \gamma_1, \qquad \alpha_2 y(b) + \beta_2 y'(b) = \gamma_2.


$$

has a *unique solution* if and only $\det(A) \neq 0.$

We summarize as follows:

- If $\det(A) \neq 0,$ then the inhomogeneous BVP has a *unique solution*.

- If $\det(A) = 0,$ then the inhomogeneous BVP either has *infinitely many solutions* or *no solution*.

We'll see how this works with concrete examples on the next slides.

### Example: Classifying Solutions of Inhomogeneous BVPs

#### Question

Consider the following boundary value problem (BVP).

$$


y'' + 16y = x^3 e^{x}, \qquad y'(0) = y'(\pi) = 0,\quad 0\leq x \leq \pi


$$

Let $y_1(x)$ and $y_2(x)$ be the fundamental solutions, and suppose we define the matrix $A$ as

$$


[\begin{aligned}𝑦_{′1}(0) & 𝑦_{′2}(0) \\ 𝑦_{′1}(𝜋) & 𝑦_{′2}(𝜋)\end{aligned}]


$$

Fill in the correct options in the reasoning below.

$\quad$ The absolute value of $\det(A)$ is $𝐴𝐴𝐴𝐴𝐴$

$\quad$ Therefore, the corresponding homogeneous BVP $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$

$\quad$ Therefore, our inhomogeneous BVP $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$

#### Explanation

Suppose we have the second-order inhomogeneous boundary value problem (BVP)

$$


y''(x) + P(x)y' + Q(x)y = f(x), \qquad a \leq x \leq b


$$

with the Robin (mixed) boundary conditions

$$


\alpha_1 y(a) + \beta_1 y'(a) = \gamma_1, \qquad \alpha_2 y(b) + \beta_2 y'(b) = \gamma_2


$$

where $P, Q,$ and $f$ are continuous on $[a,b],$ and $\alpha_i$ and $\beta_i$ are real constants such that $(\alpha_i, \beta_i) \neq (0,0).$

The inhomogeneous BVP has at most one solution if and only if the associated homogeneous BVP has only the trivial solution $y \equiv 0.$ Specifically:

- If the homogeneous BVP has the unique solution $y \equiv 0,$ then the inhomogeneous problem either has no solution or a unique solution.

- If the homogeneous BVP has (infinitely many) nontrivial solutions, then the inhomogeneous problem either has infinitely many solutions or no solution.

To classify the solutions of the corresponding homogeneous BVP, we define the matrix $A$ as

$$


[\begin{aligned}\,𝛼_{1}𝑦_{1}(𝑎)+𝛽_{1}𝑦_{′1}(𝑎) & 𝛼_{1}𝑦_{2}(𝑎)+𝛽_{1}𝑦_{′2}(𝑎) \\ 𝛼_{2}𝑦_{1}(𝑏)+𝛽_{2}𝑦_{′1}(𝑏) & 𝛼_{2}𝑦_{2}(𝑏)+𝛽_{2}𝑦_{′2}(𝑏)\end{aligned}]


$$

The homogeneous BVP has a unique, trivial solution $y \equiv 0$ if and only if $\det(A) \neq 0.$ In other words, if the determinant equals zero, then the homogeneous BVP has **.

Notice that, in our case, we have Neumann boundary conditions. So, setting $\alpha_i = 0, \beta_i = 1, a = 0,$ and $b = \pi,$ the matrix $A$ reduces to

$$


[\begin{aligned}𝑦_{′1}(0) & 𝑦_{′2}(0) \\ 𝑦_{′1}(𝜋) & 𝑦_{′2}(𝜋)\end{aligned}]


$$

To find the fundamental solutions, we set $y = e^{m x}.$ The auxiliary equation is

$$


\begin{aligned}𝑚^{2}+16 & =0.\end{aligned}


$$

So, we have $m = \pm 4\textrm i.$ So, the fundamental solutions are

$$


y_1(x) = \cos 4x, \qquad y_2(x) = \sin 4x.


$$

Differentiating, we have

$$


y_1'(x) = -4\sin 4x, \qquad y_2'(x) = 4\cos 4x.


$$

Therefore, the matrix $A$ is

$$


\begin{aligned}𝐴 & =[\begin{matrix}−4sin⁡(4⋅0) & 4cos⁡(4⋅0) \\ −4sin⁡(4⋅𝜋) & 4cos⁡(4⋅𝜋)\end{matrix}] \\ & =[\begin{matrix}0 & 4 \\ 0 & 4\end{matrix}]\end{aligned}


$$

and we have

$$


\begin{aligned}|det(𝐴)| & =|0⋅4−4⋅0| \\ & =0.\end{aligned}


$$

Since $\det(A) = 0,$ the corresponding homogeneous BVP $\text{has infinitely many solutions}.$

Therefore, since the corresponding homogeneous BVP has (infinitely many) nontrivial solutions, our inhomogeneous BVP $\text{has infinitely many solutions or no solution}.$

### Example: Solving Solvable Inhomogeneous BVPs With Infinitely Many Solutions

#### Question

Consider the following boundary value problem (BVP).

$$


y'' + 16y = \sin 4x, \qquad y(0) = 0, \quad y(\pi) = -\dfrac\pi 8,\quad 0\leq x \leq \pi


$$

The solution is given by

$$


y = f(x) + B \cdot g(x)


$$

where $B\in \mathbb R$ is arbitrary. Find the functions $f(x)$ and $g(x).$

#### Explanation

Suppose we have the second-order inhomogeneous boundary value problem (BVP)

$$


y''(x) + P(x)y' + Q(x)y = f(x), \qquad a \leq x \leq b


$$

with the Robin (mixed) boundary conditions

$$


\alpha_1 y(a) + \beta_1 y'(a) = \gamma_1, \qquad \alpha_2 y(b) + \beta_2 y'(b) = \gamma_2


$$

where $P, Q,$ and $f$ are continuous on $[a,b],$ and $\alpha_i$ and $\beta_i$ are real constants such that $(\alpha_i, \beta_i) \neq (0,0).$

If the associated homogeneous BVP has nontrivial solutions, then the inhomogeneous BVP has either no solution or infinitely many solutions.

To find the solution of an inhomogeneous boundary value problem (BVP):

- First, we find the general solution $y_h(x)$ of the corresponding homogeneous equation.

- Then, we find a particular solution $y_p(x)$ of the inhomogeneous equation.

- Finally, we apply the boundary conditions to determine the arbitrary constants.

To find the fundamental solutions, we set $y = e^{m x}.$ The auxiliary equation is

$$


\begin{aligned}𝑚^{2}+16 & =0.\end{aligned}


$$

So, we have $m = \pm 4\textrm i.$ So, the fundamental solutions are

$$


y_1(x) = \cos 4x, \qquad y_2(x) = \sin 4x


$$

and the general solution to the homogeneous equation is

$$


y_h = A\cos 4x + B\sin 4x.


$$

Next, we seek a particular solution of the form

$$


y_p(x) = Cx\cos 4x + Dx\sin 4x


$$

Differentiating, we get

$$


\begin{aligned}𝑦_{′𝑝}(𝑥) & =𝐶cos⁡4𝑥−4𝐶𝑥sin⁡4𝑥+𝐷sin⁡4𝑥+4𝐷𝑥cos⁡4𝑥 \\ 𝑦_{″𝑝}(𝑥) & =−8𝐶sin⁡4𝑥−16𝐶𝑥cos⁡4𝑥+8𝐷cos⁡4𝑥−16𝐷𝑥sin⁡4𝑥\end{aligned}


$$

Substituting this into the equation, we reach (after some cancellation)

$$


\begin{aligned}−8𝐶sin⁡4𝑥+8𝐷cos⁡4𝑥=sin⁡4𝑥\end{aligned}


$$

which gives $C = -\dfrac18$ and $D = 0.$ Therefore, our general solution is

$$


y = A\cos 4x + B\sin 4x -\dfrac18x\cos4x.


$$

Applying the condition $y(0) = 0$ gives

$$


A\cos (4\cdot 0) + B\sin (4\cdot 0) - \dfrac18 \cdot 0 \cdot \cos (4\cdot 0) = 0


$$

which gives $A = 0.$ So, we have

$$


y = B\sin 4x -\dfrac18x\cos 4x.


$$

Applying the condition $y(\pi) = -\dfrac\pi8$ gives

$$


\begin{aligned}𝐵sin⁡(4𝜋)−\frac{𝜋}{8}cos⁡(4𝜋)=−\frac{𝜋}{8} \\ 0−\frac{𝜋}{8}=−\frac{𝜋}{8}\end{aligned}


$$

which is true for all values of $B$

Therefore, the solution to the boundary value problem is

$$


\begin{aligned}𝑦(𝑥) & =−\frac{1}{8}𝑥cos⁡4𝑥+𝐵⋅sin⁡4𝑥.\end{aligned}


$$

where $B$ is arbitrary.

Finally,

$$


f(x) = -\dfrac18 x\cos 4x, \qquad g(x) = \sin 4x.


$$

****: The associated homogeneous BVP

$$


y'' + 16y = 0, \qquad y(0) = 0, \quad y(\pi) = 0,\quad 0\leq x \leq \pi


$$

has infinitely many solutions. Therefore, the inhomogeneous BVP has either infinitely many solutions or no solution. Since we have found a solution that contains an arbitrary constant and satisfies both boundary conditions, the BVP has infinitely many solutions.

### Example: Solving Solvable Inhomogeneous BVPs With a Unique Solutions

#### Question

Consider the following boundary value problem (BVP).

$$


y'' - 9y = -9x - 3, \qquad y(1) = \dfrac{4}{3}, \quad y(2) = \dfrac{13}{3},\quad 1\leq x \leq 2


$$

The solution is given by

$$


y = Ae^{3x} + Be^{-3x} + g(x).


$$

Find the constants $A$ and $B,$ and the function $g(x).$

#### Explanation

Suppose we have the second-order inhomogeneous boundary value problem (BVP)

$$


y''(x) + P(x)y' + Q(x)y = f(x), \qquad a \leq x \leq b


$$

with the Robin (mixed) boundary conditions

$$


\alpha_1 y(a) + \beta_1 y'(a) = \gamma_1, \qquad \alpha_2 y(b) + \beta_2 y'(b) = \gamma_2


$$

where $P, Q,$ and $f$ are continuous on $[a,b],$ and $\alpha_i$ and $\beta_i$ are real constants such that $(\alpha_i, \beta_i) \neq (0,0).$

The inhomogeneous BVP has at most one solution if and only if the associated homogeneous BVP has only the trivial solution $y \equiv 0.$

To find the solution of an inhomogeneous boundary value problem (BVP):

- First, we find the general solution $y_h(x)$ of the corresponding homogeneous equation.

- Then, we find a particular solution $y_p(x)$ of the inhomogeneous equation.

- Finally, we apply the boundary conditions to determine the arbitrary constants.

The homogeneous equation is

$$


y'' - 9y = 0.


$$

To find the fundamental solutions, we set $y = e^{m x}.$ The auxiliary equation is

$$


\begin{aligned}𝑚^{2}−9 & =0 \\ (𝑚−3)(𝑚+3) & =0\end{aligned}


$$

So, we have $m = 3$ and $m = -3.$ So, the fundamental solutions are

$$


y_1(x) = e^{3x}, \qquad y_2(x) = e^{-3x}.


$$

Therefore, the general solution to the homogeneous equation is

$$


y_h = Ae^{3x} + Be^{-3x}.


$$

Now, we seek a particular solution $y_p$ of the form

$$


y_p = Cx + D.


$$

Substituting this into our inhomogeneous equation, we get

$$


\begin{aligned}(𝐶𝑥+𝐷)^{″}−9(𝐶𝑥+𝐷) & =−9𝑥−3 \\ −9(𝐶𝑥+𝐷) & =−9𝑥−3 \\ −9𝐶𝑥−9𝐷 & =−9𝑥−3.\end{aligned}


$$

Equating coefficients of $x$ and constants, respectively, we get

$$


\begin{aligned}−9𝐶=−9\, & ⇒\,𝐶=1 \\ −9𝐷=−3\, & ⇒\,𝐷=\frac{1}{3}\end{aligned}


$$

Therefore, the particular solution is

$$


y_p = x + \dfrac13


$$

and the general solution is

$$


\begin{aligned}𝑦 & =𝑦_{ℎ}+𝑦_{𝑝} \\ & =𝐴𝑒^{3𝑥}+𝐵𝑒^{−3𝑥}+𝑥+\frac{1}{3}.\end{aligned}


$$

Applying the condition $y(1) = \dfrac{4}{3}$ gives

$$


Ae^3 + Be^{-3} +\dfrac43 = \dfrac{4}{3} \qquad \Rightarrow\qquad B = - Ae^6.


$$

So, we have

$$


y = Ae^{3x} - Ae^{-3x+6} + x +\dfrac13.


$$

Applying the condition $y(2) = \dfrac{13}{3}$ gives

$$


Ae^6 - Ae^{0} +2 + \dfrac13 = \dfrac{13}{3} \qquad \Rightarrow\qquad Ae^6 - A = 2.


$$

Solving for $A,$ we have

$$


A = \dfrac{2}{e^6-1}.


$$

Substituting back into the first equation and solving for $B,$ we have

$$


B = - Ae^6 = -\dfrac{2e^6}{e^6-1}.


$$

Finally, for the function $g(x),$ we have

$$


g(x) = y_p(x) = x + \dfrac13.


$$

****: The associated homogeneous BVP

$$


y'' - 9y = 0, \qquad y(1) = 0, \quad y(2) = 0,\quad 1\leq x \leq 2


$$

has only the trivial solution $y\equiv 0.$ Therefore, the inhomogeneous BVP has at most one solution. Since we have found a solution satisfying both boundary conditions, the solution to this inhomogeneous BVP is unique.
