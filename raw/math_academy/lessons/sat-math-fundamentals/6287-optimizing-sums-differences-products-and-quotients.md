# Optimizing Sums, Differences, Products, and Quotients

Source: https://www.mathacademy.com/topics/6287?courseId=120
Topic ID: 6287

## Prerequisites

- [Global Extrema of Functions](../algebra-i/1888-global-extrema-of-functions.md)

## Lesson

### Introduction

In this lesson, we will discuss how to maximize or minimize the sum, product, difference, and quotient of two numbers taken from *closed* intervals. This will be very useful for some of the work that follows.

**Watch Out!** We'll *only* consider closed intervals of numbers in this lesson. Recall that closed intervals are defined using "or equal to" compound inequalities, such as

$$


1\leq x \leq 5


$$

or, using interval notation,

$$


x\in [1,5].


$$

The rules we'll discuss here *do not apply* to open or semi-open intervals, such as

$$


3< y < 5\qquad\text{or}\qquad 8 < x \leq 12.


$$

Also, it will be necessary to restrict our attention to positive numbers when discussing products and quotients.

### Maximizing a Sum or Product

Suppose we have two numbers $a$ and $b$ such that

$$


1\leq a \leq 7\qquad\text{and}\qquad 4\leq b \leq 8.


$$

What is the largest possible value of $a + b?$

We can answer this question by applying the following principle:

*To **** the sum of two numbers $a$ and $b,$ we must add the largest possible value of $a$ to the largest possible value of $b.$*

So, let's compute the largest possible values of $a$ and $b,$ and find their sum:

- Since $1\leq a \leq 7,$ the largest possible value of $a$ is $7.$ We'll write this as follows:

- Since $4\leq b \leq 8,$ the largest possible value of $b$ is $8.$

Therefore,

$$


\begin{aligned}max(𝑎+𝑏) & =max(𝑎)+max(𝑏) \\ & =7+8 \\ & =15.\end{aligned}


$$

The rule for maximizing a *product* is similar, though it only works for positive numbers:

*To **** the product of two **** numbers $a$ and $b,$ we must multiply the largest possible value of $a$ by the largest possible value of $b.$*

So, in this example, we have

$$


\begin{aligned}max(𝑎𝑏) & =max(𝑎)⋅max(𝑏) \\ & =7⋅8 \\ & =56.\end{aligned}


$$

**Note**: We can think of $\max(a)$ as a *function* that takes a number $a$ as input and returns the largest possible value of $a$ as output, and similarly for $\max(b).$

### Minimizing a Sum or Product

Let's consider our two intervals once more:

$$


1\leq a \leq 7\qquad\text{and}\qquad 4\leq b \leq 8.


$$

What is the *smallest* possible value of $a + b?$

We can answer this question by applying the following principle:

*To **** the sum of two numbers $a$ and $b,$ we must add the smallest possible value of $a$ to the smallest possible value of $b.$*

So, let's compute the smallest possible values of $a$ and $b,$ and find their sum:

- Since $1\leq a \leq 7,$ the smallest possible value of $a$ is $1.$ We'll write this as follows:

- Since $4\leq b \leq 8,$ the smallest possible value of $b$ is $4.$

Therefore,

$$


\begin{aligned}min(𝑎+𝑏) & =min(𝑎)+min(𝑏) \\ & =1+4 \\ & =5.\end{aligned}


$$

The rule for minimizing a *product* is similar, though it only works for positive numbers:

*To **** the product of two **** numbers $a$ and $b,$ we must multiply the smallest possible value of $a$ by the smallest possible value of $b.$*

So, in this example, we have

$$


\begin{aligned}min(𝑎𝑏) & =min(𝑎)⋅min(𝑏) \\ & =1⋅4 \\ & =4.\end{aligned}


$$

### Example: Optimizing Sums and Products

#### Question

If $1\leq p \leq 5$ and $6\leq q \leq 13,$ what's the smallest possible value of $pq?$

#### Explanation

To minimize the product of two positive numbers $p$ and $q,$ we must multiply the smallest possible value of $p$ by the smallest possible value of $q.$

More precisely, if $a, b, c,$ and $d$ are positive numbers such that

$$


a\leq p\leq b\quad\textrm{and}\quad c\leq q\leq d


$$

then the minimum value of $pq$ equals

$$


\begin{aligned}min(𝑝𝑞) & =min(𝑝)⋅min(𝑞) \\ & =𝑎𝑐.\end{aligned}


$$

In this case, $\min(p) = 1$ and $\min(q) = 6.$ Therefore,

$$


\begin{aligned}min(𝑝)⋅min(𝑞)=1⋅6=6.\end{aligned}


$$

### Maximizing Differences and Quotients

