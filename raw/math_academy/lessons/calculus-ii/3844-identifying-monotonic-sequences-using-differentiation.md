# Identifying Monotonic Sequences Using Differentiation

Source: https://www.mathacademy.com/topics/3844?courseId=106
Topic ID: 3844

## Prerequisites

- [Monotonic Sequences](./1096-monotonic-sequences.md)
- [Determining Intervals on Which a Function Is Increasing or Decreasing](../ap-calculus-ab/1359-determining-intervals-on-which-a-function-is-increasing-or-decreasing.md)
- [Solving Inequalities Involving Positive and Negative Factors](../integrated-math-iii-honors/2982-solving-inequalities-involving-positive-and-negative-factors.md)
- [Solving Rational Inequalities](../integrated-math-iii-honors/3355-solving-rational-inequalities.md)

## Lesson

### Introduction

There are several ways to check whether a sequence is increasing or decreasing. One way is to use differentiation.

Let's build up some intuition regarding how this works by considering some examples.

- Consider the sequence $a_n = n^2$ for $n\geq 1,$ and the continuous function $f(x) = x^2,$ defined for $x\geq 1.$ Both the sequence and the function are shown below. Notice that $f(x)$ is continuous on $x\geq1,$ differentiable on $x > 1,$ and $f'(x) \geq 0$ for $x > 1.$ Therefore, $f(x)$ is increasing for $x\geq 1.$ Now, since $a_n$ coincides with $f(x)$ for all positive integer values of $n,$ we can conclude that $a_n$ is an increasing sequence.

- Now, consider the sequence $b_n = 5-n$ for $n\geq 1,$ and the continuous function $g(x) = 5-x,$ defined for $x\geq 1,$ shown below. Notice that $g(x)$ is continuous on $x\geq1,$ differentiable on $x > 1,$ and $g'(x) \leq 0$ for $x > 1.$ Therefore, $g(x)$ is decreasing for $x\geq 1.$ Now, since $b_n$ coincides with $g(x)$ for all positive integer values of $n,$ we can conclude that $b_n$ is a decreasing sequence.

- Finally, consider the sequence $c_n = (n-3)^2$ for $n\geq 1,$ and the continuous function $h(x) = (x-3)^2,$ defined for $x\geq 1.$ The function $h(x)$ is continuous on $x\geq1,$ and differentiable on $x > 1.$ However: $h'(x) \leq 0$ for $1\leq x\leq 3.$ Therefore, $h(x)$ is decreasing on this interval. $h'(x) \geq 0$ for $x\geq 3.$ Therefore, $h(x)$ is increasing on this interval. Now, since $c_n$ coincides with $h(x)$ for all positive integer values of $n,$ we therefore conclude that $c_n$ is *neither increasing nor decreasing*.

Let's now summarize our findings.

### Determining Whether a Sequence Is Monotonic Using Derivatives

Suppose the sequence $a_n$ is defined for $n\geq 1,$ and that $f(x)$ is a function such that

- $f(n)=a_n$ for all $n \geq 1,$

- $f(x)$ is continuous for $x \geq 1,$ and

- $f(x)$ is differentiable for $x > 1.$

Then,

- if $f'(x) \geq 0$ for $x \gt 1,$ then $a_n$ is *increasing,* and

- if $f'(x) \leq 0$ for $x \gt 1,$ then $a_n$ is *decreasing.*

As an example, let's show that the following sequence is decreasing:

$$


a_n = \dfrac1n, \qquad n\geq 1


$$

Let $f(x) = \dfrac 1x$ for $x\geq 1.$ Now, notice that

- $f(n)=a_n$ for all $n \geq 1,$

- $f(x)$ is continuous for $x \geq 1,$ and

- $f(x)$ is differentiable for $x > 1.$

Taking the derivative, we get

$$


\begin{aligned}𝑓^{′}(𝑥) & =(\frac{1}{𝑥})^{′} \\ & =−\frac{1}{𝑥^{2}}.\end{aligned}


$$

Since $f'(x)$ is negative for $x \gt 1,$ we conclude that $a_n$ is a decreasing sequence.

### Example: Determining Whether a Quadratic Sequence Is Increasing or Decreasing

#### Question

Let $a_n =2 + 3n - n^2$ for $n\geq 1$ and let $f(x) =2 + 3x - x^2.$ Which of the following statements are true?

1. $f'(x) \leq 0$ for all $x > 1$

2. $a_n$ is an increasing sequence

3. $a_n$ is a decreasing sequence

#### Explanation

Suppose the sequence $a_n$ is defined for $n\geq 1,$ and that $f(x)$ is a function such that

- $f(n)=a_n$ for all $n \geq 1,$

- $f(x)$ is continuous for $x \geq 1,$ and

- $f(x)$ is differentiable for $x > 1.$

Then,

