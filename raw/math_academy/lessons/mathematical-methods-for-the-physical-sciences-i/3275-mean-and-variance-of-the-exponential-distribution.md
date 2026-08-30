# Mean and Variance of the Exponential Distribution

Source: https://www.mathacademy.com/topics/3275?courseId=154
Topic ID: 3275

## Prerequisites

- [Introduction to Integration by Parts](../ap-calculus-bc/317-introduction-to-integration-by-parts.md)
- [Variance of Continuous Random Variables](./2988-variance-of-continuous-random-variables.md)
- [Modeling With the Exponential Distribution](./3353-modeling-with-the-exponential-distribution.md)

## Lesson

### Introduction

Suppose that $X$ is an exponential random variable with rate parameter $\lambda > 0.$

$$


X\sim \textrm{Exp}(\lambda)


$$

The mean (expected value) of $X$ is given by

$$


\textrm E[X] = \dfrac{1}{\lambda}.


$$

To prove this, first recall that the PDF of $X$ is given by

$$


\begin{aligned}𝜆𝑒^{−𝜆𝑥},\, & 𝑥≥0, \\ 0, & otherwise.\end{aligned}


$$

By definition,

$$


\textrm E[X] = \int_{-\infty}^\infty x f(x)\,\textrm d x,


$$

and since $f(x) = 0$ for $x < 0,$ we have

$$


\textrm E[X] = \int_{0}^\infty \lambda xe^{-\lambda x}\,\textrm d x.


$$

We can evaluate this integral using integration by parts. First, we set

$$


u = x, \qquad v' = \lambda e^{-\lambda x},


$$

which gives

$$


u' = 1 \qquad v = -e^{-\lambda x}.


$$

Finally, applying the by-parts formula, we get

$$


\begin{aligned}E[𝑋] & =∫_{∞0}^{}𝜆𝑥𝑒^{−𝜆𝑥}\,d𝑥 \\ & =[−𝑥𝑒^{−𝜆𝑥}]_{∞0}^{}+∫_{∞0}^{}𝑒^{−𝜆𝑥}\,d𝑥 \\ & =[−𝑥𝑒^{−𝜆𝑥}]_{∞0}^{}−[\frac{𝑒^{−𝜆𝑥}}{𝜆}]_{∞0}^{} \\ & =\frac{1}{𝜆}.\end{aligned}


$$

### Example: The Mean of an Exponential Distribution

#### Question

Given that $X\sim \textrm{Exp}\left(\dfrac{\sqrt 3}{3}\right),$ what is $\textrm{E}[X]?$

#### Explanation

If $X \sim \textrm{Exp}({\lambda})$ is an exponential random variable, then

$$


\textrm E[X] = \dfrac{1}{\lambda}.


$$

Therefore, for our random variable $X \sim \textrm{Exp}\left(\dfrac{\sqrt 3}{3}\right),$ we have the following expected value:

$$


\textrm E[X] =\dfrac{1}{\left(\dfrac{\sqrt 3}{3}\right)}=\sqrt 3


$$

### Example: Modeling With the Mean of an Exponential Distribution

#### Question

The time $X,$ in hours, between two customers ordering a chocolate muffin at a pastry shop can be modeled as an exponential random variable $X\sim \textrm{Exp}(6).$ If a customer has just ordered a chocolate muffin, what is the average time, in minutes, until the next customer orders a chocolate muffin?

#### Explanation

Recall that if $X \sim \textrm{Exp}({\lambda})$ is an exponential random variable, then

$$


\textrm{E}[X] = \dfrac{1}{\lambda}.


$$

We're given that $X \sim \textrm{Exp}\left(6\right).$ Therefore, $\lambda = 6,$ which means that $6$ customers order a chocolate muffin each hour. Hence,

$$


\textrm E[X] =\dfrac{1}{6}\, \textrm{h} = 10 \, \textrm{min}.


$$

Therefore, the average time until the next customer orders a chocolate muffin is $10$ minutes.

### Proof of the Variance Formula

If the random variable $X\sim \textrm{Exp}(\lambda),$ then the variance of $X$ is given by

$$


\textrm {Var}[X] = \dfrac{1}{\lambda^2}.


$$

To prove this, we first recall that

$$


\textrm{Var}[X] = \textrm E[X^2] - \left(\textrm E[X]\right)^2.


$$

As we saw previously,

$$


\textrm E[X] = \int_0^\infty \lambda xe^{-\lambda x}\textrm d x = \dfrac1\lambda,


$$

and therefore,

$$


\left(\textrm E[X]\right)^2 = \dfrac{1}{\lambda^2}.


$$

Now, we calculate $\textrm E[X^2].$ First, note that

$$


\textrm E[X^2] = \int_0^\infty \lambda x^2e^{-\lambda x}\textrm d x.


$$

We can evaluate this integral using integration by-parts. First, we set

$$


u = x^2, \qquad v' =\lambda e^{-\lambda x},


$$

and therefore

$$


u' = 2x, \qquad v = -e^{-\lambda x}.


$$

Applying the by-parts formula, we get

$$


\begin{aligned}E[𝑋^{2}] & =∫_{∞0}^{}𝜆𝑥^{2}𝑒^{−𝜆𝑥}\,d𝑥 \\ & =[−𝑥^{2}𝑒^{−𝜆𝑥}]_{∞0}^{}+2∫_{∞0}^{}𝑥𝑒^{−𝜆𝑥} \\ & =0+2∫_{∞0}^{}𝑥𝑒^{−𝜆𝑥} \\ & =2∫_{∞0}^{}𝑥𝑒^{−𝜆𝑥}.\end{aligned}


$$

Notice that we can express this integral in terms of $\textrm E[X]$ (and therefore $\lambda$) as follows:

$$


\begin{aligned}E[𝑋^{2}] & =2∫_{∞0}^{}𝑥𝑒^{−𝜆𝑥} \\ & =\frac{2}{𝜆}∫_{∞0}^{}𝜆𝑥𝑒^{−𝜆𝑥} \\ & =\frac{2}{𝜆}⋅E[𝑋] \\ & =\frac{2}{𝜆}⋅\frac{1}{𝜆} \\ & =\frac{2}{𝜆^{2}}\end{aligned}


$$

Finally, we have

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =\frac{2}{𝜆^{2}}−\frac{1}{𝜆^{2}} \\ & =\frac{1}{𝜆^{2}}\end{aligned}


$$

as required.

### Example: The Variance of a Exponential Distribution

#### Question

Given that $X\sim \textrm{Exp}\left(0.1\right),$ what is $\textrm{SD}[X]?$

#### Explanation

If $X \sim \textrm{Exp}(\lambda)$ is an exponential random variable, then

$$


\textrm{SD}[X] = \sqrt{\textrm{Var}[X]} = \dfrac{1}{\lambda}.


$$

Therefore, for our random variable $X \sim \textrm{Exp}\left(0.1\right),$ we have the following standard deviation:

$$


\begin{aligned}SD[𝑋] & =\frac{1}{(0.1)} \\ & =10\end{aligned}


$$
