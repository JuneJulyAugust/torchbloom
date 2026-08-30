# Mean and Variance of the Poisson Distribution

Source: https://www.mathacademy.com/topics/2991?courseId=109
Topic ID: 2991

## Prerequisites

- [Variance of Discrete Random Variables](./1388-variance-of-discrete-random-variables.md)
- [Modeling With the Poisson Distribution](./2838-modeling-with-the-poisson-distribution.md)

## Lesson

### Introduction

Suppose that the random variable $X$ has a Poisson distribution with a rate parameter $\lambda{:}$

$$



X \sim \textrm{Po}(\lambda)



$$

The expected value and variance of a Poisson random variable $X$ both equal ${\color{blue}\lambda}$.

$$



\textrm E[X] =\textrm{Var}[X] = {\color{blue}\lambda}.



$$

We'll justify the formula for the mean at the end of the lesson.

For example, if $X \sim \textrm{Po}({\color{blue}5}),$ then

$$



\textrm E[X] = \textrm{Var}[X]={\color{blue}5}.



$$

### Example: The Mean of a Poisson Random Variable

#### Question

The number of patients a cardiologist sees weekly can be modeled using a Poisson distribution with parameter $\lambda = 30.$ On average, how many patients does the cardiologist see each year, assuming there are $52$ weeks in a year?

#### Explanation

If $X \sim \textrm{Po}({\lambda})$ is a Poisson random variable, then

$$



\textrm E[X] = \lambda.



$$

We are told that the number of patients $X$ seen weekly can be modeled as a Poisson random variable $X \sim \textrm{Po}(30).$ Therefore,

$$



\textrm{E}[ X ] = \lambda = 30.



$$

Finally, the expected number of patients seen annually by the cardiologist equals $30 \cdot 52 = 1560.$

### Example: The Variance and Standard Deviation of a Poisson Random Variable

#### Question

Given that $X \sim \textrm{Po}\left(\dfrac{20}{9}\right)\!,$ what is $\textrm{SD}[X]?$

#### Explanation

If $X\sim \textrm{Po}\left(\lambda\right)$ is a Poisson random variable, then

$$



\textrm{SD}[X] = \sqrt{\textrm{Var}[X]} = \sqrt{\lambda}.



$$

Therefore, for our random variable $X\sim \textrm{Po}\left(\dfrac{20}{9}\right)\!,$ we have the following standard deviation:

$$



\begin{aligned}SD[𝑋] & =\sqrt{√Var[𝑋]} \\ & =\sqrt{√\frac{20}{9}} \\ & =\frac{\sqrt{√20}}{\sqrt{√9}} \\ & =\frac{2\sqrt{√5}}{3}\end{aligned}



$$

### Justification for the Mean

Throughout this lesson, we've used the fact that if $X\sim \textrm{Po}(\lambda),$ then

$$



\textrm{E}[X] = \lambda.



$$

Let's now justify this rule.

First, recall that if $X\sim \textrm{Po}(\lambda),$ then the PMF of $X$ is given by

$$



\begin{aligned}\frac{𝑒^{−𝜆}𝜆^{𝑥}}{𝑥!}, & 𝑥=0,1,2,3…, \\ 0, & otherwise.\end{aligned}



$$

By definition, we have

$$



\textrm E[X] = \sum_{x\in \{0,1,2\ldots\}} x \cdot f(x).



$$

Therefore,

$$



\begin{aligned}E[𝑋] & =0⋅\frac{𝑒^{−𝜆}𝜆^{0}}{0!}+1⋅\frac{𝑒^{−𝜆}𝜆^{1}}{1!}+2⋅\frac{𝑒^{−𝜆}𝜆^{2}}{2!}+3⋅\frac{𝑒^{−𝜆}𝜆^{3}}{3!}+⋯ \\ & =𝑒^{−𝜆}(0⋅\frac{𝜆^{0}}{0!}+1⋅\frac{𝜆^{1}}{1!}+2⋅\frac{𝜆^{2}}{2!}+3⋅\frac{𝜆^{3}}{3!}+⋯) \\ & =𝑒^{−𝜆}(𝜆+𝜆^{2}+\frac{𝜆^{3}}{2!}+⋯) \\ & =𝜆𝑒^{−𝜆}(1+𝜆+\frac{𝜆^{2}}{2!}+⋯).\end{aligned}



$$

Now, it can be shown that

$$



e^{\lambda} = 1+\lambda + \dfrac{\lambda^2}{2!} + \dfrac{\lambda^3}{3!} +\cdots.



$$

(You will learn this when you study Maclaurin series in Calculus). Therefore,

$$



\begin{aligned}E[𝑋] & =𝜆𝑒^{−𝜆}(1+𝜆+\frac{𝜆^{2}}{2!}+⋯) \\ & =𝜆𝑒^{−𝜆}⋅𝑒^{𝜆} \\ & =𝜆\end{aligned}



$$

as required.

A similar approach could be used to prove the formula for the variance. However, the calculation is more involved, so we omit the details here.
