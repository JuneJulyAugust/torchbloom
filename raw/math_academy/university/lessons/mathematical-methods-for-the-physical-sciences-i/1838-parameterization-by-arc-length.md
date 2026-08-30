# Parameterization by Arc Length

Source: https://www.mathacademy.com/topics/1838?courseId=154
Topic ID: 1838

## Prerequisites

- [Unit Tangent Vectors](./1794-unit-tangent-vectors.md)
- [The Arc Length of a Vector-Valued Function](./1837-the-arc-length-of-a-vector-valued-function.md)

## Lesson

### Introduction

Consider the curve $C$ parametrized by the vector function

$$


\mathbf r(t) = \langle 2\sin t, \: 2\cos t, \: \sqrt{5} t\rangle, \qquad t \ge 0.


$$

For any $t >0,$ the arc length $s$ of $C$ from $\mathbf r(0)$ to $\mathbf r(t)$ is

$$


\begin{aligned}𝑠 & =∫_{𝑡0}‖𝐫^{′}(𝑢)‖\,d𝑢 \\ & =∫_{𝑡0}‖⟨2cos⁡𝑢,\,−2sin⁡𝑢,\,\sqrt{5}⟩‖\,d𝑢 \\ & =∫_{𝑡0}\sqrt{(2cos⁡𝑢)^{2}+(−2sin⁡𝑢)^{2}+(\sqrt{5})^{2}}\,d𝑢 \\ & =∫_{𝑡0}\sqrt{4(cos^{2}⁡𝑢+sin^{2}⁡𝑢)+5}\,d𝑢 \\ & =∫_{𝑡0}\sqrt{9}\,d𝑢 \\ & =3𝑢_{𝑡0} \\ & =3𝑡.\end{aligned}


$$

So, $s= 3t,$ or equivalently $t = \dfrac{s}{3}.$

Now, we can define a new vector function $\mathbf{R}$ as

$$


\mathbf R(s)= \mathbf r\left(\dfrac{s}{3}\right) = \left\langle 2\sin \left(\dfrac{s}{3}\right), \: 2\cos \left(\dfrac{s}{3}\right), \: \sqrt{5} \left(\dfrac{s}{3}\right) \right\rangle .


$$

The function $\mathbf{R}(s)$ gives us the *same* curve $C,$ but this time it is parameterized by the arc length $s.$

In general, if $\mathbf r(t)$ for $t\in [a,b]$ is a continuously differentiable vector function such that $\mathbf r'(t)\neq \mathbf{0},$ then to parametrize it in terms of arc length we perform the following steps:

1. Compute $s = \displaystyle s(t) = \int_a^t\|\mathbf r'(u)\| \, \mathrm{d}u$

2. Write $s = s(t)$ in the form $t=t(s)$

3. Substitute $t=t(s)$ back into $\mathbf r(t)$ to get $\mathbf R(s)=\mathbf r(t(s))$

**Note:** One advantage of parametrizing a curve by its arc length is that the tangent vector is always a unit vector:

$$


\left\|\dfrac{\text{d}\mathbf R}{\text{d} s}\right\| = 1


$$

### Example: Parametrization of a Curve by Arc Length Given Its Arc Length

#### Question

Consider the curve $\mathbf r(t)=\left\langle 2t-1,\: 8t+2,\: -2t \right\rangle, \, t \geq 0,$ for which the arc length $s$ from $\mathbf{r}(0)$ to $\mathbf{r}(t)$ is given by $s=6\sqrt{2}t.$ Find $\mathbf R(s),$ the parametrization of the curve by its arc length $s.$

#### Explanation

First, since $s=6\sqrt{2}t,$ we have that

$$


\begin{aligned}6\sqrt{2}𝑡 & =𝑠 \\ 𝑡 & =\frac{𝑠}{6\sqrt{2}} \\ 𝑡 & =\frac{\sqrt{2}𝑠}{12}.\end{aligned}


$$

The vector function that pametrizes the curve $\mathbf r(t)$ by its arc length $s,$ with $s \geq 0,$ is given by

$$


\begin{aligned}𝐑(𝑠) & =𝐫(\frac{\sqrt{2}𝑠}{12}) \\ & =⟨2(\frac{\sqrt{2}𝑠}{12})−1,\,8(\frac{\sqrt{2}𝑠}{12})+2,\,−2(\frac{\sqrt{2}𝑠}{12})⟩ \\ & =⟨\frac{\sqrt{2}𝑠}{6}−1,\,\frac{4\sqrt{2}𝑠}{6}+2,\,−\frac{\sqrt{2}𝑠}{6}⟩ \\ & =\frac{1}{6}⟨\sqrt{2}𝑠−6,\,4\sqrt{2}𝑠+12,\,−\sqrt{2}𝑠⟩.\end{aligned}


$$

### Example: Finding a Unit Tangent Given the Parametrization of a Curve by Arc Length

