# Linear Approximations Near Equilibria

Source: https://www.mathacademy.com/topics/6378?courseId=61
Topic ID: 6378

## Prerequisites

- [The Derivative of a Multivariable Function](../multivariable-calculus/4169-the-derivative-of-a-multivariable-function.md)
- [Shifted Systems of ODEs](./6380-shifted-systems-of-odes.md)

## Lesson

### Introduction

Consider an autonomous system written as

$$


\mathbf{x}'=\boldsymbol{f}(\mathbf{x}),


$$

where $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ and $[\begin{aligned}𝑓_{1}(𝑥,𝑦) \\ 𝑓_{2}(𝑥,𝑦)\end{aligned}]$.

The system is called **almost linear** at an equilibrium point $\mathbf{x}^\ast$ if the Jacobian determinant at this point is nonzero there, i.e.

$$


\det\!\bigl(\boldsymbol{f}'(\mathbf{x}^\ast)\bigr)\neq 0.


$$

For example, let

$$


[\begin{aligned}𝑥+𝑦+𝑦^{2} \\ 𝑥+𝑦\end{aligned}]


$$

First, notice that $\boldsymbol{f}(\mathbf{x}^\ast)=\mathbf{0},$ so $\mathbf{x}^\ast$ is an equilibrium.

Now, we compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥+𝑦+𝑦^{2})=1,\, & \frac{𝜕𝑓_{1}}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑥+𝑦+𝑦^{2})=1+2𝑦 \\ \frac{𝜕𝑓_{2}}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥+𝑦)=1,\, & \frac{𝜕𝑓_{2}}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑥+𝑦)=1\end{aligned}


$$

Thus, we have

$$


\begin{aligned}1 & 1+2𝑦 \\ 1 & 1\end{aligned}


$$

Next, we evaluate the Jacobian at the equilibrium $[\begin{aligned}0 \\ 0\end{aligned}]$ to get

$$


\begin{aligned}𝐽(0,0) & =\begin{aligned}1 & 1+2(0) \\ 1 & 1\end{aligned} \\ & =\begin{aligned}1 & 1 \\ 1 & 1\end{aligned} \\ & =0.\end{aligned}


$$

Finally, since the Jacobian is $0,$ the system is *not* almost linear at $\mathbf{x}^\ast$.

### Example: Identifying Almost Linear Systems

#### Question

Given the system of differential equations, determine whether the system is almost linear at the equilibrium point $\mathbf{x}^\ast= [0, \: 0]^T.$

$$


\begin{aligned}𝑥^{′}(𝑡)=−𝑦^{2}(𝑡)+1−𝑒^{𝑥(𝑡)} \\ 𝑦^{′}(𝑡)=−𝑥^{2}(𝑡)+1−𝑒^{𝑦(𝑡)}\end{aligned}


$$

#### Explanation

The system can be rewritten in matrix form as

$$


\mathbf{x}' = \boldsymbol{f}(\mathbf{x})


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ and $[\begin{aligned}−𝑦^{2}+1−𝑒^{𝑥} \\ −𝑥^{2}+1−𝑒^{𝑦}\end{aligned}]$

We need to compute the Jacobian determinant of $\boldsymbol{f}(\mathbf{x}).$

In our case, we have the following:

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥} & \frac{𝜕𝑓_{1}}{𝜕𝑦} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥} & \frac{𝜕𝑓_{2}}{𝜕𝑦}\end{aligned}


$$

First, we compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(−𝑦^{2}+1−𝑒^{𝑥})=−𝑒^{𝑥},\, & \frac{𝜕𝑓_{1}}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(−𝑦^{2}+1−𝑒^{𝑥})=−2𝑦 \\ \frac{𝜕𝑓_{2}}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(−𝑥^{2}+1−𝑒^{𝑦})=−2𝑥,\, & \frac{𝜕𝑓_{2}}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(−𝑥^{2}+1−𝑒^{𝑦})=−𝑒^{𝑦}\end{aligned}


$$

Thus, we have

$$


\begin{aligned}−𝑒^{𝑥} & −2𝑦 \\ −2𝑥 & −𝑒^{𝑦}\end{aligned}


$$

Next, we evaluate the Jacobian at the equilibrium $[\begin{aligned}0 \\ 0\end{aligned}]$ to get

$$


\begin{aligned}𝐽(0,0) & =\begin{aligned}−𝑒^{0} & −2(0) \\ −2(0) & −𝑒^{0}\end{aligned} \\ & =\begin{aligned}−1 & 0 \\ 0 & −1\end{aligned} \\ & =(−1)(−1)−(0)(0) \\ & =1 \\ & ≠0.\end{aligned}


$$

Finally, since the Jacobian determinant is not zero, our system is $\boxed{\text{almost linear}}$ at $\mathbf{x}^\ast.$

### Linear Approximations Near Equilibria

Suppose the system

$$


\mathbf{x}'=\boldsymbol{f}(\mathbf{x}),


$$

is almost linear at an equilibrium $\mathbf{x}^\ast.$ In this case, the system's behavior near $\mathbf{x}^\ast$ can be approximated by a linear system.

First, we define the deviation from equilibrium by

$$


\mathbf{u}=\mathbf{x}-\mathbf{x}^\ast.


