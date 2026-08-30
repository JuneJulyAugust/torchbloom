# Introduction to Differential Equations

Source: https://www.mathacademy.com/topics/3215?courseId=24
Topic ID: 3215

## Prerequisites

- [Second and Higher-Order Derivatives](./281-second-and-higher-order-derivatives.md)

## Lesson

### Introduction

An **ordinary differential equation** is an equation that involves a function with one variable (usually denoted as $y$), its derivatives, and an independent variable (usually denoted as $x$).

For example,

$$


\dfrac{\textrm{d}^2y}{\textrm{d}x^2}-3xy^2 = y^2\dfrac{\textrm{d}y}{\textrm{d}x}


$$

is an ordinary differential equation (ODE).

**Watch out!** Here, the function $y=y(x)$ actually depends on the independent variable $x.$

The **order of an ordinary differential equation** is the order of the highest derivative in the equation.

In our example above, the highest derivative is

$$


\dfrac{\textrm{d}^2y}{\textrm{d}x^2},


$$

which has order $2.$ Therefore, the order of the ODE is $2.$

### Example: Identifying the Order of an Ordinary Differential Equation

#### Question

What is the order of the ordinary differential equation $2x\dfrac{\textrm{d}^3y}{\textrm{d}x^3}+y^2\dfrac{\textrm{d}^2y}{\textrm{d}x^2}=3x^2?$

#### Explanation

The order of an ordinary differential equation (ODE) is the order of the highest derivative in the equation.

The highest derivative in the given ODE is $\dfrac{\textrm{d}^3y}{\textrm{d}x^3},$ which has order $3.$

Therefore, the order of the ODE is $3.$

### Autonomous Ordinary Differential Equations

An ordinary differential equation with dependent variable $y$ and independent variable $x$ is said to be **autonomous** if it can be written in the form

$$


\dfrac{\textrm{d}y}{\textrm{d}x}=f(y),


$$

or equivalently,

$$


y'=f(y).


$$

For example,

$$


\dfrac{\textrm{d}y}{\textrm{d}x} = -5y^2


$$

is autonomous, while the equation

$$


y' = \dfrac{y+2}{x^2}


$$

is *not* autonomous since the expression for $y'$ on the right-hand side contains the independent variable $x$ explicitly, outside the function $y=y(x).$

### Example: Determining Whether an Ordinary Differential Equation is Autonomous or Nonautonomous

#### Question

Which of the following are autonomous ordinary differential equations?

1. $\dfrac{\textrm{d}y}{\textrm{d}x}=y^3$

2. $x\dfrac{\textrm{d}y}{\textrm{d}x}- y^3=2$

3. $\dfrac{\textrm{d}y}{\textrm{d}x}-3\sqrt{y}=1$

#### Explanation

An ordinary differential equation with dependent variable $y$ and independent variable $x$ is said to be autonomous if it can be written in the form $\dfrac{\textrm{d}y}{\textrm{d}x}=f(y),$ or equivalently, $y'=f(y).$

With that in mind, let's check each of the differential equations:

- Equation I is an autonomous differential equation. We see that it is of the form $\dfrac{\textrm{d}y}{\textrm{d}x}=f(y),$ where $f(y)= y^3.$

- Equation II is not an autonomous differential equation. If we isolate the derivative term, we get where $f(x,y)= \dfrac{y^3+2}{x}.$ So, it is not possible to write the equation in the form $\dfrac{\textrm{d}y}{\textrm{d}x}=f(y).$

- Equation III is an autonomous differential equation. Writing the equation in the form $\dfrac{\textrm{d}y}{\textrm{d}x}=f(y),$ we get where $f(y)= 1+3\sqrt{y}.$

Therefore, the correct answer is "I and III only."

### First-Order Initial Value Problems

A first-order **initial value problem** (or IVP) is a first-order ordinary differential equation together with an initial condition that specifies a value of the unknown function at a point in its domain. A first-order initial value problem typically takes the form

$$


y' = f(x,y), \qquad y(x_0) = y_0,


$$

where $x_0$ and $y_0$ are constants.

For example,

$$


{\color{blue}x(2x^2-y') = -1}, \qquad {\color{red}y(e)=-2}


$$

is a first-order initial value problem. It consists of a first-order differential equation

$$


{\color{blue}x(2x^2-y') = -1}


$$

together with the initial condition

$$


{\color{red} y(e)=-2}.


$$

### Example: Initial Value Problems and Initial Conditions

#### Question

Which of the following systems is a first-order initial value problem?

1. $x^2-3y' = y^3, \quad y(1)=6$

2. $x^3y'-e^x= \sqrt{y}, \quad y(2)=e$

3. $2y'' - \dfrac{x}{2} = 3y', \quad y(2)=3, \quad y'(2) = 2$

#### Explanation

A first-order initial value problem (or IVP) is a first-order ordinary differential equation together with an initial condition that specifies a value of the unknown function at a point in its domain. A first-order initial value problem typically takes the form

$$


y' = f(x,y), \quad y(x_0) = y_0,


$$

where $x_0$ and $y_0$ are constants.

With that in mind, let's check each option.

- System I is a first-order initial value problem. It consists of a first-order differential equation $x^2-3y' = y^3$ together with the initial condition $y(1)=6.$

- System II is also a first-order initial value problem. It consists of a first-order differential equation $x^3y'-e^x= \sqrt{y}$ together with the initial condition $y(2)=e.$

- System III is not a first-order initial value problem. It consists of a **-order differential equation $2y'' - \dfrac{x}{2} = 3y'$ together with ** initial conditions $y(2)=3,\, y'(2) = 2.$ This is a second-order initial value problem.

Therefore, the correct answer is "I and II only."
