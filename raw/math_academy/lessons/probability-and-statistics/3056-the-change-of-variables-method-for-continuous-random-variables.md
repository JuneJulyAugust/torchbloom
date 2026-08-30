# The Change-of-Variables Method for Continuous Random Variables

Source: https://www.mathacademy.com/topics/3056?courseId=73
Topic ID: 3056

## Prerequisites

- [Inverses of Exponential and Logarithmic Functions](../algebra-ii/1472-inverses-of-exponential-and-logarithmic-functions.md)
- [The Distribution Function Method](./3055-the-distribution-function-method.md)
- [Inverses of Quadratic Functions](../algebra-ii/3830-inverses-of-quadratic-functions.md)
- [Inverses of Radical Functions](../algebra-ii/3943-inverses-of-radical-functions.md)
- [Inverses of Reciprocal Functions](../algebra-ii/3944-inverses-of-reciprocal-functions.md)

## Lesson

### Introduction

Let $X$ be a continuous random variable whose probability density function is known. We know that if $Y = u(X),$ then we can apply the distribution function method to compute the PDF of $Y.$

It's possible to generalize the distribution function method when $u(X)$ is strictly monotonic. This generalization is known as the **change-of-variables method**, and is stated below:

*If $X\in (a,b)$ is a continuous random variable with probability density function $f_X$ and $Y = u(X),$ where the function $u(x)$ is strictly monotonic, then according to the change-of-variables method, the probability density function of $Y$ is given by*

$$


\begin{aligned}𝑓_{𝑋}(𝑢^{−1}(𝑦))⋅(𝑢^{−1})^{′}(𝑦), & 𝑦 is between 𝑢(𝑎) and 𝑢(𝑏) \\ 0, & otherwise.\end{aligned}


$$

Proof of this result will be provided at the end of the lesson.

The advantage of the change-of-variables method is that it's often easier and faster to implement than the distribution function method. The disadvantage is that it only works when $u$ is monotonic, whereas the distribution function method can be extended to deal with non-monotonic functions.

For example, suppose that $X$ has the probability density function

$$


\begin{aligned}\frac{1}{2}𝑥, & 0<𝑥<2 \\ 0, & otherwise.\end{aligned}


$$

Let the random variable $Y = 3X.$ Then $u(x) = 3x,$ which is strictly monotonically increasing. Therefore, the change-of-variables method can be used to compute the PDF of $Y.$

First, we find $u^{-1}(y)$ as follows:

$$


\begin{aligned}𝑢(𝑦) & =3𝑦 \\ 𝑦 & =3𝑢^{−1}(𝑦) \\ 𝑢^{−1}(𝑦) & =\frac{1}{3}𝑦\end{aligned}


$$

Then, we find $(u^{-1})'(y){:}$

$$


u^{-1}(y) = \dfrac{1}{3}y \quad \Longrightarrow \quad (u^{-1})'(y) = \dfrac{1}{3}


$$

According to the change-of-variables method, for nonzero $f_Y,$ we have

$$


\begin{aligned}𝑓_{𝑌}(𝑦) & =𝑓_{𝑋}(𝑢^{−1}(𝑦))⋅(𝑢^{−1})^{′}(𝑦) \\ & =𝑓_{𝑋}(\frac{1}{3}𝑦)⋅\frac{1}{3} \\ & =\frac{1}{2}(\frac{1}{3}𝑦)⋅\frac{1}{3} \\ & =\frac{1}{18}𝑦.\end{aligned}


$$

Finally, since $f_X$ is nonzero on $0 < x < 2,$ the bounds are $a=0$ and $b=2,$ and we have

$$


u(0) = 0, \qquad u(2) = 6.


$$

Therefore, the probability distribution of $Y$ is

$$


\begin{aligned}\frac{1}{18}𝑦, & 0<𝑦<6 \\ 0, & otherwise.\end{aligned}


$$

### Example: Identifying Transformations Where the Change-of-Variables Method Is Applicable

#### Question

Suppose that $X$ is a continuous random variable. For which of the following transformations can the change-of-variables method be applied to find the probability density function of $Y?$

1. $Y = X^4,$ where $X\in (0,2)$

2. $Y = \cos X,$ where $X\in (-\infty, \infty)$

3. $Y = e^{-X},$ where $X\in (0, \infty)$

#### Explanation

The change-of-variables method can be applied when a transformation $Y = u(X)$ is strictly increasing or strictly decreasing (i.e., strictly monotonic) over the entire support of $X.$

With that in mind, let's inspect each transformation in turn.

- Transformation I is strictly monotonic. The function $u(x) = x^4$ is strictly increasing for $x\in (0,2).$

- Transformation II is ** strictly monotonic. For example, $u(x) = \cos x$ is decreasing on $x \in \left(0,\pi \right)$ and increasing on $x \in \left(\pi,2\pi\right).$

- Transformation III is strictly monotonic. The function $u(x) =e^{-x}$ is strictly decreasing for $x\in (0,\infty).$

Therefore, the correct answer is "I and III only."

### Example: Computing the PDF of a Random Variable Under an Affine Transformation

#### Question

Let be a continuous random variable with the following probability density function:

If use the change-of-variables method to find the probability density function of

#### Explanation

If is a continuous random variable with probability density function and where the function is strictly monotonic, then according to the change-of-variables method, the probability density function of is given by

The transformation is strictly monotonically **, so the change-of-variables method can be used.

First, we find. Since

we solve for:

Therefore,

Then, we find

According to the change-of-variables method, for nonzero we have

Finally, since is nonzero on the bounds are and we have

