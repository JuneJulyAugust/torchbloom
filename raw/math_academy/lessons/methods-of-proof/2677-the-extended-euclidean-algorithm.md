# The Extended Euclidean Algorithm

Source: https://www.mathacademy.com/topics/2677?courseId=76
Topic ID: 2677

## Prerequisites

- [The Euclidean Algorithm](./2676-the-euclidean-algorithm.md)

## Lesson

### Introduction

For any two integers $a$ and $b,$ there exist integers $u$ and $v$ such that

$$


au+bv= \textrm{gcd}(a,b).


$$

This is known as **Bézout's identity**.

To find the integers $u$ and $v,$ we can use the **extended Euclidean algorithm**, which involves the following three steps:

1. Carry out the Euclidean algorithm to find $\textrm{gcd}(a,b).$

2. Solve for the remainder at each step, up to (and including) the step where the greatest common divisor appeared as a remainder.

3. Back-substitute the remainders to reach the equation $au+bv= \textrm{gcd}(a,b).$

For example, let's use the extended Euclidean algorithm to find integers $u$ and $v$ such that

$$


48u+18v= \textrm{gcd}(48,18).


$$

- **Step 1:** First, we carry out the Euclidean algorithm to find $\textrm{gcd}(48,18).$ So, we find that $\text{gcd}(48,18) =6.$

- **Step 2:** We solve for the remainder (the rightmost term) at each step, up to (and including) the step where the greatest common divisor appeared as an integer.

- **Step 3:** Finally, we back-substitute the remainders to reach the equation $48u+18v= 6.$

Therefore, $u=-1$ and $v=3.$

### Example: Applying the Extended Euclidean Algorithm When the Two Numbers are Not Coprime

#### Question

Using the extended Euclidean algorithm, compute integers $u$ and $v$ such that $30u + 8v = \text{gcd}(30,8).$ What is the value of $u+v?$

#### Explanation

We will use the extended Euclidean algorithm. First, we apply the forward reduction:

$$


\begin{aligned}\begin{aligned}30 & = & 8⋅3 & + & 6 \\ & ↙ & & ↙ & \\ 8 & = & 6⋅1 & + & 2 \\ & ↙ & & ↙ & \\ 6 & = & 2⋅3 & + & 0\end{aligned}\end{aligned}


$$

As a result, $\text{gcd}(30,8) =2.$

Solving for the remainders (the rightmost terms) in the equations above, up to (and including) the equation where the greatest common divisor appeared as a remainder, we get

$$


\begin{aligned}6 & =30−8⋅3 \\ 2 & =8−6.\end{aligned}


$$

Then, we back-substitute:

$$


\begin{aligned}2 & =8−6 \\ & =8−(30−8⋅3) \\ & =8⋅4−30 \\ & =30⋅(−1)+8⋅4\end{aligned}


$$

Therefore, $u=-1$ and $v=4.$

Finally,

$$


u+v=(-1)+4=3.


$$

### Example: Applying the Extended Euclidean Algorithm When the Two Numbers are Coprime

#### Question

Using the extended Euclidean algorithm, compute integers $u$ and $v$ such that $36u + 19v = \text{gcd}(36,19).$ What is the value of $u+v?$

#### Explanation

We will use the extended Euclidean algorithm. First, we apply the forward reduction:

$$


\begin{aligned}\begin{aligned}36 & = & 19⋅1 & + & 17 \\ & ↙ & & ↙ & \\ 19 & = & 17⋅1 & + & 2 \\ & ↙ & & ↙ & \\ 17 & = & 2⋅8 & + & 1\end{aligned}\end{aligned}


$$

As a result, $\text{gcd}(19,36) =1.$

Solving for the remainders (the rightmost terms) in the equations above, up to (and including) the equation where the greatest common divisor appeared as a remainder, we get

$$


\begin{aligned}17 & =36−19⋅1 \\ 2 & =19−17 \\ 1 & =17−2⋅8.\end{aligned}


$$

Then, we back-substitute:

$$


\begin{aligned}1 & =17−2⋅8 \\ & =17−(19−17)⋅8 \\ & =17⋅9−19⋅8 \\ & =[36−19]⋅9−19⋅8 \\ & =36⋅9−19⋅17 \\ & =36⋅9+19⋅(−17)\end{aligned}


$$

Therefore, $u=9,v=-17,$ and we can write

$$


1 = 36\cdot \boxed{9} + 19\cdot (\boxed{-17}) .


$$

Finally,

$$


u+v=9+(-17)=-8.


$$

### Final Remarks

Throughout this lesson we've made use of **Bézout's identity**, which states that for any two integers $a$ and $b,$ there exist integers $u$ and $v$ such that

$$


au+bv= \textrm{gcd}(a,b).


$$

It can also be shown that any integer combination of $a$ and $b$ is also a multiple of $\textrm{gcd}(a,b).$ In other words, for *any* integers $u'$ and $v',$ we have

$$


\textrm{gcd}(a,b) \mid (au'+bv')


$$

Moreover, the set of integers

$$


\big\{ au'+bv' \,:\, u', v' \in\mathbb Z \big \}


$$

contains *all* the multiples of $\textrm{gcd}(a,b).$

We'll make use of these results in future lessons.
