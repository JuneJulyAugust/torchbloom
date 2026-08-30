# Integrating Rational Functions with Irreducible Quadratic Factors

Source: https://www.mathacademy.com/topics/447?courseId=21
Topic ID: 447

## Prerequisites

- [Integration by Substitution With Inverse Trigonometric Functions](../ap-calculus-ab/315-integration-by-substitution-with-inverse-trigonometric-functions.md)
- [Integrating Rational Functions Using Partial Fractions](./445-integrating-rational-functions-using-partial-fractions.md)
- [Expressing Rational Functions with Irreducible Quadratic Factors as Sums of Partial Fractions](./1063-expressing-rational-functions-with-irreducible-quadratic-factors-as-sums-of-partial-fractions.md)

## Lesson

### Introduction

To perform partial fraction decomposition, we always need to factor the denominator as much as possible before using the factors to write the partial fractions.

Sometimes, however, we get **irreducible quadratic factors** that cannot be written as a product of linear factors with real coefficients. For example, the factor $x^2+4$ is irreducible.

Remember that in the partial fraction corresponding to an irreducible quadratic factor, the numerator is a linear expression. For example,

$$


\begin{aligned}\frac{2𝑥+3}{(𝑥^{2}+4)(𝑥−1)} & =\frac{𝐴𝑥+𝐵}{(𝑥^{2}+4)}+\frac{𝐶}{(𝑥−1)}\,.\end{aligned}


$$

In general:

- Any expression of the form $x^2+c,$ where $c>0,$ is irreducible.

- Any expression of the form $ax^2 + bx + c$ is irreducible if the discriminant $\mathcal{D}$ is negative, i.e., if $\mathcal{D} = b^2 - 4ac < 0.$

- Any expression of the form $ax^2 + bx + c$ is irreducible (over the rational numbers) if the discriminant $\mathcal{D} > 0$ is not a perfect square. For example, if $\mathcal D = 5,$ then the quadratic term does not factor over the rational numbers because $\sqrt{\mathcal{D}} = \sqrt 5$ is not a rational number.

### Example: Integrating a Rational Function Given Part Of the Partial Fraction Decomposition

#### Question

Given that

$$


\dfrac{4x^2-6}{(x-3)(x^2+1)} = \dfrac{A}{x-3} + \dfrac{x+3}{x^2 + 1},


$$

where $A$ is a constant to be found, calculate $\displaystyle{\int \dfrac{4x^2-6}{(x-3)(x^2+1)}\,\textrm d x}.$

#### Explanation

First, we find the constant $A.$ Multiplying both sides of the given equality by $(x-3)(x^2 + 1)$ gives

$$


\begin{aligned}4𝑥^{2}−6=𝐴(𝑥^{2}+1)+𝑥^{2}−9.\end{aligned}


$$

Substituting $x=0$ into the above gives

$$


\begin{aligned}4(0)^{2}−6 & =𝐴(0^{2}+1)+0^{2}−9 \\ −6 & =𝐴−9 \\ 𝐴 & =3.\end{aligned}


$$

We now integrate this function term by term, adding the constant of integration at the very end.

$$


\begin{aligned} \int \dfrac{4x^2 - 6}{(x-3)(x^2+1)} \, \textrm{d}x & = \int \left(\dfrac{3}{x-3} + \dfrac{x+3}{x^2 + 1}\right) \textrm{d}x \\\[5pt] & = 3\int\dfrac{1}{x-3}\,\textrm{d}x + \int \dfrac{x}{x^2+1}\,\textrm d x + 3\int \dfrac{1}{x^2 + 1} \, \textrm{d}x \end{aligned}


$$

For the first integral, we get

$$


\int \dfrac{1}{x-3} \textrm{d}x = \ln|x-3|.


$$

For the second integral, we use the substitution $x^2 + 1 = u.$ Then, $2x\,\textrm{d}x=\textrm{d}u,$ and we get

$$


