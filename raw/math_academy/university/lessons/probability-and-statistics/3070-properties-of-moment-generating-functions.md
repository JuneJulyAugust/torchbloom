# Properties of Moment-Generating Functions

Source: https://www.mathacademy.com/topics/3070?courseId=73
Topic ID: 3070

## Prerequisites

- [Constructing Moment-Generating Functions for Continuous Probability Distributions](./3601-constructing-moment-generating-functions-for-continuous-probability-distributions.md)
- [Independence of Continuous Random Variables](./3863-independence-of-continuous-random-variables.md)

## Lesson

### Introduction

If we know the moment-generating function (MGF) for a random variable $X,$ then we can easily find the MGF for any linear transformation of $X$ using the following theorem:

*If $Y = aX+b,$ where $X$ is a random variable with the MGF $M_X(t),$ then the MGF of $Y$ is*

For example, consider a binomial random variable $X \sim B(0.3, 4),$ which has the MGF

$$


M_X(t) = (0.7 + 0.3e^t)^4.


$$

If we have another random variable $Y = 5X+6,$ then we can use the theorem above to conclude that the MGF for $Y$ is

$$


\begin{aligned}𝑀_{𝑌}(𝑡) & =𝑒^{6𝑡}𝑀_{𝑋}(5𝑡) \\ & =𝑒^{6𝑡}𝑀_{𝑋}(5𝑡) \\ & =𝑒^{6𝑡}(0.7+0.3𝑒^{5𝑡})^{4}.\end{aligned}


$$

To see where this theorem comes from, we apply the definition of the MGF:

$$


\begin{aligned}𝑀_{𝑌}(𝑡) & =E[𝑒^{𝑡𝑌}] \\ & =E[𝑒^{𝑡(𝑎𝑋+𝑏)}] \\ & =E[𝑒^{𝑡𝑎𝑋}⋅𝑒^{𝑡𝑏}] \\ & =𝑒^{𝑡𝑏}⋅E[𝑒^{(𝑎𝑡)𝑋}] \\ & =𝑒^{𝑡𝑏}⋅M_{𝑋}(𝑎𝑡).\end{aligned}


$$

Note that for a fixed value of $t,$ we have that $e^{tb}$ is constant (i.e., it does not depend on $X$), which allows us to take it outside the expectation operator.

### Example: Finding the MGF of a Linearly Transformed Random Variable

#### Question

You're given that if $X \sim \text{Exp}(\lambda),$ the moment-generating function (MGF) of $X$ is

$$


M_X(t) = \dfrac{\lambda}{\lambda - t}, \qquad t < \lambda.


$$

Let $Y = 3X+2,$ where $X \sim \text{Exp}(2).$ What is the MGF of $Y$ for $t < \dfrac23?$

#### Explanation

If $Y = aX+b,$ where $X$ is a random variable with the MGF $M_X(t),$ then the MGF of $Y$ is

$$


M_Y(t) = e^{bt} M_X(at).


$$

For an exponential random variable $X \sim \text{Exp}(\lambda),$ we have

$$


M_X(t) = \dfrac{\lambda}{\lambda - t}, \qquad t < \lambda.


$$

In our case, since $X \sim \text{Exp}(2),$ we have

$$


M_X(t) = \dfrac{2}{2 - t}, \qquad t < 2.


$$

Therefore, since $Y = 3X+2,$ we have

$$


\begin{aligned}𝑀_{𝑌}(𝑡) & =𝑒^{2𝑡}𝑀_{𝑋}(3𝑡) \\ & =𝑒^{2𝑡}⋅\frac{2}{2−3𝑡} \\ & =\frac{2𝑒^{2𝑡}}{2−3𝑡},\end{aligned}


$$

where we assume that $3t < 2.$ Finally, we get

$$


\begin{aligned}𝑀_{𝑌}(𝑡)=\frac{2𝑒^{2𝑡}}{2−3𝑡},\,𝑡<\frac{2}{3}.\end{aligned}


$$

### Sums of Independent Random Variables

