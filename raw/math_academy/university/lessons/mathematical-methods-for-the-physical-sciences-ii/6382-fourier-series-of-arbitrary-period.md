# Fourier Series of Arbitrary Period

Source: https://www.mathacademy.com/topics/6382?courseId=155
Topic ID: 6382

## Prerequisites

- [Properties of Fourier Series](./6709-properties-of-fourier-series.md)

## Lesson

### Introduction

When a function has period $2L$ (instead of $2\pi$), the "usual" Fourier formulas still work, but the sine and cosine inputs must be rescaled so that each term completes an integer number of oscillations over one period.

We do this by converting the $2L$-periodic function into a $2\pi$-periodic one using a change of variables.

Let $f(x)$ be the $2L$-periodic extension of a function $F(x)$ from $x\in[-L,L)$ to $x\in\mathbb{R}$. To use the standard $2\pi$-period Fourier formulas, define

$$


s=\frac{\pi}{L}x \qquad\text{and}\qquad g(s)=f\!\left(\frac{L}{\pi}s\right).


$$

Then $g$ is $2\pi$-periodic.

For a $2\pi$-periodic function $g$, the Fourier series is

$$


g(s)\sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}\bigl(a_n\cos(ns)+b_n\sin(ns)\bigr),


$$

where

$$


\begin{aligned}𝑎_{0} & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑔(𝑠)\,d𝑠, \\ 𝑎_{𝑛} & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑔(𝑠)cos⁡(𝑛𝑠)\,d𝑠,\,𝑛≥1, \\ 𝑏_{𝑛} & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑔(𝑠)sin⁡(𝑛𝑠)\,d𝑠,\,𝑛≥1.\end{aligned}


$$

Now substitute $g(s)=f\!\left(\dfrac{L}{\pi}s\right)$ and $s=\dfrac{\pi}{L}x$. First, for $a_n{:}$

$$


\begin{aligned}𝑎_{𝑛} & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑔(𝑠)cos⁡(𝑛𝑠)\,d𝑠 \\ & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑓\,(\frac{𝐿}{𝜋}𝑠)cos⁡(𝑛𝑠)\,d𝑠 \\ & =\frac{1}{𝜋}∫_{𝐿−𝐿}𝑓\,(\frac{𝐿}{𝜋}⋅\frac{𝜋}{𝐿}𝑥)cos\,(𝑛⋅\frac{𝜋}{𝐿}𝑥)\,d\,(\frac{𝜋}{𝐿}𝑥) \\ & =\frac{1}{𝜋}⋅\frac{𝜋}{𝐿}∫_{𝐿−𝐿}𝑓(𝑥)cos\,(\frac{𝑛𝜋}{𝐿}𝑥)\,d𝑥 \\ & =\frac{1}{𝐿}∫_{𝐿−𝐿}𝑓(𝑥)cos\,(\frac{𝑛𝜋}{𝐿}𝑥)\,d𝑥\end{aligned}


$$

Coefficients $b_n$ (for $n \geq 1$) and $a_0$ can be found similarly.

To summarize, the Fourier series of $f$ is

$$


f(x)\sim \frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\!\left(\frac{n\pi}{L}x\right)+b_n\sin\!\left(\frac{n\pi}{L}x\right)\right),


$$

where the coefficients are the following:

$$


\begin{aligned}𝑎_{0} & =\frac{1}{𝐿}∫_{𝐿−𝐿}𝑓(𝑥)\,d𝑥 \\ 𝑎_{𝑛} & =\frac{1}{𝐿}∫_{𝐿−𝐿}𝑓(𝑥)cos\,(\frac{𝑛𝜋}{𝐿}𝑥)\,d𝑥,\,𝑛≥1 \\ 𝑏_{𝑛} & =\frac{1}{𝐿}∫_{𝐿−𝐿}𝑓(𝑥)sin\,(\frac{𝑛𝜋}{𝐿}𝑥)\,d𝑥,\,𝑛≥1\end{aligned}


$$

Next, let's see some concrete examples.

### Example: Identifying Effects of the Horizontal Scaling on Coefficients

#### Question

Let $f(x)$ be the $2L$-periodic extension of a function $F(x)$ from $x\in [-L,L)$ to $x \in \mathbb R.$ Given that $L=2$ and $f(x) = \cosh{(x+1)}$, find the $4$th cosine and the $4$th sine coefficients.

