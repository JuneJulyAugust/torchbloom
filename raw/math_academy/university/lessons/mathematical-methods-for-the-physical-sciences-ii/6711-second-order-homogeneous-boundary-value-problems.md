# Second-Order Homogeneous Boundary Value Problems

Source: https://www.mathacademy.com/topics/6711?courseId=155
Topic ID: 6711

## Prerequisites

- [Second-Order Homogeneous ODEs: Characteristic Equations With Complex Roots](../differential-equations/880-second-order-homogeneous-odes-characteristic-equations-with-complex-roots.md)
- [The Invertible Matrix Theorem in Terms of 2x2 Systems of Equations](../linear-algebra/1730-the-invertible-matrix-theorem-in-terms-of-2x2-systems-of-equations.md)
- [Introduction to Boundary Value Problems](./2742-introduction-to-boundary-value-problems.md)

## Lesson

### Introduction

Suppose we have the second-order homogeneous boundary value (BVP) problem

$$


y''(x) + P(x)y' + Q(x)y = 0, \qquad a \leq x \leq b


$$

with the *Robin (mixed) boundary conditions*

$$


\alpha_1 y(a) + \beta_1 y'(a) = 0, \qquad \alpha_2 y(b) + \beta_2 y'(b) = 0


$$

where $P$ and $Q$ are continuous on $[a,b],$ and $\alpha_i$ and $\beta_i$ are real constants such that $(\alpha_i, \beta_i) \neq (0,0).$ Furthermore, suppose the fundamental solutions to the equation are $y_1(x)$ and $y_2(x).$

The general solution is given by $y(x) = c_1 y_1(x) + c_2 y_2(x).$ Substituting this into the boundary conditions yields a linear system for the constants $c_1, c_2$ with coefficient matrix $A$:

$$


[\begin{aligned}\,𝛼_{1}𝑦_{1}(𝑎)+𝛽_{1}𝑦_{′1}^{}(𝑎) & 𝛼_{1}𝑦_{2}(𝑎)+𝛽_{1}𝑦_{′2}^{}(𝑎) \\ 𝛼_{2}𝑦_{1}(𝑏)+𝛽_{2}𝑦_{′1}^{}(𝑏) & 𝛼_{2}𝑦_{2}(𝑏)+𝛽_{2}𝑦_{′2}^{}(𝑏)\end{aligned}]


$$

Then, we have the following theorem:

The BVP has a **unique, trivial solution** $y \equiv 0$ if and only if $\det(A) \neq 0.$

In other words, if the determinant equals zero, then the BVP has *infinitely many solutions* (since $y \equiv 0$ is *always* a solution to the BVP).

Let's see a concrete example.

### A Worked Example

Consider the following boundary value problem (BVP).

$$


y'' + 9y = 0, \qquad y(0) = 0, \quad y\!\left(\dfrac{\pi}{6}\right) = 0,\quad 0\leq x \leq \dfrac{\pi}{6}


$$

First, we solve the differential equation to find the *fundamental solutions*, $y_1(x)$ and $y_2(x).$

Set $y = e^{m x}.$ The auxiliary equation is

$$


m^2 + 9 = 0.


$$

So, we have $m = \pm 3i,$ and thus the fundamental solutions are

$$


y_1(x) = \cos 3x \qquad\textrm{and}\qquad y_2(x) = \sin 3x.


$$

Then, we construct the boundary condition matrix.

The BVP has a unique, trivial solution $y \equiv 0$ if and only if the determinant of the boundary matrix $A$ is non-zero. Notice that our boundary conditions are in the form $\alpha y + \beta y' = 0$ with coefficients:

$$


1 \cdot y(0) + 0 \cdot y'(0) = 0, \qquad 1 \cdot y\left(\dfrac{\pi}{6}\right) + 0 \cdot y'\left(\dfrac{\pi}{6}\right) = 0.


$$

We define the matrix $A$ using these coefficients and our fundamental solutions:

$$


\begin{aligned}𝐴 & =\begin{aligned}1⋅𝑦_{1}(0)+0⋅𝑦_{′1}^{}(0) & 1⋅𝑦_{2}(0)+0⋅𝑦_{′2}^{}(0) \\ 1⋅𝑦_{1}(\frac{𝜋}{6})+0⋅𝑦_{′1}^{}(\frac{𝜋}{6}) & 1⋅𝑦_{2}(\frac{𝜋}{6})+0⋅𝑦_{′2}^{}(\frac{𝜋}{6})\end{aligned} \\ & =\begin{aligned}cos⁡(0) & sin⁡(0) \\ cos\,(\frac{𝜋}{2}) & sin\,(\frac{𝜋}{2})\end{aligned} \\ & =[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}].\end{aligned}


$$

Finally, we calculate the determinant:

$$


\det(A) = (1)(1) - (0)(0) = 1.


$$

