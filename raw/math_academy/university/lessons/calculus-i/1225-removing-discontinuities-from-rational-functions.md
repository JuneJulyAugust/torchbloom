# Removing Discontinuities From Rational Functions

Source: https://www.mathacademy.com/topics/1225?courseId=105
Topic ID: 1225

## Prerequisites

- [Removing Jump Discontinuities](./638-removing-jump-discontinuities.md)

## Lesson

### Introduction

Consider the function $f(x)$ below:

$$


\begin{aligned}\frac{𝑥^{2}−1}{𝑥^{2}+𝑥−2},\, & 𝑥≠1 \\ 𝑘,\, & 𝑥=1\end{aligned}


$$

The function $f(x)$ seems to have a point discontinuity at $x=1.$ However, by selecting a particular value for $k,$ we can remove the point discontinuity and make the function continuous.

We can find this value of $k$ by forcing the limit of the function to be equal to the value of the function at $x=1\mathbin{:}$

$$


\lim\limits_{x\to 1} f(x) = f(1)


$$

Remember that $\lim\limits_{x\to 1} f(x)$ represents the value that $f(x)$ approaches as $x$ gets closer and closer, but not equal, to $1.$ So, when evaluating $\lim\limits_{x\to 1} f(x),$ we need to use the function definition for $x \neq 1.$

$$


\begin{aligned}\underset{𝑥→1}{lim}𝑓(𝑥) & =\underset{𝑥→1}{lim}\frac{𝑥^{2}−1}{𝑥^{2}+𝑥−2} \\ & =\underset{𝑥→1}{lim}\frac{(𝑥−1)(𝑥+1)}{(𝑥−1)(𝑥+2)} \\ & =\underset{𝑥→1}{lim}\frac{(𝑥−1)(𝑥+1)}{(𝑥−1)(𝑥+2)} \\ & =\underset{𝑥→1}{lim}\frac{𝑥+1}{𝑥+2} \\ & =\frac{1+1}{1+2} \\ & =\frac{2}{3}\end{aligned}


$$

At $x=1,$ the function is defined as $f(x)=k.$ So, $f(1)=k$, and for continuity we must have

$$


\begin{aligned}\underset{𝑥→1}{lim}𝑓(𝑥) & =𝑓(1) \\ \frac{2}{3} & =𝑘.\end{aligned}


$$

Therefore, to make $f(x)$ continuous at $x=1,$ we need to choose $k=\dfrac{2}{3}.$

### Example: Removing Point Discontinuities From Rational Functions

#### Question

Let $g(x)$ be the function defined below. For what value(s) of $k$ is $g(x)$ continuous at $x=-1?$

$$


\begin{aligned}\frac{𝑥^{3}+1}{𝑘𝑥+𝑘}, & 𝑥≠−1 \\ \frac{𝑘}{3}, & 𝑥=−1\end{aligned}


$$

#### Explanation

First, we factor the numerator and denominator and cancel any common factors:

$$


\begin{aligned}\frac{𝑥^{3}+1}{𝑘𝑥+𝑘} & =\frac{(𝑥+1)(𝑥^{2}−𝑥+1)}{𝑘(𝑥+1)} \\ & =\frac{(𝑥+1)(𝑥^{2}−𝑥+1)}{𝑘(𝑥+1)} \\ & =\frac{𝑥^{2}−𝑥+1}{𝑘}.\end{aligned}


$$

Now we can compute the limit at $x=-1,$ and get

$$


\lim\limits_{x\to -1} g(x) = \lim\limits_{x\to -1} \left(\dfrac{x^2-x+1}{k}\right) = \dfrac{3}{k}.


$$

For $g(x)$ to be continuous at $x=-1,$ we must have

$$


\begin{aligned}\underset{𝑥→−1}{lim}𝑔(𝑥) & =𝑔(−1) \\ \frac{3}{𝑘} & =\frac{𝑘}{3} \\ 9 & =𝑘^{2} \\ ±3 & =𝑘.\end{aligned}


$$

Therefore, for the function to be continuous at $x=-1,$ the value of $k$ must be either $-3$ or $3.$

### Example: Removing Jump Discontinuities From Rational Functions

#### Question

Let $f(x)$ be the function defined below. Find the values of $k$ for which $f(x)$ is continuous at $x=2.$

$$


\begin{aligned}\frac{𝑥^{2}+4𝑥−12}{𝑥^{2}−4}, & 𝑥<2 \\ 2^{𝑘𝑥}, & 𝑥≥2.\end{aligned}


$$

#### Explanation

From the definition of $f(x)$, the left-sided limit of $f(x)$ at $x=2$ is

$$


\begin{aligned}\underset{𝑥→2^{−}}{lim}𝑓(𝑥) & =\underset{𝑥→2^{−}}{lim}\frac{𝑥^{2}+4𝑥−12}{𝑥^{2}−4} \\ & =\underset{𝑥→2^{−}}{lim}\frac{(𝑥−2)(𝑥+6)}{(𝑥−2)(𝑥+2)} \\ & =\underset{𝑥→2^{−}}{lim}\frac{(𝑥−2)(𝑥+6)}{(𝑥−2)(𝑥+2)} \\ & =\underset{𝑥→2^{−}}{lim}\frac{𝑥+6}{𝑥+2} \\ & =\frac{2+6}{2+2} \\ & =2.\end{aligned}


$$

On the other hand, the right-sided limit is

$$


\begin{aligned}\underset{𝑥→2^{+}}{lim}𝑓(𝑥) & =\underset{𝑥→2^{+}}{lim}2^{𝑘𝑥} \\ & =2^{2𝑘}.\end{aligned}


$$

We also note that $f(2) = 2^{2k}.$

So, for $f(x)$ to be continuous at $x=2,$ we must have

$$


\begin{aligned}\underset{𝑥→2^{+}}{lim}𝑓(𝑥) & =\underset{𝑥→2^{−}}{lim}𝑓(𝑥) \\ 2^{2𝑘} & =2 \\ 2^{2𝑘} & =2^{1} \\ 2𝑘 & =1 \\ 𝑘 & =\frac{1}{2}\end{aligned}


$$

Therefore, $k=\dfrac12$ removes the discontinuity at $x=2.$