#### Explanation

Recall that multiplying the argument of a function by $k \neq 0$ represents the horizontal stretching of the corresponding graph by a factor of $\dfrac{1}{k}.$

Now, let $s=\dfrac{\pi}{L}x.$ Then, since $f(x)$ has a period of $2L,$ the function

$$


g(s) = f\left(\dfrac{L}{\pi}s\right)


$$

must have a period of $2L \cdot \dfrac{\pi}{L} = 2\pi.$

The Fourier series of $g(s)$ is

$$


g(s) \sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos(ns)+b_n\sin(ns),


$$

where:

$$


\begin{aligned}𝑎_{0} & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑔(𝑠)\,d𝑠 \\ 𝑎_{𝑛} & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑔(𝑠)cos⁡(𝑛𝑠)\,d𝑠,\,𝑛≥1 \\ 𝑏_{𝑛} & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑔(𝑠)sin⁡(𝑛𝑠)\,d𝑠,\,𝑛≥1\end{aligned}


$$

Substituting $s=\dfrac{\pi}{L}x$ and using the fact that $g(s) = f\left(\dfrac{L}{\pi}s\right),$ we get the Fourier series of $f(x){:}$

$$


f(x) \sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty} a_n\cos\bigg(\boxed{\dfrac{n\pi}{L}x}\bigg)+ b_n\sin\bigg(\boxed{\dfrac{n\pi}{L}x}\bigg)


$$

Therefore, $4$th cosine coefficient of $f(x)$ is

$$


\begin{aligned}𝑎_{4} & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑔(𝑠)cos⁡(4𝑠)\,d𝑠 \\ & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑓(\frac{𝐿}{𝜋}𝑠)cos⁡(4𝑠)\,d𝑠 \\ & =\frac{1}{𝜋}∫_{𝐿−𝐿}𝑓(\frac{𝐿}{𝜋}⋅\frac{𝜋}{𝐿}𝑥)cos⁡(4⋅\frac{𝜋}{𝐿}𝑥)\,d(\frac{𝜋}{𝐿}𝑥) \\ & =\frac{1}{𝜋}⋅\frac{𝜋}{𝐿}∫_{𝐿−𝐿}𝑓(𝑥)cos⁡(\frac{4𝜋}{𝐿}𝑥)\,d𝑥 \\ & =\frac{1}{𝐿}∫_{𝐿−𝐿}𝑓(𝑥)cos⁡(\frac{4𝜋}{𝐿}𝑥)\,d𝑥.\end{aligned}


$$

Next, $4$th sine coefficient of $f(x)$ is

$$


\begin{aligned}𝑏_{4} & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑔(𝑠)sin⁡(4𝑠)\,d𝑠 \\ & =\frac{1}{𝜋}∫_{𝜋−𝜋}𝑓(\frac{𝐿}{𝜋}𝑠)sin⁡(4𝑠)\,d𝑠 \\ & =\frac{1}{𝜋}∫_{𝐿−𝐿}𝑓(\frac{𝐿}{𝜋}⋅\frac{𝜋}{𝐿}𝑥)sin⁡(4⋅\frac{𝜋}{𝐿}𝑥)\,d(\frac{𝜋}{𝐿}𝑥) \\ & =\frac{1}{𝜋}⋅\frac{𝜋}{𝐿}∫_{𝐿−𝐿}𝑓(𝑥)sin⁡(\frac{4𝜋}{𝐿}𝑥)\,d𝑥 \\ & =\frac{1}{𝐿}∫_{𝐿−𝐿}𝑓(𝑥)sin⁡(\frac{4𝜋}{𝐿}𝑥)\,d𝑥.\end{aligned}


$$

Finally, substituting $L=2$ and $f(x)=\cosh(x+1),$ we get

$$


\begin{aligned}𝑎_{4} & =\frac{1}{2}∫_{2−2}cosh⁡(𝑥+1)cos⁡(\frac{4𝜋}{2}𝑥)\,d𝑥 \\ & =\frac{1}{2}∫_{2−2}cosh⁡(𝑥+1)cos⁡(2𝜋𝑥)\,d𝑥, \\ 𝑏_{4} & =\frac{1}{2}∫_{2−2}cosh⁡(𝑥+1)sin⁡(\frac{4𝜋}{2}𝑥)\,d𝑥 \\ & =\frac{1}{2}∫_{2−2}cosh⁡(𝑥+1)sin⁡(2𝜋𝑥)\,d𝑥.\end{aligned}


