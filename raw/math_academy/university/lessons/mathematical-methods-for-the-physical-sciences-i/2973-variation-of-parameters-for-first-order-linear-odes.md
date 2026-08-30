# Variation of Parameters for First-Order Linear ODEs

Source: https://www.mathacademy.com/topics/2973?courseId=154
Topic ID: 2973

## Prerequisites

- [The Hyperbolic Functions](../calculus-i/967-the-hyperbolic-functions.md)
- [Solving First-Order Linear ODEs With Exponential Forcing](./6679-solving-first-order-linear-odes-with-exponential-forcing.md)
- [Solving First-Order Linear ODEs With Sinusoidal Forcing](./6680-solving-first-order-linear-odes-with-sinusoidal-forcing.md)

## Lesson

### Introduction

In this topic, we’ll learn another method for solving inhomogeneous linear ODEs: **variation of parameters** (VOP).

Recall that a *first-order linear ODE* can be written in the standard form

$$


\dfrac{\textrm d y}{\textrm d x} + P(x)y = Q(x).


$$

To solve it, we look for a solution of the form

$$


y(x) = y_c(x) + y_p(x),


$$

where $y_c(x)$ is the *complementary solution* (solution to the homogeneous equation) and $y_p(x)$ is a *particular solution* (any one solution to the original equation).

In variation of parameters, we start with the homogeneous solution and then allow its constant to vary with $x.$

- **Step 1:** Solve the corresponding homogeneous equation Its general solution has the form where $C$ is an arbitrary constant.

- **Step 2:** Guess the form of a particular solution by allowing the constant $C$ to depend on $x.$ We now choose an **ansatz**, meaning an *assumed form* for a solution. In VOP, we assume where $u(x)$ is an unknown function. Intuitively, $y_p(x)$ has the same form as the homogeneous solution $y_c(x),$ but its amplitude changes with $x.$

- **Step 3:** Substitute $y_p(x)$ into the original ODE. Using the product rule, we find the derivative: When substituted into $y' + Py = Q,$ the second term above cancels with $Py_p,$ leaving This allows us to solve for $u'(x),$ integrate to find $u(x),$ and finally recover $y_p(x).$

On the next slide, we'll construct a suitable VOP ansatz for a particular first-order equation.

### Example: Finding a Suitable Variation of Parameters Ansatz

#### Question

Consider the first-order linear ODE

$$


\dfrac{\textrm d y}{\textrm d x} - 6y = (3x+1)\sin(x).


$$

According to the method of variation of parameters, what is a suitable ansatz for the particular solution $y_p(x)?$

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c,$ we solve the corresponding homogeneous equation, given by

$$


y_c' - 6y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{6x}


$$

where $A$ is an arbitrary constant.

The method of variation of parameters constructs a particular solution by varying the constant in the homogeneous solution. So, to find a suitable $y_p,$ we set $A = u(x)$ in the complementary solution, as given by the following ansatz:

$$


y_p(x) = u(x)e^{6x}


$$

Intuitively, this form of $y_p$ tracks the homogeneous solution but with a varying amplitude.

### Applying Variation of Parameters

Now, consider the first-order linear ODE

$$


\dfrac{\textrm d y}{\textrm d x} + 3y = e^{2x}.


$$

Let's solve this equation using the method of variation of parameters (VOP).

To find the general solution of an inhomogeneous first-order linear equation, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c,$ we solve the corresponding homogeneous equation, given by

$$


y_c' + 3y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{-3x}


$$

where $A$ is an arbitrary constant.

The method of variation of parameters constructs a particular solution by varying the constant in the homogeneous solution. So, to find a suitable $y_p,$ we set $A = u(x)$ in the complementary solution, as given by the following ansatz:

$$


y_p(x) = u(x)e^{-3x}


$$

Intuitively, this form of $y_p$ tracks the homogeneous solution but with a varying amplitude.

To find $u,$ we substitute our ansatz into the equation, apply the product rule to the derivative term, and simplify to isolate $u'{:}$

$$


\begin{aligned}(𝑢𝑒^{−3𝑥})^{′}+3(𝑢𝑒^{−3𝑥}) & =𝑒^{2𝑥} \\ 𝑢^{′}𝑒^{−3𝑥}−3𝑢𝑒^{−3𝑥}+3𝑢𝑒^{−3𝑥} & =𝑒^{2𝑥} \\ 𝑢^{′}𝑒^{−3𝑥}−3𝑢𝑒^{−3𝑥}+3𝑢𝑒^{−3𝑥} & =𝑒^{2𝑥} \\ 𝑢^{′}𝑒^{−3𝑥} & =𝑒^{2𝑥} \\ 𝑢^{′} & =𝑒^{5𝑥}\end{aligned}


$$

Integrating both sides with respect to $x$ (omitting the arbitrary constant), we have

$$


\begin{aligned}𝑢^{′} & =𝑒^{5𝑥} \\ ∫𝑢^{′}\,d𝑥 & =∫𝑒^{5𝑥}\,d𝑥 \\ 𝑢 & =\frac{1}{5}𝑒^{5𝑥}.\end{aligned}