Since $\det(A)\neq 0,$ we conclude that this BVP has the unique solution $y\equiv 0.$

### Example: Classifying Solutions of Homogeneous BVPs

#### Question

Consider the following boundary value problem (BVP).

$$


y'' - 2y' - 3y = 0, \qquad y'(1) = y'(3) = 0,\quad 1\le x\le3


$$

Let $y_1(x)$ and $y_2(x)$ be the fundamental solutions, and suppose we define the matrix $A$ as

$$


[\begin{aligned}𝑦_{′1}^{}(1) & 𝑦_{′2}^{}(1) \\ 𝑦_{′1}^{}(3) & 𝑦_{′2}^{}(3)\end{aligned}]


$$

Find the fundamental solutions and use $A$ to determine if the given BVP has a unique or infinitely many solutions.

#### Explanation

Suppose we have the second-order homogeneous boundary value (BVP) problem

$$


y''(x)+P(x)y'(x)+Q(x)y=0,\qquad a\le x\le b


$$

with the Robin (mixed) boundary conditions

$$


\alpha_{1}y(a)+\beta_{1}y'(a)=0,\qquad \alpha_{2}y(b)+\beta_{2}y'(b)=0,


$$

where $P$ and $Q$ are continuous on $[a,b],$ and $\alpha_i, \beta_i$ are real constants such that $(\alpha_i,\beta_i)\ne(0,0).$ Furthermore, suppose the fundamental solutions to the equation are $y_1(x)$ and $y_2(x).$

Now, let's define the following matrix:

$$


[\begin{aligned}𝛼_{1}𝑦_{1}(𝑎)+𝛽_{1}𝑦_{′1}^{}(𝑎) & 𝛼_{1}𝑦_{2}(𝑎)+𝛽_{1}𝑦_{′2}^{}(𝑎) \\ 𝛼_{2}𝑦_{1}(𝑏)+𝛽_{2}𝑦_{′1}^{}(𝑏) & 𝛼_{2}𝑦_{2}(𝑏)+𝛽_{2}𝑦_{′2}^{}(𝑏)\end{aligned}]


$$

Then, the BVP has a unique, trivial solution $y\equiv0$ if and only if $\det(A)\ne0.$ In other words, if the determinant equals zero, then the BVP has **.

Notice that, in our case, we have Neumann boundary conditions. So, setting $\alpha_i=0,$ $\beta_i=1,$ $a=1,$ and $b=3,$ the matrix $A$ reduces to

$$


[\begin{aligned}𝑦_{′1}^{}(1) & 𝑦_{′2}^{}(1) \\ 𝑦_{′1}^{}(3) & 𝑦_{′2}^{}(3)\end{aligned}]


$$

To find the fundamental solutions, we set $y=e^{mx}.$ The auxiliary equation is

$$


\begin{aligned}𝑚^{2}−2𝑚−3 & =0 \\ (𝑚−3)(𝑚+1) & =0.\end{aligned}


$$

So, we have $m=3$ and $m=-1,$ and so the fundamental solutions are

$$


y_{1}(x)=e^{3x}\;\textrm{and}\;y_{2}(x)=e^{-x}.


$$

Differentiating, we have

$$


y_1'(x) = 3e^{3x}, \qquad y_2'(x) = -e^{-x}.


$$

Therefore, the matrix $A$ is

$$


\begin{aligned}𝐴 & =[\begin{aligned}3𝑒^{3(1)} & −𝑒^{−1} \\ 3𝑒^{3(3)} & −𝑒^{−3}\end{aligned}] \\ & =[\begin{aligned}3𝑒^{3} & −𝑒^{−1} \\ 3𝑒^{9} & −𝑒^{−3}\end{aligned}],\end{aligned}


$$

and we have

$$


\begin{aligned}det(𝐴) & =(3𝑒^{3})(−𝑒^{−3})−(−𝑒^{−1})(3𝑒^{9}) \\ & =−3+3𝑒^{8} \\ & =3(𝑒^{8}−1).\end{aligned}


$$

Since $\det(A)\ne0,$ we conclude that this BVP has the unique trivial solution $y\equiv0.$

### Solving BVPs with Non-Trivial Solutions

Now, we'll learn how to find non-trivial solutions.

For example, consider the following boundary value problem:

$$


y'' + 9y = 0, \qquad y(0) = 0,\quad y'\!\left(\dfrac{\pi}{6}\right) = 0,\quad 0\leq x \leq \dfrac{\pi}{6}


$$

To solve the homogeneous boundary value problem, we first find the general solution and then determine the values of the arbitrary constants that fit the boundary conditions.

To find the fundamental solutions, we set $y = e^{m x}.$ The auxiliary equation is

$$


\begin{aligned}𝑚^{2}+9 & =0.\end{aligned}


$$

This yields $m = \pm 3\textrm i.$ Thus, the fundamental solutions are

$$


