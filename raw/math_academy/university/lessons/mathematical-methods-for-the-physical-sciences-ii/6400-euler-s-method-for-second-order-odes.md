# Euler's Method for Second-Order ODEs

Source: https://www.mathacademy.com/topics/6400?courseId=155
Topic ID: 6400

## Prerequisites

- [Euler's Method for Systems of ODEs](./3245-euler-s-method-for-systems-of-odes.md)
- [Expressing Inhomogeneous ODEs as First-Order Systems](./3635-expressing-inhomogeneous-odes-as-first-order-systems.md)

## Lesson

### Introduction

Can we apply Euler's method to approximate solutions to second-order initial value problems, such as the one below?

$$


xy'' - y' - y = 2x, \qquad y(1) = -1, \quad y'(1) = 1


$$

Well, for a second-order initial value problem,

$$


y'' = f(x, y, y'), \qquad y(a) = c, \quad y'(a) = d,


$$

we can use Euler's method to approximate a solution by first reducing the second-order ODE to a system of first-order ODEs,

$$


\begin{aligned}𝑦^{′}=𝑧,\, & 𝑦(𝑎)=𝑐, \\ 𝑧^{′}=𝑓(𝑥,𝑦,𝑧),\, & 𝑧(𝑎)=𝑑,\end{aligned}


$$

before applying the update rule component-wise to each equation:

$$


\begin{aligned}Δ𝑦=𝑦^{′}⋅Δ𝑥 \\ Δ𝑧=𝑧^{′}⋅Δ𝑥\end{aligned}


$$

The new values are then given by $y_\text{new} = y + \Delta y$ and $z_\text{new} = z + \Delta z.$

In the example above, we set up Euler's method by first isolating $y''$ so it can serve as the derivative of a new variable $z{:}$

$$


\begin{aligned}𝑥𝑦^{″}−𝑦^{′}−𝑦 & =2𝑥 \\ 𝑥𝑦^{″} & =𝑦+𝑦^{′}+2𝑥 \\ 𝑦^{″} & =\frac{𝑦+𝑦^{′}}{𝑥}+2\end{aligned}


$$

Then, we substitute our new variable $z=y',$ $z'=y''$ in the above. This gives the system

$$


\begin{aligned}𝑦^{′}=𝑧,\, & 𝑦(1)=−1 \\ 𝑧^{′}=\frac{𝑦+𝑧}{𝑥}+2,\, & 𝑧(1)=1.\end{aligned}


$$

On the next slide, we will approximate values for this system using step size $\Delta x = \dfrac12.$

### A Worked Example

We now apply the update rules $\Delta y = y' \cdot \Delta x$ and $\Delta z = z' \cdot \Delta x$ to our system below starting at $x=1$ with step size $\Delta x = \dfrac12.$

$$


\begin{aligned}𝑦^{′}=𝑧,\, & 𝑦(1)=−1 \\ 𝑧^{′}=\frac{𝑦+𝑧}{𝑥}+2,\, & 𝑧(1)=1.\end{aligned}


$$

We'll start by creating a table that includes the initial condition data $y(1)=-1$ and $z(1)=1.$

We compute $y'$ and $\Delta y,$ $z'$ and $\Delta z$ (using the values of $x$, $y,$ and $z,$ in the first row), and the values of $x_\text{new},$ $y_\text{new},$ and $z_\text{new}$ using Euler's method:

$$


\begin{aligned}𝑦^{′} & =𝑧=1 \\ 𝑧^{′} & =\frac{𝑦+𝑧}{𝑥}+2=\frac{−1+1}{1}+2=2 \\ Δ𝑦 & =𝑦^{′}⋅Δ𝑥=1⋅\frac{1}{2}=\frac{1}{2} \\ Δ𝑧 & =𝑧^{′}⋅Δ𝑥=2⋅\frac{1}{2}=1 \\ 𝑥_{new} & =𝑥+Δ𝑥=1+\frac{1}{2}=\frac{3}{2} \\ 𝑦_{new} & =𝑦+Δ𝑦=−1+\frac{1}{2}=−\frac{1}{2} \\ 𝑧_{new} & =𝑧+Δ𝑧=1+1=2\end{aligned}


$$

We add these values to our table.

After several steps, we obtain the following table of values.

Therefore, we conclude that $y\left(\dfrac52\right) \approx \dfrac94$ and $y'\left(\dfrac52\right) = z\left(\dfrac52\right) \approx \dfrac{11}2.$

Notice that this approach of splitting a second-order ODE into a system of first-order ODEs is not specific to Euler's method. Indeed, we could apply any numerical method component-wise to approximate the solution to a second-order ODE once split into a system of first-order ODEs!

### Example: Completing a Row of a Table Using Euler's Method for Second-Order ODEs

#### Question

Consider the following initial value problem:

$$


y'' + 4xy' - 3y = 2x, \qquad y(0) = 1, \quad y'(0) = -2


$$

We wish to approximate the solution using Euler's method by introducing $z = y'$ and reducing the equation to a system of first-order ODEs. What entries should be placed in the columns for $\Delta y$ and $\Delta z$ in the table below if the step size is $\Delta x = 1?$

Use the information above to approximate the value of $y(1).$

#### Explanation

For a second-order initial value problem

$$


y'' = f(x,y,y'), \qquad y(a) = c, \quad y'(a) = d,


$$

we can use Euler's method to approximate a solution by first reducing the second-order ODE to a system of first-order ODEs,

$$


\begin{aligned}𝑦^{′}=𝑧,\, & 𝑦(𝑎)=𝑐, \\ 𝑧^{′}=𝑓(𝑥,𝑦,𝑧)\, & 𝑧(𝑎)=𝑑,\end{aligned}


$$

before applying the update rule component-wise to each equation.

To apply Euler’s method, we first isolate $y''$ so it can serve as the derivative of a new variable $z{:}$

$$


\begin{aligned}𝑦^{″}+4𝑥𝑦^{′}−3𝑦 & =2𝑥 \\ 𝑦^{″} & =−4𝑥𝑦^{′}+3𝑦+2𝑥\end{aligned}


$$

Then, we substitute our new variable $z = y', z' = y''$ in the right-hand side of the above equation. This gives

$$


z' = -4xz + 3y + 2x.


$$

Note that the initial value of $z$ is $z(0) = y'(0) = -2.$ So, the initial value problem reduces to the following system of first-order ODEs:

$$


\begin{aligned}𝑦^{′}=𝑧,\, & 𝑦(0)=1, \\ 𝑧^{′}=−4𝑥𝑧+3𝑦+2𝑥,\, & 𝑧(0)=−2\end{aligned}


$$

Now, we can proceed with Euler's method by applying the update rule component-wise.

First, because the initial conditions are $y(0)=1$ and $z(0)=-2,$ we place $y=1$ and $z=-2$ in the table.

Next, we compute both $y'$ and $z'$ according to the given rules:

$$


\begin{aligned}𝑦^{′} & =𝑧=−2 \\ 𝑧^{′} & =−4𝑥𝑧+3𝑦+2𝑥 \\ & =−4⋅0⋅(−2)+3⋅1+2⋅0 \\ & =0+3+0 \\ & =3\end{aligned}


$$

So, we add these to our table.

Finally, we compute $\Delta y$ and $\Delta z$ using Euler's method:

$$


\begin{aligned}Δ𝑦 & =𝑦^{′}⋅Δ𝑥 \\ & =(−2)⋅1 \\ & =−2 \\ Δ𝑧 & =𝑧^{′}⋅Δ𝑥 \\ & =3⋅1 \\ & =3\end{aligned}


$$

We add these to our table.

To get the new values of $x,$ $y,$ and $z$ in the ** row, we add $\Delta x$ to $x,$ $\Delta y$ to $y,$ and $\Delta z$ to $z,$ as follows:

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥=0+1=1 \\ 𝑦_{new} & =𝑦+Δ𝑦=1+(−2)=−1 \\ 𝑧_{new} & =𝑧+Δ𝑧=−2+3=1\end{aligned}


$$

Adding these values to our table in a new row gives the following:

Therefore, we conclude that

$$


y(1) \approx -1.


$$

### Example: Approximating the Solution to a Second-Order ODE Using Euler's Method With One Step

#### Question

Consider the following initial value problem:

$$


x^2y'' + 2y' = 4x^2, \qquad y(1) = -1, \qquad y'(1) = -1


$$

Use Euler's Method with one step to approximate $y\left(\dfrac32\right)$ and $y'\left(\dfrac32\right).$

#### Explanation

For a second-order initial value problem

$$


y'' = f(x,y,y'), \qquad y(a) = c, \quad y'(a) = d,


$$

we can use Euler's method to approximate a solution by first reducing the second-order ODE to a system of first-order ODEs,

$$


\begin{aligned}𝑦^{′}=𝑧,\, & 𝑦(𝑎)=𝑐, \\ 𝑧^{′}=𝑓(𝑥,𝑦,𝑧)\, & 𝑧(𝑎)=𝑑,\end{aligned}


$$

before applying the update rule component-wise to each equation.

To apply Euler’s method, we first isolate $y''$ so it can serve as the derivative of a new variable $z{:}$

$$


\begin{aligned}𝑥^{2}𝑦^{″}+2𝑦^{′} & =4𝑥^{2} \\ 𝑥^{2}𝑦^{″} & =4𝑥^{2}−2𝑦^{′} \\ 𝑦^{″} & =\frac{4𝑥^{2}−2𝑦^{′}}{𝑥^{2}}\end{aligned}


$$

Then, we substitute our new variable $z = y', z' = y''$ in the right-hand side of the above equation. This gives

$$


z' = \dfrac{4x^2 - 2z}{x^2}.


$$

Note that the initial value of $z$ is $z(1) = y'(1) = -1.$ So, the initial value problem reduces to the following system of first-order ODEs:

$$


\begin{aligned}𝑦^{′}=𝑧,\, & 𝑦(1)=−1, \\ 𝑧^{′}=\frac{4𝑥^{2}−2𝑧}{𝑥^{2}},\, & 𝑧(1)=−1\end{aligned}


$$

Now, we can proceed with Euler's method by applying the update rule component-wise.

Since we want to find the values of $y$ and $y'=z$ at $x=\dfrac32,$ we will use a step size of

$$


\Delta x = \dfrac32 - 1 = \dfrac12.


$$

First, we place the initial condition data in the table.

Next, we compute both $y'$ and $z'$ according to the given rules:

$$


\begin{aligned}𝑦^{′} & =𝑧=−1 \\ 𝑧^{′} & =\frac{4𝑥^{2}−2𝑧}{𝑥^{2}} \\ & =\frac{4⋅1^{2}−2⋅(−1)}{1^{2}} \\ & =\frac{4+2}{1} \\ & =6\end{aligned}


$$

So, we add these to our table.

Next, we compute $\Delta y$ and $\Delta z$ using Euler's method:

$$


\begin{aligned}Δ𝑦 & =𝑦^{′}⋅Δ𝑥 \\ & =(−1)⋅\frac{1}{2} \\ & =−\frac{1}{2} \\ Δ𝑧 & =𝑧^{′}⋅Δ𝑥 \\ & =6⋅\frac{1}{2} \\ & =3\end{aligned}


$$

We add these to our table.

To get the new values of $x,$ $y,$ and $z$ in the ** row, we add $\Delta x$ to $x,$ $\Delta y$ to $y,$ and $\Delta z$ to $z,$ as follows:

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥=1+\frac{1}{2}=\frac{3}{2} \\ 𝑦_{new} & =𝑦+Δ𝑦=−1+(−\frac{1}{2})=−\frac{3}{2} \\ 𝑧_{new} & =𝑧+Δ𝑧=−1+3=2\end{aligned}


$$

Adding these values to our table in a new row gives the following:

Therefore, we conclude that $y\left(\dfrac32\right) \approx -\dfrac32$ and $y'\left(\dfrac32\right) = z\left(\dfrac32\right) \approx 2.$

### Example: Approximating the Solution to a Second-Order ODE Using Euler's Method With Two Steps

#### Question

Consider the following initial value problem:

$$


2x y'' - (y')^2 + 4y = 0, \qquad y(1) = -1, \quad y'(1) = 2


$$

Use Euler's Method with two steps to approximate $y(3)$ and $y'(3).$

#### Explanation

For a second-order initial value problem

$$


y'' = f(x,y,y'), \qquad y(a) = c, \quad y'(a) = d,


$$

we can use Euler's method to approximate a solution by first reducing the second-order ODE to a system of first-order ODEs,

$$


\begin{aligned}𝑦^{′}=𝑧,\, & 𝑦(𝑎)=𝑐, \\ 𝑧^{′}=𝑓(𝑥,𝑦,𝑧)\, & 𝑧(𝑎)=𝑑,\end{aligned}


$$

before applying the update rule component-wise to each equation.

To apply Euler’s method, we first isolate $y''$ so it can serve as the derivative of a new variable $z{:}$

$$


\begin{aligned}2𝑥𝑦^{″}−(𝑦^{′})^{2}+4𝑦 & =0 \\ 2𝑥𝑦^{″} & =(𝑦^{′})^{2}−4𝑦 \\ 𝑦^{″} & =\frac{(𝑦^{′})^{2}−4𝑦}{2𝑥}.\end{aligned}


$$

Then, we substitute our new variable $z = y',$ $z' = y''$ in the right-hand side of the above equation. This gives

$$


z' = \dfrac{z^2 - 4y}{2x}.


$$

Note that the initial value of $z$ is $z(1) = y'(1) = 2.$ So, the initial value problem reduces to the following system of first-order ODEs:

$$


\begin{aligned}𝑦^{′}=𝑧,\, & 𝑦(1)=−1, \\ 𝑧^{′}=\frac{𝑧^{2}−4𝑦}{2𝑥},\, & 𝑧(1)=2\end{aligned}


$$

Now, we can proceed with Euler's method by applying the update rule component-wise.

First, note that we are given the values of $y$ and $z=y'$ at $x=1$ and asked to find their values at $x=3.$ The distance from $x=1$ to $x=3$ is $2,$ and since we are asked to use two steps of equal size, our step size must be

$$


\Delta x = \dfrac{3 - 1}2 = 1.


$$

Now, we'll start by creating a table that includes the initial condition data $y(1)=-1$ and $z(1)=2.$

****.

We compute $y'$ and $\Delta y,$ $z'$ and $\Delta z$ (using the values of $x,$ $y,$ and $z$ in the first row), and the values of $x_\text{new},$ $y_\text{new},$ and $z_\text{new}$ using Euler's method:

$$


\begin{aligned}𝑦^{′} & =𝑧=2 \\ 𝑧^{′} & =\frac{𝑧^{2}−4𝑦}{2𝑥}=\frac{2^{2}−4(−1)}{2⋅1}=4 \\ Δ𝑦 & =𝑦^{′}⋅Δ𝑥=2⋅1=2 \\ Δ𝑧 & =𝑧^{′}⋅Δ𝑥=4⋅1=4 \\ 𝑥_{new} & =𝑥+Δ𝑥=1+1=2 \\ 𝑦_{new} & =𝑦+Δ𝑦=−1+2=1 \\ 𝑧_{new} & =𝑧+Δ𝑧=2+4=6\end{aligned}


$$

We add these values to our table.

****.

We compute $y'$ and $\Delta y,$ $z'$ and $\Delta z$ (using the values of $x,$ $y,$ and $z$ in the second row), and the values of $x_\text{new},$ $y_\text{new},$ and $z_\text{new}$ using Euler's method:

$$


\begin{aligned}𝑦^{′} & =𝑧=6 \\ 𝑧^{′} & =\frac{𝑧^{2}−4𝑦}{2𝑥}=\frac{6^{2}−4⋅1}{2⋅2}=8 \\ Δ𝑦 & =𝑦^{′}⋅Δ𝑥=6⋅1=6 \\ Δ𝑧 & =𝑧^{′}⋅Δ𝑥=8⋅1=8 \\ 𝑥_{new} & =𝑥+Δ𝑥=2+1=3 \\ 𝑦_{new} & =𝑦+Δ𝑦=1+6=7 \\ 𝑧_{new} & =𝑧+Δ𝑧=6+8=14\end{aligned}


$$

We add these values to our table.

Therefore, we conclude that $y(3) \approx 7$ and $y'(3) = z(3) \approx 14.$
