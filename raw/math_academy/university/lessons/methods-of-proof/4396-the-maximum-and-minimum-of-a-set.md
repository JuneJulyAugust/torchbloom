# The Maximum and Minimum of a Set

Source: https://www.mathacademy.com/topics/4396?courseId=76
Topic ID: 4396

## Prerequisites

- [The Conditional Definition of a Set](./4425-the-conditional-definition-of-a-set.md)

## Lesson

### Introduction

The **minimum** of a set $S$ is the element $x_{\min} \in S$ such that

$$


x_{\min} \leq x


$$

for all $x \in S.$ In other words, the minimum is the element of $S$ that is *smaller than or equal to* any other element.

Similarly, the **maximum** of a set $S$ is the element $x_{\max} \in S$ such that

$$


x \leq x_{\max}


$$

for all $x \in S.$ In other words, the maximum is the element of $S$ that is *larger than or equal to* any other element.

For example, what are the minimum and maximum of the following set?

$$


A = \big\{ 2, \: -\sqrt{5}, \: 3, \: -1 \big\}


$$

Note that $-\sqrt{5} \approx -2.236.$ Therefore:

$$


\begin{aligned}min(𝐴) & =min{2,\,−\sqrt{5},\,3,\,−1}=−\sqrt{5} \\ max(𝐴) & =max{2,\,−\sqrt{5},\,3,\,−1}=3\end{aligned}


$$

Some sets may not have a maximum or minimum.

For example, consider the semi-open interval of real numbers $B=[1, 5).$ In this case, we have

$$


\min(B) = \min[1, 5) = 1.


$$

However, since $5 \notin B,$ the set has no maximum!

Finally, note the following:

- The maximum and minimum elements *must* belong to the underlying set.

- If the maximum or minimum elements exist, they are unique. In other words, there can be, at most, only one maximum and only one minimum.

- If the "less than or equal to" operation is not defined *for all* elements of a set $S,$ then the set has no maximum or minimum. For example, the following set has no minimum and maximum:

### Example: Finding the Maximum and Minimum of a Set

#### Question

What are the minimum and maximum of the set $A = \left[0,3\right]?$

#### Explanation

Recall that

- $x_{\max}$ is the maximum of a set $S$ if $x_{\max} \in S$ and $x \leq x_{\max}$ for all $x \in S,$ and

- $x_{\min}$ is the minimum of a set $S$ if $x_{\min} \in S$ and $x_{\min} \leq x$ for all $x \in S.$

Therefore, we have the following:

$$


\begin{aligned}min(𝐴) & =min[0,3]=0 \\ max(𝐴) & =max[0,3]=3\end{aligned}


$$

### Example: Explaining the Existence of a Maximum of Minimum

#### Question

Given the set $S = (-\infty,7],$ explain why $\max(S) = 7.$

#### Explanation

Recall that $x_{\max}$ is the maximum of a set $S$ if

- $x_{\max} \in S,$ and

- $x\leq x_{\max}$ for all $x \in S.$

In our case, we have that $7$ is the maximum of the set $S$ because

- $7 \in S,$ and

- $x \leq 7$ for all $x \in S.$

### Example: Maximums and Minimums in More Complex Settings

#### Question

What are the maximum and minimum values of the set $A = \{n \in \mathbb{Z} \mid \: 3 \lt n \leq 8 \}?$

#### Explanation

Recall that

- $x_{\max}$ is the maximum of a set $S$ if $x_{\max} \in S$ and $x \leq x_{\max}$ for all $x \in S,$ and

- $x_{\min}$ is the minimum of a set $S$ if $x_{\min} \in S$ and $x_{\min} \leq x$ for all $x \in S.$

Notice that the elements of the set can be listed as

$$


A = \{ 4, \: 5, \: 6, \: 7, 8\}.


$$

Therefore, the minimum of the set equals $4,$ while the maximum of the set equals $8.$
