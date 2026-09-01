# Abel's Identity

Source: https://www.mathacademy.com/topics/6367?courseId=61
Topic ID: 6367

## Prerequisites

- [Solving First-Order IVPs Using Separation of Variables](./1179-solving-first-order-ivps-using-separation-of-variables.md)
- [Linear Independence of Solutions to Homogeneous ODEs](./2547-linear-independence-of-solutions-to-homogeneous-odes.md)

## Lesson

### Introduction

The Wronskian is a quick way to check whether two solutions of a homogeneous ODE are linearly independent.

In this lesson, we learn an identity, which tells us how the Wronskian changes with $x$ for an equation of the form

$$


y''+P(x)y'+Q(x)y=0.


$$

Suppose $y_1$ and $y_2$ are solutions of the second-order linear homogeneous ODE above on some interval $I.$ Let $W(x)$ be their Wronskian:

$$


\begin{aligned}𝑦_{1}(𝑥) & 𝑦_{2}(𝑥) \\ 𝑦_{′1}(𝑥) & 𝑦_{′2}(𝑥)\end{aligned}


$$

Then, **Abel's identity** states that the Wronskian satisfies the first-order linear differential equation

$$


W'(x)=-P(x)W(x).


$$

Solving this equation via separation of variables gives the general form for $W(x){:}$

$$


W(x) = C e^{-\int P(x) \, \text{d}x}


$$

This allows us to determine the behavior of the Wronskian without knowing the solutions $y_1$ and $y_2.$

For example, consider the second-order homogeneous differential equation

$$


y''+3xy'+e^x y=0


$$

with solutions $y_1$ and $y_2,$ and the corresponding Wronskian $W(x).$ Let's determine the differential equation that $W(x)$ must satisfy.

In our equation, the coefficient of $y'$ is

$$


P(x)=3x.


$$

Substituting this into Abel's identity gives

$$


\begin{aligned}𝑊^{′}(𝑥) & =−3𝑥𝑊(𝑥).\end{aligned}


$$

**Watch out!** If the equation is not already in standard form, we should rewrite it before applying Abel’s identity.

### Example: Identifying Wronskian Differential Equation

#### Question

$$


x^2y''-5xy'+\ln(x)y=0, \qquad x>0


$$

Consider the second-order homogeneous differential equation above. Let $y_1$ and $y_2$ be solutions, and let $W(x)$ be their Wronskian. Which differential equation must $W(x)$ satisfy?

#### Explanation

Abel's identity says that if $y_1$ and $y_2$ are solutions of

$$


y''+P(x)y'+Q(x)y=0,


$$

then their Wronskian $W(x)$ satisfies

$$


W'(x)=-P(x)W(x).


$$

First, we rewrite our equation in standard form. Since $x>0$, we can divide both sides by $x^2$ to get

$$


y''-\frac{5}{x}y'+\frac{\ln(x)}{x^2}y=0.


$$

Now, the coefficient of $y'$ is

$$


P(x)=-\frac{5}{x}.


$$

Substituting this into Abel's identity gives

$$


W'(x)= \boxed{\frac{5}{x}W(x)}.


$$

### Example: Computing the Wronskian Using Abel's Identity

#### Question

Consider the differential equation

$$


y''+\tan(x)y'+e^x y=0, \qquad -\frac{\pi}{2} < x < \frac{\pi}{2}.


$$

Suppose $y_1$ and $y_2$ are solutions and their Wronskian $W(x)$ satisfies $W(0)=4.$ What is $W\left(\dfrac{\pi}{3}\right)?$

#### Explanation

Abel's identity says that if $y_1$ and $y_2$ are solutions of

$$


y''+P(x)y'+Q(x)y=0,


$$

then their Wronskian $W(x)$ satisfies

$$


W'(x)=-P(x)W(x).


$$

In our equation, the coefficient of $y'$ is

$$


P(x)=\tan(x).


$$

Substituting into Abel's identity gives

$$


W'(x)=-\tan(x)W(x).


$$

Now, we solve the first-order differential equation for $W{:}$

$$


\begin{aligned}𝑊^{′} & =−tan⁡(𝑥)𝑊 \\ \frac{d𝑊}{𝑊} & =−tan⁡(𝑥)\,d𝑥 \\ ∫\frac{d𝑊}{𝑊} & =∫−tan⁡(𝑥)\,d𝑥 \\ ln⁡|𝑊| & =ln⁡(cos⁡𝑥)+𝐾 \\ |𝑊| & =𝑒^{𝐾}cos⁡𝑥 \\ 𝑊 & =𝐶cos⁡𝑥\end{aligned}


$$

where $C$ is a constant.

Next, we use the given value $W(0)=4$ to find $C{:}$

$$


\begin{aligned}𝑊(0) & =𝐶cos⁡(0) \\ 4 & =𝐶⋅1 \\ 𝐶 & =4\end{aligned}


$$

Thus, we have

$$


W(x)=4\cos x.


