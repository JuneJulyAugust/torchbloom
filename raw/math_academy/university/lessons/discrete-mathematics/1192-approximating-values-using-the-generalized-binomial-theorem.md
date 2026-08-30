# Approximating Values Using the Generalized Binomial Theorem

Source: https://www.mathacademy.com/topics/1192?courseId=109
Topic ID: 1192

## Prerequisites

- [Working With the Generalized Binomial Theorem](./695-working-with-the-generalized-binomial-theorem.md)
- [Approximating Values Using the Binomial Theorem](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/1158-approximating-values-using-the-binomial-theorem.md)

## Lesson

### Introduction

Recall that, for a rational number $n,$ the generalized binomial theorem states that for $|x| < 1,$ we have

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)}{2!}x^2 + \dfrac{n(n-1)(n-2)}{3!}x^3 + \cdots.



$$

We can often use the first few terms of a binomial expansion to approximate numerical expressions to high degrees of accuracy.

For example, consider the binomial expansion

$$



\sqrt{1+4x} = 1 + 2x - 2x^2 + 4x^3 - \cdots.



$$

The range of validity for this expansion is $|x|<\dfrac{1}{4}$. Let's use this to find an approximation to $\sqrt{1.04}.$

First, note that if $x$ is sufficiently small, we only need to keep the first few terms of the expansion to obtain a high-accuracy approximation. Therefore, for sufficiently small $x,$ we have

$$



\sqrt{1+4x} \approx 1 + 2x - 2x^2 + 4x^3.



$$

Next, we find the exact value of $x$ that needs to be plugged into the expansion formula. Since we require an approximation $\sqrt{1.04},$ we equate $1.04$ with the expression underneath the radical in our binomial approximation. This gives the equation

$$



1+4x = 1.04



$$

Solving this equation, we get $x=0.01.$ Notice that this $x$-value lies within the permitted range of validity.

$$



|0.01| < 0.25 = \dfrac{1}{4}



$$

Finally, we obtain our approximation by substituting $x=0.01$ into the binomial approximation and evaluating:

$$



\begin{aligned}\sqrt{1.04} & =\sqrt{1+4(0.01)} \\ & ≈1+2(0.01)−2(0.01)^{2}+4(0.01)^{3} \\ & =1+0.02−0.000\,2+0.000\,004 \\ & ≈1.020\end{aligned}



$$

rounded to three decimal places.

### Example: Approximating Values of Radicals Using a Given Binomial Expansion

#### Question

Consider the binomial expansion

$$



\dfrac{7}{\sqrt{9-3x}} = \dfrac73 + \dfrac{7}{18}x + \dfrac{7}{72}x^2 + \cdots, \qquad |x| < 3.



$$

By selecting a suitable value of $x,$ approximate the value of $\sqrt{7}$ to $3$ decimal places.

#### Explanation

Since we want to approximate $\sqrt{7}$ using $\dfrac{7}{\sqrt{9-3x}},$ we find a suitable value of $x$ by equating the expressions and solving for $x{:}$

$$



\begin{aligned}\sqrt{7} & =\frac{7}{\sqrt{9−3𝑥}} \\ \sqrt{9−3𝑥} & =\sqrt{7} \\ 9−3𝑥 & =7 \\ −3𝑥 & =−2 \\ 𝑥 & =\frac{2}{3}\end{aligned}



$$

Note that, since $\left|\dfrac23\right| < 3,$ this value of $x$ lies within the permitted range of validity.

Therefore, we can approximate the value of $\sqrt{7}$ by substituting $x=\dfrac23$ into the given expansion. Doing so, we conclude that

$$



\begin{aligned}\frac{7}{\sqrt{9−3(\frac{2}{3})}} & ≈\frac{7}{3}+\frac{7}{18}(\frac{2}{3})+\frac{7}{72}(\frac{2}{3})^{2} \\ \frac{7}{\sqrt{9−2}} & ≈\frac{7}{3}+\frac{7}{27}+\frac{7}{162} \\ \frac{7}{\sqrt{7}} & ≈\frac{427}{162} \\ \sqrt{7} & ≈2.636,\end{aligned}



$$

rounded to $3$ decimal places.

### Example: Approximating Values of Radicals

#### Question

Approximate the value of $\sqrt{68}$ using the first three terms of the binomial expansion of $10\sqrt{1-2x}.$

#### Explanation

The generalized binomial formula states that

$$



(1+x)^n = 1 + nx + \dfrac{n(n-1)x^2}{2!} +\cdots.



$$

First, we rewrite the given expression as

$$



10\sqrt{1-2x} = 10(1-2x)^{1/2}.



$$

Now, applying the generalized binomial formula with $n=\dfrac12$ and $-2x$ instead of $x,$ we obtain

$$



\begin{aligned}10\sqrt{1−2𝑥} & =10(1−2𝑥)^{1/2} \\ & =101+(\frac{1}{2})(−2𝑥)+\frac{(\frac{1}{2})(\frac{1}{2}−1)(−2𝑥)^{2}}{2}+⋯ \\ & =101−𝑥+\frac{(\frac{1}{2})(−\frac{1}{2})4𝑥^{2}}{2}+⋯ \\ & =10[1−𝑥−\frac{1}{2}𝑥^{2}+⋯] \\ & =10−10𝑥−5𝑥^{2}+⋯.\end{aligned}



$$

The binomial expansion is valid for $|-2x| < 1$ or, equivalently, for $|x| < \dfrac12.$

Since we want to approximate $\sqrt{68}$ using $10\sqrt{1-2x},$ we find a suitable value of $x$ by equating the expressions and solving for $x{:}$

$$



\begin{aligned}10\sqrt{1−2𝑥} & =\sqrt{68} \\ 100(1−2𝑥) & =68 \\ 100−200𝑥 & =68 \\ 32 & =200𝑥 \\ 𝑥 & =0.16\end{aligned}



$$

Note that, since $|0.16| < \dfrac 12,$ this value lies within the permitted range of validity.

Therefore, we can approximate the value of $\sqrt{68}$ by substituting $x=0.16$ into the given expansion. Doing so, we conclude that

$$



\begin{aligned}10\sqrt{1−2(0.16)} & ≈10−10(0.16)−5(0.16)^{2} \\ \sqrt{10^{2}⋅(1−0.32)} & ≈10−1.6−0.128 \\ \sqrt{68} & ≈8.272.\end{aligned}



$$
