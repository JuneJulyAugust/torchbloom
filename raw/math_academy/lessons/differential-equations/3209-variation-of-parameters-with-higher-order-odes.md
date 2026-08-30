# Variation of Parameters With Higher-Order ODEs

Source: https://www.mathacademy.com/topics/3209?courseId=61
Topic ID: 3209

## Prerequisites

- [Solving Second-Order ODEs Using Variation of Parameters](./6704-solving-second-order-odes-using-variation-of-parameters.md)

## Lesson

### Introduction

For a third-order linear differential equation

$$


y''' + a_2(x)y'' + a_1(x)y' + a_0(x)y = g(x),


$$

we can find a *particular solution* using the method of *variation of parameters*.

- **Step 1.** Find a set of *fundamental solutions* $\{y_1, \, y_2, \, y_3\}$ for the corresponding *homogeneous equation*.

- **Step 2.** Assume the particular solution has the form $y_p(x) = u_1(x)y_1(x) + u_2(x)y_2(x) + u_3(x)y_3(x)$.

- **Step 3.** To find the functions $u_1, u_2, u_3$, we first compute the *Wronskian* $W(x)$ of the fundamental solutions: We also compute the determinants $W_1(x), W_2(x), W_3(x)$, where $W_i(x)$ is the $2 \times 2$ determinant obtained from the Wronskian by deleting the $3$rd row and the $i$th column.

- **Step 4.** The functions $u_i(x)$ are found by integrating:

- **Step 5.** The *general solution* is $y(x) = c_1y_1(x) + c_2y_2(x) + c_3y_3(x) + y_p(x)$.

We'll see how to derive the formulas at the end of the lesson.

Let's see a concrete example.

### Example: Finding the Particular Solution of a Differential Equation Using Variation of Parameters

#### Question

$$


y''' - 3y'' - 6y' + 8y = 2 + 5e^{-x}, \qquad \big\{ y_1 = e^{-2x}, \: y_2 = e^{x}, \: y_3 = e^{4x} \big\}


$$

Consider the differential equation and the set of fundamental solutions of the corresponding homogeneous equation above. Using the method of variation of parameters, the particular solution of the equation can be written in the form

$$


y_p(x) = u_1(x)e^{-2x} +u_2(x)e^{x} + u_3(x)e^{4x}.


$$

What is the function $u_1(x)?$

#### Explanation

According to the method of variation of parameters, the particular solution is

$$


{y_p} = {u_1}{y_1} + {u_2}{y_2} + {u_3}{y_3}, \qquad {u_i} = (-1)^{3-i} \int{{\frac{{g(x){W_i}(x)}}{W(x)}\,\text{d}x}}, \qquad i=1,2,3,


$$

where $g(x)$ is the forcing term, $W(x)$ is the Wronskian of $y_1,y_2,y_3,$ and

$$


\begin{aligned}𝑊_{1}(𝑥)=\begin{aligned}𝑦_{2} & 𝑦_{3} \\ 𝑦_{′2}^{} & 𝑦_{′3}^{}\end{aligned},\,𝑊_{2}(𝑥)=\begin{aligned}𝑦_{1} & 𝑦_{3} \\ 𝑦_{′1}^{} & 𝑦_{′3}^{}\end{aligned},\,𝑊_{3}(𝑥)=\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned}.\end{aligned}


$$

In our case, the forcing term is $g(x) = 2 + 5e^{-x}.$ Additionally, we're given the fundamental solutions

$$


y_1= e^{ - 2x}, \qquad y_2= e^{x}, \qquad y_3= e^{4x}.


$$

First, let's verify that the fundamental solutions $y_1,$ $y_2,$ and $y_3$ are independent by computing the Wronskian:

$$


\begin{aligned}𝑊(𝑥) & =𝑊(𝑦_{1},𝑦_{2},𝑦_{3}) \\ & =\begin{aligned}𝑒^{−2𝑥} & 𝑒^{𝑥} & 𝑒^{4𝑥} \\ −2𝑒^{−2𝑥} & 𝑒^{𝑥} & 4𝑒^{4𝑥} \\ 4𝑒^{−2𝑥} & 𝑒^{𝑥} & 16𝑒^{4𝑥}\end{aligned} \\ & =(𝑒^{−2𝑥}⋅𝑒^{𝑥}⋅𝑒^{4𝑥})\begin{aligned}1 & 1 & 1 \\ −2 & 1 & 4 \\ 4 & 1 & 16\end{aligned} \\ & =𝑒^{3𝑥}[1(16−4)−1(−32−16)+1(−2−4)] \\ & =𝑒^{3𝑥}(12+48−6) \\ & =54𝑒^{3𝑥}\end{aligned}