\begin{aligned} \int \dfrac{x}{x^2+1}\,\textrm{d}x & = \int \left(\dfrac{1}{u}\right) \dfrac{\textrm d u}{2} \\\[5pt] &= \dfrac{1}{2}\ln \vert u\vert \\\[5pt] &= \dfrac{1}{2}\ln \vert x^2 + 1\vert \\\[5pt] & = \dfrac{1}{2}\ln \left(x^2+1\right). \end{aligned}


$$

Finally, for the third integral, we use the fact that $\displaystyle \int \dfrac{1}{x^2 + a^2} \, \textrm{d}x = \dfrac{1}{a}\arctan\left(\dfrac{x}{a}\right),$ which results in

$$


\int \dfrac{1}{x^2+1}\,\textrm{d}x = \arctan{x}.


$$

So, we get the following result:

$$


\begin{aligned}∫\frac{4𝑥^{2}−6}{(𝑥−3)(𝑥^{2}+1)}\,d𝑥 & =3∫\frac{1}{𝑥−3}\,d𝑥+∫\frac{𝑥}{𝑥^{2}+1}\,d𝑥+3∫\frac{1}{𝑥^{2}+1}\,d𝑥 \\ & =3ln⁡|𝑥−3|+\frac{1}{2}ln⁡(𝑥^{2}+1)+3arctan⁡𝑥+𝐶\end{aligned}


$$

### Example: Integrating a Rational Function With an Irreducible Binomial Quadratic Factor

#### Question

Calculate $\displaystyle \int \dfrac{2x+3}{(x^2+4)(x-1)} \, \textrm{d}x.$

#### Explanation

The quadratic factor $x^2+4$ is irreducible, so we proceed with the following partial fraction decomposition:

$$


\begin{aligned}\frac{2𝑥+3}{(𝑥^{2}+4)(𝑥−1)} & =\frac{𝐴𝑥+𝐵}{(𝑥^{2}+4)}+\frac{𝐶}{(𝑥−1)}\end{aligned}


$$

To determine the coefficients $A,$ $B,$ and $C,$ we first multiply both sides of the above equation by $(x^2+4)(x-1),$ and we get

$$


\begin{aligned}2𝑥+3 & =(𝐴𝑥+𝐵)(𝑥−1)+𝐶(𝑥^{2}+4)\,.\end{aligned}


$$

Solving for the unknown constants using the usual methods, we get $A=-1, B=1,$ and $C=1.$ Therefore,

$$


\dfrac{2x+3}{(x^2+4)(x-1)} = \dfrac{-x+1}{x^2+4} +\dfrac{1}{x-1}.


$$

Now we integrate this function term by term, adding the constant of integration at the very end.

$$


\begin{aligned}∫\frac{2𝑥+3}{(𝑥^{2}+4)(𝑥−1)}\,d𝑥 & =∫(\frac{−𝑥+1}{𝑥^{2}+4}+\frac{1}{𝑥−1})d𝑥 \\ & =−∫\frac{𝑥}{𝑥^{2}+4}\,d𝑥+∫\frac{1}{𝑥^{2}+4}\,d𝑥+∫\frac{1}{𝑥−1}\,d𝑥\end{aligned}


$$

For the first integral, we use the substitution $u = x^2+4.$ Then $2x\,\textrm{d}x=\textrm{d}u,$ and we get

$$


\begin{aligned}∫\frac{𝑥}{𝑥^{2}+4}\,d𝑥 & =∫(\frac{1}{𝑢})\frac{d𝑢}{2} \\ & =\frac{1}{2}ln⁡|𝑢| \\ & =\frac{1}{2}ln⁡𝑥^{2}+4 \\ & =\frac{1}{2}ln⁡(𝑥^{2}+4).\end{aligned}


$$

For the second integral, we use the fact that $\displaystyle \int \dfrac{1}{x^2+a^2} \, \textrm{d}x = \dfrac{1}{a}\arctan\left(\dfrac{x}{a}\right),$ which results in

$$


\begin{aligned}∫\frac{1}{𝑥^{2}+4}\,d𝑥 & =\frac{1}{2}arctan⁡(\frac{𝑥}{2}).\end{aligned}


