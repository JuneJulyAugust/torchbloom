# Expressing Homogeneous ODEs as First-Order Systems

Source: https://www.mathacademy.com/topics/3186?courseId=61
Topic ID: 3186

## Prerequisites

- [Introduction to Systems of Linear ODEs](./2086-introduction-to-systems-of-linear-odes.md)
- [Introduction to Second-Order Linear ODEs](./2548-introduction-to-second-order-linear-odes.md)

## Lesson

### Introduction

To solve a second or third order homogeneous ODE, we can re-write it as an equivalent first order linear system of differential equations.

For example, let's consider the following initial value problem:

$$


y'' -4 y' + e^t y= 0 , \qquad y(1)= 1, \quad y'(1)= 0


$$

where $y=y(t)$ is a function of $t.$

First, we make the following change of variables:

$$


\begin{aligned}𝑥_{1}(𝑡) & =𝑦 \\ 𝑥_{2}(𝑡) & =𝑦^{′}\end{aligned}


$$

We also convert the initial conditions, as follows:

$$


\begin{aligned}𝑦(1) & =𝑥_{1}(1)=1 \\ 𝑦^{′}(1) & =𝑥_{2}(1)=0\end{aligned}


$$

Differentiating the above equations with respect to $t,$ we get

$$


\begin{aligned}𝑥_{′1}(𝑡) & =𝑦^{′} \\ 𝑥_{′2}(𝑡) & =𝑦^{″}\end{aligned}


$$

which we can rewrite as

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=𝑦^{″}.\end{aligned}


$$

At this point, we're almost done. We just need to write the right-hand side of the last equation in terms of $x_1$ and $x_2.$ Solving our original differential equation for the highest-order derivative $(y''),$ we obtain

$$


y'' = 4y' - e^t y.


$$

Then, we substitute our new variables into the right-hand side of the above equation. This gives

$$


y'' = 4x_2 - e^t x_1.


$$

Notice that we do not include any derivative terms on the right-hand side.

Therefore, our complete system of equations is as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2},\, & 𝑥_{1}(1)=1 \\ 𝑥_{′2}=−𝑒^{𝑡}𝑥_{1}+4𝑥_{2},\, & 𝑥_{2}(1)=0\end{aligned}


$$

We can also write it in matrix form:

$$


[\begin{aligned}𝑥_{′1} \\ 𝑥_{′2}\end{aligned}]


$$

**Note:** In the case of a higher order differential equation, the procedure is quite similar. For example, to convert a third-order linear differential equation into a system, we start by making the following change of variables:

$$


\begin{aligned}𝑥_{1} & =𝑦 \\ 𝑥_{2} & =𝑦^{′} \\ 𝑥_{3} & =𝑦^{″}\end{aligned}


$$

### Example: Reducing a Homogeneous ODE to a First-Order System

#### Question

The third-order differential equation

$$


y''' - 3\sqrt{t}\, y'' + t^3 y' - 4t^2 y= 0


$$

can be written as a system of first-order differential equations, as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=𝑥_{3} \\ 𝑥_{′3}=𝑓(𝑡)\end{aligned}


$$

where $x_1(t) = y(t),$ $x_2(t) = y'(t)$ and $x_3(t) = y''(t).$ Find the function $f(t).$

#### Explanation

First, we make the following change of variables:

$$


\begin{aligned}𝑥_{1} & =𝑦 \\ 𝑥_{2} & =𝑦^{′} \\ 𝑥_{3} & =𝑦^{″}\end{aligned}


$$

Differentiating the above equations with respect to $t,$ we get

$$


\begin{aligned}𝑥_{′1}=𝑦^{′} \\ 𝑥_{′2}=𝑦^{″} \\ 𝑥_{′3}=𝑦^{‴}\end{aligned}


$$

which we can rewrite as

$$


\begin{aligned}𝑥_{′1}=𝑥_{2}, \\ 𝑥_{′2}=𝑥_{3}, \\ 𝑥_{′3}=𝑦^{‴}.\end{aligned}


$$

At this point, we're almost done. We just need to write the right-hand side of the last equation in terms of $x_1, x_2,$ and $x_3.$

Solving our original differential equation for the highest-order derivative $(y'''),$ we obtain

$$


y''' = 3\sqrt{t}\,y'' - t^3 y' + 4t^2 y.


$$

Then, we substitute our new variables into the right-hand side of the above equation. This gives

$$


y''' = 3\sqrt{t}\, x_3 - t^3 x_2 + 4t^2 x_1.


