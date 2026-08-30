# Solving Second-Order ODEs Using Variation of Parameters

Source: https://www.mathacademy.com/topics/6704?courseId=154
Topic ID: 6704

## Prerequisites

- [Cramer's Rule for 2x2 Systems of Linear Equations](./1775-cramer-s-rule-for-2x2-systems-of-linear-equations.md)
- [Variation of Parameters for Second-Order ODEs](./2527-variation-of-parameters-for-second-order-odes.md)

## Lesson

### Introduction

In this topic, we'll derive a formula for variation of parameters for second-order linear ODEs.

Suppose we're given the differential equation

$$


y'' + p(x)y' + q(x)y = f(x)


$$

and let $y_1$ and $y_2$ be fundamental solutions of the corresponding homogeneous equation.

Recall that the method of variation of parameters begins by assuming that a particular solution satisfies the following constraints:

$$


\begin{aligned}𝑦_{𝑝}=𝑢_{1}𝑦_{1}+𝑢_{2}𝑦_{2} \\ 𝑦_{′𝑝}^{}=𝑢_{1}𝑦_{′1}^{}+𝑢_{2}𝑦_{′2}^{}\end{aligned}


$$

Using these constraints, we will set up a system of two equations that we can solve for $u_1$ and $u_2.$

- To obtain the first equation, we differentiate the constraint for $y_p$ given above, and since we assumed that $y_p' = u_1 y_1' + u_2 y_2',$ we reach

- To obtain another equation, we substitute the constraints into the differential equation and simplify: Here, $y_1'' + p(x) y_1' + q(x)y_1=0$ and $y_2'' + p(x) y_2' + q(x) y_2=0$ since $y_1$ and $y_2$ are solutions of the corresponding homogeneous ODE. Thus, we get

So, we have the following system:

$$


\begin{aligned}𝑢_{′1}^{}𝑦_{1}+𝑢_{′2}^{}𝑦_{2}=0 \\ 𝑢_{′1}^{}𝑦_{′1}^{}+𝑢_{′2}^{}𝑦_{′2}^{}=𝑓\end{aligned}


$$

According to Cramer's rule, the solution of the system is the following:

$$


\begin{aligned}𝑢_{′1}^{} & =\frac\begin{aligned}0 & 𝑦_{2} \\ 𝑓 & 𝑦_{′2}^{}\end{aligned}}\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned}}=−\frac{𝑦_{2}𝑓}{𝑦_{1}𝑦_{′2}^{}−𝑦_{2}𝑦_{′1}^{}}=−\frac{𝑓(𝑥)𝑦_{2}(𝑥)}{𝑊(𝑦_{1},𝑦_{2})} \\ 𝑢_{′2}^{} & =\frac\begin{aligned}𝑦_{1} & 0 \\ 𝑦_{′1}^{} & 𝑓\end{aligned}}\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned}}=\frac{𝑦_{1}𝑓}{𝑦_{1}𝑦_{′2}^{}−𝑦_{2}𝑦_{′1}^{}}=\frac{𝑓(𝑥)𝑦_{1}(𝑥)}{𝑊(𝑦_{1},𝑦_{2})}\end{aligned}


$$

where $W(y_1,y_2)$ is the Wronskian.

Integrating, we reach the final result:

$$


\begin{aligned}𝑢_{1}=−∫\frac{𝑓(𝑥)𝑦_{2}(𝑥)}{𝑊(𝑦_{1},𝑦_{2})}\,d𝑥,\,𝑢_{2}=∫\frac{𝑓(𝑥)𝑦_{1}(𝑥)}{𝑊(𝑦_{1},𝑦_{2})}\,d𝑥\end{aligned}


$$

### Example: Solving a Differential Equation Whose Characteristic Equation Has Real Roots

#### Question

Consider the following differential equation.

$$


y'' - 2y' + y = 18x e^{x}


$$

The general solution to this equation can be written as

$$


y(x) = A e^{x} + B x e^{x} + g(x),


$$

where $A$ and $B$ are constants. What could be the function $g(x)?$

#### Explanation

Suppose we have a second-order linear differential equation with linearly independent fundamental solutions $y_1(x)$ and $y_2(x)$. Then, according to the method of variation of parameters, we can seek a particular solution $y_p$ may be written as

$$


\begin{aligned}𝑦_{𝑝}(𝑥) & =𝑢_{1}(𝑥)𝑦_{1}(𝑥)+𝑢_{2}(𝑥)𝑦_{2}(𝑥),\end{aligned}