$$

Finally, we compute $W\left(\dfrac{\pi}{3}\right){:}$

$$


\begin{aligned}𝑊(\frac{𝜋}{3}) & =4cos⁡(\frac{𝜋}{3})=2.\end{aligned}


$$

### Applications of Abel's Identity

Because the exponential factor in Abel's identity is *never zero*, we can deduce the following facts:

- If $W(x_0)=0$ at some point $x_0 \in I,$ then $W(x) = 0$ for all $x \in I.$

- If $W(x_0)\neq 0,$ then $W(x) \neq 0$ for all $x \in I.$

Let's see how this works on concrete examples.

### Example: Using Abel's Identity to Conclude Independence/Dependence

#### Question

$$


y''+4y'+Q(x)y=0


$$

Let $y_1$ and $y_2$ be solutions to the second-order homogeneous differential equation above, where $Q(x)$ is continuous on $(-\infty,\infty).$ The Wronskian satisfies $W(2)=-3.$ Use Abel's identity to conclude whether $y_1$ and $y_2$ are linearly independent on $\mathbb{R}.$

#### Explanation

Abel's identity says that if $y_1$ and $y_2$ are solutions of

$$


y''+P(x)y'+Q(x)y=0,


$$

then their Wronskian $W(x)$ satisfies

$$


W'(x)=-P(x)W(x).


$$

In our equation, the coefficient of $y'$ is

$$


P(x)=4.


$$

Substituting into Abel's identity gives

$$


W'(x)= \boxed{-4}W(x).


$$

Now, we solve the first-order differential equation for $W{:}$

$$


\begin{aligned}𝑊^{′} & =−4𝑊 \\ \frac{d𝑊}{𝑊} & =−4\,d𝑥 \\ ∫\frac{d𝑊}{𝑊} & =∫−4\,d𝑥 \\ ln⁡|𝑊| & =−4𝑥+𝐾 \\ |𝑊| & =𝑒^{𝐾}𝑒^{−4𝑥} \\ 𝑊 & =𝐶𝑒^{−4𝑥}\end{aligned}


$$

where $C$ is a constant.

Next, we use the given value $W(2)=-3$ to find $C{:}$

$$


\begin{aligned}𝑊(2) & =𝐶𝑒^{−4⋅2} \\ −3 & =𝐶𝑒^{−8} \\ 𝐶 & =−3𝑒^{8}\end{aligned}


$$

Therefore, we have

$$


W(x)=-3e^{8}e^{-4x}.


$$

Since $-3e^{8}e^{-4x}\neq 0$ for all $x\in\mathbb{R}$, we conclude that $𝑊(𝑥)≠0$

So, $y_1$ and $y_2$ are $ℝ$

### The Proof of Abel's Identity

*Abel's identity* says that if $y_1$ and $y_2$ are solutions of

$$


y''+p(x)y'+q(x)y=0,


$$

then their *Wronskian* $W(x)$ satisfies

$$


W'(x)=-p(x)W(x).


$$

To prove it, we start with the definition

$$


W(x)=y_1y_2'-y_2y_1'


$$

and differentiate both sides:

$$


\begin{aligned}𝑊^{′}(𝑥) & =\frac{d}{d𝑥}(𝑦_{1}𝑦_{′2}−𝑦_{2}𝑦_{′1}) \\ & =𝑦_{′1}𝑦_{′2}+𝑦_{1}𝑦_{″2}−𝑦_{′2}𝑦_{′1}−𝑦_{2}𝑦_{″1} \\ & =𝑦_{1}𝑦_{″2}−𝑦_{2}𝑦_{″1}\end{aligned}


$$

Since $y_1$ and $y_2$ are solutions of $y''+p(x)y'+q(x)y=0$, we have

$$


y_1''=-p(x)y_1'-q(x)y_1 \qquad\text{and}\qquad y_2''=-p(x)y_2'-q(x)y_2.


$$

Now, we substitute these into the expression for $W'(x)$:

$$


\begin{aligned}𝑊^{′}(𝑥) & =𝑦_{1}𝑦_{″2}−𝑦_{2}𝑦_{″1} \\ & =𝑦_{1}(−𝑝(𝑥)𝑦_{′2}−𝑞(𝑥)𝑦_{2})−𝑦_{2}(−𝑝(𝑥)𝑦_{′1}−𝑞(𝑥)𝑦_{1}) \\ & =−𝑝(𝑥)𝑦_{1}𝑦_{′2}−𝑞(𝑥)𝑦_{1}𝑦_{2}+𝑝(𝑥)𝑦_{2}𝑦_{′1}+𝑞(𝑥)𝑦_{1}𝑦_{2} \\ & =−𝑝(𝑥)(𝑦_{1}𝑦_{′2}−𝑦_{2}𝑦_{′1}) \\ & =−𝑝(𝑥)𝑊(𝑥)\end{aligned}


$$

Therefore, $W'(x)=-p(x)W(x)$, as required.
