# Reducing ODEs to First-Order Linear by Substitution

Source: https://www.mathacademy.com/topics/1164?courseId=154
Topic ID: 1164

## Prerequisites

- [Solving First-Order Linear ODEs Using Integrating Factors](./877-solving-first-order-linear-odes-using-integrating-factors.md)

## Lesson

### Introduction

Let's consider the first-order differential equation

$$


2y\dfrac {\text{d}y} {\text{d}x}+y^2=x.


$$

Notice that it is *not* a first-order linear equation because it cannot be written in the form $y' + P(x) y = Q(x).$ In fact, this equation is an example of a *nonlinear* first-order differential equation.

We can sometimes transform a nonlinear differential equation into a linear differential equation using a substitution. If we can do this, then we can apply the method of integrating factors to solve it.

To transform the above equation into a linear differential equation, we can use the substitution

$$


z=y^2.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac {\text{d}z} {\text{d}x}=2y\dfrac {\text{d}y} {\text{d}x}.


$$

Consequently, the original differential equation can be written in terms of $z$ as follows:

$$


\dfrac {\text{d}z} {\text{d}x}+z=x


$$

This differential equation is linear! So, we can use the method of integrating factors. The given equation is in the standard form

$$


\frac{\text{d}z}{\text{d}x} + P(x)z = Q(x)


$$

with $P(x)=1$ and $Q(x)=x.$ We then compute an integrating factor:

$$


\begin{aligned}𝐼(𝑥) & =𝑒^{∫𝑃(𝑥)\,d𝑥} \\ & =𝑒^{∫1\,d𝑥} \\ & =𝑒^{𝑥}\end{aligned}


$$

Multiplying both sides of the standard form equation by $I(x)=e^x$ yields

$$


\begin{aligned}𝑒^{𝑥}(\frac{d𝑧}{d𝑥}+𝑧) & =𝑒^{𝑥}⋅𝑥 \\ \frac{d𝑧}{d𝑥}𝑒^{𝑥}+𝑧𝑒^{𝑥} & =𝑥𝑒^{𝑥} \\ \frac{d}{d𝑥}(𝑧𝑒^{𝑥}) & =𝑥𝑒^{𝑥}\,.\end{aligned}


$$

We now integrate with respect to $x,$ using integration by parts to integrate the right-hand side:

$$


\begin{aligned}∫\frac{d}{d𝑥}(𝑧𝑒^{𝑥})\,d𝑥 & =∫𝑥𝑒^{𝑥}d𝑥 \\ 𝑧𝑒^{𝑥} & =(𝑥−1)𝑒^{𝑥}+𝐶 \\ 𝑧 & =𝑥−1+𝐶𝑒^{−𝑥}\end{aligned}


$$

Finally, we determine $y(x)$ by substituting the solution into $z=y^2.$ This results in

$$


\begin{aligned}𝑦^{2} & =𝑧 \\ 𝑦^{2} & =𝑥−1+𝐶𝑒^{−𝑥} \\ 𝑦 & =±\sqrt{𝑥−1+𝐶𝑒^{−𝑥}}.\end{aligned}


$$

### Example: Reducing a First-Order ODE to a First-Order Linear ODE Using a Substitution

#### Question

The substitution $z= y^2$ can be used to transform the equation

$$


\dfrac{{{\rm{d}}y}}{{{\rm{d}}x}} = \dfrac{x+2}{2y} + 2x^2y


$$

into an equation of the form $z'(x) + P(x)z(x) = Q(x).$ What is the function $P(x)?$

#### Explanation

First, we make the substitution

$$


z= y^{2}.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = 2y \,\dfrac{\text{d}y}{\text{d}x} \quad\Longrightarrow\quad \dfrac{\text{d}y}{\text{d}x} = \dfrac{1}{2z^{1/2}}\,\dfrac{\text{d}z}{\text{d}x}.


$$

Consequently, the original differential equation can be written in terms of $z$ as follows:

$$


\begin{aligned}\frac{1}{2𝑧^{1/2}}\,\frac{d𝑧}{d𝑥} & =\frac{𝑥+2}{2𝑧^{1/2}}+2𝑥^{2}𝑧^{1/2}\end{aligned}


$$

We now write the above equation in standard form

$$


\frac{\text{d}z}{\text{d}x} + P(x)z = Q(x).


$$

In doing so, we obtain

$$


\begin{aligned}\frac{d𝑧}{d𝑥} & =𝑥+2+4𝑥^{2}𝑧 \\ \frac{d𝑧}{d𝑥}−4𝑥^{2}𝑧 & =𝑥+2.\end{aligned}


$$

Therefore, $P(x) = - 4x^2.$

### Example: Solving a First-Order ODE Using a Substitution

#### Question

Find the general solution to the following first-order ODE using the substitution $z=y^3.$

$$


xy^2\dfrac {\text{d}y} {\text{d}x} = x^2+y^3


$$

#### Explanation

Let's make a substitution

$$


z=y^3\,.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x}=3y^2\,\dfrac{\text{d}y}{\text{d}x} \quad\Longrightarrow\quad y^2\dfrac{\text{d}y}{\text{d}x}=\dfrac{1}{3}\,\dfrac{\text{d}z}{\text{d}x}.


$$

Consequently, the original differential equation can be written in terms of $z$ as follows:

$$


\frac{x}{3}\left(\dfrac{\text{d}z}{\text{d}x}\right)=x^2+z


