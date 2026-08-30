# Solving Homogeneous Systems of ODEs Using Laplace Transforms

Source: https://www.mathacademy.com/topics/3232?courseId=61
Topic ID: 3232

## Prerequisites

- [Solving Homogeneous Systems of ODEs With Distinct Eigenvalues and Initial Conditions](./2088-solving-homogeneous-systems-of-odes-with-distinct-eigenvalues-and-initial-conditions.md)
- [Solving First-Order ODEs With Time-Delayed Forcing Using Laplace Transforms](./6718-solving-first-order-odes-with-time-delayed-forcing-using-laplace-transforms.md)

## Lesson

### Introduction

In this topic, we'll learn how to use Laplace transforms to solve homogeneous systems like the one below.

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=5𝑥_{1}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=−2𝑥_{1}(𝑡)+6𝑥_{2}(𝑡),\end{aligned}


$$

The process can be split into three steps.

- **Step 1.** Apply the Laplace transform $\mathcal{L}$ to both sides of each equation, to get a system with variables

- **Step 2.** Solve the obtained system for variables

- **Step 3.** To find the initial variables satisfying the original initial value problem, apply the inverse Laplace transform to

Let's see how this works in practice.

### A Worked Example

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=5𝑥_{1}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=−2𝑥_{1}(𝑡)+6𝑥_{2}(𝑡),\end{aligned}


$$

**Step 1**. In the initial value problem above, we apply the Laplace transform $\mathcal{L}$ to both sides of each equation.

First, we find the Laplace transforms of both sides of each equation in our system:

$$


\begin{aligned}L{𝑥_{′1}^{}(𝑡)}=L{5𝑥_{1}(𝑡)} \\ L{𝑥_{′2}^{}(𝑡)}=L{−2𝑥_{1}(𝑡)+6𝑥_{2}(𝑡)}\end{aligned}


$$

Using the derivative property of the Laplace transform, we obtain the system

$$


\begin{aligned}𝑠L{𝑥_{1}(𝑡)}−𝑥_{1}(0)=5L{𝑥_{1}(𝑡)} \\ 𝑠L{𝑥_{2}(𝑡)}−𝑥_{2}(0)=−2L{𝑥_{1}(𝑡)}+6L{𝑥_{2}(𝑡)}\end{aligned}


$$

which can be simplified to the following:

$$


\begin{aligned}𝑠𝑋_{1}(𝑠)+3=5𝑋_{1}(𝑠) \\ 𝑠𝑋_{2}(𝑠)−2=−2𝑋_{1}(𝑠)+6𝑋_{2}(𝑠)\end{aligned}


$$

where $X_1(s) = \mathcal{L}\left\{x_1(t) \right\}$ and $X_2(s) = \mathcal{L}\left\{x_2(t) \right\}.$

**Step 2**. Now, solving the first equation for $X_1(s),$ we get

$$


s X_1(s) + 3 = 5 X_1(s) \qquad\Longrightarrow\qquad X_1(s) = -\dfrac{3}{s-5}.


$$

Substituting this in the second equation and solving for $X_2(s),$ we have

$$


s X_2(s) - 2 = -2\left(-\dfrac{3}{s-5}\right) + 6 X_2(s) \qquad\Longrightarrow\qquad X_2(s) = \dfrac{2s-4}{(s-5)(s-6)}.


$$

**Step 3**. To find $x_1(t)$ and $x_2(t)$ satisfying the original initial value problem, we apply the inverse Laplace transform to $X_1(s)$ and $X_2(s){:}$

$$


\begin{aligned}𝑥_{1}(𝑡) & =L^{−1}{𝑋_{1}(𝑠)} \\ & =L^{−1}{−\frac{3}{𝑠−5}} \\ & =−3L^{−1}{\frac{1}{𝑠−5}} \\ & =−3𝑒^{5𝑡} \\ 𝑥_{2}(𝑡) & =L^{−1}{𝑋_{2}(𝑠)} \\ & =L^{−1}{\frac{2𝑠−4}{(𝑠−5)(𝑠−6)}} \\ & =L^{−1}{\frac{8}{𝑠−6}−\frac{6}{𝑠−5}} \\ & =8L^{−1}{\frac{1}{𝑠−6}}−6L^{−1}{\frac{1}{𝑠−5}} \\ & =8𝑒^{6𝑡}−6𝑒^{5𝑡}\end{aligned}


$$

Finally, we write down the solution to the initial value problem:

$$


