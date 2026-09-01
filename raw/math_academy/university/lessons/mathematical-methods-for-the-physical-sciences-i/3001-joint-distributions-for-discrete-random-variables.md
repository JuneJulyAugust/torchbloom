# Joint Distributions for Discrete Random Variables

Source: https://www.mathacademy.com/topics/3001?courseId=154
Topic ID: 3001

## Prerequisites

- [The Cartesian Product](./49-the-cartesian-product.md)
- [Probability Mass Functions of Discrete Random Variables](../discrete-mathematics/1290-probability-mass-functions-of-discrete-random-variables.md)

## Lesson

### Introduction

We often want to know if there is a relationship between two random variables. For this reason, we wish to formulate the idea of a joint probability distribution.

To introduce this concept, suppose the random variable $X$ represents the number of heads obtained when a fair coin is flipped. The support of $X,$ denoted $S_X,$ consists of all possible values of $X$ and in this case is given by

$$


S_X = \{0,1\}.


$$

Now suppose that the random variable $Y$ represents the result of rolling a fair tetrahedral die. Then the support of $Y,$ denoted $S_Y,$ is

$$


S_Y = \{1,2,3,4\}.


$$

The **joint support** of $X$ and $Y,$ denoted $S,$ consists of all possible pairs $(x,y)$ such that $x$ is a possible outcome for $X$ and $y$ is a possible outcome for $Y\mathbin{:}$

$$


\begin{aligned}(0,1), & (0,2), & (0,3), & (0,4) \\ (1,1), & (1,2), & (1,3), & (1,4)\end{aligned}


$$

Note that $S_X\times S_Y$ is the cartesian product of $S_X$ and $S_Y.$

Let's assume that the flipping of the coin and rolling of the die are independent. Then, for any $x \in X$ and any $y \in Y,$ we have that

$$


P(X=x\:\text{and}\:Y=y) = \dfrac{1}{2} \cdot \dfrac{1}{4} = \dfrac{1}{8}.


$$

The **joint probability mass function** of $X$ and $Y,$ denoted $f(x,y),$ can be represented by the following table:

Similar to the case of single random variables, we have

$$


f(x,y) = P(X=x\:\text{ and }\:Y=y).


$$

Going forward, we will use the shorthand notation $P(X=x, Y=y)$ to mean $P(X=x\:\text{and}\:Y=y).$

### Bivariate and Multivariate Distributions

Let $X$ and $Y$ be discrete random variables with supports $S_X$ and $S_Y$, respectively. For a function

$$


f(x,y)=P(X=x, Y=y)


$$

to be a valid joint probability mass function with joint support $S=S_X\times S_Y,$ it must satisfy the following conditions:

- $0 \leq f(x,y) \leq 1$ for all $(x,y) \in S$

- $\displaystyle\sum\limits_{(x,y) \in S} f(x,y)= 1$

- $P\left((X,Y) \in A \right) = \displaystyle \sum\limits_{(x,y) \in A} f(x,y),$ where $A$ is a subset of $S.$

There is some nice intuition to these conditions.

- The condition $0 \leq f(x,y) \leq 1$ for all $(x,y)\in S$ states that any possible outcome for $(X,Y)$ must have a probability between $0$ and $1.$

- The condition $\displaystyle \sum\limits_{(x,y) \in S} f(x,y) = 1$ states that the sum of all the probabilities over all possible values of $X$ and $Y$ must add up to $1.$

- The third condition states that we compute the probability of an event $A$ by adding up the probabilities associated with $A.$

The joint probability mass function of a discrete random variable with finite support can be represented using a table, as shown below.

In the case of two random variables, the joint distribution is sometimes called a **bivariate distribution**. However, the concept generalizes to any number of random variables, giving a **multivariate distribution**.

### Example: Finding the Joint Distribution of Two Discrete Random Variables

#### Question

The joint probability mass function $f(x,y)$ for the discrete random variables $X$ and $Y$ is given above. Find the value of $a.$

#### Explanation

The support of $X$ is $S_X = \{0,1\},$ the support of $Y$ is $S_Y = \{0,1\},$ and therefore the joint support $S$ is

$$


S= S_X\times S_Y = \left\{(0,0), (0,1), (1,0), (1,1) \right\}.


$$

Since we're given a joint probability distribution $f(x,y),$ we must have

$$


\displaystyle \sum\limits_{(x,y) \in S} f(x,y) = 1.


$$

Therefore,

$$


\begin{aligned}𝑓(0,0)+𝑓(0,1)+𝑓(1,0)+𝑓(1,1) & =1 \\ \frac{𝑎}{2}+𝑎+𝑎+\frac{5}{2}𝑎 & =1 \\ 5𝑎 & =1 \\ 𝑎 & =\frac{1}{5}.\end{aligned}


$$

### Example: Calculating a Joint Probability From a Table

#### Question

Compute $P\Big((X,Y) \in \{(2,3), (6,1) \}\Big)$ given that the random variables $X$ and $Y$ have the joint probability mass function $f(x,y)$ shown in the table above.

#### Explanation

Using the values in the table, we have

$$


\begin{aligned}𝑃((𝑋,𝑌)∈{(2,3),(6,1)}) & =𝑃((𝑋,𝑌)=(2,3))+𝑃((𝑋,𝑌)=(6,1)) \\ & =𝑓(2,3)+𝑓(6,1) \\ & =0.25+0.3 \\ & =0.55.\end{aligned}


$$

### Example: Calculating a Joint Probability Containing Inequalities From a Table

#### Question

Compute $P\left(X\cdot Y \geq 4 \right)$ given that the random variables $X$ and $Y$ have the joint probability mass function $f(x,y)$ shown in the table above.

#### Explanation

Using the values in the table, we have

$$


\begin{aligned}𝑃(𝑋⋅𝑌≥4) & =𝑃((𝑋,𝑌)∈{(1,4),(2,2),(2,4)}) \\ & =𝑃((𝑋,𝑌)=(1,4))+𝑃((𝑋,𝑌)=(2,2))+𝑃((𝑋,𝑌)=(2,4)) \\ & =𝑓(1,4)+𝑓(2,2)+𝑓(2,4) \\ & =0.05+0.25+0.15 \\ & =0.45.\end{aligned}


$$
