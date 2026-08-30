# Solving Inhomogeneous Systems of ODEs

Source: https://www.mathacademy.com/topics/3189?courseId=155
Topic ID: 3189

## Prerequisites

- [Solving Homogeneous Systems of ODEs With Repeated Eigenvalues](./2818-solving-homogeneous-systems-of-odes-with-repeated-eigenvalues.md)
- [Solving Homogeneous Systems of ODEs With Complex Eigenvalues](./2819-solving-homogeneous-systems-of-odes-with-complex-eigenvalues.md)
- [Solving First-Order Linear ODEs With Exponential Forcing](../differential-equations/6679-solving-first-order-linear-odes-with-exponential-forcing.md)
- [Solving First-Order Linear ODEs With Sinusoidal Forcing](../differential-equations/6680-solving-first-order-linear-odes-with-sinusoidal-forcing.md)

## Lesson

### Introduction

Consider an **inhomogeneous** linear system of ordinary differential equations in component form:

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=𝑎_{11}𝑥_{1}(𝑡)+𝑎_{12}𝑥_{2}(𝑡)+𝑓_{1}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=𝑎_{21}𝑥_{1}(𝑡)+𝑎_{22}𝑥_{2}(𝑡)+𝑓_{2}(𝑡)\end{aligned}


$$

Here, we can package the unknown functions into vectors

$$


[\begin{aligned}𝑥_{1}(𝑡) \\ 𝑥_{2}(𝑡)\end{aligned}]


$$

Then, the system can be written as

$$


[\begin{aligned}𝑎_{11} & 𝑎_{12} \\ 𝑎_{21} & 𝑎_{22}\end{aligned}]


$$

Often, the **forcing functions** $f_1(t), f_2(t)$ are linear combinations of a few basic functions (such as $e^{3t},$ $t^2,$ or $\sin t$). In that case, it is useful to write $\mathbf{g}(t)$ as a sum of those basic functions times constant vectors.

For example, let's write down the system of linear ODEs below in matrix form.

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=4𝑥_{1}(𝑡)+2𝑥_{2}(𝑡)+8𝑒^{3𝑡} \\ 𝑥_{′2}^{}(𝑡)=−3𝑥_{1}(𝑡)+5𝑥_{2}(𝑡)+10𝑒^{4𝑡}\end{aligned}


$$

First, let's rewrite our system, highlighting the coefficients:

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=4⋅𝑥_{1}(𝑡)+2⋅𝑥_{2}(𝑡)+𝑒^{3𝑡}⋅8+𝑒^{4𝑡}⋅0 \\ 𝑥_{′2}^{}(𝑡)=(−3)⋅𝑥_{1}(𝑡)+5⋅𝑥_{2}(𝑡)+𝑒^{3𝑡}⋅0+𝑒^{4𝑡}⋅10\end{aligned}


$$

Now, we can write the system in matrix form:

$$


[\begin{aligned}4 & 2 \\ −3 & 5\end{aligned}]


$$

where $[\begin{aligned}𝑥_{1}(𝑡) \\ 𝑥_{2}(𝑡)\end{aligned}]$

### Example: Writing Down an Inhomogeneous System of Linear ODEs in Matrix Form

#### Question

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=−2𝑥_{1}(𝑡)−𝑥_{2}(𝑡)+4𝑡^{2}+𝑡−2 \\ 𝑥_{′2}^{}(𝑡)=3𝑥_{1}(𝑡)−𝑡^{2}+5𝑡+6\end{aligned}


$$

Write the system of linear ODEs in matrix form.

#### Explanation

First, let's rewrite our system, highlighting the coefficients:

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=(−2)⋅𝑥_{1}(𝑡)+(−1)⋅𝑥_{2}(𝑡)+4⋅𝑡^{2}+1⋅𝑡+(−2) \\ 𝑥_{′2}^{}(𝑡)=3⋅𝑥_{1}(𝑡)+0⋅𝑥_{2}(𝑡)+(−1)⋅𝑡^{2}+5⋅𝑡+6\end{aligned}


