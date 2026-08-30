# Expressing Inhomogeneous ODEs as First-Order Systems

Source: https://www.mathacademy.com/topics/3635?courseId=61
Topic ID: 3635

## Prerequisites

- [Expressing Homogeneous ODEs as First-Order Systems](./3186-expressing-homogeneous-odes-as-first-order-systems.md)

## Lesson

### Introduction

Recall, previously, we saw how to express second-order and third-order *homogeneous* ODEs as a system of first-order differential equations. We use the same method for second-order and third-order *inhomogeneous* ODEs.

For instance, consider the third-order inhomogeneous differential equation

$$


y''' + 5y'' - 4y' + t^2y = t+1.


$$

We write this equation as a system of first-order differential equations using the following change of variables:

$$


\begin{aligned}𝑥_{1}(𝑡) & =𝑦 \\ 𝑥_{2}(𝑡) & =𝑦^{′} \\ 𝑥_{3}(𝑡) & =𝑦^{″}\end{aligned}


$$

Differentiating the above equations with respect to $t,$ we get

$$


\begin{aligned}𝑥_{′1}(𝑡) & =𝑦^{′} \\ 𝑥_{′2}(𝑡) & =𝑦^{″} \\ 𝑥_{′3}(𝑡) & =𝑦^{‴}\end{aligned}


$$

which we can rewrite as

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=𝑥_{3} \\ 𝑥_{′3}=𝑦^{‴}.\end{aligned}


$$

At this point, we're almost done. We just need to write the right-hand side of the last equation in terms of $x_1,$ $x_2,$ and $x_3.$

Solving our original differential equation for the highest-order derivative $(y'''),$ we obtain

$$


y''' = -5y'' + 4y' - t^2y + t + 1.


$$

Then, we substitute our new variables into the right-hand side of the above equation. This gives

$$


y''' = -5x_3 + 4x_2 - t^2x_1 + t + 1.


$$

Notice that we do not include any derivative terms on the right-hand side.

Therefore, our complete system of equations is as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=𝑥_{3} \\ 𝑥_{′3}=−5𝑥_{3}+4𝑥_{2}−𝑡^{2}𝑥_{1}+𝑡+1\end{aligned}


$$

### Example: Reducing an Inhomogeneous ODE to First-Order System

#### Question

The second-order differential equation

$$


y'' - 7t y' + e^{t}y= -t


$$

can be written as a system of first-order differential equations, as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=𝑓(𝑡)\end{aligned}


$$

where $x_1(t) = y(t)$ and $x_2(t) = y'(t).$ Find the function $f(t).$

#### Explanation

First, we make the following change of variables:

$$


\begin{aligned}𝑥_{1}(𝑡) & =𝑦 \\ 𝑥_{2}(𝑡) & =𝑦^{′}\end{aligned}


$$

Differentiating the above equations with respect to $t,$ we get

$$


\begin{aligned}𝑥_{′1}(𝑡) & =𝑦^{′} \\ 𝑥_{′2}(𝑡) & =𝑦^{″}\end{aligned}


$$

which we can rewrite as

$$


\begin{aligned}𝑥_{′1}=𝑥_{2}, \\ 𝑥_{′2}=𝑦^{″}.\end{aligned}


$$

At this point, we're almost done. We just need to write the right-hand side of the last equation in terms of $x_1$ and $x_2.$

Solving our original differential equation for the highest-order derivative $(y''),$ we obtain

$$


y'' = 7t y' - e^{t}y - t.


$$

Then, we substitute our new variables into the right-hand side of the above equation. This gives

$$


y'' = 7t x_2 -e^{t}x_1 - t.


$$

Notice that we do not include any derivative terms on the right-hand side.

Therefore, our complete system of equations is as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=7𝑡𝑥_{2}−𝑒^{𝑡}𝑥_{1}−𝑡\end{aligned}


$$

Finally,

$$


f(t) = -e^{t}x_1 + 7t x_2 - t.


$$

### Expressing Inhomogeneous ODEs as Matrix Differential Equations

Consider the second-order differential equation

$$


y'' + (t+1)y' - 4y = t^{2},


$$

where $y = y(t).$ If $y = x_1(t)$ and $y' = x_2(t),$ then the given differential equation can be rewritten as the matrix equation $\mathbf{x}'(t)=A\mathbf{x}(t) + \mathbf f(t),$ where

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

