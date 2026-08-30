# Improper Integrals of the Second Kind

Source: https://www.mathacademy.com/topics/759?courseId=136
Topic ID: 759

## Prerequisites

- [Integration by Substitution With Inverse Trigonometric Functions](./315-integration-by-substitution-with-inverse-trigonometric-functions.md)
- [Integrating Trigonometric Functions Using Substitution](./478-integrating-trigonometric-functions-using-substitution.md)
- [Integrating Exponential Functions Using Substitution](./3770-integrating-exponential-functions-using-substitution.md)

## Lesson

### Introduction

An **improper integral of the second kind** is the integral of the form

$$


\displaystyle \int_{\color{red}{a}}^{\color{blue}{b}} f(x)\,\textrm d x


$$

where the integration limits $\color{red}a$ and $\color{blue}b$ are both finite, and the function $f(x)$ is unbounded as we approach one of these limits.

For instance, the definite integral

$$


\int_{\color{red}{0}}^{\color{blue}{1}}\frac{1}{\sqrt{x}}\textrm{d}x


$$

is an improper integral of the second kind because

- both limits ($\color{red}0$ and $\color{blue}1$) are finite, and

- the function under the integral is unbounded as we approach one of the limits (the *lower* limit in this case):

Let's look at some examples of integrals that are *not* improper integrals of the second kind:

- For the integral the upper limit is infinite. Therefore, it is *not* an improper integral of the second kind.

- For the integral the function $f(x)$ under the integral is finite at both limits: Therefore, it is *not* an improper integral of the second kind.

### Example: Identifying Improper Integrals of the Second Kind

#### Question

Which of the following is an improper integral of the second kind?

1. $\displaystyle \int_{0}^{\infty} \dfrac{\text{d}x}{x-2}\qquad$ II. $\displaystyle \int_{-2}^{0} \dfrac{\text{d}x}{x+2}\qquad$ III. $\displaystyle \int_{2}^{3} \dfrac{\text{d}x}{x^2-1}$

#### Explanation

Let's examine each of the given integrals.

- Integral I is an improper integral over an ** domain since its upper limit is infinite. So, it is not an improper integral of the second kind.

- Integral II is an improper integral of the second kind since it has finite limits, and

- Integral III is not an improper integral since it has finite limits, and the function under the integral is finite at every point $x\in[2,3].$

Therefore, the correct answer is "II only."

### Improper Integrals of the Second Kind: Rewriting the Lower Limit

Let's once again consider the following improper integral:

$$


I = \int_{\color{red}{0}}^{\color{blue}1}\frac{1}{\sqrt{x}}\textrm{d}x


$$

The function under the integral is unbounded as we approach the *lower* integration limit from any point that lies in the interval $x\in ({\color{red}{0}},{\color{blue}{1}})\mathbin{:}$

$$


f(x) = \frac{1}{\sqrt{x}} \rightarrow \infty \quad\textrm{ as }\quad x\rightarrow {\color{red}0}^+


$$

We can attempt to evaluate this integral by integrating $f(x)$ over the interval $x\in [a, 1]$ for some parameter $a\in ({\color{red}{0}},{\color{blue}{1}})$ and taking the limit as $a\to{\color{red}0}^+\mathbin{:}$

$$


I = \lim_{a\to{\color{red}0}^+} \int_a^1 \frac{1}{\sqrt{x}}\textrm{d}x


$$

### Improper Integrals of the Second Kind: Rewriting the Upper Limit

Now let's consider the following improper integral:

$$


I = \int_{\color{red}0}^{\color{blue}{2}}\frac{1}{\sqrt[3]{x-2}}\textrm{d}x


$$

The function under the integral is unbounded as we approach the *upper* integration limit from any point that lies in the interval $x\in ({\color{red}{0}},{\color{blue}{2}})$

$$


f(x) = \frac{1}{\sqrt[3]{x-2}} \rightarrow -\infty \quad\textrm{ as }\quad x\rightarrow {\color{blue}2}^-


$$

We can attempt to evaluate this integral by integrating $f(x)$ over the interval $x\in [0, b]$ for some parameter $b\in ({\color{red}{0}},{\color{blue}{2}})$ and taking the limit as $b\to{\color{blue}2}^-\mathbin{:}$

$$


I = \lim_{b\to{\color{blue}2}^-} \int_{0}^b \frac{1}{\sqrt[3]{x-2}}\textrm{d}x


$$

### Example: Rewriting One of the Limits of an Improper Integral

#### Question

Rewrite the improper integral $\displaystyle {\int_{0}^{1} \dfrac{\textrm{d}x}{x^2-1}}$ as the limit of definite integral.

#### Explanation