$$

Finally, since $y_p = u(x)e^{-3x},$ we have

$$


\begin{aligned}𝑦_{𝑝} & =𝑢(𝑥)𝑒^{−3𝑥} \\ & =\frac{1}{5}𝑒^{5𝑥}⋅𝑒^{−3𝑥} \\ & =\frac{1}{5}𝑒^{2𝑥}.\end{aligned}


$$

Finally, the general solution is the sum of $y_c$ and $y_p{:}$

$$


y = y_c + y_p = Ae^{-3x} + \dfrac15 e^{2x}


$$

### Example: Solving First-Order Linear ODEs Using Variation of Parameters

#### Question

Consider the first-order linear ODE

$$


\dfrac{\textrm d y}{\textrm d x} - 5y = \cos 2x.


$$

We wish to solve this equation using the method of variation of parameters (VOP).

Select the correct options below.

$\qquad$ According to VOP, we assume a particular solution of the form $𝐴𝐴𝐴𝐴𝐴$.

$\qquad$ Solving for $u,$ we have $u(x) =$ $𝐴𝐴𝐴𝐴𝐴$.

$\qquad$ Therefore, the particular solution is $y_p(x) =$ $𝐴𝐴𝐴𝐴𝐴$.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c,$ we solve the corresponding homogeneous equation, given by

$$


y_c' - 5y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{5x}


$$

where $A$ is an arbitrary constant.

The method of variation of parameters constructs a particular solution by varying the constant in the homogeneous solution. So, to find a suitable $y_p,$ we set $A = u(x)$ in the complementary solution, as given by the following ansatz:

$$


y_p(x) = u(x)e^{5x}


$$

Intuitively, this form of $y_p$ tracks the homogeneous solution but with a varying amplitude.

To find $u,$ we substitute our ansatz into the equation, apply the product rule to the derivative term, and simplify to isolate $u'{:}$

$$


\begin{aligned}(𝑢𝑒^{5𝑥})^{′}−5(𝑢𝑒^{5𝑥}) & =cos⁡2𝑥 \\ 𝑢^{′}𝑒^{5𝑥}+5𝑢𝑒^{5𝑥}−5𝑢𝑒^{5𝑥} & =cos⁡2𝑥 \\ 𝑢^{′}𝑒^{5𝑥}+5𝑢𝑒^{5𝑥}−5𝑢𝑒^{5𝑥} & =cos⁡2𝑥 \\ 𝑢^{′}𝑒^{5𝑥} & =cos⁡2𝑥 \\ 𝑢^{′} & =𝑒^{−5𝑥}cos⁡2𝑥\end{aligned}


$$

Integrating both sides with respect to $x$ (omitting the arbitrary constant), we have

$$


\begin{aligned}𝑢^{′} & =𝑒^{−5𝑥}cos⁡2𝑥 \\ ∫𝑢^{′}\,d𝑥 & =∫𝑒^{−5𝑥}cos⁡2𝑥\,d𝑥 \\ 𝑢 & =∫𝑒^{−5𝑥}cos⁡2𝑥\,d𝑥.\end{aligned}


$$

Finally, since $y_p = u(x)e^{5x},$ we have

$$


\begin{aligned}𝑦_{𝑝} & =𝑢(𝑥)𝑒^{5𝑥} \\ & =∫𝑒^{−5𝑥}cos⁡2𝑥\,d𝑥⋅𝑒^{5𝑥} \\ & =𝑒^{5𝑥}∫𝑒^{−5𝑥}cos⁡2𝑥\,d𝑥.\end{aligned}


$$

### Cases When the Forcing Term is Part of the Complementary Solution

Next, consider the first-order linear ODE

$$


\dfrac{\textrm d y}{\textrm d x} - 5y = e^{5x}.


$$

We wish to solve this equation using the method of variation of parameters (VOP).

To find the general solution of an inhomogeneous first-order linear equation, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c,$ we solve the corresponding homogeneous equation, given by

$$


y_c' - 5y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{5x}


$$

where $A$ is an arbitrary constant. We call this a **resonant case** because the forcing term is proportional to the homogeneous solution $e^{5x}.$

The method of variation of parameters constructs a particular solution by varying the constant in the homogeneous solution. So, to find a suitable $y_p,$ we set $A = u(x)$ in the complementary solution, as given by the following ansatz:

$$


y_p(x) = u(x)e^{5x}


$$

Intuitively, this form of $y_p$ tracks the homogeneous solution but with a varying amplitude.

**Watch out!** Even in resonant cases, the VOP ansatz is unchanged. The only difference is that the resulting equation for $u'$ becomes especially simple. Let's see how.

To find $u,$ we substitute our ansatz into the equation, apply the product rule to the derivative term, and simplify to isolate $u'{:}$

$$


