# Integrating Rational Functions with Repeated Factors

Source: https://www.mathacademy.com/topics/446?courseId=136
Topic ID: 446

## Prerequisites

- [Integrating Rational Functions Using Partial Fractions](./445-integrating-rational-functions-using-partial-fractions.md)
- [Expressing Rational Functions with Repeated Factors as Sums of Partial Fractions](./1062-expressing-rational-functions-with-repeated-factors-as-sums-of-partial-fractions.md)

## Lesson

### Introduction

Suppose we are given the integral $\displaystyle \int \dfrac{3x+2}{(x+1)^2} \textrm{d}x.$ Note that we have the repeated factor $(x+1)$ in the denominator.

The correct form of the partial fraction expansion of the integrand is

$$


\dfrac{3x+2}{(x+1)^2}=\dfrac{A}{(x+1)} +\dfrac{B}{(x+1)^2} \,.


$$

To determine the coefficients $A$ and $B,$ we first multiply both sides the above equation by $(x+1)^2$ and get

$$


\begin{aligned}3𝑥+2 & =𝐴(𝑥+1)+𝐵.\end{aligned}


$$

Plugging in $x=-1,$ we can eliminate $A$ and solve for $B\mathbin{:}$

$$


\begin{aligned}3(−1)+2 & =𝐴(−1+1)+𝐵 \\ 𝐵 & =−1.\end{aligned}


$$

Plugging in $x=0$ and substituting the known value of $B,$ we can solve for $A\mathbin{:}$

$$


\begin{aligned}3(0)+2 & =𝐴(0+1)+𝐵 \\ 2 & =𝐴+𝐵 \\ 2 & =𝐴−1 \\ 𝐴 & =3.\end{aligned}


$$

Therefore,

$$


\dfrac{3x+2}{(x+1)^2}= \dfrac{3}{(x+1)} -\dfrac{1}{(x+1)^2}.


$$

Now this function can be integrated term by term. We get

$$


\begin{aligned}∫\frac{3𝑥+2}{(𝑥+1)^{2}}d𝑥 & =∫(\frac{3}{(𝑥+1)}−\frac{1}{(𝑥+1)^{2}})d𝑥 \\ & =3∫\frac{1}{𝑥+1}d𝑥−∫\frac{1}{(𝑥+1)^{2}}d𝑥 \\ & =3ln⁡|𝑥+1|+\frac{1}{𝑥+1}+𝐶\,,\end{aligned}


$$

where $C$ is a constant of integration.

### Example: Integrating Rational Functions With Repeated Factors of Degree Two

#### Question

Calculate $\displaystyle \int_0^1 \dfrac{2x+3}{(x+1)^2} \,\textrm{d}x.$

#### Explanation

First, we convert the integrand into a sum of partial fractions:

$$


\dfrac{2x+3}{(x+1)^2} = \dfrac{A}{(x+1)} +\dfrac{B}{(x+1)^2}


$$

To determine the coefficients $A,$ and $B,$ we first multiply both sides of the above equation by $(x+1)^2$ and get

$$


2x+3 = A(x+1)+B .


$$

Plugging in $x=-1,$ we can eliminate $A$ and solve for $B\mathbin{:}$

$$


\begin{aligned}2(−1)+3 & =𝐴(−1+1)+𝐵 \\ 1 & =0+𝐵 \\ 𝐵 & =1\end{aligned}


$$

Now, plugging in $x=0$ and substituting the known value of $B,$ we can solve for $A\mathbin{:}$

$$


\begin{aligned}2(0)+3 & =𝐴(0+1)+𝐵 \\ 3 & =𝐴+𝐵 \\ 3 & =𝐴+1 \\ 𝐴 & =2\end{aligned}


$$

Therefore, we can write the integrand as the partial sum

$$


\dfrac{2x+3}{(x+1)^2} = \dfrac{2}{(x+1)} +\dfrac{1}{(x+1)^2}.


$$

Finally, we integrate this expression term by term to get

$$


\begin{aligned}∫_{10}^{}\frac{2𝑥+3}{(𝑥+1)^{2}}\,d𝑥 & =∫_{10}^{}(\frac{2}{(𝑥+1)}+\frac{1}{(𝑥+1)^{2}})\,d𝑥 \\ & =2∫_{10}^{}\frac{1}{𝑥+1}\,d𝑥+∫_{10}^{}\frac{1}{(𝑥+1)^{2}}\,d𝑥 \\ & =2ln⁡|𝑥+1||_{10}^{}+(−\frac{1}{𝑥+1})_{10}^{} \\ & =2ln⁡|𝑥+1||_{10}^{}−\frac{1}{𝑥+1}_{10}^{} \\ & =2[ln⁡2−ln⁡1]−[\frac{1}{2}−1] \\ & =2ln⁡2+\frac{1}{2}\end{aligned}


$$

### Example: Integrating Rational Functions With a Repeated Factor and Another Factor

#### Question

