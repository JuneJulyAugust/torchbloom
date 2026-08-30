# The Smoothness Property of Laplace Transforms

Source: https://www.mathacademy.com/topics/6402?courseId=61
Topic ID: 6402

## Prerequisites

- [Linearity of Laplace Transforms](./2537-linearity-of-laplace-transforms.md)
- [Differentiating Under the Integral Sign](../multivariable-calculus/6682-differentiating-under-the-integral-sign.md)
- [Laplace Transforms of Piecewise Continuous Functions](./6717-laplace-transforms-of-piecewise-continuous-functions.md)

## Lesson

### Introduction

When studying differential equations, we often face expressions like

$$


t\,e^{kt},\qquad t\,\sin(\omega t), \qquad t^2\,\cosh(kt)


$$

or higher powers of $t$ multiplying familiar functions. The Laplace transform gives a systematic way to handle these by converting “multiply by $t$” into “differentiate with respect to $s$.”

In this topic, we focus on a key regularity fact: even if $f(t)$ has corners or jumps, its Laplace transform $F(s)$ is *perfectly smooth* as a function of $s$ (within its region of convergence). This is called the **smoothness property** (or the **differentiation of transforms** property).

First, let's assume that

- $f(t)$ is *piecewise continuous* on $[0,\infty)$, and

- $f(t)$ is of exponential order $a$ (so $|f(t)| = O(e^{at})$ as $t\to\infty$).

Then the Laplace transform

$$


F(s)=\mathcal L\{f(t)\}


$$

exists for all $s>a$, and $F$ is *infinitely differentiable* with respect to $s$ on this interval.

Moreover, for every integer $n\ge 0$ and every $s>a$,

$$


\mathcal L\{t^n f(t)\}(s)=(-1)^n F^{(n)}(s),


$$

where $F^{(n)}$ denotes the $n$th derivative of $F$ with respect to $s$.

In particular,

$$


\mathcal L\{t f(t)\}=-F'(s), \qquad \mathcal L\{t^2 f(t)\}=F''(s).


$$

This matters because it turns multiplication by powers of $t$ into differentiation with respect to $s$, which is often much faster than re-integrating from scratch or applying integration by parts multiple times.

In the next slide, we will apply this property to work through a concrete example.

### A Worked Example

Let's use the smoothness property to find the Laplace transform of $\mathcal L\{t e^{-9t}\}.$

If a function $f(t)$ is piecewise continuous on $[0,\infty)$ and has exponential order $a,$ then its Laplace transform

$$


F(s) = \mathcal{L}\{f(t)\}


$$

exists for every real $s > a,$ and $F$ is infinitely differentiable in this region of convergence. Moreover, for each integer $n\geq 0$ and every such $s,$ we have

$$


\mathcal{L}\{ t^n f(t) \} = (-1)^n F^{(n)}(s).


$$

In particular, for $n=1,$ we have

$$


\mathcal{L}\{ tf(t) \} = -F'(s).


$$

We have that $f(t) = e^{-9t}.$ Therefore, for $s > -9,$ we have

$$


F(s) = \dfrac{1}{s+9}.


$$

Differentiating with respect to $s,$ we have

$$


\begin{aligned}𝐹^{′}(𝑠) & =\frac{d}{d𝑠}(\frac{1}{𝑠+9}) \\ & =\frac{d}{d𝑠}((𝑠+9)^{−1}) \\ & =−(𝑠+9)^{−2} \\ & =−\frac{1}{(𝑠+9)^{2}}.\end{aligned}


$$

Therefore, by the smoothness property,

$$


\begin{aligned}L{𝑡𝑒^{−9𝑡}} & =−𝐹^{′}(𝑠) \\ & =−[−\frac{1}{(𝑠+9)^{2}}] \\ & =\frac{1}{(𝑠+9)^{2}},\,𝑠>−9.\end{aligned}


$$

### A Table of Laplace Transforms

In previous lessons, we derived several basic Laplace transforms directly from the definition.

One goal of this lesson is to expand this table by using the **smoothness property**. In the next slide, we will apply this property to derive a new transform without computing integrals from scratch.

### Example: Finding Laplace Transforms Using the Smoothness Property (1st Derivative)

#### Question

Use the smoothness property to find the Laplace transform of

$$


\mathcal L\{t \cos 5t\}.


$$

You may make use of the following result:

$$


\mathcal L \{\cos \omega t\} = \dfrac{s}{s^2+\omega^2}, \qquad s > 0.


$$

#### Explanation

If a function $f(t)$ is piecewise continuous on $[0,\infty)$ and has exponential order $a,$ then its Laplace transform

$$


F(s) = \mathcal{L}\{f(t)\}


$$

