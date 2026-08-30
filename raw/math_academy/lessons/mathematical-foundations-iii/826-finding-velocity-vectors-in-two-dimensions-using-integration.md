# Finding Velocity Vectors in Two Dimensions Using Integration

Source: https://www.mathacademy.com/topics/826?courseId=136
Topic ID: 826

## Prerequisites

- [Calculating Acceleration for Plane Motion Using Differentiation](./825-calculating-acceleration-for-plane-motion-using-differentiation.md)
- [Integrating Vector-Valued Functions](./1085-integrating-vector-valued-functions.md)
- [Determining Characteristics of Moving Objects Using Integration](./3582-determining-characteristics-of-moving-objects-using-integration.md)

## Lesson

### Introduction

For a particle moving in the $xy$-plane with velocity $\mathbf{v}(t),$ we calculate the acceleration vector $\mathbf{a}(t)$ by differentiating $\mathbf{v}(t)$ with respect to $t.$ But how do we find the velocity $\mathbf{v}(t)$ given the acceleration $\mathbf{a}(t)?$

To find $\mathbf{v}(t)$ we need to do the reverse of differentiation, so we integrate $\mathbf{a}(t)$ with respect to $t\mathbin{:}$

$$


\mathbf{a}(t) = \frac{\textrm{d}\mathbf{v}}{\textrm{d}t} \quad\Longrightarrow\quad \mathbf{v}(t) = \int \mathbf{a}(t)\,\textrm{d}t


$$

We're often told the value of the velocity at some time $t,$ and we can determine the arbitrary constant of integration using this information.

### Example: Finding the Velocity Vector Given the Acceleration Vector

#### Question

The acceleration $\mathbf{a}$ at time $t$ of a particle $P$ moving in the $xy$-plane is given by

$$


\mathbf{a}(t) = \langle 10, 0\rangle.


$$

Given that the particle has velocity $\mathbf{v} = \langle 10,20\rangle$ when $t=1,$ calculate the velocity vector of $P$ at time $t.$

#### Explanation

To compute the velocity vector, we need to integrate the acceleration vector:

$$


\begin{aligned}𝐯(𝑡) & =∫𝐚(𝑡)\,d𝑡 \\ & =∫⟨10,0⟩\,d𝑡 \\ & =⟨∫10\,d𝑡,∫0\,d𝑡⟩ \\ & =⟨10𝑡+𝐶_{1},\,𝐶_{2}⟩\end{aligned}


$$

Now, we can solve for the constants of integration using the fact that $\mathbf{v} (1)= \langle 10,20\rangle.$ Substituting $t=1,$ we get

$$


\begin{aligned}𝐯(1) & =⟨10(1)+𝐶_{1},\,𝐶_{2}⟩ \\ ⟨10,20⟩ & =⟨10+𝐶_{1},\,𝐶_{2}⟩.\end{aligned}


$$

So we must have

$$


\begin{aligned}10 & =10+𝐶_{1} \\ 𝐶_{1} & =0,\end{aligned}


$$

and

$$


C_2 = 20.


$$

Therefore, the velocity vector is

$$


\begin{aligned}𝐯(𝑡) & =⟨10𝑡,\,20⟩.\end{aligned}


$$

### Example: Calculating the Velocity Vector at a Point in Time Given the Acceleration Vector

#### Question

The acceleration $\mathbf{a}$ at time $t$ of a particle $P$ moving in the $xy$-plane is given by

$$


\mathbf{a}(t) = \langle 2e^{2t}, 3e^{3t}\rangle.


$$

Given that the particle has velocity $\mathbf{v} = \langle e^2, 2e^3 \rangle$ when $t=1,$ calculate the velocity vector of $P$ at time $t=2.$

#### Explanation

To compute the velocity vector, we need to integrate the acceleration vector:

$$


