# Solving Exact ODEs Using Integrating Factors

Source: https://www.mathacademy.com/topics/6353?courseId=61
Topic ID: 6353

## Prerequisites

- [Exact Differential Equations](./2521-exact-differential-equations.md)

## Lesson

### Introduction

Sometimes, we might be asked to analyze a first-order ODE expressed in differential form:

$$


M(x,y)\,\textrm{d}x + N(x,y)\,\textrm{d}y = 0


$$

Recall that an equation in differential form is *exact* if it satisfies the exactness test, given by

$$


\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}.


$$

If an equation in differential form is not exact, then it's **inexact.**

Now, suppose we have the *inexact* equation

$$


P(x,y)\,\textrm{d}x + Q(x,y)\,\textrm{d}y = 0.


$$

Sometimes, inexact equations can be converted into exact equations by multiplying them by a special function $I(x,y),$ called an **integrating factor**.

Let's assume that such a function $I(x,y)$ exists. Multiplying our equation by $I(x,y),$ we get

$$


\begin{aligned}𝐼(𝑥,𝑦)⋅[𝑃(𝑥,𝑦)\,d𝑥+𝑄(𝑥,𝑦)\,d𝑦] & =𝐼(𝑥,𝑦)⋅0\end{aligned}


$$

which yields

$$


\begin{aligned}𝐼(𝑥,𝑦)⋅𝑃(𝑥,𝑦)\,d𝑥+𝐼(𝑥,𝑦)⋅𝑄(𝑥,𝑦)\,d𝑦 & =0.\end{aligned}


$$

Since the resulting equation is exact, it must satisfy the exactness test:

$$


\frac{\partial }{\partial y}\left(I(x, y)\cdot P(x,y)\right) = \frac{\partial}{\partial x} \left(I(x, y)\cdot Q(x,y)\right)


$$

Once we confirm that our equation is exact, we can solve it using methods for exact equations.

Let's solidify this idea with a concrete example.

### A Worked Example

Consider the differential equation

$$


y\,\textrm{d}x + xy\,\textrm{d}y = 0.


$$

Here, we have the functions

$$


P(x,y)=y,\qquad Q(x,y)=xy.


$$

So, the partial derivatives are

$$


\dfrac{\partial P}{\partial y}=1,\qquad \dfrac{\partial Q}{\partial x}=y.


$$

Since $\dfrac{\partial P}{\partial y}\neq\dfrac{\partial Q}{\partial x},$ the equation is *not* exact.

We now consider the integrating factor

$$


I(x,y)=\dfrac{e^{y}}{y}.


$$

Multiplying the original equation by $I(x,y),$ we obtain

$$


\dfrac{e^{y}}{y}\Big[y\,\textrm{d}x + xy\,\textrm{d}y\Big]=0,


$$

which simplifies to

$$


e^{y}\,\textrm{d}x + xe^{y}\,\textrm{d}y=0.


$$

Let's define the new functions $M$ and $N$ as

$$


M(x,y)=e^{y},\qquad N(x,y)=xe^{y}.


$$

So, we have

$$


\dfrac{\partial M}{\partial y}=e^{y},\qquad \dfrac{\partial N}{\partial x}=e^{y}.


$$

Since $\dfrac{\partial M}{\partial y}=\dfrac{\partial N}{\partial x},$ the transformed equation is exact.

Therefore, $I(x,y)=\dfrac{e^{y}}{y}$ is an integrating factor for the original equation.

### Example: Testing Integrating Factors for ODEs in Differential Form

#### Question

Show that $I(x) = \dfrac{1}{xy^3}$ is an integrating factor of the equation

$$


(x^2y-y^3) \,\textrm{d}x - x^{3} \,\textrm{d}y = 0


$$

#### Explanation

A function $I(x,y)$ is an integrating factor for the differential equation

$$


P(x,y) \,\textrm{d} x+Q(x,y)\,\textrm{d}y=0,


$$

if the following equation is exact:

$$


I(x,y)[P(x,y) \,\textrm{d} x+Q(x,y)\,\textrm{d}y] = 0


$$

In our case, we need to check if the following equation is exact:

$$


\begin{aligned}\frac{1}{𝑥𝑦^{3}}((𝑥^{2}𝑦−𝑦^{3})\,d𝑥−𝑥^{3}\,d𝑦) & =0 \\ (\frac{𝑥}{𝑦^{2}}−\frac{1}{𝑥})\,d𝑥−\frac{𝑥^{2}}{𝑦^{3}}\,d𝑦 & =0\end{aligned}


$$

Recall that a differential equation of the form

$$


P(x,y)\, \textrm{d}x +Q(x,y)\, \textrm{d}y = 0


$$

is exact if it passes the exactness test, i.e.,

$$


\frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x}.


$$

For our transformed equation, we have

$$


P(x,y) = \dfrac{x}{y^2}-\dfrac{1}{x}, \qquad Q(x,y) =- \dfrac{x^2}{y^3}.


$$

