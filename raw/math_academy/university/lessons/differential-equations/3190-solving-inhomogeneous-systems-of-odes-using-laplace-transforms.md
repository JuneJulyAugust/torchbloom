# Solving Inhomogeneous Systems of ODEs Using Laplace Transforms

Source: https://www.mathacademy.com/topics/3190?courseId=61
Topic ID: 3190

## Prerequisites

- [Solving Inhomogeneous Systems of ODEs](./3189-solving-inhomogeneous-systems-of-odes.md)
- [Solving Homogeneous Systems of ODEs Using Laplace Transforms](./3232-solving-homogeneous-systems-of-odes-using-laplace-transforms.md)

## Lesson

### Introduction

In this topic, we'll learn how to use Laplace transforms to solve inhomogeneous systems like the one below.

$$


\begin{aligned}𝑥_{′1}(𝑡)=𝑥_{1}(𝑡)+5 \\ 𝑥_{′2}(𝑡)=−2𝑥_{1}(𝑡)+4𝑥_{2}(𝑡)−2,\end{aligned}


$$

Similar to the homogeneous case, the process can be split into three steps.

- **Step 1.** Apply the Laplace transform $\mathcal{L}$ to both sides of each equation, to get a system with variables

- **Step 2.** Solve the obtained system for variables

- **Step 3.** To find initial variables satisfying the original initial value problem, apply the inverse Laplace transform to

Let's see how this works in practice.

### A Worked Example

$$


\begin{aligned}𝑥_{′1}(𝑡)=𝑥_{1}(𝑡)+5 \\ 𝑥_{′2}(𝑡)=−2𝑥_{1}(𝑡)+4𝑥_{2}(𝑡)−2,\end{aligned}


$$

**Step 1**. In the initial value problem above, we apply the Laplace transform $\mathcal{L}$ to both sides of each equation.

First, we compute the Laplace transforms of both sides of each equation in our system:

$$


\begin{aligned}L{𝑥_{′1}(𝑡)}=L{𝑥_{1}(𝑡)+5} \\ L{𝑥_{′2}(𝑡)}=L{−2𝑥_{1}(𝑡)+4𝑥_{2}(𝑡)−2}\end{aligned}


$$

Using the derivative property of the Laplace transform, we obtain the system

$$


\begin{aligned}𝑠L{𝑥_{1}(𝑡)}−𝑥_{1}(0)=L{𝑥_{1}(𝑡)}+5L{1} \\ 𝑠L{𝑥_{2}(𝑡)}−𝑥_{2}(0)=−2L{𝑥_{1}(𝑡)}+4L{𝑥_{2}(𝑡)}−2L{1}\end{aligned}


$$

Using the result

$$


\mathcal L\{1\} = \dfrac{1}{s},


$$

we can write our system as follows:

$$


\begin{aligned}𝑠𝑋_{1}(𝑠)+2=𝑋_{1}(𝑠)+\frac{5}{𝑠} \\ 𝑠𝑋_{2}(𝑠)−3=−2𝑋_{1}(𝑠)+4𝑋_{2}(𝑠)−\frac{2}{𝑠}\end{aligned}


$$

where $X_1(s) = \mathcal{L}\left\{x_1(t) \right\}$ and $X_2(s) = \mathcal{L}\left\{x_2(t) \right\}$ are the Laplace transforms of the functions $x_1(t)$ and $x_2(t),$ respectively.

**Step 2**. Now, solving the first equation for $X_1(s),$ we get

$$


\begin{aligned}𝑠𝑋_{1}(𝑠)+2=𝑋_{1}(𝑠)+\frac{5}{𝑠}\,⟹\,𝑋_{1}(𝑠) & =\frac{−2𝑠+5}{𝑠(𝑠−1)}.\end{aligned}


$$

Substituting this in the second equation and solving for $X_2(s),$ we have

$$


s X_2(s) - 3 = - 2 \left(\dfrac{-2s+5}{s(s-1)}\right) + 4 X_2(s) - \dfrac{2}{s} \qquad\Longrightarrow\qquad X_2(s) = \dfrac{3s^2-s-8}{s(s-1)(s-4)}.


$$

**Step 3**. To find $x_1(t)$ and $x_2(t)$ satisfying the original initial value problem, we apply the inverse Laplace transform to $X_1(s)$ and $X_2(s){:}$

$$


