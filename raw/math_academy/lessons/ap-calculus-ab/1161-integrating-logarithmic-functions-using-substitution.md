# Integrating Logarithmic Functions Using Substitution

Source: https://www.mathacademy.com/topics/1161?courseId=24
Topic ID: 1161

## Prerequisites

- [Calculating Definite Integrals Using Substitution](./1159-calculating-definite-integrals-using-substitution.md)

## Lesson

### Introduction

Let's think about how to calculate an integral like $\displaystyle \int \dfrac {\ln x} {x} \,\textrm d x.$

Notice that this integral can be written as

$$


\int \dfrac {\ln x} {x} \,\textrm d x = \int \underbrace{\ln x}_{u} \cdot\overbrace{\dfrac {1} {x}}^{u'} \,\textrm d x.


$$

We've seen integrals like this before, where the integrand consists of a function $u(x)$ multiplied by its derivative $u'(x).$ Such integrals can be solved by substitution.

So, we let $u = \ln x,$ which gives

$$


\dfrac{\textrm{d}u}{\textrm{d}x}= \dfrac 1 x\quad \Longrightarrow \quad \dfrac 1 x \,\textrm{d}x={\textrm{d}u}.


$$

Therefore, we can calculate our integral as follows:

$$


\begin{aligned} \int \dfrac{\ln x}{x}\, \textrm{d}x &=\int \ln x\cdot \dfrac {1} {x} \,\textrm d x \\\[5pt] & = \int u \, \textrm{d} u \\\[5pt] &= \dfrac{1}{2}u^2 +C \\\[5pt] &= \dfrac{1}{2}\ln^2 x +C\end{aligned}


$$

After solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}(\frac{1}{2}ln^{2}⁡𝑥+𝐶) & =\frac{1}{2}⋅\frac{d}{d𝑥}(ln^{2}⁡𝑥)+\frac{d}{d𝑥}(𝐶) \\ & =\frac{1}{2}⋅\frac{d}{d𝑥}[(ln⁡𝑥)^{2}]+\frac{d}{d𝑥}(𝐶) \\ & =\frac{1}{2}⋅2ln⁡𝑥⋅\frac{d}{d𝑥}(ln⁡𝑥)+0 \\ & =ln⁡𝑥⋅\frac{1}{𝑥} \\ & =\frac{ln⁡𝑥}{𝑥}\,✓\end{aligned}


$$

### Example: Integrating Functions Containing the Natural Logarithm

#### Question

Calculate $\displaystyle{\int \dfrac{3}{x \sqrt{\ln x}} \, \textrm{d}x}.$

#### Explanation

Let's set $u = \ln x.$ Then, we have

$$


\dfrac{\textrm{d}u}{\textrm{d}x}= \dfrac 1 x\quad\Longrightarrow\quad \textrm{d}u=\dfrac 1 x\,{\textrm{d}x}.


$$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}\begin{aligned}∫\frac{3}{𝑥\sqrt{√ln⁡𝑥}}\,d𝑥 & =3∫\frac{1}{\sqrt{√ln⁡𝑥}}⋅\frac{1}{𝑥}\,d𝑥 \\ & =3∫\frac{1}{\sqrt{√𝑢}}\,d𝑢 \\ & =3∫𝑢^{−1/2}\,d𝑢 \\ & =3⋅2𝑢^{1/2}+𝐶 \\ & =6\sqrt{√𝑢}+𝐶 \\ & =6\sqrt{√ln⁡𝑥}+𝐶\end{aligned}\end{aligned}


$$

### Example: Integrating Functions Containing Other Logarithms

#### Question

Calculate the integral $\displaystyle \int \dfrac{\log^2_3 x}{x} \,\textrm d x.$

#### Explanation

Let's rewrite our integral as

$$


\int \dfrac{(\log_3 x)^2 }{x} \,\textrm d x.


$$

Let $u=\log_3 x.$ Differentiating, we get

$$


\dfrac{\textrm d u}{\textrm d x} = \dfrac{1}{x\ln 3}\quad\Longrightarrow\quad\ln 3\,\textrm d u = \dfrac 1 x \textrm d x.


$$

Using the above, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}∫\frac{(log_{3}⁡𝑥)^{2}}{𝑥}\,d𝑥 & =∫(log_{3}⁡𝑥)^{2}⋅\frac{1}{𝑥}\,d𝑥 \\ & =∫𝑢^{2}⋅ln⁡3\,d𝑢 \\ & =ln⁡3∫𝑢^{2}\,d𝑢 \\ & =ln⁡3⋅\frac{1}{3}𝑢^{3}+𝐶 \\ & =\frac{1}{3}ln⁡3(log_{3}⁡𝑥)^{3}+𝐶 \\ & =\frac{1}{3}ln⁡3log_{33}^{}⁡𝑥+𝐶\end{aligned}


$$

### Definite Integrals

Let's evaluate the following definite integral:

$$


\displaystyle{\int_{e}^{e^4} \dfrac{3}{x \sqrt{\ln x}} \, \textrm{d}x }


$$

We'll use the change of variable method, which comprises three steps:

**Step 1:** Change the variable.

Let's introduce the new variable $u = \ln x.$ Differentiating gives

$$


\dfrac{\textrm{d}u}{\textrm{d}x} = \dfrac{1}{x} \qquad\Longrightarrow\qquad \textrm{d}u = \dfrac{\textrm{d}x}{x}.


$$

**Step 2:** Find the new limits of integration.

We use the table below to change our limits of integration from $x$ to $u{:}$

**Step 3:** Evaluate the integral in the new variable $u.$

$$


\begin{aligned}∫_{𝑒^{4}𝑒}^{}\frac{3}{𝑥\sqrt{√ln⁡𝑥}}\,d𝑥 & =∫_{𝑒^{4}𝑒}^{}\frac{3}{\sqrt{√ln⁡𝑥}}⋅\frac{d𝑥}{𝑥} \\ & =∫_{41}^{}\frac{3}{\sqrt{√𝑢}}⋅d𝑢 \\ & =3∫_{41}^{}𝑢^{−1/2}\,d𝑢 \\ & =6𝑢^{1/2}\,_{41}^{} \\ & =6(\sqrt{√4}−\sqrt{√1}) \\ & =6(2−1) \\ & =6.\end{aligned}


$$

### Example: Evaluating Definite Integrals

#### Question

Evaluate $\displaystyle{\int_{e}^{e^2} \dfrac{\ln^2 x}{x}\,\textrm{d}x}.$

#### Explanation

Let's set $u = \ln x.$ Then, we have

$$


\dfrac{\textrm{d}u}{\textrm{d}x}= \dfrac 1 x\quad\Longrightarrow\quad \textrm{d}u=\dfrac 1 x\,{\textrm{d}x}.


$$

Calculating the limits for $u$ gives the following:

We now substitute and evaluate as follows:

$$


\begin{aligned} \int_{e}^{e^2} \dfrac{\ln^2 x}{x}\,\textrm{d}x &= \int_{e}^{e^2} (\ln x)^2\cdot \dfrac{\textrm{d}x}{x}\\\[5pt] &=\int_{1}^{2} u^2\,\textrm{d}u\\\[5pt] &=\left.\dfrac13u^{3}\right|_{1}^{2}\\\[5pt] &=\dfrac{1}{3}\left(2^3-1^3 \right)\\\[5pt] &=\dfrac{1}{3}\left(8-1 \right)\\\[5pt] &=\dfrac{7}{3} \end{aligned}


$$
