# Order of Numerical Methods

Source: https://www.mathacademy.com/topics/6399?courseId=155
Topic ID: 6399

## Prerequisites

- [Big-O Notation](./2854-big-o-notation.md)
- [Error in Numerical Methods](./3246-error-in-numerical-methods.md)

## Lesson

### Introduction

Each step of a numerical method produces a local truncation error $\tau,$ which, over multiple steps, accumulates into a global truncation error $e.$ Both LTE and GTE depend on step size $\Delta x.$

The **order** of a numerical method describes how fast these errors shrink as $\Delta x$ decreases. A numerical method has order $p$ if $p$ is the *largest positive* integer such that the global truncation error (GTE) satisfies

$$


e(\Delta x) = \mathcal O\!\left((\Delta x)^p\right)\quad\textrm{as}\quad \Delta x \to 0.


$$

In other words, a numerical method has order $p$ if, for sufficiently small step sizes, reducing the step size by a factor of $k$ reduces the GTE by a factor of approximately $k^p{:}$

$$


\begin{aligned}𝑒(\frac{Δ𝑥}{𝑘}) & ≈𝐾(\frac{Δ𝑥}{𝑘})^{𝑝}=\frac{𝐾(Δ𝑥)^{𝑝}}{𝑘^{𝑝}}≈\frac{𝑒(Δ𝑥)}{𝑘^{𝑝}}\end{aligned}


$$

Let's demonstrate with an example. Suppose a numerical method is used to approximate the solution to an initial value problem.

- With step size $\Delta x = 0.21,$ the observed global truncation error is $e(0.21) = 0.785.$

- With step size $\Delta x = 0.07,$ the observed global truncation error is $e(0.07) = 0.010.$

Using this data, we can estimate the order of the numerical method.

The step size decreases from $0.21$ to $0.07.$ So, it reduces by a factor of

$$


k = \dfrac{0.21}{0.07} = 3.


$$

As a result, for a numerical method of order $p,$ the GTE should decrease by a factor of approximately

$$


k^p = 3^p.


$$

On the other hand, the GTE actually decreases from $0.785$ to $0.010.$ So, it reduces by a factor of

$$


\dfrac{0.785}{0.010} = 78.5.


$$

Comparing the two scale factors for the GTE, we get

$$


\begin{aligned}3^{𝑝} & ≈78.5 \\ 𝑝 & ≈log_{3}⁡(78.5) \\ 𝑝 & ≈3.97….\end{aligned}


$$

Therefore, rounding to the nearest integer, the approximate order of the method is $4.$

But why is order important? Well, a higher order means that the error decreases faster as $\Delta x$ decreases. As a result, higher-order methods can achieve a target accuracy *with fewer steps*. In this way, order predicts the accuracy you gain when you make steps smaller.

### Example: Determining the Order of a Numerical Method By Comparing GTE for Different Step Sizes

#### Question

The global truncation error (GTE) of a numerical method with step size $\Delta x$ is

$$


e(\Delta x) = 4(\Delta x)^3 + (\Delta x)^4.


$$

Complete the following sentences.

$\quad$ With step size $\Delta x = 0.4,$ the global truncation error is $𝑋𝑋𝑋$

$\quad$ With step size $\Delta x = 0.2,$ the global truncation error is $𝑋𝑋𝑋$

$\quad$ Decreasing from $\Delta x = 0.4$ to $\Delta x = 0.2,$ the GTE is reduced by a factor of $𝑋𝑋𝑋$

$\quad$ According to this data, the order of the method is approximately $𝑋𝑋𝑋$

#### Explanation

A numerical method has order $p$ if $p$ is the largest positive integer such that the global truncation error (GTE) satisfies

$$


e(\Delta x) = \mathcal O\!\left((\Delta x)^p\right)\quad\textrm{as}\quad \Delta x \to 0.


$$

The order describes how fast errors shrink as $\Delta x$ decreases.

In other words, a numerical method has order $p$ if, for sufficiently small step sizes, reducing the step size by a factor of $k$ reduces the GTE by a factor of approximately $k^p.$

First, we compute the GTE for the given step sizes:

- With step size $\Delta x = 0.4,$ the GTE is

- With step size $\Delta x = 0.2,$ the GTE is

Next, we determine the order by comparing the errors. The step size decreases from $0.4$ to $0.2.$ So, it reduces by a factor of

$$


k = \dfrac{0.4}{0.2} = 2.


$$

As a result, for a numerical method of order $p,$ the GTE should decrease by a factor of approximately

$$


k^p = 2^p.


$$

On the other hand, the GTE actually decreases from $0.281\,6$ to $0.033\,6.$ So, it reduces by a factor of

$$


\dfrac{0.281\,6}{0.033\,6} = 8.380\,95\ldots \approx \boxed{8.381}.


$$

Comparing the two scale factors for the GTE, we get

$$


\begin{aligned}2^{𝑝} & ≈8.380\,952… \\ 𝑝 & ≈log_{2}⁡(8.380\,95…) \\ 𝑝 & ≈3.067….\end{aligned}


