# Combining Multiple Normally Distributed Random Variables

Source: https://www.mathacademy.com/topics/3638?courseId=73
Topic ID: 3638

## Prerequisites

- [Combining Two Normally Distributed Random Variables](./3009-combining-two-normally-distributed-random-variables.md)

## Lesson

### Introduction

When we form a random variable $Y$ from a sum of **mutually independent**, normally distributed random variables, the distribution of $Y$ is also normal.

More precisely, we have the following theorem:

*If $X_1, X_2,\ldots, X_n$ are mutually independent normal random variables such that*

$$


X_1 \sim N(\mu_1,\sigma_1^2), \qquad X_2\sim (\mu_2,\sigma_2^2), \qquad \ldots, \quad X_n\sim(\mu_n,\sigma_n^2),


$$

*then the random variable*

$$


Y=X_1+X_2+\ldots+X_n


$$

*is normally distributed, where*

$$


Y\sim N(\mu_1+\mu_2+\ldots+\mu_n, \: \sigma_1^2+\sigma_2^2+\ldots+\sigma_n^2).


$$

For example, if the random variables

$$


X_1\sim N({\color{blue}2},{\color{red}3}), \qquad X_2\sim N({\color{blue}1},{\color{red}4}), \qquad X_3\sim N({\color{blue}1},{\color{red}1})


$$

are mutually independent, then

$$


Y=X_1+X_2+X_3


$$

is normally distributed.

Let's figure out the distribution of $Y.$ We start by computing its mean and variance:

$$


\begin{aligned}E[𝑌] & =𝜇_{1}+𝜇_{2}+𝜇_{3} \\ & =2+1+1 \\ & =4, \\ Var[𝑌] & =𝜎_{21}^{}+𝜎_{22}^{}+𝜎_{23}^{} \\ & =3+4+1 \\ & =8.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2}+𝑋_{3} & ∼𝑁(4,8).\end{aligned}


$$

**Watch out!** It is vital that $X_1, X_2,\ldots X_n$ are *mutually independent*.

### Example: Finding the Distribution of a Sum of Normal Random Variables

#### Question

Given that the random variables

$$


X_1\sim N(-1,2^2), \qquad X_2\sim N(3, 3^2), \qquad X_3\sim N(4,2)


$$

are mutually independent, what is the distribution of $Y = X_1 + X_2 + X_3?$

#### Explanation

Recall that if $X_1, X_2,$ and $X_3$ are mutually independent random variables, where

$$


X_1\sim N(\mu_1,\sigma^2_1),\qquad X_2\sim N(\mu_2,\sigma^2_2),\qquad X_3\sim N(\mu_3,\sigma^2_3),


$$

then

$$


\begin{aligned}𝑌 & =𝑋_{1}+𝑋_{2}+𝑋_{3} \\ & ∼𝑁(𝜇_{1}+𝜇_{2}+𝜇_{3},\,𝜎_{21}^{}+𝜎_{22}^{}+𝜎_{23}^{}).\end{aligned}


$$

In our case, we have

$$


X_1\sim N(-1,2^2), \qquad X_2\sim N(3, 3^2), \qquad X_3\sim N(4,2),


$$

and

$$


Y = X_1 + X_2 + X_3.


$$

Since $X_1, X_2,$ and $X_3$ are mutually independent, we have

$$


\begin{aligned}E[𝑌] & =𝜇_{1}+𝜇_{2}+𝜇_{3} \\ & =−1+3+4 \\ & =6, \\ Var[𝑌] & =𝜎_{21}^{}+𝜎_{22}^{}+𝜎_{23}^{} \\ & =2^{2}+3^{2}+2 \\ & =4+9+2 \\ & =15.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑌=𝑋_{1}+𝑋_{2}+𝑋_{3} & ∼𝑁(6,15).\end{aligned}


$$

### Linear Combinations of Normally Distributed Random Variables

When we form a random variable $Y$ from a linear combination of mutually independent, normally distributed random variables, the distribution of $Y$ is also normal.

More precisely, we have the following theorem:

*If $X_1, X_2,\ldots, X_n$ are mutually independent normal random variables such that*

$$


X_1 \sim N(\mu_1,\sigma_1^2), \qquad X_2\sim (\mu_2,\sigma_2^2), \qquad \ldots, \quad X_n\sim(\mu_n,\sigma_n^2),


$$

*and $a_1,a_2,\ldots,a_n$ are real constants, then the linear combination*

$$


Y=a_1X_1+a_2X_2+\ldots+a_nX_n


$$

*is normally distributed, where*

$$


Y\sim N(a_1\mu_1+a_2\mu_2+\ldots+a_n\mu_n, \: a_1^2\sigma_1^2+a_2^2\sigma_2^2+\ldots+a_n^2\sigma_n^2).


