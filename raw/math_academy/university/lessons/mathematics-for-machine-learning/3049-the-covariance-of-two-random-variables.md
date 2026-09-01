# The Covariance of Two Random Variables

Source: https://www.mathacademy.com/topics/3049?courseId=145
Topic ID: 3049

## Prerequisites

- [Variance of Continuous Random Variables](./2988-variance-of-continuous-random-variables.md)
- [The Rule of the Lazy Statistician for Two Random Variables](./3061-the-rule-of-the-lazy-statistician-for-two-random-variables.md)
- [Computing Expected Values From Joint Distributions](./3856-computing-expected-values-from-joint-distributions.md)
- [Independence of Continuous Random Variables](./3863-independence-of-continuous-random-variables.md)
- [Sums of Squares](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/5204-sums-of-squares.md)

## Lesson

### Introduction

We often want to measure the strength of the (linear) dependence between two random variables. One measure that we use for this purpose is covariance.

The **covariance** between two discrete random variables $X$ and $Y$ is defined as

$$


\text{Cov}[X, Y] = \text{E}\Big[\left(X - \text{E}[X]\right)\left(Y - \text{E}[Y]\right) \Big].


$$

Let's break this formula down a bit:

- $\left(X - \text{E}[X]\right)$ is the deviation of $X$ from its mean

- $\left(Y - \text{E}[Y]\right)$ is the deviation of $Y$ from its mean

Therefore, the covariance measures the expected value of the product of these deviations.

The covariance can also be expressed as

$$


\text{Cov}[X, Y] =\sum_{(x,y)\in S}(x − \textrm E[X])(y − \textrm E[Y])f(x,y)


$$

where $f(x,y)$ is the joint PMF of $X$ and $Y,$ and $S$ is the joint support.

Let's sketch a few diagrams to get a feel for what the covariance tells us.

- A *positive* covariance means that if $X$ increases, then $Y$ is likely to increase. We say that $X$ and $Y$ are **positively correlated**.

- A *negative* covariance means that if $X$ increases, then $Y$ is likely to decrease. We say that $X$ and $Y$ are **negatively correlated**.

Note the following:

- If $X$ and $Y$ are independent, then The reverse implication does not always hold! For example, two random variables can have zero covariance yet be dependent. This is because covariance measures *linear* dependence only.

- The covariance of a random variable with itself is its variance:

- Aside from indicating whether two random variables are positively or negatively correlated, the covariance *by itself* does not tell us very much. For example, if this does not necessarily mean that the dependence between $X_1$ and $Y_1$ is somehow "stronger" than the dependence between $X_2$ and $Y_2.$ This is because the covariance does not take the variance of the individual random variables into account. In a future lesson, we'll use the covariance to define the so-called **correlation coefficient,** which *does* consider the variance of the individual random variables and so *can* be used to compare the relative strength of the linear dependence between two pairs of random variables.

### Example: Stating the Covariance Using the Definition

#### Question

The joint probability mass function $f(x,y)$ for the discrete random variables $X$ and $Y$ with joint support $S=S_X\times S_Y$ is given below.

Find an expression for the covariance in sigma notation.

#### Explanation

The covariance of two discrete random variables $X$ and $Y$ with joint support $S$ is defined as

$$


\text{Cov}[X, Y] = \sum_{(x,y)\in S}(x − \textrm E[X])(y − \textrm E[Y])f(x,y).


$$

First, let's find the marginal mass functions for $X$ and $Y.$ These are given by the row and column totals, respectively.

We now compute $\text{E}[X]$ and $\text{E}[Y],$ as follows:

$$


\begin{aligned}E[𝑋] & =\underset{𝑥∈𝑆_{𝑋}}{∑}𝑥⋅𝑓_{𝑋}(𝑥) \\ & =1⋅0.4+4⋅0.6 \\ & =0.4+2.4 \\ & =2.8 \\ E[𝑌] & =\underset{𝑦∈𝑆_{𝑌}}{∑}𝑦⋅𝑓_{𝑌}(𝑦) \\ & =2⋅0.6+5⋅0.4 \\ & =1.2+2 \\ & =3.2\end{aligned}


$$

Applying the formula for the covariance, we have

$$


\begin{aligned}Cov[𝑋,𝑌] & =\underset{(𝑥,𝑦)∈𝑆}{∑}(𝑥−E[𝑋])(𝑦−E[𝑌])𝑓(𝑥,𝑦) \\ & =\underset{(𝑥,𝑦)∈𝑆}{∑}(𝑥−2.8)(𝑦−3.2)𝑓(𝑥,𝑦).\end{aligned}


$$

### Example: Calculating Covariance Using the Definition

#### Question

