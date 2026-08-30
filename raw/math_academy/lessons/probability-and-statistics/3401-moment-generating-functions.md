# Moment-Generating Functions

Source: https://www.mathacademy.com/topics/3401?courseId=73
Topic ID: 3401

## Prerequisites

- [Introduction to Integration by Parts](../ap-calculus-bc/317-introduction-to-integration-by-parts.md)
- [Improper Integrals Over the Real Line](../ap-calculus-bc/1382-improper-integrals-over-the-real-line.md)
- [Moments of Continuous Random Variables](./2987-moments-of-continuous-random-variables.md)
- [Open and Closed Sets](../multivariable-calculus/4097-open-and-closed-sets.md)

## Lesson

### Introduction

Let $X$ be a discrete random variable with probability mass function $f(x)$ and support $S$. **The moment-generating function** (or **MGF** or **Laplace transform**) of $X$ is defined as

$$


M(t) = \textrm E \left[ e^{tX} \right] = \sum_{x \in S} f(x) e^{tx}.


$$

The MGF of a random variable exists if $M(t)$ is finite in some open neighborhood of $t=0.$

For example, consider the random variable $X$ with the following probability mass function.

The MGF of $X$ is given by

$$


\begin{aligned}𝑀(𝑡) & =\underset{𝑥∈𝑆}{∑}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =\underset{\underset{𝑥=1}{∑}}{\overset{}{3}}𝑓(𝑥)𝑒^{𝑡𝑥} \\ & =𝑓(1)𝑒^{𝑡}+𝑓(2)𝑒^{2𝑡}+𝑓(3)𝑒^{3𝑡} \\ & =\frac{1}{2}𝑒^{𝑡}+\frac{1}{3}𝑒^{2𝑡}+\frac{1}{6}𝑒^{3𝑡},\end{aligned}


$$

which is finite for every $t \in \mathbb{R}.$

We can use moment-generating functions to calculate the moments of a probability distribution. More importantly, we also use them to prove many important theorems about probability distributions and random variables. We'll see some examples of this in future lessons.

### Example: Computing a Moment-Generating Function for a Discrete Random Variable

#### Question

Calculate the moment-generating function (MGF) for the discrete random variable $X,$ given that $X$ has the probability mass function $f(x)$ shown in the table below.

#### Explanation

For a discrete random variable $X$ with probability mass function $f(x)$ and support $S,$ the MGF is defined as

$$


M(t) = \textrm E \left[ e^{tX} \right] = \sum_{x \in S} f(x) e^{tx}.


$$

Let $S = \{0, 1, 2, 3, 4 \}$ be the support. Then, the MGF is given by

$$


\begin{aligned}𝑀(𝑡) & =𝑓(0)𝑒^{0𝑡}+𝑓(1)𝑒^{𝑡}+𝑓(2)𝑒^{2𝑡}+𝑓(3)𝑒^{3𝑡}+𝑓(4)𝑒^{4𝑡} \\ & =0.1+0.2𝑒^{𝑡}+0.4𝑒^{2𝑡}+0.2𝑒^{3𝑡}+0.1𝑒^{4𝑡}.\end{aligned}


$$

### Moment-Generating Functions for Continuous Random Variables

Let $X$ be a continuous random variable with probability density function $f(x).$ The MGF of $X$ is defined as

$$


M(t) =\textrm E \left[ e^{tX} \right] =\int^{\infty}_{-\infty} f (x) e^{tx} \textrm dx.


$$

For example, suppose that the continuous random $X$ has the following probability distribution:

$$


\begin{aligned}1,\, & 0≤𝑥≤1 \\ 0, & otherwise\end{aligned}


$$

Then, the MGF of $X$ is given by

$$


\begin{aligned}𝑀(𝑡) & =∫_{10}^{}𝑓(𝑥)𝑒^{𝑡𝑥}\,d𝑥 \\ & =∫_{10}^{}𝑒^{𝑡𝑥}\,d𝑥.\end{aligned}


$$

Calculating our integral, we get

$$


\begin{aligned}𝑀(𝑡) & =∫_{10}^{}𝑒^{𝑡𝑥}\,d𝑥 \\ & =\frac{𝑒^{𝑡𝑥}}{𝑡}_{10}^{} \\ & =\frac{𝑒^{𝑡}−1}{𝑡}.\end{aligned}


$$

Notice that this result is not valid for $t=0.$ For $t=0,$ we have

$$


\begin{aligned}𝑀(0) & =∫_{10}^{}𝑒^{0𝑥}\,d𝑥 \\ & =∫_{10}^{}\,d𝑥 \\ & =1.\end{aligned}


$$

Finally, the MGF for our continuous random variable $X$ is

$$


\begin{aligned}\frac{𝑒^{𝑡}−1}{𝑡},\, & 𝑡≠0 \\ 1, & 𝑡=0.\end{aligned}


$$

### Example: Computing a Moment-Generating Function for a Continuous Random Variable

#### Question

Calculate the moment-generating function (MGF) for the random variable $X,$ given that $X$ has the following probability distribution:

$$


