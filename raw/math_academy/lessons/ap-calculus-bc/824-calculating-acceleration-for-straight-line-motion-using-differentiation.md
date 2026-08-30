# Calculating Acceleration for Straight-Line Motion Using Differentiation

Source: https://www.mathacademy.com/topics/824?courseId=21
Topic ID: 824

## Prerequisites

- [Second and Higher-Order Derivatives](../ap-calculus-ab/281-second-and-higher-order-derivatives.md)
- [Calculating Velocity for Straight-Line Motion Using Differentiation](../ap-calculus-ab/284-calculating-velocity-for-straight-line-motion-using-differentiation.md)
- [Speed-Time Graphs](../algebra-i/2327-speed-time-graphs.md)

## Lesson

### Introduction

Suppose that you are riding a bicycle and you are changing velocity as you go. How can we calculate your acceleration at a given time?

The **acceleration** $a(t)$ is defined as the derivative of the velocity $v(t)$ with respect to time:

$$


a(t) = \frac{\textrm{d}v}{\textrm{d}t}.


$$

So, if we know how the velocity changes with time (that is, if we know $v(t)$), we can calculate the acceleration by simply differentiating the velocity $v(t)$.

### Example: Calculating the Acceleration of a Particle Given Its Velocity

#### Question

The velocity $v$ of a particle at time $t$ is given by $v(t) = -6t-3t^2$. Calculate the acceleration of the particle at time $t$.

#### Explanation

We differentiate $v(t)$ to calculate $a(t)$:

$$


\begin{aligned}𝑎(𝑡) & =\frac{d𝑣}{d𝑡} \\ & =\frac{d}{d𝑡}(−6𝑡−3𝑡^{2}) \\ & =−6−6𝑡 \\ & =−6(1+𝑡).\end{aligned}


$$

### Calculating the Acceleration Given the Displacement

If we only know how the position of a particle changes with time, but not the velocity, we can still find the acceleration by differentiating the position function $x(t)$ twice. In fact,

$$


\begin{aligned}𝑎(𝑡) & =\frac{d𝑣}{d𝑡} \\ & =\frac{d}{d𝑡}(\frac{d𝑥}{d𝑡}) \\ & =\frac{d^{2}𝑥}{d𝑡^{2}}.\end{aligned}


$$

### Example: Calculating the Acceleration of a Particle at a Particular Moment Given Its Position

#### Question

The position $x$ of a particle at time $t$ is given by $x(t) = 1+2t+3t^2+4t^3$. Calculate the acceleration of the particle at time $t=0$.

#### Explanation

First, we calculate $v(t)$ by differentiating $x(t)$:

$$


\begin{aligned}𝑣(𝑡) & =\frac{d𝑥}{d𝑡} \\ & =\frac{d}{d𝑡}(1+2𝑡+3𝑡^{2}+4𝑡^{3}) \\ & =2+6𝑡+12𝑡^{2}.\end{aligned}


$$

Now, we differentiate $v(t)$ to find $a(t)$:

$$


\begin{aligned}𝑎(𝑡) & =\frac{d𝑣}{d𝑡} \\ & =\frac{d}{d𝑡}(2+6𝑡+12𝑡^{2}) \\ & =6+24𝑡.\end{aligned}


$$

To calculate the acceleration at time $t=0$, we substitute this into the above:

$$


\begin{aligned}𝑎(0) & =6+24(0) \\ & =6.\end{aligned}


$$

Therefore, the acceleration when $t=0$ is $6$.

### Intuition Behind the Definition of Acceleration

The acceleration of a particle is defined as

$$


a(t) = \frac{\textrm{d}v}{\textrm{d}t},


$$

but where does this definition come from?

Suppose that you are riding a bike with a constant acceleration. This means that your velocity increases (or decreases) at a constant rate. For example, if you start from stationary ($v=0$) and after $10\,\textrm{s}$ your velocity is $v=5\,\textrm{m/s}$, the acceleration is given by the change of velocity with time:

$$


\begin{aligned}𝑎 & =\frac{Δ𝑣}{Δ𝑡} \\ & =\frac{5}{10} \\ & =0.5\,m/s^{2}.\end{aligned}


$$

This process works only if the acceleration is constant. If the acceleration is *not* constant, then the formula above only gives the *average* acceleration.

Now suppose that the acceleration is not constant. To find a more precise estimate for the acceleration at time $t,$ we would need to apply the above formula with a small time interval, i.e.,

$$


a\approx \dfrac{\Delta v}{\Delta t},


$$

where it's assumed that $\Delta t$ is very small.

Now, by taking the limit as $\Delta t\to 0,$ we can get an *exact* value for the acceleration at time $t\mathbin{:}$

$$


\begin{aligned}𝑎(𝑡) & =\underset{Δ𝑡→0}{lim}\frac{Δ𝑣}{Δ𝑡} \\ & =\frac{d𝑣}{d𝑡},\end{aligned}


$$

which is the rate of change of the velocity.
