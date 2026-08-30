# Computing Expected Values From Joint Distributions

Source: https://www.mathacademy.com/topics/3856?courseId=145
Topic ID: 3856

## Prerequisites

- [Expected Values of Sums and Products of Random Variables](./3292-expected-values-of-sums-and-products-of-random-variables.md)
- [Marginal Distributions for Continuous Random Variables](./3636-marginal-distributions-for-continuous-random-variables.md)
- [Expected Values of Continuous Random Variables](./4012-expected-values-of-continuous-random-variables.md)

## Lesson

### Introduction

To compute the expected value of a discrete random variable $X$ given a joint mass function $f(x,y),$ we must first find its marginal mass function $f_X.$ Once the marginal mass function is known, we can then compute $\textrm{E}[X]$ using the formula

$$


\textrm{E}[X] = \sum\limits_{i=1}^n x_i \, f_X(x_i).


$$

For example, consider the joint probability mass function $f(x,y)$ for the discrete random variables $X$ and $Y,$ shown below.

Recall that the marginal distribution for $X$ corresponds to the row totals, and the marginal distribution for $Y$ corresponds to the column totals. Since we're only interested in the expected value of $X,$ let's compute the row totals only.

Therefore, the marginal mass function of $X$ is as follows:

We can now compute the expected value of $X\mathbin{:}$

$$


\begin{aligned}E[𝑋] & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖}\,𝑓_{𝑋}(𝑥_{𝑖}) \\ & =1⋅0.2+2⋅0.8 \\ & =0.2+1.6 \\ & =1.8\end{aligned}


$$

Therefore, we conclude that $\textrm{E}[X] = 1.8.$

### Example: Finding the Expected Value of a Discrete Random Variable From a Joint Distribution

#### Question

Given the joint probability distribution for two discrete random variables $X$ and $Y$ below, find $\textrm{E}[4X-3Y].$

#### Explanation

Recall that the marginal distribution for $X$ corresponds to the row totals, and the marginal distribution for $Y$ corresponds to the column totals.

Therefore, the probability mass functions for $X$ and $Y$ are given by the following tables:

Now, we can compute the expected values for $X$ and $Y{:}$

$$


\begin{aligned}E[𝑋] & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖}\,𝑓_{𝑋}(𝑥_{𝑖}) \\ & =(−1)⋅0.35+2⋅0.35+4⋅0.3 \\ & =−0.35+0.7+1.2 \\ & =1.55\end{aligned}


$$

$$


\begin{aligned}E[𝑌] & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑦_{𝑖}\,𝑓_{𝑌}(𝑦_{𝑖}) \\ & =0⋅0.3+1⋅0.2+3⋅0.2+5⋅0.3 \\ & =0+0.2+0.6+1.5 \\ & =2.3\end{aligned}


$$

Finally, using the properties of expectation, we obtain

$$


\begin{aligned}E[4𝑋−3𝑌] & =4E[𝑋]−3\,E[𝑌] \\ & =4(1.55)−3(2.3) \\ & =6.2−6.9 \\ & =−0.7.\end{aligned}


$$

### Continuous Random Variables

To compute the expected value of a *continuous* random variable $X$ given a joint density function $f(x,y),$ we must first find its marginal density function $f_X.$ Once the marginal density function is known, we can then compute $\textrm{E}[X]$ using the formula

$$


\textrm{E}[X] = \int_{-\infty}^\infty x \cdot f_X(x)\,\textrm d x.


$$

Let's see an example.

### Example: Finding the Expected Value of a Continuous Random Variable From a Joint Distribution

#### Question

Let $X$ and $Y$ be two continuous random variables with the joint probability density function

$$


\begin{aligned}\frac{4}{𝑥^{3}𝑦^{3}}, & 𝑥≥1,\,𝑦≥1, \\ 0, & otherwise.\end{aligned}


$$

Find the expected value of $Y.$

#### Explanation

The marginal density function for $Y$ when $y \geq 1$ is

$$


\begin{aligned}𝑓_{𝑌}(𝑦) & =∫_{∞1}^{}\frac{4}{𝑥^{3}𝑦^{3}}\,d𝑥 \\ & =\frac{4}{𝑦^{3}}\underset{𝑏→∞}{lim}∫_{𝑏1}^{}\frac{1}{𝑥^{3}}\,d𝑥 \\ & =\frac{4}{𝑦^{3}}\underset{𝑏→∞}{lim}[−\frac{1}{2𝑥^{2}}]_{𝑏1}^{} \\ & =\frac{4}{𝑦^{3}}\underset{𝑏→∞}{lim}(\frac{1}{2}−\frac{1}{2𝑏^{2}}) \\ & =\frac{4}{𝑦^{3}}(\frac{1}{2}−0) \\ & =\frac{2}{𝑦^{3}}.\end{aligned}


$$

Therefore, the full expression for $f_Y(y)$ is given by

$$


\begin{aligned}\frac{2}{𝑦^{3}}, & 𝑦≥1, \\ 0, & otherwise.\end{aligned}


$$

Finally, the expected value of $Y$ is

$$


\begin{aligned}E[𝑌] & =∫_{∞−∞}^{}𝑦⋅𝑓_{𝑌}(𝑦)\,d𝑦 \\ & =∫_{∞1}^{}𝑦⋅\frac{2}{𝑦^{3}}\,d𝑦 \\ & =2\underset{𝑏→∞}{lim}∫_{𝑏1}^{}\frac{1}{𝑦^{2}}\,d𝑦 \\ & =2\underset{𝑏→∞}{lim}[−\frac{1}{𝑦}]_{𝑏1}^{} \\ & =2\underset{𝑏→∞}{lim}(1−\frac{1}{𝑏}) \\ & =2.\end{aligned}


$$
