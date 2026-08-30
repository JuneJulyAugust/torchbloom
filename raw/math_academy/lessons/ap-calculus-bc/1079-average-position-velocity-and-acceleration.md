# Average Position, Velocity, and Acceleration

Source: https://www.mathacademy.com/topics/1079?courseId=21
Topic ID: 1079

## Prerequisites

- [Calculating Acceleration for Straight-Line Motion Using Differentiation](../ap-calculus-ab/824-calculating-acceleration-for-straight-line-motion-using-differentiation.md)
- [The Average Value of a Function](../ap-calculus-ab/1203-the-average-value-of-a-function.md)

## Lesson

### Introduction

For a particle with position $x(t),$ the **average velocity** of the particle over the time interval $[a,b]$ is given by the average rate of change of position:

$$


v_{\textrm{avg}} = \dfrac{\Delta x}{\Delta t} = \dfrac{x(b) - x(a)}{b-a}.


$$

Similarly, the **average acceleration** of a particle with velocity $v(t)$ over the time interval $[a,b]$ is given by the average rate of change of velocity:

$$


a_{\textrm{avg}} = \dfrac{\Delta v}{\Delta t} = \dfrac{v(b) - v(a)}{b-a}.


$$

To demonstrate, suppose that a particle moves along a straight line, and its position (in meters) relative to a fixed origin $O$ is given by the function

$$


x(t) = 2t^3,


$$

where $t \geq 0$ is the time measured in seconds. The average velocity of the particle over the time interval $[0,1]$ is

$$


\begin{aligned}𝑣_{avg}=\frac{Δ𝑥}{Δ𝑡}=\frac{𝑥(1)−𝑥(0)}{1−0}=\frac{2(1)^{3}−2(0)^{3}}{1−0}=2\,m/s.\end{aligned}


$$

Likewise, the velocity is $v(t) = x'(t) = 6t^2,$ so the average acceleration of the particle over the time interval $[0,1]$ is

$$


\begin{aligned}𝑎_{avg}=\frac{Δ𝑣}{Δ𝑡}=\frac{𝑣(1)−𝑣(0)}{1−0}=\frac{6(1)^{2}−6(0)^{2}}{1−0}=6\,m/s^{2}.\end{aligned}


$$

### Example: Calculating the Average Velocity of a Particle Given Its Position Function

#### Question

A particle moves on a line such that after $t$ seconds it is $e^t+4t$ meters from a fixed origin $O.$ Find the average velocity of the particle over the time interval $[0,2].$

#### Explanation

The average velocity is the average rate of change of the position, so

$$


\begin{aligned}𝑣_{avg} & =\frac{𝑥(𝑏)−𝑥(𝑎)}{𝑏−𝑎} \\ & =\frac{𝑥(2)−𝑥(0)}{2−0} \\ & =\frac{(𝑒^{2}+4(2))−(𝑒^{0}+4(0))}{2} \\ & =\frac{𝑒^{2}+7}{2}.\end{aligned}


$$

Therefore, the average velocity is $\dfrac {e^2+7} {2} \, \textrm{m}/\textrm{sec}.$

### Example: Calculating the Average Acceleration of a Particle Given Its Velocity Function

#### Question

A train is moving west with velocity $v(t)=t+\sqrt{t},$ where $t > 0$ is the time in minutes and $v$ is measured in miles per minute. Find the average acceleration of the train between $1$ and $4$ minutes.

#### Explanation

The average acceleration is the average rate of change of the velocity, so

$$


\begin{aligned}𝑎_{avg} & =\frac{𝑣(𝑏)−𝑣(𝑎)}{𝑏−𝑎} \\ & =\frac{𝑣(4)−𝑣(1)}{4−1} \\ & =\frac{(4+\sqrt{√4})−(1+\sqrt{√1})}{3} \\ & =\frac{6−2}{3} \\ & =\frac{4}{3}.\end{aligned}


$$

Therefore, the average acceleration is $\dfrac{4}{3} \, \textrm{mi}/\textrm{min}^2.$

### Calculating Average Velocity Using Integration

So, we now know how to find

- the average *velocity* (given the *position*), and

- the average *acceleration* (given the *velocity*).

But what if we are given the *velocity* and asked to find the average *velocity*? That's a bit trickier. However, we can solve this problem by recalling that the average value of a function $v(t)$ over the interval $[t_1,t_2]$ is given by

$$


v_{\textrm{avg}} = \dfrac{1}{t_2-t_1}\int_{t_1}^{t_2} v(t)\,\textrm d t.


$$

### Example: Calculating the Average Velocity of a Particle Using Integration

#### Question

A weight attached to a spring oscillates in the vertical direction with velocity $v(t)=2\pi\sin(\pi t)\,\textrm{cm/s},$ where $t\geq 0$ is the time in seconds. Find the average velocity of the weight on the interval $[0, 1].$

#### Explanation

To calculate the average value of the velocity on $[t_1,t_2],$ we use the average value formula

$$


v_{\textrm{avg}} = \dfrac {1}{t_2-t_1}\, \int_{t_1}^{t_2} v(t) \, \textrm dt.


$$

So, we get

$$


\begin{aligned}𝑣_{avg} & =\frac{1}{1−0}\,∫_{10}^{}2𝜋sin⁡(𝜋𝑡)\,d𝑡 \\ & =2𝜋(−\frac{1}{𝜋}cos⁡(𝜋𝑡))_{10}^{} \\ & =−2(cos⁡𝜋−cos⁡0) \\ & =−2(−1−1) \\ & =4.\end{aligned}


$$

Therefore, the average velocity is $4 \, \textrm{cm/s}.$

### Calculating Average Position and Acceleration Using Integration

We can also calculate the average position $x_{\textrm{avg}}$ and average acceleration $a_{\textrm{avg}}$ of a particle over an interval $[t_1, t_2]$ using the following formulas:

$$


\begin{aligned}𝑥_{avg}=\frac{1}{𝑡_{2}−𝑡_{1}}∫_{𝑡_{2}𝑡_{1}}^{}𝑥(𝑡)\,d𝑡 \\ 𝑎_{avg}=\frac{1}{𝑡_{2}−𝑡_{1}}∫_{𝑡_{2}𝑡_{1}}^{}𝑎(𝑡)\,d𝑡\end{aligned}


$$

### Example: Calculating the Average Position or Acceleration of a Particle Using Integration

#### Question

A particle’s position relative to a fixed origin $O$ is given by the function $x(t) = \dfrac{3}{t} + 2t$ meters, where $t$ is time in seconds. Find the average position of the particle between $1$ and $2$ seconds.

#### Explanation

To calculate the average value of the position on $[t_1,t_2],$ we use the average value formula

$$


x_{\textrm{avg}} = \dfrac {1}{t_2-t_1}\, \int_{t_1}^{t_2} x(t) \, \textrm dt.


$$

So, we get

$$


\begin{aligned}𝑥_{avg} & =\frac{1}{2−1}\,∫_{21}^{}(\frac{3}{𝑡}+2𝑡)d𝑡 \\ & =(3ln⁡|𝑡|+𝑡^{2})_{21}^{} \\ & =(3ln⁡|2|+2^{2})−(3ln⁡|1|+1^{2}) \\ & =(3ln⁡2+4)−(0+1) \\ & =3+3ln⁡2.\end{aligned}


$$

Therefore, the average position is $(3 + 3 \ln 2) \, \textrm{m}.$
