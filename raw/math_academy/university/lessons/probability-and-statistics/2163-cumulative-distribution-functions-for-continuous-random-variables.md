# Cumulative Distribution Functions for Continuous Random Variables

Source: https://www.mathacademy.com/topics/2163?courseId=73
Topic ID: 2163

## Prerequisites

- [Cumulative Distribution Functions for Discrete Random Variables](../discrete-mathematics/2024-cumulative-distribution-functions-for-discrete-random-variables.md)
- [Continuous Random Variables Over Infinite Domains](./4100-continuous-random-variables-over-infinite-domains.md)

## Lesson

### Introduction

The cumulative distribution function (or CDF) of a continuous random variable is defined the same way as for a discrete random variable.

Given a continuous random variable $X,$ the CDF is the function $F(x)$ such that

$$


F(x) = P(X \leq x).


$$

If our random variable has the probability density function (or PDF) $f(x),$ then we have

$$


F(x) = P(X \leq x) = \int_{-\infty}^x f(t) \, \textrm dt.


$$

Note that we use $f(t)dt$ in the integrand because $x$ serves as the upper limit of integration.

For example, consider the random variable $X$ with the following PDF:

$$


\begin{aligned}\frac{2}{𝜋(1+𝑥^{2})},\, & 𝑥∈[0,∞) \\ 0, & otherwise\end{aligned}


$$

Since $f(x)= 0$ for all $x < 0,$ we have

$$


F(x) = \int_{-\infty}^x 0 \, \textrm dt = 0


$$

if $x<0.$

To compute the CDF for $x\geq 0,$ we integrate $f(x)$ as follows:

$$


\begin{aligned}𝐹(𝑥) & =∫_{𝑥−∞}𝑓(𝑡)\,d𝑡 \\ & =∫_{0−∞}𝑓(𝑡)\,d𝑡+∫_{𝑥0}𝑓(𝑡)\,d𝑡 \\ & =0+∫_{𝑥0}\frac{2}{𝜋(1+𝑡^{2})}\,d𝑡 \\ & =\frac{2}{𝜋}arctan⁡𝑡_{𝑥0} \\ & =\frac{2}{𝜋}arctan⁡𝑥−\frac{2}{𝜋}(0) \\ & =\frac{2}{𝜋}arctan⁡𝑥\end{aligned}


$$

Expressing our CDF as a function defined over the entire real line, we get

$$


\begin{aligned}0, & \,𝑥<0, \\ \frac{2}{𝜋}arctan⁡𝑥, & \,𝑥≥0.\end{aligned}


$$

### Example: Finding a CDF Given a PDF With a Lower Bound

#### Question

Given that the random variable $X$ has the probability density function

$$


\begin{aligned}𝑒^{−𝑥},\, & 𝑥≥0, \\ 0,\, & 𝑥<0,\end{aligned}


$$

find the cumulative distribution function $F(x).$

#### Explanation

Since our random variable $X$ has a probability distribution function $f(x)$ that is strictly positive only for $x \geq 0,$ the cumulative distribution function takes the following form:

$$


\begin{aligned}0, & 𝑥<0, \\ ∫_{𝑥0}𝑓(𝑡)\,d𝑡, & 𝑥≥0.\end{aligned}


$$

For the given probability density function, we have

$$


\begin{aligned}∫_{𝑥0}𝑓(𝑡)\,d𝑡 & =∫_{𝑥0}𝑒^{−𝑡}\,d𝑡 \\ & =−𝑒^{−𝑡}_{𝑥0} \\ & =−𝑒^{−𝑥}+1 \\ & =1−𝑒^{−𝑥}.\end{aligned}


$$

So, the cumulative distribution function is given by

$$


\begin{aligned}0, & 𝑥<0, \\ 1−𝑒^{−𝑥}, & 𝑥≥0.\end{aligned}


$$

### Example: Computing a CDF Given a PDF That’s Nonzero Over All Real Numbers

#### Question

Given that the random variable $X$ has the probability density function

$$


f(x) = e^{-|2x|}, \quad x \in (-\infty, \infty),


$$

find the cumulative distribution function $F(x).$

#### Explanation

Since our random variable $X$ has a probability distribution function $f(x)$ that involves an absolute value, the cumulative distribution function takes the following form:

$$


\begin{aligned}∫_{𝑥−∞}𝑒^{2𝑡}\,d𝑡, & 𝑥<0, \\ ∫_{0−∞}𝑒^{2𝑡}\,d𝑡+∫_{𝑥0}𝑒^{−2𝑡}\,d𝑡, & 𝑥≥0.\end{aligned}


