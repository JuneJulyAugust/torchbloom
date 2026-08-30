# Calculating Definite Integrals Using Substitution

Source: https://www.mathacademy.com/topics/1159?courseId=24
Topic ID: 1159

## Prerequisites

- [Integration Using Substitution](./443-integration-using-substitution.md)
- [The Sum and Constant Multiple Rules for Definite Integrals](./1685-the-sum-and-constant-multiple-rules-for-definite-integrals.md)

## Lesson

### Introduction

Suppose that we have the definite integral $\displaystyle\int_1^2 (x-1)^5\,\text{d}x.$ Can we solve it using the method of integration by substitution?

The answer is yes, and the procedure is very similar to the one that we followed for the indefinite integrals. The main difference is that this time, we need to change the limits of integration too. We proceed via three steps, as follows.

**Step 1**: Change of variable in the integrand.

We start by setting the base of the power equal to $u.$ Computing the derivative, we get

$$


\begin{aligned}𝑢 & =𝑥−1 \\ \frac{d𝑢}{d𝑥} & =1 \\ d𝑢 & =d𝑥,\end{aligned}


$$

and substituting, we get

$$


(x-1)^5\,\text{d}x=u^5\,\text{d}u.


$$

**Step 2**: Calculate the new limits.

We now have to change the limits of integration, $x=1$ and $x=2.$ Since we want to express the integral in terms of the new variable, $u,$ we need to change the variable in the limits too.

The lower limit $x=1$ becomes

$$


\begin{aligned}𝑢 & =𝑥−1 \\ 𝑢 & =1−1 \\ 𝑢 & =0,\end{aligned}


$$

while the upper limit $x=2$ becomes

$$


\begin{aligned}𝑢 & =𝑥−1 \\ 𝑢 & =(2)−1 \\ 𝑢 & =1.\end{aligned}


$$

It is useful to use a table like the following when changing limits of integration:

$$


\begin{aligned}𝑥 & 1 & 2 \\ 𝑢 & 0 & 1\end{aligned}


$$

**Step 3**: Solve the integral in the new variable $u,$ using the new limits:

$$


\begin{aligned}∫_{21}(𝑥−1)^{5}\,d𝑥 & =∫_{10}𝑢^{5}\,d𝑢 \\ & =\frac{1}{6}𝑢^{6}_{10} \\ & =\frac{1}{6}(1)^{6}−\frac{1}{6}(0)^{6} \\ & =\frac{1}{6}.\end{aligned}


$$

Note that when applying integration by substitution to definite integrals, there is no need to substitute the variable $x$ back in the final answer. We can simply evaluate it using the new variable $u.$

### Example: Calculating a Definite Integral of Function Using Substitution

#### Question

Calculate the definite integral $\displaystyle\int_{-1}^0 x(x^2+1)^3\,\text{d}x.$

#### Explanation

We start by changing the variable:

$$


\begin{aligned}𝑢 & =𝑥^{2}+1 \\ \frac{d𝑢}{d𝑥} & =2𝑥 \\ d𝑢 & =2𝑥\,d𝑥 \\ \frac{1}{2}d𝑢 & =𝑥\,d𝑥.\end{aligned}


$$

Next, we create a table for the limits of integration using the rule $u=x^2+1.$

$$


\begin{aligned}𝑥 & −1 & 0 \\ 𝑢 & 2 & 1\end{aligned}


$$

So, the integral in terms of the new variable is

$$


\int_{-1}^0 x(x^2+1)^3\,\text{d}x=\int_2^1 u^3\,\cdot \dfrac{1}{2}\text{d}u.


$$

Finally, we can solve it and get

$$


\begin{aligned}∫_{12}𝑢^{3}\,⋅\frac{1}{2}d𝑢 & =\frac{1}{2}∫_{12}𝑢^{3}\,d𝑢 \\ & =\frac{1}{2}⋅\frac{𝑢^{4}}{4}_{12} \\ & =\frac{1}{2}⋅\frac{1^{4}−2^{4}}{4} \\ & =\frac{1}{2}⋅\frac{1−16}{4} \\ & =−\frac{15}{8}.\end{aligned}


$$

****: Note that in this example, when we changed the limits the integral $\displaystyle \int_{-1}^0 \ldots \text{d}x$ became $\displaystyle \int_{2}^1 \ldots \text{d}u.$ When changing the limits, it is important to respect the order in which the limits are applied. The lower limit of the integral in $u$ must correspond to the lower limit of the integral in $x.$ Same for the upper limit.

### Example: Calculating a Definite Integral of a Rational Function Using Substitution

#### Question

Calculate the definite integral $\displaystyle\int_{-1}^2 \dfrac{x^2}{x^3+2}\,\text{d}x.$

#### Explanation

We start by changing the variable:

$$


\begin{aligned}𝑢 & =𝑥^{3}+2 \\ \frac{d𝑢}{d𝑥} & =3𝑥^{2} \\ d𝑢 & =3𝑥^{2}\,d𝑥 \\ \frac{1}{3}d𝑢 & =𝑥^{2}\,d𝑥.\end{aligned}


$$

Next, we create a table for the limits of integration using the rule $u=x^3+2.$

$$


\begin{aligned}𝑥 & −1 & 2 \\ 𝑢 & 1 & 10\end{aligned}


$$

So, the integral in terms of the new variable is

$$


\int_{-1}^2 \dfrac{1}{(x^3+2)}\,x^2\text{d}x=\int_1^{10} \dfrac{1}{u}\,\cdot \dfrac{1}{3}\text{d}u.


$$

Finally, we can solve it and get

$$


\begin{aligned}∫_{101}\frac{1}{𝑢}\,⋅\frac{1}{3}d𝑢 & =\frac{1}{3}∫_{101}\frac{1}{𝑢}\,d𝑢 \\ & =\frac{1}{3}ln⁡(𝑢)_{101} \\ & =\frac{1}{3}(ln⁡(10)−ln⁡(1)) \\ & =\frac{1}{3}ln⁡(10).\end{aligned}


$$
