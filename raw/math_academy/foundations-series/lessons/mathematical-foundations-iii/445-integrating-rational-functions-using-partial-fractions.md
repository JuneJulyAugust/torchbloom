# Integrating Rational Functions Using Partial Fractions

Source: https://www.mathacademy.com/topics/445?courseId=136
Topic ID: 445

## Prerequisites

- [Expressing Rational Functions as Sums of Partial Fractions](./1060-expressing-rational-functions-as-sums-of-partial-fractions.md)
- [Calculating Definite Integrals Using Substitution](./1159-calculating-definite-integrals-using-substitution.md)

## Lesson

### Introduction

How do we evaluate an integral like $\displaystyle \int \dfrac{2x-1}{(x+2)(x-3)} \text{d}x?$

First of all, note that the integrand can be converted into a sum of partial fractions:

$$


\dfrac{2x-1}{(x+2)(x-3)}=\dfrac{A}{(x+2)} +\dfrac{B}{(x-3)}


$$

If we can figure out the partial fractions, then we can integrate each of the partial fractions using the natural logarithm.

So, let's compute the partial fractions. If we multiply the above equation by $(x+2)(x-3),$ we get

$$


\begin{aligned}2𝑥−1 & =𝐴(𝑥−3)+𝐵(𝑥+2).\end{aligned}


$$

The expression above must hold for all values of $x.$ Plugging in $x=-2,$ we can eliminate $B$ and solve for $A\mathbin{:}$

$$


\begin{aligned}2(−2)−1 & =𝐴(−2−3)+𝐵(−2+2) \\ −5 & =𝐴(−5)+𝐵(0) \\ 𝐴 & =1.\end{aligned}


$$

On the other hand, plugging in $x=3,$ we can eliminate $A$ and solve for $B\mathbin{:}$

$$


\begin{aligned}2(3)−1 & =𝐴(3−3)+𝐵(3+2) \\ 5 & =𝐴(0)+𝐵(5) \\ 𝐵 & =1.\end{aligned}


$$

Therefore,

$$


\dfrac{2x-1}{(x+2)(x-3)} = \dfrac{1}{(x+2)} +\dfrac{1}{(x-3)}.


$$

Finally, we can integrate each of the partial fractions separately:

$$


\begin{aligned}∫\frac{2𝑥−1}{(𝑥+2)(𝑥−3)}d𝑥 & =∫(\frac{1}{𝑥+2}+\frac{1}{𝑥−3})d𝑥 \\ & =∫\frac{1}{𝑥+2}d𝑥+∫\frac{1}{𝑥−3}d𝑥 \\ & =ln⁡|𝑥+2|+ln⁡|𝑥−3|+𝐶.\end{aligned}


$$

And we're done!

### Example: Calculating an Indefinite Integral of a Rational Function Using Partial Fractions

#### Question

Evaluate $\displaystyle \int \dfrac{5x}{x^2+3x-4} \,\text{d}x.$

#### Explanation

First, we note that the denominator of the integrand can be factored as

$$


x^2+3x-4 = (x-1)(x+4) \,.


$$

So, the integrand can be converted into a sum of partial fractions,

$$


\begin{aligned}\frac{5𝑥}{𝑥^{2}+3𝑥−4} & =\frac{5𝑥}{(𝑥−1)(𝑥+4)} \\ & =\frac{𝐴}{(𝑥−1)}+\frac{𝐵}{(𝑥+4)},\end{aligned}


$$

which gives

$$


\begin{aligned}5𝑥 & =𝐴(𝑥+4)+𝐵(𝑥−1).\end{aligned}


$$

Plugging in $x=-4,$ we can eliminate $A$ and solve for $B\mathbin{:}$

$$


\begin{aligned}5(−4) & =𝐴(−4+4)+𝐵(−4−1) \\ −20 & =−5𝐵 \\ 𝐵 & =4.\end{aligned}


$$

On the other hand, by plugging in $x=1,$ we can eliminate $B$ and solve for $A\mathbin{:}$

$$


\begin{aligned}5(1) & =𝐴(1+4)+𝐵(1−1) \\ 5 & =5𝐴 \\ 𝐴 & =1.\end{aligned}


$$

Therefore,

$$


\dfrac{5x}{x^2+3x-4} = \dfrac{1}{(x-1)} +\dfrac{4}{(x+4)}.


