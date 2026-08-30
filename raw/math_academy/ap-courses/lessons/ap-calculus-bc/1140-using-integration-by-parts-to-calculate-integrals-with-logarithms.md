# Using Integration by Parts to Calculate Integrals With Logarithms

Source: https://www.mathacademy.com/topics/1140?courseId=21
Topic ID: 1140

## Prerequisites

- [Introduction to Integration by Parts](./317-introduction-to-integration-by-parts.md)

## Lesson

### Introduction

Suppose that we want to evaluate the integral

$$


\int x\ln{x}\, \textrm{d}x \,.


$$

The method of integration by parts can help us solve this problem. Let's remind ourselves of the "by-parts" formula,

$$


\int u v' \textrm{d}x = uv - \int v u'\textrm{d}x.


$$

We usually let $u = x,$ but that would leave us with $v' = \ln(x)$ which is hard to integrate. So instead, we're going to choose our $u$ and $v'$ slightly differently, as follows:

$$


\begin{aligned}𝑢=ln⁡𝑥\, & ⟹\,𝑢^{′}=\frac{1}{𝑥} \\ 𝑣^{′}=𝑥\, & ⟹\,𝑣=\frac{1}{2}𝑥^{2}.\end{aligned}


$$

Now the formula of integration by parts gives

$$


\begin{aligned}∫𝑥\,ln⁡𝑥\,d𝑥 & =∫\underset{𝑢}{\underset{}{ln⁡𝑥}}⋅\underset{𝑣^{′}}{\underset{}{𝑥}}\,d𝑥 \\ & =ln⁡𝑥⋅\frac{1}{2}\,𝑥^{2}−∫\frac{1}{2}𝑥^{2}⋅\frac{1}{𝑥}d𝑥 \\ & =\frac{1}{2}\,𝑥^{2}ln⁡𝑥−\frac{1}{2}∫𝑥d𝑥 \\ & =\frac{1}{2}\,𝑥^{2}ln⁡𝑥−\frac{1}{4}𝑥^{2}+𝐶.\end{aligned}


$$

When we apply integration by parts to integrals containing logarithmic functions, we should *always* identify the logarithmic function with $u,$ not with $v'.$

### Example: Using Integration by Parts to Compute an Integral Containing a Natural Logarithm

#### Question

Evaluate $\displaystyle \int_{1}^{e} 4x\ln\left(x^3\right) \textrm{d}x.$

#### Explanation

We will solve this problem using integration by parts. We start by defining $u$ and $v',$ as follows:

$$


\begin{aligned}𝑢=ln⁡(𝑥^{3})\, & ⟹\,𝑢^{′}=\frac{1}{𝑥^{3}}⋅3𝑥^{2}=\frac{3}{𝑥} \\ 𝑣^{′}=4𝑥\, & ⟹\,𝑣=∫4𝑥\,d𝑥=2𝑥^{2}\end{aligned}


$$

Using the formula of integration by parts, we get

$$


\begin{aligned}∫_{𝑒1}^{}4𝑥ln⁡(𝑥^{3})d𝑥 & =∫_{𝑒1}^{}𝑢𝑣^{′}d𝑥 \\ & =𝑢𝑣_{𝑒1}^{}−∫_{𝑒1}^{}𝑣𝑢^{′}d𝑥 \\ & =ln⁡(𝑥^{3})⋅(2𝑥^{2})_{𝑒1}^{}−∫_{𝑒1}^{}(2𝑥^{2})⋅\frac{3}{𝑥}\,d𝑥 \\ & =[2(𝑒)^{2}ln⁡(𝑒^{3})−2(1)^{2}ln⁡(1^{3})]−6∫_{𝑒1}^{}𝑥d𝑥 \\ & =6𝑒^{2}−6(\frac{1}{2}\,𝑥^{2})_{𝑒1}^{} \\ & =6𝑒^{2}−3𝑥^{2}_{𝑒1}^{} \\ & =6𝑒^{2}−3(𝑒^{2}−1^{2}) \\ & =3𝑒^{2}+3.\end{aligned}


$$

### Example: Using Integration by Parts to Compute an Integral Containing an Arbitrary Logarithm

#### Question

Calculate $\displaystyle \int \dfrac{\log_4{x}}{x^3} \,\textrm{d}x.$

#### Explanation

We define

$$


\begin{aligned}𝑢=log_{4}⁡𝑥\, & ⟹\,𝑢^{′}=\frac{1}{𝑥ln⁡4} \\ 𝑣^{′}=\frac{1}{𝑥^{3}}\, & ⟹\,𝑣=∫\frac{1}{𝑥^{3}}\,d𝑥=−\,\frac{1}{2𝑥^{2}}\,.\end{aligned}


$$

Using the formula of integration by parts, we get

$$


\begin{aligned}∫\frac{log_{4}⁡𝑥}{𝑥^{3}}\,d𝑥 & =∫𝑢𝑣^{′}d𝑥 \\ & =𝑢𝑣−∫𝑣𝑢^{′}\,d𝑥 \\ & =log_{4}⁡𝑥(−\,\frac{1}{2𝑥^{2}})−∫(−\,\frac{1}{2𝑥^{2}})\frac{1}{𝑥ln⁡4}\,d𝑥 \\ & =−\frac{1}{2𝑥^{2}}\,log_{4}⁡𝑥+\frac{1}{2ln⁡4}∫\frac{1}{𝑥^{3}}\,d𝑥 \\ & =−\frac{ln⁡𝑥}{2𝑥^{2}ln⁡4}+\frac{1}{2ln⁡4}(−\,\frac{1}{2𝑥^{2}})+𝐶 \\ & =−\frac{ln⁡𝑥}{2𝑥^{2}ln⁡4}−\frac{1}{4𝑥^{2}ln⁡4}+𝐶 \\ & =−\frac{2ln⁡𝑥+1}{4𝑥^{2}ln⁡4}+𝐶,\end{aligned}


$$

Note that in the above calculation we used the change of base formula $\log_4{x}=\dfrac{\ln{x}}{\ln{4}}.$

### Example: Using Integration by Parts to Compute an Integral Containing a Single Logarithmic Factor

#### Question

Calculate $\displaystyle \int \ln{x}\,\textrm{d}x.$

#### Explanation

At first, it may not look like we have two factors. Actually, we do, but one of them is implicit. The trick is to write the integral as

$$


\int \ln{x}\,\textrm{d}x = \int \ln{x} \cdot 1 \cdot \textrm{d}x.


$$

Using this trick, we can now use integration by parts. We let

$$


\begin{aligned}𝑢=ln⁡𝑥\, & ⟹\,𝑢^{′}=\frac{1}{𝑥} \\ 𝑣^{′}=1\, & ⟹\,𝑣=𝑥.\end{aligned}


$$

Now, using the by-parts formula, we get

$$


\begin{aligned}∫ln⁡𝑥\,d𝑥 & =𝑥ln⁡𝑥−∫𝑥⋅\frac{1}{𝑥}\,d𝑥 \\ & =𝑥ln⁡𝑥−∫1\,d𝑥 \\ & =𝑥ln⁡𝑥−𝑥+𝐶 \\ & =𝑥(ln⁡𝑥−1)+𝐶.\end{aligned}


$$
