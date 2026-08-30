# Constructing Moment-Generating Functions for Continuous Probability Distributions

Source: https://www.mathacademy.com/topics/3601?courseId=73
Topic ID: 3601

## Prerequisites

- [Integrating Functions by Completing the Square](../../../ap-courses/lessons/ap-calculus-ab/444-integrating-functions-by-completing-the-square.md)
- [The Continuous Uniform Distribution](./791-the-continuous-uniform-distribution.md)
- [The Normal Distribution](./1843-the-normal-distribution.md)
- [The Chi-Square Distribution](./3023-the-chi-square-distribution.md)
- [The Gamma Distribution](./3075-the-gamma-distribution.md)
- [Constructing Moment-Generating Functions for Discrete Probability Distributions](./3288-constructing-moment-generating-functions-for-discrete-probability-distributions.md)

## Lesson

### Introduction

Let $X$ be a continuous random variable with probability density function $f(x).$ Recall that the moment-generating function of $X$ is defined as

$$


M(t) =\textrm E \left[ e^{tX} \right] =\int^{\infty}_{-\infty} f (x) e^{tx} \textrm dx.


$$

In this lesson, we'll construct moment-generating functions for some important continuous probability distributions, namely:

- the uniform distribution

- the exponential distribution

- the normal distribution

- the chi-square distribution

As we'll soon see, we can use the moment-generating functions to prove certain properties about these distributions.

Let's begin by considering the MGF of a uniformly distributed random variable.

### Example: MGFs of Continuous Uniform Random Variables

#### Question

Find the moment-generating function $M(t)$ of $X\sim U(0, 3)$ for $t\neq 0.$

#### Explanation

The moment-generating function of a continuous random variable $X$ is given by

$$


M(t) =\textrm E \left[ e^{tX} \right] =\int^{\infty}_{-\infty} f (x) e^{tx} \,\textrm dx


$$

where $f(x)$ is its probability density function.

Given that $X\sim U(0, 3),$ we have the following probability density function:

$$


\begin{aligned}\frac{1}{3}, & 0<𝑥<3 \\ 0, & otherwise\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =∫_{∞−∞}^{}𝑓(𝑥)𝑒^{𝑡𝑥}d𝑥 \\ & =∫_{30}^{}\frac{1}{3}𝑒^{𝑡𝑥}d𝑥 \\ & =\frac{1}{3}⋅\frac{𝑒^{𝑡𝑥}}{𝑡}_{30}^{} \\ & =\frac{1}{3}⋅(\frac{𝑒^{3𝑡}}{𝑡}−\frac{1}{𝑡}) \\ & =\frac{𝑒^{3𝑡}−1}{3𝑡}.\end{aligned}


$$

Notice that when finding the antiderivative, we used the fact that $t\neq0,$ which ensures we can divide by $t.$

### Example: MGFs of Exponential Random Variables

#### Question

Find the moment-generating function $M(t)$ of $X\sim \mathrm{Exp}(5)$ for $t < 5.$

#### Explanation

The moment-generating function of a continuous random variable $X$ is given by

$$


M(t) =\textrm E \left[ e^{tX} \right] =\int^{\infty}_{-\infty} f (x) e^{tx} \,\textrm dx


$$

where $f(x)$ is its probability density function.

Given that $X\sim \mathrm{Exp}(5),$ we have the following probability density function:

$$


\begin{aligned}5𝑒^{−5𝑥}, & 𝑥≥0 \\ 0, & otherwise\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =∫_{∞−∞}^{}𝑓(𝑥)𝑒^{𝑡𝑥}d𝑥 \\ & =∫_{∞0}^{}5𝑒^{−5𝑥}𝑒^{𝑡𝑥}\,d𝑥 \\ & =∫_{∞0}^{}5𝑒^{(𝑡−5)𝑥}\,d𝑥.\end{aligned}


$$

Now, note the following:

- For $t=5,$ our integral becomes which doesn't converge.

- For $t \neq 5,$ our integral becomes To evaluate the limit at infinity, we consider two cases: If $t < 5,$ then $t-5< 0,$ and $\lim\limits_{x \to \infty} e^{(t - 5)x} = 0.$ If $t > 5,$ then $t-5 > 0,$ and $\lim\limits_{x \to \infty} e^{(t - 5)x} = \infty.$

Therefore,

$$


M(t) = - \dfrac{5}{t-5} = \boxed{\color{blue}\dfrac{5}{5-t}}, \qquad t < 5


$$

and $M(t)$ is undefined for $t \geq 5.$

### Example: MGFs of Normal Random Variables

#### Question

Find the moment-generating function $M(t)$ of $X\sim N(0, 1).$

**

$$


f(x) = \dfrac{1}{\sqrt{2\pi}} e^{-x^2/2}.


$$

**

$$


\int^{\infty}_{-\infty} e^{-b(x+a)^2} \textrm dx = \sqrt{\dfrac{\pi}{b}}


$$

where $a\in \mathbb R$ and $b \in \mathbb R^+.$

#### Explanation

The moment-generating function of a continuous random variable $X$ is given by

$$


M(t) =\textrm E \left[ e^{tX} \right] =\int^{\infty}_{-\infty} f (x) e^{tx} \,\textrm dx


$$

where $f(x)$ is its probability density function.

We are given that

$$


f(x) = \dfrac{1}{\sqrt{2\pi}} e^{-x^2/2}.


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =∫_{∞−∞}^{}𝑓(𝑥)𝑒^{𝑡𝑥}\,d𝑥 \\ & =∫_{∞−∞}^{}\frac{1}{\sqrt{√2𝜋}}𝑒^{−𝑥^{2}/2}⋅𝑒^{𝑡𝑥}\,d𝑥 \\ & =\frac{1}{\sqrt{√2𝜋}}∫_{∞−∞}^{}𝑒^{−𝑥^{2}/2+𝑡𝑥}\,d𝑥.\end{aligned}


