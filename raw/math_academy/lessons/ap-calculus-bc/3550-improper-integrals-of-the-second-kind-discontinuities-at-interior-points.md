# Improper Integrals of the Second Kind: Discontinuities at Interior Points

Source: https://www.mathacademy.com/topics/3550?courseId=21
Topic ID: 3550

## Prerequisites

- [Improper Integrals of the Second Kind](./759-improper-integrals-of-the-second-kind.md)

## Lesson

### Introduction

Let's take a look at the integral

$$


I = \int_1^5\dfrac 1 {x-2} \,\textrm {d}x.


$$

**Watch out!** In this particular case, it is *incorrect* to say

$$


\int_1^5\dfrac 1 {x-2} \,\textrm {d}x \:{\color{red}\boldsymbol{=}}\: \ln|x-2| \,\Big|_1^5 = \ln 3 - \ln 1 = \ln 3.\quad{\color{red}\times}


$$

This is incorrect because the integrand $\dfrac{1}{x-2}$ has an infinite discontinuity at $x=2,$ and this point lies within the domain of integration! Therefore, we cannot directly apply the first fundamental theorem of calculus.

Instead, what we can do is write the original integral as a sum of improper integrals:

$$


\int_1^5\dfrac 1 {x-2} \,\textrm {d}x = \underbrace{\int_1^2\dfrac 1 {x-2} \,\textrm {d}x}_{I_1} + \underbrace{\int_2^5\dfrac 1 {x-2} \,\textrm {d}x}_{I_2}.


$$

Let's evaluate $I_1\mathbin{:}$

$$


\begin{aligned}∫_{21}^{}\frac{1}{𝑥−2}\,d𝑥 & =\underset{𝑎→2^{−}}{lim}∫_{𝑎1}^{}\frac{1}{𝑥−2}\,d𝑥 \\ & =\underset{𝑎→2^{−}}{lim}ln⁡|𝑥−2|\,_{𝑎1}^{} \\ & =\underset{𝑎→2^{−}}{lim}(ln⁡|𝑎−2|−ln⁡|1−2|) \\ & =\underset{𝑎→2^{−}}{lim}(ln⁡|𝑎−2|−0) \\ & =\underset{𝑎→2^{−}}{lim}(ln⁡|𝑎−2|) \\ & =−∞.\end{aligned}


$$

Since $I_1$ diverges, the integral $I$ also diverges. Since we know that $I$ diverges, there is no need to evaluate $I_2.$

In general, if a function $f(x)$ is continuous on $[a,b]$ *except* at some point $c \in (a,b)$ where it has an infinite discontinuity, then

$$


\int_a^b f(x)\,\textrm d x = \int_a^c f(x)\,\textrm d x + \int_c^b f(x)\,\textrm d x.


$$

The integral on the left-hand side is convergent if and only if both integrals on the right-hand side are convergent. If either integral on the right-hand side diverges, then the integral on the left-hand side also diverges.

### Example: Identifying a Divergent Improper Integral With a Discontinuity at an Interior Point

#### Question

Given the function $f(x) = \dfrac{e^{2x}}{1-e^{2x}},$ which of the following statements are true?

1. $\displaystyle \int_{-1}^0 f(x) \,\textrm d x$ is divergent

2. $\displaystyle \int_{0}^1 f(x) \,\textrm d x$ is divergent

3. $\displaystyle \int_{-1}^1 f(x) \,\textrm d x$ is divergent

#### Explanation

Let's evaluate each integral in turn.

- Statement I is true. To compute the integral, we use the substitution Calculating the integral, we get

- Statement II is true. To compute the integral in statement II, we use the same process as before.

- Statement III is true. We can write down this integral by splitting it over the discontinuity at $x=0,$ as follows: Since both integrals on the right-hand side are divergent, the integral on the left-hand side is divergent, too.

In conclusion, statements I, II, and III are all true.

### Example: Calculating an Improper Integral with a Discontinuity at an Interior Point

#### Question

Find the value of $\displaystyle\int_{-2}^2\frac{1}{\sqrt[3]{x-1}}\textrm{d}x.$

#### Explanation

Notice that the denominator of the integrand vanishes at $x=1.$ Therefore, to evaluate the integral, we need to split it up over the point of discontinuity:

$$


\begin{aligned}∫_{2−2}^{}\frac{1}{\sqrt[√𝑥−1]{3}}d𝑥 & =\underset{𝐼_{1}}{\underset{}{∫_{1−2}^{}\frac{1}{\sqrt[√𝑥−1]{3}}d𝑥}}+\underset{𝐼_{2}}{\underset{}{∫_{21}^{}\frac{1}{\sqrt[√𝑥−1]{3}}d𝑥}}\end{aligned}


$$

Let's evaluate the first integral. Using the substitution $u = x-1,$ we get

$$


\begin{aligned}𝐼_{1} & =∫_{1−2}^{}\frac{1}{\sqrt[√𝑥−1]{3}}d𝑥 \\ & =∫_{0−3}^{}\frac{1}{\sqrt[√𝑢]{3}}d𝑢 \\ & =\underset{𝑎→0^{−}}{lim}∫_{𝑎−3}^{}𝑢^{−1/3}d𝑢 \\ & =\underset{𝑎→0^{−}}{lim}[\frac{3}{2}𝑢^{2/3}]_{𝑎−3}^{} \\ & =\underset{𝑎→0^{−}}{lim}\frac{3}{2}[𝑎^{2/3}−(−3)^{2/3}] \\ & =\frac{3}{2}[(0)^{2/3}−\sqrt[√(−3)^{2}]{3}] \\ & =−\frac{3}{2}\sqrt[√9]{3}.\end{aligned}


$$

Similarly, for $I_2,$ we have

$$


\begin{aligned}𝐼_{2} & =∫_{21}^{}\frac{1}{\sqrt[√𝑥−1]{3}}d𝑥 \\ & =∫_{10}^{}\frac{1}{\sqrt[√𝑢]{3}}d𝑢 \\ & =\underset{𝑎→0^{+}}{lim}∫_{1𝑎}^{}𝑢^{−1/3}d𝑢 \\ & =\underset{𝑎→0^{+}}{lim}[\frac{3}{2}𝑢^{2/3}]_{1𝑎}^{} \\ & =\underset{𝑎→0^{+}}{lim}\frac{3}{2}[1^{2/3}−𝑎^{2/3}] \\ & =\frac{3}{2}[1−0] \\ & =\frac{3}{2}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}∫_{2−2}^{}\frac{1}{\sqrt[√𝑥−1]{3}}d𝑥 & =𝐼_{1}+𝐼_{2} \\ & =−\frac{3}{2}\sqrt[√9]{3}+\frac{3}{2} \\ & =\frac{3}{2}(1−\sqrt[√9]{3}).\end{aligned}


$$
