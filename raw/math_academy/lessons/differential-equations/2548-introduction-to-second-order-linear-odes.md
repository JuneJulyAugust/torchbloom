# Introduction to Second-Order Linear ODEs

Source: https://www.mathacademy.com/topics/2548?courseId=61
Topic ID: 2548

## Prerequisites

- [Introduction to First-Order Linear ODEs](./906-introduction-to-first-order-linear-odes.md)
- [Linear Differential Operators](./6707-linear-differential-operators.md)

## Lesson

### Introduction

A second-order ordinary differential equation in the variable $y(x)$ is **linear** if it can be written in the form

$$


a(x)y'' + b(x)y' + c(x) y = f(x)


$$

where

- $a(x),$ $b(x),$ $c(x),$ and $f(x)$ are functions of $x$ only, and

- $a(x)\neq 0$ on the interval under consideration.

For example, the equation

$$


e^x y'' + 3xy' + \cos (x)y = 0


$$

is a second-order linear ODE with

$$


a(x)=e^x, \qquad b(x)=3x, \qquad c(x)=\cos(x), \qquad f(x)=0.


$$

On the other hand, the equation

$$


{\color{red}y^2} y'' + x{\color{red}y}y' + 2y = 0


$$

is **nonlinear**. The coefficient of $y''$ is $y^2$ and the coefficient of $y'$ is $xy$. Since these coefficients depend on $y$, they are not functions of $x$ only, violating the definition of a linear equation.

### Differential Operators Revisited

Every linear ODE can be written in the form

$$


L(y) = f(x),


$$

where $L$ is a **linear differential operator**. This operator notation helps us to study the properties of linear ODEs in a more general way.

In this topic, we'll primarily concern ourselves with **second-order linear ODEs**. For these equations, the operator $L$ has the general form:

$$


L = a(x)\dfrac{\textrm d^2}{\textrm d x^2} + b(x)\dfrac{\textrm d}{\textrm d x} + c(x).


$$

For example, consider the second-order linear ODE:

$$


x^2 y'' - 2x y' + 2y = \ln x.


$$

We can write this as $L(y) = f(x)$, where the linear operator $L$ and the function $f(x)$ are:

$$


L = x^2\dfrac{\textrm d^2}{\textrm d x^2} - 2x\dfrac{\textrm d}{\textrm d x} + 2 \quad \text{and} \quad f(x) = \ln x.


$$

Applying this operator to a function $y$ gives back the left-hand side of the ODE:

$$


L(y) = \left(x^2\dfrac{\textrm d^2}{\textrm d x^2} - 2x\dfrac{\textrm d}{\textrm d x} + 2\right)y = x^2y''-2xy'+2y.


$$

### Example: Identifying Second-Order Linear ODEs

#### Question

Which of the following second-order differential equations are linear?

1. $y'' + (y-1)y'+x = 2$

2. $y''+y'=x \cos x$

3. $yy'' - y'+ 9 = 0$

#### Explanation

A second-order linear differential equation has the form

$$


a(x)y'' + b(x)y' + c(x) y = f(x).


$$

Let's look at each equation in turn.

- The equation is **** linear because it contains the nonlinear term $(y-1)y'.$

- The equation is a second-order linear ODE with $a(x) = 1, b(x) = 1, c(x) = 0,$ and $f(x) = x\cos{x}.$

- The equation is **** linear because it contains the nonlinear term $yy''.$

Therefore, the correct answer is "II only."

### Second-Order Homogeneous ODEs

A second-order linear ODE

$$


a(x)y'' + b(x)y' + c(x) y = f(x)


$$

is called **homogeneous** if $f(x) = 0$ for all $x.$

A second-order linear ODE is **inhomogeneous** if it is not homogeneous. Note that the words homogeneous and inhomogeneous are associated *only* with linear equations.

Let's look at some examples.

- Consider the second-order linear ODE Comparing this equation with the general form, we see that Since the right-hand side $f(x) = 0$ for all $x,$ this equation is *homogeneous*.

- Next, consider the following second-order linear ODE. To compare this with the general form, we can write it as We can now see that Since the right-hand side $f(x) = \sin x,$ which is not identical to zero, this equation is *inhomogeneous*.

### Example: Identifying Second-Order Homogeneous ODEs

#### Question

Determine which of the following second-order ODEs are homogeneous, and which are inhomogeneous.

