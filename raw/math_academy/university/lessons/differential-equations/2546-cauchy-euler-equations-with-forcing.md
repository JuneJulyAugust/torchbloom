# Cauchy-Euler Equations With Forcing

Source: https://www.mathacademy.com/topics/2546?courseId=61
Topic ID: 2546

## Prerequisites

- [Second-Order Inhomogeneous ODEs With Polynomial Forcing](./881-second-order-inhomogeneous-odes-with-polynomial-forcing.md)
- [Second-Order Inhomogeneous ODEs With Exponential Forcing](./882-second-order-inhomogeneous-odes-with-exponential-forcing.md)
- [Second-Order Inhomogeneous ODEs With Sinusoidal Forcing](./883-second-order-inhomogeneous-odes-with-sinusoidal-forcing.md)
- [Cauchy-Euler Equations: Characteristic Equations With Repeated Roots](./2544-cauchy-euler-equations-characteristic-equations-with-repeated-roots.md)
- [Cauchy-Euler Equations: Characteristic Equations With Complex Roots](./2545-cauchy-euler-equations-characteristic-equations-with-complex-roots.md)
- [Solving Second-Order ODEs Using Variation of Parameters](./6704-solving-second-order-odes-using-variation-of-parameters.md)

## Lesson

### Introduction

A Cauchy-Euler equation with forcing takes the form

$$


ax^2y''+bxy'+cy=f(x),


$$

where $a,b,$ and $c$ are constants and $f(x)$ is a nonzero function. If $f(x)$ is a polynomial, then we say that the Cauchy-Euler equation experiences polynomial forcing.

To find the particular solution to a Cauchy-Euler equation with polynomial forcing, we assume that the terms of a particular solution are proportional to the terms of $f.$

For example, to find a particular solution to the equation

$$


ax^2y''+bxy'+cy=2x^3 - 5x,


$$

where $f(x) = 2x^3 - 5x,$ we would assume that a particular solution takes the form

$$


y_p(x) = \alpha x^3 + \beta x.


$$

In other words, we just have to replace the coefficients of $f(x)$ with unknown constants and then solve for those unknown constants.

**Caution:** This method only works for Cauchy-Euler equations with *polynomial* forcing. Later, we will see how to solve Cauchy-Euler equations with other types of forcing.

### Example: Calculating a Particular Solution For a Cauchy-Euler Equation with Forcing

#### Question

Given that the differential equation

$$


t^2 y'' - 4ty' + 6y = 2t+6, \quad t > 0


$$

has the complementary solution $y_c(t) = At^3 + Bt^2,$ find the particular solution $y_p(t)$ to this equation.

#### Explanation

The right-hand side of the inhomogeneous equation is $2t+6.$ Therefore, we assume that the particular solution is of the form

$$


y_p(t) = \alpha t + \beta


$$

where $\alpha$ and $\beta$ are constants that are to be determined.

Calculating the first and second derivatives of $y_p$ gives

$$


y_p' = \alpha, \qquad y_p'' = 0.


$$

To find the values of $\alpha$ and $\beta,$ we substitute the derivatives into the differential equation and group the terms on the left-hand side:

$$


\begin{aligned}𝑡^{2}(0)−4𝑡(𝛼)+6(𝛼𝑡+𝛽) & =2𝑡+6 \\ (−4𝛼+6𝛼)𝑡+6𝛽 & =2𝑡+6 \\ 2𝛼𝑡+6𝛽 & =2𝑡+6\end{aligned}


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{matrix}2𝛼=2\, & (equating the coefficients of\,\,𝑡) \\ 6𝛽=6\, & (equating the constants)\end{matrix}\end{aligned}


$$

Solving this system gives $\alpha = 1$ and $\beta =1.$

Therefore, the particular solution $y_p(t)$ is

$$


y_p(t) = t + 1.


$$

### Example: Solving a Cauchy-Euler Equation With Forcing

#### Question

Find the general solution to the equation

$$


x^2 y'' + xy' - y = 3x^2, \quad x>0.


$$

#### Explanation

First, we need to find the complimentary function $y_c(x)$ which is the solution to the homogeneous equation

$$


x^2y'' + xy' - y = 0.


$$

Let $y=x^\lambda.$ Differentiating $y$ with respect to $x$ gives

$$


y' = \lambda x^{\lambda -1}, \qquad y'' = \lambda(\lambda-1)x^{\lambda-2}.


$$

Substituting the above to our differential equation gives

$$


\begin{aligned}𝑥^{2}⋅𝜆(𝜆−1)𝑥^{𝜆−2}+𝑥⋅𝜆𝑥^{𝜆−1}−𝑥^{𝜆} & =0 \\ 𝜆(𝜆−1)𝑥^{𝜆}+𝜆𝑥^{𝜆}−𝑥^{𝜆} & =0 \\ 𝑥^{𝜆}[𝜆(𝜆−1)+𝜆−1] & =0.\end{aligned}


$$

Therefore, the characteristic equation is

$$


\begin{aligned}𝜆(𝜆−1)+𝜆−1 & =0 \\ 𝜆^{2}−1 & =0 \\ (𝜆+1)(𝜆−1) & =0.\end{aligned}


$$

The roots of the characteristic equation are $\lambda = -1$ and $\lambda = 1.$ Therefore, the complementary solution $y_c(x)$ is

$$


y_c(x) = \dfrac{c_1}{x}+ c_2 x.


$$

Now, we find the particular solution. The right-hand side of the inhomogeneous equation $(3x^2)$ contains only an $x^2$ term, so we assume that the particular solution is also of the form

$$


y_p(x) = \alpha x^2


$$

where $\alpha$ is a constant that is to be determined.

Calculating the first and second derivatives of $y_p$ gives

$$


\frac{\text{d}y_p}{\text{d}x} =2 \alpha x, \qquad \frac{\text{d}^2y_p}{\text{d}x^2} = 2 \alpha .


$$

To find the value of $\alpha,$ we substitute the derivatives into the differential equation and group the terms on the left-hand side:

$$


\begin{aligned}𝑥^{2}(2𝛼)+𝑥(2𝛼𝑥)−𝛼𝑥^{2} & =3𝑥^{2} \\ (2𝛼+2𝛼−𝛼)𝑥^{2} & =3𝑥^{2} \\ 3𝛼𝑥 & =3𝑥^{2}\end{aligned}


$$

Equating the coefficients, we get $\alpha = 1.$

Therefore, the particular solution is

$$


y_p(x) =x^2,


$$

and the general solution is

$$


\begin{aligned}𝑦(𝑥) & =𝑦_{𝑐}(𝑥)+𝑦_{𝑝}(𝑥) \\ & =\frac{𝑐_{1}}{𝑥}+𝑐_{2}𝑥+𝑥^{2}.\end{aligned}


$$

### Solving a Cauchy-Euler Equation Using Variation of Parameters

To solve a Cauchy-Euler equation with non-polynomial forcing, we need to use other techniques.

Another technique that we can use is variation of parameters. If we know two fundamental solutions to a Cauchy-Euler equation, then we can use variation of parameters to find a particular solution.

Note that, in order to use variation of parameters, we must reduce our Cauchy-Euler equation to the form

$$


y'' + P(t) y' +Q(t) y = f(t)


$$

We can do this by dividing by the coefficient of the $y''$ term. Let's see an example of this.

### Example: Calculating a Particular Solution For a Cauchy-Euler Equation Using Variation of Parameters

#### Question

Given that the differential equation

$$


t^2 y'' +2ty' = t^2 e ^ {t}, \quad t>0


$$

has the complementary solution $y_c(t) = \dfrac{A}{t} + B,$ find the particular solution $y_p(t)$ to this equation.

#### Explanation

The right-hand side is not a polynomial, so we need to use another solution technique. Here, we are given the complementary solution $y_c(t) = \dfrac{A}{t} + B,$ which means that we have two fundamental solutions

$$


y_1(t) = \dfrac{1}{t} , \qquad y_2(t) = 1.


$$

Because we have two fundamental solutions, we can use variation of parameters.

To use variation of parameters, we must first reduce the differential equation to the form

$$


y'' + P(t) y' +Q(t) y = f(t).


$$

To do this, we divide both sides of the given equation by $t^2,$ and get

$$


y'' + \dfrac{2}{t}y' = e ^ {t}.


$$

So, we have the following:

$$


y_1(t) = \dfrac{1}{t} , \qquad y_2(t) = 1, \qquad f(t) = e^t.


$$

First, let's compute the Wronskian:

$$


\begin{aligned}𝑊(𝑦_{1},𝑦_{2}) & =\begin{matrix}𝑦_{1} & 𝑦_{2} \\ 𝑦_{′1} & 𝑦_{′2}\end{matrix} \\ & =𝑦_{1}𝑦_{′2}−𝑦_{′1}𝑦_{2} \\ & =(\frac{1}{𝑡})(1)^{′}−(\frac{1}{𝑡})^{′}(1) \\ & =0+\frac{1}{𝑡^{2}} \\ & =\frac{1}{𝑡^{2}}\end{aligned}


$$

Since the Wronskian is not equal to zero, this confirms that the functions $y_1(t)$ and $y_2(t)$ are independent.

According to the method of variation of parameters, a particular solution of the differential equation is

$$


\begin{aligned}𝑦_{𝑝}(𝑡) & =𝑦_{1}(𝑡)𝑢(𝑡)+𝑦_{2}(𝑡)𝑣(𝑡),\end{aligned}


$$

where

$$


\begin{aligned}𝑢(𝑡) & =−∫\frac{𝑓(𝑡)𝑦_{2}(𝑡)}{𝑊(𝑦_{1},𝑦_{2})}\,d𝑡=−∫𝑡^{2}𝑒^{𝑡}=−(𝑡^{2}−2𝑡+2)𝑒^{𝑡}, \\ 𝑣(𝑡) & =∫\frac{𝑓(𝑡)𝑦_{1}(𝑡)}{𝑊(𝑦_{1},𝑦_{2})}\,d𝑡=∫𝑡𝑒^{𝑡}=(𝑡−1)𝑒^{𝑡}.\end{aligned}


