# Mean and Variance of the Continuous Uniform Distribution

Source: https://www.mathacademy.com/topics/3277?courseId=73
Topic ID: 3277

## Prerequisites

- [The Continuous Uniform Distribution](./791-the-continuous-uniform-distribution.md)
- [Variance of Continuous Random Variables](./2988-variance-of-continuous-random-variables.md)

## Lesson

### Introduction

Recall that if the random variable $X$ is uniformly distributed over the interval $[a,b],$ then $X$ has the following probability density function:

$$


\begin{aligned}\frac{1}{𝑏−𝑎}, & \,𝑎≤𝑥≤𝑏 \\ \,0, & \,otherwise\end{aligned}


$$

It can be shown that the expected value and variance of $X$ are as follows:

$$


\begin{aligned}E[𝑋] & =\frac{𝑎+𝑏}{2} \\ Var[𝑋] & =\frac{(𝑏−𝑎)^{2}}{12}\end{aligned}


$$

The result for $\textrm{E}[X]$ is intuitive as it's simply the midpoint of the interval $[a,b].$

We will derive both of these results at the end of the lesson.

### Example: Computing the Expected Value of a Uniformly Distributed Random Variable

#### Question

Given that $X$ is a random variable such that $X\sim U[2,8],$ find $\textrm{E}[X].$

#### Explanation

If the random variable $X$ is distributed uniformly over the interval $[a,b],$ then

$$


\textrm{E}[X] = \dfrac{a+b}{2}.


$$

In our case, we have $a=2$ and $b=8.$ Therefore,

$$


\textrm{E}[X] = \dfrac{2+8}{2} =5.


$$

### Example: Computing the Variance of a Uniformly Distributed Random Variable

#### Question

Given that $X$ is a random variable such that $X\sim U[2,10],$ find $\textrm{Var}[X].$

#### Explanation

If the random variable $X$ is distributed uniformly over the interval $[a,b],$ then

$$


\textrm{Var}[X] = \dfrac{(b-a)^2}{12}.


$$

In our case, we have $a=2$ and $b=10.$ Therefore,

$$


\textrm{Var}[X] = \dfrac{(10-2)^2}{12} = \dfrac{64}{12} = \dfrac{16}{3}.


$$

### Example: Computing the Standard Deviation of a Uniformly Distributed Random Variable

#### Question

Given that $X$ is a random variable such that $X\sim U[-9,-3],$ find $\textrm{SD}[X].$ Round your answer to three decimal places.

#### Explanation

If the random variable $X$ is distributed uniformly over the interval $[a,b],$ then

$$


\textrm{Var}[X] = \dfrac{(b-a)^2}{12}.


$$

In our case, we have $a=-9$ and $b=-3.$ Therefore,

$$


\textrm{Var}[X] = \dfrac{(-3-(-9))^2}{12} = \dfrac{36}{12} = 3.


$$

Finally,

$$


\textrm{SD}[X] = \sqrt{3} \approx 1.732.


$$

### Deriving the Formula for the Mean

If $X\sim U[a,b],$ then $X$ has the following probability density function:

$$


\begin{aligned}\frac{1}{𝑏−𝑎}, & \,𝑎≤𝑥≤𝑏 \\ \,0, & \,otherwise\end{aligned}


$$

We can compute the formula for $\textrm E[X]$ using the usual definition:

$$


\begin{aligned}E[𝑋] & =∫_{𝑏𝑎}^{}𝑥𝑓(𝑥)\,d𝑥 \\ & =∫_{𝑏𝑎}^{}\frac{𝑥}{𝑏−𝑎}\,d𝑥 \\ & =\frac{1}{𝑏−𝑎}∫_{𝑏𝑎}^{}𝑥\,d𝑥 \\ & =\frac{1}{𝑏−𝑎}⋅\frac{1}{2}𝑥^{2}_{𝑏𝑎}^{} \\ & =\frac{1}{2(𝑏−𝑎)}⋅(𝑏^{2}−𝑎^{2}) \\ & =\frac{1}{2(𝑏−𝑎)}⋅(𝑏−𝑎)(𝑏+𝑎) \\ & =\frac{1}{2(𝑏−𝑎)}⋅(𝑏−𝑎)(𝑏+𝑎) \\ & =\frac{𝑎+𝑏}{2}\end{aligned}


$$

### Deriving the Formula for the Variance

If $X\sim U[a,b],$ then $X$ has the following probability density function:

$$


\begin{aligned}\frac{1}{𝑏−𝑎}, & \,𝑎≤𝑥≤𝑏 \\ \,0, & \,otherwise\end{aligned}


$$

To compute $\textrm{Var}[X],$ we use the relation

$$


\textrm{Var}[X] = \textrm{E}[X^2] - (\textrm{E}[X])^2.


$$

First, we compute $\textrm E[X^2]$ as follows:

$$


\begin{aligned}E[𝑋^{2}] & =∫_{𝑏𝑎}^{}𝑥^{2}𝑓(𝑥)\,d𝑥 \\ & =∫_{𝑏𝑎}^{}\frac{𝑥^{2}}{𝑏−𝑎}\,d𝑥 \\ & =\frac{1}{𝑏−𝑎}∫_{𝑏𝑎}^{}𝑥^{2}\,d𝑥 \\ & =\frac{1}{𝑏−𝑎}⋅\frac{1}{3}𝑥^{3}_{𝑏𝑎}^{} \\ & =\frac{1}{3(𝑏−𝑎)}⋅(𝑏^{3}−𝑎^{3}) \\ & =\frac{1}{3(𝑏−𝑎)}⋅(𝑏−𝑎)(𝑏^{2}+𝑎𝑏+𝑎^{2}) \\ & =\frac{1}{3(𝑏−𝑎)}⋅(𝑏−𝑎)(𝑏^{2}+𝑎𝑏+𝑎^{2}) \\ & =\frac{1}{3}(𝑏^{2}+𝑎𝑏+𝑎^{2})\end{aligned}


$$

Now, since $\textrm E[X] = \dfrac12(b+a),$ we have

$$


(\textrm E[X])^2 = \dfrac14(b^2+2ab+a^2).


$$

Therefore,

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−(E[𝑋])^{2} \\ & =\frac{1}{3}(𝑏^{2}+𝑎𝑏+𝑎^{2})−\frac{1}{4}(𝑏^{2}+2𝑎𝑏+𝑎^{2}) \\ & =\frac{4}{12}(𝑏^{2}+𝑎𝑏+𝑎^{2})−\frac{3}{12}(𝑏^{2}+2𝑎𝑏+𝑎^{2}) \\ & =\frac{1}{12}(4𝑏^{2}+4𝑎𝑏+4𝑎^{2})−\frac{1}{12}(3𝑏^{2}+6𝑎𝑏+3𝑎^{2}) \\ & =\frac{1}{12}(𝑏^{2}−2𝑎𝑏+𝑎^{2}) \\ & =\frac{1}{12}(𝑏−𝑎)^{2}.\end{aligned}


$$
