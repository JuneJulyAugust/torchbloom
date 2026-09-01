# Integrating Exponential Functions Using Linear Substitution

Source: https://www.mathacademy.com/topics/1112?courseId=21
Topic ID: 1112

## Prerequisites

- [Calculating Definite Integrals Using Substitution](../ap-calculus-ab/1159-calculating-definite-integrals-using-substitution.md)

## Lesson

### Introduction

We know how to integrate $e^x,$ but how do we integrate a function like $e^{2x}?$

The answer is to use a substitution. If we let $u=2x,$ then

$$


\dfrac{\textrm d u}{\textrm d x} = 2\quad\Longrightarrow\quad \textrm d x = \dfrac 1 2 \textrm d u.


$$

Now, we can write our original integral in terms of the new variable $u,$ as follows:

$$


\begin{aligned}∫𝑒^{2𝑥}\,d𝑥 & =∫𝑒^{𝑢}⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫𝑒^{𝑢}\,d𝑢 \\ & =\frac{1}{2}𝑒^{𝑢}+𝐶 \\ & =\frac{1}{2}𝑒^{2𝑥}+𝐶.\end{aligned}


$$

After solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}(\frac{1}{2}𝑒^{2𝑥}+𝐶) & =\frac{1}{2}⋅\frac{d}{d𝑥}(𝑒^{2𝑥})+\frac{d}{d𝑥}(𝐶) \\ & =\frac{1}{2}⋅𝑒^{2𝑥}⋅\frac{d}{d𝑥}(2𝑥)+0 \\ & =\frac{1}{2}𝑒^{2𝑥}⋅2 \\ & =𝑒^{2𝑥}\,✓\end{aligned}


$$

### Example: Integrating the Exponential Function With a Linear Exponent

#### Question

Calculate $\displaystyle{\int e^{1-3x}\, \text{d}x}.$

#### Explanation

If we let $u=1-3x,$ then

$$


\dfrac{\textrm d u}{\textrm d x} = -3\quad\Longrightarrow\quad \textrm d x = -\dfrac 1 3 \textrm d u.


$$

Then, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}∫𝑒^{1−3𝑥}\,d𝑥 & =∫𝑒^{𝑢}⋅(−\frac{1}{3})\,d𝑢 \\ & =−\frac{1}{3}∫𝑒^{𝑢}\,d𝑢 \\ & =−\frac{1}{3}𝑒^{𝑢}+𝐶 \\ & =−\frac{1}{3}𝑒^{1−3𝑥}+𝐶\end{aligned}


$$

### Example: Integrating a General Exponential Function With a Linear Exponent

#### Question

Calculate $\displaystyle{\int 3^{5+4x}\, \text{d}x}.$

#### Explanation

If we let $u=5+4x,$ then

$$


\dfrac{\textrm d u}{\textrm d x} = 4\quad\Longrightarrow\quad \textrm d x = \dfrac 1 4 \textrm d u.


$$

Then, we can write the integral in terms of $u$ and evaluate:

$$


\begin{aligned}∫3^{5+4𝑥}\,d𝑥 & =∫3^{𝑢}⋅\frac{1}{4}\,d𝑢 \\ & =\frac{1}{4}∫3^{𝑢}\,d𝑢 \\ & =\frac{1}{4}⋅\frac{3^{𝑢}}{ln⁡3}+𝐶 \\ & =\frac{3^{5+4𝑥}}{4ln⁡3}+𝐶\end{aligned}


$$

### General Formulas for Integrating Exponential Functions With Linear Exponents

If you're comfortable with memorizing formulas, then it's worth noting that

$$


\begin{aligned}∫𝑒^{𝑝𝑥+𝑞}\,d𝑥 & =\frac{1}{𝑝}𝑒^{𝑝𝑥+𝑞}+𝐶, \\ ∫𝑎^{𝑝𝑥+𝑞}\,d𝑥 & =\frac{1}{𝑝ln⁡𝑎}𝑎^{𝑝𝑥+𝑞}+𝐶.\end{aligned}


$$

If you don't like to memorize formulas, you can always use substitution to solve these types of integrals.
