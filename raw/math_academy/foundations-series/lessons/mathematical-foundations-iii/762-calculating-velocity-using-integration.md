# Calculating Velocity Using Integration

Source: https://www.mathacademy.com/topics/762?courseId=136
Topic ID: 762

## Prerequisites

- [Integrating Trigonometric Functions Using Substitution](./478-integrating-trigonometric-functions-using-substitution.md)
- [Calculating Acceleration for Straight-Line Motion Using Differentiation](./824-calculating-acceleration-for-straight-line-motion-using-differentiation.md)
- [Integrating Exponential Functions Using Substitution](./3770-integrating-exponential-functions-using-substitution.md)

## Lesson

### Introduction

For a particle moving along a straight line with velocity $v(t),$ we calculate the acceleration $a(t)$ by differentiating $v$ with respect to $t.$ But what if we're given the acceleration and want to find the velocity?

We need to do the reverse operation of differentiation, which is integration. So, we integrate $a(t)$ with respect to $t\mathbin{:}$

$$


a(t) = \frac{\text{d}v}{\text{d}t} \quad\Longrightarrow\quad v(t) = \int a(t)\text{d}t.


$$

We determine the arbitrary constant of integration using some information that's known about the system.

### Example: Finding the Velocity of a Particle Whose Acceleration Is Given By a Polynomial

#### Question

A particle moves along a straight line relative to a fixed origin $O$ with acceleration, measured in $\textrm m / \textrm s^2,$ given by the function $a(t) = 4t^2 - 3t^3,$ where $t$ is the time in seconds. If the particle has velocity $v=2\,\textrm m / \textrm s$ when $t=0 \,\textrm s,$ calculate the velocity (in $\textrm m / \textrm s$) of the particle at time $t.$

#### Explanation

First, we find $v(t)$ by integrating the acceleration with respect to time:

$$


\begin{aligned}𝑣(𝑡) & =∫𝑎(𝑡)d𝑡 \\ & =∫(4𝑡^{2}−3𝑡^{3})d𝑡 \\ & =\frac{4}{3}𝑡^{3}−\frac{3}{4}𝑡^{4}+𝐶\end{aligned}


$$

To determine $C,$ we use the fact that $v(0) = 2.$ Substituting this into the above gives

$$


\begin{aligned}2 & =\frac{4}{3}(0)^{3}−\frac{3}{4}(0)^{4}+𝐶 \\ 𝐶 & =2.\end{aligned}


$$

Therefore, the velocity $v$ of the particle at time $t$ is $v(t) = \dfrac{4}{3}t^3 -\dfrac{3}{4}t^4 + 2.$

### Example: Finding the Velocity of a Particle Whose Acceleration Is Not a Polynomial

#### Question

A particle moves along a straight line relative to a fixed origin $O$ with acceleration, measured in $\textrm m / \textrm s^2,$ given by the function $a(t) =2e^{-t}+6t^2$, where $t$ is the time in seconds. If the particle has velocity $v=-4 \,\textrm m / \textrm s$ when $t=0 \,\textrm s,$ calculate the speed of the particle at the moment $t=1\,\text{s}.$

#### Explanation

First, we find $v(t)$ by integrating the acceleration with respect to time:

$$


\begin{aligned}𝑣(𝑡) & =∫𝑎(𝑡)d𝑡 \\ & =∫(2𝑒^{−𝑡}+6𝑡^{2})d𝑡 \\ & =2(−𝑒^{−𝑡})+\frac{6}{3}𝑡^{3}+𝐶 \\ & =−2𝑒^{−𝑡}+2𝑡^{3}+𝐶\end{aligned}


$$

To determine $C$, we use the fact that $v(0) = -4.$ Substituting this into the above gives

$$


\begin{aligned}−4 & =−2𝑒^{−0}+2⋅0^{3}+𝐶 \\ −4 & =−2+0+𝐶 \\ 𝐶 & =−2.\end{aligned}


$$

Therefore, the velocity $v$ of the particle at time $t$ is $v(t) = -2 e^{-t}+ 2t^3 -2.$

We evaluate the velocity at time $t=1\,\text{s}\mathbin{:}$

$$


\begin{aligned}𝑣(1) & =−2𝑒^{−1}+2(1)^{3}−2 \\ & =−2𝑒^{−1}+2−2 \\ & =−\frac{2}{𝑒}\,m/s\end{aligned}


$$

Finally, since the speed is equal to $|v(t)|,$ we conclude that the speed of the particle is $\dfrac 2 e\,\text{m/s}.$
