# Recognizing Standard Maclaurin Series for Trigonometric Functions

Source: https://www.mathacademy.com/topics/3573?courseId=21
Topic ID: 3573

## Prerequisites

- [Recognizing Standard Maclaurin Series](./884-recognizing-standard-maclaurin-series.md)

## Lesson

### Introduction

We need to recognize when a particular series looks like a standard Maclaurin series. A list of some common Maclaurin series is given below.

$$


\begin{aligned} & \frac{1}{1−𝑥}=1+𝑥+𝑥^{2}+⋯+𝑥^{𝑛}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}𝑥^{𝑛}, & & 𝑥∈(−1,1) \\ & \frac{1}{1+𝑥}=1−𝑥+𝑥^{2}−⋯+(−1)^{𝑛}𝑥^{𝑛}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}(−1)^{𝑛}𝑥^{𝑛}, & & 𝑥∈(−1,1) \\ & 𝑒^{𝑥}=1+𝑥+\frac{1}{2!}𝑥^{2}+⋯+\frac{𝑥^{𝑛}}{𝑛!}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}\frac{𝑥^{𝑛}}{𝑛!}, & & 𝑥∈(−∞,∞) \\ & ln⁡(1+𝑥)=𝑥−\frac{1}{2}𝑥^{2}+\frac{1}{3}𝑥^{3}−⋯+\frac{(−1)^{𝑛+1}𝑥^{𝑛}}{𝑛}+⋯=\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{(−1)^{𝑛+1}𝑥^{𝑛}}{𝑛}, & & 𝑥∈(−1,1] \\ & sin⁡(𝑥)=𝑥−\frac{1}{3!}𝑥^{3}+\frac{1}{5!}𝑥^{5}+⋯+\frac{(−1)^{𝑛}𝑥^{2𝑛+1}}{(2𝑛+1)!}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}\frac{(−1)^{𝑛}𝑥^{2𝑛+1}}{(2𝑛+1)!}, & & 𝑥∈(−∞,∞) \\ & cos⁡(𝑥)=1−\frac{1}{2!}𝑥^{2}+\frac{1}{4!}𝑥^{4}−⋯+\frac{(−1)^{𝑛}𝑥^{2𝑛}}{(2𝑛)!}+⋯=\underset{\underset{𝑛=0}{∑}}{\overset{}{∞}}\frac{(−1)^{𝑛}𝑥^{2𝑛}}{(2𝑛)!}, & & 𝑥∈(−∞,∞)\end{aligned}


$$

In this lesson, we will focus on recognizing the standard Maclaurin series for the sine and cosine functions.

**Note:** To remember the series for $\sin x$ and $\cos x$ easily, notice that they are both alternating series that contain every other term of the expansion for $e^x.$ Sine has the odd-degree terms (since it is an odd function), and cosine has the even-degree terms (since it is an even function).

### Example: Recognizing Series That Are Similar to the Maclaurin Expansion for Sine

#### Question

What is the sum of the series $\dfrac{\pi}{3} - \dfrac{(\pi/3)^3}{3!} + \dfrac{(\pi/3)^5}{5!}-\cdots + \dfrac{(-1)^{n}(\pi/3)^{2n+1}}{(2n+1)!}+\cdots\,?$

#### Explanation

We recognize that the series looks similar to the Maclaurin expansion for $f(x) = \sin x.$

$$


\begin{aligned}sin⁡𝑥 & =𝑥−\frac{𝑥^{3}}{3!}+\frac{𝑥^{5}}{5!}−⋯+\frac{(−1)^{𝑛}𝑥^{2𝑛+1}}{(2𝑛+1)!}+⋯\,\end{aligned}


$$

Substituting $x=\dfrac{\pi}{3}$ into our Maclaurin expansion gives

$$


\begin{aligned}sin⁡(\frac{𝜋}{3}) & =\frac{𝜋}{3}−\frac{(𝜋/3)^{3}}{3!}+\frac{(𝜋/3)^{5}}{5!}−⋯+\frac{(−1)^{𝑛}(𝜋/3)^{2𝑛+1}}{(2𝑛+1)!}+⋯ \\ \frac{\sqrt{3}}{2} & =\frac{𝜋}{3}−\frac{(𝜋/3)^{3}}{3!}+\frac{(𝜋/3)^{5}}{5!}−⋯+\frac{(−1)^{𝑛}(𝜋/3)^{2𝑛+1}}{(2𝑛+1)!}+⋯\,.\end{aligned}


$$

Therefore, the sum of the series is $\dfrac{\sqrt{3}}{2}.$

### Example: Recognizing Series That Are Similar to the Maclaurin Expansion for Cosine

#### Question

Find the sum $1 - \dfrac{9}{2!} + \dfrac{81}{4!}-\cdots + \dfrac{(-1)^{n}3^{2n}}{(2n)!} \,\cdots \,.$

#### Explanation

We recognize that the series looks similar to the Maclaurin expansion for $f(x) = \cos x.$

$$


\begin{aligned}cos⁡𝑥=1−\frac{1}{2!}𝑥^{2}+\frac{1}{4!}𝑥^{4}−⋯+\frac{(−1)^{𝑛}\,𝑥^{2𝑛}}{(2𝑛)!}+⋯\end{aligned}


$$

Substituting $x=3$ into our Maclaurin expansion gives

$$


\begin{aligned}cos⁡(3) & =1−\frac{3^{2}}{2!}+\frac{3^{4}}{4!}−⋯+\frac{(−1)^{𝑛}3^{2𝑛}}{(2𝑛)!}\,⋯ \\ cos⁡(3) & =1−\frac{9}{2!}+\frac{81}{4!}−⋯+\frac{(−1)^{𝑛}3^{2𝑛}}{(2𝑛)!}\,⋯\,.\end{aligned}


$$

Therefore, the sum of the series is $\cos(3).$