$$

Small values of $\mathbf{u}$ correspond to points close to the equilibrium.

Next, assuming $\mathbf{x} = [x, y]^T,$ we compute the Jacobian matrix

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥} & \frac{𝜕𝑓_{1}}{𝜕𝑦} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥} & \frac{𝜕𝑓_{2}}{𝜕𝑦}\end{aligned}


$$

and evaluate it at $\mathbf{x}^\ast$ to obtain the constant matrix $J = \boldsymbol{f}'(\mathbf{x}^\ast).$

Finally, since $\boldsymbol{f}(\mathbf{x}^\ast)=\mathbf{0},$ the nonlinear system can be approximated by the **linearized system**

$$


\mathbf{u}'= J \mathbf{u}.


$$

This linear system captures the leading-order behavior of solutions close to the equilibrium.

Let's see an example.

### Example: Finding the Linear Approximations Near Equilibria

#### Question

$$


\begin{aligned}𝑥^{′}(𝑡)=𝑥^{2}(𝑡)+3𝑦(𝑡)−4𝑥(𝑡)+4 \\ 𝑦^{′}(𝑡)=𝑥^{2}(𝑡)−2𝑥(𝑡)+𝑦^{2}(𝑡)\end{aligned}


$$

Consider the system of differential equations above. What is the corresponding linearized system at the equilibrium point $\mathbf{x}^\ast=[2, \ 0]^T?$

#### Explanation

The system can be rewritten in matrix form as

$$


\mathbf{x}' = \boldsymbol{f}(\mathbf{x})


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ and $[\begin{aligned}𝑥^{2}+3𝑦−4𝑥+4 \\ 𝑥^{2}−2𝑥+𝑦^{2}\end{aligned}]$

We need to compute the Jacobian matrix (or the total derivative) of $\boldsymbol{f}(\mathbf{x}).$

In our case, we have the following:

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥} & \frac{𝜕𝑓_{1}}{𝜕𝑦} \\ \frac{𝜕𝑓_{2}}{𝜕𝑥} & \frac{𝜕𝑓_{2}}{𝜕𝑦}\end{aligned}


$$

First, we compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑓_{1}}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}+3𝑦−4𝑥+4)=2𝑥−4,\, & \frac{𝜕𝑓_{1}}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑥^{2}+3𝑦−4𝑥+4)=3 \\ \frac{𝜕𝑓_{2}}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}−2𝑥+𝑦^{2})=2𝑥−2,\, & \frac{𝜕𝑓_{2}}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑥^{2}−2𝑥+𝑦^{2})=2𝑦\end{aligned}


$$

Thus, we have

$$


[\begin{aligned}2𝑥−4 & 3 \\ 2𝑥−2 & 2𝑦\end{aligned}]


$$

Next, we evaluate the Jacobian at the equilibrium $[\begin{aligned}2 \\ 0\end{aligned}]$ to get

$$


[\begin{aligned}2(2)−4 & 3 \\ 2(2)−2 & 2(0)\end{aligned}]


$$

Finally, near the equilibrium, the nonlinear system is approximated by

$$


\begin{aligned}0 & 3 \\ 2 & 0\end{aligned}


$$

where the deviation vector is

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

### Stability and Classification of Isolated Critical Points

Again, suppose $\mathbf{x}^\ast$ is an equilibrium of the nonlinear system

$$


\mathbf{x}'=\boldsymbol{f}(\mathbf{x}),


$$

and assume the system is *almost linear* at $\mathbf{x}^\ast$. If

$$


J=\boldsymbol{f}'(\mathbf{x}^\ast)


$$

denotes the Jacobian matrix evaluated at the equilibrium, then the behavior of solutions near $\mathbf{x}^\ast$ is determined by the eigenvalues of $J.$

This information can be summarized in the following table.

Let's now consider a concrete example.

### Example: Classifying an Isolated Critical Point of a Nonlinear System

#### Question

Consider the system of differential equations above. What is the behavior of the system’s solutions near the equilibrium

#### Explanation

The system can be rewritten in matrix form as where and

We need to compute the Jacobian matrix (or the total derivative) of

In our case, we have the following:

First, we compute the partial derivatives:

Thus, we have:

Now, we evaluate the Jacobian at the equilibrium to get

Notice that the matrix is invertible (its determinant is not zero), so the system is almost linear at

To find the eigenvalues of the Jacobian matrix, we write down the characteristic equation:

Solving the equation, we get the eigenvalues

Finally, since we have two real eigenvalues with opposite signs, our equilibrium is an

### A Note About Stable Centers

In the classification above, we intentionally skipped one case:

The eigenvalues $\lambda_1$ and $\lambda_2$ of the Jacobian at the equilibrium are purely imaginary.

In this situation, the corresponding linearized system has a *center* at the origin, meaning that solutions neither grow nor decay, but instead circulate around the equilibrium.

For the original nonlinear system, however, this case is *inconclusive*. While the linearized system predicts closed orbits, the nonlinear system *may* exhibit a stable center, an unstable spiral, or other nearby behavior.

Therefore, when the Jacobian has purely imaginary eigenvalues, linearization alone is not sufficient to classify the equilibrium. In such cases, further analysis beyond linear approximation is required.