\begin{aligned}𝐱(𝑡) & =[\begin{aligned}𝑥_{1}(𝑡) \\ 𝑥_{2}(𝑡)\end{aligned}]=[\begin{aligned}−3𝑒^{5𝑡} \\ 8𝑒^{6𝑡}−6𝑒^{5𝑡}\end{aligned}]=[\begin{aligned}0 \\ 8\end{aligned}]𝑒^{6𝑡}+[\begin{aligned}−3 \\ −6\end{aligned}]𝑒^{5𝑡}\end{aligned}


$$

### Example: Applying the Laplace Transform to a System of Linear ODEs

#### Question

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=−3𝑥_{1}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=9𝑥_{1}(𝑡)+5𝑥_{2}(𝑡),\end{aligned}


$$

Consider the initial value problem above. By applying the Laplace transform to both sides of each equation, we get the system

$$


\begin{aligned}\phantom{XXX}=−3𝑋_{1}(𝑠) \\ \phantom{XXX}=\phantom{XXXXXXXX}\end{aligned}


$$

where $X_1(s) = \mathcal{L}\left\{x_1(t) \right\}$ and $X_2(s) = \mathcal{L}\left\{x_2(t) \right\}$ are the Laplace transforms of the functions $x_1(t)$ and $x_2(t),$ respectively.

#### Explanation

First, we find the Laplace transforms of both sides of each equation in our system:

$$


\begin{aligned}L{𝑥_{′1}^{}(𝑡)}=L{−3𝑥_{1}(𝑡)} \\ L{𝑥_{′2}^{}(𝑡)}=L{9𝑥_{1}(𝑡)+5𝑥_{2}(𝑡)}\end{aligned}


$$

Using the derivative property of the Laplace transform, we obtain the system

$$


\begin{aligned}𝑠L{𝑥_{1}(𝑡)}−𝑥_{1}(0)=−3L{𝑥_{1}(𝑡)} \\ 𝑠L{𝑥_{2}(𝑡)}−𝑥_{2}(0)=9L{𝑥_{1}(𝑡)}+5L{𝑥_{2}(𝑡)}\end{aligned}


$$

which can be simplified to the following:

$$


\begin{aligned}𝑠𝑋_{1}(𝑠)−3=−3𝑋_{1}(𝑠) \\ 𝑠𝑋_{2}(𝑠)−7=9𝑋_{1}(𝑠)+5𝑋_{2}(𝑠)\end{aligned}


$$

where $X_1(s) = \mathcal{L}\left\{x_1(t) \right\}$ and $X_2(s) = \mathcal{L}\left\{x_2(t) \right\}$ are the Laplace transforms of the functions $x_1(t)$ and $x_2(t),$ respectively.

### Example: Finding the Solution of a Laplace Transformed Initial Value Problem

#### Question

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=−3𝑥_{1}(𝑡)+𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=3𝑥_{1}(𝑡)−𝑥_{2}(𝑡),\end{aligned}


$$

Consider the initial value problem above. By applying the Laplace transform $\mathcal{L}$ to both sides of each equation in our system, we get a system with variables $X_1(s) = \mathcal{L}\!\left\{x_1(t) \right\}$ and $X_2(s) = \mathcal{L}\!\left\{x_2(t) \right\}.$ Find the solution of the new system in terms of the parameter $s.$

#### Explanation

First, we find the Laplace transforms of both sides of each equation in our system:

$$


\begin{aligned}L\,{𝑥_{′1}^{}(𝑡)}=L\,{−3𝑥_{1}(𝑡)+𝑥_{2}(𝑡)} \\ L\,{𝑥_{′2}^{}(𝑡)}=L\,{3𝑥_{1}(𝑡)−𝑥_{2}(𝑡)}\end{aligned}


$$

Using the derivative property of the Laplace transform, we obtain the system

$$


\begin{aligned}𝑠L\,{𝑥_{1}(𝑡)}−𝑥_{1}(0)=−3L\,{𝑥_{1}(𝑡)}+L\,{𝑥_{2}(𝑡)} \\ 𝑠L\,{𝑥_{2}(𝑡)}−𝑥_{2}(0)=3L\,{𝑥_{1}(𝑡)}−L\,{𝑥_{2}(𝑡)}\end{aligned}


$$

which simplifies to the following system:

$$


\begin{aligned}𝑠𝑋_{1}(𝑠)−4=−3𝑋_{1}(𝑠)+𝑋_{2}(𝑠) \\ 𝑠𝑋_{2}(𝑠)−4=3𝑋_{1}(𝑠)−𝑋_{2}(𝑠)\end{aligned}


$$

where $X_1(s) = \mathcal{L}\!\left\{x_1(t) \right\}$ and $X_2(s) = \mathcal{L}\!\left\{x_2(t) \right\}.$