$$

This differential equation is linear, so we can use the method of integrating factors. First, we write the above equation in standard form:

$$


\begin{aligned}\frac{d𝑧}{d𝑥} & =\frac{3}{𝑥}(𝑥^{2}+𝑧) \\ \frac{d𝑧}{d𝑥} & =3𝑥+\frac{3}{𝑥}𝑧 \\ \frac{d𝑧}{d𝑥}−\frac{3}{𝑥}\,𝑧 & =3𝑥\end{aligned}


$$

The above equation is in the standard form

$$


\frac{\text{d}z}{\text{d}x} + P(x)y = Q(x)


$$

with

$$


\begin{aligned}𝑃(𝑥)=−\frac{3}{𝑥},\,𝑄(𝑥)=3𝑥\,.\end{aligned}


$$

We then compute an integrating factor:

$$


\begin{aligned}𝐼(𝑥) & =𝑒^{∫𝑃(𝑥)\,d𝑥} \\ & =𝑒^{∫(−3/𝑥)\,d𝑥} \\ & =𝑒^{−3ln⁡𝑥} \\ & =\frac{1}{𝑥^{3}}\end{aligned}


$$

Multiplying both sides of the standard form equation by $I(x)=\dfrac{1}{x^3}$ yields

$$


\begin{aligned}\frac{1}{𝑥^{3}}(\frac{d𝑧}{d𝑥}−\frac{3}{𝑥}\,𝑧) & =\frac{1}{𝑥^{3}}⋅3𝑥 \\ \frac{1}{𝑥^{3}}⋅\frac{d𝑧}{d𝑥}−\frac{3}{𝑥^{4}}\,𝑧 & =\frac{3}{𝑥^{2}} \\ \frac{d}{d𝑥}(\frac{𝑧}{𝑥^{3}}) & =\frac{3}{𝑥^{2}}\,.\end{aligned}


$$

Now, we integrate with respect to $x\mathbin{:}$

$$


\begin{aligned}∫\frac{d}{d𝑥}(\frac{𝑧}{𝑥^{3}})\,d𝑥 & =∫\frac{3}{𝑥^{2}}d𝑥 \\ \frac{𝑧}{𝑥^{3}} & =−\frac{3}{𝑥}+𝐶 \\ 𝑧 & =−3𝑥^{2}+𝐶𝑥^{3}\end{aligned}


$$

Finally, we determine $y(x)$ by substituting the solution into $z=y^3.$ This results in

$$


\begin{aligned}𝑦^{3} & =𝑧 \\ 𝑦^{3} & =−3𝑥^{2}+𝐶𝑥^{3} \\ 𝑦 & =\sqrt[√−3𝑥^{2}+𝐶𝑥^{3}]{3}\,.\end{aligned}


$$

### Example: Solving a First-Order Initial Value Problem Using a Substitution

#### Question

Find the specific solution of the first-order ODE

$$


xe^y\dfrac {\text{d}y} {\text{d}x}+e^y = e^{x} \, ,


$$

given that $y(1)=1$ and $x>0.$

#### Explanation

Let's make a substitution

$$


z=e^y\,.


$$

Differentiating $z(x)$ with the chain rule, we get $\dfrac{\text{d}z}{\text{d}x}=e^y\,\dfrac{\text{d}y}{\text{d}x}.$ Consequently, the original differential equation can be written in terms of $z$ as follows:

$$


x\dfrac{\text{d}z}{\text{d}x}+z=e^x\,,


$$

with the initial condition

$$


z(1)=e^{y(1)}=e^1=e\,.


$$

Notice that the left-hand side of the differential equation is now an exact derivative:

$$


\begin{aligned}𝑥\frac{d𝑧}{d𝑥}+𝑧 & =\frac{d}{d𝑥}(𝑥𝑧)\,.\end{aligned}


$$

So, we have

$$


\begin{aligned}\frac{d}{d𝑥}(𝑥𝑧) & =𝑒^{𝑥} \\ ∫\frac{d}{d𝑥}(𝑥𝑧)\,d𝑥 & =∫𝑒^{𝑥}d𝑥 \\ 𝑥𝑧 & =𝑒^{𝑥}+𝐶 \\ 𝑧 & =\frac{𝑒^{𝑥}+𝐶}{𝑥}\,.\end{aligned}


$$

Now, we determine the value of $C$ that satisfies the initial condition $z(1)=e\mathbin{:}$

$$


\begin{aligned}𝑧(1) & =𝑒 \\ \frac{𝑒^{1}+𝐶}{1} & =𝑒 \\ 𝑒+𝐶 & =𝑒 \\ 𝐶 & =0\,.\end{aligned}


$$

So we have

$$


z = \frac{e^x}{x}\,.


$$

Finally, we determine $y(x)$ by substituting the solution into $z=e^y.$ This results in

$$


\begin{aligned}𝑒^{𝑦} & =𝑧 \\ 𝑒^{𝑦} & =\frac{𝑒^{𝑥}}{𝑥} \\ 𝑦 & =ln⁡(\frac{𝑒^{𝑥}}{𝑥}) \\ & =ln⁡(𝑒^{𝑥})−ln⁡(𝑥) \\ & =𝑥−ln⁡(𝑥)\,,\end{aligned}


$$

under the condition that $x>0.$ So, the final solution is

$$


y = x - \ln (x), \quad x > 0.


$$
