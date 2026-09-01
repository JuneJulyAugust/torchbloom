# Solving Homogeneous Systems of ODEs Using Matrix Methods

Source: https://www.mathacademy.com/topics/6690?courseId=61
Topic ID: 6690

## Prerequisites

- [The Hyperbolic Functions](../calculus-i/967-the-hyperbolic-functions.md)
- [Fundamental Matrices](./6376-fundamental-matrices.md)

## Lesson

### Introduction

Matrix exponentials can be used for solving homogeneous systems of the form

$$


\mathbf{x}'(t)=A\mathbf{x}(t),


$$

where $A$ is a constant square matrix.

For example, consider the system

$$


\begin{aligned}𝑥^{′}(𝑡)=5𝑦(𝑡) \\ 𝑦^{′}(𝑡)=−5𝑥(𝑡)\end{aligned}


$$

Writing our system in matrix form, we get

$$


[\begin{aligned}0 & 5 \\ −5 & 0\end{aligned}]


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ So, the matrix of the system is $[\begin{aligned}0 & 5 \\ −5 & 0\end{aligned}]$

Recall that given the system $\mathbf{x}'(t) = A \mathbf{x}(t),$ where $A$ is a constant square matrix, the general solution of the system can be written as

$$


\mathbf{x}(t) = \Phi(t) \, \mathbf{c},


$$

where $\Phi(t)$ is a fundamental matrix of the system, and $\mathbf{c}$ is some constant vector.

Since we have already seen how to compute the standard fundamental matrix, we will not repeat the calculation here. So, computing the standard fundamental matrix $\Phi_0(t)$ of the system, we get

$$


[\begin{aligned}cos⁡(5𝑡) & sin⁡(5𝑡) \\ −sin⁡(5𝑡) & cos⁡(5𝑡)\end{aligned}]


$$

Therefore, the general solution is

$$


\begin{aligned}𝐱(𝑡) & =Φ_{0}(𝑡)\,𝐜 \\ & =𝑒^{𝐴𝑡}\,𝐜 \\ & =[\begin{matrix}cos⁡(5𝑡) & sin⁡(5𝑡) \\ −sin⁡(5𝑡) & cos⁡(5𝑡)\end{matrix}][\begin{matrix}𝑐_{1} \\ 𝑐_{2}\end{matrix}] \\ & =𝑐_{1}[\begin{matrix}cos⁡(5𝑡) \\ −sin⁡(5𝑡)\end{matrix}]+𝑐_{2}[\begin{matrix}sin⁡(5𝑡) \\ cos⁡(5𝑡)\end{matrix}],\end{aligned}


$$

where $c_1,c_2 \in \mathbb{R}.$

**Note:** Recall that for the general solution of the ordinary differential equation $x'(t)=ax(t),$ we have

$$


x'(t)=ax(t) \qquad\Rightarrow\qquad x(t) = c \, e^{at}, \quad c \in \mathbb{R}.


$$

Now, for the general solution of the matrix differential equation $\mathbf{x}'(t)=A\mathbf{x}(t),$ we obtain

$$


\mathbf{x}'(t)=A\mathbf{x}(t) \qquad\Rightarrow\qquad \mathbf{x}(t) = e^{At} \, \mathbf{c}, \quad \mathbf{c} \in \mathbb{R}^n.


$$

Let's see more examples.

### Example: Finding the General Solution of a Homogeneous System Using a Given Matrix Exponential

#### Question

$$


\begin{aligned}𝑥^{′}(𝑡)=−7𝑥(𝑡)+𝑦(𝑡) \\ 𝑦^{′}(𝑡)=−7𝑦(𝑡)\end{aligned}


$$

Find the general solution to the system of ODEs above.

**

#### Explanation

Writing our system in matrix form, we get

$$


[\begin{aligned}−7 & 1 \\ 0 & −7\end{aligned}]


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ So, the matrix of the system is $[\begin{aligned}−7 & 1 \\ 0 & −7\end{aligned}]$

Given the system $\mathbf{x}'(t) = A \mathbf{x}(t),$ where $A$ is a constant square matrix, the general solution of the system can be written as

$$


\mathbf{x}(t) = \Phi(t) \, \mathbf{c},


$$

where $\Phi(t)$ is a fundamental matrix of the system, and $\mathbf{c}$ is a constant vector.

Now, using the given information, the standard fundamental matrix $\Phi_0(t)$ of the system is given by

$$


[\begin{aligned}𝑒^{−7𝑡} & 𝑡𝑒^{−7𝑡} \\ 0 & 𝑒^{−7𝑡}\end{aligned}]


$$

Therefore, the general solution is

$$


