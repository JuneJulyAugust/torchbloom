# Calculating the Position Function of a Particle Using Integration

Source: https://www.mathacademy.com/topics/335?courseId=106
Topic ID: 335

## Prerequisites

- [Calculating Velocity Using Integration](./762-calculating-velocity-using-integration.md)
- [Integrating Logarithmic Functions Using Substitution](./1161-integrating-logarithmic-functions-using-substitution.md)
- [Calculating Distance From a Speed-Time Graph](../../../high-school/traditional/lessons/algebra-i/1590-calculating-distance-from-a-speed-time-graph.md)

## Lesson

### Introduction

For a particle moving along a straight line with position $x(t),$ we calculate the velocity $v(t)$ by differentiating $x$ with respect to $t.$ This means that $x(t)$ is the antiderivative of the velocity $v(t).$

Therefore, to find the position $x(t)$ of a particle given its velocity $v(t),$ we integrate $v(t)$ with respect to $t\mathbin{:}$

$$


v(t) = \frac{\text{d}x}{\text{d}t} \quad\Rightarrow\quad x(t) = \int v(t) \, \text{d}t.


$$

We determine the arbitrary constant of integration using some information that's known about the system.

### Example: Determining the Position of a Particle Given Its Velocity and Initial Position

#### Question

A particle moves along a straight line relative to a fixed origin $O$ with velocity $v(t) = 2t+3t^2,$ where $t\geq 0$ is the time. If the particle is at the position $x=1$ when $t=0,$ calculate the position $x$ of the particle at time $t.$

#### Explanation

We start by integrating the velocity to get $x(t)\mathbin{:}$

$$


\begin{aligned}𝑥(𝑡) & =∫𝑣(𝑡)\,d𝑡 \\ & =∫(2𝑡+3𝑡^{2})\,d𝑡 \\ & =𝑡^{2}+𝑡^{3}+𝐶\end{aligned}


$$

To determine $C,$ we use the fact that $x(0) = 1.$ Substituting this into the above gives

$$


\begin{aligned}1 & =(0)^{2}+(0)^{3}+𝐶 \\ 𝐶 & =1.\end{aligned}


$$

Therefore, the position $x$ of the particle at time $t$ is

$$


x(t) = t^3+t^2+1.


$$

### Example: Determining the Position of a Particle Given Its Acceleration, Initial Velocity and Initial Position

#### Question

A particle moves along a straight line relative to a fixed origin $O$ with acceleration $a(t) = 1-2t,$ where $t\geq 0$ is the time. If the particle has position $x=1$ and velocity $v=2$ when $t=1,$ calculate the position $x$ of the particle at time $t >0.$

#### Explanation

We start by integrating the acceleration to get the velocity $v(t)\mathbin{:}$

$$


\begin{aligned}𝑣(𝑡) & =∫𝑎(𝑡)\,d𝑡 \\ & =∫(1−2𝑡)\,d𝑡 \\ & =𝑡−𝑡^{2}+𝐶\end{aligned}


$$

To determine $C,$ we use the fact that $v(1) = 2.$ Substituting this into the above gives

$$


\begin{aligned}2 & =(1)−(1)^{2}+𝐶 \\ 𝐶 & =2.\end{aligned}


$$

So the velocity is given by $v(t) = t-t^2 + 2.$

Now, we integrate the velocity to get $x(t)\mathbin{:}$

$$


\begin{aligned}𝑥(𝑡) & =∫𝑣(𝑡)\,d𝑡 \\ & =∫(𝑡−𝑡^{2}+2)\,d𝑡 \\ & =\frac{1}{2}𝑡^{2}−\frac{1}{3}𝑡^{3}+2𝑡+𝐾\end{aligned}


$$

To determine $K,$ we use the fact that $x(1) = 1.$ Substituting this into the above gives

$$


\begin{aligned}1 & =\frac{1}{2}(1)^{2}−\frac{1}{3}(1)^{3}+2(1)+𝐾 \\ 𝐾 & =−\frac{7}{6}.\end{aligned}


$$

Therefore, the position $x$ of the particle at time $t$ is

$$


x(t) = \dfrac{1}{2}t^2-\dfrac{1}{3}t^3 +2t -\dfrac{7}{6}.


$$
