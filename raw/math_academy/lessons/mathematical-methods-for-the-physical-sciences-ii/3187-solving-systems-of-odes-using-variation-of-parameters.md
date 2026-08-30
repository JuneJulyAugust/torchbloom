# Solving Systems of ODEs Using Variation of Parameters

Source: https://www.mathacademy.com/topics/3187?courseId=155
Topic ID: 3187

## Prerequisites

- [Introduction to Integration by Parts](../ap-calculus-bc/317-introduction-to-integration-by-parts.md)
- [Variation of Parameters for First-Order Linear ODEs](../differential-equations/2973-variation-of-parameters-for-first-order-linear-odes.md)
- [Solving Inhomogeneous Systems of ODEs Using Matrix Methods](./6691-solving-inhomogeneous-systems-of-odes-using-matrix-methods.md)

## Lesson

### Introduction

Consider the system of ordinary differential equations

$$


\mathbf{x}'(t) = A \mathbf{x}(t) + \mathbf{f}(t)


$$

where $A$ is a constant square matrix and $\mathbf{f}(t)$ is a forcing vector.

In this lesson, we'll derive the formula for the particular solution of the above system using the method of variation of parameters.

Recall that the general solution of the corresponding homogeneous system is given by

$$


\mathbf{x}_c(t) = \Phi \, \mathbf{c}


$$

where $\mathbf{c}$ is a vector of constants, and $\Phi$ is the fundamental matrix.

As usual, for the method of variation of parameters, we'll look for a particular solution of our inhomogeneous system by varying the constant parameters, i.e., in the form

$$


\mathbf{x}_p(t) = \Phi \, \mathbf{u}(t)


$$

where $\mathbf{u}(t)$ is a column vector of functions to be determined.

Differentiating $\mathbf{x}_p(t)$ with respect to $t,$ we get

$$


\begin{aligned}𝐱_{′𝑝}^{}(𝑡) & =(Φ\,𝐮(𝑡))^{′} \\ & =Φ𝐮^{′}(𝑡)+Φ^{′}𝐮(𝑡).\end{aligned}


$$

Now, since $\mathbf{x}_p(t)$ is a solution, substituting it back into the initial system gives a true equation:

$$


\begin{aligned}𝐱^{′}(𝑡) & =𝐴𝐱(𝑡)+𝐟(𝑡) \\ Φ𝐮^{′}(𝑡)+Φ^{′}𝐮(𝑡) & =𝐴Φ𝐮(𝑡)+𝐟(𝑡)\end{aligned}


$$

Next, since $\Phi$ is a fundamental matrix, $\Phi' = A \Phi.$ Substituting this into the equation simplifies it to the following:

$$


\begin{aligned}Φ𝐮^{′}(𝑡)+𝐴Φ𝐮(𝑡) & =𝐴Φ𝐮(𝑡)+𝐟(𝑡) \\ Φ𝐮^{′}(𝑡) & =𝐟(𝑡)\end{aligned}


$$

Then, since $\Phi$ is invertible, we can pre-multiply both sides by $\Phi^{-1}{:}$

$$


\begin{aligned}Φ^{−1}⋅Φ𝐮^{′}(𝑡) & =Φ^{−1}⋅𝐟(𝑡) \\ 𝐮^{′}(𝑡) & =Φ^{−1}(𝑡)𝐟(𝑡)\end{aligned}


$$

Finally, we integrate both sides of the final equations (ignoring the constant term):

$$


\begin{aligned}∫𝐮^{′}(𝑡)\,d𝑡 & =∫Φ^{−1}𝐟(𝑡)\,d𝑡 \\ 𝐮(𝑡) & =∫Φ^{−1}𝐟(𝑡)\,d𝑡\end{aligned}


$$

Therefore, our particular solution is

$$


\mathbf{x}_p(t) = \Phi \displaystyle\int \Phi^{-1}\mathbf{f}(t) \, \text{d}t.


$$

### Example: Constructing the Formulas for Variation of Parameters

#### Question

Consider the following system of differential equations:

$$


\mathbf{x}'(t) = A \mathbf{x}(t) + \mathbf{f}(t)


$$

Using the method of variation of parameters, we wish to find a particular solution in the form $\mathbf{x}_p(t) = \Phi \mathbf{u}(t),$ where $\Phi$ is a fundamental matrix for the corresponding homogeneous system and $\mathbf{u}(t)$ is a column vector of functions to be determined. A derivation of the formula for $\mathbf x_p(t)$ is given below.

$\textrm{L1}{:}\:$ $\mathbf{x}_p(t) = \Phi \mathbf{u}(t)$

$\textrm{L2}{:}\:$ $\mathbf{x}'_p(t) = \Phi \mathbf{u}'(t) + \Phi' \mathbf{u}(t)$

$\textrm{L3}{:}\:$ $\Phi \mathbf{u}'(t) + \Phi' \mathbf{u}(t) = A \Phi \mathbf{u}(t) + \mathbf{f}(t)$

$\textrm{L4}{:}\:$ $\Phi' = A \Phi$

