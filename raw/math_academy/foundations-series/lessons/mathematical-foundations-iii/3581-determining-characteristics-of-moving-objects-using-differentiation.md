# Determining Characteristics of Moving Objects Using Differentiation

Source: https://www.mathacademy.com/topics/3581?courseId=136
Topic ID: 3581

## Prerequisites

- [Calculating Acceleration for Straight-Line Motion Using Differentiation](./824-calculating-acceleration-for-straight-line-motion-using-differentiation.md)
- [Solving Inequalities Involving Exponential Functions](./2857-solving-inequalities-involving-exponential-functions.md)
- [Solving Inequalities Involving Logarithmic Functions](./2858-solving-inequalities-involving-logarithmic-functions.md)
- [Solving Inequalities Involving Exponential Functions and Polynomials](./2859-solving-inequalities-involving-exponential-functions-and-polynomials.md)
- [Solving Rational Inequalities](./3355-solving-rational-inequalities.md)

## Lesson

### Introduction

When a particle moves along a straight line relative to a fixed origin $O,$ it moves in one of two directions:

- the particle moves in the direction of increasing $x$ (positive direction) when its velocity is positive, and

- the particle moves in the direction of decreasing $x$ (negative direction) when its velocity is negative.

Suppose the position of the particle (in meters) at time $t$ seconds is given by

$$


s(t) = 3t^2-t^3, \qquad t > 0.


$$

Recall that we find the velocity of the particle by taking the derivative of the position function, as follows:

$$


\begin{aligned}𝑣(𝑡) & =\frac{d𝑠}{d𝑡} \\ & =\frac{d}{d𝑡}(3𝑡^{2}−𝑡^{3}) \\ & =6𝑡−3𝑡^{2}\end{aligned}


$$

From the resulting velocity function above, we can find some characteristics of the particle.

- *Time intervals in which the particle is moving in the direction of increasing $x.$* This occurs when its velocity is positive. Solving the inequality $v(t) > 0$ for the particle described above, we get Note we can divide through by $t$ without changing the inequality since $t > 0.$ Therefore, the time interval in which the particle is moving to the direction of increasing $x$ is $t\in (0,2).$

- *Time intervals in which the particle is moving in the direction of decreasing $x.$* This occurs when its velocity is negative. Solving the inequality $v(t) < 0$ for the particle described above, we get Note we can divide through by $t$ without changing the inequality since $t > 0.$ Therefore, the time interval in which the particle is moving to the direction of decreasing $x$ is $t\in (2,\infty).$

- *Moments when the particle is stationary.* The particle is stationary when $v=0\,\textrm{m}/\textrm{s}.$ So, we set $v=0$ and solve for $t{:}$ The solutions are $t=0$ and $t=2.$ So the particle is stationary at $t=0\,\textrm{s}$ and $t=2\,\textrm{s}.$

- *Moments when the acceleration of the particle is zero.* For the particle above, we differentiate $v(t)$ to find $a(t)$ as follows: Then, we put $a=0$ into the above to find the time when the acceleration is zero: Therefore, the acceleration is zero when $t=1.$

### Example: Finding a Moment in Time When a Particle is Stationary

#### Question

The position $s(t)$ of a particle (in meters) at time $t$ seconds is given by

$$


s(t) = -\frac{1}{3}t^3 + \frac{5}{2}t^2 + 6t + 1,\quad t\geq 0.


$$

Calculate the time at which the particle is stationary, and give the displacement of the particle from the origin at this time.

#### Explanation

The particle is stationary when its velocity is zero. So first, we need to calculate the velocity function. We can do that by taking the derivative of the position function, as follows:

$$


\begin{aligned}𝑣(𝑡) & =\frac{d𝑠}{d𝑡} \\ & =\frac{d}{d𝑡}(−\frac{1}{3}𝑡^{3}+\frac{5}{2}𝑡^{2}+6𝑡+1) \\ & =−𝑡^{2}+5𝑡+6\end{aligned}