\begin{aligned}𝑥_{1}(𝑡) & =L^{−1}{𝑋_{1}(𝑠)} \\ & =L^{−1}{\frac{−2𝑠+5}{𝑠(𝑠−1)}} \\ & =L^{−1}{\frac{3}{𝑠−1}−\frac{5}{𝑠}} \\ & =3L^{−1}{\frac{1}{𝑠−1}}−5L^{−1}{\frac{1}{𝑠}} \\ & =3𝑒^{𝑡}−5 \\ 𝑥_{2}(𝑡) & =L^{−1}{𝑋_{2}(𝑠)} \\ & =L^{−1}{\frac{3𝑠^{2}−𝑠−8}{𝑠(𝑠−1)(𝑠−4)}} \\ & =L^{−1}{\frac{2}{𝑠−1}+\frac{3}{𝑠−4}−\frac{2}{𝑠}} \\ & =2L^{−1}{\frac{1}{𝑠−1}}+3L^{−1}{\frac{1}{𝑠−4}}−2L^{−1}{\frac{1}{𝑠}} \\ & =2𝑒^{𝑡}+3𝑒^{4𝑡}−2\end{aligned}


$$

Finally, we write down the solution to the initial value problem:

$$


\begin{aligned}𝐱(𝑡) & =[\begin{matrix}𝑥_{1}(𝑡) \\ 𝑥_{2}(𝑡)\end{matrix}]=[\begin{matrix}3𝑒^{𝑡}−5 \\ 2𝑒^{𝑡}+3𝑒^{4𝑡}−2\end{matrix}]\end{aligned}


$$

### Example: Applying the Laplace Transform to a System of Linear ODEs

#### Question

$$


\begin{aligned}𝑥_{′1}(𝑡)=2𝑥_{1}(𝑡)+5cos⁡(2𝑡)−3 \\ 𝑥_{′2}(𝑡)=−3𝑥_{1}(𝑡)+4𝑥_{2}(𝑡)+2sin⁡(2𝑡),\end{aligned}


$$

Consider the initial value problem above. By applying the Laplace transform to both sides of each equation, find the system of equations.

#### Explanation

First, we compute the Laplace transforms of both sides of each equation in our system:

$$


\begin{aligned}L{𝑥_{′1}(𝑡)}=L{2𝑥_{1}(𝑡)+5cos⁡(2𝑡)−3} \\ L{𝑥_{′2}(𝑡)}=L{−3𝑥_{1}(𝑡)+4𝑥_{2}(𝑡)+2sin⁡(2𝑡)}\end{aligned}


$$

Using the derivative property of the Laplace transform, we obtain the system

$$


\begin{aligned}𝑠L{𝑥_{1}(𝑡)}−𝑥_{1}(0)=2L{𝑥_{1}(𝑡)}+5L{cos⁡(2𝑡)}−3L{1} \\ 𝑠L{𝑥_{2}(𝑡)}−𝑥_{2}(0)=−3L{𝑥_{1}(𝑡)}+4L{𝑥_{2}(𝑡)}+2L{sin⁡(2𝑡)}\end{aligned}


$$

Finally, using the results

$$


\mathcal L\{1\} = \dfrac{1}{s}, \quad \mathcal L\{\cos(2t)\} = \dfrac{s}{s^2+4}, \quad \mathcal L\{\sin(2t)\} = \dfrac{2}{s^2+4},


$$

we can write our system as follows:

$$


\begin{aligned}𝑠𝑋_{1}(𝑠)−1=2𝑋_{1}(𝑠)+\frac{5𝑠}{𝑠^{2}+4}−\frac{3}{𝑠} \\ 𝑠𝑋_{2}(𝑠)+2=−3𝑋_{1}(𝑠)+4𝑋_{2}(𝑠)+\frac{4}{𝑠^{2}+4}\end{aligned}


$$

where $X_1(s) = \mathcal{L}\left\{x_1(t) \right\}$ and $X_2(s) = \mathcal{L}\left\{x_2(t) \right\}$ are the Laplace transforms of the functions $x_1(t)$ and $x_2(t),$ respectively.

### Example: Finding the Solution of a Laplace Transformed Initial Value Problem

#### Question

$$


\begin{aligned}𝑥_{′1}(𝑡)=−𝑥_{1}(𝑡)+4 \\ 𝑥_{′2}(𝑡)=2𝑥_{1}(𝑡)−3𝑥_{2}(𝑡),\end{aligned}


$$

Consider the initial value problem above. By applying the Laplace transform $\mathcal{L}$ to both sides of each equation in our system, we get a system with variables $X_1(s) = \mathcal{L}\left\{x_1(t) \right\}$ and $X_2(s) = \mathcal{L}\left\{x_2(t) \right\}.$ In terms of the parameter $s,$ find the solution of the new system.

#### Explanation

First, we compute the Laplace transforms of both sides of each equation in our system:

$$


\begin{aligned}L{𝑥_{′1}(𝑡)}=L{−𝑥_{1}(𝑡)+4} \\ L{𝑥_{′2}(𝑡)}=L{2𝑥_{1}(𝑡)−3𝑥_{2}(𝑡)}\end{aligned}


$$

Using the derivative property of the Laplace transform, we obtain the system

$$


