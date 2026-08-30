# Elementary Trigonometric Equations Containing Cotangent

Source: https://www.mathacademy.com/topics/1567?courseId=101
Topic ID: 1567

## Prerequisites

- [Elementary Trigonometric Equations Containing Tangent](./915-elementary-trigonometric-equations-containing-tangent.md)

## Lesson

### Introduction

Suppose we want to solve the equation

$$


\cot x = 1, \qquad 0 \leq x < 2\pi.


$$

Most calculators don't have a $\text{arccot}$ button, so we can't get a principal value immediately. However, recall that $\cot x = \dfrac{1}{\tan x}.$ We can get a principal value if we rewrite the equation in terms of $\tan x\mathbin{:}$

$$


\tan{x} = \frac{1}{1} = 1


$$

Now, we can proceed as usual. Our principal value is

$$


\begin{aligned}𝑥 & =arctan⁡(1)=\frac{𝜋}{4}.\end{aligned}


$$

Since $\dfrac\pi 4$ lies inside the required domain, our first solution is $x_1 = \dfrac{\pi}{4}.$

Since we're dealing with the tangent function, we can get additional solutions by adding multiples of $\pm \pi$ to our principal value until we find all solutions. So we get another solution,

$$


\begin{aligned}𝑥_{2} & =𝑥_{1}+𝜋 \\ & =\frac{𝜋}{4}+𝜋 \\ & =\frac{5𝜋}{4}.\end{aligned}


$$

There are no more solutions in the desired domain. So, the solutions are $x=\dfrac{\pi}{4}, \dfrac{5\pi}{4}.$

### Example: Solving a Trigonometric Equation Involving Cotangent with Special Angles

#### Question

Given that $x_1$ and $x_2$ are the solutions to the equation $3\cot x + 3\sqrt{3}=0$ for $0^\circ \leq x < 360^\circ,$ what is the numerical value of $x_1\cdot x_2?$

#### Explanation

First, we rearrange the equation to isolate $\cot x\mathbin{:}$

$$


\begin{aligned}3cot⁡𝑥+3\sqrt{3} & =0 \\ 3cot⁡𝑥 & =−3\sqrt{3} \\ cot⁡𝑥 & =−\frac{3\sqrt{3}}{3} \\ cot⁡𝑥 & =−\sqrt{3}\end{aligned}


$$

Recall that $\cot{x}=\dfrac{1}{\tan{x}}.$ Therefore, the given equation is equivalent to

$$


\tan{x} =-\dfrac{1}{\sqrt{3}}=-\dfrac{\sqrt{3}}{3}.


$$

Now, we find the principal value:

$$


\begin{aligned}𝑥 & =arctan⁡(−\frac{\sqrt{3}}{3})=−30^{∘}\end{aligned}


$$

Since $-30^\circ$ lies outside the given domain, it is not a solution. However, we can generate solutions by adding integer multiples of $180^\circ$ as follows:

$$


\begin{aligned}𝑥_{1} & =𝑥+180^{∘} \\ & =−30^{∘}+180^{∘} \\ & =150^{∘} \\ & \\ 𝑥_{2} & =𝑥+360^{∘} \\ & =−30^{∘}+360^{∘} \\ & =330^{∘}\end{aligned}


$$

So, the solutions are $x=150^\circ, 330^\circ.$

Finally, the numerical value of $x_1 \cdot x_2$ is $150 \cdot 330 = 49\,500.$

### Example: Solving a Trigonometric Equation Involving Cotangent with Non-Special Angles

#### Question

Given that $x_1$ and $x_2$ are the solutions to the equation $2\cot x =9 - \cot x$ for $0 \leq x < 2\pi,$ what is the value of $x_1\cdot x_2,$ rounded to one decimal place?

#### Explanation

First, we rearrange the equation to isolate $\cot x\mathbin{:}$

$$


\begin{aligned}2cot⁡𝑥 & =9−cot⁡𝑥 \\ 3cot⁡𝑥 & =9 \\ cot⁡𝑥 & =3\end{aligned}


$$

Recall that $\cot{x}=\dfrac{1}{\tan{x}}.$ Therefore, the given equation is equivalent to

$$


\tan{x} =\dfrac{1}{3} .


$$

Now, we find the principal value:

$$


\begin{aligned}𝑥=arctan(\frac{1}{3})=0.321\,750≈0.321\,8\end{aligned}


$$

Since $0.321\,8$ lies inside the given domain, our first solution is $x_1 = 0.321\,8.$

To generate more solutions, we add integer multiples of $\pi,$ as follows:

$$


\begin{aligned}𝑥_{2} & =𝑥_{1}+𝜋 \\ & =𝜋+0.321\,8 \\ & =3.463\,4\end{aligned}


$$

Finally, the value of $x_1\cdot x_2$ is

$$


0.321\,8 \cdot 3.463\,4 \approx 1.1


$$

rounded to one decimal place.

### Equations Involving Cotangent Under a Modified Domain

We can solve an equation involving cotangent over any given domain. For example, suppose that we want to solve the equation

$$


\cot x = 1, \qquad -2\pi \leq x < 0.


$$

We can proceed as usual. Recall that $\cot{x}=\dfrac{1}{\tan{x}}.$ Therefore, the given equation is equivalent to

$$


\tan{x} = \frac{1}{1} = 1.


$$

Now, we find the principal value:

$$