\begin{aligned}𝐱(𝑡) & =Φ_{0}(𝑡)\,𝐜 \\ & =𝑒^{𝐴𝑡}\,𝐜 \\ & =[\begin{matrix}𝑒^{−7𝑡} & 𝑡𝑒^{−7𝑡} \\ 0 & 𝑒^{−7𝑡}\end{matrix}][\begin{matrix}𝑐_{1} \\ 𝑐_{2}\end{matrix}] \\ & =𝑐_{1}[\begin{matrix}𝑒^{−7𝑡} \\ 0\end{matrix}]+𝑐_{2}[\begin{matrix}𝑡𝑒^{−7𝑡} \\ 𝑒^{−7𝑡}\end{matrix}] \\ & =𝑐_{1}[\begin{matrix}1 \\ 0\end{matrix}]𝑒^{−7𝑡}+𝑐_{2}[\begin{matrix}𝑡 \\ 1\end{matrix}]𝑒^{−7𝑡},\end{aligned}


$$

where $c_1,c_2 \in \mathbb{R}.$

### Solving Initial Value Problems

Now, let's find the solution to the initial value problem below

$$


\begin{aligned}𝑥^{′}(𝑡)=7𝑥(𝑡)+𝑦(𝑡) \\ 𝑦^{′}(𝑡)=7𝑦(𝑡),\end{aligned}


$$

Writing our system in matrix form, we get

$$


[\begin{aligned}7 & 1 \\ 0 & 7\end{aligned}]


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ So, the matrix of the system is $[\begin{aligned}7 & 1 \\ 0 & 7\end{aligned}]$

Recall that the general solution of the system $\mathbf{x}'(t) = A \mathbf{x}(t),$ where $A$ is a constant square matrix, can be written as

$$


\mathbf{x}(t) = \Phi_0(t) \, \mathbf{c},


$$

where $\Phi_0(t) = e^{At}$ is the standard fundamental matrix of the system, and $\mathbf{c}$ is some constant vector.

Evaluating both sides of $\mathbf{x}(t) = e^{At} \mathbf{c}$ at $t=0,$ we get

$$


\begin{aligned}𝐱(0) & =Φ_{0}(0)\,𝐜 \\ 𝐱(0) & =𝑒^{𝐴(0)}\,𝐜 \\ 𝐱(0) & =𝐼\,𝐜 \\ 𝐜 & =𝐱(0).\end{aligned}


$$

Thus, the solution to our initial value problem is

$$


\mathbf{x}(t) = \Phi_0(t) \, \mathbf{x}(0).


$$

Computing the standard fundamental matrix $\Phi_0(t)$ of the system, we get

$$


[\begin{aligned}𝑒^{7𝑡} & 𝑡𝑒^{7𝑡} \\ 0 & 𝑒^{7𝑡}\end{aligned}]


$$

Therefore, the solution is

$$


\begin{aligned}𝐱(𝑡) & =𝑒^{𝐴𝑡}\,𝐱(0) \\ & =[\begin{matrix}𝑒^{7𝑡} & 𝑡𝑒^{7𝑡} \\ 0 & 𝑒^{7𝑡}\end{matrix}][\begin{matrix}3 \\ −2\end{matrix}] \\ & =[\begin{matrix}(3−2𝑡)𝑒^{7𝑡} \\ −2𝑒^{7𝑡}\end{matrix}].\end{aligned}


$$

### Example: Solving a Homogeneous Initial Value Problem Using a Given Matrix Exponential

#### Question

$$


\begin{aligned}𝑥^{′}(𝑡)=3𝑦(𝑡) \\ 𝑦^{′}(𝑡)=−3𝑥(𝑡),\end{aligned}


$$

Find the solution to the initial value problem above.

**

#### Explanation

Writing our system in matrix form, we get

$$


[\begin{aligned}0 & 3 \\ −3 & 0\end{aligned}]


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ So, the matrix of the system is $[\begin{aligned}0 & 3 \\ −3 & 0\end{aligned}]$

Given the system $\mathbf{x}'(t) = A \mathbf{x}(t),$ where $A$ is a constant square matrix, the solution of the initial value problem can be written as

$$


\mathbf{x}(t) = \Phi_0(t) \, \mathbf{x}(0),


$$

where $\Phi_0(t) = e^{At}$ is the standard fundamental matrix of the system, and $\mathbf{x}(0)$ is the initial condition vector.

Now, using the given information, the standard fundamental matrix $\Phi_0(t)$ of the system is given by

$$


[\begin{aligned}cos⁡(3𝑡) & sin⁡(3𝑡) \\ −sin⁡(3𝑡) & cos⁡(3𝑡)\end{aligned}]


$$

Therefore, the solution is

$$


\begin{aligned}𝐱(𝑡) & =𝑒^{𝐴𝑡}\,𝐱(0) \\ & =[\begin{matrix}cos⁡(3𝑡) & sin⁡(3𝑡) \\ −sin⁡(3𝑡) & cos⁡(3𝑡)\end{matrix}][\begin{matrix}2 \\ −1\end{matrix}] \\ & =[\begin{matrix}2cos⁡(3𝑡)−sin⁡(3𝑡) \\ −2sin⁡(3𝑡)−cos⁡(3𝑡)\end{matrix}].\end{aligned}


$$

### Solving Initial Value Problems With Shifted Conditions

Next, let's find the solution to the initial value problem

$$


\begin{aligned}𝑥^{′}(𝑡)=−7𝑦(𝑡) \\ 𝑦^{′}(𝑡)=7𝑥(𝑡),\end{aligned}


$$

given that $[\begin{aligned}cos⁡(7𝑡) & −sin⁡(7𝑡) \\ sin⁡(7𝑡) & cos⁡(7𝑡)\end{aligned}]$ where $[\begin{aligned}0 & −7 \\ 7 & 0\end{aligned}]$

Writing our system in matrix form, we get

$$


[\begin{aligned}0 & −7 \\ 7 & 0\end{aligned}]


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ So, the matrix of the system is $[\begin{aligned}0 & −7 \\ 7 & 0\end{aligned}]$

Given the system $\mathbf{x}'(t) = A \mathbf{x}(t),$ where $A$ is a constant square matrix, the general solution is $\mathbf{x}(t) = e^{At} \, \mathbf{c}.$ We can determine the constant vector $\mathbf{c}$ using the initial condition at time $t=t_0{:}$

$$


\mathbf{x}(t_0) = e^{At_0} \, \mathbf{c} \implies \mathbf{c} = e^{-At_0} \, \mathbf{x}(t_0),


$$

since the inverse of $e^{At_0}$ is $e^{-At_0}.$ Plugging this back into our general solution gives the formula

$$


\begin{aligned}𝐱(𝑡) & =𝑒^{𝐴𝑡}\,𝑒^{−𝐴𝑡_{0}}\,𝐱(𝑡_{0}) \\ & =𝑒^{𝐴(𝑡−𝑡_{0})}\,𝐱(𝑡_{0}).\end{aligned}


$$

Therefore, the solution to our specific problem (with $t_0=1$) is

$$


\begin{aligned}𝐱(𝑡) & =𝑒^{𝐴(𝑡−1)}\,𝐱(1) \\ & =[\begin{matrix}cos⁡(7(𝑡−1)) & −sin⁡(7(𝑡−1)) \\ sin⁡(7(𝑡−1)) & cos⁡(7(𝑡−1))\end{matrix}][\begin{matrix}0 \\ −4\end{matrix}] \\ & =[\begin{matrix}4sin⁡(7(𝑡−1)) \\ −4cos⁡(7(𝑡−1))\end{matrix}].\end{aligned}


$$

### Example: Solving a Homogeneous Initial Value Problem Using a Given Matrix Exponential: Shifted Initial Conditions

#### Question

$$


\begin{aligned}𝑥^{′}(𝑡)=7𝑦(𝑡) \\ 𝑦^{′}(𝑡)=7𝑥(𝑡),\end{aligned}


$$

Find the solution to the initial value problem above.

**

#### Explanation

Writing our system in matrix form, we get

$$


[\begin{aligned}0 & 7 \\ 7 & 0\end{aligned}]


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ So, the matrix of the system is $[\begin{aligned}0 & 7 \\ 7 & 0\end{aligned}]$

Given the system $\mathbf{x}'(t) = A \mathbf{x}(t),$ where $A$ is a constant square matrix, the general solution of the system can be written as

$$


\mathbf{x}(t) = \Phi(t) \, \mathbf{c},


$$

where $\Phi(t)$ is a fundamental matrix of the system, and $\mathbf{c}$ is a constant vector.

So, we can write our general solution as

$$


\mathbf{x}(t) = \Phi_0(t) \mathbf{c} =e^{At} \, \mathbf{c},


$$

where $\Phi_0(t) = e^{At}$ is the standard fundamental matrix of the system. Substituting $t = t_0,$ we have

$$


\mathbf{x}(t_0) = e^{At_0} \, \mathbf{c},


$$

and since $e^{At}$ is invertible for all $t,$ we have

$$


\mathbf{c} = e^{-At_0} \, \mathbf{x}(t_0).


$$

Plugging the above back into our expression for $\mathbf{x}(t),$ we get

$$


\begin{aligned}𝐱(𝑡) & =𝑒^{𝐴𝑡}\,𝑒^{−𝐴𝑡_{0}}\,𝐱(𝑡_{0}) \\ & =𝑒^{𝐴(𝑡−𝑡_{0})}\,𝐱(𝑡_{0}).\end{aligned}


$$

Therefore, the solution is

$$


\begin{aligned}𝐱(𝑡) & =𝑒^{𝐴(𝑡−1)}\,𝐱(1) \\ & =[\begin{matrix}cosh⁡(7(𝑡−1)) & sinh⁡(7(𝑡−1)) \\ sinh⁡(7(𝑡−1)) & cosh⁡(7(𝑡−1))\end{matrix}][\begin{matrix}0 \\ 3\end{matrix}] \\ & =[\begin{matrix}3sinh⁡(7(𝑡−1)) \\ 3cosh⁡(7(𝑡−1))\end{matrix}].\end{aligned}


$$

### Reminder: Properties of Matrix Exponentials

Before proceeding with the next example, let's recall some important properties of matrix exponentials:

1. *Law of Exponents:* If $A$ is a constant square matrix, then

2. *Inverse:* For any $t,$ the matrix $e^{At}$ is invertible and

3. *Identity:* For any square matrix $A,$

4. *Product of exponentials:* If $A$ and $B$ commute (i.e., $AB = BA$), then **Watch out!** In general, this identity is *not true* unless $A$ and $B$ commute.

Let's see how these properties can be used in practice.

### Example: Proving the Matrix Exponential Formula for IVP Solution: Homogeneous Systems

#### Question

Consider the homogeneous system $\mathbf{x}'(t)=A\mathbf{x}(t),$ where $A$ is a constant square matrix. You're given that the standard fundamental matrix $\Phi_0(t)$ is the unique solution to the initial value problem

$$


\Phi_0'(t) = A\Phi_0(t), \qquad \Phi_0(0) = I_n.


$$

A derivation of the formula for the solution $\mathbf{x}(t)$ passing through $\mathbf{x}(t_0)$ is presented below.

$\text{L1}{:}\;$ Let $\Phi_0(t)=e^{At}$

$\text{L2}{:}\;$ $\mathbf{x}(t)=\Phi_0(t)\,\mathbf{c}$ for some constant vector $\mathbf{c}$

$\text{L3}{:}\;$ $\mathbf{x}(t)=e^{At}\,\mathbf{c}$

$\text{L4}{:}\;$ $\mathbf{x}(t_0)=e^{A t_0} \, \mathbf{c}$

$\text{L5}{:}\;$ $(e^{A t_0})^{-1} \mathbf{x}(t_0)=(e^{At_0})^{-1} e^{A t_0} \, \mathbf{c}$

$\text{L6}{:}\;$ $\mathbf{c} = e^{-A t_0} \mathbf{x}(t_0) \,$

$\text{L7}{:}\;$ $\mathbf{x}(t) = e^{At} e^{-At_0} \mathbf{x}(t_0) \,$

$\text{L8}{:}\;$ $\mathbf{x}(t) = e^{At - At_0} \mathbf{x}(t_0) \,$

$\text{L9}{:}\;$ $\mathbf{x}(t) = e^{A(t-t_0)} \mathbf{x}(t_0) \,$

Fill in the blanks to justify each step of the following reasoning.

$\qquad$ Line $\text{L5}$ follows from $\text{L4}$ by $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$

$\qquad$ The property of the matrix exponential used in $\text{L8}$ is $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$

$\qquad$ Line $\text{L9}$ follows from $\text{L8}$ by the fact that $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$

#### Explanation

Let's justify each of the selected steps.

- We first consider lines $\text{L4}$ and $\text{L5}.$ Starting from $\text{L4},$ we multiply both sides on the left by $(e^{At_0})^{-1}$ to get which is line $\text{L5}.$ Therefore, $\text{L5}$ follows from $\text{L4}$ by $(𝑒^{𝐴𝑡_{0}})^{−1}$

- Next, we justify the step $\text{L7}$ to $\text{L8}.$ Since $At$ and $-At_0$ commute, we may combine exponentials: Substituting this into line $\text{L7}$ produces line $\text{L8}.$ Hence, the property of the matrix exponential used in $\text{L8}$ is $𝑋$

- Finally, we consider lines $\text{L8}$ and $\text{L9}.$ Starting from $\text{L8},$ we rewrite the exponent using the algebraic identity $At-At_0=A(t-t_0)$ to get which is line $\text{L9}.$ Thus, $\text{L9}$ follows from $\text{L8}$ by the fact that $\boxed{At-At_0=A(t-t_0)\text{for any}t\text{and}t_0}.$