$$

For example, if the random variables

$$


X_1\sim N({\color{blue}2},{\color{red}3}), \qquad X_2\sim N({\color{blue}1},{\color{red}4}), \qquad X_3\sim N({\color{blue}1},{\color{red}1})


$$

are mutually independent, then

$$


Y= \boxed{3}X_1+\boxed{2}X_2+\boxed{4}X_3


$$

is normally distributed.

Let's figure out the distribution of $Y.$ We start by computing its mean and variance:

$$


\begin{aligned}E[𝑌] & =𝑎_{1}𝜇_{1}+𝑎_{2}𝜇_{2}+𝑎_{3}𝜇_{3} \\ & =3⋅2+2⋅1+4⋅1 \\ & =6+2+4 \\ & =12, \\ Var[𝑌] & =𝑎_{21}^{}𝜎_{21}^{}+𝑎_{22}^{}𝜎_{22}^{}+𝑎_{23}^{}𝜎_{23}^{} \\ & =3^{2}⋅3+2^{2}⋅4+4^{2}⋅1 \\ & =9⋅3+4⋅4+16⋅1 \\ & =27+16+16 \\ & =59.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑌=3𝑋_{1}+2𝑋_{2}+4𝑋_{3} & ∼𝑁(12,59).\end{aligned}


$$

**Watch out!** It is vital that $X_1, X_2,\ldots X_n$ are *mutually independent*. If they are *not*, their linear combination may *not* be normally distributed!

### Example: Finding the Distribution of a Linear Combination of Normal Random Variables

#### Question

Given that the random variables

$$


X_1 \sim N(-1,3), \qquad X_2 \sim N(3,2), \qquad X_3 \sim N(2,1)


$$

are mutually independent, what is the distribution of $Y = X_1 - 2X_2 - X_3?$

#### Explanation

Recall that if $X_1, X_2,$ and $X_3$ are mutually independent random variables, where

$$


X_1\sim N(\mu_1,\sigma^2_1), \qquad X_2\sim N(\mu_2,\sigma^2_2), \qquad X_3\sim N(\mu_3,\sigma^2_3),


$$

and $a_1,a_2,a_3$ are real constants, then

$$


\begin{aligned}𝑌 & =𝑎_{1}𝑋_{1}+𝑎_{2}𝑋_{2}+𝑎_{3}𝑋_{3} \\ & ∼𝑁(𝑎_{1}𝜇_{1}+𝑎_{2}𝜇_{2}+𝑎_{3}𝜇_{3},\,𝑎_{21}^{}𝜎_{21}^{}+𝑎_{22}^{}𝜎_{22}^{}+𝑎_{23}^{}𝜎_{23}^{}).\end{aligned}


$$

In our case, we have

$$


X_1 \sim N(-1,3), \qquad X_2 \sim N(3,2), \qquad X_3 \sim N(2,1),


$$

and

$$


Y = X_1 - 2X_2 - X_3.


$$

Since $X_1, X_2,$ and $X_3$ are mutually independent, we have

$$


\begin{aligned}E[𝑌] & =𝑎_{1}𝜇_{1}+𝑎_{2}𝜇_{2}+𝑎_{3}𝜇_{3} \\ & =1⋅(−1)+(−2)⋅3+(−1)⋅2 \\ & =−1−6−2 \\ & =−9, \\ Var[𝑌] & =𝑎_{21}^{}𝜎_{21}^{}+𝑎_{22}^{}𝜎_{22}^{}+𝑎_{23}^{}𝜎_{23}^{} \\ & =1^{2}⋅3+(−2)^{2}⋅2+(−1)^{2}⋅1 \\ & =1⋅3+4⋅2+1⋅1 \\ & =3+8+1 \\ & =12.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑌=𝑋_{1}−2𝑋_{2}−𝑋_{3} & ∼𝑁(−9,12).\end{aligned}


$$

### Example: Calculating Probabilities Involving Linear Combinations of Normally Distributed Random Variables

#### Question

Given that the random variables

$$


X_1\sim N(4,5), \qquad X_2\sim N(-2,2), \qquad X_3\sim N(3,1)


$$

are mutually independent and $Y=3X_1-3X_2-X_3,$ calculate $P(|Y| \lt 3).$

**

#### Explanation

Recall that if $X_1, X_2,$ and $X_3$ are mutually independent random variables, where

$$


X_1\sim N(\mu_1,\sigma^2_1), \qquad X_2\sim N(\mu_2,\sigma^2_2), \qquad X_3\sim N(\mu_3,\sigma^2_3),


$$

and $a_1,a_2,a_3$ are real constants, then

$$


