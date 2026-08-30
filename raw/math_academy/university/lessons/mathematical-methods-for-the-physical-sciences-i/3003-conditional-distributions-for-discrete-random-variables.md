# Conditional Distributions for Discrete Random Variables

Source: https://www.mathacademy.com/topics/3003?courseId=154
Topic ID: 3003

## Prerequisites

- [Independence of Discrete Random Variables](./3048-independence-of-discrete-random-variables.md)

## Lesson

### Introduction

Let's recall the multiplication law for conditional probability for two events $A$ and $B\mathbin{:}$

$$


P(A|B) = \dfrac{P(A\cap B)}{P(B)}


$$

Now suppose that $X$ and $Y$ are discrete random variables. The conditional probability that $X=x$ *given that* $Y = y$ follows immediately from the multiplication law and is given by

$$


P(X = x \,|\, Y = y) = \dfrac{P(X =x, \, Y = y)}{P(Y = y)} = \dfrac{f(x,y)}{f_Y(y)},


$$

where $f(x,y)$ is the joint PMF of $X$ and $Y,$ and $f_Y(y)$ is the marginal mass function of $Y.$

Note the following:

- To avoid getting a zero in the denominator, this formula assumes that $P(Y = y) = f_Y(y) \neq 0.$

- In the case where $P(Y=y) = 0,$ the corresponding conditional probability for $X$ does not exist. It makes no sense to ask about the event of $X=x$ occurring *given that* $Y=y$ has occurred if the event $Y=y$ is impossible!

In the similar manner, the conditional probability that $Y=y$ given that $X = x$ can be calculated as

$$


P(Y = y \,|\, X = x) = \dfrac{P(X = x, \, Y = y)}{P(X = x)} = \dfrac{f(x,y)}{f_X(x)},


$$

where $f_X(x)$ is the marginal mass function of $X.$ This formula assumes that $P(X=x)\neq 0.$

### Example: Computing a Conditional Probability

#### Question

Compute $P(Y=0 \,|\, X=1)$ given that the discrete random variables $X$ and $Y$ have the joint probability mass function $f(x,y)$ shown in the table above.

#### Explanation

By the multiplication law for conditional probability, the required probability is given by

$$


P(Y = 0 \,|\, X = 1) = \dfrac{P(X = 1 , Y = 0)}{P(X = 1)} = \dfrac{f(1,0)}{f_X(1)},


$$

where $f(x,y)$ is the joint probability mass function of $X$ and $Y,$ and $f_X(x)$ is the marginal distribution of $X.$

Recall that the marginal distribution for $X$ corresponds to the row totals. Thus,

$$


\begin{aligned}𝑓_{𝑋}(1) & =𝑓(1,0)+𝑓(1,1) \\ & =0.15+0.3 \\ & =0.45.\end{aligned}


$$

From the given table, we have that $f(1,0) = 0.15.$

Finally, substituting $f_X(1) = 0.45$ and $f(1,0) = 0.15$ in our formula above, we obtain

$$


\begin{aligned}𝑃(𝑌=0\,|\,𝑋=1) & =\frac{𝑓(1,0)}{𝑓_{𝑋}(1)} \\ & =\frac{0.15}{0.45} \\ & =\frac{1}{3}.\end{aligned}


$$

### Example: Computing a Conditional Probability Over an Interval

#### Question

Compute $P(0\lt Y \lt 3\,|\, X=0)$ given that the discrete random variables $X$ and $Y$ have the joint probability mass function $f(x,y)$ shown in the table above. Round your answer to two decimal places.

#### Explanation

By the multiplication law for conditional probability, the required conditional probability is given by

$$


\begin{aligned}𝑃(0<𝑌<3\,|\,𝑋=0) & =\frac{𝑃((0<𝑌<3),𝑋=0)}{𝑃(𝑋=0)} \\ & =\frac{𝑃(𝑋=0,(0<𝑌<3))}{𝑃(𝑋=0)} \\ & =\frac{𝑃(𝑋=0,𝑌=1)+𝑃(𝑋=0,𝑌=2)}{𝑃(𝑋=0)} \\ & =\frac{𝑓(0,1)+𝑓(0,2)}{𝑓_{𝑋}(0)},\end{aligned}


$$

where $f(x,y)$ is the joint probability mass function of $X$ and $Y,$ and $f_X(x)$ is the marginal distribution of $X.$

Recall that the marginal distribution for $X$ corresponds to the row totals. Thus,

