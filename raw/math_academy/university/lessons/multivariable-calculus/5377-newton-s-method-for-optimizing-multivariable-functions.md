# Newton's Method for Optimizing Multivariable Functions

Source: https://www.mathacademy.com/topics/5377?courseId=54
Topic ID: 5377

## Prerequisites

- [The Second Derivative of a Multivariable Function](./2824-the-second-derivative-of-a-multivariable-function.md)
- [Newton's Method for Optimizing Single-Variable Functions](../calculus-i/2926-newton-s-method-for-optimizing-single-variable-functions.md)
- [Newton's Method for Multivariable Functions](./5379-newton-s-method-for-multivariable-functions.md)

## Lesson

### Introduction

In a previous lesson, we saw how Newton’s method can be used to find local minima or maxima of a smooth function $f: \mathbb{R} \to \mathbb{R}$ by approximating the function near the current guess with a parabola.

Recall that in one variable, Newton’s update rule is

$$


x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)},


$$

where $f'(x)$ is the first derivative, and $f''(x)$ is the second derivative.

To generalize this idea to higher dimensions, we need analogues of the first and second derivatives.

Recall that the gradient vector $\nabla f(\mathbf{x})$ generalizes the first derivative to multivariable functions, and the Hessian matrix $H_f(\mathbf{x})$ generalizes the second derivative.

Like before, we aim to find critical points, which are the points where the gradient vanishes:

$$


\nabla f(\mathbf{x}) = \mathbf{0}


$$

So once again, optimization becomes a root-finding problem, but now for the gradient vector $\nabla f(\mathbf{x}).$

Just like in one dimension, we approximate $f(\mathbf{x})$ near our current guess $\mathbf{x}_n$ using a second-order Taylor expansion

$$


f(\mathbf{x}) \approx f(\mathbf{x}_n) + \nabla f(\mathbf{x}_n)^T (\mathbf{x} - \mathbf{x}_n) + \frac{1}{2} (\mathbf{x} - \mathbf{x}_n)^T H_f(\mathbf{x}_n) (\mathbf{x} - \mathbf{x}_n).


$$

This is the multivariable analogue of a parabola, a *quadratic surface*.

To find the minimum of this quadratic surface, we compute its gradient with respect to $\mathbf{x}$ and set it equal to zero. The gradient of the approximation is

$$


\nabla f(\mathbf{x}) \approx \nabla f(\mathbf{x}_n) + H_f(\mathbf{x}_n)(\mathbf{x} - \mathbf{x}_n).


$$

We then set the gradient equal to the zero vector:

$$


\nabla f(\mathbf{x}_n) + H_f(\mathbf{x}_n)(\mathbf{x} - \mathbf{x}_n) = \mathbf{0}


$$

Finally, we isolate $\mathbf{x},$ as follows:

$$


\begin{aligned}𝐻_{𝑓}(𝐱_{𝑛})(𝐱−𝐱_{𝑛}) & =−∇𝑓(𝐱_{𝑛}) \\ 𝐱−𝐱_{𝑛} & =−[𝐻_{𝑓}(𝐱_{𝑛})]^{−1}∇𝑓(𝐱_{𝑛}) \\ 𝐱 & =𝐱_{𝑛}−[𝐻_{𝑓}(𝐱_{𝑛})]^{−1}∇𝑓(𝐱_{𝑛})\end{aligned}


$$

This new value becomes our next guess, which we call $\mathbf{x}_{n+1}.$ So, we write

$$


\boxed{\mathbf{x}_{n+1} = \mathbf{x}_n - [H_f(\mathbf{x}_n)]^{-1} \nabla f(\mathbf{x}_n).}


$$

Newton’s method can be extremely fast, but only under the following conditions:

- The function $f$ is twice continuously differentiable (i.e., smooth).

- The starting point $\mathbf{x}_0$ is close to a critical point.

- The Hessian $H_f(\mathbf{x})$ is invertible and preferably positive definite near the solution.

When these conditions are met, Newton’s method often converges in just a few iterations.

### A Worked Example

Suppose we wish to find a critical point of the function $f(x,y)$ in the region $[0,2]\times[0,2] \subseteq \mathbb{R}^2,$ where

$$


f(x,y) =x^2y-2xy^2+x^3-4x.


$$