#### Question

Given the curve $\mathbf r(t)=\cos{t}\,\mathbf i - \sin{t}\,\mathbf j+\sqrt{3}t\,\mathbf k, \, t \geq 0,$ for which the arc length $s$ from $\mathbf r(0)$ to $\mathbf r(t)$ is given by $s=2t,$ find the corresponding unit tangent $\mathbf{T}(s),$ parametrized by $s.$

#### Explanation

First, since $s=2t,$ we have that $t=\dfrac{s}{2}.$

Therefore, the vector function $\mathbf R(s)$ that parametrizes $\mathbf r(t)$ by its arc length is

$$


\begin{aligned}𝐑(𝑠) & =𝐫(\frac{𝑠}{2}) \\ & =cos⁡(\frac{𝑠}{2})\,𝐢−sin⁡(\frac{𝑠}{2})\,𝐣+\sqrt{3}⋅\frac{𝑠}{2}𝐤 \\ & =cos⁡(\frac{𝑠}{2})\,𝐢−sin⁡(\frac{𝑠}{2})\,𝐣+\frac{\sqrt{3}𝑠}{2}\,𝐤.\end{aligned}


$$

Now, since the curve is parametrized by its arc length $s,$ the unit tangent can be found as

$$


\mathbf T(s) = \dfrac{\text{d}}{\text{d}s}\mathbf R(s).


$$

So, we obtain

$$


\begin{aligned}𝐓(𝑠) & =\frac{d}{d𝑠}𝐑(𝑠) \\ & =\frac{d}{d𝑠}(cos⁡(\frac{𝑠}{2}))\,𝐢+\frac{d}{d𝑠}(−sin⁡(\frac{𝑠}{2}))𝐣+\frac{d}{d𝑠}(\frac{\sqrt{3}𝑠}{2})𝐤 \\ & =−\frac{1}{2}sin⁡(\frac{𝑠}{2})\,𝐢−\frac{1}{2}cos⁡(\frac{𝑠}{2})\,𝐣+\frac{\sqrt{3}}{2}\,𝐤 \\ & =\frac{1}{2}(−sin⁡(\frac{𝑠}{2})\,𝐢−cos⁡(\frac{𝑠}{2})\,𝐣+\sqrt{3}\,𝐤).\end{aligned}


$$

### Example: Finding the Parametrization of a Curve by Arc Length

#### Question

What is the parametrization of the curve $\mathbf r(t)=2(t\cos{t}-\sin{t})\,\mathbf i+2(t\sin{t}+\cos{t})\,\mathbf j, \, t \geq 0$ by its arc length $s?$

#### Explanation

First, we find $\mathbf{r}'(t)$ and its magnitude $\|\mathbf{r}'(t)\|\mathbin{:}$

$$


\begin{aligned}𝐫^{′}(𝑡) & =2\frac{d}{d𝑡}(𝑡cos⁡𝑡−sin⁡𝑡)\,𝐢+2\frac{d}{d𝑡}(𝑡sin⁡𝑡+cos⁡𝑡)\,𝐣 \\ & =2(cos⁡𝑡−𝑡sin⁡𝑡−cos⁡𝑡)\,𝐢+2(sin⁡𝑡+𝑡cos⁡𝑡−sin⁡𝑡)\,𝐣 \\ & =−2𝑡sin⁡𝑡\,𝐢+2𝑡cos⁡𝑡\,𝐣 \\ ‖𝑟^{′}(𝑡)‖ & =|2𝑡|\sqrt{(−sin⁡𝑡)^{2}+cos^{2}⁡𝑡} \\ & =2𝑡\end{aligned}


$$

Note that in the last step, we removed the absolute value bars since $t>0.$

Next, we calculate the arc length of the curve from $0$ to $t\mathbin{:}$

$$


\begin{aligned}𝑠 & =∫_{𝑡0}‖𝐫^{′}(𝑢)‖\,d𝑢 \\ & =∫_{𝑡0}2𝑢\,d𝑢 \\ & =𝑢^{2}_{𝑡0} \\ & =𝑡^{2}−0 \\ & =𝑡^{2}\end{aligned}


$$

Now, since $s=t^2,$ we have

$$


\begin{aligned}𝑡^{2} & =𝑠 \\ 𝑡 & =±\sqrt{𝑠} \\ 𝑡 & =\sqrt{𝑠},\end{aligned}


$$

taking the positive root because $t>0.$

Finally, the vector function that parametrizes $\mathbf r(t)$ by its arc length is given by

$$


\begin{aligned}𝐑(𝑠) & =𝐫(\sqrt{𝑠}) \\ & =2(\sqrt{𝑠}cos⁡\sqrt{𝑠}−sin⁡\sqrt{𝑠})\,𝐢+2(\sqrt{𝑠}sin⁡\sqrt{𝑠}+cos⁡\sqrt{𝑠})\,𝐣.\end{aligned}


$$
