# Properties of Fourier Series

Source: https://www.mathacademy.com/topics/6709?courseId=61
Topic ID: 6709

## Prerequisites

- [Products of Even and Odd Functions](../algebra-ii/1827-products-of-even-and-odd-functions.md)
- [Introduction to Fourier Series](./3195-introduction-to-fourier-series.md)

## Lesson

### Introduction

In applications, we often build new periodic signals by adding old ones together or scaling their amplitudes. The Fourier series behaves well under these transformations, i.e., scaling and adding functions simply scales and adds their Fourier coefficients.

More precisely, let $f(x)$ and $g(x)$ be $2\pi$-periodic functions with Fourier series

$$


\begin{aligned}𝑓(𝑥) & ∼\frac{𝑎_{0}}{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(𝑎_{𝑛}cos⁡(𝑛𝑥)+𝑏_{𝑛}sin⁡(𝑛𝑥)), \\ 𝑔(𝑥) & ∼\frac{𝑐_{0}}{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(𝑐_{𝑛}cos⁡(𝑛𝑥)+𝑑_{𝑛}sin⁡(𝑛𝑥)).\end{aligned}


$$

For constants $\alpha$ and $\beta,$ define

$$


h(x)=\alpha f(x)+\beta g(x).


$$

Then $h$ is also $2\pi$-periodic, and its Fourier series has the form

$$


h(x)\sim \dfrac{A_0}{2}+\sum_{n=1}^{\infty}\big(A_n\cos(nx)+B_n\sin(nx)\big),


$$

where the coefficients are obtained by combining the coefficients term-by-term:

- $A_0=\alpha a_0+\beta c_0$

- $A_n=\alpha a_n+\beta c_n$ for $n\ge 1$

- $B_n=\alpha b_n+\beta d_n$ for $n\ge 1$

Equivalently,

$$


\alpha f(x)+\beta g(x) \sim \dfrac{\alpha a_0+\beta c_0}{2} +\sum_{n=1}^{\infty}\Big((\alpha a_n+\beta c_n)\cos(nx)+(\alpha b_n+\beta d_n)\sin(nx)\Big).


$$

**Watch out!** In this notation,

- the *constant Fourier coefficient* is $A_0,$ while

- the *term* in the series is $\dfrac{A_0}{2}.$

Let's see a concrete example below.

### Example: Using Linearity of Fourier Series

#### Question

$$


\begin{aligned}𝑓(𝑥) & ∼\frac{𝑎_{0}}{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}cos⁡(𝑛𝑥)+𝑏_{𝑛}sin⁡(𝑛𝑥) \\ 𝑔(𝑥) & ∼\frac{𝑐_{0}}{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑐_{𝑛}cos⁡(𝑛𝑥)+𝑑_{𝑛}sin⁡(𝑛𝑥)\end{aligned}


$$

Let $f(x)$ and $g(x)$ be $2\pi$-periodic extensions of some functions from $x \in [-\pi,\pi)$ to $x \in \mathbb{R}$ with the Fourier series shown above. What are the Fourier constant coefficient, the $3\textrm{rd}$ Fourier sine coefficient, and the $8\textrm{th}$ Fourier cosine coefficient of $-3f(x)+4g(x)$?

#### Explanation

Let $f(x)$ and $g(x)$ be $2\pi$-periodic functions with Fourier series

$$


\begin{aligned}𝑓(𝑥) & ∼\frac{𝑎_{0}}{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(𝑎_{𝑛}cos⁡(𝑛𝑥)+𝑏_{𝑛}sin⁡(𝑛𝑥)), \\ 𝑔(𝑥) & ∼\frac{𝑐_{0}}{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(𝑐_{𝑛}cos⁡(𝑛𝑥)+𝑑_{𝑛}sin⁡(𝑛𝑥)).\end{aligned}


$$

Then for any constants $\alpha$ and $\beta$,

$$


\alpha f(x) + \beta g(x) \sim \frac{\alpha a_0 + \beta c_0}{2} + \sum_{n=1}^{\infty} \Big( (\alpha a_n + \beta c_n)\cos(nx) + (\alpha b_n + \beta d_n)\sin(nx) \Big).


$$

Using the linearity property of Fourier series, the corresponding Fourier coefficients of $-3f(x)+4g(x)$ are

- $-3a_0+4c_0$ for the constant coefficient,

- $-3a_n+4c_n,$ $n \ge 1$ for the cosine coefficients, and

- $-3b_n+4d_n,$ $n \ge 1$ for the sine coefficients.

Therefore,

- the Fourier constant coefficient of $-3f(x)+4g(x)$ is $-3a_0+4c_0$,

- the $3$rd Fourier sine coefficient of $-3f(x)+4g(x)$ is $-3b_3+4d_3$, and

- the $8$th Fourier cosine coefficient of $-3f(x)+4g(x)$ is $-3a_8+4c_8$.

### Fourier Series Properties: Vertical Shifting

Some simple transformations of a periodic function have very predictable effects on its Fourier coefficients. First, we consider the effect of *adding a constant* (a *vertical shift*).

Assume $f$ has the Fourier series

$$


f(x)\sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}\big(a_n\cos(nx)+b_n\sin(nx)\big).


$$

If $h(x)=f(x)+C$ for a constant $C,$ then only the constant part of the Fourier series changes:

$$


h(x)\sim \dfrac{a_0+2C}{2}+\sum_{n=1}^{\infty}\big(a_n\cos(nx)+b_n\sin(nx)\big).


$$

So, the coefficients of the transformed series are

$$


a_0^{(h)}=a_0+2C, \qquad a_n^{(h)}=a_n, \qquad b_n^{(h)}=b_n.


$$

In the next slides, we will apply this rule to a concrete example.

### Fourier Series Properties: Horizontal Reflection

Another simple transformation is *reflecting a function across the $y$-axis*.

Again, assume $f$ has the Fourier series

$$


f(x)\sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}\big(a_n\cos(nx)+b_n\sin(nx)\big).


$$

If $h(x)=f(-x),$ then cosine terms stay the same while sine terms change sign (because $\cos(nx)$ is even and $\sin(nx)$ is odd):

$$


h(x)\sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}\big(a_n\cos(nx)-b_n\sin(nx)\big).


$$

So, the coefficients of the transformed series are

$$


a_0^{(h)}=a_0, \qquad a_n^{(h)}=a_n, \qquad b_n^{(h)}=-b_n.


$$

Let's see how to apply this rule in practice on the next slides.

### Example: Identifying Effects of Vertical Shifting and Horizontal Reflection on Coefficients

#### Question

$$


f(x) \sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos(nx)+b_n\sin(nx)


$$

Let $f(x)$ be the $2\pi$-periodic extesion of a function from $x \in [-\pi,\pi)$ to $x \in \mathbb{R}$ with the Fourier series shown above. What is the $5$th sine Fourier coefficient of $f(-x)?$

#### Explanation

The Fourier series of $f(x)$ is

$$


f(x) \sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}a_n\cos(nx)+b_n\sin(nx).


$$

Recall that the corresponding Fourier coefficients of $f(-x)$ are

- $a_0$ for the constant coefficient,

- $a_n$ $n \ge 1,$ for the cosine coefficients, and

- $-b_n$ $n \ge 1,$ for the sine coefficients.

Therefore, the $5$th sine coefficient of $f(-x)$ is $-b_5.$

### Fourier Series of Odd and Even Functions

When a $2\pi$-periodic function has symmetry, many of its Fourier coefficients must be zero. This can simplify Fourier series computations dramatically.

Assume $f(x)$ is $2\pi$-periodic and piecewise continuous on $[-\pi,\pi),$ with Fourier series

$$


f(x)\sim \dfrac{a_0}{2}+\sum_{n=1}^{\infty}\big(a_n\cos(nx)+b_n\sin(nx)\big).


$$

We will use the property that the integral of an odd function over a symmetric interval like $[-\pi, \pi]$ is always zero.

- If $f$ is an *even* function, meaning $f(-x)=f(x),$ then all sine coefficients $b_n$ must be zero. This is because each $b_n$ is calculated from an integral of an *odd* function: The Fourier series of an even function has *cosine terms only*:

- If $f$ is an *odd* function, meaning $f(-x)=-f(x),$ then the constant and all cosine coefficients (both $a_0$ and $a_n$) must be zero. This is because these coefficients are calculated from integrals of *odd* functions: The Fourier series of an odd function has *sine terms only*:

**Note:** We may use either $[-\pi,\pi)$ or $[-\pi,\pi]$ as the base interval. Including or excluding the endpoints does not affect the conclusions.

Let's see how this works on concrete examples below.

### Example: Parity Recognition and Series Type

#### Question

Consider the function $f(x)=x\cos(2x)$ on $x \in [-\pi,\pi].$ Complete the statements below by filling in the blanks. Determine if the function $f(x)$ is odd or even, and which terms of the corresponding Fourier series of $f(x)$ must be zero.

#### Explanation

To determine whether $f$ is even or odd, we compare $f(-x)$ and $f(x){:}$

$$


\begin{aligned}𝑓(−𝑥) & =(−𝑥)cos⁡(2(−𝑥)) \\ & =(−𝑥)cos⁡(−2𝑥) \\ & =(−𝑥)cos⁡(2𝑥) \\ & =−𝑓(𝑥).\end{aligned}


$$

Since $f(-x) = -f(x),$ we have that $f$ is odd.

For Fourier series on $[-\pi,\pi],$ the cosine coefficients are given by

$$


a_n=\frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\cos(nx)\,\text{d}x,


$$

and the constant coefficient is

$$


a_0=\frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\,\text{d}x.


$$

Here, $f(x)$ is odd and $\cos(nx)$ is even, so $f(x)\cos(nx)$ is odd. Also, $f(x)$ itself is odd.

Now, the integral of an odd function over $[-\pi,\pi]$ is $0.$ Thus, $a_n=0$ for all $n\ge1,$ and $a_0=0.$

Therefore, the function $f(x)$ is $\boxed{\text{odd}}$ and the $\boxed{\text{cosine}}$ terms in its Fourier series must be zero.