The joint probability mass function $f(x,y)$ for the discrete random variables $X$ and $Y$ is given below.

Calculate the covariance of $X$ and $Y.$

#### Explanation

The covariance of two discrete random variables $X$ and $Y$ with joint support $S$ is defined as

$$


\text{Cov}[X, Y] = \sum_{(x,y)\in S}(x − \textrm E[X])(y − \textrm E[Y])f(x,y).


$$

First, let's find the marginal mass functions for $X$ and $Y.$ These are given by the row and column totals, respectively.

We now compute $\text{E}[X]$ and $\text{E}[Y],$ as follows:

$$


\begin{aligned}E[𝑋] & =\underset{𝑥∈𝑆_{𝑋}}{∑}𝑥⋅𝑓_{𝑋}(𝑥) \\ & =1⋅0.6+2⋅0.4 \\ & =0.6+0.8 \\ & =1.4 \\ E[𝑌] & =\underset{𝑦∈𝑆_{𝑌}}{∑}𝑦⋅𝑓_{𝑌}(𝑦) \\ & =0⋅0.1+1⋅0.9 \\ & =0+0.9 \\ & =0.9\end{aligned}


$$

Applying the formula for the covariance, we have

$$


\begin{aligned}Cov[𝑋,𝑌] & =\underset{(𝑥,𝑦)∈𝑆}{∑}(𝑥−E[𝑋])(𝑦−E[𝑌])𝑓(𝑥,𝑦) \\ & =\underset{(𝑥,𝑦)∈𝑆}{∑}(𝑥−1.4)(𝑦−0.9)𝑓(𝑥,𝑦) \\ & =(1−1.4)(0−0.9)𝑓(1,0) \\ & =+(1−1.4)(1−0.9)𝑓(1,1) \\ & =+(2−1.4)(0−0.9)𝑓(2,0) \\ & =+(2−1.4)(1−0.9)𝑓(2,1) \\ & =(−0.4)(−0.9)(0.1) \\ & =+(−0.4)(0.1)(0.5) \\ & =+(0.6)(−0.9)(0) \\ & =+(0.6)(0.1)(0.4) \\ & =0.04.\end{aligned}


$$

### A Formula for Quickly Computing Covariance

You may have noticed that computing the covariance using the definition is quite a lot of work. Is there a formula that makes it easier?

Indeed, there is. It can be shown that

$$


\text{Cov}[X, Y] =\textrm E [XY] − \textrm E [X]\cdot \textrm E [Y].


$$

We'll prove this formula at the end of the lesson. But for now, let's get some practice at applying it.

### Example: Finding the Covariance Using the Shortcut Formula

#### Question

The joint probability mass function $f(x,y)$ for the discrete random variables $X$ and $Y$ is given below.

If $\text{E} [X]=2.8$ and $\text{E}[Y] = 2.4,$ calculate the covariance of $X$ and $Y.$

#### Explanation

The covariance of $X$ and $Y$ can be calculated using the formula

$$


\text{Cov}[X,Y] = \text{E} [XY] - \text{E}[X]\cdot \text{E}[Y].


$$

We use the rule of the lazy statistician to find $\text{E}[XY]\mathbin{:}$

$$


\begin{aligned}E[𝑋𝑌] & =\underset{(𝑥,𝑦)∈𝑆}{∑}𝑥𝑦⋅𝑓(𝑥,𝑦) \\ & =(1)(2)(0.2)+(1)(3)(0.2)+(4)(2)(0.4)+(4)(3)(0.2) \\ & =6.6\end{aligned}


$$

Then, using the covariance formula, we have

$$


\begin{aligned}Cov[𝑋,𝑌] & =E[𝑋𝑌]−E[𝑋]⋅E[𝑌] \\ & =6.6−(2.8)(2.4) \\ & =−0.12.\end{aligned}


$$

### Covariance for Continuous Random Variables

If $X$ and $Y$ are continuous random variables, the covariance between $X$ and $Y$ is given by

$$


\text{Cov}[X, Y] =\iint\limits_{\mathbb R^2}(x − \textrm E[X])(y − \textrm E[Y])f(x,y) \, \textrm d x\textrm d y.


$$

As is the case with discrete random variables, it's often easier to compute the covariance using the following formula:

$$


\text{Cov}[X,Y] = \text{E} [XY] - \text{E}[X]\cdot \text{E}[Y]


$$

Suppose we're given that the random variables $X$ and $Y$ have the joint probability density function

$$


\begin{aligned}\frac{1}{2}(𝑥+\frac{𝑦}{2}),\, & 0≤𝑥≤1,\,0≤𝑦≤2, \\ 0, & otherwise.\end{aligned}


$$

To compute the covariance of this distribution, we first use the rule of the lazy statistician to find $\text{E}[XY]\mathbin{:}$

$$


\begin{aligned}E[𝑋𝑌] & =∫_{20}∫_{10}𝑥𝑦𝑓(𝑥,𝑦)\,d𝑥\,d𝑦 \\ & =∫_{20}∫_{10}𝑥𝑦⋅\frac{1}{2}(𝑥+\frac{𝑦}{2})\,d𝑥\,d𝑦 \\ & =∫_{20}\frac{1}{2}𝑦∫_{10}(𝑥^{2}+\frac{1}{2}𝑥𝑦)\,d𝑥\,d𝑦 \\ & =∫_{20}\frac{1}{2}𝑦[\frac{1}{3}𝑥^{3}+\frac{1}{4}𝑥^{2}𝑦]_{𝑥=1𝑥=0}\,d𝑦 \\ & =∫_{20}\frac{1}{2}𝑦[\frac{1}{3}+\frac{1}{4}𝑦]\,d𝑦 \\ & =∫_{20}(\frac{1}{6}𝑦+\frac{1}{8}𝑦^{2})\,d𝑦 \\ & =[\frac{1}{12}𝑦^{2}+\frac{1}{24}𝑦^{3}]_{𝑦=2𝑦=0} \\ & =\frac{1}{12}⋅2^{2}+\frac{1}{24}⋅2^{3} \\ & =\frac{1}{3}+\frac{1}{3} \\ & =\frac{2}{3}.\end{aligned}


$$

Using methods discussed in previous lessons, we can compute $\text{E}[X]$ and $\text{E}[Y]{:}$

$$


\text{E}[X] = \dfrac{7}{12}, \qquad \text{E}[Y] = \dfrac76


$$

Finally, using the covariance formula, we get

$$


\begin{aligned}Cov[𝑋,𝑌] & =E[𝑋𝑌]−E[𝑋]⋅E[𝑌] \\ & =\frac{2}{3}−(\frac{7}{12})(\frac{7}{6}) \\ & =−\frac{1}{72}.\end{aligned}


$$

Remember that if two random variables are independent then their covariance equals zero. Let's see an example.

### Example: Finding the Covariance Given a Joint Probability Density Function

#### Question

The random variables $X$ and $Y$ have the joint probability density function

$$


\begin{aligned}\frac{3}{5}\sqrt{𝑥}\,𝑦, & 0≤𝑥≤1,\,2≤𝑦≤3, \\ 0, & otherwise.\end{aligned}


$$

Find the covariance of $X$ and $Y.$

#### Explanation

The joint support of $X$ and $Y$ is given by the rectangle

$$


S = [0,1] \times [2,3].


$$

Moreover, we can write

$$


f(x,y) = g(x) \cdot h(y),


$$

where $g(x) =\dfrac{3}{5} \sqrt{x}$ and $h(y) =y.$

Therefore, $X$ and $Y$ are independent, and consequently $\text{Cov}[X,Y] = 0.$

### Proof of the Covariance Formula

Let's now prove the following formula:

$$


\text{Cov}[X, Y] =\textrm E [XY] − \textrm E[X]\cdot \textrm E[Y]


$$

We start with the definition of covariance, given by

$$


\text{Cov}[X, Y] =\textrm E\Big[\left(X− \textrm E[X]\right)\left(Y−\textrm E[Y]\right)\Big].


$$

Expanding the product in the brackets, we get

$$


\begin{aligned}Cov[𝑋,𝑌]=E[𝑋𝑌−𝑋⋅E[𝑌]−E[𝑋]⋅𝑌+E[𝑋]⋅E[𝑌]].\end{aligned}


$$

Now, recall that if $a$ and $b$ are constants, then

$$


\textrm E[a]=a, \qquad \text{E}[aX + bY] = a\cdot \text{E}[X] + b \cdot \text{E}[Y].


$$

Since $\text{E}[X]$ and are $\text{E}[Y]$ are both constants, the covariance formula simplifies as follows:

$$


\begin{aligned}Cov[𝑋,𝑌] & =E[𝑋𝑌−𝑋⋅E[𝑌]−E[𝑋]⋅𝑌+E[𝑋]⋅E[𝑌]] \\ & =E[𝑋𝑌]−E[𝑋⋅E[𝑌]]−E[E[𝑋]⋅𝑌]+E[E[𝑋]⋅E[𝑌]] \\ & =E[𝑋𝑌]−E[𝑋]⋅E[𝑌]−E[𝑋]⋅E[𝑌]+E[𝑋]⋅E[𝑌] \\ & =E[𝑋𝑌]−E[𝑋]⋅E[𝑌]\end{aligned}


$$
