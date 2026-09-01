# Solving ODEs Using Fourier Series

Source: https://www.mathacademy.com/topics/6386?courseId=61
Topic ID: 6386

## Prerequisites

- [Fourier Sine Series](./3196-fourier-sine-series.md)
- [Fourier Cosine Series](./3197-fourier-cosine-series.md)
- [Differentiating and Integrating Fourier Series](./6383-differentiating-and-integrating-fourier-series.md)
- [Resonance in Vibrating Systems](./6720-resonance-in-vibrating-systems.md)

## Lesson

### Introduction

Suppose a linear ODE has a periodic forcing term whose Fourier series is known, for example

$$


y' + ky = f(x), \qquad\text{where}\qquad f(x) \sim \frac{c_0}{2} + \sum_{n=1}^\infty \Big(c_n\cos(\omega_n x) + d_n\sin(\omega_n x)\Big).


$$

A standard strategy is to look for a *particular* solution with the *same Fourier frequencies*:

$$


y_p \sim \frac{a_0}{2} + \sum_{n=1}^\infty \Big(a_n\cos(\omega_n x) + b_n\sin(\omega_n x)\Big)


$$

Then, the method includes the following steps:

- **Step 1:** Differentiate term-by-term. Using $\dfrac{\text{d}}{\text{d}x}\cos(\omega_n x)=-\omega_n\sin(\omega_n x)$ and $\dfrac{\text{d}}{\text{d}x}\sin(\omega_n x)=\omega_n\cos(\omega_n x)$, we get

- **Step 2:** Substitute into the ODE and collect like terms Then, we plug $y_p$ and $y_p'$ into the equation, and rewrite the left-hand side as

- **Step 3:** Equate coefficients. Because the Fourier series representation is unique (up to convergence issues we ignore here), we match: the free terms, and for each $n\ge 1$, the cosine coefficients and sine coefficients. This produces: one equation for $a_0$ (from the constant term), and a $2\times 2$ linear system for $(a_n,b_n)$ for each $n\ge 1$.

- **Step 4:** Write the Fourier series of $y_p.$ After solving for $a_0$, $a_n$, and $b_n$, substitute them back into

Let's see some examples.

### Example: Solving First Order ODEs Given the Fourier Series of the Forcing Function

#### Question

Find the Fourier series of a particular solution of the differential equation

$$


y'-2y=f(x),


$$

where the Fourier series of the $6$-periodic forcing function is given by

$$


f(x) \sim 3 + \sum_{n=1}^\infty \dfrac{12}{n^2\pi}\cos\left(\dfrac{n\pi x}{3}\right).


$$

#### Explanation

We assume that a particular solution has the following Fourier series:

$$


y_p \sim \dfrac{a_0}{2} + \sum_{n=1}^\infty a_n \cos\left(\dfrac{n\pi x}{3}\right) + b_n \sin\left(\dfrac{n\pi x}{3}\right).


$$

Now, we compute the derivative:

$$


\begin{aligned}𝑦_{′𝑝} & ∼\frac{d}{d𝑥}(\frac{𝑎_{0}}{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}cos⁡(\frac{𝑛𝜋𝑥}{3})+𝑏_{𝑛}sin⁡(\frac{𝑛𝜋𝑥}{3})) \\ & ∼0+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}⋅(−\frac{𝑛𝜋}{3}sin⁡(\frac{𝑛𝜋𝑥}{3}))+𝑏_{𝑛}⋅\frac{𝑛𝜋}{3}cos⁡(\frac{𝑛𝜋𝑥}{3}) \\ & ∼\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}−\frac{𝑎_{𝑛}𝑛𝜋}{3}sin⁡(\frac{𝑛𝜋𝑥}{3})+\frac{𝑏_{𝑛}𝑛𝜋}{3}cos⁡(\frac{𝑛𝜋𝑥}{3}).\end{aligned}


$$

Next, we substitute the expressions for $y'_p$ and $y_p$ into the equation:

$$


\begin{aligned} & (\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}−\frac{𝑎_{𝑛}𝑛𝜋}{3}sin⁡(\frac{𝑛𝜋𝑥}{3})+\frac{𝑏_{𝑛}𝑛𝜋}{3}cos⁡(\frac{𝑛𝜋𝑥}{3})) \\ & \,−2(\frac{𝑎_{0}}{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}cos⁡(\frac{𝑛𝜋𝑥}{3})+𝑏_{𝑛}sin⁡(\frac{𝑛𝜋𝑥}{3})) \\ & \,\,=3+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{12}{𝑛^{2}𝜋}cos⁡(\frac{𝑛𝜋𝑥}{3}).\end{aligned}


