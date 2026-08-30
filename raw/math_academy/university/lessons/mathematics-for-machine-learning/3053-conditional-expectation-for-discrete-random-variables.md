# Conditional Expectation for Discrete Random Variables

Source: https://www.mathacademy.com/topics/3053?courseId=145
Topic ID: 3053

## Prerequisites

- [Expected Values of Discrete Random Variables](./730-expected-values-of-discrete-random-variables.md)
- [Conditional Distributions for Discrete Random Variables](./3003-conditional-distributions-for-discrete-random-variables.md)

## Lesson

### Introduction

For discrete random variables $X$ and $Y$, the **conditional expected value of $X$ given $Y=y$** is defined by

$$


\textrm E[X|Y=y]=\sum_{x}x f_{X|Y}(x|y)


$$

where $f_{X|Y}(x|y)$ is the conditional probability mass function of $X$ given $Y.$

This definition is similar to that of $\textrm{E}[X].$ However, we now use the conditional PMF $f_{X|Y}(x|y)$ instead of the marginal PMF $f_X(x)$ in the summation.

Note the following:

- The conditional expectation $\textrm E[X | Y = y]$ is (in general) a function of $y.$ This makes intuitive sense. If the distribution of $X$ varies with $Y,$ then the expected value of $X$ for a given $Y$ must vary with the value of $Y.$

- If $y$ is replaced with a number, then $\textrm E[X | Y = y]$ returns a single value.

- If $X$ and $Y$ are independent, then $\textrm E[X | Y = y] = \textrm E[X]$ for all $y$. Again, this makes intuitive sense. If the outcome of $Y$ has no influence on the outcome of $X,$ then the distribution of $X$ and, consequently, its mean, is also unaffected by $Y.$

- We sometimes use the notation $\mu_{X|y}$ to denote $E[X | Y = y].$

Finally, we have an analogous definition for $\textrm E[Y|X=x]\mathbin{:}$

$$


\textrm E[Y|X=x]=\sum_{y}y f_{Y|X}(y|x)


$$

### Example: Calculating a Conditional Expected Value Given a Conditional Mass Function

#### Question

Find the $\textrm{E}\big[Y \,|\, X=2\big]$ given that the conditional probability mass function $f_{Y|X}(y \,|\, 2)$ is shown in the table above.

#### Explanation

The conditional expected value of $Y$ given $X=x$ is defined by

$$


\textrm{E}\big[Y \,|\, X=x\big] = \sum_{y} y \, f_{Y | X}(y \,|\, x).


$$

Therefore, we obtain

$$


\begin{aligned}E[𝑌\,|\,𝑋=2] & =\underset{𝑦}{∑}𝑦\,𝑓_{𝑌|𝑋}(𝑦\,|\,2) \\ & =1⋅\frac{2}{3}+2⋅\frac{1}{3} \\ & =\frac{4}{3}.\end{aligned}


$$

### Example: Calculating a Conditional Expectation Using Row Totals

#### Question

Find $\textrm{E}\big[Y \,|\, X=2\big]$ given that the random variables $X$ and $Y$ have the joint probability mass function $f(x,y)$ shown in the table above.

#### Explanation

Recall that the conditional expected value of $Y$ given $X=x$ is defined by

$$


\textrm{E}\big[Y \,|\, X=x\big] = \sum_{y} y \, f_{Y | X}(y \,|\, x).


$$

In order to find $f_{Y | X}(y \,|\, x),$ let's first find the marginal distribution for $X,$ corresponding to the row totals:

The conditional probability mass function of $Y$ given that $X=x$ is

$$


f_{Y | X}(y \,|\, x) = \dfrac{f(x,y)}{f_X(x)}.


$$

Therefore, dividing each joint probability by the corresponding row total, we obtain the conditional probability mass function of $Y$ given that $X=x{:}$

Finally, we obtain

$$


\begin{aligned}E[𝑌\,|\,𝑋=2] & =\underset{𝑦}{∑}𝑦\,𝑓_{𝑌|𝑋}(𝑦\,|\,2) \\ & =1⋅\frac{8}{13}+2⋅\frac{5}{13} \\ & =\frac{18}{13}.\end{aligned}


$$

### Example: Calculating a Conditional Expectation Using Column Totals

#### Question

Find $\textrm{E}\big[X \,|\, Y=1\big]$ given that the random variables $X$ and $Y$ have the joint probability mass function $f(x,y)$ shown in the table above.

#### Explanation

Recall that the conditional expected value of $X$ given $Y=y$ is defined by

$$


\textrm{E}\big[X \,|\, Y=y\big] = \sum_{x} x \, f_{X | Y}(x \,|\, y).


$$

In order to find $f_{X | Y}(x \,|\, y),$ let's first find the marginal distribution for $Y,$ corresponding to the column totals:

The conditional probability mass function of $X$ given that $Y=y$ is

$$


f_{X | Y}(x \,|\, y) = \dfrac{f(x,y)}{f_Y(y)}.


$$

Therefore, dividing each joint probability by the corresponding column total, we obtain the conditional probability mass function of $X$ given that $Y=y{:}$

Finally, we obtain

$$


\begin{aligned}E[𝑋\,|\,𝑌=1] & =\underset{𝑥}{∑}𝑥\,𝑓_{𝑋|𝑌}(𝑥\,|\,1) \\ & =2⋅\frac{1}{5}+4⋅\frac{3}{5}+6⋅\frac{1}{5} \\ & =\frac{20}{5} \\ & =4.\end{aligned}


$$