$$

Let's express the exponent with a common denominator and complete the square:

$$


\begin{aligned}−\frac{𝑥^{2}}{2}+𝑡𝑥 & =−\frac{𝑥^{2}−2𝑡𝑥}{2} \\ & =−\frac{𝑥^{2}−2𝑡𝑥+𝑡^{2}−𝑡^{2}}{2} \\ & =−\frac{(𝑥−𝑡)^{2}−𝑡^{2}}{2} \\ & =−\frac{(𝑥−𝑡)^{2}}{2}+\frac{𝑡^{2}}{2}\end{aligned}


$$

Substituting the above result in our integral, we get

$$


\begin{aligned}𝑀(𝑡) & =\frac{1}{\sqrt{√2𝜋}}∫_{∞−∞}^{}𝑒^{−𝑥^{2}/2+𝑡𝑥}\,d𝑥 \\ & =\frac{𝑒^{𝑡^{2}/2}}{\sqrt{√2𝜋}}∫_{∞−∞}^{}𝑒^{−(𝑥−𝑡)^{2}/2}\,d𝑥.\end{aligned}


$$

Next, by applying the given formula

$$


\int^{\infty}_{-\infty} e^{-b(x+a)^2} \,\textrm dx = \sqrt{\dfrac{\pi}{b}},


$$

with $a=-t$ and $b=\dfrac{1}{2},$ we get

$$


\int^{\infty}_{-\infty} e^{-(x-t)^2/2} \,\textrm dx = \sqrt{2 \pi}.


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =\frac{𝑒^{𝑡^{2}/2}}{\sqrt{√2𝜋}}∫_{∞−∞}^{}𝑒^{−(𝑥−𝑡)^{2}/2}\,d𝑥 \\ & =\frac{𝑒^{𝑡^{2}/2}}{\sqrt{√2𝜋}}⋅\sqrt{√2𝜋} \\ & =𝑒^{𝑡^{2}/2}.\end{aligned}


$$

### Example: MGFs of Chi-Square Random Variables

#### Question

Find the moment-generating function $M(t)$ of $X\sim \chi^2(4)$ for $t < \dfrac12.$

**

$$


\begin{aligned}\frac{𝑥⋅𝑒^{−𝑥/2}}{4⋅Γ(2)} & 𝑥≥0, \\ 0 & otherwise\end{aligned}


$$

**

$$


\Gamma(k) = \int_{0}^\infty t^{k-1} e^{-t}\,\mathrm d t


$$

is the gamma function.

#### Explanation

The moment-generating function of a continuous random variable $X$ is given by

$$


M(t) =\textrm E \left[ e^{tX} \right] =\int^{\infty}_{-\infty} f (x) e^{tx}\, \textrm dx


$$

where $f(x)$ is its probability density function.

We are given that

$$


f(x) = \dfrac{{x} \cdot e^{-x/2}}{4 \cdot \Gamma\left( 2 \right)}.


$$

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =∫_{∞−∞}^{}𝑓(𝑥)𝑒^{𝑡𝑥}\,d𝑥 \\ & =∫_{∞0}^{}\frac{𝑥⋅𝑒^{−𝑥/2}}{4⋅Γ(2)}⋅𝑒^{𝑡𝑥}\,d𝑥 \\ & =\frac{1}{4⋅Γ(2)}∫_{∞0}^{}𝑥⋅𝑒^{𝑡𝑥−𝑥/2}\,d𝑥 \\ & =\frac{1}{4⋅Γ(2)}∫_{∞0}^{}𝑥⋅𝑒^{𝑥(𝑡−1/2)}\,d𝑥\end{aligned}


$$

Now, note the following:

- For $t=\dfrac 12$ our integral becomes which doesn't converge.

- For $t > \dfrac 12,$ we have $t - \dfrac 12 > 0,$ which means So, our integral doesn't converge.

- For $t < \dfrac 12,$ we use the substitution Rewriting our integral, we get

Therefore,

$$


\begin{aligned}𝑀(𝑡) & =\frac{1}{4⋅Γ(2)}∫_{∞0}^{}𝑥⋅𝑒^{𝑥(𝑡−1/2)}\,d𝑥 \\ & =\frac{1}{4⋅Γ(2)}⋅\frac{1}{(1/2−𝑡)^{2}}⋅Γ(2) \\ & =\frac{1}{4⋅Γ(2)}⋅\frac{1}{(1/2−𝑡)^{2}}⋅Γ(2) \\ & =\frac{1}{2^{2}}⋅\frac{1}{(1/2−𝑡)^{2}} \\ & =\frac{1}{(1−2𝑡)^{2}}\,for\,𝑡<\frac{1}{2},\end{aligned}


$$

and $M(t)$ is undefined for $t\geq \dfrac 12.$

### A Summary of the MGFs for Some Important Continuous Distributions

The table below gives the moment-generating functions $M(t)$ of some common continuous probability distributions.

From here, we can make some observations:

- At the beginning of this lesson, we proved the formula for a continuous uniform random variable $X\sim U[a,b]$ for some specific values of $a$ and $b,$ where we assumed $t\neq 0.$ However, when $t=0,$ we have

- Notice the similarity between the MGFs of the exponential and gamma random variables. This is reflective of the relationship between the distributions: $\textrm{Exp}(\lambda)$ gives the total time until the next event occurs in a Poisson process, while $\Gamma(\alpha, \lambda)$ gives the total time for $\alpha$ events to occur. In a future lesson, we will discuss the precise relationship between these two MGFs.
