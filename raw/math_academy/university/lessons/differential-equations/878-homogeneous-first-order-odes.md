# Homogeneous First-Order ODEs

Source: https://www.mathacademy.com/topics/878?courseId=61
Topic ID: 878

## Prerequisites

- [Solving First-Order ODEs Using Separation of Variables](./466-solving-first-order-odes-using-separation-of-variables.md)
- [Introduction to First-Order Linear ODEs](./906-introduction-to-first-order-linear-odes.md)
- [Homogeneous Functions](./2536-homogeneous-functions.md)

## Lesson

### Introduction

If we're given a differential equation of the form

$$


\dfrac{\textrm d y}{\textrm d x} = f(x,y),


$$

and the right-hand side is a **homogeneous function of degree zero**, meaning that it satisfies

$$


f(tx,ty) = f(x,y),


$$

then we say that the differential equation is a **homogeneous differential equation**.

For instance, let's take a look at the following differential equation:

$$


\dfrac{\textrm d y}{\textrm d x} = \dfrac{x^2-y^2}{x^2+y^2}


$$

This differential equation is homogeneous. Here's why:

- Both the numerator and denominator of the function on the right-hand side are homogeneous polynomials of degree $2.$

- So, the rational function on the right-hand side is a homogeneous function of degree $2-2 = 0.$

- Since the right-hand side is a homogeneous function of degree $0,$ the differential equation is homogeneous.

By contrast, the equation

$$


\dfrac{\textrm d y}{\textrm d x} = \dfrac{x^3-y^3}{x^2+y^2}


$$

is *not* a homogeneous differential equation. Although the function on the right-hand side is homogeneous, its degree is $1,$ not zero.

**Watch out!** In this context, the word homogeneous refers only to the function $f(x,y)$ being a homogeneous function of degree zero. It does *not* mean the same thing as a homogeneous linear differential equation (such as one with zero forcing term). These are completely different uses of the word homogeneous, even though they share the same name.

A differential equation can be homogeneous in this sense without being linear, and a linear differential equation can be homogeneous without being homogeneous in this sense. Always check which definition is being used.

### Example: Identifying Homogeneous Differential Equations

#### Question

Which of the following differential equations are homogeneous?

1. $\dfrac{\textrm d y}{\textrm d x} = \dfrac{y}{x}$

2. $\dfrac{\textrm d y}{\textrm d x} = \dfrac{y}{x^2}$

3. $\dfrac{\textrm d y}{\textrm d x} = \dfrac{y}{2x}\sin{\left(\dfrac{x^2}{y^2}\right)}$

#### Explanation

A first-order ordinary differential equation that is written in the form

$$


\dfrac {\text{d}y} {\text{d}x} = f(x, y)


$$

is said to be homogeneous if $f(x,y)$ is a homogeneous function of degree zero, meaning that it satisfies

$$


f(tx, ty) = f(x, y).


$$

With that in mind, let's take a look at the right-hand side function in each differential equation.

- The function $f(x,y) = \dfrac{y}{x}$ is a homogeneous function of degree zero: Therefore, equation I is a homogenous differential equation.

- The function $f(x,y) = \dfrac{y}{x^2}$ is ** a homogeneous function of degree $0.$ Rather, it is a homogeneous function of degree $-1\mathbin{:}$ Therefore, equation II is ** a homogenous differential equation.

- The function $f(x,y) = \dfrac{y}{2x}\sin{\left(\dfrac{x^2}{y^2}\right)}$ is a homogeneous function of degree zero: Therefore, equation III is a homogenous differential equation.

In conclusion, the correct answer is "I and III only."

### Solving a Homogeneous Differential Equation

Consider the homogeneous differential equation

$$


\frac{\text{d}y}{\text{d}x} = \dfrac{x+y}{x} \,.


$$

This differential equation cannot be solved using separation of variables. So, how can we solve it?

Given any homogeneous differential equation, if we substitute $y=vx$ where $v=v(x)$ is a function of $x,$ then we can transform the differential equation into one that is separable.

Differentiating the substitution $y=vx,$ we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =𝑥\frac{d𝑣}{d𝑥}+𝑣\frac{d}{d𝑥}(𝑥) \\ & =𝑥\frac{d𝑣}{d𝑥}+𝑣\,.\end{aligned}


$$