\begin{aligned}(𝑢𝑒^{5𝑥})^{′}−5(𝑢𝑒^{5𝑥}) & =𝑒^{5𝑥} \\ 𝑢^{′}𝑒^{5𝑥}+5𝑢𝑒^{5𝑥}−5𝑢𝑒^{5𝑥} & =𝑒^{5𝑥} \\ 𝑢^{′}𝑒^{5𝑥}+5𝑢𝑒^{5𝑥}−5𝑢𝑒^{5𝑥} & =𝑒^{5𝑥} \\ 𝑢^{′}𝑒^{5𝑥} & =𝑒^{5𝑥} \\ 𝑢^{′} & =1\end{aligned}


$$

Integrating both sides with respect to $x$ (omitting the arbitrary constant), we have

$$


\begin{aligned}𝑢^{′} & =1 \\ ∫𝑢^{′}\,d𝑥 & =∫\,d𝑥 \\ 𝑢 & =𝑥.\end{aligned}


$$

**Note:** We omit the constant of integration when solving for $u(x),$ since adding a constant to $u(x)$ would just add a multiple of the homogeneous solution.

Finally, since $y_p = u(x)e^{5x},$ we have

$$


\begin{aligned}𝑦_{𝑝} & =𝑢(𝑥)𝑒^{5𝑥} \\ & =𝑥𝑒^{5𝑥}.\end{aligned}


$$

Finally, we identify $y_p$ and sum the solutions to find the general solution:

$$


\begin{aligned}𝑦 & =𝑦_{𝑐}+𝑦_{𝑝}=𝐴𝑒^{5𝑥}+𝑥𝑒^{5𝑥}.\end{aligned}


$$

### Example: Solving First-Order Linear ODEs Using VOP When the Forcing Term is Part of the Complementary Solution

#### Question

Consider the first-order linear ODE

$$


\dfrac{\textrm d y}{\textrm d x} - 3y = 12\sinh 3x.


$$

We wish to solve this equation using the method of variation of parameters (VOP).

Select the correct options below.

$\qquad$ According to VOP, we assume a particular solution of the form $𝐴𝐴𝐴𝐴𝐴$.

$\qquad$ Solving for $u,$ we have $u(x) =$ $𝐴𝐴𝐴𝐴𝐴$.

$\qquad$ Therefore, the particular solution is $y_p(x) =$ $𝐴𝐴𝐴𝐴𝐴$.

#### Explanation

To find the general solution of an inhomogeneous first-order linear equation, we must find the sum of the complementary and particular solutions.

To find the complementary solution $y_c,$ we solve the corresponding homogeneous equation, given by

$$


y_c' - 3y_c = 0.


$$

Solving this equation, we find that the complementary solution is

$$


y_c = Ae^{3x}


$$

where $A$ is an arbitrary constant.

The method of variation of parameters constructs a particular solution by varying the constant in the homogeneous solution. So, to find a suitable $y_p,$ we set $A = u(x)$ in the complementary solution, as given by the following ansatz:

$$


y_p(x) = u(x)e^{3x}


$$

Intuitively, this form of $y_p$ tracks the homogeneous solution but with a varying amplitude.

To find $u,$ we substitute our ansatz into the equation, apply the product rule to the derivative term, and simplify to isolate $u'{:}$

$$


\begin{aligned}(𝑢𝑒^{3𝑥})^{′}−3(𝑢𝑒^{3𝑥}) & =12sinh⁡3𝑥 \\ 𝑢^{′}𝑒^{3𝑥}+3𝑢𝑒^{3𝑥}−3𝑢𝑒^{3𝑥} & =12sinh⁡3𝑥 \\ 𝑢^{′}𝑒^{3𝑥}+3𝑢𝑒^{3𝑥}−3𝑢𝑒^{3𝑥} & =12sinh⁡3𝑥 \\ 𝑢^{′}𝑒^{3𝑥} & =12sinh⁡3𝑥 \\ 𝑢^{′} & =12𝑒^{−3𝑥}sinh⁡3𝑥\end{aligned}


$$

Using the fact that

$$


\sinh 3x = \dfrac{e^{3x} - e^{-3x}}{2}


$$

our equation for $u$ becomes

$$


\begin{aligned}𝑢^{′} & =12𝑒^{−3𝑥}sinh⁡3𝑥 \\ & =12𝑒^{−3𝑥}(\frac{𝑒^{3𝑥}−𝑒^{−3𝑥}}{2}) \\ & =6𝑒^{−3𝑥}(𝑒^{3𝑥}−𝑒^{−3𝑥}) \\ & =6−6𝑒^{−6𝑥}.\end{aligned}


$$

Integrating both sides with respect to $x$ (omitting the arbitrary constant), we have

$$


\begin{aligned}𝑢^{′} & =6−6𝑒^{−6𝑥} \\ ∫𝑢^{′}\,d𝑥 & =∫6−6𝑒^{−6𝑥}\,d𝑥 \\ 𝑢 & =6𝑥+𝑒^{−6𝑥}.\end{aligned}


$$

Finally, since $y_p = u(x)e^{3x},$ we have

$$


\begin{aligned}𝑦_{𝑝} & =𝑢(𝑥)𝑒^{3𝑥} \\ & =6𝑥𝑒^{3𝑥}+𝑒^{−3𝑥}.\end{aligned}


$$
