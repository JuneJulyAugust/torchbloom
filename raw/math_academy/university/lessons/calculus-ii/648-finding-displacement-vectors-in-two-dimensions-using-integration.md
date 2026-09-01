# Finding Displacement Vectors in Two Dimensions Using Integration

Source: https://www.mathacademy.com/topics/648?courseId=106
Topic ID: 648

## Prerequisites

- [Finding Velocity Vectors in Two Dimensions Using Integration](./826-finding-velocity-vectors-in-two-dimensions-using-integration.md)
- [Calculating the Displacement of a Particle Using Integration](./3576-calculating-the-displacement-of-a-particle-using-integration.md)

## Lesson

### Introduction

For a particle moving in the $xy$-plane with position vector $\mathbf{r}(t),$ we calculate the velocity vector $\mathbf{v}(t)$ by differentiating $\mathbf{r}$ with respect to $t.$ So, how do we find the position vector $\mathbf{r}(t)$ of a particle given its velocity $\mathbf{v}(t)?$

We need to do the reverse of differentiation, so we integrate $\mathbf{v}(t)$ with respect to $t\mathbin{:}$

$$


\mathbf{v}(t) = \frac{\text{d}\mathbf{r}}{\text{d}t} \quad\Longrightarrow\quad \mathbf{r}(t) = \int \mathbf{v}(t)\,\text{d}t.


$$

We're often given the position at some time $t,$ and we can determine the arbitrary constant of integration using that information.

### Example: Finding a Position Vector Given a Velocity Vector

#### Question

The velocity $\mathbf{v}$ at time $t$ of a particle $P$ moving in the $xy$-plane is given by

$$


\mathbf{v}(t) = \langle 2t, 3t^2\rangle.


$$

Given that the particle is at the position $(1,2)$ when $t=0,$ calculate the position vector of $P$ at time $t.$

#### Explanation

To compute the position vector, we need to integrate the velocity vector:

$$


\begin{aligned}𝐫(𝑡) & =∫𝐯(𝑡)\,d𝑡 \\ & =∫⟨2𝑡,3𝑡^{2}⟩\,d𝑡 \\ & =⟨∫2𝑡\,d𝑡,\,∫3𝑡^{2}\,d𝑡⟩ \\ & =⟨𝑡^{2}+𝐶_{1},\,𝑡^{3}+𝐶_{2}⟩.\end{aligned}


$$

Now, we can solve for the constants of integration using the fact that $\mathbf{r} (0)= \langle 1,2 \rangle.$ Substituting $t=0,$ we get

$$


\begin{aligned}𝐫(0) & =⟨(0)^{2}+𝐶_{1},\,(0)^{3}+𝐶_{2}⟩ \\ ⟨1,2⟩ & =⟨𝐶_{1},𝐶_{2}⟩,\end{aligned}


$$

so we must have $C_1=1$ and $C_2=2.$ Therefore, the position vector is

$$


\begin{aligned}𝐫(𝑡) & =⟨𝑡^{2}+1,\,𝑡^{3}+2⟩.\end{aligned}


$$

### Example: Calculating a Position Vector Given a Velocity Vector and Time

#### Question

The velocity $\mathbf{v}$ at time $t$ of a particle $P$ moving in the $xy$-plane is given by

$$


\mathbf{v}(t) = \langle \cos t, \sin t\rangle.


$$

Given that the particle is at the position $\mathbf{r}=\left\langle 0,\, 0\right\rangle$ when $t=\dfrac{\pi}2,$ calculate the position of $P$ at time $t=\pi.$

#### Explanation

To compute the position vector, we need to integrate the velocity vector:

$$


\begin{aligned}𝐫(𝑡) & =∫𝐯(𝑡)\,d𝑡 \\ & =∫⟨cos⁡𝑡,sin⁡𝑡⟩\,d𝑡 \\ & =⟨∫cos⁡𝑡\,d𝑡,\,∫sin⁡𝑡\,d𝑡⟩ \\ & =⟨sin⁡𝑡+𝐶_{1},\,−cos⁡𝑡+𝐶_{2}⟩.\end{aligned}


$$

Now, we can solve for the constants of integration using the fact that $\mathbf{r}\left(\dfrac{\pi}{2} \right) = \langle 0,0 \rangle.$ Substituting $t=\dfrac{\pi}{2},$ we get

$$


\begin{aligned}𝐫(\frac{𝜋}{2}) & =⟨sin⁡(\frac{𝜋}{2})+𝐶_{1},\,−cos⁡(\frac{𝜋}{2})+𝐶_{2}⟩ \\ ⟨0,0⟩ & =⟨1+𝐶_{1},\,0+𝐶_{2}⟩,\end{aligned}


$$

so we must have $C_1=-1$ and $C_2 = 0.$ Therefore, the position is given by

$$


\begin{aligned}𝐫(𝑡) & =⟨sin⁡𝑡−1,\,−cos⁡𝑡⟩,\end{aligned}


$$

and the position at time $t=\pi$ is given by

$$


\begin{aligned}𝐫(𝜋) & =⟨sin⁡𝜋−1,\,−cos⁡𝜋⟩ \\ & =⟨0−1,\,−(−1)⟩ \\ & =⟨−1,\,1⟩.\end{aligned}


$$

### Example: Finding the Times When a Particle Is at a Certain Location Given Its Velocity Vector

#### Question