\begin{aligned}𝐯(𝑡) & =∫𝐚(𝑡)\,d𝑡 \\ & =∫⟨2𝑒^{2𝑡},3𝑒^{3𝑡}⟩\,d𝑡 \\ & =⟨∫2𝑒^{2𝑡}\,d𝑡,\,∫3𝑒^{3𝑡}\,d𝑡⟩ \\ & =⟨𝑒^{2𝑡}+𝐶_{1},\,𝑒^{3𝑡}+𝐶_{2}⟩\end{aligned}


$$

Now, we can solve for the constants of integration using the fact that $\mathbf{v}(1) = \langle e^2, 2e^3 \rangle.$ Substituting $t=1,$ we get

$$


\begin{aligned}𝐯(1) & =⟨𝑒^{2(1)}+𝐶_{1},\,𝑒^{3(1)}+𝐶_{2}⟩ \\ ⟨𝑒^{2},2𝑒^{3}⟩ & =⟨𝑒^{2}+𝐶_{1},\,𝑒^{3}+𝐶_{2}⟩,\end{aligned}


$$

so we must have $C_1=0$ and $C_2 = e^3.$ Therefore, the velocity is given by

$$


\begin{aligned}𝐯(𝑡) & =⟨𝑒^{2𝑡},\,𝑒^{3𝑡}+𝑒^{3}⟩.\end{aligned}


$$

Finally, the velocity at time $t=2$ is

$$


\begin{aligned}𝐯(2) & =⟨𝑒^{2(2)},\,𝑒^{3(2)}+𝑒^{3}⟩ \\ & =⟨𝑒^{4},\,𝑒^{6}+𝑒^{3}⟩.\end{aligned}


$$

### Example: Finding the Points at Which a Particle is Stationary Given the Acceleration Vector

#### Question

The acceleration $\mathbf{a}$ at time $t$ of a particle $P$ moving in the $xy$-plane is given by

$$


\mathbf{a}(t) = \langle 1, 2t \rangle, \quad -\infty < t < \infty.


$$

Given that the particle has velocity $\mathbf{v} = \langle 2,0 \rangle$ when $t=1,$ calculate the times at which the particle is stationary.

#### Explanation

The particle is stationary when its velocity is zero. So first, we need to compute the velocity of the particle.

To compute the velocity vector, we need to integrate the acceleration vector:

$$


\begin{aligned}𝐯(𝑡) & =∫𝐚(𝑡)\,d𝑡 \\ & =∫⟨1,2𝑡⟩\,d𝑡 \\ & =⟨∫1\,d𝑡,∫2𝑡\,d𝑡⟩ \\ & =⟨𝑡+𝐶_{1},\,𝑡^{2}+𝐶_{2}⟩\end{aligned}


$$

Now, we can solve for the constants of integration using the fact that $\mathbf{v} (1)= \langle 2,0\rangle.$ Substituting $t=1,$ we get

$$


\begin{aligned}𝐯(1) & =⟨1+𝐶_{1},\,1^{2}+𝐶_{2}⟩ \\ ⟨2,0⟩ & =⟨1+𝐶_{1},\,1+𝐶_{2}⟩,\end{aligned}


$$

so we must have $C_1=1$ and $C_2=-1.$ Therefore, the velocity is given by

$$


\begin{aligned}𝐯(𝑡) & =⟨𝑡+1,\,𝑡^{2}−1⟩.\end{aligned}


$$

To find the times at which the particle is stationary, we solve for the times at which the velocity is zero:

$$


\begin{aligned}𝐯(𝑡) & =𝟎 \\ ⟨𝑡+1,\,𝑡^{2}−1⟩ & =⟨0,0⟩.\end{aligned}


$$

So we need

$$


\begin{aligned}𝑡+1 & =0\,⇒\,𝑡=−1, \\ 𝑡^{2}−1=(𝑡+1)(𝑡−1) & =0\,⇒\,𝑡=±1.\end{aligned}


$$

The only solution that satisfies both equations is $t= -1,$ so this is the only value of $t$ when the particle is stationary.
