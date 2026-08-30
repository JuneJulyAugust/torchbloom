# The Rule of the Lazy Statistician

Source: https://www.mathacademy.com/topics/1335?courseId=154
Topic ID: 1335

## Prerequisites

- [Expected Values of Continuous Random Variables](./4012-expected-values-of-continuous-random-variables.md)

## Lesson

### Introduction

Suppose we have a discrete random variable $X$ with probability mass function $f_X$ and support $S_X = \{-1,0,1\},$ shown below.

Now suppose that we define a new random variable $Y$ as follows:

$$


Y = (X+1)^3.


$$

Computing $\textrm{E}[Y]$ is quite a lot of work if we use only the methods we've seen up to now. Typically, we would need to find the probability mass function $f_Y$ of $Y,$ and then compute $\textrm{E}[Y].$

Thankfully, there is a handy rule, called **the rule of the lazy statistician,** that allows us to compute $\textrm{E}[Y]$ *without* having to find $f_Y$ first! This is useful because $\textrm{E}[Y]$ might be the only quantity we're interested in.

The rule of the lazy statistician states that if $Y = r(X),$ then

$$


\textrm{E}[Y] = \sum_{x \in S_X}r(x) \, f_X(x).


$$

Applying the rule of the lazy statistician with the function $r(x) = (x+1)^3$ for our PMF $f_X,$ we have

$$


\begin{aligned}E[𝑌] & =\underset{𝑥∈𝑆_{𝑋}}{∑}𝑟(𝑥)\,𝑓_{𝑋}(𝑥) \\ & =\underset{𝑥∈𝑆_{𝑋}}{∑}(𝑥+1)^{3}\,𝑓_{𝑋}(𝑥) \\ & =(−1+1)^{3}⋅0.25+(0+1)^{3}⋅0.5+(1+1)^{3}⋅0.25 \\ & =0^{3}⋅0.25+1^{3}⋅0.5+2^{3}⋅0.25 \\ & =0⋅0.25+1⋅0.5+8⋅0.25 \\ & =0+0.5+2 \\ & =2.5\end{aligned}


$$

Therefore, we conclude that $\textrm{E}[Y] = 2.5.$

### Some Comments

The rule of the lazy statistician states that if $Y = r(X),$ then

$$


\textrm{E}[Y] = \sum_{x \in S_X}r(x) \, f_X(x).


$$

Note the following points:

- The reason for the name "the rule of the lazy statistician" is that the rule is sometimes mistaken as a definition when, in fact, it is a statement that requires rigorous proof (we won't do that here).

- The rule is sometimes called the **law of the unconscious statistician** (or **LOTUS**).

- In general $\textrm E[r(X)] \ne r(\textrm E[X]).$

The rule has some nice intuition behind it. We demonstrate with a simple example.

Suppose a spinner has four sides, labeled $1$ through $4.$ Let the random variable $X$ equal the result when the spinner is spun once, and let the function $Y = r(X)$ denote the profit made when the spinner lands on $X = x.$ To calculate the *expected* profit on each spin, we multiply each possible payout by the probability of that payout occurring and sum over all possible values of $X.$

Let's take a look at another example.

### Example: Applying the Rule of the Lazy Statistician for Discrete Random Variables

#### Question

A discrete random variable $X$ has the probability mass function $f(x)$ shown in the table below. Find $\textrm{E}\big[5e^{1-X}\big].$

#### Explanation

For a discrete random variable $X$ and a function $r(x),$ the rule of the lazy statistician states that

$$


\textrm{E}[r(X)] = \sum_{x \in S} r(x) f(x).


$$

In our case, we have

$$


r(x)=5e^{1-x}.


$$

Therefore, we obtain

$$


\begin{aligned}E[5𝑒^{1−𝑥}] & =\underset{𝑥∈𝑆}{∑}5𝑒^{1−𝑥}⋅𝑓(𝑥) \\ & =5𝑒^{1−1}⋅0.2+5𝑒^{1−2}⋅0.8 \\ & =5𝑒^{0}⋅0.2+5𝑒^{−1}⋅0.8 \\ & =5⋅0.2+5𝑒^{−1}⋅0.8 \\ & =1+4𝑒^{−1} \\ & =1+\frac{4}{𝑒}.\end{aligned}


$$

### The Rule of the Lazy Statistician for Continuous Random Variables

Let $X$ be a continuous random variable with the probability density function $f(x)$ and let $Y=r(X)$. Then, the rule of the lazy statistician for continuous random variables states that

$$


\textrm E[Y]=\textrm E[r(X)]=\int^{\infty}_{-\infty} r(x)f(x) \: \textrm{d}x.


$$

Notice the analogy with the discrete case.

### Example: Applying the Rule of the Lazy Statistician for Continuous Random Variables

#### Question

Find $\textrm{E}\big[X^2-3X+3\big],$ given that the continuous random variable $X$ has the probability density function

$$


f(x) = 2x, \qquad 0 < x < 1.


$$

#### Explanation

For a continuous random variable $X$ and a function $r(x),$ the rule of the lazy statistician states that

$$


\textrm{E}[r(X)] = \int^{\infty}_{-\infty} r(x)f(x) \: \textrm{d}x.


$$

In our case, we have

$$


r(X)=x^2-3x+3.


$$

Therefore, we obtain

$$


\begin{aligned}E[𝑋^{2}−3𝑋+3] & =∫_{∞−∞}^{}𝑟(𝑥)𝑓(𝑥)\,d𝑥 \\ & =∫_{10}^{}(𝑥^{2}−3𝑥+3)⋅2𝑥\,d𝑥 \\ & =∫_{10}^{}(2𝑥^{3}−6𝑥^{2}+6𝑥)\,d𝑥 \\ & =[\frac{𝑥^{4}}{2}−2𝑥^{3}+3𝑥^{2}]_{10}^{} \\ & =[\frac{1}{2}−2+3]−0 \\ & =\frac{3}{2}.\end{aligned}


$$

### Example: Applications of LOTUS

#### Question

A stick of length $1$ is broken at a point chosen uniformly at random along its length. Calculate the expected length of the shortest piece.

#### Explanation

For a continuous random variable $X$ and a function $r(x)$, the rule of the lazy statistician states that

$$


\textrm{E}[r(x)] = \int_{-\infty}^{\infty} r(x)f(x) ~ \textrm{d}x,


$$

where $f(x)$ is the probability density function of $X.$

In this problem, the break point $X$ is chosen uniformly from $[0,1]$, so the probability density function is

$$


f(x) = 1, \:\:\:\:\:\: 0 \leq x < 1.


$$

When the stick is broken at point $X$, it is divided into two pieces: one of length $X$ and the other of length $1-X.$ The shorter of the two pieces, $Y$, is therefore given by

$$


Y = \textrm{min}(X, 1-X).


$$

Therefore, we define

$$


r(x) = \textrm{min}(x,1-x).


$$

To evaluate the integral, we express $r(x)$ as an explicit piecewise function. Observe that,

- if $0\leq x < \dfrac{1}{2}$, then $x < 1-x$, so the shorter piece has length $x$,

- if $\dfrac{1}{2} \leq x \leq 1$, then $x \geq 1 - x$, so the shorter piece has length $1-x.$

Therefore,

$$


\begin{aligned}𝑥, & 0≤𝑥<\frac{1}{2}, \\ 1−𝑥, & \frac{1}{2}≤𝑥≤1.\end{aligned}


$$

We now apply the rule of the lazy statistician:

$$


\begin{aligned}E[𝑌] & =E[min(𝑋,1−𝑋)] \\ & =∫_{∞−∞}^{}𝑟(𝑥)𝑓(𝑥)\,d𝑥 \\ & =∫_{\frac{1}{2}0}^{}𝑥⋅1\,d𝑥+∫_{1\frac{1}{2}}^{}(1−𝑥)⋅1\,d𝑥 \\ & =∫_{\frac{1}{2}0}^{}𝑥\,d𝑥+∫_{1\frac{1}{2}}^{}(1−𝑥)\,d𝑥 \\ & =[\frac{𝑥^{2}}{2}]_{\frac{1}{2}0}^{}+[𝑥−\frac{𝑥^{2}}{2}]_{1\frac{1}{2}}^{} \\ & =\frac{1}{2}(\frac{1}{2})^{2}+[(1−\frac{1}{2})−(\frac{1}{2}−\frac{1}{2}(\frac{1}{2})^{2})] \\ & =\frac{1}{8}+[\frac{1}{2}−(\frac{1}{2}−\frac{1}{8})] \\ & =\frac{1}{8}+\frac{1}{8} \\ & =\frac{1}{4}.\end{aligned}


$$

Therefore, the expected length of the shorter piece is $\boxed{\color{blue}\dfrac{1}{4}}.$

### Proof of the Linearity of Expectation

Although $\textrm{E}[r(X)] \ne r(\textrm{E}[X])$ in general, equality is possible for some functions.

For example, we've already seen that if $a$ and $b$ are real constants, then

$$


\textrm{E}[aX+b]=a \, \textrm{E}[X]+b.


$$

Let's prove this using the rule of the lazy statistician for a discrete random variable $X$. In this case, $r(X)=aX+b$, so we have

$$


\begin{aligned}E[𝑎𝑋+𝑏] & =\underset{𝑥∈𝑆}{∑}(𝑎𝑥+𝑏)\,𝑓(𝑥) \\ & =\underset{𝑥∈𝑆}{∑}𝑎𝑥\,𝑓(𝑥)+\underset{𝑥∈𝑆}{∑}𝑏\,𝑓(𝑥) \\ & =𝑎\underset{𝑥∈𝑆}{∑}𝑥\,𝑓(𝑥)+𝑏\underset{𝑥∈𝑆}{∑}𝑓(𝑥) \\ & =𝑎\,E[𝑋]+𝑏.\end{aligned}


$$

A similar proof can be conducted for continuous random variables.

Similarly, for functions $r(x)$ and $s(x)$ and real coefficients $a$ and $b,$ we have

$$


\textrm{E}[a \cdot r(X) + b \cdot s(X)] = a \, \textrm{E}[r(X)] + b \, \textrm{E}[s(X)].


$$