- if $f'(x) \geq 0$ for $x \gt 1,$ then $a_n$ is ** and

- if $f'(x) \leq 0$ for $x \gt 1,$ then $a_n$ is **

Notice that, in this case,

- $f(x) = 2 + 3x - x^2$ is continuous for all $x\geq 1,$ and

- $f(n) = a_n$ for all $n\geq 1.$

Now, let's analyze each statement:

- Statement I is false. Taking the derivative, we get Notice that $f'(x)$ is defined for $x > 1,$ so $f(x)$ is differentiable on $x \gt 1.$ Now, solving $f'(x) \leq 0,$ we get Therefore, $f'(x) \leq 0$ for $x \geq \dfrac32,$ and $f'(x) \geq 0$ for $x \leq \dfrac32.$ We summarize our results in the diagram below.

- Statement II is false. Since $f'(x) \ngeq 0$ for all $x > 1,$ the sequence $a_n$ is ** increasing.

- Statement III is false. Since $f'(x) \nleq 0$ for all $x > 1,$ the sequence $a_n$ is ** decreasing.

Therefore, the correct answer is "None of the statements are true."

### Example: Determining Whether a Polynomial Sequence Is Increasing or Decreasing

#### Question

Let $a_n = n^3 - 27n+9$ for $n\geq 1$ and let $f(x) = x^3 - 27x+9.$ Which of the following statements are true?

1. $f'(x) \geq 0$ for all $x > 1$

2. $a_n$ is an increasing sequence

3. $a_n$ is a decreasing sequence

#### Explanation

Suppose the sequence $a_n$ is defined for $n\geq 1,$ and that $f(x)$ is a function such that

- $f(n)=a_n$ for all $n \geq 1,$

- $f(x)$ is continuous for $x \geq 1,$ and

- $f(x)$ is differentiable for $x > 1.$

Then,

- if $f'(x) \geq 0$ for $x \gt 1,$ then $a_n$ is ** and

- if $f'(x) \leq 0$ for $x \gt 1,$ then $a_n$ is **

Notice that, in this case,

- $f(x) = x^3 - 27x+9$ is continuous for all $x\geq 1,$

- $f(n) = a_n$ for all $n\geq 1.$

With that in mind, let's analyze each statement:

- Statement I is false. Taking the derivative, we get Notice that $f'(x)$ is defined for $x > 1,$ so $f(x)$ is differentiable on $x \gt 1.$ Now, solving $f'(x) \geq 0,$ we get Therefore, $f'(x) \geq 0$ for $x \leq -3$ or $x \geq 3,$ $f'(x) \leq 0$ for $-3 \leq x \leq 3.$ We summarize our results in the diagram below.

- Statement II is false. Since $f'(x) \ngeq 0$ for all $x > 1,$ the sequence $a_n$ is ** increasing.

- Statement III is false. Since $f'(x) \nleq 0$ for all $x > 1,$ the sequence $a_n$ is ** decreasing.

Therefore, the correct answer is "None of the statements are true."

### Example: Determining Whether a Rational Sequence Is Increasing or Decreasing

#### Question

Let $a_n = \dfrac n {(n+1)^2}$ for $n\geq 1$ and let $f(x) = \dfrac{x}{(x+1)^2}.$ Which of the following statements are true?

1. $f'(x) \geq 0$ for all $x > 1$

2. $a_n$ is an increasing sequence

3. $a_n$ is a decreasing sequence

#### Explanation

Suppose the sequence $a_n$ is defined for $n\geq 1,$ and that $f(x)$ is a function such that

- $f(n)=a_n$ for all $n \geq 1,$

- $f(x)$ is continuous for $x \geq 1,$ and

- $f(x)$ is differentiable for $x > 1.$

Then,

- if $f'(x) \geq 0$ for $x \gt 1,$ then $a_n$ is ** and

- if $f'(x) \leq 0$ for $x \gt 1,$ then $a_n$ is **

Notice that, in this case,

- $f(x) = \dfrac{x}{(x+1)^2}$ is continuous for all $x\geq 1,$ and

- $f(n) = a_n$ for all $n\geq 1.$

With that in mind, let's analyze each statement:

- Statement I is false. Taking the derivative, we get Notice that $f'(x)$ is defined for $x > 1,$ so $f(x)$ is differentiable on $x \gt 1.$ Now, solving $f'(x) \geq 0,$ we get Therefore, $f'(x) \geq 0$ for $-1 < x \leq 1$. $f'(x) \leq 0$ for $x < -1$ or $x \geq 1.$ We summarize our results in the diagram below.

- Statement II is false. Since $f'(x) \ngeq 0$ for all $x > 1,$ the sequence $a_n$ is ** increasing.

- Statement III is true. Since $f'(x) \leq 0$ for all $x > 1,$ the sequence $a_n$ is decreasing.

Therefore, the correct answer is "III only."