$$


\begin{aligned}𝑓_{𝑋}(0) & =𝑓(0,0)+𝑓(0,1)+𝑓(0,2)+𝑓(0,3) \\ & =0.2+0+0.05+0.1 \\ & =0.35.\end{aligned}


$$

From the given table, we have that $f(0,1)=0$ and $f(0,2)=0.05.$

Finally, substituting our values into the formula above, we obtain

$$


\begin{aligned}𝑃(0<𝑌<3\,|\,𝑋=0) & =\frac{𝑓(0,1)+𝑓(0,2)}{𝑓_{𝑋}(0)} \\ & =\frac{0+0.05}{0.35} \\ & =\frac{0.05}{0.35} \\ & ≈0.14.\end{aligned}


$$

### Conditional Probability Mass Functions

We can now define two more probability mass functions as follows:

- The **conditional probability mass function of $X$ given that $Y=y$,** denoted $f_{X|Y}(x|y),$ is defined as where $f(x,y)$ is the joint probability mass function of $X$ and $Y,$ and $f_Y(y)$ is the marginal mass function of $Y.$

- The **conditional probability mass function of $Y$ given that $X=x,$** denoted $f_{Y|X}(y|x),$ is defined as where $f(x,y)$ is a joint probability mass function of $X$ and $Y,$ and $f_X(x)$ is the marginal mass function of $X.$

**Watch out!** The conditional distribution of $X$ given $Y$ does *not* equal the conditional distribution of $Y$ given $X$. That is, in general,

$$


f_{X|Y}(x|y) \ne f_{Y|X}(y|x).


$$

Finally, if $X$ and $Y$ are independent, then

$$


f_{X|Y}(x|y)=f_X(x),\qquad f_{Y|X}(y|x)=f_Y(y).


$$

In other words, if $X$ and $Y$ are independent, then knowing the value of one random variable does not affect the probability distribution of the other.

### Example: Computing the Value of a Conditional Probability Mass Function at a Point

#### Question

Compute $f_{X|Y}(2 \,|\, 2)$ given that the discrete random variables $X$ and $Y$ have the joint probability mass function $f(x,y)$ shown in the table above.

#### Explanation

The conditional probability mass function $f_{X|Y}(x\,|\,y)$ is defined as

$$


f_{X|Y}(x\,|\,y) = P(X = x \,|\, Y=y).


$$

Therefore, we're required to compute the conditional probability

$$


f_{X|Y}(2 \,|\, 2) = P(X = 2 \,|\, Y = 2).


$$

By the multiplication law for conditional probability, we have

$$


P(X = 2 \,|\, Y = 2) = \dfrac{P(X = 2, Y = 2)}{P(Y = 2)} = \dfrac{f(2,2)}{f_Y(2)}


$$

where $f(x,y)$ is the joint probability mass function of $X$ and $Y,$ and $f_Y(y)$ is the marginal distribution of $Y.$

Recall that the marginal distribution for $Y$ corresponds to the column totals. Thus,

$$


\begin{aligned}𝑓_{𝑌}(2) & =𝑓(1,2)+𝑓(2,2)+𝑓(3,2) \\ & =\frac{1}{6}+\frac{1}{6}+\frac{1}{18} \\ & =\frac{7}{18}.\end{aligned}


$$

From the given table, $f(2,2) = \dfrac{1}{6}.$

Finally, substituting $f_Y(2) = \dfrac{7}{18}$ and $f(2,2) = \dfrac{1}{6}$ in our formula above, we obtain

$$


\begin{aligned}𝑓_{𝑋|𝑌}(2\,|\,2) & =𝑃(𝑋=2\,|\,𝑌=2) \\ & =\frac{𝑓(2,2)}{𝑓_{𝑌}(2)} \\ & =\frac{(\frac{1}{6})}{6} \\ & =\frac{3}{7}.\end{aligned}


$$

### Example: Computing a Conditional Probability Mass Function

#### Question

Find the conditional probability mass function given that the random variables and have the joint probability mass function shown in the table above.

#### Explanation

The conditional probability mass function is defined as

Therefore, we're required to compute the following set of conditional probabilities:

By the multiplication law for conditional probability, we have

where is the joint probability mass function of and and is the marginal distribution of

Recall that the marginal distributions for and correspond to the row and column totals, respectively. So, let's compute these:

Therefore, for we obtain the following:

Finally, the conditional probability mass function can be represented by the following table:
