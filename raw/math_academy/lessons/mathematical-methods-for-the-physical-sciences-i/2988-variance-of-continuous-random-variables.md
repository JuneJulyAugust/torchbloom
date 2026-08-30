# Variance of Continuous Random Variables

Source: https://www.mathacademy.com/topics/2988?courseId=154
Topic ID: 2988

## Prerequisites

- [Variance of Discrete Random Variables](./1388-variance-of-discrete-random-variables.md)
- [Moments of Continuous Random Variables](./2987-moments-of-continuous-random-variables.md)

## Lesson

### Introduction

The **variance** of a continuous random variable is the expected squared difference between the variable and its expected value.

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ the variance is defined as follows:

$$


\begin{aligned}Var[𝑋] & =E[(𝑋−E[𝑋])^{2}] \\ & =∫_{𝑆}(𝑥−E[𝑋])^{2}⋅𝑓(𝑥)\,d𝑥\end{aligned}


$$

In practice, though, it's easier to use the following formula:

$$


\textrm{Var}[X] = \textrm E [X^2] - \textrm E[X]^2


$$

For example, consider the continuous random variable $X$ with the following probability density function:

$$


f(x) = \dfrac{x}{4}, \quad 1 < x < 3


$$

First, we compute $\textrm E[X]{:}$

$$


\begin{aligned}E[𝑋] & =∫_{31}^{}𝑥⋅\frac{𝑥}{4}\,d𝑥 \\ & =∫_{31}^{}\frac{𝑥^{2}}{4}\,d𝑥 \\ & =\frac{𝑥^{3}}{12}_{31}^{} \\ & =\frac{13}{6}\end{aligned}


$$

Then, we compute $\textrm E[X^2]{:}$

$$


\begin{aligned}E[𝑋^{2}] & =∫_{31}^{}𝑥^{2}⋅\frac{𝑥}{4}\,d𝑥 \\ & =∫_{31}^{}\frac{𝑥^{3}}{4}\,d𝑥 \\ & =\frac{𝑥^{4}}{16}_{31}^{} \\ & =5\end{aligned}


$$

Therefore, the variance is given by

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =5−(\frac{13}{6})^{2} \\ & =\frac{11}{36}.\end{aligned}


$$

### Example: Computing the Variance of a Continuous Random Variable Given a Two-Branch PDF

#### Question

The continuous random variable $X$ has the probability density function $f(x)$ stated below. Given that $\textrm E[X] = \dfrac {10}{3},$ compute $\textrm{Var}[X].$

$$


\begin{aligned}8−2𝑥,\, & 3≤𝑥≤4, \\ 0,\, & otherwise.\end{aligned}


$$

#### Explanation

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ we can calculate the variance using the following formula:

$$


\textrm{Var}[X] = \textrm E [X^2] - \textrm E[X]^2


$$

We compute $\textrm E[X^2],$ as follows:

$$


\begin{aligned}E[𝑋^{2}] & =∫_{43}^{}𝑥^{2}⋅(8−2𝑥)\,d𝑥 \\ & =∫_{43}^{}(8𝑥^{2}−2𝑥^{3})\,d𝑥 \\ & =(\frac{8𝑥^{3}}{3}−\frac{𝑥^{4}}{2})_{43}^{} \\ & =\frac{67}{6}\end{aligned}


$$

Therefore, the variance is given by

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =\frac{67}{6}−(\frac{10}{3})^{2} \\ & =\frac{1}{18}.\end{aligned}


$$

### Example: Computing the Variance of a Continuous Random Variable Given a Three-Branch PDF

#### Question

The continuous random variable $X$ has the probability density function given below. Given that $\textrm E[X]\approx 1.791\,67,$ compute $\textrm{Var}[X].$ Round your answer to $2$ decimal places.

$$


\begin{aligned}\frac{1}{4}, & 0<𝑥<2, \\ \frac{𝑥}{2}−\frac{3}{4}, & 2≤𝑥<3, \\ 0,\, & otherwise.\end{aligned}


$$

#### Explanation

For a continuous random variable $X$ with probability density function $f(x)$ defined over a set $S,$ we can calculate the variance using the following formula:

$$


\textrm{Var}[X] = \textrm E [X^2] - \textrm E[X]^2


$$

We compute $\textrm E[X^2]$ as follows:

$$


\begin{aligned}E[𝑋^{2}] & =∫_{30}^{}𝑥^{2}⋅𝑓(𝑥)\,d𝑥 \\ & =∫_{20}^{}𝑥^{2}⋅𝑓(𝑥)\,d𝑥+∫_{32}^{}𝑥^{2}⋅𝑓(𝑥)\,d𝑥 \\ & =∫_{20}^{}𝑥^{2}⋅\frac{1}{4}\,d𝑥+∫_{32}^{}𝑥^{2}⋅(\frac{𝑥}{2}−\frac{3}{4})\,d𝑥 \\ & =∫_{20}^{}\frac{𝑥^{2}}{4}\,d𝑥+∫_{32}^{}(\frac{𝑥^{3}}{2}−\frac{3𝑥^{2}}{4})\,d𝑥 \\ & =\frac{𝑥^{3}}{12}_{20}^{}+(\frac{𝑥^{4}}{8}−\frac{𝑥^{3}}{4})_{32}^{} \\ & ≈4.041\,67\end{aligned}


$$

Therefore, the variance is given by

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & ≈4.041\,67−(1.791\,67)^{2} \\ & ≈0.83\end{aligned}


$$

rounded to $2$ decimal places.