1. $\, (2-\sin(x)) y'' + x y' + y = 0$

2. $\,y'' + 6y' + 9y = 3e^x$

3. $\,y'' + x^3 y - 8 = 0$

#### Explanation

Suppose we have a second-order linear ODE given in the form

$$


a(x)y'' + b(x)y' + c(x) y = f(x).


$$

The equation is homogeneous if $f(x) = 0$ for all $x.$ If it is not homogeneous, then it is inhomogeneous.

With that in mind, let's examine each option.

- The equation is homogeneous since, for the right-hand side, we have $f(x) = 0$ for all $x.$

- The equation is inhomogeneous since, for the right-hand side, we have $f(x) = 3e^x,$ which is different from zero.

- Writing the equation in the form $ay'' + by' + cy = f,$ we have This equation is inhomogeneous since, for the right-hand side, we have $f(x) = 8,$ which is different from zero.

### The Associated Homogeneous Equation of a Second-Order Inhomogeneous ODE

Suppose we have a second-order **inhomogeneous** ODE given in the form

$$


a(x)y'' + b(x)y' + c(x) y = f(x).


$$

The **associated** (or **corresponding**) **homogeneous equation** is constructed by replacing the term $f(x)$ with zero:

$$


a(x)y'' + b(x)y' + c(x) y = 0


$$

For example, consider the following inhomogeneous ODE:

$$


\underbrace{x^2 y'' + (x+1)y' + \sin(x)y = \color{blue}3e^x}_{\text{Inhomogeneous Equation}}


$$

To get the associated homogeneous equation, we replace the right-hand side with $0.$

$$


\underbrace{x^2 y'' + (x+1)y' + \sin(x)y = \color{blue}0}_{\text{Associated Homogeneous Equation}}


$$

### Example: Identifying the Associated Homogeneous Equation of a Second-Order Inhomogeneous ODE

#### Question

For the differential equation $2xy'' +y' - y = \cos x,$ what is the associated homogeneous equation?

#### Explanation

Suppose we have a second-order inhomogeneous ODE given in the form

$$


a(x)y'' + b(x)y' + c(x) y = f(x).


$$

The associated homogeneous equation is constructed by replacing $f(x)$ with zero:

$$


a(x)y'' + b(x)y' + c(x) y = 0


$$

Therefore, in our case, the associated homogeneous equation is

$$


2xy'' +y' - y = 0.


$$

### Initial Value Problems

If a second-order differential equation for the function $y(x)$ is given with two conditions specified at the *same* location in the domain of $y,$ then this is an **initial value problem.**

For example, the following system is an initial value problem because it has two conditions that are both specified at the same location $x=2\mathbin{:}$

$$


y'' + xy' + e^x y = 1, \qquad y(2) = 3, \quad y'(2) = 5


$$

On the other hand, if the two conditions are specified at *different* locations in the domain of $y,$ then this is a **boundary value problem.**

For example, the following system is a boundary value problem because it has two conditions that are specified at *different* locations, $x=2$ and $x=7\mathbin{:}$

$$


y'' + xy' + e^x y = 1, \qquad y'(2) = 3, \quad y(7) = 5


$$

In either case, precisely two conditions must be specified. The following systems are neither initial value problems nor boundary value problems:

- The following system does not have any conditions:

- The following system only has one condition:

In this topic, we'll concern ourselves only with initial value problems. We'll discuss boundary value problems in separate lessons.

### Example: Identifying Second-Order Initial Value Problems

#### Question

Which of the following systems is an initial value problem?

1. $x^2y'' + xy' = x+2$

2. $9y'' + 4y = e^x, \quad y(0) = 1, \quad y'(4)= 1$

3. $y''+xy'+x^2y= \sin x, \quad y(1) = 0, \quad y'(1)= 5$

#### Explanation

If a second-order differential equation for the function $y(x)$ is given with two conditions specified at the ** location in the domain of $y,$ then this is an ****

With this in mind, let's go through each equation in turn.

- System I is not an initial value problem. It contains an equation only. No conditions are specified.

- System II is not an initial value problem because it consists of a differential equation together with two conditions in ** locations, $x=0$ and $x=4.$ So this is a ****, not an initial value problem.

- System III is an initial value problem. The differential equation is together with two conditions at the same location in the domain of $y(x)$ (i.e., at $x=1$).

Therefore, the correct answer is "III only".
