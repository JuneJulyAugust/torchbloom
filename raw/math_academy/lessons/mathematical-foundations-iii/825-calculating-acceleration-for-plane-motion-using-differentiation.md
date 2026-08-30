# Calculating Acceleration for Plane Motion Using Differentiation

Source: https://www.mathacademy.com/topics/825?courseId=136
Topic ID: 825

## Prerequisites

- [Calculating Velocity for Plane Motion Using Differentiation](./763-calculating-velocity-for-plane-motion-using-differentiation.md)

## Lesson

### Introduction

When a particle moves in two dimensions, we find the acceleration vector $\mathbf{a}$ by differentiating the velocity vector $\mathbf{v} = \left< u,\, v \right>$ with respect to $t\mathbin{:}$

$$


\begin{aligned}𝐚=\frac{d𝐯}{d𝑡}=⟨\frac{d𝑢}{d𝑡},\frac{d𝑣}{d𝑡}⟩\end{aligned}


$$

In other words, we need to differentiate both components of the velocity to get the acceleration.

### Example: Finding the Acceleration Vector of a Particle Given Its Velocity Vector

#### Question

The velocity vector $\mathbf{v} = \langle u, v \rangle$ of a particle $P$ at time $t$ is given by

$$


\mathbf{v} = \langle 12t+t^2, t^3+1\rangle.


$$

Calculate the acceleration vector $\mathbf{a}$.

#### Explanation

To compute the acceleration vector, we differentiate the velocity vector:

$$


\begin{aligned}𝐚 & =\frac{d𝐯}{d𝑡} \\ & =⟨\frac{d𝑢}{d𝑡},\,\frac{d𝑣}{d𝑡}⟩ \\ & =⟨\frac{d}{d𝑡}(12𝑡+𝑡^{2}),\,\frac{d}{d𝑡}(𝑡^{3}+1)⟩ \\ & =⟨12+2𝑡,\,3𝑡^{2}⟩\end{aligned}


$$

### Example: Computing the Acceleration of a Particle at a Given Moment Given Its Velocity Vector

#### Question

The velocity vector $\mathbf{v} = \langle u, v \rangle,$ measured in $\textrm{m}/\textrm s,$ of a particle $P$ at time $t$ seconds, is given by

$$


\mathbf{v} = \langle t^4-t^2, 2t^3\rangle.


$$

Find the acceleration vector and the magnitude of the acceleration of $P$ at time $t=1.$

#### Explanation

To compute the acceleration vector, we differentiate the velocity vector:

$$


\begin{aligned}𝐚 & =\frac{d𝐯}{d𝑡} \\ & =⟨\frac{d𝑢}{d𝑡},\,\frac{d𝑣}{d𝑡}⟩ \\ & =⟨\frac{d}{d𝑡}(𝑡^{4}−𝑡^{2}),\,\frac{d}{d𝑡}(2𝑡^{3})⟩ \\ & =⟨4𝑡^{3}−2𝑡,\,6𝑡^{2}⟩\end{aligned}


$$

To find the acceleration at time $t=1,$ we substitute $t=1$ into the above:

$$


\begin{aligned}𝐚(1) & =⟨4(1)^{3}−2(1),6(1)^{2}⟩ \\ & =⟨2,6⟩\end{aligned}


$$

Finally, to find the magnitude of the acceleration, we compute $|\mathbf a(1)|\mathbin{:}$

$$


\begin{aligned}|𝐚(1)| & =|⟨2,6⟩| \\ & =\sqrt{√2^{2}+6^{2}} \\ & =\sqrt{√40} \\ & =2\sqrt{√10}\,m/s^{2}.\end{aligned}


$$

### Example: Finding the Acceleration Vector of a Particle Given Its Position Vector

#### Question

The position vector $\mathbf{r}$ of a particle $P$ (relative to a fixed origin $O$) at time $t$ is given by

$$


\mathbf{r} = \langle 4t^2+1, 3t^2-t\rangle.


$$

Calculate the acceleration vector $\mathbf{a}$.

#### Explanation

To compute the acceleration vector, we need to differentiate the velocity vector. So first, we need to compute the velocity vector. We can do this by differentiating the position vector:

$$


\begin{aligned}𝐯 & =\frac{d𝐫}{d𝑡} \\ & =⟨\frac{d𝑥}{d𝑡},\,\frac{d𝑦}{d𝑡}⟩ \\ & =⟨\frac{d}{d𝑡}(4𝑡^{2}+1),\,\frac{d}{d𝑡}(3𝑡^{2}−𝑡)⟩ \\ & =⟨8𝑡,\,6𝑡−1⟩\end{aligned}


$$

Now, to compute the acceleration vector, we differentiate the velocity vector:

$$


\begin{aligned}𝐚 & =\frac{d𝐯}{d𝑡} \\ & =⟨\frac{d𝑢}{d𝑡},\,\frac{d𝑣}{d𝑡}⟩ \\ & =⟨\frac{d}{d𝑡}(8𝑡),\,\frac{d}{d𝑡}(6𝑡−1)⟩ \\ & =⟨8,6⟩\end{aligned}


$$

### Example: Computing the Acceleration of a Particle at a Given Moment Given Its Position Vector

#### Question

The position vector $\mathbf{r},$ in meters, of a particle $P$ relative to a fixed origin $O$ at time $t$ seconds is given by

$$


\mathbf{r} = \left\langle t^{5}-t^2,\, t^2+6t-3 \right\rangle.


$$

Calculate the acceleration vector and the magnitude of the acceleration of $P$ at time $t=0.$

#### Explanation

To compute the acceleration vector, we need to differentiate the velocity vector. So first, we need to compute the velocity vector, which we can do this by differentiating the position vector:

$$


\begin{aligned}𝐯 & =\frac{d𝐫}{d𝑡} \\ & =⟨\frac{d𝑥}{d𝑡},\,\frac{d𝑦}{d𝑡}⟩ \\ & =⟨\frac{d}{d𝑡}(𝑡^{5}−𝑡^{2}),\,\frac{d}{d𝑡}(𝑡^{2}+6𝑡−3)⟩ \\ & =⟨5𝑡^{4}−2𝑡,\,2𝑡+6⟩\end{aligned}


$$

Now, to compute the acceleration vector, we differentiate the velocity vector:

$$


\begin{aligned}𝐚 & =\frac{d𝐯}{d𝑡} \\ & =⟨\frac{d𝑢}{d𝑡},\,\frac{d𝑣}{d𝑡}⟩ \\ & =⟨\frac{d}{d𝑡}(5𝑡^{4}−2𝑡),\,\frac{d}{d𝑡}(2𝑡+6)⟩ \\ & =⟨20𝑡^{3}−2,\,2⟩\end{aligned}


$$

To find the acceleration at time $t=0,$ we substitute $t=0$ into the above:

$$


\begin{aligned}𝐚(0) & =⟨20(0)^{3}−2,\,2⟩ \\ & =⟨−2,\,2⟩\end{aligned}


$$

Finally, to find the magnitude of the acceleration, we compute $|\mathbf a(0)|\mathbin{:}$

$$


\begin{aligned}|𝐚(0)| & =|⟨−2,\,2⟩| \\ & =\sqrt{√(−2)^{2}+2^{2}} \\ & =\sqrt{√8} \\ & =2\sqrt{√2}\,m/s^{2}\end{aligned}


$$