$$

where $u_1$ and $u_2$ satisfy the following system:

$$


\begin{aligned}𝑢_{′1}^{}𝑦_{′1}^{}+𝑢_{′2}^{}𝑦_{′2}^{}=𝑓(𝑥) \\ 𝑢_{′1}^{}𝑦_{1}+𝑢_{′2}^{}𝑦_{2}=0\end{aligned}


$$

The solution to this system is

$$


u_1(x) = -\int \dfrac{f(x)y_2(x)}{W(y_1,y_2)}\,dx, \qquad u_2(x) = \int \dfrac{f(x)y_1(x)}{W(y_1,y_2)}\,dx,


$$

where $W(y_1,y_2)$ is the Wronskian.

From the given information, we see that the complementary solution is

$$


y_c(x) = A e^{x} + B x e^{x}.


$$

Therefore, the fundamental solutions to the corresponding homogeneous equation are

$$


y_1(x) = e^{x}, \qquad y_2(x) = x e^{x}.


$$

We can use the method of variation of parameters if these solutions are independent. So, let's first compute the Wronskian:

$$


\begin{aligned}𝑊(𝑦_{1},𝑦_{2}) & =\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned} \\ & =𝑦_{1}𝑦_{′2}^{}−𝑦_{′1}^{}𝑦_{2} \\ & =(𝑒^{𝑥})(𝑥𝑒^{𝑥})^{′}−(𝑒^{𝑥})^{′}(𝑥𝑒^{𝑥}) \\ & =(𝑒^{𝑥})(𝑒^{𝑥}+𝑥𝑒^{𝑥})−(𝑒^{𝑥})(𝑥𝑒^{𝑥}) \\ & =𝑒^{2𝑥}+𝑥𝑒^{2𝑥}−𝑥𝑒^{2𝑥} \\ & =𝑒^{2𝑥}≠0\end{aligned}


$$

Since the Wronskian is not equal to zero, this confirms that the functions $y_1(x)$ and $y_2(x)$ are independent.

Now compute $u_1(x)$ and $u_2(x)$:

$$


\begin{aligned}𝑢_{1}(𝑥) & =−∫\frac{18𝑥𝑒^{𝑥}⋅𝑥𝑒^{𝑥}}{𝑒^{2𝑥}}\,𝑑𝑥 \\ & =−18∫𝑥^{2}\,𝑑𝑥 \\ & =−6𝑥^{3} \\ 𝑢_{2}(𝑥) & =∫\frac{18𝑥𝑒^{𝑥}⋅𝑒^{𝑥}}{𝑒^{2𝑥}}\,𝑑𝑥 \\ & =18∫𝑥\,𝑑𝑥 \\ & =9𝑥^{2}\end{aligned}


$$

Therefore, the particular solution is

$$


\begin{aligned}𝑦_{𝑝}(𝑥) & =𝑢_{1}𝑦_{1}+𝑢_{2}𝑦_{2} \\ & =(−6𝑥^{3})𝑒^{𝑥}+(9𝑥^{2})(𝑥𝑒^{𝑥}) \\ & =−6𝑥^{3}𝑒^{𝑥}+9𝑥^{3}𝑒^{𝑥} \\ & =3𝑥^{3}𝑒^{𝑥}.\end{aligned}


$$

The general solution is the sum of the complementary and particular solutions, and can be written as follows:

$$


\begin{aligned}𝑦(𝑥) & =𝑦_{𝑐}(𝑥)+𝑦_{𝑝}(𝑥) \\ & =𝐴𝑒^{𝑥}+𝐵𝑥𝑒^{𝑥}+\underset{𝑔(𝑥)}{\underset{}{3𝑥^{3}𝑒^{𝑥}}}\end{aligned}


$$

Therefore, we conclude that

$$


g(x) = 3x^3 e^{x}.


$$

### Example: Solving a Differential Equation Whose Characteristic Equation Has Complex Roots

#### Question

Consider the following differential equation

$$


y''+y=\tan{x}.


$$

The general solution to this equation can be written as

$$


y(x)=A\cos x + B\sin x + g(x),


$$

where $A$ and $B$ are constants. What could be the function $g(x)?$

**

$$


\int \tan x \sin x\,\textrm{d}x = -\sin x + \ln\!\left|\tan x+\sec x\right|


$$

#### Explanation

