# Solving IVPs Using Fourier Series

Source: https://www.mathacademy.com/topics/6721?courseId=61
Topic ID: 6721

## Prerequisites

- [Solving ODEs Using Fourier Series](./6386-solving-odes-using-fourier-series.md)

## Lesson

### Introduction

We know how to find a Fourier-series particular solution $y_p$ for a periodically forced linear ODE. In this topic, the new step is how to use $y_p$ to satisfy an initial condition.

Recall that once a particular solution $y_p$ is chosen, the full solution has the form

$$


y = y_c + y_p,


$$

where $y_c$ solves the corresponding homogeneous equation.

Now, suppose the IVP is given at $x=x_0{:}$

$$


y(x_0)=y_0.


$$

Then,

$$


y_0 = y_c(x_0)+y_p(x_0).


$$

A useful simplification is to choose the particular solution so that

$$


y_p(x_0)=0.


$$

In that case, the initial condition becomes

$$


y_0 = y_c(x_0),


$$

so we can solve for the constant(s) in $y_c$ immediately (without evaluating any Fourier sums at $x_0$).

On the next slide, we’ll apply this idea in an example.

### A Worked Example

For example, consider the initial value problem

$$


y'-2y = f(x), \qquad y(0)=3,


$$

where $f(x)$ is a $2$-periodic function. Suppose we choose the forcing (and hence the Fourier-series particular solution) so that

$$


y_p(0)=0.


$$

First, solve the homogeneous equation:

$$


y' - 2y = 0 \quad\Longrightarrow\quad y_c = Ae^{2x}.


$$

A $2$-periodic forcing function can be written using harmonics of frequency $\pi$, so we may write the particular solution in the form

$$


y_p(x)=\sum_{n=1}^\infty \left(a_n\cos(n\pi x)+b_n\sin(n\pi x)\right).


$$

Thus the full solution is

$$


y(x)=Ae^{2x}+\sum_{n=1}^\infty \left(a_n\cos(n\pi x)+b_n\sin(n\pi x)\right).


$$

Now apply $y(0)=3$ and use $y_p(0)=0$:

$$


\begin{aligned}𝑦(0) & =𝐴𝑒^{2(0)}+𝑦_{𝑝}(0) \\ 3 & =𝐴(1)+0 \\ 𝐴 & =3.\end{aligned}


$$

Therefore,

$$


y(x)= 3e^{2x}+\sum_{n=1}^\infty \left(a_n\cos(n\pi x)+b_n\sin(n\pi x)\right).


$$

### Example: Solving First-Order IVPs Using Fourier Series

#### Question

Consider the initial value problem

$$


y'-6y = f(x), \qquad y(1)=4


$$

where $f(x)$ is a $2$-periodic function. Fill in the missing part in the solution of the IVP, where the infinite sum on the right-hand side below represents a particular solution $y_p$ of the differential equation.

**

$$


𝐴𝐴𝐴?𝐴𝐴𝐴


$$

#### Explanation

Recall that the general solution of a linear differential equation of the form $y' + P(x)y = f(x)$ is given by

$$


y = y_c + y_p,


$$

where $y_c$ is the general solution of the corresponding homogeneous equation, and $y_p$ is a particular solution.

First, we find the homogeneous solution. The general solution of $y' - 6y = 0$ is

$$


y_c = Ae^{6x},


$$

where $A$ is an arbitrary constant.

Next, we identify the form of the general solution. Because the operator $y' - 6y$ involves a first derivative, a periodic forcing function $f(x)$ results in a particular solution containing both sine and cosine terms:

$$


y(x) \sim Ae^{6x} + \sum_{n=1}^\infty (a_n \cos(n\pi x) + b_n \sin(n\pi x))


$$

Now, we apply the initial condition $y(1)=4.$ Using the hint that the particular solution part evaluates to zero at $x=1,$ we have

$$


\begin{aligned}𝑦(1) & =𝐴𝑒^{6(1)}+𝑦_{𝑝}(1) \\ 4 & =𝐴𝑒^{6}+0 \\ 𝐴 & =4𝑒^{−6}.\end{aligned}


$$

Finally, we substitute $A$ back into the homogeneous part:

$$


y_c = (4e^{-6})e^{6x} = 4e^{6x-6}


$$

Therefore, the solution is

$$


y(x) \sim \boxed{4e^{6x-6}} + \sum_{n=1}^\infty (a_n \cos(n\pi x) + b_n \sin(n\pi x)).


$$

### Second-Order IVPs

When we solve a second-order IVP using Fourier series, we still represent the solution in the form

$$


y = y_c + y_p,


$$

but since the homogeneous solution has *two* constants, we use *two* conditions:

$$


y(0)=y_0 \qquad\text{and}\qquad y'(0)=y_1


$$

Before we start, we can use the forcing series properties to simplify our work. For a second-order equation of the form

$$


y'' + \omega^2 y = f(x)


$$

with no $y'$ (damping) term, the particular solution can be simplified. Here, we have two cases:

- **Case 1:** $f(x)$ is odd. If $f(x)$ is *odd* and the equation has the form $y''+\omega^2 y=f(x)$, then the particular solution is also *odd*, so it is a sine series: This immediately gives $y_p(0)=0,$ so the condition $y(0)=y_0$ determines the cosine constant in $y_c$ without evaluating any infinite sum at $0$.

- **Case 2:** $f(x)$ is even. If $f(x)$ is *even* and the equation has the form $y''+\omega^2 y=f(x)$, then the particular solution is also *even*, so it is a cosine series: Here, the derivative is a sine series: This immediately gives $y_p'(0)=0,$ so the condition $y'(0)=y_1$ determines the sine constant in $y_c$ without evaluating any infinite sum at $0$.

In both cases, the key idea is that evaluating at $x=0$ (and differentiating once) lets the initial conditions pick off the constants in $y_c$ as cleanly as possible.

Let's see how this works in practice on the next slide.

### A Worked Example of a Second-Order IVP

Consider the initial value problem

$$


y''+ 7y = f(x), \qquad y(0)=3,\quad y'(0)=0


$$

where $f(x)$ is an even, $2\pi$-periodic function. Since the forcing is even and the differential operator contains no $y'$ term, we represent the particular solution as a cosine series:

$$


y_p(x)=\sum_{n=0}^\infty a_n\cos(nx)


$$

Next, we solve the homogeneous equation $y''+7y=0.$ The characteristic equation is $\lambda^2+7=0,$ so

$$


y_c=A\cos(\sqrt{7}x)+B\sin(\sqrt{7}x).


$$

To find the unknown constants, we apply the initial conditions. Differentiating the total solution gives

$$


y'(x)=-A\sqrt{7}\sin(\sqrt{7}x)+B\sqrt{7}\cos(\sqrt{7}x)-\sum_{n=1}^\infty n a_n\sin(nx).


$$

Using the derivative condition $y'(0)=0{:}$

$$


\begin{aligned}𝑦^{′}(0) & =−𝐴\sqrt{√7}sin⁡(0)+𝐵\sqrt{√7}cos⁡(0)−\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑛𝑎_{𝑛}sin⁡(0) \\ 0 & =0+𝐵\sqrt{√7}−0 \\ 𝐵 & =0\end{aligned}


$$

Note that because the total solution is an even function, its derivative is an odd function, which must vanish at $x=0.$

Next, we apply $y(0)=3.$ With $B=0,$ the total solution is

$$


y(x)\sim A\cos(\sqrt{7}x)+\sum_{n=0}^\infty a_n\cos(nx).


$$

Applying $y(0)=3$ and noting that $\cos(0)=1,$ we have

$$


\begin{aligned}3 & =𝐴+\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛} \\ 𝐴 & =3−\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑎_{𝑛}.\end{aligned}


$$

Therefore, the solution can be written as

$$


y(x)\sim \cos(\sqrt{7}x)\left(3-\sum_{n=0}^\infty a_n\right) +\sum_{n=0}^\infty a_n\cos(nx).


$$

### Example: Solving Second-Order IVPs Using Fourier Series

#### Question

$$


y''+ 7\pi^2 y = f(x), \qquad y(0)=0, \quad y'(0)=0


$$

Consider the initial value problem above, where $f(x)$ is an odd, $4$-periodic function. Fill in the missing part in the solution of the IVP, where the second infinite sum on the right-hand side below represents a particular solution of the differential equation.

$$


𝐴𝐴𝐴?𝐴𝐴𝐴


$$

#### Explanation

Recall that the general solution of a linear differential equation of the form $y'' + \omega^2 y = f(x)$ is given by $y = y_c + y_p,$ where $y_c$ is the solution to the homogeneous equation and $y_p$ is a particular solution.

First, we address the particular solution $y_p.$ Since $f(x)$ is an odd function, its Fourier series consists only of sine terms. For a second-order equation with no $y'$ (damping) term, the particular solution inherits this property and is also an odd function. This is represented by the term

$$


y_p(x) = \sum_{n=1}^\infty \dfrac{16(-1)^n}{n^2\pi^3\left(28-n^2\right)} \sin\left(\dfrac{n\pi x}{2}\right).


$$

Next, we find the homogeneous solution. The characteristic equation $\lambda^2 + 7\pi^2 = 0$ gives roots $\lambda = \pm \sqrt{7}\pi \textrm i.$ So, we have

$$


y_c = A\cos(\sqrt{7}\pi x) + B\sin(\sqrt{7}\pi x).


$$

To find the unknown constants, we apply the initial conditions. Using $y(0)=0{:}$

$$


\begin{aligned}𝑦(0) & =𝐴cos⁡(0)+𝐵sin⁡(0)+𝑦_{𝑝}(0) \\ 0 & =𝐴(1)+0+0 \\ 𝐴 & =0\end{aligned}


$$

Note that $y_p(0)=0$ because the particular solution is a sine series.

Next, we use the derivative condition $y'(0)=0.$ First, we compute the derivative of the total solution (with $A=0$):

$$


y'(x) \sim B(\sqrt{7}\pi)\cos(\sqrt{7}\pi x) + \sum_{n=1}^\infty \dfrac{8(-1)^n}{n\pi^2\left(28-n^2\right)} \cos\left(\dfrac{n\pi x}{2}\right)


$$

Applying $y'(0)=0$ and noting that $\cos(0)=1,$ we have

$$


\begin{aligned}0 & =𝐵(\sqrt{√7}𝜋)+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{8(−1)^{𝑛}}{𝑛𝜋^{2}(28−𝑛^{2})} \\ 𝐵(\sqrt{√7}𝜋) & =−\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{8(−1)^{𝑛}}{𝑛𝜋^{2}(28−𝑛^{2})} \\ 𝐵 & =−\frac{1}{\sqrt{√7}𝜋}\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{8(−1)^{𝑛}}{𝑛𝜋^{2}(28−𝑛^{2})} \\ & =−\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{8(−1)^{𝑛}}{\sqrt{√7}𝑛𝜋^{3}(28−𝑛^{2})}.\end{aligned}


$$

Substituting $B$ back into $y_c = B\sin(\sqrt{7}\pi x),$ we find the missing part:

$$


y(x)\sim \boxed{-\sin(\sqrt{7}\pi x)\sum_{n=1}^\infty \dfrac{8(-1)^n}{\sqrt{7}n\pi^3\left(28-n^2\right)}} + \sum_{n=1}^\infty \dfrac{16(-1)^n}{n^2\pi^3\left(28-n^2\right)} \sin\left(\dfrac{n\pi x}{2}\right)


$$
