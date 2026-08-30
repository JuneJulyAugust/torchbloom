# Evaluating Limits at Infinity of Radical Functions

Source: https://www.mathacademy.com/topics/616?courseId=105
Topic ID: 616

## Prerequisites

- [Simplifying Square Root Expressions Using Polynomial Factorization](../algebra-ii/448-simplifying-square-root-expressions-using-polynomial-factorization.md)
- [Limits at Infinity and Horizontal Asymptotes of Rational Functions](./1903-limits-at-infinity-and-horizontal-asymptotes-of-rational-functions.md)
- [Limits of Radical Functions](./1986-limits-of-radical-functions.md)

## Lesson

### Introduction

How do we evaluate a limit like $\displaystyle \lim_{x\to\infty}\dfrac{x^2}{\sqrt{9x^4+x}}?$

Because the ${\color{blue}{x^4}}$ in the radical is a perfect square, we can factor it outside of the radical.

$$


\begin{aligned}\underset{𝑥→∞}{lim}\frac{𝑥^{2}}{\sqrt{√9𝑥^{4}+𝑥}} & =\underset{𝑥→∞}{lim}\frac{𝑥^{2}}{\sqrt{√𝑥^{4}(9+\frac{𝑥}{𝑥^{4}})}} \\ & =\underset{𝑥→∞}{lim}\frac{𝑥^{2}}{\sqrt{√𝑥^{4}}⋅\sqrt{√9+\frac{1}{𝑥^{3}}}} \\ & =\underset{𝑥→∞}{lim}\frac{𝑥^{2}}{|𝑥^{2}|\sqrt{√9+\frac{1}{𝑥^{3}}}}\end{aligned}


$$

Since $x^2>0$ for all $x,$ we have $|x^2|=x^2.$ Then, we can cancel the $x^2$ in the numerator and denominator, and evaluate the limit.

$$


\begin{aligned}\underset{𝑥→∞}{lim}\frac{𝑥^{2}}{|𝑥^{2}|\sqrt{√9+\frac{1}{𝑥^{3}}}} & =\underset{𝑥→∞}{lim}\frac{𝑥^{2}}{𝑥^{2}\sqrt{√9+\frac{1}{𝑥^{3}}}} \\ & =\underset{𝑥→∞}{lim}\frac{1}{\sqrt{√9+\frac{1}{𝑥^{3}}}} \\ & =\frac{1}{\sqrt{√9+0}} \\ & =\frac{1}{3}\end{aligned}


$$

### Example: Finding the Horizontal Asymptote of a Radical Function

#### Question

Find the horizontal asymptote of $y=f(x)$ where $f(x)=\dfrac{\sqrt{2x^4+5}}{x^2+3}.$

#### Explanation

The horizontal asymptote of $y=f(x)$ is $y=\lim_\limits{x \rightarrow \infty} f(x).$ To evaluate the limit, note that the $x^4$ in the radical is a perfect square, so we can rewrite the function as

$$


\begin{aligned}\underset{𝑥→∞}{lim}𝑓(𝑥) & =\frac{\sqrt{√2𝑥^{4}+5}}{𝑥^{2}+3} \\ & =\underset{𝑥→∞}{lim}\frac{\sqrt{√𝑥^{4}(2+\frac{5}{𝑥^{4}})}}{𝑥^{4}} \\ & =\underset{𝑥→∞}{lim}\frac{\sqrt{√𝑥^{4}}⋅\sqrt{√2+\frac{5}{𝑥^{4}}}}{𝑥^{4}} \\ & =\underset{𝑥→∞}{lim}\frac{|𝑥^{2}|⋅\sqrt{√2+\frac{5}{𝑥^{4}}}}{𝑥^{4}}.\end{aligned}


$$

Since $x^2>0$ for all $x,$ we have $|x^2|=x^2.$

$$


\begin{aligned}\underset{𝑥→∞}{lim}\frac{|𝑥^{2}|⋅\sqrt{√2+\frac{5}{𝑥^{4}}}}{𝑥^{4}}=\underset{𝑥→∞}{lim}\frac{𝑥^{2}⋅\sqrt{√2+\frac{5}{𝑥^{4}}}}{𝑥^{4}}\end{aligned}


$$

Now, we divide the top and bottom of the fraction by $x^2$ and evaluate the limit, which gives

$$


\begin{aligned}\underset{𝑥→∞}{lim}\frac{\sqrt{√2+\frac{5}{𝑥^{4}}}}{𝑥^{4}}=\underset{𝑥→∞}{lim}\frac{\sqrt{√2+0}}{1+0}=\sqrt{√2}.\end{aligned}


