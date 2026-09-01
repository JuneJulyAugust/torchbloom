# The Division Algorithm

Source: https://www.mathacademy.com/topics/2689?courseId=76
Topic ID: 2689

## Prerequisites

- [Integer Divisibility](./3080-integer-divisibility.md)

## Lesson

### Introduction

Suppose that $a$ is an integer and that $n$ is a positive integer. Then there are *unique* integers $q$ (called the **quotient**) and $r$ (called the **remainder**) such that

$$


a = qn + r \quad\text{where}\quad 0 \leq r \lt n.


$$

This simple idea has far-reaching consequences, as we'll soon discover.

As an example, suppose that $a=56$ and $n=5.$ Then, we can write

$$


56 = \underbrace{{\color{red}{11}}}_{q}\cdot 5 + \underbrace{{\color{blue}{1}}}_{r}.


$$

We can find $q$ using integer division. Once we know $q,$ it's then straightforward to find $r.$

### Example: The Division Algorithm For Positive Integers

#### Question

Let $a=85$ and $n=8.$ Find positive integers $q$ and $r$ such that $a = qn+r,$ where $0 \leq r < n,$ and determine $q \cdot r.$

#### Explanation

Dividing $85$ by $8$ using integer division, we notice that

$$


{\color{red}{10}} < 85\div 8 < 11.


$$

The quotient $q$ is the left-hand value. So $q={\color{red}{10}}.$

Next, we find the remainder $r$ by computing $r = a-qn.$ This gives

$$


r = 85 - (10)(8) = {\color{blue}{5}}.


$$

Therefore, we can write $85 = qn + r$ as follows:

$$


\begin{aligned}85=\underset{𝑞}{\underset{}{10}}⋅8+\underset{𝑟}{\underset{}{5}}\end{aligned}


$$

Finally, $q \cdot r = 10 \cdot 5 = 50.$

### Example: The Division Algorithm For Negative Integers

#### Question

Let $a=-44$ and $n=6.$ Find integers $q$ and $r$ such that $a = qn+r,$ where $0 \leq r < n,$ and determine $q\cdot r.$

#### Explanation

Dividing $-44$ by $6$ using integer division, we notice that

$$


{\color{red}{-8}} < -44\div 6 < -7.


$$

The quotient $q$ is the left-hand value. So $q={\color{red}{-8}}.$

Next, we find the remainder $r$ by solving $r = a-qn.$ This gives

$$


r = -44 - (-8)(6) = {\color{blue}{4}}.


$$

Therefore, we can write $-44 = qn + r$ as follows:

$$


\begin{aligned}−44=\underset{𝑞}{\underset{}{(−8)}}⋅6+\underset{𝑟}{\underset{}{4}}\end{aligned}


$$

Finally, $q\cdot r = -8 \cdot 4 = -32.$