exists for every real $s > a,$ and $F$ is infinitely differentiable in this region of convergence. Moreover, for each integer $n\geq 0$ and every such $s,$ we have

$$


\mathcal{L}\{ t^n f(t) \} = (-1)^n F^{(n)}(s).


$$

In particular, for $n=1,$ we have

$$


\mathcal{L}\{ tf(t) \} = -F'(s).


$$

We have that $f(t) = \cos 5t.$ Using the given result with $\omega = 5,$ the Laplace transform of $f(t)$ is

$$


F(s) = \dfrac{s}{s^2+25}, \qquad s > 0.


$$

Differentiating with respect to $s,$ we have

$$


\begin{aligned}𝐹^{′}(𝑠) & =\frac{d}{d𝑠}(\frac{𝑠}{𝑠^{2}+25}) \\ & =\frac{d}{d𝑠}(𝑠(𝑠^{2}+25)^{−1}) \\ & =(𝑠^{2}+25)^{−1}+𝑠(−(𝑠^{2}+25)^{−2}⋅2𝑠) \\ & =\frac{𝑠^{2}+25}{(𝑠^{2}+25)^{2}}−\frac{2𝑠^{2}}{(𝑠^{2}+25)^{2}} \\ & =\frac{25−𝑠^{2}}{(𝑠^{2}+25)^{2}}.\end{aligned}


$$

Therefore, by the smoothness property,

$$


\begin{aligned}L{𝑡cos⁡5𝑡}=−𝐹^{′}(𝑠)=\frac{𝑠^{2}−25}{(𝑠^{2}+25)^{2}},\,𝑠>0.\end{aligned}


$$

### Example: Finding Laplace Transforms Using the Smoothness Property (2nd Derivative)

#### Question

Use the smoothness property to find the Laplace transform of

$$


\mathcal L\{t^2 \sinh{5t}\}.


$$

You may make use of the following result:

$$


\mathcal L \{\sinh \omega t\} = \dfrac{\omega}{s^2-\omega^2}, \qquad s > \omega.


$$

#### Explanation

If a function $f(t)$ is piecewise continuous on $[0,\infty)$ and has exponential order $a,$ then its Laplace transform

$$


F(s) = \mathcal{L}\{f(t)\}


$$

exists for every real $s > a,$ and $F$ is infinitely differentiable in this region of convergence. Moreover, for each integer $n\geq 0$ and every such $s,$ we have

$$


\mathcal{L}\{ t^n f(t) \} = (-1)^n F^{(n)}(s).


$$

In particular, for $n=2,$ we have

$$


\mathcal{L}\{ t^2 f(t) \} = F''(s).


$$

We have that $f(t) = \sinh 5t.$ Using the given result with $\omega = 5,$ the Laplace transform of $f(t)$ is

$$


F(s) = \dfrac{5}{s^2-25}, \qquad s > 5.


$$

Differentiating with respect to $s,$ we have

$$


\begin{aligned}𝐹^{′}(𝑠) & =\frac{d}{d𝑠}(\frac{5}{𝑠^{2}−25}) \\ & =\frac{d}{d𝑠}(5(𝑠^{2}−25)^{−1}) \\ & =−5(𝑠^{2}−25)^{−2}⋅2𝑠 \\ & =−\frac{10𝑠}{(𝑠^{2}−25)^{2}} \\ 𝐹^{″}(𝑠) & =\frac{d}{d𝑠}(−\frac{10𝑠}{(𝑠^{2}−25)^{2}}) \\ & =−10⋅\frac{d}{d𝑠}(\frac{𝑠}{(𝑠^{2}−25)^{2}}) \\ & =−10⋅(\frac{(𝑠)^{′}⋅(𝑠^{2}−25)^{2}−𝑠⋅((𝑠^{2}−25)^{2})^{′}}{(𝑠^{2}−25)^{4}}) \\ & =−10⋅(\frac{(𝑠^{2}−25)^{2}−𝑠⋅2(𝑠^{2}−25)⋅2𝑠}{(𝑠^{2}−25)^{4}}) \\ & =−10⋅(\frac{(𝑠^{2}−25)^{2}−4𝑠^{2}(𝑠^{2}−25)}{(𝑠^{2}−25)^{4}}) \\ & =−10⋅(\frac{𝑠^{2}−25−4𝑠^{2}}{(𝑠^{2}−25)^{3}}) \\ & =−10⋅(\frac{−3𝑠^{2}−25}{(𝑠^{2}−25)^{3}}) \\ & =\frac{30𝑠^{2}+250}{(𝑠^{2}−25)^{3}}.\end{aligned}


$$

Note that we used the quotient rule to find $F''(s).$

Therefore, by the smoothness property,

$$


