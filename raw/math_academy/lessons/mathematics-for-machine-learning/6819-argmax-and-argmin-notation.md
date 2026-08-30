# Argmax and Argmin Notation

Source: https://www.mathacademy.com/topics/6819?courseId=145
Topic ID: 6819

## Prerequisites

- [The Maximum and Minimum of a Set](./4396-the-maximum-and-minimum-of-a-set.md)

## Lesson

### Introduction

In a previous lesson, we used $\max$ and $\min$ to talk about the largest and smallest *values* a function can take on a set.

In this lesson, we learn two closely related pieces of notation:

- $\max$ and $\min$ return the best (largest/smallest) *function value*.

- $\arg\max$ and $\arg\min$ return the *input value* (the "argument") where that best value occurs.

For example, let $S = \{1,2,3\}$ and suppose

$$


f(1)=4,\qquad f(2)=7,\qquad f(3)=6.


$$

Then the largest function value is $7,$ and it occurs when $x=2{:}$

$$


\begin{aligned}\underset{𝑥∈𝑆}{max}𝑓(𝑥) & =7, \\ arg⁡\underset{𝑥∈𝑆}{max}𝑓(𝑥) & =2.\end{aligned}


$$

Similarly, $\min_{x \in S} f(x)$ is the smallest function value, and $\arg\min_{x \in S} f(x)$ is an input where that smallest value occurs.

**Watch out!** Sometimes the best value occurs at more than one input. In that case, we need to clarify what $\arg\max$ (or $\arg\min$) means. We will handle this after we practice the basic case.

### Example: Distinguishing Between Max/Min and Argmax/Argmin

#### Question

Let $S=\{-1,0,2,4\}$ and suppose

$$


f(-1)=3,\qquad f(0)=-2,\qquad f(2)=5,\qquad f(4)=1.


$$

Compute the following:

$$


\max_{x \in S} f(x),\qquad \arg\max_{x \in S} f(x),\qquad \min_{x \in S} f(x),\qquad \arg\min_{x \in S} f(x).


$$

#### Explanation

Recall that

- $\max\limits_{x \in S} f(x)$ is the largest output value, while

- $\arg\max\limits_{x \in S} f(x)$ is an input in $S$ where that largest output occurs.

On the other hand,

- $\min\limits_{x \in S} f(x)$ is the smallest output value, while

- $\arg\min\limits_{x \in S} f(x)$ is an input in $S$ where that smallest output occurs.

The outputs of $f$ on $S$ are

$$


3,\qquad -2,\qquad 5,\qquad 1.


$$

The largest output is $5,$ and it occurs at $x=2.$ Therefore,

$$


\max_{x \in S} f(x)=5, \qquad \arg\max_{x \in S} f(x)=2.


$$

Similarly, the smallest output is $-2,$ and it occurs at $x=0.$ Therefore,

$$


\min_{x \in S} f(x)=-2, \qquad \arg\min_{x \in S} f(x)=0.


$$

### Argmax and Argmin With Ties

Sometimes a function attains its largest (or smallest) value at more than one input. In that case, there are multiple inputs that satisfy the definition of $\arg\max$ (or $\arg\min$).

In this course, when a tie occurs, we report the *set* of all inputs where the maximum is achieved as follows:

$$


\arg\max_{x \in S} f(x) = {x \in S{:} f(x) = \max_{u \in S} f(u)}.


$$

Similarly, when a tie occurs, we report the set of all inputs where the minimum is achieved as follows:

$$


\arg\min_{x \in S} f(x) = {x \in S{:} f(x) = \min_{u \in S} f(u)}.


$$

The quantities $\max_{x \in S} f(x)$ and $\min_{x \in S} f(x)$ are still single numbers.

### Example: Computing Argmax and Argmin With Ties

#### Question

Let $S=\{-1,0,2,3\}$ and suppose

$$


f(-1)=4,\qquad f(0)=1,\qquad f(2)=4,\qquad f(3)=2.


$$

Compute $\max_{x \in S} f(x)$ and $\arg\max_{x \in S} f(x).$

#### Explanation

Recall that

- $\max\limits_{x \in S} f(x)$ is the largest output value, while

- $\arg\max\limits_{x \in S} f(x)$ is an input in $S$ where that largest output occurs.

The output values are $4,1,4,$ and $2.$ The maximum output value is $4.$

This maximum occurs at both $x=-1$ and $x=2.$ Therefore,

$$


\max_{x \in S} f(x)=\boxed{4} \qquad \textrm{and} \qquad \arg\max_{x \in S} f(x)=\boxed{\{-1,2\}}.


$$

### Example: Writing and Reading Formal Notation

#### Question

Let $S$ be a set and let $f$ be a real-valued function on $S.$ Consider the expression

$$


x^*=\arg\max_{x \in S} f(x).


$$

What does this statement mean in words? Also, what does $\max_{x \in S} f(x)$ represent?

#### Explanation

The expression $x^*=\arg\max_{x \in S} f(x)$ means that:

- $x^*$ is an input value in $S.$

- Among all $x \in S,$ the value $f(x^*)$ is as large as possible.

In other words, $x^*$ is a choice of input where $f$ attains its largest value on $S.$

By contrast, $\max_{x \in S} f(x)$ is not an input. It is the largest ** that $f$ attains on $S.$