$$

### Example: Computing the Constant Term For the Fourier Series

#### Question

$$


f(x) \sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos\left(\dfrac{n\pi}{2}x\right)+b_n\sin\left(\dfrac{n\pi}{2}x\right)


$$

Let $F(x)=3x^2-4x+1$ for $x\in[-2,2).$ The Fourier series of the $4$-periodic extension $f(x)$ of $F(x)$ is shown above. Find the exact value of $a_0.$

#### Explanation

For the Fourier series of a $2L$-periodic function, the constant term is given by

$$


a_0=\frac{1}{L}\int_{-L}^{L} f(x)\,\text{d}x.


$$

In our case, $L=2$ and $f(x)=3x^2-4x+1$ for $x \in [-2,2).$ So, substituting into the formula, we get

$$


\begin{aligned}𝑎_{0} & =\frac{1}{2}∫_{2−2}(3𝑥^{2}−4𝑥+1)\,d𝑥 \\ & =\frac{1}{2}[𝑥^{3}−2𝑥^{2}+𝑥]_{2−2} \\ & =\frac{1}{2}((2^{3}−2⋅2^{2}+2)−((−2)^{3}−2⋅(−2)^{2}+(−2))) \\ & =\frac{1}{2}(2−(−18)) \\ & =10.\end{aligned}


$$

### Example: Computing the Coefficients For the Fourier Series

#### Question

$$


f(x) \sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos\left(\dfrac{n\pi}{2}x\right)+b_n\sin\left(\dfrac{n\pi}{2}x\right)


$$

Let $F(x)=-5x+4$ for $x\in[-2,2).$ The Fourier series of the $4$-periodic extension $f(x)$ of $F(x)$ is shown above. Find the exact value of $a_3.$

#### Explanation

For the Fourier series of a $2L$-periodic function, the cosine coefficients are given by

$$


a_n=\frac{1}{L}\int_{-L}^{L} f(x)\cos\left(\dfrac{n\pi}{L}x\right)\,\text{d}x.


$$

In our case, $L=2$ and $f(x)=-5x+4$ for $x \in [-2,2).$ So, substituting into the formula, we get

$$


a_3 = \dfrac{1}{2}\int_{-2}^{2} (-5x+4)\cos\left(\dfrac{3\pi}{2}x\right)\,\text{d}x.


$$

We use the integration by parts:

$$


\begin{aligned}𝑢=−5𝑥+4\, & ⇒\,𝑢^{′}=−5 \\ 𝑣^{′}=cos⁡(\frac{3𝜋}{2}𝑥)\, & ⇒\,𝑣=\frac{2}{3𝜋}sin⁡(\frac{3𝜋}{2}𝑥)\end{aligned}


$$

Thus, we obtain

$$


\begin{aligned}𝑎_{3} & =\frac{1}{2}(𝑢𝑣\,_{2−2}−∫_{2−2}𝑣𝑢^{′}\,d𝑥) \\ & =\frac{1}{2}(\frac{2}{3𝜋}[(−5𝑥+4)sin⁡(\frac{3𝜋}{2}𝑥)]_{2−2}−∫_{2−2}\frac{2}{3𝜋}sin⁡(\frac{3𝜋}{2}𝑥)⋅(−5)\,d𝑥) \\ & =\frac{1}{2}(\frac{2}{3𝜋}[(−5(2)+4)sin⁡(3𝜋)−(−5(−2)+4)sin⁡(−3𝜋)]+\frac{10}{3𝜋}∫_{2−2}sin⁡(\frac{3𝜋}{2}𝑥)\,d𝑥) \\ & =\frac{1}{2}(\frac{2}{3𝜋}⋅0+\frac{10}{3𝜋}⋅(−\frac{2}{3𝜋})[cos⁡(\frac{3𝜋}{2}𝑥)]_{2−2}) \\ & =\frac{1}{2}(−\frac{20}{9𝜋^{2}}[cos⁡(3𝜋)−cos⁡(−3𝜋)]) \\ & =−\frac{10}{9𝜋^{2}}(−1−(−1)) \\ & =0.\end{aligned}


$$