$$

Rearranging the terms, we get

$$


\begin{aligned} & −𝑎_{0}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(\frac{𝑏_{𝑛}𝑛𝜋}{3}−2𝑎_{𝑛})cos⁡(\frac{𝑛𝜋𝑥}{3}) \\ & \,\,+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}(−\frac{𝑎_{𝑛}𝑛𝜋}{3}−2𝑏_{𝑛})sin⁡(\frac{𝑛𝜋𝑥}{3}) \\ & \,\,\,\,=3+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{12}{𝑛^{2}𝜋}cos⁡(\frac{𝑛𝜋𝑥}{3}).\end{aligned}


$$

Now, equating the free terms and the coefficients next to sines and cosines, we obtain the following system:

$$


\begin{aligned}−𝑎_{0}=3 \\ \frac{𝑏_{𝑛}𝑛𝜋}{3}−2𝑎_{𝑛}=\frac{12}{𝑛^{2}𝜋} \\ −\frac{𝑎_{𝑛}𝑛𝜋}{3}−2𝑏_{𝑛}=0\end{aligned}


$$

From the first equation,

$$


a_0=-3,


$$

which means the constant term is

$$


\dfrac{a_0}{2}=-\dfrac{3}{2}.


$$

Next, from the third equation, $b_n=-\dfrac{a_n n\pi}{6}.$ Substituting this into the second equation gives

$$


\left(-\dfrac{a_n n\pi}{6}\right)\dfrac{n\pi}{3}-2a_n=\dfrac{12}{n^2\pi} \qquad\Rightarrow\qquad a_n=-\dfrac{216}{n^2\pi(n^2\pi^2+36)}.


$$

Therefore, for $b_n$ with $n\ge 1,$ we have

$$


\begin{aligned}𝑏_{𝑛} & =−\frac{𝑎_{𝑛}𝑛𝜋}{6} \\ & =−\frac{𝑛𝜋}{6}⋅(−\frac{216}{𝑛^{2}𝜋(𝑛^{2}𝜋^{2}+36)}) \\ & =\frac{36}{𝑛(𝑛^{2}𝜋^{2}+36)}.\end{aligned}


$$

Therefore, our particular solution is

$$


\begin{aligned}𝑦_{𝑝}∼−\frac{3}{2} & +\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\,−\frac{216}{𝑛^{2}𝜋(𝑛^{2}𝜋^{2}+36)}⋅cos⁡(\frac{𝑛𝜋𝑥}{3}) \\ & +\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\,\frac{36}{𝑛(𝑛^{2}𝜋^{2}+36)}⋅sin⁡(\frac{𝑛𝜋𝑥}{3}).\end{aligned}


$$

### Second Order ODEs With Fourier Series

For second-order linear ODEs, the overall algorithm is the same as for first-order equations:

- we assume a Fourier series for $y_p$,

- substitute into the ODE, and

- match coefficients.

Before we start, we can use the forcing series properties to simplify our work. For a second-order equation of the form

$$


y'' + \omega^2 y = f(x)


$$

with no $y'$ (damping) term, the particular solution can be simplified.

The key insight comes from the fact that the differential operator

$$


L[y] = y'' + \omega^2 y


$$

maps cosines to cosines and sines to sines. This means we can match the form of our assumed solution $y_p$ to the form of the forcing function $f(x),$ which saves a great deal of work.

This leads to some powerful shortcuts:

- If $f(x)$ is a *pure cosine series* (an even function), we can assume $y_p$ is also a pure cosine series (all $b_n=0$).

- If $f(x)$ is a *pure sine series* (an odd function), we can assume $y_p$ is also a pure sine series (all $a_n=0$, including $a_0=0$).

- If the constant term in the series for $f(x)$ is zero, the constant term in $y_p$ will also be zero (so $a_0=0$).

Let's see an example.

### A Worked Example of Solving a Second Order ODE

Consider the differential equation $y''-4y=f(x),$ where the Fourier series of the $2$-periodic forcing function is given by

$$


f(x) \sim \sum_{n=1}^\infty \dfrac{2}{n^2}\cos(n\pi x).


$$

Because $f$ has no free term and is a pure cosine series, we assume

