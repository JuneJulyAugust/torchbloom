# Removing Point Discontinuities

Source: https://www.mathacademy.com/topics/341?courseId=105
Topic ID: 341

## Prerequisites

- [Solving Radical Equations](../algebra-i/116-solving-radical-equations.md)
- [Calculating Limits of Radical Functions Using Conjugate Multiplication](./604-calculating-limits-of-radical-functions-using-conjugate-multiplication.md)
- [Solving Logarithmic Equations Containing the Natural Logarithm](../algebra-ii/1551-solving-logarithmic-equations-containing-the-natural-logarithm.md)
- [Point Discontinuities](./2002-point-discontinuities.md)

## Lesson

### Introduction

Consider the function $f(x)$ below.

$$


\begin{aligned}3𝑥+𝑎, & 𝑥≠4, \\ 13, & 𝑥=4\end{aligned}


$$

The function $f(x)$ seems to have a point discontinuity at $x=4.$ However, by selecting a particular value for $a,$ we can remove the point discontinuity and make the function continuous.

We can find this value of $a$ by forcing the limit of the function to be equal to the value of the function at $x=4\mathbin{:}$

$$


\lim\limits_{x\to 4} f(x) = f(4)


$$

Remember that $\lim\limits_{x\to 4} f(x)$ represents the value that $f(x)$ approaches as $x$ gets closer and closer, but not equal, to $4.$ So, when evaluating $\lim\limits_{x\to 4} f(x),$ we need to use the function definition for $x \neq 4.$

$$


\begin{aligned}\underset{𝑥→4}{lim}𝑓(𝑥) & =\underset{𝑥→4}{lim}(3𝑥+𝑎) \\ & =3(4)+𝑎 \\ & =12+𝑎\end{aligned}


$$

At $x=4,$ the function is defined as $f(x)=13.$ So $f(4)=13,$ and we can solve the equation:

$$


\begin{aligned}\underset{𝑥→4}{lim}𝑓(𝑥) & =𝑓(4) \\ 12+𝑎 & =13 \\ 𝑎 & =1\end{aligned}


$$

Therefore, to make $f(x)$ continuous at $x=4,$ we need to choose $a=1.$

### Example: Removing a Point Discontinuity in a Piecewise Polynomial Function

#### Question

The function $f(x)$ is defined for every real number $x$ and is given by

$$


\begin{aligned}𝑥^{2}+2𝑘𝑥+1, & 𝑥≠1, \\ 4, & 𝑥=1.\end{aligned}


$$

If $f(x)$ is continuous at $x=1,$ what is the value of $k?$

#### Explanation

From the definition of $f(x),$

$$


\begin{aligned}\underset{𝑥→\,1}{lim}𝑓(𝑥) & =\underset{𝑥→\,1}{lim}(𝑥^{2}+2𝑘𝑥+1) \\ & =1^{2}+2𝑘(1)+1 \\ & =2+2𝑘.\end{aligned}


$$

In order for $f(x)$ to be continuous at $x=1,$ we must have

$$


\begin{aligned}\underset{𝑥→1}{lim}𝑓(𝑥) & =𝑓(1) \\ 2+2𝑘 & =4 \\ 2𝑘 & =2 \\ 𝑘 & =1.\end{aligned}


$$

Therefore, setting $k=1$ removes the point discontinuity.

### Example: Removing a Point Discontinuity in a Piecewise Exponential or Logarithmic Function

#### Question

The function $h(x)$ is given by

$$


\begin{aligned}log_{3}⁡(𝑥+𝑐), & 𝑥≠0, \\ 2, & 𝑥=0.\end{aligned}


$$

Given that $h(x)$ is continuous at $x=0,$ what is the value of $c?$

#### Explanation

From the definition of $h(x),$ we have that

$$


\begin{aligned}\underset{𝑥→0}{lim}ℎ(𝑥) & =\underset{𝑥→0}{lim}log_{3}⁡(𝑥+𝑐) \\ & =log_{3}⁡(0+𝑐) \\ & =log_{3}⁡(𝑐).\end{aligned}


$$

In order for $h(x)$ to be continuous at $x=0,$ we must have

$$


\begin{aligned}\underset{𝑥→0}{lim}ℎ(𝑥) & =ℎ(0) \\ log_{3}⁡(𝑐) & =2 \\ 𝑐 & =3^{2} \\ 𝑐 & =9.\end{aligned}


$$

Therefore, setting $c=9$ removes the point discontinuity.

### Example: Removing a Point Discontinuity in a Piecewise Radical Function

#### Question

The function $g(x)$ is given by

$$


\begin{aligned}\sqrt{√𝑏𝑥+3}, & 𝑥≠2, \\ 5, & 𝑥=2.\end{aligned}


$$

If $g(x)$ is continuous at $x=2,$ what is the value $b?$

#### Explanation

From the definition of $g(x)$,

$$


\begin{aligned}\underset{𝑥→2}{lim}𝑔(𝑥)=\underset{𝑥→2}{lim}(\sqrt{√𝑏𝑥+3})=\sqrt{√2𝑏+3}.\end{aligned}


$$

In order for $g(x)$ to be continuous at $x=2,$ we must have

$$


\begin{aligned}\underset{𝑥→2}{lim}𝑔(𝑥) & =𝑔(2) \\ \sqrt{√2𝑏+3} & =5 \\ 2𝑏+3 & =25 \\ 2𝑏 & =22 \\ 𝑏 & =11.\end{aligned}


$$
