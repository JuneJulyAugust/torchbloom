# Variance of Sums of Random Variables

Source: https://www.mathacademy.com/topics/3940?courseId=73
Topic ID: 3940

## Prerequisites

- [The Covariance of Two Random Variables](./3049-the-covariance-of-two-random-variables.md)
- [Variance of Sums of Independent Random Variables](./3062-variance-of-sums-of-independent-random-variables.md)

## Lesson

### Introduction

Given two random variables $X$ and $Y,$ the variance of the sum or difference of these variables is given by

$$


\text{Var}[X\pm Y] = \text{Var}[X] + \text{Var}[Y] \pm 2\text{Cov}[X,Y],


$$

where $\text{Cov}[X,Y]$ is the covariance of $X$ and $Y.$ We'll prove this formula at the end of the lesson.

Note that if $X$ and $Y$ are independent, then $\text{Cov}[X,Y]= 0,$ and we have

$$


\text{Var}[X\pm Y] = \text{Var}[X] + \text{Var}[Y].


$$

### Example: Calculating the Variance of a Sum or Difference of Random Variables

#### Question

For two random variables $X$ and $Y,$ we have $\text{Var}[X] = 3,$ $\text{Var}[Y] = 0.24,$ and $\text{Cov}[X,Y] = 0.2.$ Determine $\text{Var}[X-Y].$

#### Explanation

Recall that if $X$ and $Y$ are random variables, then

$$


\text{Var}[X \pm Y] = \text{Var}[X] + \text{Var}[Y] \pm 2\text{Cov}[X,Y].


$$

Substituting the given data into the formula above, we obtain

$$


\text{Var}[X - Y] = 3 + 0.24 - 2 \cdot 0.2 = 2.84.


$$

### The Variance of a Sum of Scaled Random Variables

If $X$ and $Y$ are random variables and $a$ and $b$ are constants, then

$$


\text{Var}[aX + bY] = a^2 \text{Var}[X] + b^2 \text{Var}[Y] + 2ab \text{Cov}[X,Y].


$$

If $X$ and $Y$ are independent, then $\text{Cov}[X,Y] = 0,$ and we recover the formula

$$


\text{Var}[aX + bY] = a^2 \text{Var}[X] + b^2 \text{Var}[Y] .


$$

### Example: Calculating the Variance of a Sum of Scaled Random Variables

#### Question

For two random variables $X$ and $Y,$ we have $\text{Var}[X] = 5,$ $\text{Var}[Y] = 2,$ and $\text{Cov}[X,Y] = 3.$ Find $\text{Var}[2X - 5Y].$

#### Explanation

Recall that if $X$ and $Y$ are random variables, and $a$ and $b$ are constants, then

$$


\text{Var}[aX + bY] = a^2\text{Var}[X] + b^2\text{Var}[Y] + 2ab\,\text{Cov}[X,Y].


$$

Substituting the given data into the formula above, we obtain

$$


\begin{aligned}Var[2𝑋−5𝑌] & =2^{2}⋅5+(−5)^{2}⋅2+2⋅2⋅(−5)⋅3 \\ & =20+50−60 \\ & =10.\end{aligned}


$$

### Example: Calculating a Combined Variance Given Some Moments

#### Question

The joint probability mass function of the random variables $X$ and $Y$ is given below.

Find $\text{Var}[5X+2Y].$

#### Explanation

Recall that if $X$ and $Y$ are random variables and $a$ and $b$ are constants, then

$$


\text{Var}[aX+bY] = a^2 \text{Var}[X] + b^2 \text{Var}[Y] + 2ab\,\text{Cov}[X,Y].


$$

Also, the variance of a random variable $X$ is determined by the formula

$$


\text{Var}[X] = \text{E}[X^2] - \text{E}[X]^2,


$$

and the covariance of two random variables $X$ and $Y$ is given by the formula

$$


\text{Cov}[X,Y] = \text{E}[XY] - \text{E}[X] \cdot \text{E}[Y].


$$

First, let's find the marginal mass functions for $X$ and $Y.$ These are given by the row and column totals, respectively.

Now, we can find $\text{Var}[X].$ If $X$ is defined on a sample space $S_X,$ then

$$


\begin{aligned}E[𝑋] & =\underset{𝑥∈𝑆_{𝑋}}{∑}𝑥⋅𝑓_{𝑋}(𝑥) \\ & =0⋅0.4+3⋅0.6 \\ & =1.8\end{aligned}


$$

and

$$


\begin{aligned}E[𝑋^{2}] & =\underset{𝑥∈𝑆_{𝑋}}{∑}𝑥^{2}⋅𝑓_{𝑋}(𝑥) \\ & =0^{2}⋅0.4+3^{2}⋅0.6 \\ & =5.4.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =5.4−1.8^{2} \\ & =2.16.\end{aligned}


$$

Similarly, if $Y$ is defined on a sample space $S_Y,$ then

$$


\begin{aligned}E[𝑌] & =\underset{𝑦∈𝑆_{𝑦}}{∑}𝑦⋅𝑓_{𝑌}(𝑦) \\ & =0⋅0.5+2⋅0.5 \\ & =1\end{aligned}


$$

and

$$