Evaluate $\displaystyle \int \dfrac{3x^2-5x+8}{(x-3)^2(x+1)}\textrm{d}x.$

#### Explanation

First, we convert the integrand into a sum of partial fractions:

$$


\begin{aligned}\frac{3𝑥^{2}−5𝑥+8}{(𝑥−3)^{2}(𝑥+1)} & =\frac{𝐴}{(𝑥−3)}+\frac{𝐵}{(𝑥−3)^{2}}+\frac{𝐶}{(𝑥+1)}\end{aligned}


$$

To determine the coefficients $A,$ $B,$ and $C,$ we first multiply both sides of the above equation by $(x-3)^2(x+1)$ and get

$$


\begin{aligned}3𝑥^{2}−5𝑥+8 & =𝐴(𝑥−3)(𝑥+1)+𝐵(𝑥+1)+𝐶(𝑥−3)^{2}.\end{aligned}


$$

Plugging in $x=3,$ we can eliminate $A$ and $C$ and solve for $B\mathbin{:}$

$$


\begin{aligned}3(3^{2})−5(3)+8 & =𝐴(3−3)(3+1)+𝐵(3+1)+𝐶(3−3)^{2} \\ 20 & =𝐵(4) \\ 𝐵 & =5\end{aligned}


$$

Plugging in $x=-1,$ we can eliminate $A$ and $B$ and solve for $C\mathbin{:}$

$$


\begin{aligned}3(−1)^{2}−5(−1)+8 & =𝐴(−1−3)(−1+1)+𝐵(−1+1)+𝐶(−1−3)^{2} \\ 16 & =𝐶(−4)^{2} \\ 𝐶 & =1\end{aligned}


$$

Plugging in $x=0$ and substituting the known values of $B$ and $C,$ we can solve for $A\mathbin{:}$

$$


\begin{aligned}3(0^{2})−5(0)+8 & =𝐴(0−3)(0+1)+𝐵(0+1)+𝐶(0−3)^{2} \\ 8 & =−3𝐴+𝐵+9𝐶 \\ 8 & =−3𝐴+5+9(1) \\ 3𝐴 & =6 \\ 𝐴 & =2\end{aligned}


$$

Therefore,

$$


\dfrac{3x^2-5x+8}{(x-3)^2(x+1)} = \dfrac{2}{(x-3)} +\dfrac{5}{(x-3)^2} +\dfrac{1}{(x+1)}.


$$

Finally, we integrate this expression term by term, and get

$$


\begin{aligned}∫\frac{3𝑥^{2}−5𝑥+8}{(𝑥−3)^{2}(𝑥+1)}d𝑥 & =∫(\frac{2}{(𝑥−3)}+\frac{5}{(𝑥−3)^{2}}+\frac{1}{(𝑥+1)})d𝑥 \\ & =2∫\frac{1}{𝑥−3}d𝑥+5∫\frac{1}{(𝑥−3)^{2}}d𝑥+∫\frac{1}{𝑥+1}d𝑥 \\ & =2ln⁡|𝑥−3|+5(−\,\frac{1}{𝑥−3})+ln⁡|𝑥+1|+𝐾 \\ & =2ln⁡|𝑥−3|−\frac{5}{(𝑥−3)}+ln⁡|𝑥+1|+𝐾\,,\end{aligned}


$$

where $K$ is an integral constant.

### Example: Integrating Rational Functions With Repeated Factors of Degree Two That Require Factoring

#### Question

Evaluate $\displaystyle \int_{0}^{1} \dfrac{x}{x^2+2x+1} \,\textrm{d}x.$

#### Explanation

Let's first factor the denominator of the integrand:

$$


\dfrac{x}{x^2+2x+1} = \dfrac{x}{(x+1)^2}


$$

We must convert the integrand into a sum of partial fractions:

$$


\dfrac{x}{(x+1)^2} = \dfrac {A}{x+1} + \dfrac {B}{(x+1)^2}


$$

To determine the coefficients $A$ and $B,$ we first multiply both sides of the above equation by $(x+1)^2$ and get

$$


x= A(x+1)+B.


$$

Plugging in $x=-1,$ we can eliminate $A$ and solve for $B\mathbin{:}$

$$


\begin{aligned}−1 & =𝐴(−1+1)+𝐵 \\ 𝐵 & =−1\end{aligned}


$$

Now, plugging in $x=0$ and substituting the known value of $B,$ we can solve for $A\mathbin{:}$

$$


\begin{aligned}0 & =𝐴(0+1)+𝐵 \\ 0 & =𝐴+𝐵 \\ 0 & =𝐴−1 \\ 𝐴 & =1\end{aligned}


$$

Therefore, we can write the integrand as the partial sum

$$


\dfrac{x}{(x+1)^2} = \dfrac {1}{x+1} - \dfrac {1}{(x+1)^2}.


$$

Finally, we integrate this expression term by term to get

$$