We need to be more careful when finding the maximum or minimum of a difference or a quotient!

For example, suppose we have two numbers $a$ and $b$ such that

$$


1\leq a \leq 12\qquad\text{and}\qquad 4\leq b \leq 8.


$$

What is the largest possible value of $a - b?$

We can answer this question by applying the following principle:

*To **** the difference of two numbers $a$ and $b,$ we take the **** value of $a$ and subtract the **** value of $b.$*

Take a moment to appreciate why this must be true. If we're trying to maximize a difference, we want to start with the largest number possible and then subtract as little as possible from it.

So, let's compute the largest possible value of $a,$ the smallest possible value of $b,$ and find their difference:

- Since $1\leq a \leq 12,$ the largest possible value of $a$ is $12.$

- Since $4\leq b \leq 8,$ the smallest possible value of $b$ is $4.$

Therefore,

$$


\begin{aligned}max(𝑎−𝑏) & =max(𝑎)−min(𝑏) \\ & =12−4 \\ & =8.\end{aligned}


$$

The rule for maximizing a *quotient* is similar, though it only works for positive numbers:

*To **** the quotient of two **** numbers $a$ and $b,$ we take the **** value of $a$ and divide by the **** value of $b.$*

Again, take a moment to appreciate why this must be true. We want the dividend to be as large as possible, while the divisor should be as small as possible.

So, in this example, we have

$$


\begin{aligned}max(\frac{𝑎}{𝑏}) & =\frac{max(𝑎)}{min(𝑏)} \\ & =\frac{12}{4} \\ & =3.\end{aligned}


$$

### Minimizing Differences and Quotients

Let's consider our intervals once more.

$$


1\leq a \leq 12\qquad\text{and}\qquad 4\leq b \leq 8.


$$

What is the smallest possible value of $a - b?$

We can answer this question by applying the following principle:

*To **** the difference of two numbers $a$ and $b,$ we take the **** value of $a$ and subtract the **** value of $b.$*

Again, take a moment to appreciate why this must be true. If we're trying to minimize a difference, we want to start with the smallest number possible and then subtract as much as possible from it.

So, let's compute the smallest possible value of $a,$ the largest possible value of $b,$ and find their difference:

- Since $1\leq a \leq 12,$ the smallest possible value of $a$ is $1.$

- Since $4\leq b \leq 8,$ the largest possible value of $b$ is $8.$

Therefore,

$$


\begin{aligned}min(𝑎−𝑏) & =min(𝑎)−max(𝑏) \\ & =1−8 \\ & =−7.\end{aligned}


$$

The rule for minimizing a *quotient* is similar, though it only works for positive numbers:

*To **** the quotient of two **** numbers $a$ and $b,$ we take the **** value of $a$ and divide by the **** value of $b.$*

Again, take a moment to appreciate why this must be true.

So, in this example, we have

$$


\begin{aligned}min(\frac{𝑎}{𝑏}) & =\frac{min(𝑎)}{max(𝑏)} \\ & =\frac{1}{8} \\ & =0.125\end{aligned}


$$

### Example: Optimizing Differences and Quotients

#### Question

If $3\leq u \leq 15$ and $4\leq v \leq 27,$ what's the smallest possible value of $\dfrac{u}{v}?$

#### Explanation

To minimize the quotient of two positive numbers $u$ and $v,$ we take the smallest possible value of $u$ and divide by the largest possible value of $v.$

More precisely, if $a, b, c,$ and $d$ are positive numbers such that

$$


a\leq u\leq b\quad\textrm{and}\quad c\leq v\leq d


$$

then the minimum value of $\dfrac{u}{v}$ equals

$$


\begin{aligned}min(\frac{𝑢}{𝑣}) & =\frac{min(𝑢)}{max(𝑣)} \\ & =\frac{𝑎}{𝑑}.\end{aligned}


$$

In this case, $\min(u) = 3$ and $\max(v) = 27.$ Therefore,

$$


\begin{aligned}\frac{min(𝑢)}{max(𝑣)}=\frac{3}{27}=\frac{1}{9}.\end{aligned}


$$

### Example: Identifying True Statements

#### Question

If $a\in [m,n]$ and $b\in [p,q]$ are real numbers, find $\min(a-b).$

#### Explanation

To minimize the difference of two numbers $a$ and $b,$ we take the smallest possible value of $a$ and subtract the largest possible value of $b.$

More precisely, if

$$


m\leq a\leq n\quad\textrm{and}\quad p\leq b\leq q


$$

then the minimum value of $a-b$ equals

$$


\begin{aligned}min(𝑎−𝑏) & =min(𝑎)−max(𝑏) \\ & =𝑚−𝑞.\end{aligned}


$$