y_1(x) = \cos 3x, \qquad y_2(x) = \sin 3x.


$$

Therefore, the general solution is

$$


y = A\cos 3x + B\sin 3x.


$$

Differentiating, we have

$$


y' = -3A\sin 3x + 3B\cos 3x.


$$

Next, we use the boundary conditions:

- Applying the condition $y(0) = 0,$ we have So, the solution simplifies to $y = B\sin 3x,$ and its derivative is $y' = 3B\cos 3x.$

- Applying the condition $y'\!\left(\dfrac{\pi}{6}\right) = 0,$ we have which is automatically satisfied for any $B.$

Therefore, the solution to the BVP is

$$


y = B \, \sin 3x,


$$

where $B$ is arbitrary.

### Example: Solving Homogeneous BVPs With Nontrivial Solutions

#### Question

Consider the following boundary value problem.

$$


y'' = 0, \qquad y(4) = 0, \quad y(3) + y'(3) = 0,\quad 3\leq x \leq 4


$$

Find the solution to this boundary value problem in terms of an arbitrary constant $A.$

#### Explanation

To solve the homogeneous boundary value problem, we first find the general solution and then determine the values of the arbitrary constants that fit the boundary conditions.

We have the equation

$$


y''(x) = 0.


$$

Integrating this equation twice, we get the general solution

$$


y = Ax + B.


$$

Differentiating, we have

$$


y' = A.


$$

Applying the condition $y(4) = 0,$ we have

$$


4A + B = 0 \quad\Rightarrow\quad B = -4A.


$$

So, we have

$$


y = Ax - 4A = A(x-4).


$$

Applying the condition $y(3) + y'(3) = 0,$ we have

$$


-A+A = 0,


$$

which is automatically satisfied for any $A.$

Therefore, the solution to the BVP is $y = A\cdot \left(x-4\right),$ where $A$ is arbitrary.

### Proof of the Theorem

Recall that we are considering the second-order homogeneous boundary value (BVP) problem

$$


y''(x) + P(x)y' + Q(x)y = 0, \qquad a \leq x \leq b


$$

with the Robin (mixed) boundary conditions

$$


\alpha_1 y(a) + \beta_1 y'(a) = 0, \qquad \alpha_2 y(b) + \beta_2 y'(b) = 0


$$

where $P$ and $Q$ are continuous on $[a,b],$ and $\alpha_i$ and $\beta_i$ are real constants such that $(\alpha_i, \beta_i) \neq (0,0).$ Furthermore, suppose the fundamental solutions to the equation are $y_1(x)$ and $y_2(x).$

If we define the matrix

$$


[\begin{aligned}\,𝛼_{1}𝑦_{1}(𝑎)+𝛽_{1}𝑦_{′1}^{}(𝑎) & 𝛼_{1}𝑦_{2}(𝑎)+𝛽_{1}𝑦_{′2}^{}(𝑎) \\ 𝛼_{2}𝑦_{1}(𝑏)+𝛽_{2}𝑦_{′1}^{}(𝑏) & 𝛼_{2}𝑦_{2}(𝑏)+𝛽_{2}𝑦_{′2}^{}(𝑏)\end{aligned}]


$$

then we have the following theorem:

The BVP has a unique, trivial solution $y \equiv 0$ if and only if $\det(A) \neq 0.$

**Proof:**

Since $y_1(x)$ and $y_2(x)$ are fundamental solutions of the equation, the general solution is

$$


y(x) = c_1 y_1(x) + c_2 y_2(x)


$$

where $c_1$ and $c_2$ are constants. Therefore,

$$


y'(x) = c_1 y_1'(x) + c_2 y_2'(x).


$$

- Using the first boundary condition, we have and regrouping the terms, we have

- Using the second boundary condition, we have and regrouping the terms, we have

Thus, we have the following system of equations

$$


\begin{aligned}𝑐_{1}(𝛼_{1}𝑦_{1}(𝑎)+𝛽_{1}𝑦_{′1}^{}(𝑎))+𝑐_{2}(𝛼_{1}𝑦_{2}(𝑎)+𝛽_{1}𝑦_{′2}^{}(𝑎))=0 \\ 𝑐_{1}(𝛼_{2}𝑦_{1}(𝑏)+𝛽_{2}𝑦_{′1}^{}(𝑏))+𝑐_{2}(𝛼_{2}𝑦_{2}(𝑏)+𝛽_{2}𝑦_{′2}^{}(𝑏))=0\end{aligned}


$$

which we can write in matrix form as

$$


A\,\mathbf c = \mathbf 0


$$

where $\mathbf c = [c_1, c_2]^T.$

By the *Invertible Matrix Theorem*, the *only* solution to this system is $\mathbf c = \mathbf 0$ if and only if $\det(A) \neq 0.$ Since $\mathbf c = \mathbf 0$ implies $y(x) \equiv 0,$ the theorem is proved.