This is an improper integral of the second kind because the function under the integral is unbounded as we approach the ** integration limit from any point that lies in the interval $x\in (0,{\color{blue}{1}})\mathbin{:}$

$$


f(x) = \dfrac {1}{x^2-1} \rightarrow -\infty\quad \textrm{as}\quad x\rightarrow {\color{blue}{1}} ^-


$$

We can attempt to evaluate this integral by integrating $f(x)$ over the interval $x\in [0, b]$ and taking the limit as $b\to{\color{blue}1}^-\mathbin{:}$

$$


\displaystyle {\int_{0}^{1} \dfrac{\textrm{d}x}{x^2-1}} = \lim\limits_{b \to {\color{blue}{1}}^-} \left( \displaystyle {\int_{0}^{b} \dfrac{\textrm{d}x}{x^2-1}} \right)


$$

### Evaluating Improper Integrals of the Second Kind

We've seen how to construct improper integrals of the second kind. Now, let's learn how to evaluate them.

As an example, let's consider the following integral:

$$


\int_0^1 \frac{\textrm d x}{\sqrt{1-x^2}}


$$

This is an improper integral of the second kind because the function is unbounded at the upper limit of integration:

$$


f(x) = \frac{1}{\sqrt{1-x^2}} \rightarrow \infty \quad\textrm{ as }\quad x\rightarrow 1^-


$$

Nonetheless, it is possible to evaluate the integral by setting the upper bound equal to some parameter $b,$ integrating as usual, and then taking the limit as $b\to 1^-.$

$$


\begin{aligned}∫_{10}^{}\frac{1}{\sqrt{√1−𝑥^{2}}}d𝑥 & =\underset{𝑏→1^{−}}{lim}∫_{𝑏0}^{}\frac{1}{\sqrt{√1−𝑥^{2}}}d𝑥 \\ & =\underset{𝑏→1^{−}}{lim}arcsin⁡𝑥_{𝑏0}^{} \\ & =\underset{𝑏→1^{−}}{lim}[arcsin⁡𝑏−arcsin⁡0] \\ & =\underset{𝑏→1^{−}}{lim}[arcsin⁡𝑏−0] \\ & =\underset{𝑏→1^{−}}{lim}arcsin⁡𝑏 \\ & =arcsin⁡(1) \\ & =\frac{𝜋}{2}\end{aligned}


$$

Therefore, we conclude that

$$


\int_0^1 \frac{\textrm d x}{\sqrt{1-x^2}} = \dfrac{\pi}{2}.


$$

If the limit is infinite or does not exist, we say that the integral is **divergent**. Let's see an example.

### Example: Evaluating an Improper Integral of the Second Kind

#### Question

Evaluate $\displaystyle\int_0^{\pi/2}\tan x\,\textrm d x.$

#### Explanation

First, let's rewrite the integral using a substitution. Let $u = \cos x.$ Then, we have

$$


\dfrac{\textrm d u}{\textrm d x} = -\sin x \quad\Longrightarrow\quad -\textrm d u = \sin x\,\textrm d x.


$$

We use the table below to change the limits:

Carrying out the change of variable, we have

$$


\begin{aligned}∫_{𝜋/20}^{}tan⁡𝑥\,d𝑥 & =∫_{𝜋/20}^{}\frac{sin⁡𝑥}{cos⁡𝑥}\,d𝑥 \\ & =∫_{𝜋/20}^{}\frac{sin⁡𝑥\,d𝑥}{cos⁡𝑥} \\ & =∫_{01}^{}\frac{−d𝑢}{𝑢} \\ & =−∫_{01}^{}\frac{d𝑢}{𝑢} \\ & =∫_{10}^{}\frac{d𝑢}{𝑢}.\end{aligned}


$$

This is an improper integral of the second kind because the function under the integral is unbounded at the ** limit of integration.

$$


f(u) = \dfrac{1}{u} \rightarrow \infty \quad\textrm{ as }\quad u\rightarrow 0^+.


$$

Nonetheless, it is possible to calculate the integral by setting the ** bound equal to some parameter $a,$ integrating as usual, and then taking the limit as $a\to0^+.$

$$


\begin{aligned}∫_{10}^{}\frac{d𝑢}{𝑢} & =\underset{𝑎→0^{+}}{lim}∫_{1𝑎}^{}\frac{d𝑢}{𝑢} \\ & =\underset{𝑎→0^{+}}{lim}ln⁡|𝑢||_{1𝑎}^{} \\ & =\underset{𝑎→0^{+}}{lim}[ln⁡|1|−ln⁡|𝑎|] \\ & =\underset{𝑎→0^{+}}{lim}[0−ln⁡|𝑎|] \\ & =−(−∞) \\ & =∞\end{aligned}


$$

Therefore, we conclude that the integral is divergent.
