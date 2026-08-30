# L'Hopital's Rule Applied to Tables

Source: https://www.mathacademy.com/topics/1210?courseId=21
Topic ID: 1210

## Prerequisites

- [L'Hopital's Rule](../ap-calculus-ab/463-l-hopital-s-rule.md)
- [Calculating Derivatives From Graphs Using the Chain Rule](../ap-calculus-ab/4057-calculating-derivatives-from-graphs-using-the-chain-rule.md)

## Lesson

### Introduction

The function $f(x)$ is differentiable on an open interval containing $x=2.$ The values of $f$ and $f'$ are given in the following table:

Let's find

$$


\lim\limits_{x \to 2} \dfrac{f(x)}{x^3-8}.


$$

Notice that if we try to substitute $x=2$ directly into the limit, we reach the indeterminate form $\dfrac{0}{0}.$

$$


\begin{aligned}\underset{𝑥→2}{lim}\frac{𝑓(𝑥)}{𝑥^{3}−8} & =\frac{𝑓(𝑥)}{𝑥^{3}−8}_{𝑥=2} \\ & =\frac{𝑓(2)}{2^{3}−8} \\ & =\frac{0}{8−8} \\ & =\frac{0}{0}\end{aligned}


$$

So, we use L'Hopital's rule:

$$


\begin{aligned}\underset{𝑥→2}{lim}\frac{𝑓(𝑥)}{𝑥^{3}−8} & =\underset{𝑥→2}{lim}\frac{(𝑓(𝑥))^{′}}{(𝑥^{3}−8)^{′}} \\ & =\underset{𝑥→2}{lim}\frac{𝑓^{′}(𝑥)}{3𝑥^{2}}\end{aligned}


$$

We substitute $x=2$ again, and this time, we are able to determine the result:

$$


\begin{aligned}\underset{𝑥→2}{lim}\frac{𝑓^{′}(𝑥)}{3𝑥^{2}} & =\frac{𝑓^{′}(𝑥)}{3𝑥^{2}}_{𝑥=2} \\ & =\frac{𝑓^{′}(2)}{3⋅2^{2}} \\ & =\frac{4}{3⋅2^{2}−0} \\ & =\frac{1}{3}\end{aligned}


$$

Therefore, $\lim\limits_{x \to 2} \dfrac{f(x)}{x^3-8}=\dfrac{1}{3}.$

### Example: Determining the Limit of a Function Given as a Table of Values Using L'Hopital's Rule

#### Question

The functions $f(x)$ and $g(x)$ are differentiable on an open interval containing $x=1.$ The values of $f,$ $g,$ and their respective derivatives are shown in the following table:

Find $\lim\limits_{x \to 1} \dfrac{f(x)\ln x}{x - g(x)}.$

#### Explanation

Notice that if we try to substitute $x=1$ directly into the limit, we reach the indeterminate form $\dfrac{0}{0}.$

$$


\begin{aligned}\underset{𝑥→1}{lim}\frac{𝑓(𝑥)ln⁡𝑥}{𝑥−𝑔(𝑥)} & =\frac{𝑓(𝑥)ln⁡𝑥}{𝑥−𝑔(𝑥)}_{𝑥=1} \\ & =\frac{𝑓(1)ln⁡1}{1−𝑔(1)} \\ & =\frac{(−2)⋅0}{1−1} \\ & =\frac{0}{0}\end{aligned}


$$

So, we use L'Hopital's rule:

$$


\begin{aligned}\underset{𝑥→1}{lim}\frac{𝑓(𝑥)ln⁡𝑥}{𝑥−𝑔(𝑥)} & =\underset{𝑥→1}{lim}\frac{(𝑓(𝑥)ln⁡𝑥)^{′}}{(𝑥−𝑔(𝑥))^{′}} \\ & =\underset{𝑥→1}{lim}\frac{𝑓^{′}(𝑥)ln⁡𝑥+\frac{𝑓(𝑥)}{𝑥}}{𝑥}\end{aligned}


$$

We substitute $x=1$ again, and this time, we are able to determine the result:

$$