$$

Finally, we integrate, and we get

$$


\begin{aligned}∫\frac{5𝑥}{𝑥^{2}+3𝑥−4}d𝑥 & =∫(\frac{1}{𝑥−1}+\frac{4}{𝑥+4})d𝑥 \\ & =∫\frac{1}{𝑥−1}d𝑥+4∫\frac{1}{𝑥+4}d𝑥 \\ & =ln⁡|𝑥−1|+4ln⁡|𝑥+4|+𝐶.\end{aligned}


$$

### Example: Calculating a Definite Integral of a Rational Function Using Partial Fractions

#### Question

Evaluate $\displaystyle \int_1^4 \dfrac{2x+3}{4x^2-1} \,\text{d}x.$

#### Explanation

We'll work out the indefinite integral first and then proceed with the definite integral.

First, we note that a denominator of the integrand can be factored as

$$


4x^2-1 = (2x+1)(2x-1) \,.


$$

So the integrand can be converted into a sum of partial fractions,

$$


\begin{aligned}\frac{2𝑥+3}{4𝑥^{2}−1} & =\frac{2𝑥+3}{(2𝑥+1)(2𝑥−1)} \\ & =\frac{𝐴}{(2𝑥+1)}+\frac{𝐵}{(2𝑥−1)},\end{aligned}


$$

which gives

$$


\begin{aligned}2𝑥+3 & =𝐴(2𝑥−1)+𝐵(2𝑥+1).\end{aligned}


$$

Plugging in $x=\dfrac{1}{2},$ we can eliminate $A$ and solve for $B\mathbin{:}$

$$


\begin{aligned}2(\frac{1}{2})+3 & =𝐴(2(\frac{1}{2})−1)+𝐵(2(\frac{1}{2})+1) \\ 4 & =2𝐵 \\ 𝐵 & =2.\end{aligned}


$$

On the other hand, plugging in $x=-\dfrac{1}{2},$ we can eliminate $B$ and solve for $A\mathbin{:}$

$$


\begin{aligned}2(−\frac{1}{2})+3 & =𝐴(2(−\frac{1}{2})−1)+𝐵(2(−\frac{1}{2})+1) \\ 2 & =−2𝐴 \\ 𝐴 & =−1.\end{aligned}


$$

Therefore,

$$


\dfrac{2x+3}{4x^2-1} = -\dfrac{1}{(2x+1)} +\dfrac{2}{(2x-1)}.


$$

Now, we integrate and get

$$


\begin{aligned}∫\frac{2𝑥+3}{4𝑥^{2}−1}d𝑥 & =∫(−\frac{1}{(2𝑥+1)}+\frac{2}{(2𝑥−1)})d𝑥 \\ & =−∫\frac{1}{2𝑥+1}d𝑥+2∫\frac{1}{2𝑥−1}d𝑥 \\ & =−\frac{1}{2}ln⁡|2𝑥+1|+2(\frac{1}{2}ln⁡|2𝑥−1|)+𝐶 \\ & =−\frac{1}{2}ln⁡|2𝑥+1|+ln⁡|2𝑥−1|+𝐶.\end{aligned}


$$

We can simplify the result using the laws of logarithms, as follows:

$$


\begin{aligned}∫\frac{2𝑥+3}{4𝑥^{2}−1}d𝑥 & =−\frac{1}{2}ln⁡|2𝑥+1|+ln⁡|2𝑥−1|+𝐶 \\ & =ln⁡\frac{1}{\sqrt{2𝑥+1}}+ln⁡|2𝑥−1|+𝐶 \\ & =ln⁡\frac{2𝑥−1}{\sqrt{2𝑥+1}}+𝐶\end{aligned}


$$

Finally, the definite integral is

$$


\begin{aligned}∫_{41}\frac{2𝑥+3}{4𝑥^{2}−1}\,d𝑥 & =ln⁡\frac{2𝑥−1}{\sqrt{2𝑥+1}}_{41} \\ & =ln⁡(\frac{7}{3})−ln⁡(\frac{1}{\sqrt{3}}) \\ & =ln⁡(\frac{7}{3})+ln⁡(\sqrt{3}) \\ & =ln⁡(\frac{7\sqrt{3}}{3}).\end{aligned}


$$