Now, we compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑃}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(\frac{𝑥}{𝑦^{2}}−\frac{1}{𝑥})=−\frac{2𝑥}{𝑦^{3}} \\ \frac{𝜕𝑄}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(−\frac{𝑥^{2}}{𝑦^{3}})=−\frac{2𝑥}{𝑦^{3}}\end{aligned}


$$

Since

$$


\frac{\partial P}{\partial y}=\frac{\partial Q}{\partial x},


$$

the transformed equation $\text{is}$ exact.

Therefore, $I(x)=\dfrac{1}{xy^3}$ $\text{is}$ an integrating factor for the initial differential equation.

### Finding Integrating Factors Dependent on X Only

Recall that we are considering equations of the form

$$


P(x,y)\,\text{d}x + Q(x,y)\,\text{d}y = 0.


$$

In many problems, it is possible to find an integrating factor that depends on *only one variable*.

In particular, if

$$


\frac{1}{Q}\left( \frac{\partial P}{\partial y} - \frac{\partial Q}{\partial x} \right) = g(x),


$$

where $g(x)$ is a function of $x$ alone, then an integrating factor is given by

$$


I(x) = \exp\left(\int g(x)\,\text{d}x\right).


$$

Let's take a look at a concrete example.

### Example: Finding an Integrating Factor for an Inexact Equation: Condition on X Satisfied

#### Question

Find an integrating factor for the following equation in differential form.

$$


x\,y' = 4y - 3x


$$

#### Explanation

For a differential equation of the form

$$


P(x,y) \,\textrm{d} x+Q(x,y)\,\textrm{d}y=0,


$$

we have that if

$$


\dfrac{1}{Q} \left(\dfrac{\partial P}{\partial y} - \dfrac{\partial Q}{\partial x}\right) = g(x)


$$

where $g(x)$ is independent of $y,$ then an integrating factor for the equation is

$$


I(x) = \exp\left({\int g(x)\,\textrm d x}\right)


$$

where $\exp(x)$ denotes the exponential function $e^x.$

First, we rewrite our equation in differential form:

$$


(3x - 4y) \;\textrm{d}x + (x) \;\textrm{d} y =0


$$

Let's denote

$$


P(x,y) = 3x - 4y, \qquad Q(x,y) = x.


$$

Now, let's compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑃}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(3𝑥−4𝑦)=−4 \\ \frac{𝜕𝑄}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}𝑥=1\end{aligned}


$$

Since

$$


\begin{aligned}\frac{1}{𝑄}(\frac{𝜕𝑃}{𝜕𝑦}−\frac{𝜕𝑄}{𝜕𝑥}) & =\frac{1}{𝑥}(−4−1) \\ & =−\frac{5}{𝑥},\end{aligned}


$$

is a function of $x$ only, we can conclude that an integrating factor for the equation is

$$


\begin{aligned}𝐼(𝑥) & =exp⁡(∫−\frac{5}{𝑥}\,d𝑥) \\ & =exp⁡(−5ln⁡|𝑥|) \\ & =𝑥^{−5}\end{aligned}


$$

and by multiplying our differential equation by the integrating factor, we have

$$


I(x) \cdot \left((3x - 4y) \;\textrm{d}x + x\;\textrm{d} y\right) = I(x)\cdot 0


$$

which simplifies as

$$


x^{-5} \cdot \left((3x - 4y) \;\textrm{d}x + x\;\textrm{d} y\right) = 0.


$$

### Finding Integrating Factors Dependent on Y Only

Recall that we are considering equations of the form

$$


P(x,y)\,\text{d}x + Q(x,y)\,\text{d}y = 0.


$$

In many problems, it is possible to find an integrating factor that depends on *only one variable*.

In particular, if

$$


\frac{1}{P}\left( \frac{\partial P}{\partial y} - \frac{\partial Q}{\partial x} \right) = h(y),


$$

where $h(y)$ is a function of $y$ alone, then an integrating factor is given by

$$


I(y) = \exp\left(-\int h(y)\,\text{d}y\right).


$$

Let's take a look at a concrete example.

### Example: Finding an Integrating Factor for an Inexact Equation: Condition on Y Satisfied

#### Question

Find an integrating factor for the following differential equation.

$$


y^2 \; \textrm{d}x + xy \; \textrm{d}y = 0, \qquad y > 0


$$

#### Explanation

For a differential equation of the form

$$


P(x,y) \,\textrm{d} x+Q(x,y)\,\textrm{d}y=0,


$$

we have that if

$$


\dfrac{1}{P} \left(\dfrac{\partial P}{\partial y} - \dfrac{\partial Q}{\partial x}\right) = h(y)


$$

where $h(y)$ is independent of $x,$ then an integrating factor for the equation is

$$


I(y) = \exp\left({-\int h(y)\,\textrm d y}\right)


$$

where $\exp(y)$ denotes the exponential function $e^y.$

Let's denote

$$


P(x,y) = y^2, \qquad Q(x,y) = xy.


$$

Now, let's compute the partial derivatives:

$$


\begin{aligned}\frac{𝜕𝑃}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑦^{2})=2𝑦 \\ \frac{𝜕𝑄}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥𝑦)=𝑦\end{aligned}