\begin{aligned}\underset{𝑥→1}{lim}\frac{𝑓^{′}(𝑥)ln⁡𝑥+\frac{𝑓(𝑥)}{𝑥}}{𝑥} & =\frac{𝑓^{′}(𝑥)ln⁡𝑥+\frac{𝑓(𝑥)}{𝑥}}{𝑥}_{𝑥=1} \\ & =\frac{𝑓^{′}(1)ln⁡1+\frac{𝑓(1)}{1}}{1} \\ & =\frac{(−5)⋅0+(−2)}{1−0} \\ & =−2\end{aligned}


$$

Therefore, $\lim\limits_{x \to 1} \dfrac{f(x)\ln x}{x-g(x)}=-2.$

### Example: Determining the Limit of a Function Given as a Table of Values Using L'Hopital's Rule Twice

#### Question

The functions $f(x)$ and $g(x)$ are twice-differentiable on an open interval containing $x=-3.$ The values of $f,$ $g,$ and their respective derivatives are given below:

Find $\lim\limits_{x \to -3} \dfrac{f(x)-1}{x-g(x)}.$

#### Explanation

Notice that if we try to substitute $x=-3$ directly into the limit, we reach the indeterminate form $\dfrac{0}{0}.$

$$


\begin{aligned}\underset{𝑥→−3}{lim}\frac{𝑓(𝑥)−1}{𝑥−𝑔(𝑥)} & =\frac{𝑓(𝑥)−1}{𝑥−𝑔(𝑥)}_{𝑥=−3} \\ & =\frac{𝑓(−3)−1}{(−3)−𝑔(−3)} \\ & =\frac{1−1}{(−3)−(−3)} \\ & =\frac{0}{0}\end{aligned}


$$

So, we use L'Hopital's rule:

$$


\begin{aligned}\underset{𝑥→−3}{lim}\frac{𝑓(𝑥)−1}{𝑥−𝑔(𝑥)} & =\underset{𝑥→−3}{lim}\frac{(𝑓(𝑥)−1)^{′}}{(𝑥−𝑔(𝑥))^{′}} \\ & =\underset{𝑥→−3}{lim}\frac{𝑓^{′}(𝑥)}{1−𝑔^{′}(𝑥)}\end{aligned}


$$

We substitute $x=-3$ again, but once more, we reach the indeterminate form $\dfrac{0}{0}.$

$$


\begin{aligned}\underset{𝑥→−3}{lim}\frac{𝑓^{′}(𝑥)}{1−𝑔^{′}(𝑥)} & =\frac{𝑓^{′}(𝑥)}{1−𝑔^{′}(𝑥)}_{𝑥=−3} \\ & =\frac{𝑓^{′}(−3)}{1−𝑔^{′}(−3)} \\ & =\frac{0}{1−1} \\ & =\frac{0}{0}\end{aligned}


$$

But that's okay, because we can just apply L'Hopital's rule again! We get

$$


\begin{aligned}\underset{𝑥→−3}{lim}\frac{𝑓^{′}(𝑥)}{1−𝑔^{′}(𝑥)} & =\underset{𝑥→−3}{lim}\frac{(𝑓^{′}(𝑥))^{′}}{(1−𝑔^{′}(𝑥))^{′}} \\ & =−\underset{𝑥→−3}{lim}\frac{𝑓^{″}(𝑥)}{𝑔^{″}(𝑥)},\end{aligned}


$$

and this time, when we substitute $x=-3,$ we are actually able to determine the result:

$$


\begin{aligned}−\underset{𝑥→−3}{lim}\frac{𝑓^{″}(𝑥)}{𝑔^{″}(𝑥)} & =−\frac{𝑓^{″}(𝑥)}{𝑔^{″}(𝑥)}_{𝑥=−3} \\ & =−\frac{𝑓^{″}(−3)}{𝑔^{″}(−3)} \\ & =−\frac{4}{1} \\ & =−4.\end{aligned}


$$

Therefore, $\lim\limits_{x \to -3} \dfrac{f(x)-1}{x-g(x)}=-4.$