$$

Therefore, rounding to the nearest integer, the estimated order of the method is $\boxed{3}.$

Indeed, this coincides with the definition of the order from the expression for the GTE:

$$


e(\Delta x) = 4(\Delta x)^3 + (\Delta x)^4 \quad\Rightarrow\quad e(\Delta x) = \mathcal O\!\left((\Delta x)^3\right)\quad\textrm{as}\quad \Delta x\to 0.


$$

Hence, the order of the method is $3.$

### Order From Local Truncation Error

An alternative, but equivalent, definition for the **order** can be made in terms of the local truncation error.

A numerical method has **order** $p$ if $p$ is the largest positive integer such that the local truncation error (LTE) satisfies

$$


\tau(\Delta x) = \mathcal O\!\left((\Delta x)^{p+1}\right)\quad\textrm{as}\quad \Delta x \to 0.


$$

In other words, a numerical method has **order** $p$ if, for sufficiently small step sizes, reducing the step size by a factor of $k$ reduces the LTE by a factor of approximately $k^{p+1}.$

But why is the power $p+1$ for LTE but only $p$ for GTE?

Each local truncation error measures the error made in *one step* of the method. If a method has order $p,$ then the error made in a single step shrinks like

$$


\tau(\Delta x) = \mathcal O\!\left((\Delta x)^{p+1}\right).


$$

However, on a fixed interval, using step size $\Delta x$ requires about

$$


N \approx \dfrac1{\Delta x}


$$

steps. The global truncation error results from *accumulating* these local errors over all steps.

Heuristically, adding up $N$ local errors of size $(\Delta x)^{p+1}$ gives

$$


e(\Delta x) \sim N \cdot (\Delta x)^{p+1} \sim \dfrac1{\Delta x} \cdot (\Delta x)^{p+1} = (\Delta x)^p.


$$

Thus, the local truncation error is one power of $\Delta x$ higher than the global truncation error.

Next, we will apply this definition to determine the order of a given numerical method.

### Example: Determining the Order of a Numerical Method By Comparing LTE for Different Step Sizes

#### Question

A numerical method is used to approximate the solution to an initial value problem.

- With step size $\Delta x = 0.24,$ the observed local truncation error is $\tau(0.24) = 0.8.$

- With step size $\Delta x = 0.08,$ the observed local truncation error is $\tau(0.08) = 0.01.$

Estimate the order of the numerical method, rounded to the nearest integer.

#### Explanation

A numerical method has order $p$ if $p$ is the largest positive integer such that the local truncation error (LTE) satisfies

$$


\tau(\Delta x) = \mathcal O\!\left((\Delta x)^{p+1}\right)\quad\textrm{as}\quad \Delta x \to 0.


$$

The order describes how fast errors shrink as $\Delta x$ decreases.

In other words, a numerical method has order $p$ if, for sufficiently small step sizes, reducing the step size by a factor of $k$ reduces the LTE by a factor of approximately $k^{p+1}.$

In our case, the step size decreases from $0.24$ to $0.08.$ So, it reduces by a factor of

$$


k = \dfrac{0.24}{0.08} = 3.


$$

As a result, for a numerical method of order $p,$ the LTE should decrease by a factor of approximately

$$


k^{p+1} = 3^{p+1}.


$$

On the other hand, the LTE actually decreases from $0.8$ to $0.01.$ So, it reduces by a factor of

$$


\dfrac{0.8}{0.01} = 80.


$$

Comparing the two scale factors for the LTE, we get

$$


\begin{aligned}3^{𝑝+1} & ≈80 \\ 𝑝+1 & ≈log_{3}⁡(80) \\ 𝑝+1 & ≈3.987… \\ 𝑝 & ≈2.987….\end{aligned}


$$

Therefore, rounding to the nearest integer, the estimated order of the method is $3.$

### Example: Determining the Order of a Numerical Method Given the GTE or LTE

#### Question

Which of the following expressions for the global truncation error ($e$) or local truncation error ($\tau$) represent a second-order numerical method?

1. $e(\Delta x) = 3(\Delta x)^2 + 4(\Delta x)^5$

2. $\tau(\Delta x) = 0.6(\Delta x)^3 + 2(\Delta x)^4$

3. $e(\Delta x) = 7(\Delta x)^4 + 5(\Delta x)^6$

#### Explanation

For a given numerical method, if $p$ is the largest positive integer such that

- the global truncation error (GTE) satisfies

- the local truncation error (LTE) satisfies

then the method is of order $p.$

With that in mind, let’s check each option:

- For the GTE expression $e(\Delta x) = 3(\Delta x)^2 + 4(\Delta x)^5,$ the dominant term as $\Delta x\to 0$ is $3(\Delta x)^2 = 3(\Delta x)^2.$ So, statement I corresponds to an order $2$ method.

