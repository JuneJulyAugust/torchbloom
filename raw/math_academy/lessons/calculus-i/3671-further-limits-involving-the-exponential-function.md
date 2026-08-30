# Further Limits Involving the Exponential Function

Source: https://www.mathacademy.com/topics/3671?courseId=105
Topic ID: 3671

## Prerequisites

- [Limits of Trigonometric Functions](./1719-limits-of-trigonometric-functions.md)
- [Limits of Reciprocal Functions](./1905-limits-of-reciprocal-functions.md)
- [Limits Involving the Exponential Function](./2610-limits-involving-the-exponential-function.md)
- [Dividing Polynomials by Manipulating Rational Expressions](../algebra-ii/2883-dividing-polynomials-by-manipulating-rational-expressions.md)

## Lesson

### Introduction

Recall that Euler's number can be defined as the following special limit:

$$


e = \lim_{m \to \infty} \left(1+\dfrac{1}{m}\right)^{m}


$$

We can derive an alternative version of this limit by making the substitution

$$


n=\dfrac 1m.


$$

First, we note that if $m\to \infty$ then $n \to 0.$ Therefore, applying our substitution, we arrive at the following important result:

$$


e = \lim_{n \to 0} \left(1+{n}\right)^{1/n}


$$

### Evaluating a Limit Using the Alternative Limit Definition of Euler's Number

We have shown that Euler's number $e$ is given by the following limit:

$$


e = \lim_{n \to 0} \left(1+{n}\right)^{1/n}


$$

Let's use this result to evaluate

$$


\displaystyle{\lim_{n \to 0} \left(1+n\right)^{2/n}}.


$$

Notice that as $n \to 0,$

- the expression inside the parentheses approaches $1,$ while

- the exponent approaches $\infty.$

So, if we attempt to evaluate the limit directly, we get

$$


{\lim_{n \to 0} \left(1+n\right)^{2/n}} = 1^\infty,


$$

which is an indeterminate form.

However, by rewriting the given limit using the algebra of limits and then applying our special limit, we get the following:

$$


\begin{aligned}\underset{𝑛→0}{lim}(1+𝑛)^{2/𝑛} & =\underset{𝑛→0}{lim}(1+𝑛)^{2⋅1/𝑛} \\ & =\underset{𝑛→0}{lim}[(1+𝑛)^{1/𝑛}]^{2} \\ & =[\underset{𝑛→0}{lim}(1+𝑛)^{1/𝑛}]^{2} \\ & =𝑒^{2}\end{aligned}


$$

### Example: Evaluating a Limit Using the Alternative Limit Definition of Euler's Number

#### Question

Calculate $\displaystyle{\lim_{n \to 0} \left(1+n\right)^{5/2n}}.$

#### Explanation

Notice that as $n \to 0,$

- the expression inside the parentheses approaches $1,$ while

- the exponent approaches $\infty.$

So, if we attempt to evaluate the limit directly, we get

$$


{\lim_{n \to 0} \left(1+n\right)^{5/2n}} = 1^\infty,


$$

which is an indeterminate form.

Instead, let's recall the following special limit:

$$


\lim_{n \to 0} \left(1+n\right)^{1/n} = e


$$

Rewriting the given limit using the algebra of limits and applying our special limit, we get the following:

$$


\begin{aligned}\underset{𝑛→0}{lim}(1+𝑛)^{5/2𝑛} & =\underset{𝑛→0}{lim}[(1+𝑛)^{1/𝑛}]^{5/2} \\ & =[\underset{𝑛→0}{lim}(1+𝑛)^{1/𝑛}]^{5/2} \\ & =𝑒^{5/2} \\ & =\sqrt{√𝑒^{5}}\end{aligned}


$$

### Evaluating a Limit That Resembles a Special Limit Using a Variable Substitution

Let's take stock of our two special limit definitions of Euler's number:

- $\displaystyle e = \lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n}$

- $\displaystyle e = \lim_{n \to 0} \left(1+n\right)^{1/n}$

We can use these results to evaluate more complex limits. For example, suppose we wish to evaluate the following limit:

$$


\displaystyle{\lim_{x \to \infty} \left(1+\dfrac{2}{x+3}\right)^{x+3}}


$$

Notice that as $x \to \infty,$

- the expression inside the parentheses approaches $1,$ while

- the exponent approaches $\infty.$

So, if we attempt to evaluate the limit directly, we get

$$


{\lim_{x \to \infty} \left(1+\dfrac{2}{x+3}\right)^{x+3}} = 1^\infty,


$$

which is an indeterminate form.

Instead, let's recall the following special limit:

$$


\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^n = e


$$

In the given limit, we let $\dfrac{2}{x+3}=\dfrac{1}{n}.$ Thus, we have

$$


\begin{aligned}\frac{2}{𝑥+3} & =\frac{1}{𝑛} \\ 𝑥+3 & =2𝑛.\end{aligned}


$$

Therefore, since $n \to \infty$ as $x \to \infty,$ we rewrite the given limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑥→∞}{lim}(1+\frac{2}{𝑥+3})^{𝑥+3} & =\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{2𝑛} \\ & =\underset{𝑛→∞}{lim}[(1+\frac{1}{𝑛})^{𝑛}]^{2} \\ & =[\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{𝑛}]^{2} \\ & =𝑒^{2}\end{aligned}


$$

### Example: Evaluating a Limit Using a Variable Substitution

#### Question

Calculate $\displaystyle{\lim_{z \to 0} \left(1+4z\right)^{-5/z}}.$

#### Explanation

Notice that as $z \to 0,$