$$

Since the Wronskian is not equal to zero, this confirms that the functions $y_1,$ $y_2,$ and $y_3$ are linearly independent.

Now, to find $u_1,$ we compute the determinant

$$


\begin{aligned}𝑊_{1}(𝑥) & =𝑊_{1}(𝑦_{2},𝑦_{3}) \\ & =\begin{aligned}𝑦_{2} & 𝑦_{3} \\ 𝑦_{′2}^{} & 𝑦_{′3}^{}\end{aligned} \\ & =\begin{aligned}𝑒^{𝑥} & 𝑒^{4𝑥} \\ 𝑒^{𝑥} & 4𝑒^{4𝑥}\end{aligned} \\ & =4𝑒^{5𝑥}−𝑒^{5𝑥} \\ & =3𝑒^{5𝑥}.\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}𝑢_{1}(𝑥) & =(−1)^{3−1}∫\frac{𝑔(𝑥)𝑊_{1}(𝑥)}{𝑊(𝑥)}\,d𝑥 \\ & =∫\frac{(2+5𝑒^{−𝑥})(3𝑒^{5𝑥})}{54𝑒^{3𝑥}}\,d𝑥 \\ & =\frac{1}{18}∫(2+5𝑒^{−𝑥})𝑒^{2𝑥}\,d𝑥 \\ & =\frac{1}{18}∫(2𝑒^{2𝑥}+5𝑒^{𝑥})\,d𝑥 \\ & =\frac{1}{18}(𝑒^{2𝑥}+5𝑒^{𝑥}).\end{aligned}


$$

### Example: Solving a Differential Equation Using Variation of Parameters

#### Question

$$