$$


y_p \sim \sum_{n=1}^\infty a_n\cos(n\pi x).


$$

Now, we compute the derivatives:

$$


\begin{aligned}𝑦_{′𝑝} & ∼\frac{d}{d𝑥}(\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{𝑛}cos⁡(𝑛𝜋𝑥))∼\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}−𝑎_{𝑛}𝑛𝜋sin⁡(𝑛𝜋𝑥) \\ 𝑦_{″𝑝} & ∼\frac{d}{d𝑥}(\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}−𝑎_{𝑛}𝑛𝜋sin⁡(𝑛𝜋𝑥))∼\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}−𝑎_{𝑛}𝑛^{2}𝜋^{2}cos⁡(𝑛𝜋𝑥)\end{aligned}


$$

Next, we substitute $y''_p$ and $y_p$ into the equation and have

$$


\sum_{n=1}^\infty -a_n n^2\pi^2\cos(n\pi x) - 4\left(\sum_{n=1}^\infty a_n\cos(n\pi x)\right) = \sum_{n=1}^\infty \dfrac{2}{n^2}\cos(n\pi x).


$$

Rearranging the terms, we get

$$


\sum_{n=1}^\infty -a_n(n^2\pi^2+4)\cos(n\pi x) = \sum_{n=1}^\infty \dfrac{2}{n^2}\cos(n\pi x).


$$

Now, equating the cosine coefficients, we obtain

$$


-a_n(n^2\pi^2+4)=\dfrac{2}{n^2} \qquad\Rightarrow\qquad a_n=-\dfrac{2}{n^2(n^2\pi^2+4)}.


$$

Therefore, a Fourier series for a particular solution is

$$


y_p \sim \sum_{n=1}^\infty \: -\dfrac{2}{n^2(n^2\pi^2+4)} \cdot \cos(n\pi x).


$$

### Example: Solving Second Order ODEs Given the Fourier Series of the Forcing Function

#### Question

Find the Fourier series of a particular solution of the differential equation $y''-y=f(x),$ where the Fourier series of the $2$-periodic forcing function is given by

$$


f(x) \sim 1 + \sum_{n=1}^\infty \dfrac{(-1)^{n+1}}{n^3\pi} \sin(n\pi x).


$$

**

#### Explanation

Because the forcing function has only a constant term and sine terms, we assume a particular solution of the form

$$


y_p \sim \dfrac{a_0}{2} + \sum_{n=1}^\infty b_n \sin(n\pi x).


$$

Now, we compute the derivatives:

$$


\begin{aligned}𝑦_{′𝑝} & ∼\frac{d}{d𝑥}(\frac{𝑎_{0}}{2}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛}sin⁡(𝑛𝜋𝑥))∼\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛}𝑛𝜋cos⁡(𝑛𝜋𝑥) \\ 𝑦_{″𝑝} & ∼\frac{d}{d𝑥}(\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑏_{𝑛}𝑛𝜋cos⁡(𝑛𝜋𝑥))∼\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}−𝑏_{𝑛}𝑛^{2}𝜋^{2}sin⁡(𝑛𝜋𝑥)\end{aligned}


$$

Next, we substitute the expressions for $y''_p$ and $y_p$ into the equation and have

$$


\sum_{n=1}^\infty -b_n n^2\pi^2 \sin(n\pi x) - \left( \dfrac{a_0}{2} + \sum_{n=1}^\infty b_n \sin(n\pi x) \right) = 1 + \sum_{n=1}^\infty \dfrac{(-1)^{n+1}}{n^3\pi} \sin(n\pi x).


$$

Rearranging the terms, we get

$$


-\dfrac{a_0}{2} + \sum_{n=1}^\infty b_n(-n^2\pi^2-1)\sin(n\pi x) = 1 + \sum_{n=1}^\infty \dfrac{(-1)^{n+1}}{n^3\pi} \sin(n\pi x).


$$

Now, equating the free terms and sine coefficients, we obtain:

$$


\begin{aligned}−\frac{𝑎_{0}}{2}=1 \\ 𝑏_{𝑛}(−𝑛^{2}𝜋^{2}−1)=\frac{(−1)^{𝑛+1}}{𝑛^{3}𝜋}\end{aligned}


$$

Therefore, our particular solution is

$$


y_p \sim -1 + \sum_{n=1}^\infty \: \dfrac{(-1)^n}{n^3\pi(n^2\pi^2+1)} \cdot \sin(n\pi x).


