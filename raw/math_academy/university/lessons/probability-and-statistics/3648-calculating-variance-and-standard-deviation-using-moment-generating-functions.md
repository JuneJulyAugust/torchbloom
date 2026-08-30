# Calculating Variance and Standard Deviation Using Moment-Generating Functions

Source: https://www.mathacademy.com/topics/3648?courseId=73
Topic ID: 3648

## Prerequisites

- [Calculating Moments Using Moment-Generating Functions](./3287-calculating-moments-using-moment-generating-functions.md)

## Lesson

### Introduction

Suppose that $X$ is a random variable. We know that the variance of $X$ can be expressed in terms of the raw moments $\textrm E[X]$ and $\textrm E[X^2]$ as follows:

$$


\textrm{Var}[X] = \textrm{E}[X^2] - \textrm{E}[X]^2


$$

Let $M(t)$ be the moment-generating function of $X.$ Since

$$


\textrm E [X] = M'(0), \qquad \textrm E [X^2] = M''(0),


$$

we can express the variance of $X$ in terms of derivatives of the MGF evaluated at zero:

$$


\textrm{Var}[X] =M''(0) - [M'(0)]^2


$$

For example, let the random variable $X$ have the following probability distribution:

$$


\begin{aligned}\frac{2}{3}, & 𝑥=0 \\ \frac{1}{3}, & 𝑥=1\end{aligned}


$$

Then, the MGF is given by

$$


\begin{aligned}𝑀(𝑡) & =𝑓(0)𝑒^{0𝑡}+𝑓(1)𝑒^{𝑡} \\ & =\frac{2}{3}+\frac{1}{3}𝑒^{𝑡}.\end{aligned}


$$

Taking the first derivative and the second derivative of MGF, we get

$$


\begin{aligned}𝑀^{′}(𝑡) & =\frac{d}{d𝑥}(\frac{2}{3}+\frac{1}{3}𝑒^{𝑡}) \\ & =\frac{1}{3}𝑒^{𝑡}, \\ 𝑀^{″}(𝑡) & =\frac{d}{d𝑥}(𝑀^{′}(𝑡)) \\ & =\frac{d}{d𝑥}(\frac{1}{3}𝑒^{𝑡}) \\ & =\frac{1}{3}𝑒^{𝑡}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑋] & =𝑀^{″}(0)−(𝑀^{′}(0))^{2} \\ & =\frac{1}{3}−(\frac{1}{3})^{2} \\ & =\frac{1}{3}−\frac{1}{9} \\ & =\frac{2}{9}.\end{aligned}


$$

### Example: Computing Variance From a Moment-Generating Function

#### Question

Given that the moment-generating function (MGF) of the random variable $X$ is given by

$$


\% Note: This is an MGF for X~\chi^2(4) M(t) = \dfrac{1}{(1-2t)^2}, \quad t < \dfrac 12,


$$

compute $\textrm{Var}[X].$

#### Explanation

We use the following identity:

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =𝑀^{″}(0)−[𝑀^{′}(0)]^{2}\end{aligned}


$$

First, we express $M(t)$ in a form that is easy to differentiate:

$$


M(t) = (1-2t)^{-2}


$$

Computing derivatives of $M(t),$ we get

$$


\begin{aligned}𝑀^{′}(𝑡) & =\frac{4}{(1−2𝑡)^{3}} \\ 𝑀^{″}(𝑡) & =\frac{24}{(1−2𝑡)^{4}}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑀^{′}(0) & =4 \\ 𝑀^{″}(0) & =24.\end{aligned}


$$

Finally,

$$


\begin{aligned}Var[𝑋] & =𝑀^{″}(0)−[𝑀^{′}(0)]^{2} \\ & =24−4^{2} \\ & =8.\end{aligned}


$$

### Example: Computing Standard Deviation From a Moment-Generating Function

#### Question

Given that the moment-generating function of the random variable $X$ is given by

$$


\% Note: This is an MGF for X~Bernoulli (1/5) M(t) =\dfrac{4}{5} + \dfrac{1}{5} e^t ,


$$

compute $\textrm{SD}[X].$

#### Explanation

We use the following identity:

$$


\begin{aligned}SD[𝑋] & =\sqrt{√Var[𝑋]} \\ & =\sqrt{√E[𝑋^{2}]−E[𝑋]^{2}} \\ & =\sqrt{√𝑀^{″}(0)−[𝑀^{′}(0)]^{2}}\end{aligned}


$$

Computing derivatives of $M(t),$ we get

$$


\begin{aligned}𝑀^{′}(𝑡) & =\frac{1}{5}𝑒^{𝑡} \\ 𝑀^{″}(𝑡) & =\frac{1}{5}𝑒^{𝑡}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑀^{′}(0) & =\frac{1}{5} \\ 𝑀^{″}(0) & =\frac{1}{5}.\end{aligned}


$$

Finally,

$$


\begin{aligned}SD[𝑋] & =\sqrt{√𝑀^{″}(0)−[𝑀^{′}(0)]^{2}} \\ & =\sqrt{√\frac{1}{5}−(\frac{1}{5})^{2}} \\ & =\sqrt{√\frac{4}{25}} \\ & =\frac{2}{5}.\end{aligned}


$$