y''' + 4y' = 6, \qquad \big\{ y_1 = 1, \: y_2 = \cos(2x), \: y_3 = \sin(2x) \big\}


$$

Consider the differential equation and the set of fundamental solutions of the corresponding homogeneous equation above. Using the method of variation of parameters, the general solution of the equation can be written in the form

$$


y(x) = A + B \cos(2x) + C \sin(2x) + u_1(x) + u_2(x) \cos(2x) + u_3(x) \sin(2x).


$$

What is the function $u_3(x)?$

#### Explanation

According to the method of variation of parameters, the particular solution is

$$


{y_p} = {u_1}{y_1} + {u_2}{y_2} + {u_3}{y_3}, \qquad {u_i} = (-1)^{3-i} \int \frac{g(x){W_i}(x)}{W(x)}\,\text{d}x, \qquad i=1,2,3,


$$

where $g(x)$ is the forcing term, $W(x)$ is the Wronskian of $y_1,y_2,y_3,$ and

$$


\begin{aligned}𝑊_{1}(𝑥)=\begin{aligned}𝑦_{2} & 𝑦_{3} \\ 𝑦_{′2}^{} & 𝑦_{′3}^{}\end{aligned},\,𝑊_{2}(𝑥)=\begin{aligned}𝑦_{1} & 𝑦_{3} \\ 𝑦_{′1}^{} & 𝑦_{′3}^{}\end{aligned},\,𝑊_{3}(𝑥)=\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned}.\end{aligned}


$$

In our case, the forcing term is $g(x) = 6.$ Additionally, we're given the fundamental solutions

$$


y_1= 1, \qquad y_2= \cos(2x), \qquad y_3= \sin(2x).


$$

First, let's verify that the fundamental solutions $y_1,$ $y_2,$ and $y_3$ are independent by computing the Wronskian:

$$


\begin{aligned}𝑊(𝑥) & =𝑊(𝑦_{1},𝑦_{2},𝑦_{3}) \\ & =\begin{aligned}1 & cos⁡(2𝑥) & sin⁡(2𝑥) \\ 0 & −2sin⁡(2𝑥) & 2cos⁡(2𝑥) \\ 0 & −4cos⁡(2𝑥) & −4sin⁡(2𝑥)\end{aligned} \\ & =1⋅\begin{aligned}−2sin⁡(2𝑥) & 2cos⁡(2𝑥) \\ −4cos⁡(2𝑥) & −4sin⁡(2𝑥)\end{aligned} \\ & =8sin^{2}⁡(2𝑥)+8cos^{2}⁡(2𝑥) \\ & =8.\end{aligned}


$$

Since the Wronskian is not equal to zero, this confirms that the functions $y_1,$ $y_2,$ and $y_3$ are linearly independent.

Now, to find $u_3,$ we compute the determinant $W_3(x)$:

$$


\begin{aligned}𝑊_{3}(𝑥) & =\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned} \\ & =\begin{aligned}1 & cos⁡(2𝑥) \\ 0 & −2sin⁡(2𝑥)\end{aligned} \\ & =−2sin⁡(2𝑥).\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}𝑢_{3}(𝑥) & =(−1)^{3−3}∫\frac{𝑔(𝑥)𝑊_{3}(𝑥)}{𝑊(𝑥)}\,d𝑥 \\ & =∫\frac{6(−2sin⁡(2𝑥))}{8}\,d𝑥 \\ & =−\frac{3}{2}∫sin⁡(2𝑥)\,d𝑥 \\ & =\frac{3}{4}cos⁡(2𝑥).\end{aligned}


$$

### Variation of Parameters for Nth-Order ODEs

Finally, consider an $n$th-order linear differential equation

$$


y^{(n)} + a_{n-1}(x)y^{(n-1)} + \cdots + a_1(x)y' + a_0(x)y = g(x),


$$

and let $\{y_1,\dots,y_n\}$ be a set of fundamental solutions of the corresponding homogeneous equation.

Now, we’ll derive formulas for the method of variation of parameters.

A particular solution can be written as

$$


y_p(x) = u_1(x)y_1(x) + \cdots + u_n(x)y_n(x).


$$

To find $u_1,\dots,u_n$, we impose $n-1$ auxiliary conditions:

$$


\sum_{j=1}^n u_j'(x)y_j^{(k)}(x) = 0, \qquad k=0,1,\dots,n-2,


$$

which leads to the final equation

$$


\sum_{j=1}^n u_j'(x)y_j^{(n-1)}(x) = g(x).


$$

Together, these $n$ equations form a linear system for $u_1'(x),\dots,u_n'(x)$ of the form

$$


Y \mathbf{u} = \mathbf{g},


$$

where

$$


\begin{aligned}𝑦_{1} & 𝑦_{2} & ⋯ & 𝑦_{𝑛} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{} & ⋯ & 𝑦_{′𝑛}^{} \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 𝑦_{(𝑛−2)1}^{} & 𝑦_{(𝑛−2)2}^{} & ⋯ & 𝑦_{(𝑛−2)𝑛}^{} \\ 𝑦_{(𝑛−1)1}^{} & 𝑦_{(𝑛−1)2}^{} & ⋯ & 𝑦_{(𝑛−1)𝑛}^{}\end{aligned}


$$

Now, recall that $W(x) = \det(Y)$ is the Wronskian. And for each $i=1,\dots,n,$ define:

- $\widehat{W}_i(x)$ as the determinant obtained by replacing the $i$th column of $Y$ with $\mathbf{g},$ and

- $W_i(x)$ as the determinant obtained by deleting the $n$th (final) row and the $i$th column from $Y.$

Notice that, since $\mathbf{g}$ has zeroes in all components except for the final one (which is equal to $g(x)$), by the properties of determinants we can expand $\widehat{W}_i(x)$ as

$$


\begin{aligned}\overset{𝑊}{ˆ}_{𝑖}(𝑥) & =(−1)^{𝑛+𝑖}𝑔(𝑥)𝑊_{𝑖}(𝑥) \\ & =(−1)^{𝑛−𝑖}𝑔(𝑥)𝑊_{𝑖}(𝑥).\end{aligned}


$$

Here, we used that $(-1)^{n+i} = (-1)^{n-i}$ because the exponents differ by an even number, $2i.$

Next, by *Cramer's rule*, we get

$$


u'_i = \dfrac{\widehat{W}_i(x)}{W(x)} = (-1)^{n-i} \frac{g(x)\,W_i(x)}{W(x)}, \qquad i=1,\dots,n,


$$

and integrating both sides (setting the constant of integration to zero), we obtain

$$


u_i(x) = (-1)^{n-i}\int \frac{g(x)\,W_i(x)}{W(x)}\,\text{d}x, \qquad i=1,\dots,n.


$$

Finally, the general solution is

$$


y(x)=u_1y_1(x)+\cdots+u_ny_n(x)+y_p(x).


$$