\begin{aligned}𝑥 & =arctan⁡(1)=\frac{𝜋}{4}\end{aligned}


$$

Since $\dfrac\pi 4$ lies outside the required domain, it is not a solution. However, we can use it to generate solutions that are in our domain by adding (or subtracting) integer multiples of $\pi\mathbin{:}$

$$


\begin{aligned}𝑥_{1} & =𝑥−𝜋 \\ & =\frac{𝜋}{4}−𝜋 \\ & =−\frac{3𝜋}{4} \\ 𝑥_{2} & =𝑥−2𝜋 \\ & =\frac{𝜋}{4}−2𝜋 \\ & =−\frac{7𝜋}{4}\end{aligned}


$$

Therefore, the solutions are $x= -\dfrac{3\pi}{4}$ and $-\dfrac{7\pi}{4}.$

### Example: Solving a Trigonometric Equation Involving Cotangent Under a Modified Domain

#### Question

Given that $x_1$ and $x_2$ are the solutions to the equation $3\cot x + 3\sqrt{3}=0$ for $-180^\circ < x < 180^\circ,$ what is the numerical value of $x_1\cdot x_2?$

#### Explanation

First, we rearrange the equation and isolate $\cot x\mathbin{:}$

$$


\begin{aligned}3cot⁡𝑥+3\sqrt{3} & =0 \\ 3cot⁡𝑥 & =−3\sqrt{3} \\ cot⁡𝑥 & =−\frac{3\sqrt{3}}{3} \\ cot⁡𝑥 & =−\sqrt{3}\end{aligned}


$$

Recall that $\cot{x}=\dfrac{1}{\tan{x}}.$ Therefore, the given equation is equivalent to

$$


\tan{x} =-\dfrac{1}{\sqrt{3}}=-\dfrac{\sqrt{3}}{3}


$$

Now, we find the principal value:

$$


\begin{aligned}𝑥 & =arctan⁡(−\frac{\sqrt{3}}{3})=−30^{∘}\end{aligned}


$$

Since $-30^\circ$ lies inside the given domain, our first solution is $x_1 =-30^\circ.$

To generate more solutions, we add integer multiples of $180^\circ$ as follows:

$$


\begin{aligned}𝑥_{2} & =𝑥_{1}+180^{∘} \\ & =−30^{∘}+180^{∘} \\ & =150^{∘}\end{aligned}


$$

So, the solutions are $x= -30^\circ, 150^\circ.$

Finally, the numerical value of $x_1\cdot x_2$ is

$$


-30\cdot(150) = -4\,500.


$$

### Equations Where the Cotangent Function Equals Zero

Consider the following equation:

$$


\cot x = 0, \qquad 0 < x < 2\pi


$$

We can't find an equivalent equation involving tangent, since this would lead to us dividing by $0\mathbin{:}$

$$


\tan x = \dfrac{1}{0} = \text{undefined}


$$

However, we can instead find an equivalent equation using the fact that $\cot x = \dfrac{\cos x}{\sin x}\mathbin{:}$

$$


\dfrac{\cos x}{\sin x}=0


$$

In this case, we can find the principal solution as follows:

$$


\begin{aligned} \cos x &=0\\[5pt] x &= \arccos 0 \\[5pt] x &= \dfrac{\pi}{2} \end{aligned}


$$

Since this value lies inside the desired domain, our first solution is $x_1 = \dfrac{\pi}{2}.$

To find more solutions, we add integer multiples of $\pi,$ as follows:

$$


\begin{aligned}𝑥_{2} & =𝑥_{1}+𝜋 \\ & =\frac{𝜋}{2}+𝜋 \\ & =\frac{3𝜋}{2}\end{aligned}


$$

So, our solutions are $x=\dfrac\pi2$ and $x=\dfrac{3\pi}{2}.$

### Example: Solving a Trigonometric Equation When the Cotangent Function Equals Zero

#### Question

Given that $x_1$ and $x_2$ are the solutions to the equation $3- 2\cot x =3$ for $0^\circ < x < 360^\circ,$ what is the numerical value of $x_1\cdot x_2?$

#### Explanation

First, we rearrange the equation to isolate $\cot x\mathbin{:}$

$$


\begin{aligned}3−2cot⁡𝑥 & =3 \\ −2cot⁡𝑥 & =0 \\ cot⁡𝑥 & =0\end{aligned}


$$

We can't find an equivalent equation involving tangent, since this would lead to us dividing by $0\mathbin{:}$

$$


\tan x = \dfrac{1}{0} = \text{undefined}


$$

However, we can instead find an equivalent equation using the fact that $\cot x = \dfrac{\cos x}{\sin x}\mathbin{:}$

$$


\dfrac{\cos x}{\sin x}=0


$$

In this case, we can find the principal solution as follows:

$$


\begin{aligned} \cos x &=0\\[5pt] x &= \arccos 0 \\[5pt] x &= 90^\circ \end{aligned}


$$

Since this value lies inside the desired domain, our first solution is $x_1 = 90^\circ.$

To find more solutions, we add integer multiples of $180^\circ$ as follows:

$$


\begin{aligned}𝑥_{2} & =𝑥_{1}+180^{∘} \\ & =90^{∘}+180^{∘} \\ & =270^{∘}\end{aligned}


$$

So, our solutions are $x=90^\circ, 270^\circ.$

Finally, the numerical value of $x_1\cdot x_2$ is

$$


90 \cdot(270) = 24\,300.


$$