\begin{aligned}𝑌 & =𝑎_{1}𝑋_{1}+𝑎_{2}𝑋_{2}+𝑎_{3}𝑋_{3} \\ & ∼𝑁(𝑎_{1}𝜇_{1}+𝑎_{2}𝜇_{2}+𝑎_{3}𝜇_{3},\,𝑎_{21}^{}𝜎_{21}^{}+𝑎_{22}^{}𝜎_{22}^{}+𝑎_{23}^{}𝜎_{23}^{}).\end{aligned}


$$

In our case, we have

$$


X_1\sim N(4,5), \qquad X_2\sim N(-2,2), \qquad X_3\sim N(3,1),


$$

and

$$


Y=3X_1-3X_2-X_3.


$$

Since $X_1, X_2,$ and $X_3$ are mutually independent, we have

$$


\begin{aligned}E[𝑌] & =𝑎_{1}𝜇_{1}+𝑎_{2}𝜇_{2}+𝑎_{3}𝜇_{3} \\ & =3⋅4+(−3)⋅(−2)+(−1)⋅3 \\ & =15, \\ Var[𝑌] & =𝑎_{21}^{}𝜎_{21}^{}+𝑎_{22}^{}𝜎_{22}^{}+𝑎_{23}^{}𝜎_{23}^{} \\ & =3^{2}⋅5+(−3)^{2}⋅2+(−1)^{2}⋅1 \\ & =9⋅5+9⋅2+1⋅1 \\ & =64.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑌∼𝑁(15,64).\end{aligned}


$$

We want to find $P(|Y |\lt 3)=P(-3 < Y \lt 3).$ Thus, we convert $Y$ to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(−3<𝑌<3) & =𝑃(\frac{−3−15}{\sqrt{√64}}<𝑍<\frac{3−15}{\sqrt{√64}}) \\ & ≈𝑃(−2.25<𝑍<−1.5) \\ & =𝑃(𝑍<−1.5)−𝑃(𝑍<−2.25) \\ & =Φ(−1.5)−Φ(−2.25)\end{aligned}


$$

Using the $z$-table, we see that

$$


\begin{aligned}Φ(−1.5)≈0.0668,\,Φ(−2.25)≈0.0122.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝑃(|𝑌|<3) & =Φ(−1.5)−Φ(−2.25) \\ & ≈0.0668−0.0122 \\ & =0.0546.\end{aligned}


$$

### Example: Combinations of Normally Distributed Random Variables in Context

#### Question

A shop sells $2$ types of rice, Type $A$ and Type $B.$ The volume per packet for Type $A$ rice is normally distributed with a mean of $1$ liter and a variance of $0.01$ liters2, while the volume per packet for Type $B$ rice is normally distributed with a mean of $0.7$ liters and a variance of $0.02$ liters2. During cooking, it is known that Type $A$ rice quadruples in volume, while Type $B$ rice triples in volume.

If a single package of Type $A$ rice and $2$ packages of Type $B$ rice are randomly selected and cooked, what is the probability that the resulting rice volume is less than $8$ liters? You may assume that the volumes of rice in the packages are mutually independent.

**

#### Explanation

Let $X_1$ denote the volume of the Type $A$ rice package, and let $X_2$ and $X_3$ denote the volumes of the Type $B$ rice packages. Then, we have

$$


X_1\sim N(1, 0.01), \qquad X_2\sim N(0.7, 0.02), \qquad X_3\sim N(0.7, 0.02).


$$

Let the random variable $Y$ denote the total resulting volume of rice after cooking. Since the Type $A$ rice quadruples in volume, while the type $B$ rice triples in volume, we have

$$


Y= 4X_1+3X_2 + 3X_3.


$$

The random variable $Y$ is normally distributed, where

$$


\begin{aligned}E[𝑌] & =(4⋅1+3⋅0.7+3⋅0.7) \\ & =8.2 \\ Var[𝑌] & =4^{2}⋅0.01+3^{2}⋅0.02+3^{2}⋅0.02 \\ & =16⋅0.01+9⋅0.02+9⋅0.02 \\ & =0.52.\end{aligned}


$$

Therefore,

$$


Y \sim N(8.2, 0.52).


$$

In order to find $P(Y \lt 8),$ we convert $Y$ to a standard normal random variable by $z$-scoring:

$$


\begin{aligned}𝑃(𝑌<8) & =𝑃(𝑍<\frac{8−8.2}{\sqrt{√0.52}}) \\ & ≈𝑃(𝑍<−0.28) \\ & =Φ(−0.28)\end{aligned}


$$

Using the $z$-table, we see that

$$


\Phi(-0.28)\approx 0.3897.


$$

Therefore,

$$


\begin{aligned}𝑃(𝑌<8) & ≈Φ(−0.28) \\ & ≈0.3897.\end{aligned}


$$