\begin{aligned}E[𝑌^{2}] & =\underset{𝑦∈𝑆_{𝑦}}{∑}𝑦^{2}⋅𝑓_{𝑌}(𝑦) \\ & =0^{2}⋅0.5+2^{2}⋅0.5 \\ & =2.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑌] & =E[𝑌^{2}]−E[𝑌]^{2} \\ & =2−1^{2} \\ & =1.\end{aligned}


$$

Now, let's find $\text{Cov}[X,Y].$ We find $\text{E}[XY]$ using the rule of the lazy statistician:

$$


\begin{aligned}E[𝑋𝑌] & =\underset{(𝑥,𝑦)∈𝑆}{∑}𝑥𝑦⋅𝑓(𝑥,𝑦) \\ & =0⋅0⋅𝑓(0,0)+0⋅2⋅𝑓(0,2)+3⋅0⋅𝑓(3,0)+3⋅2⋅𝑓(3,2) \\ & =0+0+0+6⋅0.2 \\ & =1.2\end{aligned}


$$

Then, using the covariance formula, we have

$$


\begin{aligned}Cov[𝑋𝑌] & =E[𝑋𝑌]−E[𝑋]⋅E[𝑌] \\ & =1.2−1.8⋅1 \\ & =−0.6.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[5𝑋+2𝑌] & =5^{2}⋅2.16+2^{2}⋅1+2⋅5⋅2⋅(−0.6) \\ & =54+4−12 \\ & =46.\end{aligned}


$$

### Generalizing to Multiple Random Variables

Finally, we have the following generalization for the variance of a sum of $n$ random variables.

$$


\text{Var} \left[ \sum\limits_{i=1}^{n} a_i X_i \right] = \sum\limits_{i=1}^{n} a_i^2 \text{Var}[X_i] + 2\sum\limits_{i < j} a_i a_j \text{Cov}[X_i, X_j]


$$

Let's see an example of how this works in practice.

### Example: Calculating the Variance of a Sum of Three Random Variables

#### Question

For three random variables $X_1,X_2,$ and $X_3,$ we have the following variances and covariances:

$$


\text{Var}[X_1] = 1, \qquad \text{Var}[X_2] = 3, \qquad \text{Var}[X_3] = 8 \qquad


$$

$$


\text{Cov}[X_1,X_2] = 2, \qquad \text{Cov}[X_1,X_3] = 4, \qquad \text{Cov}[X_2,X_3] = -5 \qquad


$$

Find $\text{Var}[5X_1 + 2X_2 + 3X_3].$

#### Explanation

Recall that if $X_1, \ldots, X_n$ are random variables, and $a_1, \ldots, a_n$ are constants, then

$$


\text{Var}\left[\sum\limits_{i=1}^{n} a_i X_i \right] = \sum\limits_{i=1}^{n} a_i^2 \text{Var}[X_i] + 2\sum\limits_{i < j} a_i a_j \text{Cov}[X_i,X_j].


$$

Hence, for $n=3$ random variables, we have

$$


\begin{aligned}Var[𝑎_{1}𝑋_{1}+𝑎_{2}𝑋_{2}+𝑎_{3}𝑋_{3}] & =𝑎_{21}Var[𝑋_{1}]+𝑎_{22}Var[𝑋_{2}]+𝑎_{23}Var[𝑋_{3}] \\ & =+2𝑎_{1}𝑎_{2}Cov[𝑋_{1},𝑋_{2}]+2𝑎_{1}𝑎_{3}Cov[𝑋_{1},𝑋_{3}]+2𝑎_{2}𝑎_{3}Cov[𝑋_{2},𝑋_{3}].\end{aligned}


$$

Substituting the given data into the formula above, we obtain

$$


\begin{aligned}Var[5𝑋_{1}+2𝑋_{2}+3𝑋_{3}] & =5^{2}⋅1+2^{2}⋅3+3^{2}⋅8 \\ & =+2⋅5⋅2⋅2+2⋅5⋅3⋅4+2⋅2⋅3⋅(−5) \\ & =25+12+72+40+120−60 \\ & =209.\end{aligned}


$$

### Proof of the Sum Formula

Let's prove the following formula:

$$


\text{Var}[X+ Y] = \text{Var}[X] + \text{Var}[Y] + 2\text{Cov}[X,Y]


$$

Applying the definition of variance and using the linearity of expectation, we have

$$


\begin{aligned}Var[𝑋+𝑌] & =E[((𝑋+𝑌)−E[𝑋+𝑌])^{2}] \\ & =E[((𝑋−E[𝑋])+(𝑌−E[𝑌]))^{2}] \\ & =E[(𝑋−E[𝑋])^{2}+(𝑌−E[𝑌])^{2}+2(𝑋−E[𝑋])(𝑌−E[𝑌])].\end{aligned}


$$

Distributing the expected value, and using the fact that $\text{E}[aX] = a\cdot \text{E}[X]$ for constant $a,$ we have

$$


\begin{aligned}Var[𝑋+𝑌] & =E[(𝑋−E[𝑋])^{2}+(𝑌−E[𝑌])^{2}+2(𝑋−E[𝑋])(𝑌−E[𝑌])] \\ & =E[(𝑋−E[𝑋])^{2}]+E[(𝑌−E[𝑌])^{2}]+2⋅E[(𝑋−E[𝑋])(𝑌−E[𝑌])] \\ & =Var[𝑋]+Var[𝑌]+2Cov[𝑋,𝑌]\end{aligned}


$$

as required.

The proof for the difference between two random variables is similar.
