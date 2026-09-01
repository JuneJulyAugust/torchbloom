# Taylor Series

Source: https://www.mathacademy.com/topics/3826?courseId=21
Topic ID: 3826

## Prerequisites

- [Maclaurin Series](./340-maclaurin-series.md)

## Lesson

### Introduction

The Maclaurin series expands $f(x)$ in powers of $x$ only. The **Taylor series** of a function $f(x)$ generalizes this by expanding a function $f(x)$ in powers of $(x-a).$

For a function $f(x)$ that's infinitely differentiable at a point $x=a,$ the Taylor series of $f(x)$ centered about the point $x=a$ is

$$


\begin{aligned}𝑓(𝑥) & =𝑓(𝑎)+𝑓^{′}(𝑎)(𝑥−𝑎)+\frac{𝑓^{″}(𝑎)}{2!}(𝑥−𝑎)^{2}+\frac{𝑓^{‴}(𝑎)}{3!}(𝑥−𝑎)^{3}+⋯ \\ & =\underset{\underset{𝑘=0}{∑}}{\overset{}{∞}}\frac{𝑓^{(𝑘)}(𝑎)}{𝑘!}(𝑥−𝑎)^{𝑘}.\end{aligned}


$$

The series converges to $f(x)$ provided that $x$ lies within the interval of convergence of the series.

Like the Maclaurin series, the Taylor series is found by taking the limit as $n\to\infty$ of the $n$th degree Taylor polynomial of $f(x).$

**Note:** Setting $a=0$ in the Taylor series formula gives the Maclaurin series. In other words, the Maclaurin series is a special case of the Taylor series.

### Example: Finding the First Terms of the Taylor Series of a Function About a Point

#### Question

Find the first four non-zero terms in the Taylor expansion of $e^{-x}$ centered about the point $x=3.$

#### Explanation

We use Taylor's theorem in the form

$$


f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 +\frac{f'''(a)}{3!}(x-a)^3+\cdots,


$$

with $f(x)=e^{-x}$ and $a=3.$

Computing the required derivatives, we have

$$


\begin{aligned}𝑓(𝑥) & =𝑒^{−𝑥} \\ 𝑓(3) & =𝑒^{−3} \\ 𝑓^{′}(𝑥) & =−𝑒^{−𝑥} \\ 𝑓^{′}(3) & =−𝑒^{−3} \\ 𝑓^{″}(𝑥) & =𝑒^{−𝑥} \\ 𝑓^{″}(3) & =𝑒^{−3} \\ 𝑓^{‴}(𝑥) & =−𝑒^{−𝑥} \\ 𝑓^{‴}(3) & =−𝑒^{−3}\,.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑒^{−𝑥} & =𝑒^{−3}+(−𝑒^{−3})(𝑥−3)+\frac{(𝑒^{−3})}{2!}(𝑥−3)^{2}+\frac{(−𝑒^{−3})}{3!}(𝑥−3)^{3}+⋯ \\ & =𝑒^{−3}−𝑒^{−3}(𝑥−3)+\frac{𝑒^{−3}}{2}(𝑥−3)^{2}−\frac{𝑒^{−3}}{6}(𝑥−3)^{3}+⋯\,.\end{aligned}


$$

### Example: Approximating the Value of a Function at a Point Using Its Taylor Series

#### Question

Use the first three terms of the Taylor expansion for $f(x) = \sqrt x$ about $x=9$ to approximate the value of $\sqrt{9.1}.$

#### Explanation

We use Taylor's theorem in the form

$$


f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 +\cdots,


$$

with $a=9.$

Calculating the necessary derivatives, we get

$$


\begin{aligned}𝑓(𝑥) & =𝑥^{1/2} \\ 𝑓(9) & =3 \\ 𝑓^{′}(𝑥) & =\frac{1}{2}𝑥^{−1/2} \\ 𝑓^{′}(9) & =\frac{1}{6} \\ 𝑓^{″}(𝑥) & =−\frac{1}{4}𝑥^{−3/2} \\ 𝑓^{″}(9) & =−\frac{1}{108}.\end{aligned}


$$

So, the Taylor series is

$$


\begin{aligned}\sqrt{𝑥} & =3+\frac{1}{6}(𝑥−9)+\frac{1}{2}(−\frac{1}{108})(𝑥−9)^{2}+⋯ \\ & =3+\frac{1}{6}(𝑥−9)−\frac{1}{216}(𝑥−9)^{2}+⋯.\end{aligned}


$$

We substitute $x = 9.1$ into the above to approximate $\sqrt{9.1}.$ We get

$$


\begin{aligned}\sqrt{9.1} & ≈3+\frac{1}{6}(9.1−9)−\frac{1}{216}(9.1−9)^{2} \\ & ≈3+\frac{1}{6}(0.1)−\frac{1}{216}(0.1)^{2} \\ & =3.016\,620,\end{aligned}


$$

to six decimal places.

**** The exact value of $\sqrt{9.1}$ is $3.016\,621$ to six decimal places. So, our approximation is very good!
