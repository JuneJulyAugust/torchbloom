# d'Alembert Differential Equations

Source: https://www.mathacademy.com/topics/6692?courseId=61
Topic ID: 6692

## Prerequisites

- [Reducing ODEs to First-Order Linear by Substitution](./1164-reducing-odes-to-first-order-linear-by-substitution.md)
- [Clairaut Differential Equations](./6355-clairaut-differential-equations.md)

## Lesson

### Introduction

A differential equation is a **d'Alembert differential equation** if it can be expressed in the form

$$


y = xf(y') + g(y'),


$$

where $f$ and $g$ are differentiable functions of $y'.$

Note that, in the special case where $f(y') = y',$ the equation reduces to a Clairaut differential equation.

For example:

- The equation is a d'Alembert differential equation of the form $y = xf(y') + g(y')$ with

- The equation is *not* a d'Alembert differential equation because the term $\sin x$ prevents it from being written in the form $y = xf(y') + g(y').$

Let's see more examples.

### Example: Identifying d'Alembert Differential Equations

#### Question

Which of the following equations is a d'Alembert differential equation?

1. $yy' = x^2y + e^x$

2. $y = x\ln(1+y') + (y')^2$

3. $y + \dfrac{x}{1+y'} - y' = 0$

#### Explanation

A differential equation is a d'Alembert differential equation if it can be expressed in the form

$$


y = xf(y') + g(y'),


$$

where $f$ and $g$ are differentiable functions of $y'.$

Note that, in the special case where $f(y') = y',$ the equation reduces to a Clairaut differential equation.

With that in mind, let's examine the given options.

- Equation I is ** a d'Alembert differential equation. Solving for $y,$ we get which cannot be written in the form $y = xf(y') + g(y').$

- Equation II is a d'Alembert differential equation of the form $y = xf(y') + g(y')$ with

- Equation III is a d'Alembert differential equation. Isolating the variable $y,$ we get which is of the form $y = xf(y') + g(y')$ with

Therefore, the correct answer is "II and III only."

### Reducing a d'Alembert Equation to First-Order Linear

Consider the d’Alembert differential equation

$$


y = xf(y') + g(y'),


$$

where $f$ and $g$ are differentiable functions of $y'.$

Using the substitution $t = \dfrac{\textrm d y}{\textrm d x},$ the equation can be transformed to a *first-order linear equation* of the form

$$


\dfrac{\textrm d x}{\textrm d t} + P(t)x = Q(t),


$$

which we already know how to solve.

This can be done in three steps. Let's see a concrete example.

### Example: Constructing a First-Order Linear Equation From a d'Alembert Equation

#### Question

Consider the d’Alembert differential equation

$$


y = 2x\sin\!\left(\dfrac{\textrm d y}{\textrm d x}\right) + 5\left(\dfrac{\textrm d y}{\textrm d x}\right)^2.


$$

Using the substitution $t = \dfrac{\textrm d y}{\textrm d x},$ the equation can be transformed to a first-order linear equation of the form

$$


\dfrac{\textrm d x}{\textrm d t} + P(t)x = Q(t).


$$

Find the functions $P$ and $Q.$

#### Explanation

A differential equation is a d'Alembert differential equation if it can be expressed in the form

$$


y = xf(y') + g(y'),


$$

where $f$ and $g$ are differentiable functions of $y'.$

In our case, we wish to transform the equation

$$


y = 2x\sin\!\left(\dfrac{\textrm d y}{\textrm d x}\right) + 5\left(\dfrac{\textrm d y}{\textrm d x}\right)^2


$$

into a first-order linear equation for $x = x(t).$ We proceed in three steps:

****: Substitute, and differentiate with respect to $x.$

We have the substitution

$$


t = \dfrac{\textrm d y}{\textrm d x}.


$$

Substituting this into the equation gives

$$


y = 2x\sin t + 5t^2.


$$

Differentiating both sides with respect to $x,$ we have

$$


\begin{aligned}\frac{d}{d𝑥}(𝑦) & =\frac{d}{d𝑥}(2𝑥sin⁡𝑡+5𝑡^{2}).\end{aligned}


$$

Applying the sum and product rules, and using implicit differentiation, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(2𝑥sin⁡𝑡)+\frac{d}{d𝑥}(5𝑡^{2}) \\ 𝑡 & =2sin⁡𝑡\frac{d}{d𝑥}(𝑥)+2𝑥\frac{d}{d𝑥}(sin⁡𝑡)+10𝑡\frac{d𝑡}{d𝑥} \\ 𝑡 & =2sin⁡𝑡+2𝑥cos⁡𝑡\frac{d𝑡}{d𝑥}+10𝑡\frac{d𝑡}{d𝑥}.\end{aligned}


$$

****: Isolate the derivative and take its reciprocal.

We isolate $\dfrac{\textrm d t}{\textrm d x}$ as follows:

$$


\begin{aligned}𝑡−2sin⁡𝑡 & =(2𝑥cos⁡𝑡+10𝑡)\frac{d𝑡}{d𝑥} \\ \frac{𝑡−2sin⁡𝑡}{2𝑥cos⁡𝑡+10𝑡} & =\frac{d𝑡}{d𝑥}\end{aligned}


$$

which gives

$$


\dfrac{\textrm d t}{\textrm d x}=\dfrac{t-2\sin t}{2x\cos t+10t}.


$$

Therefore, by taking the reciprocal of each side, we have

$$


\dfrac{\textrm d x}{\textrm d t}=\dfrac{2x\cos t+10t}{t-2\sin t}.


$$

****: Express the derivative as a first-order linear equation.

Finally, we write this in the form

$$


\dfrac{\textrm d x}{\textrm d t} + P(t)x = Q(t)


$$

as follows:

$$


\begin{aligned}\frac{d𝑥}{d𝑡} & =\frac{2𝑥cos⁡𝑡+10𝑡}{𝑡−2sin⁡𝑡} \\ (𝑡−2sin⁡𝑡)\frac{d𝑥}{d𝑡} & =2𝑥cos⁡𝑡+10𝑡 \\ (𝑡−2sin⁡𝑡)\frac{d𝑥}{d𝑡}−2𝑥cos⁡𝑡 & =10𝑡 \\ \frac{d𝑥}{d𝑡}−\frac{2cos⁡𝑡}{𝑡−2sin⁡𝑡}𝑥 & =\frac{10𝑡}{𝑡−2sin⁡𝑡} \\ \frac{d𝑥}{d𝑡}+\frac{2cos⁡𝑡}{2sin⁡𝑡−𝑡}𝑥 & =\frac{10𝑡}{𝑡−2sin⁡𝑡}\end{aligned}


$$

Therefore, we conclude that

$$


P(t) = \dfrac{2\cos t}{2\sin t-t}, \qquad Q(t) = \dfrac{10t}{t-2\sin t}.


$$

### Solving d'Alembert Differential Equations

Now, consider the d’Alembert differential equation

$$


y = x\left(\dfrac{\textrm d y}{\textrm d x}-2\right) + 2\left(\dfrac{\textrm d y}{\textrm d x}\right)^2 - 3\left(\dfrac{\textrm d y}{\textrm d x}\right).


$$

Suppose we apply the substitution $y'(x) = t.$ Using the techniques shown earlier in the lesson (differentiating with respect to $x$), we can reduce this to the following first-order linear equation:

$$


\dfrac{\textrm d x}{\textrm d t} - \dfrac12 x = 2t-\dfrac32.


$$

Using the method of integrating factors, we compute $I(t)$ based on the coefficient $P(t) = -\dfrac12{:}$

$$


I(t) = e^{\int -1/2\,\textrm dt} = e^{-t/2}.


$$

Multiplying our differential equation by $I(t)$ converts the left-hand side into an exact derivative:

$$


\begin{aligned}𝑒^{−𝑡/2}\frac{d𝑥}{d𝑡}−\frac{1}{2}𝑥𝑒^{−𝑡/2} & =(2𝑡−\frac{3}{2})𝑒^{−𝑡/2} \\ \frac{d}{d𝑡}(𝑥𝑒^{−𝑡/2}) & =(2𝑡−\frac{3}{2})𝑒^{−𝑡/2}.\end{aligned}


$$

Integrating both sides with respect to $t,$ we have

$$


\begin{aligned}𝑥𝑒^{−𝑡/2} & =∫(2𝑡−\frac{3}{2})𝑒^{−𝑡/2}\,d𝑡 \\ 𝑥𝑒^{−𝑡/2} & =2∫𝑡𝑒^{−𝑡/2}\,d𝑡−\frac{3}{2}∫𝑒^{−𝑡/2}\,d𝑡.\end{aligned}


$$

Using integration by parts for the first integral, we obtain

$$


\begin{aligned}𝑥𝑒^{−𝑡/2} & =2(−2𝑡−4)𝑒^{−𝑡/2}−\frac{3}{2}(−2)𝑒^{−𝑡/2}+𝐶 \\ 𝑥𝑒^{−𝑡/2} & =(−4𝑡−8)𝑒^{−𝑡/2}+3𝑒^{−𝑡/2}+𝐶 \\ 𝑥𝑒^{−𝑡/2} & =(−4𝑡−5)𝑒^{−𝑡/2}+𝐶 \\ 𝑥(𝑡) & =−4𝑡−5+𝐶𝑒^{𝑡/2}.\end{aligned}


$$

Finally, to construct the function $y,$ we simply substitute $y' = t$ and $x = x(t)$ into our original equation. Note that the solution $y(t)$ is dependent on the parameter $t.$

Let's see another example.

### Example: Finding the General Solution

#### Question

Consider the d’Alembert differential equation

$$


y = x\left(\dfrac{\textrm d y}{\textrm d x}-1\right)^2 + 2\left(\dfrac{\textrm d y}{\textrm d x}\right).


$$

If $y'(x) = t,$ then general solution can be expressed in parametric form $(x(t), y(t)),$ where

$$


y(t) = \left( \dfrac{2\ln|t| - t^2+C}{2(t-1)^2} \right) f(t) + g(t)


$$

and $C$ is an arbitrary constant. Find $f(t)+g(t).$

**

$$


\dfrac{\textrm d x}{\textrm d t} + \dfrac{2x}{t-1} = \frac{1+t}{t(1-t)}


$$

#### Explanation

A differential equation is a d'Alembert differential equation if it can be expressed in the form

$$


y = xf(y') + g(y'),


$$

where $f$ and $g$ are differentiable functions of $y'.$

We're told that, under the substitution $y'(x) = t,$ our d’Alembert differential equation transforms to the first-order linear equation

$$


\dfrac{\textrm d x}{\textrm d t} + \dfrac{2x}{t-1} = \frac{1+t}{t(1-t)}.


$$

We'll solve this equation using the method of integrating factors. Since this equation is already of the form

$$


\dfrac{\textrm d x}{\textrm d t} + P(t)x = Q(t)


$$

we compute our integrating factor as follows:

$$


\begin{aligned}𝐼(𝑡) & =𝑒^{∫𝑃(𝑡)\,d𝑡} \\ & =𝑒^{∫2/(𝑡−1)\,d𝑡} \\ & =𝑒^{2ln⁡|𝑡−1|} \\ & =𝑒^{ln⁡(𝑡−1)^{2}} \\ & =(𝑡−1)^{2}\end{aligned}


$$

Multiplying our differential equation by $I(t)$ gives

$$


\begin{aligned}(𝑡−1)^{2}\frac{d𝑥}{d𝑡}+2(𝑡−1)𝑥 & =(𝑡−1)^{2}\frac{1+𝑡}{𝑡(1−𝑡)} \\ (𝑡−1)^{2}\frac{d𝑥}{d𝑡}+2(𝑡−1)𝑥 & =\frac{1−𝑡^{2}}{𝑡}.\end{aligned}


$$

Rewriting the left-hand side as an exact derivative, and integrating both sides of the equation with respect to $t,$ we have

$$


\begin{aligned}\frac{d}{d𝑡}(𝑥(𝑡−1)^{2}) & =\frac{1−𝑡^{2}}{𝑡} \\ ∫\frac{d}{d𝑡}(𝑥(𝑡−1)^{2})\,d𝑡 & =∫\frac{1−𝑡^{2}}{𝑡}\,d𝑡 \\ 𝑥(𝑡−1)^{2} & =∫\frac{1}{𝑡}−𝑡\,d𝑡 \\ 𝑥(𝑡−1)^{2} & =ln⁡|𝑡|−\frac{𝑡^{2}}{2}+𝐶 \\ 𝑥 & =\frac{2ln⁡|𝑡|−𝑡^{2}+𝐶}{2(𝑡−1)^{2}}.\end{aligned}


$$

Therefore, we have that

$$


x(t) = \dfrac{2\ln|t| - t^2+C}{2(t-1)^2}.


$$

To recover $y$, we substitute $x$ into

$$


y = x(t-1)^2 + 2t,


$$

which gives

$$


\begin{aligned}𝑦(𝑡) & =(\frac{2ln⁡|𝑡|−𝑡^{2}+𝐶}{2(𝑡−1)^{2}})(𝑡−1)^{2}+2𝑡.\end{aligned}


$$

Finally, we conclude that $f(t)=(t-1)^2,\ g(t)=2t,$ and

$$


f(t)+g(t) = t^2 +1.


$$

### The General Result

Finally, we'll show the derivation of reducing a d'Alembert Equation to a first-order linear ODE.

We start from

$$


y = x f(y') + g(y').


$$

Then, we introduce the substitution

$$


t = y',


$$

so the equation becomes

$$


y = x f(t) + g(t).


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\dfrac{\text{d}y}{\text{d}x} = f(t) + x f'(t)\dfrac{\text{d}t}{\text{d}x} + g'(t)\frac{\text{d}t}{\text{d}x}.


$$

Since $\dfrac{\text{d}y}{\text{d}x} = t,$ this simplifies to

$$


t = f(t) + \bigl(x f'(t) + g'(t)\bigr)\frac{\text{d}t}{\text{d}x}.


$$

Now, assuming $f(t) \neq t$, we rearrange the equation as follows:

$$


\begin{aligned}(𝑥𝑓^{′}(𝑡)+𝑔^{′}(𝑡))\frac{d𝑡}{d𝑥} & =𝑡−𝑓(𝑡) \\ \frac{d𝑡}{d𝑥} & =\frac{𝑡−𝑓(𝑡)}{𝑥𝑓^{′}(𝑡)+𝑔^{′}(𝑡)} \\ \frac{d𝑥}{d𝑡} & =\frac{𝑥𝑓^{′}(𝑡)+𝑔^{′}(𝑡)}{𝑡−𝑓(𝑡)} \\ \frac{d𝑥}{d𝑡} & =\frac{𝑓^{′}(𝑡)}{𝑡−𝑓(𝑡)}𝑥+\frac{𝑔^{′}(𝑡)}{𝑡−𝑓(𝑡)} \\ \frac{d𝑥}{d𝑡}+\frac{𝑓^{′}(𝑡)}{𝑓(𝑡)−𝑡}𝑥 & =−\frac{𝑔^{′}(𝑡)}{𝑓(𝑡)−𝑡}\end{aligned}


$$

This is a *first-order linear ODE* for $x$ as a function of $t$:

$$


\frac{\text{d}x}{\text{d}t} + P(t)x = Q(t),


$$

with

$$


P(t) = \frac{f'(t)}{f(t) - t}, \qquad Q(t) = -\frac{g'(t)}{f(t) - t}.


$$