Rewriting the system in standard form, we get

$$


\begin{aligned}(𝑠+3)𝑋_{1}(𝑠)−𝑋_{2}(𝑠)=4 \\ −3𝑋_{1}(𝑠)+(𝑠+1)𝑋_{2}(𝑠)=4\end{aligned}


$$

Now, from the first equation, we have

$$


X_2(s) = (s+3)X_1(s) - 4.


$$

Substituting this into the second equation, we get

$$


\begin{aligned}−3𝑋_{1}(𝑠)+(𝑠+1)\,[(𝑠+3)𝑋_{1}(𝑠)−4] & =4 \\ −3𝑋_{1}(𝑠)+(𝑠+1)(𝑠+3)𝑋_{1}(𝑠)−4(𝑠+1) & =4 \\ [(𝑠+1)(𝑠+3)−3]𝑋_{1}(𝑠) & =4+4(𝑠+1) \\ 𝑠(𝑠+4)𝑋_{1}(𝑠) & =4𝑠+8 \\ 𝑋_{1}(𝑠)=\frac{4(𝑠+2)}{𝑠(𝑠+4)}. & \end{aligned}


$$

Next, we find $X_2(s):$

$$


\begin{aligned}𝑋_{2}(𝑠) & =(𝑠+3)𝑋_{1}(𝑠)−4 \\ & =(𝑠+3)\,(\frac{4(𝑠+2)}{𝑠(𝑠+4)})−4 \\ & =\frac{4(𝑠+3)(𝑠+2)−4𝑠(𝑠+4)}{𝑠(𝑠+4)} \\ & =\frac{4(𝑠^{2}+5𝑠+6)−4(𝑠^{2}+4𝑠)}{𝑠(𝑠+4)} \\ & =\frac{4𝑠^{2}+20𝑠+24−4𝑠^{2}−16𝑠}{𝑠(𝑠+4)} \\ & =\frac{4(𝑠+6)}{𝑠(𝑠+4)}.\end{aligned}


$$

Therefore, we have

$$


X_1(s) =\dfrac{4(s+2)}{s(s+4)}, \qquad X_2(s) = \dfrac{4(s+6)}{s(s+4)}.


$$

### Example: Solving an Initial Value Problem Given the Laplace Transformed Solution

#### Question

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=5𝑥_{1}(𝑡)−𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=−5𝑥_{1}(𝑡)+𝑥_{2}(𝑡),\end{aligned}


$$

Consider the initial value problem above. By applying the Laplace transform to both sides of each equation in our system, we get a transformed system with the solution

$$


X_1(s) = \mathcal{L}\left\{ x_1(t) \right\} = \dfrac{4}{s} + \dfrac{1}{s-6}, \qquad X_2(s) = \mathcal{L}\left\{ x_2(t) \right\} = \dfrac{20}{s} - \dfrac{1}{s-6}.


$$

Find the solution to the original initial value problem.

#### Explanation

To find $x_1(t)$ and $x_2(t)$ satisfying the original initial value problem, we apply the inverse Laplace transform to $X_1(s)$ and $X_2(s){:}$

$$


\begin{aligned}𝑥_{1}(𝑡) & =L^{−1}{𝑋_{1}(𝑠)} \\ & =L^{−1}{\frac{4}{𝑠}+\frac{1}{𝑠−6}} \\ & =4L^{−1}{\frac{1}{𝑠}}+L^{−1}{\frac{1}{𝑠−6}} \\ & =4⋅1+𝑒^{6⋅𝑡} \\ & =4+𝑒^{6𝑡} \\ 𝑥_{2}(𝑡) & =L^{−1}{𝑋_{2}(𝑠)} \\ & =L^{−1}{\frac{20}{𝑠}−\frac{1}{𝑠−6}} \\ & =20L^{−1}{\frac{1}{𝑠}}−L^{−1}{\frac{1}{𝑠−6}} \\ & =20⋅1−𝑒^{6⋅𝑡} \\ & =20−𝑒^{6𝑡}\end{aligned}


$$

Finally, we write down the solution to the initial value problem:

$$


\begin{aligned}𝐱(𝑡) & =[\begin{aligned}𝑥_{1}(𝑡) \\ 𝑥_{2}(𝑡)\end{aligned}]=[\begin{aligned}4+𝑒^{6𝑡} \\ 20−𝑒^{6𝑡}\end{aligned}]=[\begin{aligned}4 \\ 20\end{aligned}]+[\begin{aligned}1 \\ −1\end{aligned}]𝑒^{6𝑡}\end{aligned}


$$