Now, substituting into the original differential equation gives

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{𝑥+𝑦}{𝑥} \\ 𝑥\frac{d𝑣}{d𝑥}+𝑣 & =\frac{𝑥+𝑣𝑥}{𝑥} \\ 𝑥\frac{d𝑣}{d𝑥}+𝑣 & =1+𝑣 \\ \frac{d𝑣}{d𝑥} & =\frac{1}{𝑥}\,.\end{aligned}


$$

The differential equation above is separable! We can solve it by integrating both sides with respect to $x\mathbin{:}$

$$


\begin{aligned}∫\frac{d𝑣}{d𝑥}d𝑥 & =∫\frac{1}{𝑥}\,d𝑥 \\ 𝑣 & =ln⁡|𝑥|+𝐶\end{aligned}


$$

Finally, substituting $y=v x$ we obtain the solution to the original differential equation as

$$


\begin{aligned}𝑦 & =𝑣𝑥 \\ & =(ln⁡|𝑥|+𝐶)𝑥 \\ & =𝑥ln⁡|𝑥|+𝐶𝑥\,.\end{aligned}


$$

### Example: Transforming a Homogeneous Differential Equation into a Separable Equation Using a Substitution

#### Question

Use the transformation $y = vx$ (where $v=v(x)$) to rewrite the given first-order homogeneous ODE

$$


\dfrac {\text{d}y} {\text{d}x} = \cos \left( \frac {y} {x} \right)


$$

as a separable ODE in $v$ and $x.$

#### Explanation

With $y = vx$ (where $v = v(x)$), we have

$$


\begin{aligned}\frac{d𝑦}{d𝑥}=𝑥\frac{d𝑣}{d𝑥}+𝑣\,.\end{aligned}


$$

Plugging that into the differential equation and separating variables, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =cos⁡(\frac{𝑦}{𝑥}) \\ 𝑥\frac{d𝑣}{d𝑥}+𝑣 & =cos⁡(𝑣) \\ 𝑥\frac{d𝑣}{d𝑥} & =cos⁡(𝑣)−𝑣 \\ (\frac{1}{cos⁡(𝑣)−𝑣})\frac{d𝑣}{d𝑥} & =\frac{1}{𝑥}\,.\end{aligned}


$$

### Example: Solving a Homogeneous Differential Equation

#### Question

Find the general solution to the equation

#### Explanation

We note that this equation is a homogeneous first-order differential equation because

The given equation is not separable, but we can transform it into a separable equation by carrying out the substitution

Carrying out the substitution and separating variables, we have

Integrating both sides, we get where (with) and

Finally, substituting and simplifying, we get where Therefore, the general solution is

### Proof That Homogeneous First-Order Differential Equations Can Always Be Made Separable

Given any homogeneous first-order ordinary differential equation, we can always transform it into a separable equation through the substitution $y=vx,$ where $v=v(x)$ is a function of $x.$

To understand why, suppose we have a homogeneous first-order ordinary differential equation

$$


\dfrac {\text{d}y} {\text{d}x} = f(x, y).


$$

Then because $f$ is homogeneous of degree zero, we have

$$


f(tx, ty) = f(x, y)


$$

for any $t.$ By letting $t=\dfrac{1}{x},$ we get

$$


\begin{aligned}𝑓(𝑥,𝑦) & =𝑓(𝑡𝑥,𝑡𝑦) \\ & =𝑓(\frac{1}{𝑥}⋅𝑥,\frac{1}{𝑥}⋅𝑦) \\ & =𝑓(1,\frac{𝑦}{𝑥}) \\ & =𝐹(\frac{𝑦}{𝑥})\end{aligned}


$$

where the function $F$ is defined as $F(v) = f(1,v).$

Now, letting $v = \dfrac{y}{x}$ (or equivalently, $y=vx$), we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =𝐹(\frac{𝑦}{𝑥}) \\ \frac{d}{d𝑥}(𝑣𝑥) & =𝐹(𝑣) \\ 𝑣+𝑥\frac{d𝑣}{d𝑥} & =𝐹(𝑣).\end{aligned}


$$

This differential equation is now separable! We can separate the variables as follows:

$$


\begin{aligned}𝑥\frac{d𝑣}{d𝑥} & =𝐹(𝑣)−𝑣 \\ \frac{1}{𝐹(𝑣)−𝑣}\frac{d𝑣}{d𝑥} & =\frac{1}{𝑥}\end{aligned}


$$