\begin{aligned}L{𝑡^{2}sinh⁡5𝑡}=𝐹^{″}(𝑠)=\frac{30𝑠^{2}+250}{(𝑠^{2}−25)^{3}},\,𝑠>5.\end{aligned}


$$

### Laplace Transforms of Polynomials

A particularly important special case occurs when $f(t)=1$. Since

$$


\mathcal L\{1\}=\frac{1}{s}, \qquad s>0,


$$

we can use the smoothness property to compute **Laplace transforms of powers of $t$** by *repeated differentiation with respect to $s$*.

First, applying the smoothness property once,

$$


\mathcal L\{t\}=-\frac{\mathrm{d}}{\mathrm{d} s}\left(\frac{1}{s}\right) =\frac{1}{s^2}, \qquad s>0.


$$

Applying it again,

$$


\mathcal L\{t^2\} =\frac{\mathrm{d}^2}{\mathrm{d} s^2}\left(\frac{1}{s}\right) =\frac{2}{s^3}, \qquad s>0.


$$

Applying it a third time (noting that $3 \times 2 = 6 = 3!$),

$$


\mathcal L\{t^3\} =-\frac{\mathrm{d}^3}{\mathrm{d} s^3}\left(\frac{1}{s}\right) =\frac{6}{s^4} = \frac{3!}{s^4}, \qquad s>0.


$$

From these examples, a clear pattern emerges. For every integer $n\ge 0$,

$$


\mathcal L\{t^n\}=\frac{n!}{s^{n+1}}, \qquad s>0.


$$

This formula allows us to compute the Laplace transform of *any polynomial* by combining linearity with this result.

### Example: Finding Laplace Transforms of Polynomials

#### Question

Given that $\mathcal L\left\{t^n\right\} = \dfrac{n!}{s^{n+1}},$ find the Laplace transform of $f(t) = (t - 5)^2$ for $s > 0.$

#### Explanation

The linearity property of the Laplace transform states that for functions $f(t)$ and $g(t),$ we have

$$


\mathcal L\{\alpha f(t) + \beta g(t)\} = \alpha\cdot \mathcal L\{f(t)\} + \beta\cdot \mathcal L \{g(t)\}


$$

where $\alpha$ and $\beta$ are constants.

First, we expand:

$$


f(t) = (t - 5)^2= t^2 - 10t + 25


$$

Now, taking the Laplace transform and applying the linearity properties, we have

$$


\begin{aligned}L{𝑓(𝑡)} & =L{𝑡^{2}−10𝑡+25} \\ & =L{𝑡^{2}}+L{−10𝑡}+L{25} \\ & =L{𝑡^{2}}−10L{𝑡}+25L{1}.\end{aligned}


$$

We're given that $\mathcal L\left\{t^n\right\} = \dfrac{n!}{s^{n+1}}.$ Therefore, we have the following:

$$


\begin{aligned}L{𝑡^{2}} & =\frac{2}{𝑠^{3}},\,𝑠>0 \\ L{𝑡} & =\frac{1}{𝑠^{2}},\,𝑠>0 \\ L{1} & =\frac{1}{𝑠},\,𝑠>0\end{aligned}


$$

Therefore, the Laplace transform of $f(t)$ is

$$


\begin{aligned}L{𝑓(𝑡)} & =L{𝑡^{2}}−10L{𝑡}+25L{1} \\ & =\frac{2}{𝑠^{3}}−10⋅\frac{1}{𝑠^{2}}+25⋅\frac{1}{𝑠} \\ & =\frac{2}{𝑠^{3}}−\frac{10}{𝑠^{2}}+\frac{25}{𝑠} \\ & =\frac{2−10𝑠+25𝑠^{2}}{𝑠^{3}} \\ & =\frac{25𝑠^{2}−10𝑠+2}{𝑠^{3}},\,𝑠>0.\end{aligned}


$$

### Proof of the Smoothness Property

Suppose that $f(t)$ is piecewise continuous on $[0,\infty)$ and of exponential order $a.$ This means that there exist constants $K>0$ and $T>0$ such that

$$


|f(t)| \le K e^{a t} \qquad \text{for all } t > T.


$$

We define the Laplace transform of $f$ by

$$


F(s) = \mathcal{L}\{f(t)\}(s) = \int_0^\infty e^{-st} f(t)\,\mathrm{d}t.


$$

If $s > a,$ then for all sufficiently large $t,$

$$


|e^{-st} f(t)| \le K e^{-(s-a)t}.


$$

Since $s-a>0,$ the function $e^{-(s-a)t}$ is integrable on $[T,\infty).$ In addition, because $f$ is piecewise continuous, it is bounded on $[0,T].$ Together, these observations show that the integral defining $F(s)$ converges, so $F(s)$ is well-defined for all $s>a.$