$$

Let's compute the integrals.

- If $x \leq 0,$ we have Therefore,

- If $x > 0,$ we have As a result, we get

So, the cumulative distribution function is given by

$$


\begin{aligned}\frac{𝑒^{2𝑥}}{2}, & 𝑥<0, \\ 1−\frac{𝑒^{−2𝑥}}{2}, & 𝑥≥0.\end{aligned}


$$

### Finding a CDF Given a PDF With Lower and Upper Bounds

When a random variable $X$ has a probability distribution function $f(x)$ that is strictly positive on the interval $a \leq x \leq b$ only, we have

- $P(X \leq x) = 0$ for $x < a,$ and

- $P(X \leq x) = 1$ for $x > b.$

In these cases, the cumulative distribution function takes the following form:

$$


\begin{aligned}0, & 𝑥<𝑎 \\ ∫_{𝑥𝑎}𝑓(𝑡)\,d𝑡, & 𝑎≤𝑥≤𝑏 \\ 1, & 𝑥>𝑏\end{aligned}


$$

### Example: Finding a CDF Given a PDF With Lower and Upper Bounds

#### Question

Given that the random variable $X$ has the probability density function

$$


\begin{aligned}\frac{1}{72}𝑥,\, & 0≤𝑥≤12, \\ 0,\, & otherwise,\end{aligned}


$$

find the cumulative distribution function $F(x).$

#### Explanation

Since our random variable $X$ has a probability distribution function $f(x)$ that is strictly positive only for $0 \leq x \leq 12,$ the cumulative distribution function takes the following form:

$$


\begin{aligned}0, & 𝑥<0 \\ ∫_{𝑥0}𝑓(𝑡)\,d𝑡, & 0≤𝑥≤12 \\ 1, & 𝑥>12\end{aligned}


$$

For the given probability density function, we have

$$


\begin{aligned}∫_{𝑥0}𝑓(𝑡)\,d𝑡 & =∫_{𝑥0}\frac{1}{72}𝑡\,d𝑡 \\ & =\frac{1}{144}𝑡^{2}_{𝑥0} \\ & =\frac{1}{144}𝑥^{2}.\end{aligned}


$$

So, the cumulative distribution function is given by

$$


\begin{aligned}0, & 𝑥<0 \\ \frac{𝑥^{2}}{144}, & 0≤𝑥≤12 \\ 1, & 𝑥>12.\end{aligned}


$$

### Using a CDF to Compute a Probability Over an Interval

As with discrete random variables, we can use the CDF of a continuous random variable to quickly compute a probability over an interval:

$$


P(a \leq X \leq b) = F(b) - F(a)


$$

For example, suppose that a random variable $X$ has the following CDF:

$$


F(x) = \dfrac{1}{1+e^{-x}}, \qquad -\infty < x < \infty.


$$

We can use the above CDF to quickly compute $P(0 \leq x \leq 1),$ as follows:

$$


\begin{aligned}𝑃(0≤𝑥≤1) & =𝐹(1)−𝐹(0) \\ & =\frac{1}{1+𝑒^{−1}}−\frac{1}{1+𝑒^{0}} \\ & =\frac{1}{1+𝑒^{−1}}−\frac{1}{2} \\ & ≈0.231\end{aligned}


$$

Remember that for continuous random variables, it doesn't matter whether or not we include the endpoints of the interval, so we have

$$


P(0 \leq X \leq 1) = P(0 < X \leq 1) = P(0 \leq X < 1) = P(0 < X < 1) = 0.231.


$$

In general, for a continuous random variable $X,$ we have

$$


P(a \leq X \leq b) = P(a < X \leq b) = P(a \leq X < b) = P(a < X < b) = F(b) - F(a).


$$

### Example: Computing a Probability Over an Interval Using a CDF

#### Question

Given that the random variable $X$ has the cumulative distribution function

$$


\begin{aligned}0, & 𝑥<5 \\ \frac{𝑥^{2}−25}{75}, & 5≤𝑥≤10 \\ 1, & 𝑥>10,\end{aligned}


$$

find $P(2\leq X \leq 6).$

#### Explanation

Remember that for continuous random variables, it doesn't matter whether or not we include the endpoints of the interval. So we can perform this computation as follows:

$$


\begin{aligned}𝑃(2≤𝑋≤6) & =𝑃(2<𝑋≤6) \\ & =𝑃(𝑋≤6)−𝑃(𝑋≤2) \\ & =𝐹(6)−𝐹(2) \\ & =\frac{6^{2}−25}{75}−0 \\ & =\frac{11}{75}\end{aligned}


$$
