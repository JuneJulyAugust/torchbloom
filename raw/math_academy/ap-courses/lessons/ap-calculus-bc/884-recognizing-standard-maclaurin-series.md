# Recognizing Standard Maclaurin Series

Source: https://www.mathacademy.com/topics/884?courseId=21
Topic ID: 884

## Prerequisites

- [Representing Functions as Power Series](./885-representing-functions-as-power-series.md)

## Lesson

### Introduction

Consider the infinite sum

$$


1 + 7 + \dfrac{7^2}{2!} + \dfrac{7^3}{3!} + \cdots + \dfrac{7^n}{n!} + \cdots\,.


$$

By examining the series, we recognize that it looks similar to the Maclaurin expansion for $f(x) = e^x\mathbin{:}$

$$


\begin{aligned}𝑒^{𝑥} & =1+𝑥+\frac{𝑥^{2}}{2!}+\frac{𝑥^{3}}{3!}+⋯+\frac{𝑥^{𝑛}}{𝑛!}+⋯ \\ & =1+\phantom{x}+\frac{\phantom{x}^{2}}{2!}+\frac{\phantom{x}^{3}}{3!}+⋯+\frac{\phantom{x}^{𝑛}}{𝑛!}+⋯\,.\end{aligned}


$$

Now, substituting $x=7$ into our Maclaurin expansion gives

$$


\begin{aligned}𝑒^{7} & =1+(7)+\frac{(7)^{2}}{2!}+\frac{(7)^{3}}{3!}+⋯+\frac{(7)^{𝑛}}{𝑛!}+⋯ \\ 𝑒^{7} & =1+7+\frac{7^{2}}{2!}+\frac{7^{3}}{3!}+⋯+\frac{7^{𝑛}}{𝑛!}+⋯\,.\end{aligned}


$$

Therefore, the sum of the series is $e^7.$

### A List of Standard Maclaurin Series

We need to recognize when a particular series looks like a standard Maclaurin series. A list of some common Maclaurin series is given below.

$$


\begin{aligned} & \frac{1}{1−𝑥}=1+𝑥+𝑥^{2}+⋯+𝑥^{𝑛}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑥^{𝑛}, & & 𝑥∈(−1,1) \\ & \frac{1}{1+𝑥}=1−𝑥+𝑥^{2}−⋯+(−1)^{𝑛}𝑥^{𝑛}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(−1)^{𝑛}𝑥^{𝑛}, & & 𝑥∈(−1,1) \\ & 𝑒^{𝑥}=1+𝑥+\frac{1}{2!}𝑥^{2}+⋯+\frac{𝑥^{𝑛}}{𝑛!}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}\frac{𝑥^{𝑛}}{𝑛!}, & & 𝑥∈(−∞,∞) \\ & ln⁡(1+𝑥)=𝑥−\frac{1}{2}𝑥^{2}+\frac{1}{3}𝑥^{3}−⋯+\frac{(−1)^{𝑛+1}𝑥^{𝑛}}{𝑛}+⋯=\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{(−1)^{𝑛+1}𝑥^{𝑛}}{𝑛}, & & 𝑥∈(−1,1] \\ & sin⁡(𝑥)=𝑥−\frac{1}{3!}𝑥^{3}+\frac{1}{5!}𝑥^{5}+⋯+\frac{(−1)^{𝑛}𝑥^{2𝑛+1}}{(2𝑛+1)!}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}\frac{(−1)^{𝑛}𝑥^{2𝑛+1}}{(2𝑛+1)!}, & & 𝑥∈(−∞,∞) \\ & cos⁡(𝑥)=1−\frac{1}{2!}𝑥^{2}+\frac{1}{4!}𝑥^{4}−⋯+\frac{(−1)^{𝑛}𝑥^{2𝑛}}{(2𝑛)!}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}\frac{(−1)^{𝑛}𝑥^{2𝑛}}{(2𝑛)!}, & & 𝑥∈(−∞,∞)\end{aligned}


$$

In this lesson, we will focus on recognizing the standard Maclaurin series for the geometric series, the exponential function, and the natural logarithm

### Example: Recognizing a Geometric Series

#### Question

What is the sum of the series $1+\dfrac{2}{3} + \dfrac{4}{9} + \dfrac{8}{27} + \cdots + \dfrac{2^n}{3^n}+\cdots\,?$

#### Explanation

The first thing we notice is that we can rewrite the terms of the series as powers of $\dfrac{2}{3}\mathbin{:}$

$$