\begin{aligned}∫_{10}^{}\frac{𝑥}{𝑥^{2}+2𝑥+1}\,d𝑥 & =∫_{10}^{}(\frac{1}{𝑥+1}−\frac{1}{(𝑥+1)^{2}})d𝑥 \\ & =∫_{10}^{}\frac{1}{𝑥+1}\,d𝑥−∫_{10}^{}\frac{1}{(𝑥+1)^{2}}\,d𝑥 \\ & =ln⁡|𝑥+1|_{10}^{}+\frac{1}{𝑥+1}_{10}^{} \\ & =(ln⁡|1+1|−ln⁡|0+1|)+(\frac{1}{1+1}−\frac{1}{0+1}) \\ & =(ln⁡2−ln⁡1)+(\frac{1}{2}−1) \\ & =ln⁡2−\frac{1}{2}.\end{aligned}


$$

### Example: Integrating a Rational Functions With a Repeated Factor of Degree Higher Than Two

#### Question

Evaluate $\displaystyle \int \dfrac{9x^2+2x-1}{(3x-1)^3}\textrm{d}x.$

#### Explanation

First, we convert the integrand into a sum of partial fractions:

$$


\begin{aligned}\frac{9𝑥^{2}+2𝑥−1}{(3𝑥−1)^{3}} & =\frac{𝐴}{(3𝑥−1)}+\frac{𝐵}{(3𝑥−1)^{2}}+\frac{𝐶}{(3𝑥−1)^{3}}\end{aligned}


$$

To determine the coefficients $A,$ $B,$ and $C,$ we first multiply both sides of the above equation by $(3x-1)^3$ and get

$$


\begin{aligned}9𝑥^{2}+2𝑥−1 & =𝐴(3𝑥−1)^{2}+𝐵(3𝑥−1)+𝐶.\end{aligned}


$$

Plugging in $x=\dfrac{1}{3},$ we can eliminate $A$ and $B$ and solve for $C\mathbin{:}$

$$


\begin{aligned}9(\frac{1}{3})^{2}+2(\frac{1}{3})−1 & =𝐴(3(\frac{1}{3})−1)^{2}+𝐵(3(\frac{1}{3})−1)+𝐶 \\ 𝐶 & =\frac{2}{3}\end{aligned}


$$

Plugging in $x=0$ and substituting the known value of $C,$ we get an equation relating $A$ and $B\mathbin{:}$

$$


\begin{aligned}9(0)^{2}+2(0)−1 & =𝐴(0−1)^{2}+𝐵(0−1)+𝐶 \\ −1 & =𝐴−𝐵+\frac{2}{3} \\ 𝐴−𝐵 & =−\frac{5}{3}\end{aligned}


$$

Plugging in $x=1$ and substituting the known value of $C,$ we get another equation relating $A$ and $B\mathbin{:}$

$$


\begin{aligned}9(1)^{2}+2(1)−1 & =𝐴(3(1)−1)^{2}+𝐵(3(1)−1)+𝐶 \\ 10 & =4𝐴+2𝐵+\frac{2}{3} \\ 2𝐴+𝐵 & =\frac{14}{3}\end{aligned}


$$

Adding our two equations $A-B=-\dfrac{5}{3}$ and $2A+B=\dfrac{14}{3},$ we get

$$


\begin{aligned}3𝐴 & =−\frac{5}{3}+\frac{14}{3} \\ 3𝐴 & =3 \\ 𝐴 & =1,\end{aligned}


$$

and substituting back into $2A+B=\dfrac{14}{3},$ we get

$$


\begin{aligned}2(1)+𝐵 & =\frac{14}{3} \\ 𝐵 & =\frac{8}{3}.\end{aligned}


$$

Therefore,

$$


\dfrac{9x^2+2x-1}{(3x-1)^3} = \dfrac{1}{(3x-1)} +\dfrac{8}{3(3x-1)^2} + \dfrac{2}{3(3x-1)^3}.


$$

Finally, we integrate this expression term by term, and get

$$


\begin{aligned}∫\frac{9𝑥^{2}+2𝑥−1}{(3𝑥−1)^{3}}d𝑥 & =∫(\frac{1}{(3𝑥−1)}+\frac{8}{3(3𝑥−1)^{2}}+\frac{2}{3(3𝑥−1)^{3}})d𝑥 \\ & =∫\frac{1}{3𝑥−1}d𝑥+\frac{8}{3}∫\frac{1}{(3𝑥−1)^{2}}d𝑥+\frac{2}{3}∫\frac{1}{(3𝑥−1)^{3}}d𝑥 \\ & =\frac{1}{3}ln⁡|3𝑥−1|+\frac{8}{3}(−\,\frac{1}{3(3𝑥−1)})+\frac{2}{3}(−\,\frac{1}{6(3𝑥−1)^{2}})+𝐾 \\ & =\frac{1}{3}ln⁡|3𝑥−1|−\frac{8}{9(3𝑥−1)}−\frac{1}{9(3𝑥−1)^{2}}+𝐾\,.\end{aligned}


$$