Suppose we have a second-order linear differential equation with linearly independent fundamental solutions $y_1(x)$ and $y_2(x).$ Then, according to the method of variation of parameters, we can seek a particular solution $y_p$ using the ansatz

$$


\begin{aligned}𝑦_{𝑝}(𝑥) & =𝑢_{1}(𝑥)𝑦_{1}(𝑥)+𝑢_{2}(𝑥)𝑦_{2}(𝑥),\end{aligned}


$$

where $u_1$ and $u_2$ satisfy the following system:

$$


\begin{aligned}𝑢_{′1}^{}𝑦_{′1}^{}+𝑢_{′2}^{}𝑦_{′2}^{}=𝑓(𝑥) \\ 𝑢_{′1}^{}𝑦_{1}+𝑢_{′2}^{}𝑦_{2}=0\end{aligned}


$$

The solution to this system is

$$


u_1(x)=-\displaystyle\int\dfrac{f(x)y_2(x)}{W(y_1,y_2)}\,\mathrm{d}x, \qquad u_2(x)=\displaystyle\int\dfrac{f(x)y_1(x)}{W(y_1,y_2)}\,\mathrm{d}x,


$$

where $W(y_1,y_2)$ is the Wronskian.

First, we note that the forcing term is $f(x)=\tan x.$

From the given information, we see that the complementary solution is

$$


y_c(x)=A\cos x + B\sin x.


$$

Therefore, the fundamental solutions to the corresponding homogeneous equation are

$$


y_1(x)=\cos x, \qquad y_2(x)=\sin x.


$$

We can use the method of variation of parameters if these solutions are linearly independent. So, let's first compute the Wronskian:

$$


\begin{aligned}𝑊(𝑦_{1},𝑦_{2}) & =\begin{aligned}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1}^{} & 𝑦_{′2}^{}\end{aligned} \\ & =𝑦_{1}(𝑥)𝑦_{′2}^{}(𝑥)−𝑦_{′1}^{}(𝑥)𝑦_{2}(𝑥) \\ & =(cos⁡𝑥)(sin⁡𝑥)^{′}−(cos⁡𝑥)^{′}(sin⁡𝑥) \\ & =(cos⁡𝑥)(cos⁡𝑥)−(−sin⁡𝑥)(sin⁡𝑥) \\ & =cos^{2}⁡𝑥+sin^{2}⁡𝑥 \\ & =1≠0\end{aligned}


$$

Since the Wronskian is not equal to zero, this confirms that the functions $y_1(x)$ and $y_2(x)$ are independent.

Let’s compute $u_1(x)$ and $u_2(x)$:

$$


\begin{aligned}𝑢_{1}(𝑥) & =−∫\frac{𝑓(𝑥)𝑦_{2}(𝑥)}{𝑊(𝑦_{1},𝑦_{2})}\,d𝑥 \\ & =−∫tan⁡𝑥sin⁡𝑥\,d𝑥 \\ & =sin⁡𝑥−ln\,|tan⁡𝑥+sec⁡𝑥| \\ 𝑢_{2}(𝑥) & =∫\frac{𝑓(𝑥)𝑦_{1}(𝑥)}{𝑊(𝑦_{1},𝑦_{2})}\,d𝑥 \\ & =∫tan⁡𝑥cos⁡𝑥\,d𝑥 \\ & =∫sin⁡𝑥\,d𝑥 \\ & =−cos⁡𝑥\end{aligned}


$$

Therefore, the particular solution is

$$


\begin{aligned}𝑦_{𝑝}(𝑥) & =𝑢_{1}𝑦_{1}+𝑢_{2}𝑦_{2} \\ & =(cos⁡𝑥)\,(sin⁡𝑥−ln\,|tan⁡𝑥+sec⁡𝑥|)+(−cos⁡𝑥)(sin⁡𝑥) \\ & =−cos⁡𝑥ln\,|tan⁡𝑥+sec⁡𝑥|.\end{aligned}


$$

The general solution is the sum of the complementary and particular solutions, and can be written as follows:

$$


\begin{aligned}𝑦(𝑥) & =𝑦_{𝑐}(𝑥)+𝑦_{𝑝}(𝑥) \\ & =𝐴cos⁡𝑥+𝐵sin⁡𝑥\,\,\underset{𝑔(𝑥)}{\underset{}{−\,cos⁡𝑥ln\,|tan⁡𝑥+sec⁡𝑥|}}\end{aligned}


$$

Therefore, we conclude that

$$


g(x)=-\cos x\ln\!\left|\tan x+\sec x\right|.


$$