$$

Now, we can write the system in matrix form:

$$


\begin{aligned}−2 & −1 \\ 3 & 0\end{aligned}


$$

where $[\begin{aligned}𝑥_{1}(𝑡) \\ 𝑥_{2}(𝑡)\end{aligned}]$

### Complementary vs. Particular Solutions

Recall that an inhomogeneous linear system has the form

$$


\mathbf{x}'(t)=A\mathbf{x}(t)+\mathbf{g}(t),


$$

where $A$ is a constant matrix and $\mathbf{g}(t)$ is a known forcing term. The associated *homogeneous* system is

$$


\mathbf{x}'(t)=A\mathbf{x}(t).


$$

A *general solution* of the *homogeneous* system is called the **complementary solution** and is denoted by $\mathbf{x}_c(t)$. A **particular solution** is any single function $\mathbf{x}_p(t)$ that satisfies the full inhomogeneous system.

These two pieces combine to give the *general solution* of the inhomogeneous system:

$$


\mathbf{x}(t)=\mathbf{x}_c(t)+\mathbf{x}_p(t)


$$

Indeed, notice that

$$


\begin{aligned}(𝐱_{𝑐}+𝐱_{𝑝})^{′} & =𝐱_{′𝑐}^{}+𝐱_{′𝑝}^{} \\ & =(𝐴𝐱_{𝑐})+(𝐴𝐱_{𝑝}+𝐠(𝑡)) \\ & =𝐴𝐱_{𝑐}+𝐴𝐱_{𝑝}+𝐠(𝑡) \\ & =𝐴(𝐱_{𝑐}+𝐱_{𝑝})+𝐠(𝑡).\end{aligned}


$$

Since $(\mathbf{x}_c+\mathbf{x}_p)' = A(\mathbf{x}_c+\mathbf{x}_p)+\mathbf{g}(t)$, the sum is a solution of the inhomogeneous system.

Notice that it doesn't matter which particular solution we take. Suppose we found two different particular solutions, $\mathbf{x}_p(t)$ and $\mathbf{y}_p(t).$ Let's examine their difference, $\mathbf{w}(t) = \mathbf{y}_p(t) - \mathbf{x}_p(t)$.

By definition, we know that $\mathbf{y}_p' = A\mathbf{y}_p + \mathbf{g}(t)$ and $\mathbf{x}_p' = A\mathbf{x}_p + \mathbf{g}(t).$ Now, let's find the derivative of the difference $\mathbf{w}(t)$:

$$


\begin{aligned}𝐰^{′} & =(𝐲_{𝑝}−𝐱_{𝑝})^{′} \\ & =𝐲_{′𝑝}^{}−𝐱_{′𝑝}^{} \\ & =(𝐴𝐲_{𝑝}+𝐠(𝑡))−(𝐴𝐱_{𝑝}+𝐠(𝑡)) \\ & =𝐴𝐲_{𝑝}−𝐴𝐱_{𝑝} \\ & =𝐴(𝐲_{𝑝}−𝐱_{𝑝}) \\ & =𝐴𝐰\end{aligned}


$$

The result $\mathbf{w}' = A\mathbf{w}$ means that the difference between any two particular solutions is itself a solution to the *homogeneous* system.

This is why *any* particular solution is enough. Any other particular solution can be written as

$$


\mathbf{y}_{p} = \underbrace{(\mathbf{y}_{p}-\mathbf{x}_{p})}_{\text{homogeneous}} \:\:\: + \underbrace{\mathbf{x}_{p}}_{\text{particular}} \!\!\!\!\!.


$$

The "variety" among particular solutions is already captured by the complementary solution $\mathbf{x}_c(t)$.

### Choosing the Form of a Particular Solution

To solve

$$


\mathbf{x}'(t)=A\mathbf{x}(t)+\mathbf{g}(t),


$$

we often look for a particular solution $\mathbf{x}_p(t)$ whose *form matches the forcing term* $\mathbf{g}(t)$.