Therefore, the probability density function of is

### Example: Computing the PDF of a Random Variable Under a Nonlinear Transformation

#### Question

Let $X$ be a continuous random variable with the following probability density function:

$$


\begin{aligned}3𝑥^{2}, & 0<𝑥<1 \\ 0, & otherwise\end{aligned}


$$

If $Y = \sqrt{X},$ use the change-of-variables method to find the probability density function of $Y.$

#### Explanation

If $X \in (a,b)$ is a continuous random variable with probability density function $f_X$ and $Y = u(X),$ where the function $u(x)$ is strictly monotonic, then according to the change-of-variables method, the probability density function of $Y$ is given by

$$


\begin{aligned}𝑓_{𝑋}(𝑢^{−1}(𝑦))⋅(𝑢^{−1})^{′}(𝑦), & 𝑦 is between 𝑢(𝑎) and 𝑢(𝑏) \\ 0, & otherwise.\end{aligned}


$$

Here, we have $Y = \sqrt{X}.$ The transformation $u(x) = \sqrt{x}$ is strictly monotonically **, so the change-of-variables method can be used.

First, we find $u^{-1}(y)$ as follows:

$$


\begin{aligned}𝑢(𝑦) & =\sqrt{√𝑦} \\ 𝑦 & =\sqrt{√𝑢^{−1}(𝑦)} \\ 𝑢^{−1}(𝑦) & =𝑦^{2}\end{aligned}


$$

Then, we find $(u^{-1})'(y){:}$

$$


(u^{-1})'(y) = 2y


$$

Therefore, according to the change-of-variable method, we have

$$


\begin{aligned}𝑓_{𝑌}(𝑦) & =𝑓_{𝑋}(𝑢^{−1}(𝑦))⋅(𝑢^{−1})^{′}(𝑦) \\ & =𝑓_{𝑋}(𝑦^{2})⋅|2𝑦| \\ & =3(𝑦^{2})^{2}⋅2𝑦 \\ & =3𝑦^{4}⋅2𝑦 \\ & =6𝑦^{5}.\end{aligned}


$$

Finally, since $f_X$ is nonzero on $0 < x < 1,$ the bounds are $a = 0$ and $b = 1,$ we have

$$


u(0) = 0, \quad u(1) = 1.


$$

Therefore, the probability distribution of $Y$ is

$$


\begin{aligned}6𝑦^{5}, & 0<𝑦<1 \\ 0, & otherwise.\end{aligned}


$$

### Proof of the Change-of-Variables Formula

Let's restate the change-of-variables method:

*If $X\in (a,b)$ is a continuous random variable with probability density function $f_X$ and $Y = u(X),$ where the function $u(x)$ is strictly monotonic, then according to the change-of-variables method, the probability density function of $Y$ is given by*

$$


\begin{aligned}𝑓_{𝑋}(𝑢^{−1}(𝑦))⋅(𝑢^{−1})^{′}(𝑦), & 𝑦 is between 𝑢(𝑎) and 𝑢(𝑏) \\ 0, & otherwise.\end{aligned}


$$

Now, let's prove this result.

The first part is simple. Because $X$ is between $a$ and $b,$ and $u$ is monotonic, $Y=u(X)$ must be between $u(a)$ and $u(b).$ So $f_Y(y) = 0$ when $y$ is not between $u(a)$ and $u(b).$

To carry out the rest of the proof, we will need to apply the distribution function method in two cases:

- **Case 1**: $u$ is monotonically increasing

- **Case 2**: $u$ is monotonically decreasing

We'll consider the case where $u$ is monotonically increasing only. The proof when $u$ is monotonically decreasing is similar.

First, we find the cumulative distribution of $Y.$ Assuming $y$ is between $u(a)$ and $u(b),$ we have

$$


\begin{aligned}𝐹_{𝑌}(𝑦) & =𝑃(𝑌≤𝑦) \\ & =𝑃(𝑢(𝑋)≤𝑦) \\ & =𝑃(𝑋≤𝑢^{−1}(𝑦)) \\ & =∫_{𝑢^{−1}(𝑦)𝑎}^{}𝑓_{𝑋}(𝑡)\,d𝑡 \\ & =𝐹_{𝑋}(𝑡)_{𝑢^{−1}(𝑦)𝑎}^{} \\ & =𝐹_{𝑋}(𝑢^{−1}(𝑦))−𝐹_{𝑋}(𝑎).\end{aligned}


$$

Then, we differentiate to get the probability density function:

$$


\begin{aligned}𝑓_{𝑌}(𝑦) & =\frac{d}{d𝑦}[𝐹_{𝑌}(𝑦)] \\ & =\frac{d}{d𝑦}[𝐹_{𝑋}(𝑢^{−1}(𝑦))−𝐹_{𝑋}(𝑎)] \\ & =𝑓_{𝑋}(𝑢^{−1}(𝑦))(𝑢^{−1})^{′}(𝑦)\end{aligned}


$$

Because $u$ is monotonically increasing, we have that $u^{-1}$ is monotonically increasing as well. To see this, it's helpful to remember that we reflect a function over the line $y=x$ to get its inverse.

Since the slope of a monotonically increasing function is always zero or positive, we have $(u^{-1})'(y) \geq 0,$ and consequently $(u^{-1})'(y) = \left| (u^{-1})'(y) \right|.$ Therefore,

$$


\begin{aligned}𝑓_{𝑌}(𝑦) & =𝑓_{𝑋}(𝑢^{−1}(𝑦))(𝑢^{−1})^{′}(𝑦)\end{aligned}


$$

as required.
