# Conditional Expectation for Continuous Random Variables

Source: https://www.mathacademy.com/topics/3057?courseId=145
Topic ID: 3057

## Prerequisites

- [Conditional Distributions for Continuous Random Variables](./3022-conditional-distributions-for-continuous-random-variables.md)
- [Conditional Expectation for Discrete Random Variables](./3053-conditional-expectation-for-discrete-random-variables.md)
- [Expected Values of Continuous Random Variables](./4012-expected-values-of-continuous-random-variables.md)

## Lesson

### Introduction

For continuous random variables $X$ and $Y,$ the **conditional expectation of $X$ given $Y=y$** is defined as

$$


\textrm E[X |Y = y] =\int\limits_{\mathbb R} x \, f_{X|Y}(x|y)\;\textrm dx,


$$

where $f_{X|Y}(x|y)$ is the conditional probability density function of $X$ given $Y.$

This definition is similar to that of $\text{E}[X].$ However, we now use the conditional PDF $f_{X|Y}(x|y)$ instead of the marginal PDF $f_X(x)$ in our integral.

Note the following:

- When we select a particular value of $y,$ the conditional expected value of $X$ given $Y=y$ returns a real number. However, if $y$ is not specified, i.e., $\text{E}[X |Y = y]$ *depends* on $y,$ we have that $\text{E}[X |Y = y]$ gives us a *function* of $y.$

- If $X$ and $Y$ are independent, then $\textrm E[X | Y = y] = \textrm E[X]$ for all $y$.

- We sometimes use the notation $\mu_{X|y}$ to denote $E[X | Y = y].$

- We have an analogous definition for $\textrm E[Y |X = x]\mathbin{:}$ where $f_{Y|X}(y|x)$ is the conditional probability density function of $Y$ given $X.$

### A Worked Example

Let's find the conditional expectation $\text{E}\big[X \,|\, Y=1\big]$ given that the conditional probability density function $f_{X|Y}(x \,|\, 1)$ is given by

$$


\begin{aligned}2(𝑥−1), & 1≤𝑥≤2 \\ 0, & otherwise.\end{aligned}


$$

Applying the formula for the conditional expectation of $X$ given $Y=y,$ we have

$$


\begin{aligned}E[𝑋\,|\,𝑌=1] & =∫_{∞−∞}𝑥\,𝑓_{𝑋|𝑌}(𝑥\,|\,1)\,d𝑥 \\ & =∫_{21}𝑥⋅2(𝑥−1)\,d𝑥 \\ & =∫_{21}2𝑥(𝑥−1)\,d𝑥 \\ & =∫_{21}2𝑥^{2}−2𝑥\,d𝑥 \\ & =[\frac{2𝑥^{3}}{3}−𝑥^{2}]_{21} \\ & =[\frac{2(2)^{3}}{3}−(2)^{2}]−[\frac{2(1)^{3}}{3}−(1)^{2}] \\ & =[\frac{16}{3}−4]−[\frac{2}{3}−1] \\ & =[\frac{16}{3}−\frac{12}{3}]−[\frac{2}{3}−\frac{3}{3}] \\ & =\frac{4}{3}−(−\frac{1}{3}) \\ & =\frac{5}{3}.\end{aligned}


$$

### Example: Calculating a Conditional Expectation From a Conditional PDF

#### Question

$$


\begin{aligned}\frac{3(1+𝑦^{2})}{4}, & \,0≤𝑦≤1 \\ 0, & \,otherwise\end{aligned}


$$

Let $X$ and $Y$ be continuous random variables. Find the conditional expected value $\text{E}\big[Y \,|\, X=1\big]$ given that the conditional probability density function $f_{Y|X}(y \,|\, 1)$ is shown above.

#### Explanation

Recall that the conditional expected value of $Y$ given $X=x$ is defined by

$$


\textrm E\big[ Y \,|\, X = x \big] = \int_{-\infty}^{\infty} y \, f_{Y|X}(y \,|\, x) \; \text{d}y.


$$

Therefore, we obtain

$$


\begin{aligned}E[𝑌\,|\,𝑋=1] & =∫_{∞−∞}𝑦\,𝑓_{𝑌|𝑋}(𝑦\,|\,1)\,d𝑦 \\ & =∫_{10}𝑦⋅\frac{3(1+𝑦^{2})}{4}\,d𝑦 \\ & =\frac{3}{4}∫_{10}(𝑦+𝑦^{3})\,d𝑦 \\ & =\frac{3}{4}[\frac{𝑦^{2}}{2}+\frac{𝑦^{4}}{4}]_{10} \\ & =\frac{3}{4}(\frac{1}{2}+\frac{1}{4}−0) \\ & =\frac{9}{16}.\end{aligned}


$$

### Example: Calculating Conditional Expectations Given Joint and Marginal PDFs

#### Question

$$


\begin{aligned}𝑓(𝑥,𝑦)=\begin{matrix}𝑦−𝑥, & −1≤𝑥≤0,\,0≤𝑦≤1, \\ 0, & otherwise\end{matrix}\,𝑓_{𝑌}(𝑦)=\begin{matrix}\frac{1}{2}+𝑦, & 0≤𝑦≤1, \\ 0, & otherwise\end{matrix}\end{aligned}


$$

Let $X$ and $Y$ be continuous random variables. Their joint probability density function and the marginal probability density function of $Y$ are shown above. Find the conditional expected value $\text{E}\bigg[X \,\bigg|\, Y=\dfrac{1}{2} \bigg].$