Determine the matrices $A$ and $\mathbf{f}(t).$

**Explanation:**

We first need to express the given differential equation as a system of first-order differential equations. Then, we write the system as a matrix equation.

We start by making the following change of variables:

$$


\begin{aligned}𝑥_{1} & =𝑦 \\ 𝑥_{2} & =𝑦^{′}\end{aligned}


$$

Differentiating the above equations with respect to $t,$ we get

$$


\begin{aligned}𝑥_{′1}=𝑦^{′} \\ 𝑥_{′2}=𝑦^{″}\end{aligned}


$$

which we can rewrite as

$$


\begin{aligned}𝑥_{′1}=𝑥_{2}, \\ 𝑥_{′2}=𝑦^{″}.\end{aligned}


$$

We must now write the right-hand side of the last equation in terms of $x_1$ and $x_2.$

Solving our original differential equation for the highest-order derivative $(y''),$ we obtain

$$


y'' = -(t+1)y' + 4y + t^{2}.


$$

Then, we substitute our new variables into the right-hand side of the above equation. This gives

$$


y'' = -(t+1)x_2 + 4x_1 + t^{2}.


$$

Notice that we do not include any derivative terms on the right-hand side.

Therefore, our complete system of equations is as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=4𝑥_{1}−(𝑡+1)𝑥_{2}+𝑡^{2}\end{aligned}


$$

We can represent this system as the matrix differential equation $\mathbf x'(t) = A\mathbf x(t) + \mathbf f(t)$ as follows:

$$


[\begin{aligned}𝑥_{′1} \\ 𝑥_{′2}\end{aligned}]


$$

Therefore, we conclude that

$$


[\begin{aligned}0 & 1 \\ 4 & −(𝑡+1)\end{aligned}]


$$

### Example: Writing an Inhomogeneous ODE as a Matrix Differential Equation

#### Question

Consider the third-order differential equation

$$


y''' + t y' - 8 y = 1 - t^2,


$$

where $y = y(t).$ If

$$


\begin{aligned}𝑦=𝑥_{1}(𝑡) \\ 𝑦^{′}=𝑥_{2}(𝑡) \\ 𝑦^{″}=𝑥_{3}(𝑡),\end{aligned}


$$

then the given differential equation can be rewritten as the matrix equation $\mathbf{x}'(t)=A\mathbf{x}(t) + \mathbf f(t),$ where

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

Determine the matrices $A$ and $\mathbf{f}(t).$

#### Explanation

We first need to express the given differential equation as a system of first-order differential equations. Then, we write the system as a matrix equation.

We start by making the following change of variables:

$$


\begin{aligned}𝑥_{1} & =𝑦 \\ 𝑥_{2} & =𝑦^{′} \\ 𝑥_{3} & =𝑦^{″}\end{aligned}


$$

Differentiating the above equations with respect to $t,$ we get

$$


\begin{aligned}𝑥_{′1} & =𝑦^{′} \\ 𝑥_{′2} & =𝑦^{″} \\ 𝑥_{′3} & =𝑦^{‴}\end{aligned}


$$

which we can rewrite as

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=𝑥_{3} \\ 𝑥_{′3}=𝑦^{‴}.\end{aligned}


$$

We must now write the right-hand side of the last equation in terms of $x_1, x_2$ and $x_3.$

Solving our original differential equation for the highest-order derivative $(y'''),$ we obtain

$$


y''' = - t y' + 8 y + 1 - t^2.


$$

Then, we substitute our new variables into the right-hand side of the above equation. This gives

$$


y''' = - t x_2 + 8 x_1 + 1 - t^2.


$$

Notice that we do not include any derivative terms on the right-hand side.

Therefore, our complete system of equations is as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=𝑥_{3} \\ 𝑥_{′3}=8𝑥_{1}−𝑡𝑥_{2}+1−𝑡^{2}\end{aligned}


$$

We can represent this system as the matrix differential equation $\mathbf x'(t) = A\mathbf x(t) + \mathbf f(t)$ as follows:

$$


\begin{aligned}𝑥_{′1} \\ 𝑥_{′2} \\ 𝑥_{′3}\end{aligned}


$$

Therefore, we conclude that

$$


\begin{aligned}0 & 1 & 0 \\ 0 & 0 & 1 \\ 8 & −𝑡 & 0\end{aligned}


$$