$$

Notice that we do not include any derivative terms on the right-hand side.

Therefore, our complete system of equations is as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=𝑥_{3} \\ 𝑥_{′3}=4𝑡^{2}\,𝑥_{1}−𝑡^{3}𝑥_{2}+3\sqrt{𝑡}\,𝑥_{3}\end{aligned}


$$

Finally, $f(t) = 4t^2 x_1 - t^3 x_2 + 3\sqrt{t} \,x_3.$

### Example: Reducing a Homogeneous Initial Value Problem to a First-Order System

#### Question

The second-order initial value problem

$$


y'' + y' - 6y= 0 , \quad y(0)= 1, \quad y'(0)= 4


$$

can be written as a system of first-order differential equations, as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2},\, & 𝑥_{1}(0)=𝑝 \\ 𝑥_{′2}=𝑓(𝑡),\, & 𝑥_{2}(0)=𝑞\end{aligned}


$$

where $x_1(t) = y(t),$ $x_2(t) = y'(t),$ and $p$ and $q$ are constants. Calculate $(p-q)\cdot f(t).$

#### Explanation

First, we make the following change of variables:

$$


\begin{aligned}𝑥_{1}(𝑡) & =𝑦 \\ 𝑥_{2}(𝑡) & =𝑦^{′}.\end{aligned}


$$

We also convert the initial conditions, as follows:

$$


\begin{aligned}𝑦(0) & =𝑥_{1}(0)=1 \\ 𝑦^{′}(0) & =𝑥_{2}(0)=4\end{aligned}


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


y'' = - y' + 6y.


$$

Then, we substitute our new variables into the right-hand side of the above equation. This gives

$$


y'' = - x_2 + 6x_1.


$$

Notice that we do not include any derivative terms on the right-hand side.

Therefore, our complete system of equations is as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2},\, & 𝑥_{1}(0)=1 \\ 𝑥_{′2}=6𝑥_{1}−𝑥_{2},\, & 𝑥_{2}(0)=4\end{aligned}


$$

Finally, $p=1, q=4, f(t) = 6x_1 - x_2,$ and

$$


\begin{aligned}(𝑝−𝑞)⋅𝑓(𝑡) & =(1−4)(6𝑥_{1}−𝑥_{2}) \\ & =−3(6𝑥_{1}−𝑥_{2}).\end{aligned}


$$

### Example: Writing a Homogeneous ODE as a Matrix Differential Equation

#### Question

The second-order differential equation $y'' + 5y' - 2y=0$ can be expressed as the matrix equation $\mathbf{x}'(t)=A\mathbf{x}(t),$ where

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

Find the matrix $A.$

#### Explanation

We first need to express the given differential equation as a system of first-order differential equations. Then, we write the system as a matrix equation.

We start by making the following change of variables:

$$


\begin{aligned}𝑥_{1} & =𝑦 \\ 𝑥_{2} & =𝑦^{′}\end{aligned}


$$

Differentiating the above equations with respect to $t,$ we get

$$


\begin{aligned}𝑥_{′1} & =𝑦^{′} \\ 𝑥_{′2} & =𝑦^{″}\end{aligned}


$$

which we can rewrite as

$$


\begin{aligned}𝑥_{′1}=𝑥_{2}, \\ 𝑥_{′2}=𝑦^{″}.\end{aligned}


$$

We must now write the right-hand side of the last equation in terms of $x_1$ and $x_2.$

Solving our original differential equation for the highest-order derivative $(y''),$ we obtain

$$


y''= -5y' + 2y.


$$

Then, we substitute our new variables into the right-hand side of the above equation. This gives

$$


y'' = -5x_2 + 2x_1.


$$

Notice that we do not include any derivative terms on the right-hand side.

Therefore, our complete system of equations is as follows:

$$


\begin{aligned}𝑥_{′1}=𝑥_{2} \\ 𝑥_{′2}=2𝑥_{1}−5𝑥_{2}\end{aligned}


$$

We can represent this system as the matrix differential equation $\mathbf x'(t) = A\mathbf x(t)$ as follows:

$$


[\begin{aligned}𝑥_{′1} \\ 𝑥_{′2}\end{aligned}]


$$

Hence, $[\begin{aligned}0 & 1 \\ 2 & −5\end{aligned}]$