$$

Therefore, the horizontal asymptote is $y=\sqrt{2}.$

### Example: Evaluating the Limit at Infinity of a Rational Function with a Radical in the Numerator

#### Question

Calculate $\displaystyle {\lim_{x\to \infty}\dfrac{\sqrt{2x^2-3x}}{x^2+x}}.$

#### Explanation

We note that the $x^2$ in the radical is a perfect square, so we can rewrite the function as

$$


\begin{aligned}\underset{𝑥→∞}{lim}\frac{\sqrt{√2𝑥^{2}−3𝑥}}{𝑥^{2}+𝑥} & =\underset{𝑥→∞}{lim}\frac{\sqrt{√𝑥^{2}(2−\frac{3𝑥}{𝑥^{2}})}}{𝑥^{2}}=\underset{𝑥→∞}{lim}\frac{\sqrt{√𝑥^{2}}⋅\sqrt{√2−\frac{3}{𝑥}}}{𝑥}.\end{aligned}


$$

Note that $\sqrt{x^2}=|x|.$ Since $x \to \infty,$ we have $x>0,$ and therefore $\sqrt{x^2}=|x|=x.$ So, the above reduces to

$$


\begin{aligned}\underset{𝑥→∞}{lim}\frac{𝑥⋅\sqrt{√2−\frac{3}{𝑥}}}{𝑥}.\end{aligned}


$$

Now, we divide the top and bottom of the fraction by $x^2$ and evaluate the limit, which gives

$$


\begin{aligned}\underset{𝑥→∞}{lim}\frac{\frac{1}{𝑥}\sqrt{√2−\frac{3}{𝑥}}}{𝑥} & =\frac{0⋅\sqrt{√2−0}}{1+0}=0.\end{aligned}


$$

### Example: Evaluating the Limit at Infinity of a Rational Function with a Radical in the Denominator

#### Question

Find the horizontal asymptote of the function $y=f(x)$ where $f(x)$ is given by

$$


f(x)=\dfrac{2x^4+x}{\sqrt{x^6-x}}, \quad x< 0.


$$

#### Explanation

The horizontal asymptote of $f(x)$ in the domain $x< 0$ is $y=\lim_\limits{x \rightarrow -\infty} f(x).$ To find the horizontal asymptote, we note that the $x^6$ in the radical is a perfect square, and so we rewrite the function as

$$


\begin{aligned}\underset{𝑥→−∞}{lim}𝑓(𝑥) & =\underset{𝑥→−∞}{lim}\frac{2𝑥^{4}+𝑥}{\sqrt{√𝑥^{6}−𝑥}}, \\ & =\underset{𝑥→−∞}{lim}\frac{2𝑥^{4}+𝑥}{\sqrt{√𝑥^{6}(1−\frac{𝑥}{𝑥^{6}})}} \\ & =\underset{𝑥→−∞}{lim}\frac{2𝑥^{4}+𝑥}{\sqrt{√𝑥^{6}}⋅\sqrt{√1−\frac{1}{𝑥^{5}}}}.\end{aligned}


$$

Note that $\sqrt{x^6}=|x^3|.$ Since $x \to -\infty,$ we have $x^3<0,$ and therefore $\sqrt{x^6}=|x^3|=-x^3.$ So, the above reduces to

$$


\begin{aligned}\underset{𝑥→−∞}{lim}𝑓(𝑥) & =\underset{𝑥→−∞}{lim}\frac{2𝑥^{4}+𝑥}{(−𝑥^{3})⋅\sqrt{√1−\frac{1}{𝑥^{5}}}}=−\underset{𝑥→−∞}{lim}\frac{2𝑥^{4}+𝑥}{𝑥^{3}⋅\sqrt{√1−\frac{1}{𝑥^{5}}}}.\end{aligned}


$$

Now, we divide the top and bottom of the fraction by $x^3$ and evaluate the limit, which gives

$$


\begin{aligned}\underset{𝑥→−∞}{lim}𝑓(𝑥) & =−\underset{𝑥→−∞}{lim}\frac{2𝑥+\frac{𝑥}{𝑥^{3}}}{𝑥^{3}} \\ & =−\underset{𝑥→−∞}{lim}\frac{2𝑥+\frac{1}{𝑥^{2}}}{𝑥^{2}} \\ & =−\underset{𝑥→−∞}{lim}\frac{2𝑥+0}{\sqrt{√1−0}} \\ & =−\underset{𝑥→−∞}{lim}2𝑥 \\ & =∞.\end{aligned}


$$

The limit is not a finite number. Therefore, there is no horizontal asymptote.