- For the LTE expression $\tau(\Delta x) = 0.6(\Delta x)^3 + 2(\Delta x)^4,$ the dominant term as $\Delta x\to 0$ is $0.6(\Delta x)^3 = 0.6(\Delta x)^{2+1}.$ So, statement II corresponds to an order $2$ method.

- For the GTE expression $e(\Delta x) = 7(\Delta x)^4 + 5(\Delta x)^6,$ the dominant term as $\Delta x\to 0$ is $7(\Delta x)^4 = 7(\Delta x)^4.$ So, statement III corresponds to an order $4$ method.

Therefore, the correct answer is "I and II only".

### Example: Making Inferences Given the Order of a Numerical Method

#### Question

A numerical method for approximating a solution to an initial value problem is known to be order $1.$ Suppose that using step size $\Delta x = 0.4$ produces a local truncation error (LTE) of $\tau(0.4) \approx 0.24.$ If we instead use a step size $\Delta x = 0.1,$ what LTE should we expect?

$$


𝑋𝑋𝑋


$$

#### Explanation

A numerical method has order $p$ if $p$ is the largest positive integer such that the local truncation error (LTE) satisfies

$$


\tau(\Delta x) = \mathcal O\!\left((\Delta x)^{p+1}\right)\quad \textrm{as}\quad \Delta x \to 0.


$$

The order describes how fast errors shrink as $\Delta x$ decreases.

In other words, a numerical method has order $p$ if, for sufficiently small step sizes, reducing the step size by a factor of $k$ reduces the LTE by a factor of approximately $k^{p+1}.$

In our case, the step size decreases from $0.4$ to $0.1.$ So, it reduces by a factor of

$$


k = \frac{0.4}{0.1} = 4.


$$

Now, since the numerical method is of order $1,$ the error is expected to decrease by a factor of

$$


k^{1+1} = 4^2 = 16.


$$

Therefore, using a step size of $\Delta x = 0.1,$ the expected LTE is

$$


\tau(0.1) \approx \frac{0.24}{16} = 0.015.


$$

### Connecting the Definitions of the Order of Numerical Methods

We'll now show that the definition of order with respect to LTE is the same as with respect to GTE.

Indeed, suppose a numerical method with increment formula $\Delta y = \Phi(x, y, \Delta x) \cdot \Delta x$ satisfies the following:

$$


\tau(\Delta x) = \mathcal O\!\left((\Delta x)^{p+1}\right)\quad\textrm{as}\quad \Delta x \to 0


$$

On a fixed interval of length $L,$ the number of steps is $N \approx \dfrac{L}{\Delta x}.$ So, $N = \mathcal O\!\left(\dfrac{1}{\Delta x}\right)$ as $\Delta x \to 0.$

Now, recall the relationship between GTE and LTE, given by

$$


e(\Delta x) = e_N = e_{N-1} + \left[ \Phi(x_{N-1}, y(x_{N-1}), \Delta x) - \Phi(x_{N-1}, y_{N-1}, \Delta x) \right] \cdot \Delta x + \tau_N.


$$

Since $y(x_{N-1}) - y_{N-1} = e_{N-1},$ it is natural to say that changing the input $y$ by $e_{N-1}$ changes $\Phi$ by about a constant multiple of $e_{N-1}.$ So, heuristically,

$$


\Phi(x_{N-1}, y(x_{N-1}), \Delta x) - \Phi(x_{N-1}, y_{N-1}, \Delta x) \approx Ce_{N-1}


$$

for some $C$ that *doesn't* depend on $\Delta x$ (on a fixed interval). Hence, the GTE satisfies approximately

$$


e(\Delta x) = e_N \approx (1+C\Delta x)e_{N-1} + \tau_N.


$$

After $N$ steps, we get

$$


e(\Delta x) \approx (1+C\Delta x)^N e_0 + \sum_{n=1}^N(1+C\Delta x)^{N-n}\tau_n.


$$

Next, note that $(1+C\Delta x)^N \approx e^{CN\Delta x} \approx e^{CL},$ which is $\mathcal O(1)$ as $\Delta x \to 0.$ So, the weights $(1+C\Delta x)^{N-n}$ don't change the *power* of $\Delta x.$

So, we can treat the GTE as roughly the sum of the per-step local errors. Therefore,

$$


e(\Delta x) \approx \sum_{n=1}^N \tau_n


$$

With $\tau_n = \mathcal O\!\left((\Delta x)^{p+1}\right)$ for each $n=1,\ldots,N,$ we get

$$


\begin{aligned}𝑒(Δ𝑥) & =\underset{\underset{𝑛=1}{∑}}{\overset{}{𝑁}}O\,((Δ𝑥)^{𝑝+1}) \\ & =𝑁⋅O\,((Δ𝑥)^{𝑝+1}) \\ & =O\,(\frac{1}{Δ𝑥})⋅O\,((Δ𝑥)^{𝑝+1}) \\ & =O\,((Δ𝑥)^{𝑝}).\end{aligned}


$$

Note that since $p$ is maximal in the LTE definition, this shows the GTE has order $p$ as well.