\begin{aligned}1+\frac{2}{3}+\frac{4}{9}+\frac{8}{27}+⋯+\frac{2^{𝑛}}{3^{𝑛}}+⋯ & =1+\frac{2}{3}+\frac{2^{2}}{3^{2}}+\frac{2^{3}}{3^{3}}+⋯+\frac{2^{𝑛}}{3^{𝑛}}+⋯ \\ & =1+\frac{2}{3}+(\frac{2}{3})^{2}+(\frac{2}{3})^{3}+⋯+(\frac{2}{3})^{𝑛}+⋯\end{aligned}


$$

Then, we recognize that the series looks similar to the Maclaurin expansion for $f({\color{blue}x}) = \dfrac{1}{1-{\color{blue}x}}.$

$$


\begin{aligned}\frac{1}{1−𝑥} & =1+𝑥+𝑥^{2}+𝑥^{3}+⋯+𝑥^{𝑛}+⋯\end{aligned}


$$

Substituting $x={\color{blue}\dfrac{2}{3}}$ into our Maclaurin expansion gives

$$


\begin{aligned}\frac{1}{(1−\frac{2}{3})} & =1+\frac{2}{3}+(\frac{2}{3})^{2}+(\frac{2}{3})^{3}+⋯+(\frac{2}{3})^{𝑛}+⋯ \\ 3 & =1+\frac{2}{3}+\frac{4}{9}+\frac{8}{27}+⋯+\frac{2^{𝑛}}{3^{𝑛}}+⋯\,.\end{aligned}


$$

Therefore, the sum of the series is $3.$

### Example: Recognizing Series That Are Similar to the Maclaurin Expansion for the Exponential Function

#### Question

Find the sum $3 + \dfrac{4}{2!} + \dfrac{8}{3!}+ \cdots + \dfrac{2^n}{n!}+ \cdots\,.$

#### Explanation

We recognize that the series looks similar to the Maclaurin expansion for $f(x) = e^x.$

$$


\begin{aligned}𝑒^{𝑥}=1+𝑥+\frac{𝑥^{2}}{2!}+\frac{𝑥^{3}}{3!}+⋯+\frac{𝑥^{𝑛}}{𝑛!}+⋯\end{aligned}


$$

Substituting $x={\color{blue}2}$ into our Maclaurin expansion gives

$$


\begin{aligned}𝑒^{2} & =1+2+\frac{2^{2}}{2!}+\frac{2^{3}}{3!}+⋯+\frac{2^{𝑛}}{𝑛!}+⋯ \\ 𝑒^{2} & =3+\frac{4}{2!}+\frac{8}{3!}+⋯+\frac{2^{𝑛}}{𝑛!}+⋯\,.\end{aligned}


$$

Therefore, the sum of the series is $e^2.$

### Example: Recognizing Series That Are Similar to the Maclaurin Expansion for the Natural Logarithm

#### Question

Find the sum $\, \dfrac{2}{3} - \dfrac{(2/3)^2}{2} + \dfrac{(2/3)^3}{3} + \cdots +\dfrac{(-1)^{n+1}(2/3)^n}{n}+\cdots\,.$

#### Explanation

Notice that we can rewrite the given sum as follows:

$$


\begin{aligned}\frac{2}{3}−\frac{(2/3)^{2}}{2}+\frac{(2/3)^{3}}{3}+⋯+\frac{(−1)^{𝑛+1}(2/3)^{𝑛}}{𝑛}+⋯\end{aligned}


$$

Then, we recognize that the series looks similar to the Maclaurin expansion for $f(x) = \ln(1+x).$

$$


\begin{aligned}ln⁡(1+𝑥) & =𝑥−\frac{𝑥^{2}}{2}+\frac{𝑥^{3}}{3}+⋯\end{aligned}


$$

Substituting $x={\color{blue}\dfrac{2}{3}}$ into our Maclaurin expansion gives

$$


\begin{aligned}ln⁡(1+\frac{2}{3}) & =\frac{2}{3}−\frac{(2/3)^{2}}{2}+\frac{(2/3)^{3}}{3}+⋯+\frac{(−1)^{𝑛+1}(2/3)^{𝑛}}{𝑛}+⋯ \\ ln⁡(\frac{5}{3}) & =\frac{2}{3}−\frac{(2/3)^{2}}{2}+\frac{(2/3)^{3}}{3}+⋯+\frac{(−1)^{𝑛+1}(2/3)^{𝑛}}{𝑛}+⋯\,.\end{aligned}


$$

Therefore, the sum of the series is $\ln\left(\dfrac{5}{3}\right).$