In each case below, the unknowns are constant vectors (to be determined by substitution).

- **Constant forcing.** If $\mathbf{g}(t)$ is a constant vector, then we try where $\mathbf{a}$ is a constant vector.

- **Polynomial forcing.** If $\mathbf{g}(t)$ is a polynomial of degree $n$, then we try where $\mathbf{a}_n,\mathbf{a}_{n-1},\ldots,\mathbf{a}_1,\mathbf{a}_0$ are constant vectors.

- **Exponential forcing.** If $\mathbf{g}(t)=e^{\alpha t}\mathbf{v}$ for some constant vector $\mathbf{v},$ then we try where $\mathbf{a}$ is a constant vector.

- **Trigonometric forcing.** If $\mathbf{g}(t)=\cos(\beta t)\mathbf{v}$ or $\mathbf{g}(t)=\sin(\beta t)\mathbf{v}$ for some constant vector $\mathbf{v},$ then we try where $\mathbf{a}$ and $\mathbf{b}$ are constant vectors.

In the next step, we substitute the chosen $\mathbf{x}_p(t)$ into the differential equation to solve for the unknown vectors.

Let's see some concrete examples.

### Example: Identifying the Form of a Particular Solution for Inhomogeneous System of Linear ODEs

#### Question

Consider the following inhomogeneous system of linear differential equations:

$$


[\begin{aligned}−3 & 6 \\ −3 & 3\end{aligned}]


$$

A complementary solution to this system is given by

$$


[\begin{aligned}2cos⁡(3𝑡) \\ cos⁡(3𝑡)−sin⁡(3𝑡)\end{aligned}]


$$

Then, the general solution of the system can be written as $\mathbf{x}(t)=\mathbf{x}_c(t)+\mathbf{x}_p(t),$ where $\mathbf{x}_p(t)$ is a particular solution. Determine the form of the particular solution $\mathbf{x}_p(t).$

#### Explanation

Recall that the general solution of an inhomogeneous system can be written as

$$


\mathbf{x}(t)=\mathbf{x}_c(t)+\mathbf{x}_p(t)


$$

where $\mathbf{x}_c(t)$ is the complementary solution (solution of the corresponding homogeneous system) and $\mathbf{x}_p(t)$ is a particular solution.

The forcing term

$$


[\begin{aligned}−3 \\ 2\end{aligned}]


$$

of the inhomogeneous system of ODEs is sinusoidal. Therefore, we assume that the particular solution is also sinusoidal, i.e.

$$


[\begin{aligned}𝑎_{1} \\ 𝑎_{2}\end{aligned}]


$$

where $a_1,a_2,b_1,b_2$ are constants that are to be determined.

### Example: Finding the Particular Solution of an Inhomogeneous System of Linear ODEs

#### Question

Consider the following inhomogeneous system of linear differential equations:

$$


[\begin{aligned}3 & 1 \\ 0 & 1\end{aligned}]


$$

The complementary solution to this system is given by

$$


[\begin{aligned}𝑒^{3𝑡} \\ 0\end{aligned}]


$$

Find the general solution of the system.

#### Explanation

Recall that the general solution of an inhomogeneous system can be written as

$$


\mathbf{x}(t) = \mathbf{x}_c(t) + \mathbf{x}_p(t)


$$

where $\mathbf{x}_c(t)$ is the complementary solution (solution of the corresponding homogeneous system) and $\mathbf{x}_p(t)$ is a particular solution.

The forcing term

$$


[\begin{aligned}−1 \\ −3\end{aligned}]


$$

of the inhomogeneous system of ODEs is exponential. Therefore, we assume that the particular solution is also exponential, i.e.

$$


[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]


$$

where $a,b$ are constants that are to be determined.

Calculating the derivative of $\mathbf{x}_p$ with respect to $t$ gives

$$


[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]


$$

To find the unknown constants, we substitute $\mathbf{x}_p$ and $\mathbf{x}'_p$ into our system:

$$


\begin{aligned}7𝑒^{7𝑡}[\begin{aligned}𝑎 \\ 𝑏\end{aligned}] & =[\begin{aligned}3 & 1 \\ 0 & 1\end{aligned}]⋅𝑒^{7𝑡}[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]+𝑒^{7𝑡}[\begin{aligned}−1 \\ −3\end{aligned}] \\ 7[\begin{aligned}𝑎 \\ 𝑏\end{aligned}] & =[\begin{aligned}3 & 1 \\ 0 & 1\end{aligned}]⋅[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]+[\begin{aligned}−1 \\ −3\end{aligned}] \\ [\begin{aligned}7𝑎 \\ 7𝑏\end{aligned}] & =[\begin{aligned}3𝑎+𝑏 \\ 𝑏\end{aligned}]+[\begin{aligned}−1 \\ −3\end{aligned}] \\ [\begin{aligned}7𝑎 \\ 7𝑏\end{aligned}] & =[\begin{aligned}3𝑎+𝑏−1 \\ 𝑏−3\end{aligned}]\end{aligned}


$$

Equating the corresponding components, we get the following system:

$$


\begin{aligned}3𝑎+𝑏−1=7𝑎 \\ 𝑏−3=7𝑏\end{aligned}


$$

From the second equation, we get

$$


b - 7b = 3 \qquad\Rightarrow\qquad b = -\dfrac12.


$$

Substituting this into the first equation and solving for $a,$ we have

$$


3a - \dfrac12 - 1 = 7a \qquad\Rightarrow\qquad a = -\dfrac38.


$$

Therefore, the particular solution is

$$


\begin{aligned}−\frac{3}{8} \\ −\frac{1}{2}\end{aligned}


$$

And thus, the general solution is given by

$$


\begin{aligned}−\frac{3}{8} \\ −\frac{1}{2}\end{aligned}


$$

### Example: Solving an Initial Value Problem for an Inhomogeneous System of Linear ODEs

#### Question

$$


[\begin{aligned}1 & 1 \\ 0 & 1\end{aligned}]


$$

Find the missing coefficients in the solution to the initial value problem, shown above.

$$


[\begin{aligned}𝑒^{𝑡} \\ 0\end{aligned}]


$$

#### Explanation

We are told that the general solution to the system is

$$


[\begin{aligned}𝑒^{𝑡} \\ 0\end{aligned}]


$$

where $c_1,c_2$ are constants that are to be determined.

Next, we find the values of $c_1$ and $c_2.$ Substituting $t = 0$ into the general solution, we get the following:

$$


\begin{aligned}𝐱(0) & =[\begin{aligned}6 \\ 1\end{aligned}] \\ 𝑐_{1}[\begin{aligned}𝑒^{0} \\ 0\end{aligned}]+𝑐_{2}[\begin{aligned}0⋅𝑒^{0} \\ 𝑒^{0}\end{aligned}]+[\begin{aligned}0^{2}−0+4 \\ −0^{2}+2\end{aligned}] & =[\begin{aligned}6 \\ 1\end{aligned}] \\ 𝑐_{1}[\begin{aligned}1 \\ 0\end{aligned}]+𝑐_{2}[\begin{aligned}0 \\ 1\end{aligned}]+[\begin{aligned}4 \\ 2\end{aligned}] & =[\begin{aligned}6 \\ 1\end{aligned}] \\ [\begin{aligned}𝑐_{1}+4 \\ 𝑐_{2}+2\end{aligned}] & =[\begin{aligned}6 \\ 1\end{aligned}]\end{aligned}


$$

So, we have the following system of linear equations:

$$


\begin{aligned}𝑐_{1}+4=6 \\ 𝑐_{2}+2=1\end{aligned}


$$

From the first equation, we get $c_1 = 2.$ From the second equation, we have $c_2 = -1.$

Therefore, the solution to the initial value problem is

$$


[\begin{aligned}𝑒^{𝑡} \\ 0\end{aligned}]


$$