\begin{aligned}\frac{2}{3}𝑥, & 0≤𝑥≤1 \\ \frac{2}{3}, & 1<𝑥≤2 \\ 0, & otherwise\end{aligned}


$$

#### Explanation

Let $X$ be a continuous random variable with probability density function $f(x).$ The MGF of $X$ is defined as

$$


M(t) =\textrm E \left[ e^{tX} \right] =\int^{\infty}_{-\infty} f (x) e^{tx} \textrm dx.


$$

So, for the given random variable, the MGF is given by

$$


\begin{aligned}𝑀(𝑡) & =∫_{20}^{}𝑓(𝑥)𝑒^{𝑡𝑥}\,d𝑥 \\ & =∫_{10}^{}\frac{2}{3}𝑥𝑒^{𝑡𝑥}\,d𝑥+∫_{21}^{}\frac{2}{3}𝑒^{𝑡𝑥}\,d𝑥.\end{aligned}


$$

First, we calculate the integrals for $t \neq 0:$

$$


\begin{aligned}𝑀(𝑡) & =∫_{10}^{}\frac{2}{3}𝑥𝑒^{𝑡𝑥}\,d𝑥+∫_{21}^{}\frac{2}{3}𝑒^{𝑡𝑥}\,d𝑥 \\ & =\frac{2}{3}∫_{10}^{}𝑥𝑒^{𝑡𝑥}\,d𝑥+\frac{2𝑒^{𝑡𝑥}}{3𝑡}_{21}^{} \\ & =\frac{2}{3}∫_{10}^{}𝑥𝑒^{𝑡𝑥}\,d𝑥+\frac{2(𝑒^{2𝑡}−𝑒^{𝑡})}{3𝑡}\end{aligned}


$$

To solve $\displaystyle \int_{0}^{1} x e^{tx},$ we first find $\displaystyle \int xe^{tx} \,\textrm{d}x$ using the by-parts formula, given by

$$


\int uv'\,\textrm{d}x= uv- \int u'v\,\textrm{d}x.


$$

We set

$$


\begin{aligned}𝑢=𝑥\, & ⟹\,𝑢^{′}=1 \\ 𝑣^{′}=𝑒^{𝑡𝑥}\, & ⟹\,𝑣=\frac{𝑒^{𝑡𝑥}}{𝑡}.\end{aligned}


$$

Substituting the above into the integration by parts formula, we get

$$


\begin{aligned}∫𝑥𝑒^{𝑡𝑥}\,d𝑥 & =\frac{𝑥𝑒^{𝑡𝑥}}{𝑡}−∫\frac{𝑒^{𝑡𝑥}}{𝑡}\,d𝑥 \\ & =\frac{𝑥𝑒^{𝑡𝑥}}{𝑡}−\frac{𝑒^{𝑡𝑥}}{𝑡^{2}}+𝐶 \\ & =\frac{(𝑥𝑡−1)𝑒^{𝑡𝑥}}{𝑡^{2}}+𝐶.\end{aligned}


$$

So, we have

$$


\begin{aligned}𝑀(𝑡) & =\frac{2}{3}∫_{10}^{}𝑥𝑒^{𝑡𝑥}\,d𝑥+\frac{2(𝑒^{2𝑡}−𝑒^{𝑡})}{3𝑡} \\ & =\frac{2(𝑥𝑡−1)𝑒^{𝑡𝑥}}{3𝑡^{2}}_{10}^{}+\frac{2(𝑒^{2𝑡}−𝑒^{𝑡})}{3𝑡} \\ & =\frac{2𝑒^{𝑡}(𝑡−1)+2}{3𝑡^{2}}+\frac{2(𝑒^{2𝑡}−𝑒^{𝑡})}{3𝑡} \\ & =\frac{2𝑒^{𝑡}(𝑡−1)+2}{3𝑡^{2}}+\frac{2𝑡(𝑒^{2𝑡}−𝑒^{𝑡})}{3𝑡^{2}} \\ & =\frac{2𝑡𝑒^{𝑡}−2𝑒^{𝑡}+2+2𝑡𝑒^{2𝑡}−2𝑡𝑒^{𝑡}}{3𝑡^{2}} \\ & =\frac{2𝑡𝑒^{2𝑡}−2𝑒^{𝑡}+2}{3𝑡^{2}} \\ & =\frac{2(𝑡𝑒^{2𝑡}−𝑒^{𝑡}+1)}{3𝑡^{2}}.\end{aligned}


$$

If $t=0,$ we get

$$


\begin{aligned}𝑀(0) & =∫_{20}^{}𝑓(𝑥)\,d𝑥 \\ & =∫_{10}^{}\frac{2}{3}𝑥\,d𝑥+∫_{21}^{}\frac{2}{3}\,d𝑥 \\ & =1.\end{aligned}


$$

Finally, the MGF for the random variable $X$ is

$$


\begin{aligned}\frac{2(𝑒^{2𝑡}−𝑒^{𝑡}+1)}{3𝑡^{2}} & 𝑡≠0 \\ 1 & 𝑡=0.\end{aligned}


$$