The velocity $\mathbf{v}$ at time $t$ of a particle $P$ moving in the $xy$-plane is given by

$$


\mathbf{v}(t) = \langle 2t, 1 \rangle\,,\quad t\in(-\infty,\infty).


$$

Given that the particle is at the position $\mathbf{r} = \left\langle -1,\, 1 \right\rangle$ when $t=0,$ calculate the times at which the particle is at the origin.

#### Explanation

The particle is at the origin when its position is $\mathbf{r} = \left< 0,0 \right>.$ So first, we need to compute the position function of the particle.

To compute the position vector, we need to integrate the velocity vector:

$$


\begin{aligned}𝐫(𝑡) & =∫𝐯(𝑡)\,d𝑡 \\ & =∫⟨2𝑡,1⟩\,d𝑡 \\ & =⟨∫2𝑡\,d𝑡,\,∫1\,d𝑡⟩ \\ & =⟨𝑡^{2}+𝐶_{1},\,𝑡+𝐶_{2}⟩.\end{aligned}


$$

Now, we can solve for the constants of integration using the fact that $\mathbf{r} (0)= \langle -1, \, 1 \rangle.$ Substituting $t=0,$ we get

$$


\begin{aligned}𝐫(0) & =⟨(0)^{2}+𝐶_{1},\,(0)+𝐶_{2}⟩ \\ ⟨−1,\,1⟩ & =⟨𝐶_{1},\,𝐶_{2}⟩,\end{aligned}


$$

so we must have $C_1=-1$ and $C_2=1.$ Therefore, the position is given by

$$


\begin{aligned}𝐫(𝑡) & =⟨𝑡^{2}−1,\,𝑡+1⟩.\end{aligned}


$$

To find the times at which the particle is at the origin, we solve for the times at which the position is zero:

$$


\begin{aligned}𝐫(𝑡) & =𝟎 \\ ⟨𝑡^{2}−1,\,𝑡+1⟩ & =⟨0,0⟩.\end{aligned}


$$

So we need

$$


\begin{aligned}𝑡^{2}−1 & =0\,⇒\,𝑡=±1, \\ 𝑡+1 & =0\,⇒\,𝑡=−1.\end{aligned}


$$

The only solution that satisfies both equations is $t= -1,$ so this is the only value of $t$ when the particle is at the origin.

### Example: Finding a Position Vector Given an Acceleration Vector

#### Question

The acceleration $\mathbf{a}$ at time $t$ of a particle $P$ moving in the $xy$-plane is given by

$$


\mathbf{a}(t) = \left< 9\cos {3t},\, \sin{t} \right>.


$$

Given that the particle is at the position $(0,0)$ and has velocity $\left\langle 2,\,0 \right\rangle$ when $t=0,$ calculate the position vector of $P$ at time $t.$

#### Explanation

To compute the position vector, we need to integrate the velocity vector. To find the velocity vector, we first need to integrate the acceleration vector.

$$


\begin{aligned}𝐯(𝑡) & =∫𝐚(𝑡)\,d𝑡 \\ & =∫⟨9cos⁡3𝑡,\,sin⁡𝑡⟩\,d𝑡 \\ & =⟨∫9cos⁡3𝑡\,d𝑡,\,∫sin⁡𝑡\,d𝑡⟩ \\ & =⟨3sin⁡3𝑡+𝐶_{1},\,−cos⁡𝑡+𝐶_{2}⟩\end{aligned}


$$

We can solve for the constants of integration using the fact that $\mathbf{v} (0)= \langle 2,\, 0 \rangle.$ Substituting $t=0,$ we get

$$


\begin{aligned}𝐯(0) & =⟨3sin⁡0+𝐶_{1},\,−cos⁡0+𝐶_{2}⟩ \\ ⟨2,\,0⟩ & =⟨𝐶_{1},−1+𝐶_{2}⟩,\end{aligned}


$$

so we must have $C_1=2$ and $C_2=1.$ Therefore, the velocity vector is

$$


\mathbf{v}(t) = \left< 3\sin{3t} +2 , \, 1-\cos{t} \right>.


$$

We can compute the position vector by integrating the velocity vector.

$$


\begin{aligned}𝐫(𝑡) & =∫𝐯(𝑡)\,d𝑡 \\ & =∫⟨3sin⁡3𝑡+2,\,1−cos⁡𝑡⟩\,d𝑡 \\ & =⟨∫3sin⁡3𝑡+2\,d𝑡,\,∫1−cos⁡𝑡\,d𝑡⟩ \\ & =⟨−cos⁡3𝑡+2𝑡+𝐶_{3},\,𝑡−sin⁡𝑡+𝐶_{4}⟩\end{aligned}


$$

Now, we can solve for the constants of integration using the fact that $\mathbf{r} (0)= \langle 0,0 \rangle.$ Substituting $t=0,$ we get

$$


\begin{aligned}𝐫(0) & =⟨−cos⁡0+2(0)+𝐶_{3},\,0−sin⁡0+𝐶_{4}⟩ \\ ⟨0,0⟩ & =⟨−1+𝐶_{3},\,𝐶_{4}⟩,\end{aligned}


$$

so we must have $C_3=1$ and $C_4=0.$ Therefore, the position of $P$ at time $t$ is

$$


\mathbf{r}(t) = \left< -\cos {3t} + 2t + 1 , \, t-\sin{t} \right>.


$$
