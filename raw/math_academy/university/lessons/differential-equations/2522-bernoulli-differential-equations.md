# Bernoulli Differential Equations

Source: https://www.mathacademy.com/topics/2522?courseId=61
Topic ID: 2522

## Prerequisites

- [Reducing ODEs to First-Order Linear by Substitution](./1164-reducing-odes-to-first-order-linear-by-substitution.md)

## Lesson

### Introduction

A **Bernoulli differential equation** is an ordinary differential equation of the form

$$


\dfrac{{{\rm{d}}y}}{{{\rm{d}}x}}+ p ( x ) y = q ( x ) y^n,


$$

where $p(x)$ and $q(x)$ are continuous functions, and $n$ is any real number.

The substitution $z=y^{1-n}$ reduces any Bernoulli equation to a first-order linear differential equation.

For example, consider the equation

$$


\dfrac{{{\rm{d}}y}}{{{\rm{d}}x}}+y = x y^2.


$$

Notice that this equation is a Bernoulli differential equation with

$$


p(x) =1, \qquad q(x) = x, \qquad n=2.


$$

To reduce our equation to a linear differential equation, we first divide it by $y^2{:}$

$$


y^{-2} \dfrac{{{\rm{d}}y}}{{{\rm{d}}x}} +y^{-1} = x


$$

Notice that the right-hand side is now a function of $x$ only.

Then, we make the substitution

$$


z= y^{1-n} = y^{1-2} = y^{-1}.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = -y^{-2} \,\dfrac{\text{d}y}{\text{d}x} \qquad\Longrightarrow\qquad y^{-2}\dfrac{\text{d}y}{\text{d}x} = -\,\dfrac{\text{d}z}{\text{d}x}.


$$

Therefore, the original equation can be written in terms of $z(x)$ as follows:

$$


-\,\dfrac{\text{d}z}{\text{d}x} +z = x


$$

Writing the above in standard form, we get

$$


\dfrac{\text{d}z}{\text{d}x} -z=-x.


$$

This differential equation is linear, so we can use integrating factors to solve it.

### Example: Identifying Bernoulli Differential Equations

#### Question

Which of the following equations is a Bernoulli differential equation?

1. $y\,y' + x^2y^2 = e^x y^4$

2. $xy' + x^3y = -x^2 y^3$

3. $y' + y\cos{x} = e^{y+1}$

#### Explanation

A Bernoulli differential equation has the form

$$


\dfrac{{{\rm{d}}y}}{{{\rm{d}}x}} + p(x)y= q(x)y^n,


$$

where $n$ is a real number.

With that in mind, let's examine the given options.

- Equation I is a Bernoulli differential equation. Writing the equation in standard form, we get which is a Bernoulli differential equation with

- Equation II is a Bernoulli differential equation. Writing the equation in standard form, we get which is a Bernoulli differential equation with

- Equation III is ** a Bernoulli differential equation. It is missing the $q(x)y^n$ term.

Therefore, the correct answer is "I and II only."

### Example: Reducing a Bernoulli Differential Equation to First Order Linear

#### Question

The substitution $z=y^m$ for some real number $m$ transforms the differential equation

$$


\dfrac{{{\rm{d}}y}}{{{\rm{d}}x}} + x^3y= \dfrac{1}{\sqrt{y}}


$$

into an equation of the form $z'(x) + P(x)z(x) = Q(x).$ What is the function $Q(x)?$

#### Explanation

Notice that our equation is an instance of the Bernoulli differential equation

$$


\dfrac{{{\rm{d}}y}}{{{\rm{d}}x}} + p(x)y= q(x)y^n.


$$

In this case, we have

$$


p(x) = x^3, \qquad q(x) = 1, \qquad n=-\dfrac12.


$$

First, we multiply the differential equation by $y^{1/2},$ and we get

$$


y^{1/2} \dfrac{{{\rm{d}}y}}{{{\rm{d}}x}} + x^3y^{3/2}= 1.\qquad\qquad (\ast)


$$

Then, we make the substitution

$$


