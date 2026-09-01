# Counting Terms in Multinomial Expansions

Source: https://www.mathacademy.com/topics/1409?courseId=109
Topic ID: 1409

## Prerequisites

- [The Multinomial Theorem](./1407-the-multinomial-theorem.md)

## Lesson

### Introduction

Let's recall the multinomial theorem:

*For any positive integer $n,$ the terms of $(a+b+c)^n$ can be written as*

$$



\binom{n}{k_1,\,k_2,\,k_3} a^{k_1} b^{k_2} c^{k_3},



$$

*where $k_1 + k_2 + k_3 = n$ and the general formula for the multinomial coefficient is*

$$



\binom{n}{k_1,\,k_2,\,k_3} = \dfrac{n!}{k_1!\, k_2! \, k_3! }.



$$

For example, using the multinomial theorem, we have

$$



\begin{aligned}(𝑎+𝑏+𝑐)^{2} & =(\frac{2}{2,\,0,\,0})𝑎^{2}𝑏^{0}𝑐^{0}+(\frac{2}{0,\,2,\,0})𝑎^{0}𝑏^{2}𝑐^{0}+(\frac{2}{0,\,0,\,2})𝑎^{0}𝑏^{0}𝑐^{2} \\ & ==+(\frac{2}{1,\,1,\,0})𝑎^{1}𝑏^{1}𝑐^{0}+(\frac{2}{1,\,0,\,1})𝑎^{1}𝑏^{0}𝑐^{1}+(\frac{2}{0,\,1,\,1})𝑎^{0}𝑏^{1}𝑐^{1} \\ & =\frac{2!}{2!\,0!\,0!}𝑎^{2}+\frac{2!}{0!\,2!\,0!}𝑏^{2}+\frac{2!}{0!\,0!\,2!}𝑐^{2}+\frac{2!}{1!\,1!\,0!}𝑎𝑏+\frac{2!}{1!\,0!\,1!}𝑎𝑐+\frac{2!}{0!\,1!\,1!}𝑏𝑐 \\ & =𝑎^{2}+𝑏^{2}+𝑐^{2}+2𝑎𝑏+2𝑎𝑐+2𝑏𝑐.\end{aligned}



$$

Notice that we have $6$ terms in the above expansion:

$$



\begin{aligned}(𝑎+𝑏+𝑐)^{2}=\underset{6 terms}{\underset{}{𝑎^{2}+𝑏^{2}+𝑐^{2}+2𝑎𝑏+2𝑎𝑐+2𝑏𝑐}}\end{aligned}



$$

In general, the number of distinct terms in the multinomial expansion with $t$ variables raised to the $n$th power is given by

$$



\binom{n+t-1}{t-1}.



$$

In the case of $(a+b+c)^2,$ we have a multinomial expansion with $t=3$ variables raised to the $n=2$nd power. Therefore, the number of distinct terms in the expansion of $(a+b+c)^2$ is

$$



\begin{aligned}(\frac{2+3−1}{3−1}) & =(\frac{4}{2})=6\,.\end{aligned}



$$

Indeed, this matches up with what we saw in our expansion.

Note that one of the variables can actually be a nonzero constant and the number of terms will still be the same. For example, we could take $c = 1$ above and we'd still get an expansion with $6$ terms:

$$



\begin{aligned}(𝑎+𝑏+1)^{2}=\underset{6 terms}{\underset{}{𝑎^{2}+𝑏^{2}+1+2𝑎𝑏+2𝑎+2𝑏}}\end{aligned}



$$

However, at most one variable can be a nonzero constant; the rest must be distinct variables.

### Example: Calculating the Number of Terms in the Expansion of a Trinomial

#### Question

How many terms are there in the expansion of $(a-b+3d)^5?$

#### Explanation

The number of distinct terms in the multinomial expansion with $t$ variables raised to the $n$th power is given by

$$



\binom{n+t-1}{t-1}.



$$

Here we have a multinomial expansion with $t=3$ variables raised to the $n=5$th power. Therefore, the number of distinct terms in the expansion of $(a-b+3d)^5$ is

$$



\begin{aligned}(\frac{5+3−1}{3−1}) & =(\frac{7}{2})=21\,.\end{aligned}



$$

### Example: Calculating the Number of Terms in the Expansion of a Larger Multinomial

#### Question

How many terms are there in the expansion of $(x+y+w+z)^7?$

#### Explanation

The number of distinct terms in the multinomial expansion with $t$ variables raised to the $n$th power is given by

$$



\binom{n+t-1}{t-1}.



$$

Here we have a multinomial expansion with $t=4$ variables raised to the $n=7$th power. Therefore, the number of distinct terms in the expansion of $(x+y+w+z)^7$ is

$$



\begin{aligned}(\frac{7+4−1}{4−1}) & =(\frac{10}{3})=120\,.\end{aligned}



$$