$$

### Cases Where the Forcing Term Induces Resonance

A forcing harmonic can cause *resonance* when its frequency matches the natural frequency of the homogeneous equation.

In cases like that, we proceed as follows:

- **Step 1:** Find the natural frequency. For an equation of the form the homogeneous solution oscillates with natural frequency $\omega$.

- **Step 2:** Find the forcing frequencies. If $f$ is $2L$-periodic, then its Fourier series uses harmonics whose frequencies are A harmonic is *resonant* exactly when $\omega_n=\omega$.

- **Step 3:** Form the particular solution ansatz for each harmonic. For a *non-resonant* harmonic ($\omega_n\ne \omega$), we use the standard ansatz: For a *resonant* harmonic ($\omega_n=\omega$), this form overlaps with the homogeneous solution. We must use the *modified ansatz* by multiplying by $x{:}$ This extra factor of $x$ produces a new trial function that can match the forcing term.

When $f$ is given as a Fourier series, we check each harmonic:

- *non-resonant* harmonics contribute ordinary sine/cosine terms to $y_p,$ while

- *resonant* harmonics contribute terms multiplied by $x.$

In particular, the resonant harmonic is the one with index $n$ satisfying

$$


\frac{n\pi}{L}=\omega.


$$

Let's see how this works in practice.

### Example: Identifying Resonant Harmonics

#### Question

Consider the differential equation $y'' + 9\pi^2 y = f(x),$ where the $2$-periodic forcing function is given by

$$


f(x) \sim \sum_{n=1}^\infty \dfrac{1}{n^2}\sin(n\pi x).


$$

What harmonic of the forcing function does the natural frequency of the system match? And what is the resonant component of a particular solution?

#### Explanation

We begin by identifying resonance. The differential equation

$$


y''+9\pi^2 y=f(x)


$$

has a natural frequency of

$$


\omega=\sqrt{9\pi^2}=3\pi.


$$

The frequencies of the forcing harmonics for a $2$-periodic function $\left(L=1\right)$ are

$$


\omega_n=\dfrac{n\pi}{1}=n\pi.


$$

For $n=3$, we have $\omega_3=3\pi.$ Since $\omega_3=\omega,$ the natural frequency of the system matches the frequency of the $n=3$ harmonic of the forcing function. This is the answer to the first question.

For the $n=3$ harmonic, the forcing term is

$$


f_3(x)=\dfrac{1}{9}\sin(3\pi x).


$$

Because this frequency matches the natural frequency, we assume a particular solution of the form

$$


y_{p_3}=x(A\cos(3\pi x)+B\sin(3\pi x)).


$$

Now, we compute the derivatives:

$$


\begin{aligned}𝑦_{′𝑝_{3}}^{} & =(𝐴cos⁡(3𝜋𝑥)+𝐵sin⁡(3𝜋𝑥))+𝑥(−3𝜋𝐴sin⁡(3𝜋𝑥)+3𝜋𝐵cos⁡(3𝜋𝑥)) \\ 𝑦_{″𝑝_{3}}^{} & =−6𝜋𝐴sin⁡(3𝜋𝑥)+6𝜋𝐵cos⁡(3𝜋𝑥)−9𝜋^{2}𝑥(𝐴cos⁡(3𝜋𝑥)+𝐵sin⁡(3𝜋𝑥))\end{aligned}


$$

Next, we substitute the expressions for $y''_{p_3}$ and $y_{p_3}$ into the equation $y''+9\pi^2 y=\dfrac{1}{9}\sin(3\pi x){:}$

$$


\left[-6\pi A\sin(3\pi x)+6\pi B\cos(3\pi x)-9\pi^2 y_{p_3}\right]+9\pi^2 y_{p_3}=\dfrac{1}{9}\sin(3\pi x)


$$

The resonant terms involving $x$ cancel out, leaving

$$


-6\pi A\sin(3\pi x)+6\pi B\cos(3\pi x)=\dfrac{1}{9}\sin(3\pi x).


$$

Now, equating the sine and cosine coefficients, we obtain:

$$


\begin{aligned}−6𝜋𝐴=\frac{1}{9} \\ 6𝜋𝐵=0\end{aligned}


$$

Therefore, the resonant component of a particular solution is

$$


y_{p_3}=-\dfrac{x}{54\pi}\cos(3\pi x).


$$
