# Product Notation

Source: https://www.mathacademy.com/topics/3081?courseId=73
Topic ID: 3081

## Prerequisites

- [Sigma Notation](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/673-sigma-notation.md)
- [Factorials in Variable Expressions](../../../high-school/traditional/lessons/geometry/3710-factorials-in-variable-expressions.md)

## Lesson

### Introduction

We're used to seeing summations written in compact form using sigma notation.

For example, the notation

$$


\sum_{i=1}^4 (2i-3)


$$

represents the sum of the first $4$ terms of the sequence $a_i = 2i-3.$ We evaluate this series as follows:

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{4}}(2𝑖−3) & =(2(1)−3)+(2(2)−3)+(2(3)−3)+(2(4)−3) \\ & =(−1)+1+3+5 \\ & =8\end{aligned}


$$

We have a similar notation that compactly represents products of terms of a sequence. For this, we use the $\prod$ symbol.

For example, let's consider the following expression:

$$


\prod_{i =1}^{4} (2i - 3)


$$

This represents the *product* of the first $4$ terms of the sequence $a_i = 2i-3.$ We evaluate this product as follows:

$$


\begin{aligned}\underset{\underset{𝑖=1}{∏}}{\overset{}{4}}(2𝑖−3) & =(2(1)−3)⋅(2(2)−3)⋅(2(3)−3)⋅(2(4)−3)⋅ \\ & =(−1)⋅1⋅3⋅5 \\ & =−15\end{aligned}


$$

### Example: Evaluating a Product

#### Question

Evaluate $\displaystyle \prod_{k=1}^{4} \dfrac{3k - 1}{6k - 1}.$

#### Explanation

We expand the product by multiplying over the index $k$ from $k = 1$ to $k = 4{:}$

$$


\begin{aligned}\underset{\underset{𝑘=1}{∏}}{\overset{}{4}}\frac{3𝑘−1}{6𝑘−1} & =\frac{3(1)−1}{6(1)−1}⋅\frac{3(2)−1}{6(2)−1}⋅\frac{3(3)−1}{6(3)−1}⋅\frac{3(4)−1}{6(4)−1} \\ & =\frac{2}{5}⋅\frac{5}{11}⋅\frac{8}{17}⋅\frac{11}{23} \\ & =\frac{2}{5}⋅\frac{5}{11}⋅\frac{8}{17}⋅\frac{11}{23} \\ & =\frac{2⋅8}{17⋅23} \\ & =\frac{16}{391}\end{aligned}


$$

### Example: Writing a Product Using Product Notation

#### Question

Express the following product using product notation:

$$


(2 - 3^2) \cdot (2 - 4^2) \cdot (2 - 5^2) \cdot \: \ldots \: \cdot (2 - 12^2)


$$

#### Explanation

We can collapse the given expression using product notation over the index $i$ from $i=3$ to $i = 12{:}$

$$


\begin{aligned}(2−3^{2})⋅(2−4^{2})⋅(2−5^{2})⋅\,…\,⋅(2−12^{2})=\underset{\underset{𝑖=3}{∏}}{\overset{}{12}}(2−𝑖^{2})\end{aligned}


$$

### Example: Simplifying a Product

#### Question

Express as a function of only.

#### Explanation

We expand the product by multiplying over the index from to inclusive: Since each denominator from to appears somewhere earlier as a numerator, these common factors cancel, giving