- the expression inside the parentheses approaches $1,$ while

- the exponent approaches $-\infty.$

So, if we attempt to evaluate the limit directly, we get

$$


{\lim_{z \to 0} \left(1+4z\right)^{-5/z}} = 1^{-\infty},


$$

which is an indeterminate form.

Instead, let's recall the following special limit:

$$


\lim_{n \to 0} \left(1+n\right)^{1/n} = e


$$

In the given limit, we let $4z=n.$ Thus, we have

$$


\begin{aligned}4𝑧 & =𝑛 \\ 𝑧 & =\frac{𝑛}{4} \\ \frac{1}{𝑧} & =\frac{4}{𝑛}.\end{aligned}


$$

Therefore, since $n \to 0$ as $z \to 0,$ we rewrite the given limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑧→0}{lim}(1+4𝑧)^{−5/𝑧} & =\underset{𝑧→0}{lim}(1+4𝑧)^{−5(1/𝑧)} \\ & =\underset{𝑛→0}{lim}(1+𝑛)^{−5(4/𝑛)} \\ & =\underset{𝑛→0}{lim}[(1+𝑛)^{1/𝑛}]^{−20} \\ & =[\underset{𝑛→0}{lim}(1+𝑛)^{1/𝑛}]^{−20} \\ & =𝑒^{−20} \\ & =\frac{1}{𝑒^{20}}\end{aligned}


$$

### Evaluating a Limit Containing a Minus Sign Using a Variable Substitution

Let's consider the following limit:

$$


{\lim_{x \to 0} \left(1-\sin{x}\right)^{3/\sin{x}}}


$$

Notice that as $x \to 0,$

- the expression inside the parentheses approaches $1,$ while

- the exponent approaches $\infty.$

So, if we attempt to evaluate the limit directly, we get

$$


\lim_{x \to 0} \left(1-\sin{x}\right)^{3/\sin{x}} = 1^{\infty},


$$

which is an indeterminate form.

Instead, let's recall the following special limit:

$$


\lim_{n \to 0} \left(1+n\right)^{1/n} = e


$$

We rewrite the given limit as follows:

$$


\begin{aligned}\underset{𝑥→0}{lim}(1−sin⁡𝑥)^{3/sin⁡𝑥} & =\underset{𝑥→0}{lim}(1+(−sin⁡𝑥))^{3/sin⁡𝑥}\end{aligned}


$$

Let $-\sin{x}=n.$ Therefore, since $n \to 0$ as $x \to 0,$ we rewrite the limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑥→0}{lim}(1−sin⁡𝑥)^{3/sin⁡𝑥} & =\underset{𝑥→0}{lim}(1+(−sin⁡𝑥))^{3/sin⁡𝑥} \\ & =\underset{𝑛→0}{lim}(1+𝑛)^{3/(−𝑛)} \\ & =\underset{𝑛→0}{lim}[(1+𝑛)^{1/𝑛}]^{−3} \\ & =[\underset{𝑛→0}{lim}(1+𝑛)^{1/𝑛}]^{−3} \\ & =𝑒^{−3} \\ & =\frac{1}{𝑒^{3}}\end{aligned}


$$

### Example: Evaluating a Limit Using a Variable Substitution: Advanced Cases

#### Question

Evaluate $\displaystyle \lim_{x \to \infty} \left(\dfrac{x+3}{x+1}\right)^{x+3}.$

#### Explanation

Notice that as $x \to \infty,$

- the expression inside the parentheses approaches $1,$ while

- the exponent approaches $\infty.$

So, if we attempt to evaluate the limit directly, we get

$$


\lim_{x \to \infty} \left(\dfrac{x+3}{x+1}\right)^{x+3} = 1^\infty,


$$

which is an indeterminate form.

Instead, let's recall the following special limit:

$$


\lim_{n \to \infty} \left(1+\dfrac{1}{n}\right)^{n} = e


$$

We rewrite the given limit as follows:

$$


\begin{aligned}\underset{𝑥→∞}{lim}(\frac{𝑥+3}{𝑥+1})^{𝑥+3} & =\underset{𝑥→∞}{lim}(\frac{(𝑥+1)+2}{𝑥+1})^{𝑥+3} \\ & =\underset{𝑥→∞}{lim}(1+\frac{2}{𝑥+1})^{𝑥+3}\end{aligned}


$$

Let $\dfrac{2}{x+1}=\dfrac{1}{n}.$ Then, we have

$$


\begin{aligned}\frac{2}{𝑥+1} & =\frac{1}{𝑛} \\ 𝑥+1 & =2𝑛 \\ 𝑥 & =2𝑛−1.\end{aligned}


$$

Therefore, since $n \to \infty$ as $x \to \infty,$ we rewrite the limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑥→∞}{lim}(\frac{𝑥+3}{𝑥+1})^{𝑥+3} & =\underset{𝑥→∞}{lim}(1+\frac{2}{𝑥+1})^{𝑥+3} \\ & =\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{(2𝑛−1)+3} \\ & =\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{2𝑛+2} \\ & =\underset{𝑛→∞}{lim}[(1+\frac{1}{𝑛})^{2𝑛}⋅(1+\frac{1}{𝑛})^{2}] \\ & =\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{2𝑛}⋅\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{2} \\ & =\underset{𝑛→∞}{lim}[(1+\frac{1}{𝑛})^{𝑛}]^{2}⋅1^{2} \\ & =[\underset{𝑛→∞}{lim}(1+\frac{1}{𝑛})^{𝑛}]^{2} \\ & =𝑒^{2}\end{aligned}


$$
