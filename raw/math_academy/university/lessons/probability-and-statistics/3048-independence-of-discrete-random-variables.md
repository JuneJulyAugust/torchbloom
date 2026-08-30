# Independence of Discrete Random Variables

Source: https://www.mathacademy.com/topics/3048?courseId=73
Topic ID: 3048

## Prerequisites

- [Marginal Distributions for Discrete Random Variables](./3002-marginal-distributions-for-discrete-random-variables.md)

## Lesson

### Introduction

Let $X$ and $Y$ be discrete random variables with supports $S_X$ and $S_Y,$ respectively. We say that $X$ and $Y$ are **independent** if, for all $x\in S_X$ and $y\in S_Y,$ we have

$$


P(X=x, Y=y)=P(X=x)\cdot P(Y=y).


$$

Moreover, if $X$ and $Y$ have the joint probability mass function $f(x,y),$ and $f_X(x)$ and $f_Y(y)$ are the marginal mass functions of $X$ and $Y,$ respectively, then

$$


f(x, y) = f_X(x)\cdot f_Y (y)


$$

for all $x\in S_X$ and $y\in S_Y.$

If the random variables are not independent, they are **dependent**.

### Example: Determining Whether Two Random Variables are Independent

#### Question

The joint probability distribution $f(x,y)$ of the discrete random variables $X$ and $Y$ is given above, while the marginal mass functions for these variables are shown below.

Which of the following statements are true?

1. $P({X = 0}, {Y = 0}) = P(X=0) \cdot P(Y=0)$

2. $P({X = x}, {Y = y}) = P(X=x) \cdot P(Y=y)$ for all possible $x$ and $y$

3. $X$ and $Y$ are independent

#### Explanation

Two discrete random variables $X$ and $Y$ with a joint probability mass function $f(x,y)$ are independent if and only if

$$


f(x, y) = f_X(x) \cdot f_Y (y)


$$

for all possible values $x$ and $y,$ where $f_X(x)$ and $f_Y (y)$ are the marginal probability mass functions for $X$ and $Y,$ respectively.

With that in mind, let's examine our statements.

- Statement I is true. From the table, we obtain that $P({X = 0}, {Y = 0}) = f(0,0) = 0.24.$ On the other hand,

- Statement II is true. Checking all other possible products, we obtain the following: So, $P({X = x}, {Y = y}) = P(X=x) \cdot P(Y=y)$ for all possible $x$ and $y.$

- Statement III is true. Since statement II is true, our random variables $X$ and $Y$ must be independent.

Therefore, the correct answer is "I, II, and III."

### Example: Determining Whether Two Random Variables are Independent Given the Joint PMF Only

#### Question

The joint probability distribution $f(x,y)$ of the discrete random variables $X$ and $Y$ is given below.

Which of the following statements are true?

1. $P({X = 0}, {Y = 0}) = P(X=0) \cdot P(Y=0)$

2. $P({X = x}, {Y = y}) = P(X=x) \cdot P(Y=y)$ for all possible $x$ and $y$

3. $X$ and $Y$ are independent

#### Explanation

Two discrete random variables $X$ and $Y$ with a joint probability mass function $f(x,y)$ are independent if and only if

$$


f(x, y) = f_X(x) \cdot f_Y (y)


$$

for all possible values $x$ and $y,$ where $f_X(x)$ and $f_Y (y)$ are the marginal probability mass functions for $X$ and $Y,$ respectively.

Computing the marginal probability mass functions for $X$ and $Y,$ we obtain the following:

With that in mind, let's examine our statements.

- Statement I is true. From the table, we obtain that $P({X = 0}, {Y = 0}) = f(0,0) = 0.28.$ Likewise,

- Statement II is true. Checking all other possible products, we obtain the following: So, $P({X = x}, {Y = y}) = P(X=x) \cdot P(Y=y)$ for all possible $x$ and $y.$

- Statement III is true. Since statement II is true, our random variables $X$ and $Y$ must be independent.

Therefore, the correct answer is "I, II, and III."

### Example: Calculating Joint Probabilities

#### Question

The marginal mass functions of the discrete random variables $X$ and $Y$ are shown below. Given that the corresponding joint probability mass function is $f(x,y),$ find $f(4,2).$

#### Explanation

Since we don't know whether $X$ and $Y$ are independent, it is impossible to determine the joint distribution of $X$ and $Y$ using only the given information.
