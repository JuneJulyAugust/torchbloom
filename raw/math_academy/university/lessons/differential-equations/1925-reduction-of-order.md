# Reduction of Order

Source: https://www.mathacademy.com/topics/1925?courseId=61
Topic ID: 1925

## Prerequisites

- [Solving First-Order ODEs Using Separation of Variables](./466-solving-first-order-odes-using-separation-of-variables.md)
- [Introduction to Second-Order Linear ODEs](./2548-introduction-to-second-order-linear-odes.md)

## Lesson

### Introduction

If we know one solution to a second-order homogeneous linear differential equation, we can use the **reduction of order method** to find a second solution to the equation.

It works like this: if we know that some function $y_1(t)$ is a solution, then we let $y_2(t) = u(t) y_1(t)$ for some unknown function $u(t),$ and we write down a differential equation in terms of $u.$ Solving this equation, and then computing $y_2,$ gives us our second solution.

For example, suppose we're given that $y_1(t) = \sin{4t}$ is a solution to the equation

$$


y'' + 16y = 0.


$$

Let's use the reduction of order method to find a second solution $y_2(t).$

According to the reduction of order method, we let $y_{2} = u(t)\sin{4t}$ for some unknown function $u(t).$ Then, we write the differential equation in terms of $u.$ To do that, we first differentiate with respect to $t\mathbin{:}$

$$


\begin{aligned}𝑦_{2} & =𝑢sin⁡4𝑡 \\ 𝑦_{′2} & =𝑢^{′}sin⁡4𝑡+4𝑢cos⁡4𝑡 \\ 𝑦_{″2} & =𝑢^{″}sin⁡4𝑡+8𝑢^{′}cos⁡4𝑡−16𝑢sin⁡4𝑡\end{aligned}


$$

Substituting the above into the differential equation gives

$$


\begin{aligned}𝑦^{″}+16𝑦 & =0 \\ (𝑢^{″}sin⁡4𝑡+8𝑢^{′}cos⁡4𝑡−16𝑢sin⁡4𝑡)+16𝑢sin⁡4𝑡 & =0 \\ 𝑢^{″}sin⁡4𝑡+8𝑢^{′}cos⁡4𝑡 & =0 \\ 𝑢^{″} & =−8𝑢^{′}cot⁡4𝑡.\end{aligned}


$$

Let $w = u'.$ Then our equation becomes a first-order equation,

$$


w' = -8w\cot{4t}.


$$

This is a separable equation that has the solution

$$


w = c_1 \csc^2{4t}.


$$

Now, since $w = u',$ we have

$$


u' = c_1 \csc^2{4t} \quad\Longrightarrow\quad u = -\dfrac{c_1}{4}\cot{4t} + c_2.


$$

Therefore, our expression for $y_2(t) = u \sin{4t}$ becomes

$$


y_2(t) = \sin{4t}\left( -\dfrac{c_1}{4}\cot{4t} + c_2 \right).


$$

We can choose any values for $c_1$ and $c_2$ to yield a second solution. For example, if we set $c_1 = -4$ and $c_2 = 0,$ then we get

$$


y_2(t) = \sin{4t}\left( \cot{4t} \right) = \cos{4t}.


$$

When selecting our constants $c_1$ and $c_2,$ we should try to get a solution that is "different" from the first. We will define precisely what we mean by "different" soon, but loosely speaking we should aim for a $y_2(x)$ that satisfies the following conditions:

- None of the terms is a constant multiple of the first solution (here, we accomplished this by choosing $c_2=0$).

- The remaining terms are as simple as possible (here, we accomplished this by choosing $c_1=-4$).

### Example: Finding the Differential Equation Satisfied by the Reduction of Order Function

#### Question

The function $y_1(x) = e^{3x}$ is a solution to the equation $y'' - 6y' + 9y = 0.$ If $y_{2} = u(x) y_1(x)$ is a second solution of the equation, then which of the following equations must be satisfied by $u(x)?$

1. $u''=0$

2. $e^{3x}u'' + u=0$

3. $u''-u=0$

#### Explanation

We're given that

$$


\begin{aligned}𝑦_{2}(𝑥) & =𝑢(𝑥)𝑦_{1}(𝑥) \\ & =𝑢(𝑥)𝑒^{3𝑥}.\end{aligned}


$$

Differentiating the above with respect to $x$ gives

$$


\begin{aligned}𝑦_{2} & =𝑢𝑒^{3𝑥} \\ 𝑦_{′2} & =𝑢^{′}𝑒^{3𝑥}+3𝑢𝑒^{3𝑥} \\ 𝑦_{″2} & =𝑢^{″}𝑒^{3𝑥}+6𝑢^{′}𝑒^{3𝑥}+9𝑢𝑒^{3𝑥}.\end{aligned}


$$

Substituting the above into the differential equation gives

$$


\begin{aligned}𝑦^{″}−6𝑦^{′}+9𝑦 & =0 \\ (𝑢^{″}𝑒^{3𝑥}+6𝑢^{′}𝑒^{3𝑥}+9𝑢𝑒^{3𝑥})−6(𝑢^{′}𝑒^{3𝑥}+3𝑢𝑒^{3𝑥})+9𝑢𝑒^{3𝑥} & =0 \\ 𝑒^{3𝑥}(𝑢^{″}+6𝑢^{′}+9𝑢−6𝑢^{′}−18𝑢+9𝑢) & =0 \\ 𝑒^{3𝑥}𝑢^{″} & =0.\end{aligned}


$$

Since $e^{3x} \neq 0,$ we must have

$$


u'' = 0.


$$

Therefore, the correct answer is "I only".

### Example: Finding a Second Solution to a Differential Equation Using Reduction of Order

#### Question

Given that $y_1(t) = e^{-t}$ is a solution to the equation $y'' - 3y ' - 4y = 0,$ use reduction of order to find a second solution $y_2(t)$ to the equation.

#### Explanation

According to the reduction of order method, we let $y_{2} = u(t)e^{-t}.$

Differentiating the above with respect to $t$ gives

$$


\begin{aligned}𝑦_{2} & =𝑢𝑒^{−𝑡} \\ 𝑦_{′2} & =𝑢^{′}𝑒^{−𝑡}−𝑢𝑒^{−𝑡} \\ 𝑦_{″2} & =𝑢^{″}𝑒^{−𝑡}−2𝑢^{′}𝑒^{−𝑡}+𝑢𝑒^{−𝑡}.\end{aligned}


$$

Substituting the above into the differential equation gives

$$


\begin{aligned}𝑦^{″}−3𝑦^{′}−4𝑦 & =0 \\ (𝑢^{″}𝑒^{−𝑡}−2𝑢^{′}𝑒^{−𝑡}+𝑢𝑒^{−𝑡})−3(𝑢^{′}𝑒^{−𝑡}−𝑢𝑒^{−𝑡})−4𝑢𝑒^{−𝑡} & =0 \\ 𝑢^{″}𝑒^{−𝑡}−5𝑢^{′}𝑒^{−𝑡} & =0 \\ 𝑒^{−𝑡}(𝑢^{″}−5𝑢^{′}) & =0.\end{aligned}


$$

Since $e^t \neq 0,$ we must have

$$


u'' - 5u' = 0.


$$

Let $w = u'.$ Then our equation becomes a first-order equation,

$$


w' - 5w=0.


$$

This is a separable equation that has the solution

$$


w = c_1 e^{5t}.


$$

Now, since since $w = u',$ we have

$$


u' = c_1e^{5t} \quad\Longrightarrow\quad u = \dfrac{c_1}{5} e^{5t} + c_2.


$$

Therefore, our expression for $y_2(t) = u e^{-t}$ becomes

$$


y_2(t) = e^{-t}\left( \dfrac{c_1}{5} e^{5t} + c_2 \right).


$$

We can choose any values for $c_1$ and $c_2$ to yield a second solution. For example, if we set $c_1 = 5$ and $c_2 = 0,$ we get

$$


y_2(t) = e^{-t} \cdot e^{5t} = e^{4t}.


$$