$$

Since

$$


\begin{aligned}\frac{1}{𝑃}(\frac{𝜕𝑃}{𝜕𝑦}−\frac{𝜕𝑄}{𝜕𝑥}) & =\frac{1}{𝑦^{2}}(2𝑦−𝑦) \\ & =𝑦^{−1}\end{aligned}


$$

is a function of $y$ only, we can conclude that an integrating factor for our equation is

$$


\begin{aligned}𝐼(𝑦) & =exp⁡(∫−(𝑦^{−1})\,d𝑦) \\ & =exp⁡(−ln⁡𝑦) \\ & =𝑦^{−1}\end{aligned}


$$

and by multiplying our differential equation by the integrating factor, we have

$$


I(y)\cdot \left(y^2 \; \textrm{d}x + xy\; \textrm{d}y \right) = I(y)\cdot 0


$$

which simplifies as

$$


\boxed{y^{-1}\left(y^2 \; \textrm{d}x + xy \; \textrm{d}y \right) = 0}.


$$

### Example: Solving Inexact Differential Equations Using Integrating Factors

#### Question

Consider the inexact differential equation

$$


\left(x + y^2\right)\,\textrm{d}x + \left(xy + \frac{2}{x}\right)\,\textrm{d}y = 0.


$$

It is known that

$$


\dfrac{1}{Q}\left(\dfrac{\partial P}{\partial y}-\dfrac{\partial Q}{\partial x}\right)=\frac{1}{x}


$$

where the functions $P$ and $Q$ are given by

$$


P(x,y)=x+y^2,\qquad Q(x,y)=xy+\frac{2}{x}.


$$

Use this information to find a suitable integrating factor $I(x)$ and hence find the general solution to the equation.

#### Explanation

For a differential equation of the form

$$


P(x,y)\,\textrm{d}x+Q(x,y)\,\textrm{d}y=0,


$$

we have that if

$$


\dfrac{1}{Q}\left(\dfrac{\partial P}{\partial y}-\dfrac{\partial Q}{\partial x}\right)=g(x)


$$

where $g(x)$ is independent of $y,$ then an integrating factor for the equation is

$$


I(x)=\exp\left(\int g(x)\,\textrm{d}x\right)


$$

where $\exp(x)$ denotes the exponential function $e^x.$

We are given that

$$


\dfrac{1}{Q}\left(\dfrac{\partial P}{\partial y}-\dfrac{\partial Q}{\partial x}\right)=\frac{1}{x}.


$$

Since $\dfrac{1}{x}$ is a function of $x$ only, we can conclude that the integrating factor for the equation is

$$


\begin{aligned}𝐼(𝑥) & =𝑒^{∫𝑥^{−1}\,d𝑥} \\ & =𝑒^{ln⁡𝑥} \\ & =𝑥.\end{aligned}


$$

Multiplying our equation by the integrating factor, we arrive at the following exact differential equation:

$$


\begin{aligned}𝑥[(𝑥+𝑦^{2})\,d𝑥+(𝑥𝑦+\frac{2}{𝑥})\,d𝑦] & =0 \\ \underset{\overset{𝑃}{˜}}{\underset{}{(𝑥^{2}+𝑥𝑦^{2})}}\,d𝑥+\underset{\overset{𝑄}{˜}}{\underset{}{(𝑥^{2}𝑦+2)}}\,d𝑦 & =0.\end{aligned}


$$

For this exact equation, we have

$$


\widetilde{P}(x,y)=x^2+xy^2,\qquad \widetilde{Q}(x,y)=x^2y+2.


$$

To solve the equation, let's first integrate $\widetilde{P}(x,y)$ with respect to $x.$ The result should include an arbitrary function of $y,$ which we'll call $F(y){:}$

$$


\begin{aligned}𝑢(𝑥,𝑦) & =∫\overset{𝑃}{˜}(𝑥,𝑦)\,d𝑥+𝐹(𝑦) \\ & =∫(𝑥^{2}+𝑥𝑦^{2})\,d𝑥+𝐹(𝑦) \\ & =\frac{𝑥^{3}}{3}+\frac{𝑥^{2}𝑦^{2}}{2}+𝐹(𝑦).\end{aligned}


$$

Next, let's integrate $\widetilde{Q}(x,y)$ with respect to $y.$ The result should include an arbitrary function of $x,$ which we'll call $G(x){:}$

$$


\begin{aligned}𝑢(𝑥,𝑦) & =∫\overset{𝑄}{˜}(𝑥,𝑦)\,d𝑦+𝐺(𝑥) \\ & =∫(𝑥^{2}𝑦+2)\,d𝑦+𝐺(𝑥) \\ & =\frac{𝑥^{2}𝑦^{2}}{2}+2𝑦+𝐺(𝑥).\end{aligned}


$$

Comparing the two solutions, we must have

$$


F(y)=2y,\qquad G(x)=\frac{x^3}{3}.


$$

Therefore, the general solution $u(x,y)=c$ is

$$


\frac{x^3}{3}+\frac{x^2y^2}{2}+2y=c.


$$