If we know the moment-generating functions (MGFs) for independent random variables $X_1$ and $X_2,$ then we can easily find the MGF for their sum using the following theorem:

*If $Y = X_1 + X_2,$ where $X_1$ and $X_2$ are independent random variables with MGF's $M_{X_1}(t)$ and $M_{X_2}(t),$ respectively, then the MGF of $Y$ is*

Let's prove this when $X_1$ and $X_2$ are continuous (the proof is similar for discrete random variables). We start with the definition of the MGF:

$$


M_Y(t) = \textrm E \left[ e^{tY} \right] = \textrm E \left[ e^{t(X_1 + X_2)} \right]


$$

Now, if $X_1$ defined on $[a,b]$ and $X_2$ is defined on $[c,d],$ then by the definition of the expected value, we have

$$


\textrm E \left[ e^{t(X_1 + X_2)} \right] = \int_c^d \int_a^b f_{X_1,X_2} (x_1, x_2) e^{t(x_1 + x_2)} \, \textrm dx_1 \textrm dx_2,


$$

where $f_{X_1,X_2}(x_1,x_2)$ is the joint probability density function of $X_1$ and $X_2.$

Finally, since $X_1$ and $X_2$ are independent, we have

$$


f_{X_1,X_2}(x_1,x_2) = f_{X_1}(x_1) f_{X_2}(x_2),


$$

and therefore

$$


\begin{aligned}𝑀_{𝑌}(𝑡) & =∫_{𝑑𝑐}∫_{𝑏𝑎}𝑓_{𝑋_{1},𝑋_{2}}(𝑥_{1},𝑥_{2})𝑒^{𝑡(𝑥_{1}+𝑥_{2})}\,d𝑥_{1}d𝑥_{2} \\ & =∫_{𝑑𝑐}∫_{𝑏𝑎}𝑓_{𝑋_{1}}(𝑥_{1})𝑓_{𝑋_{2}}(𝑥_{2})𝑒^{𝑡(𝑥_{1}+𝑥_{2})}\,d𝑥_{1}d𝑥_{2} \\ & =∫_{𝑑𝑐}∫_{𝑏𝑎}𝑓_{𝑋_{1}}(𝑥_{1})𝑓_{𝑋_{2}}(𝑥_{2})𝑒^{𝑡𝑥_{1}}𝑒^{𝑡𝑥_{2}}\,d𝑥_{1}d𝑥_{2} \\ & =∫_{𝑏𝑎}𝑓_{𝑋_{1}}(𝑥_{1})𝑒^{𝑡𝑥_{1}}\,d𝑥_{1}⋅∫_{𝑑𝑐}𝑓_{𝑋_{2}}(𝑥_{2})𝑒^{𝑡𝑥_{2}}\,d𝑥_{2} \\ & =E[𝑒^{𝑡𝑋_{1}}]⋅E[𝑒^{𝑡𝑋_{2}}] \\ & =𝑀_{𝑋_{1}}(𝑡)𝑀_{𝑋_{2}}(𝑡).\end{aligned}


$$

### Example: Finding the MGF of a Sum of Random Variables

#### Question

You're given that if $X \sim \text{Po}(\lambda),$ the moment-generating function (MGF) of $X$ is

$$


M(t) = e^{\lambda(e^t-1)}, \qquad t\in\mathbb R.


$$

Let $Y = X_1 + X_2,$ where $X_1 \sim \text{Po}(4)$ and $X_2 \sim \text{Po}(7)$ are independent. What is the moment-generating function (MGF) of $Y$ for $t\in \mathbb{R}?$

#### Explanation

If $Y = X_1 + X_2,$ where $X_1$ and $X_2$ are independent random variables with MGF's $M_{X_1}(t)$ and $M_{X_2}(t),$ respectively, then the MGF of $Y$ is

$$


M_Y(t) = M_{X_1}(t) M_{X_2}(t).


$$

For a Poisson random variable $X_1 \sim \text{Po}(\lambda),$ we have

$$


M_{X_1}(t) = e^{\lambda(e^t-1)}.


