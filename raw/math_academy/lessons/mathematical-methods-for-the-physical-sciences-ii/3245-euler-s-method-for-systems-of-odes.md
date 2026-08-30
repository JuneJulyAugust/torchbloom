# Euler's Method for Systems of ODEs

Source: https://www.mathacademy.com/topics/3245?courseId=155
Topic ID: 3245

## Prerequisites

- [Introduction to Systems of Linear ODEs](./2086-introduction-to-systems-of-linear-odes.md)
- [Euler's Method: Calculating Multiple Steps](./3668-euler-s-method-calculating-multiple-steps.md)

## Lesson

### Introduction

Consider the following initial value problem:

$$


\begin{aligned}𝑦^{′}=2𝑥+𝑦−𝑧,\, & 𝑦(0)=1 \\ 𝑧^{′}=𝑥+2𝑦+𝑧,\, & 𝑧(0)=2\end{aligned}


$$

Is it possible to approximate solutions to initial value problems involving a system of equations, such as the one above, using Euler's method?

Indeed, for a system of ODEs with initial values,

$$


\begin{aligned}𝑦^{′}=𝑓(𝑥,𝑦,𝑧),\, & 𝑦(𝑎)=𝑐, \\ 𝑧^{′}=𝑔(𝑥,𝑦,𝑧),\, & 𝑧(𝑎)=𝑑,\end{aligned}


$$

where $y = y(x), z = z(x),$ we can use Euler's method to approximate a solution by applying it to each ODE simultaneously, but separately:

$$


\begin{aligned}Δ𝑦=𝑦^{′}⋅Δ𝑥 \\ Δ𝑧=𝑧^{′}⋅Δ𝑥\end{aligned}


$$

With this in mind, let's approximate the values of $y(1)$ and $z(1)$ for our initial value problem above using Euler's method with step size $\Delta x = 1.$

We start by constructing a table that contains all relevant quantities, including slopes and increments for *both* variables. Then, because the initial conditions are $y(0)=1$ and $z(0)=2,$ we place $x=0,$ $y=1,$ and $z=2$ in the first row.

Next, we compute *both $y'$ and $z'$* according to the given rules using the current values of $x,$ $y,$ and $z{:}$

$$


\begin{aligned}𝑦^{′} & =2𝑥+𝑦−𝑧\, & \,𝑧^{′} & =𝑥+2𝑦+𝑧 \\ & =2⋅0+1−2 & & =0+2⋅1+2 \\ & =−1 & & =4\end{aligned}


$$

So, we add these to our table.

Finally, we compute $\Delta y$ and $\Delta z$ using Euler's method:

$$


\begin{aligned}Δ𝑦 & =𝑦^{′}⋅Δ𝑥\, & \,Δ𝑧 & =𝑧^{′}⋅Δ𝑥 \\ & =(−1)⋅1 & & =4⋅1 \\ & =−1 & & =4\end{aligned}


$$

We add these to our table.

To get the new values of $x,$ $y,$ and $z$ in the *next* row, we add $\Delta x$ to $x,$ $\Delta y$ to $y,$ and $\Delta z$ to $z,$ as follows:

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥=0+1=1 \\ 𝑦_{new} & =𝑦+Δ𝑦=1+(−1)=0 \\ 𝑧_{new} & =𝑧+Δ𝑧=2+4=6\end{aligned}


$$

Adding these values to our table in a new row gives the following:

Therefore, we conclude that $y(1) \approx 0$ and $z(1) \approx 6.$

Notice that this component-wise approach is not specific to Euler's method. Indeed, we could apply any numerical method component-wise to approximate the solution to a system of ODEs!

### Example: Approximating the Solution to a System of ODEs Using Euler's Method With One Step

#### Question

Consider the following initial value problem for the functions $y = y(x), z = z(x){:}$

$$


\begin{aligned}𝑦^{′}=4𝑥+5𝑦−𝑧,\, & 𝑦(0)=3 \\ 𝑧^{′}=5𝑥−4𝑦+2𝑧,\, & 𝑧(0)=4\end{aligned}


$$

Use Euler's Method with one step to approximate $y(1)$ and $z(1).$

#### Explanation

For an initial value problem

$$


\begin{aligned}𝑦^{′}=𝑓(𝑥,𝑦,𝑧),\, & 𝑦(𝑎)=𝑐, \\ 𝑧^{′}=𝑔(𝑥,𝑦,𝑧),\, & 𝑧(𝑎)=𝑑,\end{aligned}


$$

Euler's method approximates the solution by applying the update rule component-wise to each equation. More precisely, the increments on $y$ and $z$ are

$$


\begin{aligned}Δ𝑦=𝑦^{′}⋅Δ𝑥, \\ Δ𝑧=𝑧^{′}⋅Δ𝑥.\end{aligned}


$$

The new values are then given by $y_\text{new} = y + \Delta y$ and $z_\text{new} = z + \Delta z.$

Since we want to find the value of $y$ and $z$ at $x=1,$ we will use a step size of

$$


\Delta x = 1 - 0 = 1.


$$

First, we place the initial condition data in a table.

Next, we compute both $y'$ and $z'$ according to the given rules:

$$


\begin{aligned}𝑦^{′} & =4𝑥+5𝑦−𝑧 \\ & =4⋅0+5⋅3−4 \\ & =0+15−4 \\ & =11 \\ 𝑧^{′} & =5𝑥−4𝑦+2𝑧 \\ & =5⋅0−4⋅3+2⋅4 \\ & =0−12+8 \\ & =−4\end{aligned}


$$

So, we add these to our table.

Next, we compute $\Delta y$ and $\Delta z$ using Euler's method:

$$


\begin{aligned}Δ𝑦 & =𝑦^{′}⋅Δ𝑥 \\ & =11⋅1 \\ & =11 \\ Δ𝑧 & =𝑧^{′}⋅Δ𝑥 \\ & =(−4)⋅1 \\ & =−4\end{aligned}


$$

We add these to our table.

To get the new values of $x,$ $y,$ and $z$ in the ** row, we add $\Delta x$ to $x,$ $\Delta y$ to $y,$ and $\Delta z$ to $z,$ as follows:

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥=0+1=1 \\ 𝑦_{new} & =𝑦+Δ𝑦=3+11=14 \\ 𝑧_{new} & =𝑧+Δ𝑧=4+(−4)=0\end{aligned}


$$

Adding these values to our table in a new row gives the following:

Therefore, we conclude that $y(1) \approx 14$ and $z(1) \approx 0.$

### Example: Approximating the Solution to a System of ODEs Using Euler's Method With Multiple Steps

#### Question

Consider the following initial value problem for the functions $y = y(x), z = z(x){:}$

$$


\begin{aligned}𝑦^{′}=𝑥−𝑦+2𝑧,\, & 𝑦(1)=1 \\ 𝑧^{′}=3𝑥+𝑦−𝑧,\, & 𝑧(1)=0\end{aligned}


$$

Use Euler's method with two steps of equal size to approximate $y(3)$ and $z(3).$

#### Explanation

For an initial value problem

$$


\begin{aligned}𝑦^{′}=𝑓(𝑥,𝑦,𝑧),\, & 𝑦(𝑎)=𝑐, \\ 𝑧^{′}=𝑔(𝑥,𝑦,𝑧),\, & 𝑧(𝑎)=𝑑,\end{aligned}


$$

Euler's method approximates the solution by applying the update rule component-wise to each equation. More precisely, the increments on $y$ and $z$ are

$$


\begin{aligned}Δ𝑦=𝑦^{′}⋅Δ𝑥, \\ Δ𝑧=𝑧^{′}⋅Δ𝑥.\end{aligned}


$$

The new values are then given by $y_\text{new} = y + \Delta y$ and $z_\text{new} = z + \Delta z.$

First, note that we are given the values of $y$ and $z$ at $x=1$ and asked to find their values at $x=3.$ The distance from $x=1$ to $x=3$ is $2,$ and since we are asked to use two steps of equal size, our step size must be

$$


\Delta x = \dfrac{3 - 1}2 = \dfrac22 = 1.


$$

Now, let's proceed with Euler's method. We'll start by creating a table that includes the initial condition data $y(1)=1$ and $z(1)=0.$

****.

We compute $y'$ and $\Delta y,$ $z'$ and $\Delta z$ (using the values of $x,$ $y,$ and $z$ in the first row), and the values of $x_\text{new},$ $y_\text{new},$ and $z_\text{new}$ using Euler's method:

$$


\begin{aligned}𝑦^{′} & =𝑥−𝑦+2𝑧=1−1+2⋅0=0 \\ 𝑧^{′} & =3𝑥+𝑦−𝑧=3⋅1+1−0=4 \\ Δ𝑦 & =𝑦^{′}⋅Δ𝑥=0⋅1=0 \\ Δ𝑧 & =𝑧^{′}⋅Δ𝑥=4⋅1=4 \\ 𝑥_{new} & =𝑥+Δ𝑥=1+1=2 \\ 𝑦_{new} & =𝑦+Δ𝑦=1+0=1 \\ 𝑧_{new} & =𝑧+Δ𝑧=0+4=4\end{aligned}


$$

We add these values to our table.

****.

We compute $y'$ and $\Delta y,$ $z'$ and $\Delta z$ (using the values of $x,$ $y,$ and $z$ in the second row), and the values of $x_\text{new},$ $y_\text{new},$ and $z_\text{new}$ using Euler's method:

$$


\begin{aligned}𝑦^{′} & =𝑥−𝑦+2𝑧=2−1+2⋅4=9 \\ 𝑧^{′} & =3𝑥+𝑦−𝑧=3⋅2+1−4=3 \\ Δ𝑦 & =𝑦^{′}⋅Δ𝑥=9⋅1=9 \\ Δ𝑧 & =𝑧^{′}⋅Δ𝑥=3⋅1=3 \\ 𝑥_{new} & =𝑥+Δ𝑥=2+1=3 \\ 𝑦_{new} & =𝑦+Δ𝑦=1+9=10 \\ 𝑧_{new} & =𝑧+Δ𝑧=4+3=7\end{aligned}


$$

We add these values to our table.

Therefore, we conclude that $y(3) \approx 10$ and $z(3) \approx 7.$

### Euler's Method for Larger Systems of ODEs

We can apply Euler's method to a system of *any number* of simultaneous first-order ODEs. That is, for an initial value problem

$$


\begin{aligned}𝑦_{′1}^{}=𝑓_{1}(𝑥,𝑦_{1},𝑦_{2},…,𝑦_{𝑚}),\, & 𝑦_{1}(𝑎)=𝑐_{1}, \\ 𝑦_{′2}^{}=𝑓_{2}(𝑥,𝑦_{1},𝑦_{2},…,𝑦_{𝑚}),\, & 𝑦_{2}(𝑎)=𝑐_{2}, \\ \,\,⋮ & \\ 𝑦_{′𝑚}^{}=𝑓_{𝑚}(𝑥,𝑦_{1},𝑦_{2},…,𝑦_{𝑚}),\, & 𝑦_{𝑚}(𝑎)=𝑐_{𝑚},\end{aligned}


$$

Euler's method approximates a solution by applying the update rule component-wise. The increments are

$$


\begin{aligned}Δ𝑦_{1}=𝑦_{′1}^{}⋅Δ𝑥 \\ Δ𝑦_{2}=𝑦_{′2}^{}⋅Δ𝑥 \\ \,\,\,⋮ \\ Δ𝑦_{𝑚}=𝑦_{′𝑚}^{}⋅Δ𝑥\end{aligned}


$$

The new values are then given by $y_{i,\text{new}} = y_i + \Delta y_i,$ for $i=1,2,\ldots,m.$

For convenience, we can express large systems of ODEs in vector form. Let

$$


\begin{aligned}𝑦_{1} \\ 𝑦_{2} \\ ⋮ \\ 𝑦_{𝑚}\end{aligned}


$$

Then, the initial value problem

$$


\mathbf{y}' = \mathbf{f}(x, \mathbf{y}), \qquad \mathbf{y}(a) = \mathbf{c},


$$

has Euler update

$$


\Delta \mathbf{y} = \mathbf{y}' \cdot \Delta x \qquad \mathbf{y}_\text{new} = \mathbf{y} + \Delta \mathbf{y}.


$$

Next, we will apply this vector formulation to a specific numerical example.

### Example: Approximating the Solution to a System of Three ODEs Using Euler's Method

#### Question

Consider the following initial value problem for the functions $y = y(x), z = z(x), w=w(x){:}$

$$


\begin{aligned}𝑦^{′}=2𝑦+𝑧+𝑥,\, & 𝑦(0)=1 \\ 𝑧^{′}=𝑦+𝑧+2𝑥,\, & 𝑧(0)=0 \\ 𝑤^{′}=𝑤𝑦−𝑥,\, & 𝑤(0)=2\end{aligned}


$$

Approximate values of $y$, $z$ and $w$ at $x = 1$ using Euler's method if the step size is $\Delta x = 1.$

#### Explanation

Euler's method approximates the solution of an initial value problem containing a system of ODEs by applying the update rule component-wise to each equation.

First, because the initial conditions are $y(0)=1,$ $z(0)=0,$ and $w(0)=2,$ we place $y=1,$ $z=0,$ and $w=2$ in the table.

Next, we compute $y', z',$ and $w'$ according to the given rules:

$$


\begin{aligned}𝑦^{′} & =2𝑦+𝑧+𝑥 \\ & =2⋅1+0+0 \\ & =2 \\ 𝑧^{′} & =𝑦+𝑧+2𝑥 \\ & =1+0+2⋅0 \\ & =1 \\ 𝑤^{′} & =𝑤𝑦−𝑥 \\ & =2⋅1−0 \\ & =2\end{aligned}


$$

So, we add these to our table.

Finally, we compute $\Delta y,$ $\Delta z,$ and $\Delta w$ using Euler's method:

$$


\begin{aligned}Δ𝑦 & =𝑦^{′}⋅Δ𝑥=2⋅1=2 \\ Δ𝑧 & =𝑧^{′}⋅Δ𝑥=1⋅1=1 \\ Δ𝑤 & =𝑤^{′}⋅Δ𝑥=2⋅1=2\end{aligned}


$$

We add these to our table.

To get the new values of $x,$ $y,$ $z,$ and $w$ in the ** row, we add $\Delta x$ to $x,$ $\Delta y$ to $y,$ $\Delta z$ to $z,$ and $\Delta w$ to $w,$ as follows:

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥=0+1=1 \\ 𝑦_{new} & =𝑦+Δ𝑦=1+2=3 \\ 𝑧_{new} & =𝑧+Δ𝑧=0+1=1 \\ 𝑤_{new} & =𝑤+Δ𝑤=2+2=4\end{aligned}


$$

Adding these values to our table in a new row gives the following:

Therefore, we conclude that $y(1) \approx \boxed{3},$ $z(1) \approx \boxed{1},$ and $w(1) \approx \boxed{4}.$