\begin{aligned}𝑠L{𝑥_{1}(𝑡)}−𝑥_{1}(0)=−L{𝑥_{1}(𝑡)}+4L{1} \\ 𝑠L{𝑥_{2}(𝑡)}−𝑥_{2}(0)=2L{𝑥_{1}(𝑡)}−3L{𝑥_{2}(𝑡)}\end{aligned}


$$

which can be simplified to the following:

$$


\begin{aligned}𝑠𝑋_{1}(𝑠)−1=−𝑋_{1}(𝑠)+\frac{4}{𝑠} \\ 𝑠𝑋_{2}(𝑠)−0=2𝑋_{1}(𝑠)−3𝑋_{2}(𝑠)\end{aligned}


$$

where $X_1(s) = \mathcal{L}\left\{x_1(t) \right\}$ and $X_2(s) = \mathcal{L}\left\{x_2(t) \right\},$ and we have used the fact that $\mathcal L\{1\} = \dfrac1s.$

Now, solving the first equation for $X_1(s),$ we get

$$


\begin{aligned}𝑠𝑋_{1}(𝑠)−1 & =−𝑋_{1}(𝑠)+\frac{4}{𝑠} \\ (𝑠+1)𝑋_{1}(𝑠) & =1+\frac{4}{𝑠} \\ (𝑠+1)𝑋_{1}(𝑠) & =\frac{𝑠+4}{𝑠} \\ 𝑋_{1}(𝑠) & =\frac{𝑠+4}{𝑠(𝑠+1)}.\end{aligned}


$$

Substituting this in the second equation and solving for $X_2(s),$ we have

$$


\begin{aligned}𝑠𝑋_{2}(𝑠) & =2𝑋_{1}(𝑠)−3𝑋_{2}(𝑠) \\ (𝑠+3)𝑋_{2}(𝑠) & =2𝑋_{1}(𝑠) \\ (𝑠+3)𝑋_{2}(𝑠) & =2(\frac{𝑠+4}{𝑠(𝑠+1)}) \\ 𝑋_{2}(𝑠) & =\frac{2(𝑠+4)}{𝑠(𝑠+1)(𝑠+3)}.\end{aligned}


$$

Therefore, the solution of the new system in terms of parameter $s$ is

$$


X_1(s) = \dfrac{s+4}{s(s+1)} ,\qquad X_2(s) = \dfrac{2(s+4)}{s(s+1)(s+3)}.


$$

### Example: Solving an Initial Value Problem Given the Laplace Transformed Solution

#### Question

$$


\begin{aligned}𝑥_{′1}(𝑡)=𝑥_{1}(𝑡)+3𝑥_{2}(𝑡)−7 \\ 𝑥_{′2}(𝑡)=−2𝑥_{2}(𝑡)+6,\end{aligned}


$$

Consider the initial value problem above. By applying the Laplace transform to both sides of each equation in our system, we get a transformed system with the solution

$$


X_1(s) = \mathcal{L}\left\{ x_1(t) \right\} = -\dfrac{1}{s+2} + \dfrac{2}{s-1} - \dfrac{2}{s}, \qquad X_2(s) = \mathcal{L}\left\{ x_2(t) \right\} = \dfrac{1}{s+2} + \dfrac{3}{s}.


$$

Find the solution to the original initial value problem.

#### Explanation

To find $x_1(t)$ and $x_2(t)$ satisfying the original initial value problem, we apply the inverse Laplace transform to $X_1(s)$ and $X_2(s){:}$

$$


\begin{aligned}𝑥_{1}(𝑡) & =L^{−1}{𝑋_{1}(𝑠)} \\ & =L^{−1}{−\frac{1}{𝑠+2}+\frac{2}{𝑠−1}−\frac{2}{𝑠}} \\ & =−L^{−1}{\frac{1}{𝑠+2}}+2\,L^{−1}{\frac{1}{𝑠−1}}−2\,L^{−1}{\frac{1}{𝑠}} \\ & =−𝑒^{−2⋅𝑡}+2𝑒^{1⋅𝑡}−2⋅1 \\ & =2𝑒^{𝑡}−𝑒^{−2𝑡}−2 \\ 𝑥_{2}(𝑡) & =L^{−1}{𝑋_{2}(𝑠)} \\ & =L^{−1}{\frac{1}{𝑠+2}+\frac{3}{𝑠}} \\ & =L^{−1}{\frac{1}{𝑠+2}}+3\,L^{−1}{\frac{1}{𝑠}} \\ & =𝑒^{−2⋅𝑡}+3⋅1 \\ & =𝑒^{−2𝑡}+3\end{aligned}


$$

Finally, we write down the solution to the initial value problem:

$$


\begin{aligned}𝐱(𝑡) & =[\begin{matrix}𝑥_{1}(𝑡) \\ 𝑥_{2}(𝑡)\end{matrix}]=[\begin{matrix}2𝑒^{𝑡}−𝑒^{−2𝑡}−2 \\ 𝑒^{−2𝑡}+3\end{matrix}]\end{aligned}


$$