$$

In our case, since $X_1 \sim \text{Po}(4),$ we have

$$


M_{X_1}(t) = e^{4(e^t-1)}.


$$

Then, since $X_2 \sim \text{Po}(7),$ we have

$$


M_{X_2}(t) = e^{7(e^t-1)}.


$$

Therefore, we have

$$


\begin{aligned}𝑀_{𝑌}(𝑡) & =𝑒^{4(𝑒^{𝑡}−1)}⋅𝑒^{7(𝑒^{𝑡}−1)} \\ & =𝑒^{11(𝑒^{𝑡}−1)}.\end{aligned}


$$

### Further Properties of Moment-Generating Functions

If we know the moment-generating functions (MGF's) for independent random variables $X_1$ and $X_2,$ then we can easily find the MGF for any linear combination of them using the following theorem:

*If $Y = aX_1 + bX_2,$ where $X_1$ and $X_2$ are independent random variables with MGF's $M_{X_1}(t)$ and $M_{X_2}(t),$ respectively, then the MGF of $Y$ is*

Note that this is just a consequence of using the two formulas we've already covered. Since $Y$ is a sum of independent random variables $aX_1$ and $bX_2,$ we have

$$


M_Y = M_{aX_1}(t) M_{bX_2} (t),


$$

and since $M_{aX}(t) = M_X(at)$ for any random variable $X,$ we have

$$


M_Y = M_{X_1}(at) M_{X_2} (bt).


$$

### Example: Finding the MGF of a Linear Combination of Random Variables

#### Question

You're given that if $X\sim\chi^2(k),$ the moment-generating function (MGF) of $X$ is

$$


M(t) = (1-2t)^{-k/2}, \qquad t < \dfrac12.


$$

Let $Y = 8X_1 - 2X_2,$ where $X_1 \sim \chi^2(4)$ and $X_2 \sim \chi^2(2)$ are independent. What is the moment-generating function (MGF) of $Y$ for $-\dfrac14 < t < \dfrac1{16}?$

#### Explanation

If $Y = a_1X_1 + a_2X_2,$ where $X_1$ and $X_2$ are independent random variables with MGF's $M_{X_1}(t)$ and $M_{X_2}(t),$ respectively, and $a_1$ and $a_2$ are constants, then the MGF of $Y$ is

$$


M_Y(t) = M_{X_1}(a_1t) M_{X_2}(a_2t).


$$

Here, we're given $Y = 8X_1 - 2X_2,$ so we have

$$


M_Y(t) = M_{X_1}(8t) M_{X_2}(-2t).


$$

If $X \sim \chi^2(k),$ then the MGF of $X$ is given by

$$


M_X(t) = (1-2t)^{-k/2}, \qquad t < \dfrac12.


$$

Since $X_1 \sim \chi^2(4),$ we have

$$


\begin{aligned}𝑀_{𝑋_{1}}(𝑡) & =(1−2𝑡)^{−2},\,𝑡<\frac{1}{2} \\ 𝑀_{𝑋_{1}}(8𝑡) & =\frac{1}{(1−16𝑡)^{2}},\,𝑡<\frac{1}{16}.\end{aligned}


$$

Likewise, since $X_2 \sim \chi^2(2),$ we have

$$


\begin{aligned}𝑀_{𝑋_{2}}(𝑡) & =(1−2𝑡)^{−1},\,𝑡<\frac{1}{2} \\ 𝑀_{𝑋_{2}}(−2𝑡) & =\frac{1}{(1+4𝑡)},\,𝑡>−\frac{1}{4}.\end{aligned}


$$

Therefore, for $-\dfrac14 < t < \dfrac1{16},$ we have

$$


\begin{aligned}𝑀_{𝑌}(𝑡) & =\frac{1}{(1−16𝑡)^{2}(1+4𝑡)}.\end{aligned}


$$

That is,

$$


M_Y(t) = \dfrac{1}{(1-16t)^{2}(1+4t)}, \quad-\dfrac14 < t < \dfrac1{16}.


$$