$$

The particle is stationary when $v=0\, \textrm{m/s}$. So, we set $v = 0$ and solve for $t \mathbin{:}$

$$


\begin{aligned}0 & =−𝑡^{2}+5𝑡+6 \\ 0 & =𝑡^{2}−5𝑡−6 \\ 0 & =(𝑡−6)(𝑡+1)\end{aligned}


$$

The solutions are $t=6$ and $t=-1.$ Since $t\geq 0,$ we discard the solution $t=-1$ and keep only $t=6.$

So the particle is stationary only at $t=6\, \textrm{s}.$ To find the displacement from the origin at this time, we substitute $t=6$ back into $s(t)$ and get

$$


\begin{aligned}𝑠(6) & =−\frac{1}{3}⋅6^{3}+\frac{5}{2}⋅6^{2}+6⋅6+1 \\ & =−72+90+36+1 \\ & =55\,m.\end{aligned}


$$

Therefore, the particle is stationary at $t = 6\, \textrm{s}$ and its displacement from the origin at this time is $55\, \textrm{m}.$

### Example: Determining Intervals of Increasing or Decreasing Displacement

#### Question

The displacement $s,$ in meters, relative to a fixed origin $O$ of a particle moving in a straight line along the $x$-axis is given by $s(t) = t^4 - 32t$, where $t \geq 0$ is the time measured in seconds. Determine the time intervals in which the particle is moving in the direction of decreasing $x.$

#### Explanation

If the particle moves in the direction of decreasing $x,$ then its velocity is negative.

First, we calculate the velocity function by differentiating the position function:

$$


\begin{aligned}𝑣(𝑡) & =\frac{d𝑠}{d𝑡} \\ & =\frac{d}{d𝑡}(𝑡^{4}−32𝑡) \\ & =4𝑡^{3}−32\end{aligned}


$$

To calculate time intervals in which the particle is moving in the direction of decreasing $x$, we solve the inequality $v(t) < 0\mathbin{:}$

$$


\begin{aligned}𝑣(𝑡) & <0 \\ 4𝑡^{3}−32 & <0 \\ 4𝑡^{3} & <32 \\ 𝑡^{3} & <8 \\ 𝑡 & <2\end{aligned}


$$

Hence, the time interval in which the particle is moving to the direction of decreasing $x$ is $t\in\left[0, 2\right).$

### Example: Calculating the Velocity of a Particle at the Moment When Its Acceleration is Zero

#### Question

A particle $P$ is traveling along the $x$-axis with displacement $s(t)$ from a fixed origin $O$ given by

$$


s(t) = t^3-3t^2+12t,\quad t\geq 0.


$$

Find the time at which the acceleration is zero, and find the value of the velocity at this moment.

#### Explanation

First, we calculate $v(t)$ by differentiating $s(t)$:

$$


\begin{aligned}𝑣(𝑡) & =\frac{d𝑠}{d𝑡} \\ & =\frac{d}{d𝑡}(𝑡^{3}−3𝑡^{2}+12𝑡) \\ & =3𝑡^{2}−6𝑡+12\end{aligned}


$$

Now, we differentiate $v(t)$ to find $a(t)$:

$$


\begin{aligned}𝑎(𝑡) & =\frac{d𝑣}{d𝑡} \\ & =\frac{d}{d𝑡}(3𝑡^{2}−6𝑡+12) \\ & =6𝑡−6\end{aligned}


$$

Next, we put $a=0$ to find the time when the acceleration is zero:

$$


\begin{aligned}0 & =6𝑡−6 \\ 6𝑡 & =6 \\ 𝑡 & =1\end{aligned}


$$

So the acceleration is zero when $t=1$. To find the velocity at this moment, we substitute this back into $v(t)$ to get

$$


v(1) = 3(1)^2 - 6(1)+12 = 9.


$$