$\textrm{L5}{:}\:$ $\Phi \mathbf{u}'(t) = \mathbf{f}(t)$

$\textrm{L6}{:}\:$ $\mathbf{u}'(t) = \Phi^{-1}(t) \mathbf{f}(t)$

$\textrm{L7}{:}\:$ $\displaystyle\mathbf{u}(t) = \int \Phi^{-1} \mathbf{f}(t) \, \text{d}t$

$\textrm{L8}{:}\:$ $\displaystyle\mathbf{x}_p(t) = \Phi \int \Phi^{-1}\mathbf{f}(t) \, \text{d}t$

Fill in the blanks with the correct reasons to justify each step of the reasoning.

$\quad$ Line $\textrm{L4}$ follows from the fact that $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$ matrix.

$\quad$ Line $\textrm{L6}$ follows from line $\textrm{L5}$ by $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$ both sides of the equation.

$\quad$ Line $\textrm{L8}$ is obtained by substituting $\textrm{L7}$ into $𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴$

#### Explanation

Let's examine each statement in turn.

- We first consider line $\textrm{L4}.$ Since $\Phi$ is a fundamental matrix, its columns are solutions to the homogeneous system $\mathbf{x}'(t) =A\mathbf{x}(t),$ i.e., by substituting any column $\mathbf{c}(t)$ of $\Phi$ into the homogeneous system, we get where $\mathbf{c}'(t)$ is the corresponding column of derivatives in $\Phi.$ As a result, this means that $\Phi' = A \Phi.$ Therefore, $\textrm{L4}$ follows from the fact that $Φ$ matrix.

- Next, we consider lines $\textrm{L5}$ and $\textrm{L6}.$ Since $\Phi$ is a fundamental matrix, its columns are linearly independent. So, $\Phi$ is invertible. Therefore, $\textrm{L6}$ follows from $\textrm{L5}$ by $Φ^{−1}$ both sides of the equation:

- Finally, we consider lines $\textrm{L1},$ $\textrm{L7},$ and $\textrm{L8}.$ Substituting from $\textrm{L7}$ into $\textrm{L1},$ we get Therefore, $\textrm{L8}$ is obtained by substituting $\textrm{L7}$ into $L1$

### Example: Finding the Particular Solution of an Inhomogeneous System of Linear ODEs

#### Question

$$


[\begin{aligned}−4 & 0 \\ 7 & 3\end{aligned}]


$$

Consider the system of differential equations and the fundamental matrix of the corresponding homogeneous system above. Using the method of variation of parameters, compute $\Phi^{-1} \, \mathbf{f}(t)$ and the particular solution $\mathbf{x}_p(t)$ of the system.

#### Explanation

We'll look for a particular solution in the form

$$


\mathbf{x}_p(t) = \Phi \, \mathbf{u}(t)


$$

where $\Phi$ is a fundamental matrix for the corresponding homogeneous system, $\mathbf{f}(t)$ is the forcing column vector and

$$


\mathbf{u}(t) = \int \Phi^{-1} \, \mathbf{f}(t) \, \text{d}t.


$$

In our case,

$$


[\begin{aligned}0 & 2𝑒^{−4𝑡} \\ 𝑒^{3𝑡} & −2𝑒^{−4𝑡}\end{aligned}]


$$

Since $\Phi$ is a fundamental matrix, it must be invertible. Using the formula for the inverse of a $2 \times 2$ matrix, we get the following:

$$


\begin{aligned}Φ^{−1} & =\frac{1}{0⋅(−2𝑒^{−4𝑡})−2𝑒^{−4𝑡}⋅𝑒^{3𝑡}}[\begin{aligned}−2𝑒^{−4𝑡} & −2𝑒^{−4𝑡} \\ −𝑒^{3𝑡} & 0\end{aligned}] \\ & =−\frac{𝑒^{𝑡}}{2}[\begin{aligned}−2𝑒^{−4𝑡} & −2𝑒^{−4𝑡} \\ −𝑒^{3𝑡} & 0\end{aligned}] \\ & =\begin{aligned}𝑒^{−3𝑡} & 𝑒^{−3𝑡} \\ \frac{1}{2}𝑒^{4𝑡} & 0\end{aligned} \\ Φ^{−1}\,𝐟(𝑡) & =\begin{aligned}𝑒^{−3𝑡} & 𝑒^{−3𝑡} \\ \frac{1}{2}𝑒^{4𝑡} & 0\end{aligned}[\begin{aligned}𝑒^{𝑡} \\ 2𝑒^{𝑡}\end{aligned}] \\ & =\begin{aligned}3𝑒^{−2𝑡} \\ \frac{1}{2}𝑒^{5𝑡}\end{aligned}\end{aligned}


$$

Now, using our formula for $\mathbf{u}(t),$ we obtain

$$


