# Independence of Continuous Random Variables

Source: https://www.mathacademy.com/topics/3863?courseId=73
Topic ID: 3863

## Prerequisites

- [Independence of Discrete Random Variables](./3048-independence-of-discrete-random-variables.md)
- [Marginal Distributions for Continuous Random Variables](./3636-marginal-distributions-for-continuous-random-variables.md)

## Lesson

### Introduction

Let $X$ and $Y$ be continuous random variables. We say that $X$ and $Y$ are **independent** if, for all $A\subseteq \mathbb R$ and $B\subseteq \mathbb R,$ we have

$$


P(X\in A, Y\in B)=P(X\in A)\cdot P(Y\in B).


$$

In practice, this is not a very helpful definition when checking for independence since it involves verifying that it's true for all possible subsets $A$ and $B!$

Now suppose that $X$ and $Y$ have the joint probability density function $f(x,y),$ and $f_X(x)$ and $f_Y(y)$ are the marginal density functions of $X$ and $Y,$ respectively. Then, it can be shown that $X$ and $Y$ are independent if and only if

$$


f(x, y) = f_X(x)\cdot f_Y (y)


$$

for all values of $x$ and $y.$ Notice that this has a direct analogy with the case of independence for discrete random variables.

### Example: Finding the Joint PDF of Two Independent Random Variables Using Marginal PDFs

#### Question

Let $X$ and $Y$ be two independent continuous random variables whose marginal density functions are as follows:

$$


\begin{aligned}\frac{2}{9}𝑥, & \,0≤𝑥≤3, \\ 0, & \,otherwise\end{aligned}


$$

Find the joint probability density function $f(x,y).$

#### Explanation

Two continuous random variables $X$ and $Y$ with joint probability density function $f(x,y)$ are independent if and only if

$$


f(x, y) = f_X(x) \cdot f_Y (y)


$$

for all possible values $x$ and $y,$ where $f_X(x)$ and $f_Y (y)$ are the marginal probability density functions for $X$ and $Y,$ respectively.

Since our random variables are independent, we obtain

$$


\begin{aligned}𝑓(𝑥,𝑦) & =𝑓_{𝑋}(𝑥)⋅𝑓_{𝑌}(𝑦) \\ & =\frac{2}{9}𝑥⋅\frac{1}{4}𝑦^{3} \\ & =\frac{1}{18}𝑥𝑦^{3}\end{aligned}


$$

where $(x,y) \in [0, 3] \times [0, 2].$ Therefore, the full expression for $f(x,y)$ is

$$


\begin{aligned}\frac{1}{18}𝑥𝑦^{3}, & \,0≤𝑥≤3,\,0≤𝑦≤2 \\ 0, & \,otherwise.\end{aligned}


$$

### Example: Finding a Joint Probability for Some Independent Random Variables Using Marginal PDFs

#### Question

Let $X$ and $Y$ be two independent continuous random variables whose marginal density functions are as follows:

$$


\begin{aligned}\frac{10}{3𝑥^{2}}, & \,2≤𝑥≤5, \\ 0, & \,otherwise\end{aligned}


$$

Find $P(X \geq 3, Y \leq 2).$

#### Explanation

Two continuous random variables $X$ and $Y$ with joint probability density function $f(x,y)$ are independent if and only if

$$


f(x, y) = f_X(x) \cdot f_Y (y)


$$

for all possible values $x$ and $y,$ where $f_X(x)$ and $f_Y (y)$ are the marginal probability density functions for $X$ and $Y,$ respectively.

Since our random variables are independent, we obtain

$$


\begin{aligned}𝑓(𝑥,𝑦) & =𝑓_{𝑋}(𝑥)⋅𝑓_{𝑌}(𝑦) \\ & =\frac{10}{3𝑥^{2}}⋅\frac{1}{4}𝑦 \\ & =\frac{5𝑦}{6𝑥^{2}},\end{aligned}


$$

where $(x,y) \in \left[2,5\right]\times \left[1,3\right].$ Therefore, the full expression for $f(x,y)$ is

$$


\begin{aligned}\frac{5𝑦}{6𝑥^{2}}, & \,2≤𝑥≤5,\,1≤𝑦≤3 \\ 0, & \,otherwise.\end{aligned}


$$

Finally, the required probability is

$$


\begin{aligned}𝑃(𝑋≥3,𝑌≤2) & =∫_{53}[∫_{21}\frac{5𝑦}{6𝑥^{2}}\,d𝑦]d𝑥 \\ & =∫_{53}\frac{5}{6𝑥^{2}}[\frac{𝑦^{2}}{2}]_{21}\,d𝑥 \\ & =∫_{53}\frac{5}{6𝑥^{2}}(\frac{3}{2})\,d𝑥 \\ & =∫_{53}\frac{5}{4𝑥^{2}}\,d𝑥 \\ & =[−\frac{5}{4𝑥}]_{53} \\ & =−\frac{5}{4}(\frac{1}{5}−\frac{1}{3}) \\ & =\frac{1}{6}.\end{aligned}


$$

### Example: Determining Whether Two Continuous Random Variables are Independent

#### Question

The joint probability density function for the continuous random variables $X$ and $Y$ is given by

$$


\begin{aligned}\frac{1}{4}𝑥𝑒^{−𝑦/2},\, & 0≤𝑥≤2,\,𝑦≥0, \\ 0,\, & otherwise.\end{aligned}


$$

Which of the following statements are true?

1. $f_Y(y) = \dfrac{1}{2}e^{-y/2}$ for $y\in \left[0,\infty\right)$

2. $f(x, y) = f_X(x) \cdot f_Y (y)$ for all possible $x$ and $y$

3. $X$ and $Y$ are independent

#### Explanation

Two continuous random variables $X$ and $Y$ with a joint probability density function $f(x,y)$ are independent if and only if

$$


f(x, y) = f_X(x) \cdot f_Y (y)


$$

for all possible values $x$ and $y,$ where $f_X(x)$ and $f_Y (y)$ are the marginal probability density functions for $X$ and $Y,$ respectively.

With that in mind, let's examine our statements.

- Statement I is true. Computing the marginal density function for $Y,$ we get where $y \in \left[0,\infty\right).$

- Statement II is true. Computing the marginal density function for $X,$ we get where $x \in \left[0,2\right].$ So, when $x \in \left[0,2\right]$ and $y\in \left[0,\infty\right),$ we obtain that

- Statement III is true. Since statement II is true, our random variables $X$ and $Y$ are independent.

Therefore, the correct answer is "I, II, and III."

### Independence When the Joint Support Is Rectangular

For continuous random variables $X$ and $Y$ whose joint support $S$ is rectangular, we have the following theorem:

*Suppose that the joint support of two continuous random variables $X$ and $Y$ with a joint probability density function $f(x,y)$ is rectangular. If for some two functions $g$ and $h$ (not necessarily probability density functions), then $X$ and $Y$ are independent. Note that the rectangular joint support $S$ does not need to be finite.*

For example, let's consider the random variables $X$ and $Y$ with the following joint PDF:

$$


\begin{aligned}\frac{1}{4}𝑥𝑒^{−𝑦/2},\, & 0≤𝑥≤2,\,𝑦≥0, \\ 0,\, & otherwise.\end{aligned}


$$

The joint support $[0,2]\times [0, \infty)$ is rectangular. Also, we can write $f(x,y) = g(x)\cdot h(y),$ where

$$


g(x) = \dfrac14 x, \qquad h(y) = e^{-y/2}.


$$

Therefore, $X$ and $Y$ are independent.