$$

Therefore, a particular solution is given by

$$


\begin{aligned}𝑦_{𝑝}(𝑡) & =𝑦_{1}(𝑡)𝑢(𝑡)+𝑦_{2}(𝑡)𝑣(𝑡) \\ & =−\frac{(𝑡^{2}−2𝑡+2)𝑒^{𝑡}}{𝑡}+(𝑡−1)𝑒^{𝑡} \\ & =(1−\frac{2}{𝑡})𝑒^{𝑡}.\end{aligned}


$$

### Solving a Cauchy-Euler Equation Using a Substitution

If we need to solve a Cauchy-Euler equation with non-polynomial forcing, but we are not given two fundamental solutions, we cannot use variation of parameters.

However, if we make a substitution $x=e^t,$ we can transform the Cauchy-Euler equation into a linear ODE with constant coefficients.

We can then solve the linear ODE in terms of $u$ using the usual methods, and then back-substitute $t = \ln x$ to write the final solution in terms of $x.$

Let's see an example of this.

### Example: Solving a Cauchy-Euler Equation Using a Substitution

#### Question

Find the particular solution $y_p(x)$ of the equation

$$


x^2y''+xy' + y = \ln x, \quad x>0.


$$

#### Explanation

This Cauchy-Euler equation has non-polynomial forcing, but we are not given two fundamental solutions, so we cannot use variation of parameters.

However, if we make a substitution $x=e^t,$ we can transform the Cauchy-Euler equation into a linear ODE with constant coefficients.

Letting $x=e^t,$ we note that

$$


\dfrac{\textrm dx}{\textrm d t} = e^t = x\quad\Longrightarrow\quad \dfrac{\textrm d t}{\textrm d x} = \dfrac1x.


$$

Then, we use the chain rule to compute the first and second derivatives.

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d𝑦}{d𝑡}\frac{d𝑡}{d𝑥}=\frac{1}{𝑥}\frac{d𝑦}{d𝑡}, \\ \frac{d^{2}𝑦}{d𝑥^{2}} & =\frac{d}{d𝑥}(\frac{1}{𝑥}\frac{d𝑦}{d𝑡}) \\ & =\underset{product rule}{\underset{}{\frac{d}{d𝑥}(\frac{1}{𝑥})⋅\frac{d𝑦}{d𝑡}+\frac{1}{𝑥}⋅\frac{d}{d𝑥}(\frac{d𝑦}{d𝑡})}} \\ & =−\frac{1}{𝑥^{2}}\frac{d𝑦}{d𝑡}+\frac{1}{𝑥}⋅\underset{chain rule}{\underset{}{\frac{d𝑡}{d𝑥}\frac{d}{d𝑡}}}(\frac{d𝑦}{d𝑡}) \\ & =−\frac{1}{𝑥^{2}}\frac{d𝑦}{d𝑡}+\frac{1}{𝑥^{2}}\frac{d^{2}𝑦}{d𝑡^{2}} \\ & =\frac{1}{𝑥^{2}}\frac{d^{2}𝑦}{d𝑡^{2}}−\frac{1}{𝑥^{2}}\frac{d𝑦}{d𝑡}\end{aligned}


$$

Substituting the above to our differential equation gives

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑡^{2}}+𝑦=𝑡.\end{aligned}


$$

This equation is a second-order inhomogeneous ODE equation with constant coefficients and polynomial forcing.

Using the usual methods for solving second-order ODEs, we find that the complementary solution is

$$


y_c(x) = A\cos t+B\sin t.


$$

Since right-hand side of the inhomogeneous ODE is a polynomial of degree $1,$ we assume that the particular solution is also a polynomial of degree $1,$ i.e.

$$


y_p(t)=\alpha t+ \beta


$$

where $\alpha$ and $\beta$ are constants that are to be determined.

Calculating the first and second derivatives of $y_p$ gives:

$$


\frac{\text{d}y_p}{\text{d}t} = \alpha ,\qquad \frac{\text{d}^2y_p}{\text{d}t^2} = 0.


$$

To find the values of $\alpha$ and $\beta,$ we substitute the derivatives into the differential equation for $y(t)\mathbin{:}$

$$


0+(\alpha t+\beta)=t


$$

Equating the coefficients, we get the following system of equations:

$$


\begin{aligned}\begin{matrix}𝛼=1\, & (equating the coefficients of t) \\ 𝛽=0\, & (equating the constants)\end{matrix}\end{aligned}


$$

This system has the solution $\alpha=1$ and $\beta=0.$

Therefore, the particular solution is

$$


y_p(t) = t.


$$

Now, all that remains is to write the above solution in terms of the original variable $x.$ Since $x=e^t,$ we have $t = \ln x,$ and therefore

$$


y_p(x) =\ln x.


$$