$$

Finally, for the third integral we have

$$


\begin{aligned}∫\frac{1}{𝑥−1}d𝑥 & =ln⁡|𝑥−1|.\end{aligned}


$$

So we get the following result:

$$


\begin{aligned}∫\frac{2𝑥+3}{(𝑥^{2}+4)(𝑥−1)}\,d𝑥 & =−∫\frac{𝑥}{𝑥^{2}+4}\,d𝑥+∫\frac{1}{𝑥^{2}+4}\,d𝑥+∫\frac{1}{𝑥−1}\,d𝑥 \\ & =−\frac{1}{2}ln⁡(𝑥^{2}+4)+\frac{1}{2}arctan⁡(\frac{𝑥}{2})+ln⁡|𝑥−1|+𝐾\end{aligned}


$$

### Example: Integrating a Rational Function With an Irreducible Trinomial Quadratic Factor

#### Question

Evaluate $\displaystyle \int \dfrac{4x^2-x}{(x^2+x+1)(x-2)} \, \textrm{d}x.$

#### Explanation

Notice that the quadratic factor in the denominator has a negative discriminant:

$$


\mathcal{D} = 1^2 - 4(1)(1) = -3 < 0


$$

So, we proceed with the following partial fraction decomposition:

$$


\begin{aligned}\frac{4𝑥^{2}−𝑥}{(𝑥^{2}+𝑥+1)(𝑥−2)} & =\frac{𝐴𝑥+𝐵}{𝑥^{2}+𝑥+1}+\frac{𝐶}{𝑥−2}\end{aligned}


$$

To determine the coefficients $A,$ $B,$ and $C,$ we first multiply both sides of the above equation by $(x^2+x+1)(x-2)$ and get

$$


\begin{aligned}4𝑥^{2}−𝑥 & =(𝐴𝑥+𝐵)(𝑥−2)+𝐶(𝑥^{2}+𝑥+1).\end{aligned}


$$

Solving for the unknown constants using the usual methods, we get $A=2,$ $B=1,$ and $C=2.$ Therefore,

$$


\dfrac{4x^2-x}{(x^2+x+1)(x-2)} = \dfrac{2x+1}{x^2+x+1} + \dfrac{2}{x-2}.


$$

Now we integrate this function term by term, adding the constant of integration only at the very end.

$$


\begin{aligned}∫\frac{4𝑥^{2}−𝑥}{(𝑥^{2}+𝑥+1)(𝑥−2)}\,d𝑥 & =∫(\frac{2𝑥+1}{𝑥^{2}+𝑥+1}+\frac{2}{𝑥−2})d𝑥 \\ & =∫\frac{2𝑥+1}{𝑥^{2}+𝑥+1}\,d𝑥+2∫\frac{1}{𝑥−2}\,d𝑥\end{aligned}


$$

For the first integral, we use the substitution $u = x^2+x+1.$ Then $(2x+1) \, \textrm{d}x=\textrm{d}u,$ and we get

$$


\begin{aligned}∫\frac{2𝑥+1}{𝑥^{2}+𝑥+1}\,d𝑥 & =∫(\frac{1}{𝑢})d𝑢 \\ & =ln⁡|𝑢| \\ & =ln⁡𝑥^{2}+𝑥+1 \\ & =ln⁡(𝑥^{2}+𝑥+1).\end{aligned}


$$

For the second integral we have

$$


\begin{aligned}∫\frac{1}{𝑥−2}\,d𝑥 & =ln⁡|𝑥−2|.\end{aligned}


$$

So we get the following result:

$$


\begin{aligned}∫\frac{4𝑥^{2}−𝑥}{(𝑥^{2}+𝑥+1)(𝑥−2)}\,d𝑥 & =∫\frac{2𝑥+1}{𝑥^{2}+𝑥+1}\,d𝑥+2∫\frac{1}{𝑥−2}\,d𝑥 \\ & =ln⁡(𝑥^{2}+𝑥+1)+2ln⁡|𝑥−2|+𝐾\end{aligned}


$$
