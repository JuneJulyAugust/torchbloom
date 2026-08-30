# Applying Newton's Second Law in the Plane

Source: https://www.mathacademy.com/topics/3340?courseId=54
Topic ID: 3340

## Prerequisites

- [Finding Velocity Vectors in Two Dimensions Using Integration](../../../ap-courses/lessons/ap-calculus-bc/826-finding-velocity-vectors-in-two-dimensions-using-integration.md)
- [Newton's Second Law](./2722-newton-s-second-law.md)

## Lesson

### Introduction

**Newton's second law** states that the **resultant force** acting on a particle equals the product of its mass and acceleration:

$$


\mathbf F = m \mathbf a,


$$

where $\mathbf F$ is the resultant force, measured in **Newtons** $(\text N),$ $m$ is the mass, measured in $\textrm{kg},$ and $\mathbf a$ is the acceleration, measured in $\textrm{m/s}^2.$

Note the following:

- Force, like acceleration, is a *vector* quantity.

- The term "resultant force" means the (vector) sum of forces acting on the particle.

- When considering forces acting in one dimension, we usually write From this equation, we see that a $1\,\textrm{N}$ is the total force required to accelerate a mass of $m = 1\,\textrm{kg}$ at a rate of $a = 1\,\textrm{m/s}^2.$

Let's see a concrete example.

### A Worked Example

Suppose that the velocity $\mathbf v,$ in meters per second, of a particle $P$ of mass $2\,\textrm{kg}$ is given by

$$


\mathbf v = \langle t,\: t^2 \rangle,


$$

where $t \gt 0$ is the time in seconds.

Let's use Newton's second law to calculate the resultant force acting on this particle.

We start by calculating the acceleration vector by differentiating the velocity vector:

$$


\begin{aligned}𝐚 & =\frac{d𝐯}{d𝑡} \\ & =⟨\frac{d}{d𝑡}(𝑡),\,\frac{d}{d𝑡}(𝑡^{2})⟩ \\ & =⟨1,\,2𝑡⟩\end{aligned}


$$

So, the resultant force $\mathbf F$ at time $t$ equals

$$


\begin{aligned}𝐅 & =𝑚𝐚 \\ & =2⋅⟨1,\,2𝑡⟩ \\ & =⟨2,\,4𝑡⟩.\end{aligned}


$$

This gives the resultant force acting on the particle at time $t.$

To calculate the force at a particular moment, say, $t = 3\,\textrm s,$ we substitute this value into the expression for $\mathbf F{:}$

$$


\begin{aligned}𝐅(3)=⟨2,\,4(3)⟩=⟨2,\,12⟩\end{aligned}


$$

Therefore, the resultant force acting on $P$ when $t=3\,\textrm s$ equals $\left\langle 2,\: 12 \right\rangle\!\,\textrm N.$

### Example: Calculating the Resultant Force Acting on a Particle Given Its Velocity Vector

#### Question

The velocity $\mathbf v,$ in meters per second, of a particle $P$ of mass $5\,\textrm{kg}$ is given by

$$


\mathbf v = \langle 3e^{t},\: t^3-t^2\rangle,


$$

where $t\gt 0$ is the time in seconds. Calculate the magnitude of the resultant force acting on the particle when $t=2\,\textrm s.$ Round your final answer to the nearest Newton.

#### Explanation

Newton’s second law states that

$$


\mathbf F = m \mathbf a,


$$

where $\mathbf F$ is the ** force, $m$ is the mass, and $\mathbf a$ is the acceleration.

To compute the acceleration vector, we differentiate the velocity vector:

$$


\begin{aligned}𝐚 & =\frac{d𝐯}{d𝑡} \\ & =⟨\frac{d}{d𝑡}(3𝑒^{𝑡}),\,\frac{d}{d𝑡}(𝑡^{3}−𝑡^{2})⟩ \\ & =⟨3𝑒^{𝑡},\,3𝑡^{2}−2𝑡⟩\end{aligned}


$$

Therefore, the resultant force $\mathbf F$ at time $t$ equals

$$


\begin{aligned}𝐅 & =𝑚𝐚 \\ & =5⋅⟨3𝑒^{𝑡},\,3𝑡^{2}−2𝑡⟩ \\ & =⟨15𝑒^{𝑡},\,15𝑡^{2}−10𝑡⟩.\end{aligned}


$$

When $t = 2\,\textrm s,$ we have

$$


\begin{aligned}𝐅(2) & =⟨15𝑒^{2},\,15(2^{2})−10(2)⟩ \\ & =⟨15𝑒^{2},\,40⟩.\end{aligned}


$$

Finally, the magnitude of $\mathbf F(2)$ is given by

$$


\begin{aligned}|𝐅(2)| & =\sqrt{√(15𝑒^{2})^{2}+(40)^{2}} \\ & =\sqrt{√225𝑒^{4}+1\,600} \\ & ≈118\,N\end{aligned}


$$

rounded to the nearest Newton.

### Example: Calculating the Resultant Force Acting on a Particle Given Its Displacement Vector

#### Question

The displacement $\mathbf r,$ in meters, of a particle $P$ of mass $3\,\textrm{kg}$ is given by

$$


\mathbf r = \langle 3\cos{t}-\sin{t},\: 2\cos{t}\rangle,


$$

where $t\gt 0$ is the time in seconds. Calculate the resultant force acting on the particle when $t=\dfrac{3\pi}{4}\,\textrm s.$

#### Explanation

Newton’s second law states that

$$


\mathbf F = m \mathbf a,


$$

where $\mathbf F$ is the ** force, $m$ is the mass, and $\mathbf a$ is the acceleration.

To compute the acceleration vector, we first differentiate $\mathbf r$ to get the velocity vector:

$$


\begin{aligned}𝐯 & =\frac{d𝐫}{d𝑡} \\ & =⟨\frac{d}{d𝑡}(3cos⁡𝑡−sin⁡𝑡),\,\frac{d}{d𝑡}(2cos⁡𝑡)⟩ \\ & =⟨−3sin⁡𝑡−cos⁡𝑡,\,−2sin⁡𝑡⟩\end{aligned}


$$

Next, we differentiate the velocity vector to get the acceleration vector:

$$


\begin{aligned}𝐚 & =\frac{d𝐯}{d𝑡} \\ & =⟨\frac{d}{d𝑡}(−3sin⁡𝑡−cos⁡𝑡),\,\frac{d}{d𝑡}(−2sin⁡𝑡)⟩ \\ & =⟨−3cos⁡𝑡+sin⁡𝑡,\,−2cos⁡𝑡⟩\end{aligned}


$$

Therefore, the resultant force $\mathbf F$ at time $t$ equals

$$


\begin{aligned}𝐅 & =𝑚𝐚 \\ & =3⋅⟨−3cos⁡𝑡+sin⁡𝑡,\,−2cos⁡𝑡⟩ \\ & =⟨3sin⁡𝑡−9cos⁡𝑡,\,−6cos⁡𝑡⟩.\end{aligned}


$$

Finally, when $t = \dfrac{3\pi}{4}\,\textrm s,$ we have

$$


\begin{aligned}𝐅(\frac{3𝜋}{4}) & =⟨3sin⁡(\frac{3𝜋}{4})−9cos⁡(\frac{3𝜋}{4}),\,−6cos⁡(\frac{3𝜋}{4})⟩ \\ & =⟨\frac{3\sqrt{√2}}{2}+\frac{9\sqrt{√2}}{2},\,\frac{6\sqrt{√2}}{2}⟩ \\ & =⟨6\sqrt{√2},\,3\sqrt{√2}⟩.\end{aligned}


$$

Therefore, we conclude that the resultant force acting on $P$ when $t=\dfrac{3\pi}{4}\,\textrm s$ equals $\left\langle 6\sqrt{2},\: 3\sqrt{2}\right\rangle\,\textrm N.$

### Example: Working With Resultant Forces

#### Question

A particle $P$ of mass $6\,\textrm{kg}$ is subject to the external forces $\mathbf F_1$ and $\mathbf F_2,$ given by

$$


\mathbf F_1 = \left\langle \dfrac2{t+1}+12t,\: \dfrac3{\sqrt t} \right\rangle, \qquad \mathbf F_2 = \left\langle \dfrac 4{t+1},\: 6\right\rangle,


$$

where $\mathbf F_1$ and $\mathbf F_2$ are measured in Newtons and $t > 0$ is the time, in seconds. Given that the velocity of $P$ equals $\langle -\ln 3,\:-2\rangle\,\textrm{m/s}$ when $t=0\,\textrm s,$ calculate the speed of $P$ when $t=2\,\textrm s.$

#### Explanation

Newton's second law states that

$$


\mathbf F = m \mathbf a,


$$

where $\mathbf F$ is the ** force, $m$ is the mass, and $\mathbf a$ is the acceleration.

The resultant force $\mathbf F$ acting on $P$ equals the sum of the forces acting on $P.$ Therefore,

$$


\begin{aligned}𝐅 & =𝐅_{1}+𝐅_{2} \\ & =⟨\frac{2}{𝑡+1}+12𝑡,\,\frac{3}{\sqrt{√𝑡}}⟩+⟨\frac{4}{𝑡+1},\,6⟩ \\ & =⟨\frac{6}{𝑡+1}+12𝑡,\,\frac{3}{\sqrt{√𝑡}}+6⟩.\end{aligned}


$$

By Newton's second law, we have

$$


\begin{aligned}𝐚 & =\frac{𝐅}{𝑚} \\ & =\frac{1}{6}⋅⟨\frac{6}{𝑡+1}+12𝑡,\,\frac{3}{\sqrt{√𝑡}}+6⟩ \\ & =⟨\frac{1}{𝑡+1}+2𝑡,\,\frac{1}{2\sqrt{√𝑡}}+1⟩.\end{aligned}


$$

To compute the velocity vector $\mathbf v,$ we need to integrate the acceleration vector:

$$


\begin{aligned}𝐯 & =∫𝐚\,d𝑡 \\ & =∫⟨\frac{1}{𝑡+1}+2𝑡,\,\frac{1}{2\sqrt{√𝑡}}+1⟩\,d𝑡 \\ & =⟨∫(\frac{1}{𝑡+1}+2𝑡)\,d𝑡,\,∫(\frac{1}{2\sqrt{√𝑡}}+1)\,d𝑡⟩ \\ & =⟨ln⁡(𝑡+1)+𝑡^{2},\,\sqrt{√𝑡}+𝑡⟩+𝐂\end{aligned}


$$

where $\mathbf C$ is a (vector) constant of integration.

We can solve for $\mathbf C$ by substituting $\mathbf v = \langle -\ln 3,\:-2\rangle\,\textrm{m/s}$ and $t=0\,\textrm s$ into the above, as follows:

$$


\begin{aligned}⟨−ln⁡3,\,−2⟩ & =⟨ln⁡(0+1)+0^{2},\,\sqrt{√0}+0⟩+𝐂 \\ ⟨−ln⁡3,\,−2⟩ & =⟨0,\,0⟩+𝐂 \\ 𝐂 & =⟨−ln⁡3,\,−2⟩\end{aligned}


$$

Therefore, the velocity of $P$ at time $t$ is given by

$$


\begin{aligned}𝐯 & =⟨ln⁡(𝑡+1)+𝑡^{2},\,\sqrt{√𝑡}+𝑡⟩+⟨−ln⁡3,\,−2⟩ \\ & =⟨ln⁡(𝑡+1)+𝑡^{2}−ln⁡3,\,\sqrt{√𝑡}+𝑡−2⟩.\end{aligned}


$$

When $t=2,$ the velocity equals

$$


\begin{aligned}𝐯(2) & =⟨ln⁡(2+1)+2^{2}−ln⁡3,\,\sqrt{√2}+2−2⟩ \\ & =⟨4,\,\sqrt{√2}⟩.\end{aligned}


$$

Finally, the speed of $P$ when $t=2$ equals the magnitude of $\mathbf v(2).$ Therefore,

$$


\begin{aligned}|𝐯(2)| & =\sqrt{√4^{2}+(\sqrt{√2})^{2}} \\ & =\sqrt{√16+2} \\ & =\sqrt{√18} \\ & =3\sqrt{√2}\,m/s.\end{aligned}


$$