z= y^{1-n} = y^{3/2}.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = \dfrac{3}{2}y^{1/2} \,\dfrac{\text{d}y}{\text{d}x} \quad\Longrightarrow\quad y^{1/2}\dfrac{\text{d}y}{\text{d}x} = \dfrac{2}{3}\,\dfrac{\text{d}z}{\text{d}x}.


$$

Therefore, equation $(\ast)$ can be written as a linear equation in $z(x)$ as follows:

$$


\dfrac{2}{3}\,\dfrac{\text{d}z}{\text{d}x} + x^3\,z = 1


$$

Finally, we write the above equation in standard form, which gives

$$


\dfrac{\text{d}z}{\text{d}x} + \dfrac{3}{2}x^3z = \dfrac{3}{2}.


$$

Therefore, $Q(x) = \dfrac{3}{2}.$

### Example: Solving a Bernoulli Differential Equation

#### Question

Find the general solution to the differential equation

$$


\dfrac {\text{d}y} {\text{d}x} + \dfrac{y}{x} = \dfrac{x^2}{y} .


$$

#### Explanation

Notice that our equation is an instance of the Bernoulli differential equation

$$


\dfrac{{{\rm{d}}y}}{{{\rm{d}}x}} + p(x)y= q(x)y^n.


$$

In this case, we have

$$


p(x) = \dfrac{1}{x}, \qquad q(x) = x^2, \qquad n=-1.


$$

First, we divide the differential equation by $y^{-1},$ and we get

$$


y \dfrac{{{\rm{d}}y}}{{{\rm{d}}x}} + \dfrac{y^{2}}{x}= x^2.


$$

Then, we make the substitution

$$


z= y^{1-n} = y^{2}.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = 2y \,\dfrac{\text{d}y}{\text{d}x} \quad\Longrightarrow\quad y\dfrac{\text{d}y}{\text{d}x} = \dfrac{1}{2}\,\dfrac{\text{d}z}{\text{d}x}.


$$

Therefore, the original equation can be written in terms of $z(x)$ as follows:

$$


\dfrac{1}{2}\,\dfrac{\text{d}z}{\text{d}x} + \dfrac{1}{x}z = x^2


$$

This differential equation is linear, so we can use the method of integrating factors. But first, we write the above equation in standard form:

$$


\dfrac{\text{d}z}{\text{d}x} + \dfrac{2}{x} z =2x^2


$$

The above equation is in the standard form

$$


\frac{\text{d}z}{\text{d}x} + P(x)z = Q(x)


$$

with

$$


\begin{aligned}𝑃(𝑥)=\frac{2}{𝑥},\,𝑄(𝑥)=2𝑥^{2}\,.\end{aligned}


$$

We then compute an integrating factor:

$$


\begin{aligned}𝐼(𝑥) & =𝑒^{∫𝑃(𝑥)\,d𝑥} \\ & =𝑒^{∫(2/𝑥)\,d𝑥} \\ & =𝑒^{2ln⁡𝑥} \\ & =𝑥^{2}\end{aligned}


$$

Multiplying both sides of the standard form equation by $I(x)=x^2$ yields

$$


\begin{aligned}𝑥^{2}⋅(\frac{d𝑧}{d𝑥}+\frac{2}{𝑥}𝑧) & =𝑥^{2}⋅(2𝑥^{2}) \\ 𝑥^{2}⋅\frac{d𝑧}{d𝑥}+2𝑥𝑧 & =2𝑥^{4} \\ \frac{d}{d𝑥}(𝑧𝑥^{2}) & =2𝑥^{4}.\end{aligned}


$$

Now, we integrate with respect to $x$ and get

$$


\begin{aligned}∫\frac{d}{d𝑥}(𝑧𝑥^{2})\,d𝑥 & =∫2𝑥^{4}\,d𝑥 \\ 𝑧𝑥^{2} & =\frac{2𝑥^{5}}{5}+𝐶_{1} \\ 𝑧 & =\frac{2𝑥^{5}+𝐶}{5𝑥^{2}},\end{aligned}


$$

where $C=5C_1.$

Finally, we determine $y(x)$ by writing $z=y^{2}.$ This results in the general solution

$$


y^{ 2} =\dfrac{2x^5 + C}{5x^2}.


$$