Now fix $s>a$ and compute the derivative of $F(s).$ Starting from the definition,

$$


F'(s) = \frac{\mathrm{d}}{\mathrm{d}s} \int_0^\infty e^{-st} f(t)\,\mathrm{d}t.


$$

The exponential-order assumption ensures that this integral converges, which allows us to differentiate under the integral sign. Therefore,

$$


F'(s) = \int_0^\infty \frac{\partial}{\partial s}\big(e^{-st} f(t)\big)\, \mathrm{d}t.


$$

Since $f(t)$ does not depend on $s,$ applying the chain rule gives

$$


\frac{\partial}{\partial s}\big(e^{-st} f(t)\big) = -t e^{-st} f(t).


$$

Substituting this expression into the integral, we obtain

$$


F'(s) = -\int_0^\infty t e^{-st} f(t)\,\mathrm{d}t.


$$

Finally, by definition of the Laplace transform,

$$


\int_0^\infty t e^{-st} f(t)\,\mathrm{d}t = \mathcal{L}\{t f(t)\}(s).


$$

Hence,

$$


F'(s) = -\mathcal{L}\{t f(t)\}(s),


$$

which proves the smoothness property in the case $n=1.$

Repeating this argument shows that the Laplace transform is infinitely differentiable in its region of convergence.

### Example: Proving the Smoothness Property

#### Question

Suppose that $f(t)$ is piecewise continuous on $[0,\infty)$ and its Laplace transform

$$


F(s) = \mathcal{L}\{f(t)\}


$$

exists for $s > a.$ Then, $F(s)$ is twice differentiable at every point $s > a,$ and we have

$$


F''(s) = \mathcal{L}\{ t^2\cdot f(t) \}.


$$

A proof of this statement is given below.

$\text{L1}{:}\:$ $F(s) = \displaystyle \int_0^\infty e^{-st} f(t)\,\text{d}t$ exists for $s > a.$

$\text{L2}{:}\:$ $F''(s) = \displaystyle \frac{\text{d}^2}{\text{d}s^2}\int_0^\infty e^{-st} f(t)\,\text{d}t$

$\text{L3}{:}\:$ $F''(s) = \displaystyle \int_0^\infty \frac{\partial^2}{\partial s^2}\big(e^{-st} f(t)\big)\,\text{d}t$

$\text{L4}{:}\:$ $\displaystyle \frac{\partial^2}{\partial s^2}\big(e^{-st} f(t)\big) = t^2 e^{-st} f(t)$

$\text{L5}{:}\:$ $F''(s) = \displaystyle \int_0^\infty t^2 e^{-st} f(t)\,\text{d}t$

$\text{L6}{:}\:$ $F''(s) = \mathcal{L}\{t^2\cdot f(t)\}$

Explain the reasoning behind:

- How line $\text{L2}$ follows from line $\text{L1}.$

- How line $\text{L4}$ follows from its preceding line.

- How line $\text{L6}$ follows from $\text{L5}.$

#### Explanation

If a function $f(t)$ is piecewise continuous on $[0,\infty)$ and has exponential order $a,$ then its Laplace transform

$$


F(s) = \mathcal{L}\{f(t)\}


$$

exists for every real $s > a,$ and $F$ is infinitely differentiable in this region of convergence.

The smoothness property states that, for each integer $n\geq 0$ and $s > a,$ we have

$$


F^{(n)}(s) = (-1)^n\, \mathcal{L}\{ t^n f(t) \}.


$$

We're asked to prove the smoothness property in the case $n = 2.$

With that in mind, let's examine each statement in turn.

- We first consider line $\text{L2}.$ From line $\text{L1}$ we know that By the definition of the second derivative with respect to $s,$ we get which is exactly the statement in line $\text{L2}.$

- We now consider line $\text{L4}.$ The function $f(t)$ does not depend on $s$, so Thus line $\text{L4}$ follows from the chain rule.

- Finally, we consider line $\text{L6}.$ By the definition of the Laplace transform, Comparing this with the integral in line $\text{L5}$, we see that which is exactly the expression in line $\text{L6}.$

### Updated Table of Laplace Transforms

Using the smoothness property, we can now add transforms involving factors of $t$ and higher powers of $t$ by differentiating previously known formulas.

Finally, note that we have a shortcut pattern for exponentials. If

$$


\mathcal L\{e^{kt}\}=\frac{1}{s-k}, \qquad s>k,


$$

then repeated differentiation shows that

$$


\mathcal L\{t^n e^{kt}\}=\frac{n!}{(s-k)^{n+1}}, \qquad s>k.


$$

This pattern is a direct consequence of the smoothness property and provides a fast way to compute many common transforms.