Let’s calculate one iteration of the Newton-Raphson method, starting at the point $\mathbf x_0 = \big[1, \: 1 \big]^T.$

The Newton-Raphson method of optimizing a multivariable function $f: \mathbb{R}^n \to \mathbb{R}$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [H_f(\mathbf{x}_n)]^{-1} \nabla{f}(\mathbf{x}_n),


$$

where $H_f(\mathbf{x}_n)$ and $\nabla{f}(\mathbf{x}_n)$ are the Hessian and gradient of $f$, respectively, evaluated at $\mathbf{x}_n.$

In our case, the gradient is

$$


\begin{aligned}∇𝑓(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(𝑥^{2}𝑦−2𝑥𝑦^{2}+𝑥^{3}−4𝑥) \\ \frac{𝜕}{𝜕𝑦}(𝑥^{2}𝑦−2𝑥𝑦^{2}+𝑥^{3}−4𝑥)\end{matrix} \\ & =[\begin{matrix}2𝑥𝑦−2𝑦^{2}+3𝑥^{2}−4 \\ 𝑥^{2}−4𝑥𝑦\end{matrix}],\end{aligned}


$$

and the Hessian is

$$


\begin{aligned}𝐻_{𝑓}(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(2𝑥𝑦−2𝑦^{2}+3𝑥^{2}−4) & \frac{𝜕}{𝜕𝑥}(𝑥^{2}−4𝑥𝑦) \\ \frac{𝜕}{𝜕𝑦}(2𝑥𝑦−2𝑦^{2}+3𝑥^{2}−4) & \frac{𝜕}{𝜕𝑦}(𝑥^{2}−4𝑥𝑦)\end{matrix} \\ & =[\begin{matrix}2𝑦+6𝑥 & 2𝑥−4𝑦 \\ 2𝑥−4𝑦 & −4𝑥\end{matrix}].\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


[\begin{aligned}2𝑦+6𝑥 & 2𝑥−4𝑦 \\ 2𝑥−4𝑦 & −4𝑥\end{aligned}]


$$

Starting with $[\begin{aligned}1 \\ 1\end{aligned}]$ we have

$$


\begin{aligned}𝐱_{1} & =𝐱_{0}−[\begin{matrix}2𝑦+6𝑥 & 2𝑥−4𝑦 \\ 2𝑥−4𝑦 & −4𝑥\end{matrix}]_{−1𝐱_{0}}^{}[\begin{matrix}2𝑥𝑦−2𝑦^{2}+3𝑥^{2}−4 \\ 𝑥^{2}−4𝑥𝑦\end{matrix}]_{𝐱_{0}} \\ & =[\begin{matrix}1 \\ 1\end{matrix}]−[\begin{matrix}2(1)+6(1) & 2(1)−4(1) \\ 2(1)−4(1) & −4(1)\end{matrix}]^{−1}[\begin{matrix}2(1)(1)−2(1)^{2}+3(1)^{2}−4 \\ (1)^{2}−4(1)(1)\end{matrix}] \\ & =[\begin{matrix}1 \\ 1\end{matrix}]−[\begin{matrix}8 & −2 \\ −2 & −4\end{matrix}]^{−1}[\begin{matrix}−1 \\ −3\end{matrix}] \\ & =[\begin{matrix}1 \\ 1\end{matrix}]−\frac{1}{(8)⋅(−4)−(−2)⋅(−2)}[\begin{matrix}−4 & 2 \\ 2 & 8\end{matrix}][\begin{matrix}−1 \\ −3\end{matrix}] \\ & =[\begin{matrix}1 \\ 1\end{matrix}]−\frac{1}{−36}[\begin{matrix}−2 \\ −26\end{matrix}] \\ & =[\begin{matrix}1 \\ 1\end{matrix}]+\begin{matrix}−\frac{1}{18} \\ −\frac{13}{18}\end{matrix} \\ & =\begin{matrix}\frac{17}{18} \\ \frac{5}{18}\end{matrix}.\end{aligned}


$$

### Example: Computing One Iteration of the Newton-Raphson Method

#### Question

Suppose we wish to find a critical point of the function $f(x,y)$ in the region $[0,1] \times [0,1] \subseteq \mathbb{R}^2,$ where

$$


f(x,y) = 2x^2y-2x^2+3xy^2+3xy+1.


$$

Calculate one iteration of the Newton-Raphson process for optimization that starts at $\mathbf x_0 = \big[1, \: 1 \big]^T.$ Round your final answer to ****

#### Explanation

The Newton-Raphson method of optimizing a multivariable function $f: \mathbb{R}^n \to \mathbb{R}$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [H_f(\mathbf{x}_n)]^{-1} \nabla{f}(\mathbf{x}_n),


$$

where $H(\mathbf{x}_n)$ and $\nabla{f}(\mathbf{x}_n)$ are the Hessian and gradient of $f$, respectively, evaluated at $\mathbf{x}_n.$

In our case, the gradient is

$$


\begin{aligned}∇𝑓(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(2𝑥^{2}𝑦−2𝑥^{2}+3𝑥𝑦^{2}+3𝑥𝑦+1) \\ \frac{𝜕}{𝜕𝑦}(2𝑥^{2}𝑦−2𝑥^{2}+3𝑥𝑦^{2}+3𝑥𝑦+1)\end{matrix} \\ & =[\begin{matrix}4𝑥𝑦−4𝑥+3𝑦^{2}+3𝑦 \\ 2𝑥^{2}+6𝑥𝑦+3𝑥\end{matrix}],\end{aligned}


$$

and the Hessian is

$$


\begin{aligned}𝐻_{𝑓}(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(4𝑥𝑦−4𝑥+3𝑦^{2}+3𝑦) & \frac{𝜕}{𝜕𝑥}(2𝑥^{2}+6𝑥𝑦+3𝑥) \\ \frac{𝜕}{𝜕𝑦}(4𝑥𝑦−4𝑥+3𝑦^{2}+3𝑦) & \frac{𝜕}{𝜕𝑦}(2𝑥^{2}+6𝑥𝑦+3𝑥)\end{matrix} \\ & =[\begin{matrix}4𝑦−4 & 4𝑥+6𝑦+3 \\ 4𝑥+6𝑦+3 & 6𝑥\end{matrix}].\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


[\begin{aligned}4𝑦−4 & 4𝑥+6𝑦+3 \\ 4𝑥+6𝑦+3 & 6𝑥\end{aligned}]


$$

Starting with $[\begin{aligned}1 \\ 1\end{aligned}]$ we have

$$


\begin{aligned}𝐱_{1} & =𝐱_{0}−[\begin{matrix}4𝑦−4 & 4𝑥+6𝑦+3 \\ 4𝑥+6𝑦+3 & 6𝑥\end{matrix}]_{−1𝐱_{0}}^{}[\begin{matrix}4𝑥𝑦−4𝑥+3𝑦^{2}+3𝑦 \\ 2𝑥^{2}+6𝑥𝑦+3𝑥\end{matrix}]_{𝐱_{0}} \\ & =[\begin{matrix}1 \\ 1\end{matrix}]−[\begin{matrix}4(1)−4 & 4(1)+6(1)+3 \\ 4(1)+6(1)+3 & 6(1)\end{matrix}]^{−1}[\begin{matrix}4(1)(1)−4(1)+3(1)^{2}+3(1) \\ 2(1)^{2}+6(1)(1)+3(1)\end{matrix}] \\ & =[\begin{matrix}1 \\ 1\end{matrix}]−[\begin{matrix}0 & 13 \\ 13 & 6\end{matrix}]^{−1}[\begin{matrix}6 \\ 11\end{matrix}] \\ & =[\begin{matrix}1 \\ 1\end{matrix}]−\frac{1}{0⋅6−13⋅13}[\begin{matrix}6 & −13 \\ −13 & 0\end{matrix}][\begin{matrix}6 \\ 11\end{matrix}] \\ & =[\begin{matrix}1 \\ 1\end{matrix}]+\frac{1}{169}[\begin{matrix}−107 \\ −78\end{matrix}] \\ & ≈[\begin{matrix}0.367 \\ 0.538\end{matrix}].\end{aligned}


$$

### Example: Computing Two Iterations of the Newton-Raphson Method

#### Question

Suppose we wish to find a critical point of the function $f(x,y)$ in the region $[1,2] \times [1,2] \subseteq \mathbb{R}^2,$ where

$$


f(x,y) = x^3+y^3-3x-6y+9.


$$

Calculate the second iteration of the Newton-Raphson process for optimization that starts at $\mathbf x_0 = \big[1, \: 2 \big]^T$ if the first iteration of the algorithm gives $\mathbf x_1 = \big[1, \: 1.5 \big]^T.$ Round your final answer to ****

#### Explanation

The Newton-Raphson method of optimizing a multivariable function $f: \mathbb{R}^n \to \mathbb{R}$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [H_f(\mathbf{x}_n)]^{-1} \nabla{f}(\mathbf{x}_n),


$$

where $H(\mathbf{x}_n)$ and $\nabla{f}(\mathbf{x}_n)$ are the Hessian and gradient of $f$, respectively, evaluated at $\mathbf{x}_n.$

In our case, the gradient is

$$


\begin{aligned}∇𝑓(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(𝑥^{3}+𝑦^{3}−3𝑥−6𝑦+9) \\ \frac{𝜕}{𝜕𝑦}(𝑥^{3}+𝑦^{3}−3𝑥−6𝑦+9)\end{matrix} \\ & =[\begin{matrix}3𝑥^{2}−3 \\ 3𝑦^{2}−6\end{matrix}],\end{aligned}


$$

and the Hessian is

$$


\begin{aligned}𝐻_{𝑓}(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(3𝑥^{2}−3) & \frac{𝜕}{𝜕𝑥}(3𝑦^{2}−6) \\ \frac{𝜕}{𝜕𝑦}(3𝑥^{2}−3) & \frac{𝜕}{𝜕𝑦}(3𝑦^{2}−6)\end{matrix} \\ & =[\begin{matrix}6𝑥 & 0 \\ 0 & 6𝑦\end{matrix}].\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


[\begin{aligned}6𝑥 & 0 \\ 0 & 6𝑦\end{aligned}]


$$

For the second iteration, we have

$$


\begin{aligned}𝐱_{2} & =𝐱_{1}−[\begin{matrix}6𝑥 & 0 \\ 0 & 6𝑦\end{matrix}]_{−1𝐱_{1}}^{}[\begin{matrix}3𝑥^{2}−3 \\ 3𝑦^{2}−6\end{matrix}]_{𝐱_{1}} \\ & =[\begin{matrix}1 \\ 1.5\end{matrix}]−[\begin{matrix}6(1) & 0 \\ 0 & 6(1.5)\end{matrix}]^{−1}[\begin{matrix}3(1)^{2}−3 \\ 3(1.5)^{2}−6\end{matrix}] \\ & =[\begin{matrix}1 \\ 1.5\end{matrix}]−[\begin{matrix}6 & 0 \\ 0 & 9\end{matrix}]^{−1}[\begin{matrix}0 \\ 0.75\end{matrix}] \\ & =[\begin{matrix}1 \\ 1.5\end{matrix}]−\frac{1}{6⋅9−0⋅0}[\begin{matrix}9 & 0 \\ 0 & 6\end{matrix}][\begin{matrix}0 \\ 0.75\end{matrix}] \\ & =[\begin{matrix}1 \\ 1.5\end{matrix}]−\frac{1}{54}[\begin{matrix}0 \\ 4.5\end{matrix}] \\ & ≈\begin{matrix}1 \\ 1.417\end{matrix}.\end{aligned}


$$

### Alternative to Newton's Method for Multivariable Functions Using Linear Systems

Recall that the standard Newton’s method update for multivariable optimization is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [H_f(\mathbf{x}_n)]^{-1} \nabla f(\mathbf{x}_n).


$$

In higher dimensions, it’s often more useful to avoid calculating the inverse of a large Hessian matrix by rewriting the update as a linear system instead.

Let’s see how.

We start with the original update formula:

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [H_f(\mathbf{x}_n)]^{-1} \nabla f(\mathbf{x}_n)


$$

Next, we subtract $\mathbf{x}_n$ from both sides:

$$


\mathbf{x}_{n+1} - \mathbf{x}_n = -[H_f(\mathbf{x}_n)]^{-1} \nabla f(\mathbf{x}_n)


$$

Then, we multiply both sides by $H_f(\mathbf{x}_n){:}$

$$


H_f(\mathbf{x}_n)(\mathbf{x}_{n+1} - \mathbf{x}_n) = -\nabla f(\mathbf{x}_n)


$$

This is a linear system of equations. It’s mathematically equivalent to the original update rule, but much better for actual computation, since we no longer need to invert the Hessian; we just need to solve for $(\mathbf{x}_{n+1} - \mathbf{x}_n)$.

### A Worked Example

Recall the example we worked on, where we computed one iteration of the Newton–Raphson method.

We aim to find a critical point of the function

$$


f(x,y) =x^2y-2xy^2+x^3-4x,


$$

in the region $[0,2]\times[0,2] \subseteq \mathbb{R}^2,$ starting at the point $\big[1, \: 1 \big]^T$.

Now, let’s carry out one iteration of Newton–Raphson using linear systems.

The Newton-Raphson method of optimizing a multivariable function $f: \mathbb{R}^n \to \mathbb{R}$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [H_f(\mathbf{x}_n)]^{-1} \nabla{f}(\mathbf{x}_n),


$$

where $H_f(\mathbf{x}_n)$ and $\nabla{f}(\mathbf{x}_n)$ are the Hessian and gradient of $f$, respectively, evaluated at $\mathbf{x}_n.$

Equivalently, at each iteration, the above equation can be rewritten as

$$


H_f(\mathbf{x}_n)(\mathbf{x}_{n+1} - \mathbf{x}_n) = -\nabla{f}(\mathbf{x}_n).


$$

In our case, the gradient is

$$


\begin{aligned}∇𝑓(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(𝑥^{2}𝑦−2𝑥𝑦^{2}+𝑥^{3}−4𝑥) \\ \frac{𝜕}{𝜕𝑦}(𝑥^{2}𝑦−2𝑥𝑦^{2}+𝑥^{3}−4𝑥)\end{matrix} \\ & =[\begin{matrix}2𝑥𝑦−2𝑦^{2}+3𝑥^{2}−4 \\ 𝑥^{2}−4𝑥𝑦\end{matrix}],\end{aligned}


$$

and the Hessian is

$$


\begin{aligned}𝐻_{𝑓}(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(2𝑥𝑦−2𝑦^{2}+3𝑥^{2}−4) & \frac{𝜕}{𝜕𝑥}(𝑥^{2}−4𝑥𝑦) \\ \frac{𝜕}{𝜕𝑦}(2𝑥𝑦−2𝑦^{2}+3𝑥^{2}−4) & \frac{𝜕}{𝜕𝑦}(𝑥^{2}−4𝑥𝑦)\end{matrix} \\ & =[\begin{matrix}2𝑦+6𝑥 & 2𝑥−4𝑦 \\ 2𝑥−4𝑦 & −4𝑥\end{matrix}].\end{aligned}


$$

Therefore, our Newton-Raphson system of equations is

$$


[\begin{aligned}2𝑦+6𝑥 & 2𝑥−4𝑦 \\ 2𝑥−4𝑦 & −4𝑥\end{aligned}]


$$

Starting with $[\begin{aligned}1 \\ 1\end{aligned}]$ we have

$$


\begin{aligned}[\begin{matrix}2𝑦+6𝑥 & 2𝑥−4𝑦 \\ 2𝑥−4𝑦 & −4𝑥\end{matrix}]_{𝐱_{0}}(𝐱_{1}−𝐱_{0}) & =−[\begin{matrix}2𝑥𝑦−2𝑦^{2}+3𝑥^{2}−4 \\ 𝑥^{2}−4𝑥𝑦\end{matrix}]_{𝐱_{0}} \\ [\begin{matrix}2(1)+6(1) & 2(1)−4(1) \\ 2(1)−4(1) & −4(1)\end{matrix}](𝐱_{1}−𝐱_{0}) & =−[\begin{matrix}2(1)(1)−2(1)^{2}+3(1)^{2}−4 \\ (1)^{2}−4(1)(1)\end{matrix}] \\ [\begin{matrix}8 & −2 \\ −2 & −4\end{matrix}](𝐱_{1}−𝐱_{0}) & =[\begin{matrix}1 \\ 3\end{matrix}].\end{aligned}


$$

Solving this system of equations, we get $[\begin{aligned}−1/18 \\ −13/18\end{aligned}]$ Hence,

$$


\begin{aligned}𝐱_{1} & =𝐱_{0}+\begin{matrix}−\frac{1}{18} \\ −\frac{13}{18}\end{matrix} \\ & =[\begin{matrix}1 \\ 1\end{matrix}]+\begin{matrix}−\frac{1}{18} \\ −\frac{13}{18}\end{matrix} \\ & =\begin{matrix}\frac{17}{18} \\ \frac{5}{18}\end{matrix}.\end{aligned}


$$

This is the same result we obtained previously.

### Example: Computing Iterations of the Newton-Raphson Method Using Linear Systems

#### Question

Suppose we wish to find a critical point of the function $f(x,y)$ in the region $[0,1]\times[0,1] \subseteq \mathbb{R}^2,$ where

$$


f(x,y) = xy^2+3x^2-xy-x.


$$

Find the matrix equation that defines the first iteration of the Newton-Raphson process starting at the point $\big[1, \: 1 \big]^T,$ and compute the components of the first iteration

#### Explanation

The Newton-Raphson method of optimizing a multivariable function $f: \mathbb{R}^n \to \mathbb{R}$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [H_f(\mathbf{x}_n)]^{-1} \nabla{f}(\mathbf{x}_n),


$$

where $H(\mathbf{x}_n)$ and $\nabla{f}(\mathbf{x}_n)$ are the Hessian and gradient of $f$, respectively, evaluated at $\mathbf{x}_n.$

Equivalently, at each iteration, the above equation can be rewritten as

$$


H_f(\mathbf{x}_n)(\mathbf{x}_{n+1} - \mathbf{x}_n) = -\nabla{f}(\mathbf{x}_n).


$$

In our case, the gradient is

$$


\begin{aligned}∇𝑓(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(𝑥𝑦^{2}+3𝑥^{2}−𝑥𝑦−𝑥) \\ \frac{𝜕}{𝜕𝑦}(𝑥𝑦^{2}+3𝑥^{2}−𝑥𝑦−𝑥)\end{matrix} \\ & =[\begin{matrix}𝑦^{2}+6𝑥−𝑦−1 \\ 2𝑥𝑦−𝑥\end{matrix}],\end{aligned}


$$

and the Hessian is

$$


\begin{aligned}𝐻_{𝑓}(𝐱) & =\begin{matrix}\frac{𝜕}{𝜕𝑥}(𝑦^{2}+6𝑥−𝑦−1) & \frac{𝜕}{𝜕𝑥}(2𝑥𝑦−𝑥) \\ \frac{𝜕}{𝜕𝑦}(𝑦^{2}+6𝑥−𝑦−1) & \frac{𝜕}{𝜕𝑦}(2𝑥𝑦−𝑥)\end{matrix} \\ & =[\begin{matrix}6 & 2𝑦−1 \\ 2𝑦−1 & 2𝑥\end{matrix}].\end{aligned}


$$

Therefore, our Newton-Raphson system of equations is

$$


[\begin{aligned}6 & 2𝑦−1 \\ 2𝑦−1 & 2𝑥\end{aligned}]


$$

Starting with $[\begin{aligned}1 \\ 1\end{aligned}]$ we have

$$


\begin{aligned}[\begin{matrix}6 & 2𝑦−1 \\ 2𝑦−1 & 2𝑥\end{matrix}]_{𝐱_{0}}(𝐱_{1}−𝐱_{0}) & =−[\begin{matrix}𝑦^{2}+6𝑥−𝑦−1 \\ 2𝑥𝑦−𝑥\end{matrix}]_{𝐱_{0}} \\ [\begin{matrix}6 & 2(1)−1 \\ 2(1)−1 & 2(1)\end{matrix}](𝐱_{1}−𝐱_{0}) & =−[\begin{matrix}(1)^{2}+6(1)−(1)−1 \\ 2(1)(1)−1\end{matrix}] \\ [\begin{matrix}6 & 1 \\ 1 & 2\end{matrix}](𝐱_{1}−𝐱_{0}) & =[\begin{matrix}−5 \\ −1\end{matrix}].\end{aligned}


$$

Solving this system of equations, we get $[\begin{aligned}−9/11 \\ −1/11\end{aligned}]$ Hence,

$$


\begin{aligned}𝐱_{1} & =𝐱_{0}+[\begin{matrix}−9/11 \\ −1/11\end{matrix}] \\ & =[\begin{matrix}1 \\ 1\end{matrix}]+[\begin{matrix}−9/11 \\ −1/11\end{matrix}] \\ & ≈[\begin{matrix}0.182 \\ 0.909\end{matrix}].\end{aligned}


$$
