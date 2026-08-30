# Newton's Method for Multivariable Functions

Source: https://www.mathacademy.com/topics/5379?courseId=54
Topic ID: 5379

## Prerequisites

- [Solving 2x2 Systems of Equations Using Gaussian Elimination](../linear-algebra/151-solving-2x2-systems-of-equations-using-gaussian-elimination.md)
- [Newton's Method](../calculus-i/912-newton-s-method.md)
- [The Jacobian](./1999-the-jacobian.md)

## Lesson

### Introduction

In a previous lesson, we learned how Newton’s method works for functions of a single variable. Given a function $f: \mathbb{R} \to \mathbb{R}$, the method generates a sequence of approximations using the rule

$$


x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.


$$

This formula uses the derivative $f'(x_n)$ to construct a local linear approximation of $f$ near $x_n$, which we then use to refine our guess.

In this lesson, we turn to the multivariable case, where we want to solve systems of nonlinear equations. Specifically, we are interested in finding a vector $\mathbf{x} \in \mathbb{R}^n$ that solves

$$


\boldsymbol{f}(\mathbf{x}) = \mathbf{0},


$$

for a vector-valued function $\boldsymbol{f}: \mathbb{R}^n \to \mathbb{R}^n$.

The multivariable version of Newton’s method updates our guess using the formula

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [J_\boldsymbol{f}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n),


$$

where $J_{\boldsymbol{f}}(\mathbf{x}_n)$ is the Jacobian matrix of $\boldsymbol{f}$, evaluated at $\mathbf{x}_n$.

This is a natural extension of the single-variable rule, replacing the derivative with the Jacobian and the scalar update with a vector.

To see how this method works in practice, let’s walk through a concrete example.

### A Worked Example

Suppose we are looking for a zero of the function

$$


[\begin{aligned}𝑥^{4}−𝑦^{2}+5 \\ 𝑥^{2}−𝑦^{3}+1\end{aligned}]


$$

in the region $[-2, 2] \times [-2, 2] \subseteq \mathbb{R}^2$.

We will perform one iteration of the Newton–Raphson method, starting from the initial guess

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

The Newton-Raphson method of finding the zeros of a multivariable function $\boldsymbol{f}: \mathbb{R}^n \to \mathbb{R}^n$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [J_\boldsymbol{f}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n),


$$

where $J_\boldsymbol{f}(\mathbf{x}_n)$ is the Jacobian of $\boldsymbol f$ evaluated at $\mathbf{x}_n.$

In our case, the Jacobian is

$$


\begin{aligned}𝐽_{𝒇}(𝐱) & =\begin{aligned}\frac{𝜕}{𝜕𝑥}(𝑥^{4}−𝑦^{2}+5) & \frac{𝜕}{𝜕𝑦}(𝑥^{4}−𝑦^{2}+5) \\ \frac{𝜕}{𝜕𝑥}(𝑥^{2}−𝑦^{3}+1) & \frac{𝜕}{𝜕𝑦}(𝑥^{2}−𝑦^{3}+1)\end{aligned} \\ & =[\begin{aligned}4𝑥^{3} & −2𝑦 \\ 2𝑥 & −3𝑦^{2}\end{aligned}].\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


[\begin{aligned}4𝑥^{3} & −2𝑦 \\ 2𝑥 & −3𝑦^{2}\end{aligned}]


$$

Starting with $[\begin{aligned}1 \\ 1\end{aligned}]$ we have

$$


\begin{aligned}𝐱_{1} & =𝐱_{0}−[\begin{aligned}4𝑥^{3} & −2𝑦 \\ 2𝑥 & −3𝑦^{2}\end{aligned}]_{−1𝐱_{0}}^{}[\begin{aligned}𝑥^{4}−𝑦^{2}+5 \\ 𝑥^{2}−𝑦^{3}+1\end{aligned}]_{𝐱_{0}} \\ & =[\begin{aligned}1 \\ 1\end{aligned}]−[\begin{aligned}4(1)^{3} & −2(1) \\ 2(1) & −3(1)^{2}\end{aligned}]^{−1}[\begin{aligned}(1)^{4}−(1)^{2}+5 \\ (1)^{2}−(1)^{3}+1\end{aligned}] \\ & =[\begin{aligned}1 \\ 1\end{aligned}]−[\begin{aligned}4 & −2 \\ 2 & −3\end{aligned}]^{−1}[\begin{aligned}5 \\ 1\end{aligned}] \\ & =[\begin{aligned}1 \\ 1\end{aligned}]−\frac{1}{4⋅(−3)−(−2)⋅2}[\begin{aligned}−3 & 2 \\ −2 & 4\end{aligned}][\begin{aligned}5 \\ 1\end{aligned}] \\ & =[\begin{aligned}1 \\ 1\end{aligned}]+\frac{1}{8}[\begin{aligned}−13 \\ −6\end{aligned}] \\ & =[\begin{aligned}−0.625 \\ 0.25\end{aligned}].\end{aligned}


$$

### Example: Computing One Iteration of the Newton-Raphson Method

#### Question

Suppose we wish to find a zero of the function $\boldsymbol{f}(x,y)$ in the region $[-2,2] \times [0,2] \subseteq \mathbb{R}^2,$ where

$$


[\begin{aligned}𝑥^{2}𝑦−𝑥−2 \\ 𝑥𝑦^{2}−𝑦+1\end{aligned}]


$$

Calculate one iteration of the Newton-Raphson process that starts with $\mathbf x_0 = \big[1, \: 2 \big]^T.$

#### Explanation

The Newton-Raphson method of finding the zeros of a multivariable function $\boldsymbol{f}: \mathbb{R}^n \to \mathbb{R}^n$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [J_\boldsymbol{f}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n),


$$

where $J_\boldsymbol{f}(\mathbf{x}_n)$ is the Jacobian of $\boldsymbol f$ evaluated at $\mathbf{x}_n.$

In our case, the Jacobian is

$$


\begin{aligned}𝐽_{𝒇}(𝐱) & =\begin{aligned}\frac{𝜕}{𝜕𝑥}(𝑥^{2}𝑦−𝑥−2) & \frac{𝜕}{𝜕𝑦}(𝑥^{2}𝑦−𝑥−2) \\ \frac{𝜕}{𝜕𝑥}(𝑥𝑦^{2}−𝑦+1) & \frac{𝜕}{𝜕𝑦}(𝑥𝑦^{2}−𝑦+1)\end{aligned} \\ & =[\begin{aligned}2𝑥𝑦−1 & 𝑥^{2} \\ 𝑦^{2} & 2𝑥𝑦−1\end{aligned}].\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


[\begin{aligned}2𝑥𝑦−1 & 𝑥^{2} \\ 𝑦^{2} & 2𝑥𝑦−1\end{aligned}]


$$

Starting with $[\begin{aligned}1 \\ 2\end{aligned}]$ we have

$$


\begin{aligned}𝐱_{1} & =𝐱_{0}−[\begin{aligned}2𝑥𝑦−1 & 𝑥^{2} \\ 𝑦^{2} & 2𝑥𝑦−1\end{aligned}]_{−1𝐱_{0}}^{}[\begin{aligned}𝑥^{2}𝑦−𝑥−2 \\ 𝑥𝑦^{2}−𝑦+1\end{aligned}]_{𝐱_{0}} \\ & =[\begin{aligned}1 \\ 2\end{aligned}]−[\begin{aligned}2(1)(2)−1 & (1)^{2} \\ (2)^{2} & 2(1)(2)−1\end{aligned}]^{−1}[\begin{aligned}(1)^{2}(2)−1−2 \\ 1(2)^{2}−2+1\end{aligned}] \\ & =[\begin{aligned}1 \\ 2\end{aligned}]−[\begin{aligned}3 & 1 \\ 4 & 3\end{aligned}]^{−1}[\begin{aligned}−1 \\ 3\end{aligned}] \\ & =[\begin{aligned}1 \\ 2\end{aligned}]−\frac{1}{3⋅3−4⋅1}[\begin{aligned}3 & −1 \\ −4 & 3\end{aligned}][\begin{aligned}−1 \\ 3\end{aligned}] \\ & =[\begin{aligned}1 \\ 2\end{aligned}]−\frac{1}{5}[\begin{aligned}−6 \\ 13\end{aligned}] \\ & =\begin{aligned}\frac{11}{5} \\ −\frac{3}{5}\end{aligned} \\ & =[\begin{aligned}2.2 \\ −0.6\end{aligned}].\end{aligned}


$$

### Example: Computing Two Iterations of the Newton-Raphson Method

#### Question

Suppose we wish to find a zero of the function $\boldsymbol{f}(x,y)$ in the region $[1,3] \times [-2,0] \subseteq \mathbb{R}^2,$ where

$$


[\begin{aligned}𝑥^{2}+𝑦−4 \\ 𝑥+𝑦^{2}−3\end{aligned}]


$$

Calculate the second iteration of the Newton-Raphson process that starts at $\mathbf x_0 = \big[1, \: 0 \big]^T$ if the first iteration of the algorithm gives $\mathbf{x}_1 = \big[3, \: -1 \big]^T.$ Round your final answer to three decimal places (if needed).

#### Explanation

The Newton-Raphson method of finding the zeros of a multivariable function $\boldsymbol{f}: \mathbb{R}^n \to \mathbb{R}^n$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [J_\boldsymbol{f}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n),


$$

where $J_\boldsymbol{f}(\mathbf{x}_n)$ is the Jacobian of $\boldsymbol f$ evaluated at $\mathbf{x}_n.$

In our case, the Jacobian is

$$


\begin{aligned}𝐽_{𝒇}(𝐱) & =\begin{aligned}\frac{𝜕}{𝜕𝑥}(𝑥^{2}+𝑦−4) & \frac{𝜕}{𝜕𝑦}(𝑥^{2}+𝑦−4) \\ \frac{𝜕}{𝜕𝑥}(𝑥+𝑦^{2}−3) & \frac{𝜕}{𝜕𝑦}(𝑥+𝑦^{2}−3)\end{aligned} \\ & =[\begin{aligned}2𝑥 & 1 \\ 1 & 2𝑦\end{aligned}].\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


[\begin{aligned}2𝑥 & 1 \\ 1 & 2𝑦\end{aligned}]


$$

For the second iteration, we have

$$


\begin{aligned}𝐱_{2} & =𝐱_{1}−[\begin{aligned}2𝑥 & 1 \\ 1 & 2𝑦\end{aligned}]_{−1𝐱_{1}}^{}[\begin{aligned}𝑥^{2}+𝑦−4 \\ 𝑥+𝑦^{2}−3\end{aligned}]_{𝐱_{1}} \\ & =[\begin{aligned}3 \\ −1\end{aligned}]−[\begin{aligned}2(3) & 1 \\ 1 & 2(−1)\end{aligned}]^{−1}[\begin{aligned}3^{2}+(−1)−4 \\ 3+(−1)^{2}−3\end{aligned}] \\ & =[\begin{aligned}3 \\ −1\end{aligned}]−[\begin{aligned}6 & 1 \\ 1 & −2\end{aligned}]^{−1}[\begin{aligned}4 \\ 1\end{aligned}] \\ & =[\begin{aligned}3 \\ −1\end{aligned}]−\frac{1}{6⋅(−2)−1⋅1}[\begin{aligned}−2 & −1 \\ −1 & 6\end{aligned}][\begin{aligned}4 \\ 1\end{aligned}] \\ & =[\begin{aligned}3 \\ −1\end{aligned}]+\frac{1}{13}[\begin{aligned}−9 \\ 2\end{aligned}] \\ & =\begin{aligned}\frac{30}{13} \\ −\frac{11}{13}\end{aligned} \\ & ≈[\begin{aligned}2.308 \\ −0.846\end{aligned}],\end{aligned}


$$

rounded to three decimal places.

### Alternative to Newton's Method for Multivariable Functions Using Linear Systems

Now that we’ve seen how to apply Newton’s method in the multivariable case, it’s worth noting that the standard update formula

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [J_{\boldsymbol{f}}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n)


$$

is not always the most practical way for us to compute the next step. In higher dimensions, it’s often more useful to avoid calculating the inverse of a large matrix by rewriting the update as a linear system instead.

Let’s go through how we can do that step by step.

We start with the standard Newton update

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [J_{\boldsymbol{f}}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n).


$$

Next, we subtract $\mathbf{x}_n$ from both sides

$$


\mathbf{x}_{n+1} - \mathbf{x}_n = - [J_{\boldsymbol{f}}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n).


$$

Then, we multiply both sides by $J_{\boldsymbol{f}}(\mathbf{x}_n)$

$$


J_{\boldsymbol{f}}(\mathbf{x}_n)(\mathbf{x}_{n+1} - \mathbf{x}_n) = -\boldsymbol{f}(\mathbf{x}_n).


$$

This gives us the *linear system form* of Newton’s method. This equivalent form allows us to solve directly for the update direction $\mathbf{x}_{n+1} - \mathbf{x}_n$ without ever computing the inverse of the Jacobian.

To better understand how the method works in practice, let’s walk through a concrete example.

### A Worked Example

Suppose we are looking for a zero of the function

$$


[\begin{aligned}𝑥^{4}−𝑦^{2}+5 \\ 𝑥^{2}−𝑦^{3}+1\end{aligned}]


$$

in the region $[-2, 2] \times [-2, 3] \subseteq \mathbb{R}^2$.

The Newton-Raphson method of finding the zeros of a multivariable function $\boldsymbol{f}: \mathbb{R}^n \to \mathbb{R}^n$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [J_\boldsymbol{f}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n),


$$

where $J_\boldsymbol{f}(\mathbf{x}_n)$ is the Jacobian of $\boldsymbol f$ evaluated at $\mathbf{x}_n.$

Equivalently, at each iteration, the above equation can be re-written as

$$


J_\boldsymbol{f}(\mathbf{x}_n)(\mathbf{x}_{n+1}-\mathbf{x}_n) = -\boldsymbol{f}(\mathbf{x}_n).


$$

In our case, the Jacobian is

$$


\begin{aligned}𝐽_{𝒇}(𝐱) & =\begin{aligned}\frac{𝜕}{𝜕𝑥}(𝑥^{4}−𝑦^{2}+5) & \frac{𝜕}{𝜕𝑦}(𝑥^{4}−𝑦^{2}+5) \\ \frac{𝜕}{𝜕𝑥}(𝑥^{2}−𝑦^{3}+1) & \frac{𝜕}{𝜕𝑦}(𝑥^{2}−𝑦^{3}+1)\end{aligned} \\ & =[\begin{aligned}4𝑥^{3} & −2𝑦 \\ 2𝑥 & −3𝑦^{2}\end{aligned}].\end{aligned}


$$

Therefore, our Newton-Raphson system of equations is

$$


[\begin{aligned}4𝑥^{3} & −2𝑦 \\ 2𝑥 & −3𝑦^{2}\end{aligned}]


$$

Starting with $[\begin{aligned}1 \\ 1\end{aligned}]$ we have

$$


\begin{aligned}[\begin{aligned}4𝑥^{3} & −2𝑦 \\ 2𝑥 & −3𝑦^{2}\end{aligned}]_{𝐱_{0}}(𝐱_{1}−𝐱_{0}) & =−[\begin{aligned}𝑥^{4}−𝑦^{2}+5 \\ 𝑥^{2}−𝑦^{3}+1\end{aligned}]_{𝐱_{0}} \\ [\begin{aligned}4(1)^{3} & −2(1) \\ 2(1) & −3(1)^{2}\end{aligned}](𝐱_{1}−𝐱_{0}) & =−[\begin{aligned}(1)^{4}−(1)^{2}+5 \\ (1)^{2}−(1)^{3}+1\end{aligned}] \\ [\begin{aligned}4 & −2 \\ 2 & −3\end{aligned}](𝐱_{1}−𝐱_{0}) & =[\begin{aligned}−5 \\ −1\end{aligned}].\end{aligned}


$$

Let’s solve this system using Gaussian elimination. We first set $[\begin{aligned}𝑑_{1} \\ 𝑑_{2}\end{aligned}]$, so the system becomes

$$


[\begin{aligned}4 & −2 \\ 2 & −3\end{aligned}]


$$

We write the augmented matrix as

$$


\begin{aligned}4 & −2 & −5 \\ 2 & −3 & −1\end{aligned}


$$

To eliminate the entry below the leading $4$, we perform the row operation $R_2:= R_2 - \dfrac{1}{2} R_1{:}$

$$


\begin{aligned}4 & −2 & −5 \\ 0 & −2 & 1.5\end{aligned}


$$

From the second row, we get

$$


-2d_2 = 1.5 \quad \Rightarrow \quad d_2 = -0.75.


$$

We then substitute this into the first row, which gives

$$


4d_1 - 2(-0.75) = -5 \quad \Rightarrow \quad 4d_1 = -6.5 \quad \Rightarrow \quad d_1 = -1.625.


$$

So, the update vector is

$$


[\begin{aligned}−1.625 \\ −0.75\end{aligned}]


$$

Hence, our updated approximation of the root is given by

$$


\begin{aligned}𝐱_{1} & =𝐱_{0}+[\begin{aligned}−1.625 \\ −0.75\end{aligned}] \\ & =[\begin{aligned}1 \\ 1\end{aligned}]+[\begin{aligned}−1.625 \\ −0.75\end{aligned}] \\ & =[\begin{aligned}−0.625 \\ 0.25\end{aligned}].\end{aligned}


$$

### Example: Computing Iterations of the Newton-Raphson Method Using Linear Systems

#### Question

Suppose we wish to find a zero of the function $\boldsymbol{f}(x,y)$ in the region $[0,1] \times [0,1] \subseteq \mathbb{R}^2,$ where

$$


[\begin{aligned}𝑥^{2}−𝑦^{2} \\ 2𝑥𝑦−1\end{aligned}]


$$

Find the matrix equation that defines the first iteration of the Newton-Raphson process starting at the point $\big[1, \: 1 \big]^T,$ and compute the components of the first iteration.

#### Explanation

The Newton-Raphson method of finding the zeros of a multivariable function $\boldsymbol{f}: \mathbb{R}^n \to \mathbb{R}^n$ is

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [J_\boldsymbol{f}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n),


$$

where $J_\boldsymbol{f}(\mathbf{x}_n)$ is the Jacobian of $\boldsymbol f$ evaluated at $\mathbf{x}_n.$

Equivalently, at each iteration, the above equation can be re-written as

$$


J_\boldsymbol{f}(\mathbf{x}_n)(\mathbf{x}_{n+1}-\mathbf{x}_n) = -\boldsymbol{f}(\mathbf{x}_n).


$$

In our case, the Jacobian is

$$


\begin{aligned}𝐽_{𝒇}(𝐱) & =\begin{aligned}\frac{𝜕}{𝜕𝑥}(𝑥^{2}−𝑦^{2}) & \frac{𝜕}{𝜕𝑦}(𝑥^{2}−𝑦^{2}) \\ \frac{𝜕}{𝜕𝑥}(2𝑥𝑦−1) & \frac{𝜕}{𝜕𝑦}(2𝑥𝑦−1)\end{aligned} \\ & =[\begin{aligned}2𝑥 & −2𝑦 \\ 2𝑦 & 2𝑥\end{aligned}].\end{aligned}


$$

Therefore, our Newton-Raphson system of equations is

$$


[\begin{aligned}2𝑥 & −2𝑦 \\ 2𝑦 & 2𝑥\end{aligned}]


$$

Starting with $[\begin{aligned}1 \\ 1\end{aligned}]$ we have

$$


\begin{aligned}[\begin{aligned}2𝑥 & −2𝑦 \\ 2𝑦 & 2𝑥\end{aligned}]_{𝐱_{0}}(𝐱_{1}−𝐱_{0}) & =−[\begin{aligned}𝑥^{2}−𝑦^{2} \\ 2𝑥𝑦−1\end{aligned}]_{𝐱_{0}} \\ [\begin{aligned}2(1) & −2(1) \\ 2(1) & 2(1)\end{aligned}](𝐱_{1}−𝐱_{0}) & =−[\begin{aligned}(1)^{2}−(1)^{2} \\ 2(1)(1)−1\end{aligned}] \\ [\begin{aligned}2 & −2 \\ 2 & 2\end{aligned}](𝐱_{1}−𝐱_{0}) & =[\begin{aligned}0 \\ −1\end{aligned}].\end{aligned}


$$

Solving this system of equations, we get $[\begin{aligned}−0.25 \\ −0.25\end{aligned}]$ Hence,

$$


\begin{aligned}𝐱_{1} & =𝐱_{0}+[\begin{aligned}−0.25 \\ −0.25\end{aligned}] \\ & =[\begin{aligned}1 \\ 1\end{aligned}]+[\begin{aligned}−0.25 \\ −0.25\end{aligned}] \\ & =[\begin{aligned}0.75 \\ 0.75\end{aligned}].\end{aligned}


$$

### Derivation of the Formula

Just like in the single-variable case, the idea is to simplify the problem by replacing a nonlinear function with its linear approximation near our current guess.

Suppose we want to solve a system of nonlinear equations

$$


\boldsymbol{f}(\mathbf{x}) = \mathbf{0},


$$

where $\boldsymbol{f}: \mathbb{R}^n \to \mathbb{R}^n$ is a vector-valued function.

Near a point $\mathbf{x}_0$, we approximate $\boldsymbol{f}(\mathbf{x})$ using its first-order Taylor expansion:

$$


\boldsymbol{f}(\mathbf{x}) \approx \boldsymbol{f}(\mathbf{x}_0) + J_{\boldsymbol{f}}(\mathbf{x}_0)(\mathbf{x} - \mathbf{x}_0),


$$

where $J_{\boldsymbol{f}}(\mathbf{x}_0)$ is the Jacobian matrix of $\boldsymbol{f}$ evaluated at $\mathbf{x}_0$.

Since this linear approximation is valid near $\mathbf{x}_0$, we solve the simpler system

$$


\boldsymbol{f}(\mathbf{x}_0) + J_{\boldsymbol{f}}(\mathbf{x}_0)(\mathbf{x} - \mathbf{x}_0) = \mathbf{0}


$$

instead of the full nonlinear system.

To find the next guess $\mathbf{x}_1$, we solve this linear system for $\mathbf{x}$. We isolate the term $\mathbf{x}$, as follows:

$$


\begin{aligned}𝐽_{𝒇}(𝐱_{0})(𝐱−𝐱_{0}) & =−𝒇(𝐱_{0}) \\ 𝐱−𝐱_{0} & =−[𝐽_{𝒇}(𝐱_{0})]^{−1}𝒇(𝐱_{0}) \\ 𝐱 & =𝐱_{0}−[𝐽_{𝒇}(𝐱_{0})]^{−1}𝒇(𝐱_{0})\end{aligned}


$$

This new value becomes our next guess, which we call $\mathbf{x}_1$. So, we write

$$


\mathbf{x}_{n+1} = \mathbf{x}_n - [J_{\boldsymbol{f}}(\mathbf{x}_n)]^{-1} \boldsymbol{f}(\mathbf{x}_n).


$$

This is the multivariable version of the Newton–Raphson update rule.
