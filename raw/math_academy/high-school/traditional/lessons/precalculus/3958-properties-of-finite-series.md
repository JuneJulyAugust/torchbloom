# Properties of Finite Series

Source: https://www.mathacademy.com/topics/3958?courseId=43
Topic ID: 3958

## Prerequisites

- [Sigma Notation](./673-sigma-notation.md)

## Lesson

### Introduction

Suppose we have a sequence $a_i$ for $i\geq 1,$ and the sum of the first $10$ terms of a sequence equals $25.$ We can express this using sigma notation as follows:

$$



\sum_{i=1}^{10} a_i = 25



$$

If we multiply each term of the sequence by $2,$ what will be the sum of the first $10$ terms of this new sequence? In other words, what is the value of the following sum?

$$



\sum_{i=1}^{10} 2a_i



$$

We can compute this sum by expanding the summation:

$$



\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}2𝑎_{𝑖} & =2𝑎_{1}+2𝑎_{2}+⋯+2𝑎_{10} \\ & =2⋅(𝑎_{1}+𝑎_{2}+⋯+𝑎_{10}) \\ & =2⋅\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}𝑎_{𝑖} \\ & =2⋅25 \\ & =50\end{aligned}



$$

In short, we found that

$$



\sum_{i=1}^{10} 2a_i = 2\cdot \sum_{i=1}^{10} a_i .



$$

In general, if $a_i$ is a sequence and $c$ is any constant, then

$$



\sum_{i=1}^{n} c a_i = c \cdot \sum_{i=1}^{n} a_i.



$$

### Example: Evaluating a Series Using the Constant Multiple Rule

#### Question

Given that $\displaystyle{\sum_{i=1}^{10} a_i} = 5,$ find the value of $\displaystyle{\sum_{i=1}^{10} (-2a_i)}.$

#### Explanation

Recall that for any constant $c,$ we have

$$



\sum_{i=1}^{n} c a_i = c \cdot \sum_{i=1}^{n} a_i.



$$

Therefore,

$$



\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}(−2𝑎_{𝑖}) & =−2⋅\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}𝑎_{𝑖} \\ & =−2⋅5 \\ & =−10.\end{aligned}



$$

### Sums of Constants

Let's now determine the value of the following sum:

$$



\sum_{i=1}^{15} 1



$$

This is an example of a series where every term in the corresponding sequence equals $1.$

To compute this sum, let's write out the summation explicitly:

$$



\sum_{i=1}^{15} 1 = \underbrace{1+1+\cdots + 1}_{15\,\text{times}}



$$

Therefore,

$$



\sum_{i=1}^{15} 1 = 15\cdot 1 = 15.



$$

In general, for any integer $n \geq 1,$ we have

$$



\sum_{i=1}^{n} 1 = n.



$$

### Example: Evaluating a Sum of Constants

#### Question

Evaluate $\displaystyle{\sum_{i=1}^{100} \dfrac14}.$

#### Explanation

Using the constant multiple rule, we can write

$$



\sum_{i=1}^{100}\dfrac14 =\dfrac14\cdot \sum_{i=1}^{100} 1.



$$

Then, we note that

$$



\sum_{i=1}^{100} 1 = \underbrace{1+1+\cdots + 1}_{100\,\text{times}} = 100.



$$

Therefore,

$$



\dfrac14\cdot \sum_{i=1}^{100} 1 = \dfrac14\cdot 100= 25.



$$

### The Sum Rule

If $a_i$ and $b_i$ for $i\geq 1$ are sequences, then we have the following property:

$$



\sum_{i=1}^{n} (a_i+b_i) = \sum_{i=1}^{n} a_i + \sum_{i=1}^{n} b_i



$$

We sometimes call this property the **sum rule**.

To see how we might apply this rule, suppose we are given the following series:

$$



\sum_{i=1}^{10} a_i = 5, \qquad \sum_{i=1}^{10} b_i = 8



$$

Let's find the value of

$$



\sum_{i=1}^{10} (2a_i-3b_i).



$$

First, we apply the sum rule:

$$



\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}(2𝑎_{𝑖}−3𝑏_{𝑖}) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}(2𝑎_{𝑖}+(−3𝑏_{𝑖})) \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}2𝑎_{𝑖}+\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}(−3𝑏_{𝑖})\end{aligned}



$$

Now, recall that for any constant $c,$ we have

$$



\sum_{i=1}^{n} c a_i = c \cdot \sum_{i=1}^{n} a_i.



$$

Applying the constant multiple rule to our two series, we finally arrive at

$$



\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}2𝑎_{𝑖}+\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}(−3𝑏_{𝑖}) & =2⋅\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}𝑎_{𝑖}−3⋅\underset{\underset{𝑖=1}{∑}}{\overset{}{10}}𝑏_{𝑖} \\ & =2⋅5−3⋅8 \\ & =−14.\end{aligned}



$$

### Example: Evaluating a Sum Using Finite Series Properties

#### Question

Given that $\displaystyle{\sum_{i=1}^{20} s_i} = -7$ and $\displaystyle{\sum_{i=1}^{20} t_i} = 9,$ find the value of $\displaystyle{\sum_{i=1}^{20} (10s_i+12t_i+5)}.$

#### Explanation

Recall the following properties of sums:

- $\displaystyle \sum_{i=1}^{n} (s_i+t_i) = \sum_{i=1}^{n} s_i + \sum_{i=1}^{n} t_i$

- $\displaystyle \sum_{i=1}^{n} c s_i = c \cdot \sum_{i=1}^{n} s_i$

- $\displaystyle \sum_{i=1}^{n} 1 = n$

By applying each property in turn, we obtain

$$



\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{20}}(10𝑠_{𝑖}+12𝑡_{𝑖}+5) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{20}}10𝑠_{𝑖}+\underset{\underset{𝑖=1}{∑}}{\overset{}{20}}12𝑡_{𝑖}+\underset{\underset{𝑖=1}{∑}}{\overset{}{20}}5 \\ & =10⋅\underset{\underset{𝑖=1}{∑}}{\overset{}{20}}𝑠_{𝑖}+12⋅\underset{\underset{𝑖=1}{∑}}{\overset{}{20}}𝑡_{𝑖}+5⋅\underset{\underset{𝑖=1}{∑}}{\overset{}{20}}1 \\ & =10⋅(−7)+12⋅9+5⋅20 \\ & =138.\end{aligned}



$$