\begin{aligned}𝐮(𝑡) & =∫Φ^{−1}\,𝐟(𝑡)\,d𝑡 \\ & =∫\begin{aligned}3𝑒^{−2𝑡} \\ \frac{1}{2}𝑒^{5𝑡}\end{aligned}\,d𝑡 \\ & =\begin{aligned}∫3𝑒^{−2𝑡}\,d𝑡 \\ ∫\frac{1}{2}𝑒^{5𝑡}\,d𝑡\end{aligned} \\ & =\begin{aligned}−\frac{3}{2}𝑒^{−2𝑡} \\ \frac{1}{10}𝑒^{5𝑡}\end{aligned}.\end{aligned}


$$

Therefore, our particular solution is

$$


\begin{aligned}𝐱_{𝑝}(𝑡) & =Φ\,𝐮(𝑡) \\ & =[\begin{aligned}0 & 2𝑒^{−4𝑡} \\ 𝑒^{3𝑡} & −2𝑒^{−4𝑡}\end{aligned}]\begin{aligned}−\frac{3}{2}𝑒^{−2𝑡} \\ \frac{1}{10}𝑒^{5𝑡}\end{aligned} \\ & =\begin{aligned}\frac{1}{5}𝑒^{𝑡} \\ −\frac{17}{10}𝑒^{𝑡}\end{aligned} \\ & =𝑒^{𝑡}\begin{aligned}\frac{1}{5} \\ −\frac{17}{10}\end{aligned}.\end{aligned}


$$

### Example: Solving an Inhomogeneous System of Linear ODEs Using Variation of Parameters

#### Question

$$


[\begin{aligned}−2 & 0 \\ 0 & −4\end{aligned}]


$$

Consider the system of differential equations. Using the method of variation of parameters, the general solution of the equation can be written in the form

#### Explanation

Recall that the general solution of an inhomogeneous system can be written as

$$


\mathbf{x}(t) = \mathbf{x}_c(t) + \mathbf{x}_p(t)


$$

where $\mathbf{x}_c(t)$ is the complementary solution (solution of the corresponding homogeneous system) and $\mathbf{x}_p(t)$ is a particular solution.

Notice that we are given that

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

We'll look for a particular solution in the form

$$


\mathbf{x}_p(t) = \Phi \, \mathbf{u}(t)


$$

where $\Phi$ is a fundamental matrix for the corresponding homogeneous system, $\mathbf{f}(t)$ is the forcing column vector and

$$


\mathbf{u}(t) = \int \Phi^{-1} \, \mathbf{f}(t) \, \text{d}t.


$$

In our case,

$$


[\begin{aligned}𝑒^{−2𝑡} & 0 \\ 0 & 𝑒^{−4𝑡}\end{aligned}]


$$

Since $\Phi$ is a fundamental matrix, it must be invertible. Using the formula for the inverse of a $2 \times 2$ matrix, we get the following:

$$


\begin{aligned}Φ^{−1} & =\frac{1}{𝑒^{−2𝑡}⋅𝑒^{−4𝑡}−0}[\begin{aligned}𝑒^{−4𝑡} & 0 \\ 0 & 𝑒^{−2𝑡}\end{aligned}] \\ & =𝑒^{6𝑡}[\begin{aligned}𝑒^{−4𝑡} & 0 \\ 0 & 𝑒^{−2𝑡}\end{aligned}] \\ & =[\begin{aligned}𝑒^{2𝑡} & 0 \\ 0 & 𝑒^{4𝑡}\end{aligned}]. \\ Φ^{−1}\,𝐟(𝑡) & =[\begin{aligned}𝑒^{2𝑡} & 0 \\ 0 & 𝑒^{4𝑡}\end{aligned}][\begin{aligned}2𝑡 \\ 0\end{aligned}] \\ & =[\begin{aligned}2𝑡𝑒^{2𝑡} \\ 0\end{aligned}].\end{aligned}


$$

Now, using our formula for $\mathbf{u}(t),$ we obtain

$$


\begin{aligned}𝐮(𝑡) & =∫Φ^{−1}\,𝐟(𝑡)\,d𝑡 \\ & =∫[\begin{aligned}2𝑡𝑒^{2𝑡} \\ 0\end{aligned}]\,d𝑡 \\ & =\begin{aligned}∫2𝑡𝑒^{2𝑡}\,d𝑡 \\ ∫0\,d𝑡\end{aligned}.\end{aligned}


$$

Integrating the components by parts, we get the following:

- For the first component, let $u=2t$ and $\text{d}v=e^{2t}\,\text{d}t.$ Then, $\text{d}u=2\,\text{d}t$ and $v=\dfrac{1}{2}e^{2t}.$ So,

- For the second component, the integrand is zero, so the integral is zero.

Therefore, our particular solution is

$$


\begin{aligned}𝐱_{𝑝}(𝑡) & =Φ\,𝐮(𝑡) \\ & =[\begin{aligned}𝑒^{−2𝑡} & 0 \\ 0 & 𝑒^{−4𝑡}\end{aligned}]\begin{aligned}\frac{1}{2}𝑒^{2𝑡}(2𝑡−1) \\ 0\end{aligned} \\ & =\frac{1}{2}[\begin{aligned}2𝑡−1 \\ 0\end{aligned}].\end{aligned}


$$
