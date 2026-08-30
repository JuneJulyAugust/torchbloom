# Further Integration of Algebraic Functions Using Substitution

Source: https://www.mathacademy.com/topics/316?courseId=21
Topic ID: 316

## Prerequisites

- [Calculating Definite Integrals Using Substitution](../ap-calculus-ab/1159-calculating-definite-integrals-using-substitution.md)

## Lesson

### Introduction

At first sight, the integral

$$


\displaystyle \int x \sqrt{x+2} \,\textrm{d}x


$$

might not seem like it can be solved using substitution because $x$ is not the derivative of $x+2.$ But in fact, with some clever manipulation, we can indeed solve it using substitution!

Setting

$$


u=x+2,


$$

and computing the required derivatives gives

$$


\begin{aligned}\frac{d𝑢}{d𝑥}=1\,⟹\,d𝑢=d𝑥.\end{aligned}


$$

Substituting into our integral, we get

$$


\int x \sqrt{x+2} \,\textrm{d}x=\int x \sqrt{u} \,\textrm{d}u.


$$

So we still have an $x$ in our integrand. However, we can get rid of it by solving for $x$ in the rule $u=x+2.$ We get

$$


x=u-2,


$$

and using this, the integral becomes

$$


\begin{aligned}∫𝑥\sqrt{√𝑢}\,d𝑢= & ∫(𝑢−2)\sqrt{√𝑢}\,d𝑢 \\ & =∫(𝑢−2)𝑢^{1/2}\,d𝑢.\end{aligned}


$$

We can now solve the integral by multiplying out the product and integrating the resulting function with respect to $u\mathbin{:}$

$$


\begin{aligned}∫(𝑢−2)𝑢^{1/2}\,d𝑢 & =∫(𝑢^{3/2}−2𝑢^{1/2})\,d𝑢 \\ & =∫𝑢^{3/2}\,d𝑢−2∫𝑢^{1/2}\,d𝑢 \\ & =\frac{2}{5}𝑢^{5/2}−\frac{4}{3}𝑢^{3/2}+𝐶.\end{aligned}


$$

For the final step, we substitute $u=x+2,$ and we get

$$


\begin{aligned}∫𝑥\sqrt{√𝑥+2}\,d𝑥 & =\frac{2}{5}(𝑥+2)^{5/2}−\frac{4}{3}(𝑥+2)^{3/2}+𝐶 \\ & =\frac{2}{5}\sqrt{√(𝑥+2)^{5}}−\frac{4}{3}\sqrt{√(𝑥+2)^{3}}+𝐶.\end{aligned}


$$

### Example: Calculating Indefinite Integrals of Algebraic Functions Using Substitution

#### Question

Calculate $\displaystyle \int x^3\sqrt{x^2 + 1}\, \textrm{d}x.$

#### Explanation

Let $u = x^2+1.$ Then, we have

$$


\begin{aligned}\frac{d𝑢}{d𝑥}=2𝑥\,⟹\,\frac{1}{2}d𝑢=𝑥\,d𝑥.\end{aligned}


$$

We can now solve the integral in terms of $u,$ and then express our final answer in terms of $x\mathbin{:}$

$$


\begin{aligned}∫𝑥^{3}\sqrt{√𝑥^{2}+1}\,d𝑥 & =∫𝑥^{2}⋅𝑥\sqrt{√𝑥^{2}+1}\,d𝑥 \\ & =∫𝑥^{2}\sqrt{√𝑥^{2}+1}\,⋅𝑥\,d𝑥 \\ & =∫\overset{\overset{𝑥^{2}}{}}{𝑢−1}\sqrt{√𝑥^{2}+1}⋅\overset{\overset{𝑥\,d𝑥}{}}{\frac{1}{2}d𝑢} \\ & =∫(𝑢−1)\sqrt{√𝑢}⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫(𝑢−1)𝑢^{1/2}\,d𝑢 \\ & =\frac{1}{2}∫(𝑢^{3/2}−𝑢^{1/2})\,d𝑢 \\ & =\frac{1}{2}(\frac{2}{5}𝑢^{5/2}−\frac{2}{3}𝑢^{3/2})+𝐶 \\ & =\frac{1}{5}(𝑥^{2}+1)^{5/2}−\frac{1}{3}(𝑥^{2}+1)^{3/2}+𝐶 \\ & =\frac{1}{5}\sqrt{√(𝑥^{2}+1)^{5}}−\frac{1}{3}\sqrt{√(𝑥^{2}+1)^{3}}+𝐶\end{aligned}


$$

### Example: Calculating Definite Integrals of Algebraic Functions Using Substitution

#### Question

Evaluate $\displaystyle \int_0^{1/2}x(1-2x)^5\,\textrm d x.$

#### Explanation

Let $u=1-2x.$ Then, we have

$$


\dfrac{\textrm d u}{\textrm d x} = -2\quad\Longrightarrow\quad -\dfrac 1 2 \,\textrm d u = \textrm d x.


$$

We also note that $x = \dfrac 1 2 (1-u).$

Computing our limits of integration, we get

We can now solve the integral using our new variable $u,$ remembering to use the new limits of integration:

$$


\begin{aligned}∫_{1/20}^{}𝑥(1−2𝑥)^{5}\,d𝑥 & =∫_{01}^{}\frac{1}{2}⋅(1−𝑢)⋅𝑢^{5}⋅(−\frac{1}{2})\,d𝑢 \\ & =−\frac{1}{4}∫_{01}^{}(1−𝑢)⋅𝑢^{5}\,d𝑢 \\ & =−\frac{1}{4}∫_{01}^{}(𝑢^{5}−𝑢^{6})\,d𝑢 \\ & =−\frac{1}{4}(\frac{1}{6}𝑢^{6}−\frac{1}{7}𝑢^{7})_{01}^{} \\ & =−\frac{1}{4}([0−0]−[\frac{1}{6}−\frac{1}{7}]) \\ & =−\frac{1}{4}(−\frac{1}{42}) \\ & =\frac{1}{168}\end{aligned}


$$
