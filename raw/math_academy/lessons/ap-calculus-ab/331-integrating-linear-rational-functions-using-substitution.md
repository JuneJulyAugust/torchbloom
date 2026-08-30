# Integrating Linear Rational Functions Using Substitution

Source: https://www.mathacademy.com/topics/331?courseId=24
Topic ID: 331

## Prerequisites

- [Integrating Algebraic Functions Using Substitution](./334-integrating-algebraic-functions-using-substitution.md)
- [Integrating the Reciprocal Function](./1361-integrating-the-reciprocal-function.md)

## Lesson

### Introduction

Suppose that we want to calculate an integral like

$$


\displaystyle \int \dfrac{1}{2x+1} \, \textrm{d}x.


$$

We know that $\displaystyle \int \dfrac{1}{x} \, \textrm dx = \ln |x|,$ but our case is different because now it's a whole function $(2x+1)$ that is in the denominator.

For integrals like the one above, we can use a substitution. First, let $u=2x+1.$ Then differentiating with respect to $x$ gives

$$


\dfrac{\textrm d u}{\textrm d x} = 2\quad\Longrightarrow\quad \textrm d x = \dfrac 1 2 \, \textrm d u.


$$

We can now rewrite the integral in terms of $u$ and solve it:

$$


\begin{aligned}∫\frac{1}{2𝑥+1}\,d𝑥 & =∫\frac{1}{𝑢}⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫\frac{1}{𝑢}\,d𝑢 \\ & =\frac{1}{2}ln⁡|𝑢|+𝐶\end{aligned}


$$

Lastly, we write the final answer in terms of $x$:

$$


\begin{aligned}∫\frac{1}{2𝑥+1}\,d𝑥 & =\frac{1}{2}ln⁡|2𝑥+1|+𝐶\end{aligned}


$$

**Note:** After solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}[\frac{1}{2}ln⁡|2𝑥+1|+𝐶] & =\frac{1}{2}⋅\frac{d}{d𝑥}[ln⁡|2𝑥+1|]+\frac{d}{d𝑥}(𝐶) \\ & =\frac{1}{2}⋅\frac{1}{2𝑥+1}⋅\frac{d}{d𝑥}(2𝑥+1)+0 \\ & =\frac{1}{2(2𝑥+1)}⋅2 \\ & =\frac{1}{2𝑥+1}\,✓\end{aligned}


$$

### Example: Integrating a Linear Rational Function

#### Question

Calculate $\displaystyle{\int \dfrac{3}{5x+2}\textrm{d}x}.$

#### Explanation

First, let $u=5x+2.$ Then differentiating with respect to $x$ gives

$$


\dfrac{\textrm d u}{\textrm d x} = 5\quad\Longrightarrow\quad \textrm d x = \dfrac 1 5 \textrm d u.


$$

We can now rewrite the integral in terms of $u,$ solve it, and write the final answer in terms of $x$ as follows:

$$


\begin{aligned}∫\frac{3}{5𝑥+2}d𝑥 & =3∫\frac{1}{5𝑥+2}d𝑥 \\ & =3∫\frac{1}{𝑢}⋅\frac{1}{5}\,d𝑢 \\ & =\frac{3}{5}∫\frac{1}{𝑢}\,d𝑢 \\ & =\frac{3}{5}ln⁡|𝑢|+𝐶 \\ & =\frac{3}{5}ln⁡|5𝑥+2|+𝐶\end{aligned}


$$

### Example: Integrating a Linear Rational Function and Simplifying the Arbitrary Constant

#### Question

Calculate $\displaystyle{\int \dfrac{1}{1+2x}\textrm{d}x},$ writing your final answer as a single function.

#### Explanation

First, let $u=1+2x.$ Then differentiating with respect to $x$ gives

$$


\dfrac{\textrm d u}{\textrm d x} = 2\quad\Longrightarrow\quad \textrm d x = \dfrac 1 2 \textrm d u.


$$

We can now rewrite the integral in terms of $u,$ solve it, and write the final answer in terms of $x$ as follows:

$$


\begin{aligned}∫\frac{1}{1+2𝑥}d𝑥 & =∫\frac{1}{𝑢}⋅\frac{1}{2}\,d𝑢 \\ & =\frac{1}{2}∫\frac{1}{𝑢}\,d𝑢 \\ & =\frac{1}{2}ln⁡|𝑢|+𝐶 \\ & =\frac{1}{2}ln⁡|1+2𝑥|+𝐶\end{aligned}


$$

We can further simplify the above by writing $C = \dfrac 1 2\ln K$ for another arbitrary constant $K > 0,$ and then we can combine the two terms using the laws of logarithms, as follows:

$$


\begin{aligned}\frac{1}{2}ln⁡|1+2𝑥|+𝐶 & =\frac{1}{2}ln⁡|1+2𝑥|+\frac{1}{2}ln⁡𝐾 \\ & =\frac{1}{2}ln⁡(𝐾⋅|1+2𝑥|) \\ & =\frac{1}{2}ln⁡(𝐾|1+2𝑥|)\end{aligned}


$$

So, we finally conclude that

$$


\int \dfrac{1}{1+2x}\textrm{d}x = \dfrac 1 2 \ln \left(K |1+2x|\right).


$$

### The General Formula

In general,

$$


\int \dfrac{1}{ax+b}\,\textrm d x = \dfrac 1 a \ln|ax+b| + C.


$$

These types of integrals come up quite often in calculus, so it's worth remembering this formula.

### Example: Integrating a Combination of Linear Rational Functions Using the General Formula

#### Question

Calculate $\displaystyle \int\left(\dfrac{1}{1+2x} + \dfrac{1}{1-2x}\right)\,\textrm d x.$

#### Explanation

Let's solve this using the general formula:

$$


\begin{aligned}∫(\frac{1}{1+2𝑥}+\frac{1}{1−2𝑥})\,d𝑥 & =∫\frac{1}{1+2𝑥}\,d𝑥+∫\frac{1}{1−2𝑥}\,d𝑥 \\ & =\frac{1}{2}ln⁡|1+2𝑥|−\frac{1}{2}ln⁡|1−2𝑥|+𝐶 \\ & =\frac{1}{2}ln⁡\frac{1+2𝑥}{1−2𝑥}+\frac{1}{2}ln⁡𝐾 \\ & =\frac{1}{2}ln⁡(𝐾\frac{1+2𝑥}{1−2𝑥})\end{aligned}


$$

Notice that we used the laws of logarithms to write the result as a single logarithm.