#### Explanation

Recall that the conditional expected value of $X$ given $Y=y$ is defined by

$$


\textrm E\big[ X \,|\, Y = y \big] = \int_{-\infty}^{\infty} x \, f_{X|Y}(x \,|\, y) \; \text{d}x.


$$

Note that $\textrm E\big[X \,|\, Y = y \big]$ is a function of $y.$

The conditional density function of $X$ given $Y=y$ can be computed as

$$


\begin{aligned}𝑓_{𝑋|𝑌}(𝑥\,|\,𝑦) & =\frac{𝑓(𝑥,𝑦)}{𝑓_{𝑌}(𝑦)} \\ & =\frac{𝑦−𝑥}{\frac{1}{2}+𝑦} \\ & =\frac{2(𝑦−𝑥)}{1+2𝑦},\end{aligned}


$$

where $-1 \leq x \leq 0, \: 0 \leq y \leq 1.$ Outside this domain, we have $f_{X|Y} (x \,|\, y) = 0.$

Now, substituting $y=\dfrac{1}{2}$ into the expression for $f_{X|Y} (x \,|\, y),$ we get

$$


\begin{aligned}𝑓_{𝑋|𝑌}(𝑥\,\,\frac{1}{2}) & =\frac{2(\frac{1}{2}−𝑥)}{2} \\ & =\frac{1−2𝑥}{2} \\ & =\frac{1}{2}−𝑥.\end{aligned}


$$

Therefore, using the definition of the conditional expectation above, we obtain

$$


\begin{aligned}E[𝑋\,\,𝑌=\frac{1}{2}] & =∫_{∞−∞}𝑥\,𝑓_{𝑋|𝑌}(𝑥\,\,\frac{1}{2})\,d𝑥 \\ & =∫_{0−1}𝑥(\frac{1}{2}−𝑥)d𝑥 \\ & =∫_{0−1}(\frac{𝑥}{2}−𝑥^{2})d𝑥 \\ & =[\frac{𝑥^{2}}{4}−\frac{𝑥^{3}}{3}]_{0−1} \\ & =0−(\frac{1}{4}+\frac{1}{3}) \\ & =−\frac{7}{12}.\end{aligned}


$$

### Example: Conditional Expectation as a Function

#### Question

$$


\begin{aligned}𝑓(𝑥,𝑦)=\begin{matrix}\frac{𝑥+𝑦}{4}, & 0≤𝑦≤𝑥,\,\,0<𝑥<2 \\ 0, & otherwise\end{matrix}\,𝑓_{𝑋}(𝑥)=\begin{matrix}\frac{3𝑥^{2}}{8}, & 0<𝑥<2 \\ 0, & otherwise\end{matrix}\end{aligned}


$$

Let $X$ and $Y$ be continuous random variables. Their joint probability density function and the marginal probability density function of $X$ are shown above. Find the expression for the conditional expected value $\text{E}\big[Y \,|\, X=x\big]$ for $0 < x < 2.$

#### Explanation

Recall that the conditional expected value of $Y$ given $X=x$ is defined by

$$


\textrm E\big[ Y \,|\, X = x \big] = \int_{-\infty}^{\infty} y \, f_{Y|X}(y \,|\, x) \; \text{d}y.


$$

Note that $\textrm E\big[Y \,|\, X = x \big]$ is a function of $x.$

The conditional density function of $Y$ given $X=x$ can be computed as

$$


\begin{aligned}𝑓_{𝑌|𝑋}(𝑦\,|\,𝑥) & =\frac{𝑓(𝑥,𝑦)}{𝑓_{𝑋}(𝑥)} \\ & =\frac{(\frac{𝑥+𝑦}{4})}{4} \\ & =\frac{2(𝑥+𝑦)}{3𝑥^{2}},\end{aligned}


$$

where $0 \leq y \leq x,\; 0 < x < 2.$ Outside this domain, we have $f_{Y|X} (y \,|\, x) = 0.$

Therefore, using the definition of the conditional expectation above, we obtain

$$


\begin{aligned}E[𝑌\,|\,𝑋=𝑥] & =∫_{∞−∞}𝑦\,𝑓_{𝑌|𝑋}(𝑦\,|\,𝑥)\,d𝑦 \\ & =∫_{𝑥0}𝑦⋅\,\frac{2(𝑥+𝑦)}{3𝑥^{2}}\,d𝑦 \\ & =\frac{2}{3𝑥^{2}}∫_{𝑥0}(𝑥𝑦+𝑦^{2})\,d𝑦 \\ & =\frac{2}{3𝑥^{2}}[\frac{𝑥𝑦^{2}}{2}+\frac{𝑦^{3}}{3}]_{𝑥0} \\ & =\frac{2}{3𝑥^{2}}[\frac{𝑥^{3}}{2}+\frac{𝑥^{3}}{3}−0] \\ & =\frac{2}{3𝑥^{2}}⋅\frac{5𝑥^{3}}{6} \\ & =\frac{1}{3𝑥^{2}}⋅\frac{5𝑥^{2}⋅𝑥}{3} \\ & =\frac{1}{3𝑥^{2}}⋅\frac{5𝑥^{2}⋅𝑥}{3} \\ & =\frac{5𝑥}{9}.\end{aligned}


$$
