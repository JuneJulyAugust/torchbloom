# Laplace Transforms of Piecewise Continuous Functions

Source: https://www.mathacademy.com/topics/6717?courseId=155
Topic ID: 6717

## Prerequisites

- [Definite Integrals of Piecewise Functions](../ap-calculus-ab/626-definite-integrals-of-piecewise-functions.md)
- [Introduction to Laplace Transforms](./2529-introduction-to-laplace-transforms.md)

## Lesson

### Introduction

So far, we have focused on finding the Laplace transforms of functions such as $1$ and $e^{kt}$, which are defined by a single formula.

In many real-world applications, however, a function is defined by different rules on different time intervals.

Recall that a function is *piecewise continuous* on $[0,\infty)$ if it is continuous on each interval of a finite partition, with possible jump discontinuities at the partition points. A basic example is the **unit step function**:

$$


\begin{aligned}0, & 𝑡<0 \\ 1, & 𝑡≥0.\end{aligned}


$$

Even though $u(t)$ is defined for all real $t$, notice that the Laplace transform only “sees” values for $t\ge 0$:

$$


\mathcal L\{f(t)\} = \int_0^\infty e^{-st}f(t)\,\textrm d t.


$$

So, on $[0,\infty)$ we have $u(t)=1$, and the Laplace transform reduces to

$$


\mathcal L\{u(t)\} = \int_0^\infty e^{-st}\,\textrm d t.


$$

This improper integral converges exactly when $s>0$, and in that case

$$


\boxed{\mathcal L\{u(t)\} = \dfrac{1}{s},\qquad s>0.}


$$

**Note.** As far as Laplace transforms are concerned, $u(t)$ and the constant function $1$ are *indistinguishable*, because both equal $1$ for all $t\ge 0$.

### Taking Laplace Transforms of Piecewise Functions

When $f(t)$ is defined by different formulas on different intervals, the Laplace transform is computed by **splitting the integral at the breakpoints**.

Suppose $f(t)$ has breakpoints at $t=a$ and $t=b$, where $0 < a < b$, so that

$$


\begin{aligned}𝑓_{1}(𝑡), & 0≤𝑡<𝑎, \\ 𝑓_{2}(𝑡), & 𝑎≤𝑡<𝑏, \\ 𝑓_{3}(𝑡), & 𝑡≥𝑏.\end{aligned}


$$

Then, we have

$$


\mathcal L\{f(t)\} = \int_0^a e^{-st}f_1(t)\,\textrm d t + \int_a^b e^{-st}f_2(t)\,\textrm d t + \int_b^\infty e^{-st}f_3(t)\,\textrm d t.


$$

**Key Considerations:**

- **Computation:** Each piece is usually a standard definite or improper integral.

- **Domain:** The Laplace transform exists only for those $s$ where *every improper integral you create is finite*. The final domain is the *intersection* of the domains needed for each piece.

In this lesson, the only improper integrals we will encounter are of the form

$$


\int_c^\infty e^{(\alpha-s)t}\,\textrm d t,


$$

which converges exactly when $s>\alpha.$

Next, we will apply this method to a concrete example.

### Example: Finding Laplace Transforms of Step Functions

#### Question

Use the definition of Laplace transforms to calculate $F(s) = \mathcal L\{f(t)\}$ for $f(t) = u(t - 2) + u(t-6),$ where $u$ is the unit step function.

#### Explanation

We apply the definition of the Laplace transform:

$$


\begin{aligned}L{𝑓(𝑡)} & =𝐹(𝑠)=∫_{∞0}^{}𝑓(𝑡)𝑒^{−𝑠𝑡}\,d𝑡\end{aligned}


$$

Recall that the unit step function is defined as

$$


\begin{aligned}𝑢(𝑡)=\begin{aligned}0,\, & 𝑡<0 \\ 1,\, & 𝑡≥0.\end{aligned}\end{aligned}


$$

So, for the piecewise functions $u(t-2)$ and $u(t-6),$ we have

$$


\begin{aligned}𝑢(𝑡−2) & =\begin{aligned}0,\, & 𝑡<2 \\ 1,\, & 𝑡≥2\end{aligned} \\ 𝑢(𝑡−6) & =\begin{aligned}0,\, & 𝑡<6 \\ 1,\, & 𝑡≥6.\end{aligned}\end{aligned}


$$

Therefore,

$$


\begin{aligned}0,\, & 𝑡<2 \\ 1,\, & 2≤𝑡<6 \\ 2,\, & 𝑡≥6.\end{aligned}


$$

So, for our Laplace transform, we have

$$


\begin{aligned}𝐹(𝑠) & =∫_{∞0}^{}𝑓(𝑡)𝑒^{−𝑠𝑡}\,d𝑡 \\ & =∫_{20}^{}0⋅𝑒^{−𝑠𝑡}\,d𝑡+∫_{62}^{}1⋅𝑒^{−𝑠𝑡}\,d𝑡+∫_{∞6}^{}2⋅𝑒^{−𝑠𝑡}\,d𝑡 \\ & =∫_{62}^{}𝑒^{−𝑠𝑡}\,d𝑡+∫_{∞6}^{}2𝑒^{−𝑠𝑡}\,d𝑡.\end{aligned}


$$

Note that the second integral diverges for $s \leq 0.$

For $s > 0,$ we calculate our Laplace transform as follows:

$$


\begin{aligned}𝐹(𝑠) & =∫_{62}^{}𝑒^{−𝑠𝑡}\,d𝑡+∫_{∞6}^{}2𝑒^{−𝑠𝑡}\,d𝑡 \\ & =∫_{62}^{}𝑒^{−𝑠𝑡}\,d𝑡+2\underset{𝑎→∞}{lim}∫_{𝑎6}^{}𝑒^{−𝑠𝑡}\,d𝑡 \\ & =[−\frac{𝑒^{−𝑠𝑡}}{𝑠}]_{62}^{}+2\underset{𝑎→∞}{lim}(−\frac{𝑒^{−𝑠𝑡}}{𝑠})_{𝑎6}^{} \\ & =−\frac{𝑒^{−6𝑠}}{𝑠}+\frac{𝑒^{−2𝑠}}{𝑠}−\frac{2}{𝑠}⋅\underset{𝑎→∞}{lim}(𝑒^{−𝑠𝑎}−𝑒^{−6𝑠}) \\ & =\frac{𝑒^{−2𝑠}}{𝑠}−\frac{𝑒^{−6𝑠}}{𝑠}−\frac{2}{𝑠}(0−𝑒^{−6𝑠}) \\ & =\frac{𝑒^{−2𝑠}}{𝑠}−\frac{𝑒^{−6𝑠}}{𝑠}+\frac{2𝑒^{−6𝑠}}{𝑠} \\ & =\frac{𝑒^{−2𝑠}}{𝑠}+\frac{𝑒^{−6𝑠}}{𝑠}\end{aligned}


$$

Therefore, the Laplace transform of $f(t)$ is

$$


\mathcal{L}\left\{f(t)\right\} =\dfrac{e^{-2s}}{s} +\dfrac{e^{-6s}}{s}, \qquad s > 0.


$$

### The General Result for the Shifted Unit Step Function

As we've seen, the *unit step function* shifted by $a>0$ is defined by

$$


\begin{aligned}0, & 𝑡<𝑎, \\ 1, & 𝑡≥𝑎.\end{aligned}


$$

To compute its Laplace transform, we apply the definition. Since $u(t-a) = 0$ for $t < a,$ the integral vanishes on the interval $[0,a){:}$

$$


\mathcal L\{u(t-a)\} = \int_0^\infty e^{-st}u(t-a)\,\textrm d t = \int_a^\infty e^{-st}\,\textrm d t.


$$

For $s>0,$ this improper integral converges and evaluates to

$$


\int_a^\infty e^{-st}\,\textrm d t = \left[-\dfrac{e^{-st}}{s}\right]_a^\infty = \dfrac{e^{-as}}{s}.


$$

Therefore, the **Laplace transform of the shifted unit step function** is

$$


\mathcal L\{u(t-a)\} = \dfrac{e^{-as}}{s}, \qquad s>0.


$$

This result will be used repeatedly to simplify Laplace transforms of piecewise-defined functions involving step functions.

### Example: Finding Laplace Transforms of Other Piecewise Continuous Functions

#### Question

Use the definition of Laplace transforms to calculate $F(s) = \mathcal L\{f(t)\},$ where $f(t)$ is given by

$$


\begin{aligned}𝑒^{2𝑡},\, & 𝑡≤3 \\ 1\, & 𝑡>3.\end{aligned}


$$

#### Explanation

We apply the definition of the Laplace transform:

$$


\begin{aligned}L{𝑓(𝑡)} & =𝐹(𝑠)=∫_{∞0}^{}𝑓(𝑡)𝑒^{−𝑠𝑡}\,d𝑡\end{aligned}


$$

So, for the piecewise function

$$


\begin{aligned}𝑒^{2𝑡},\, & 𝑡≤3 \\ 1\, & 𝑡>3\end{aligned}


$$

we have

$$


\begin{aligned}𝐹(𝑠) & =∫_{∞0}^{}𝑓(𝑡)𝑒^{−𝑠𝑡}\,d𝑡 \\ & =∫_{30}^{}𝑒^{2𝑡}⋅𝑒^{−𝑠𝑡}\,d𝑡+∫_{∞3}^{}1⋅𝑒^{−𝑠𝑡}\,d𝑡 \\ & =∫_{30}^{}𝑒^{2𝑡−𝑠𝑡}\,d𝑡+∫_{∞3}^{}𝑒^{−𝑠𝑡}\,d𝑡 \\ & =∫_{30}^{}𝑒^{(2−𝑠)𝑡}\,d𝑡+∫_{∞3}^{}𝑒^{−𝑠𝑡}\,d𝑡.\end{aligned}


$$

Note that the improper integral diverges if $s \leq 0.$

For $s > 0,$ we calculate our Laplace transform as follows:

$$


\begin{aligned}𝐹(𝑠) & =∫_{30}^{}𝑒^{(2−𝑠)𝑡}\,d𝑡+∫_{∞3}^{}𝑒^{−𝑠𝑡}\,d𝑡 \\ & =\frac{1}{2−𝑠}[𝑒^{(2−𝑠)𝑡}]_{30}^{}+∫_{∞3}^{}𝑒^{−𝑠𝑡}\,d𝑡 \\ & =\frac{𝑒^{3(2−𝑠)}−1}{2−𝑠}+\underset{𝑎→∞}{lim}∫_{𝑎3}^{}𝑒^{−𝑠𝑡}\,d𝑡 \\ & =\frac{𝑒^{3(2−𝑠)}−1}{2−𝑠}+\underset{𝑎→∞}{lim}(\frac{−𝑒^{−𝑠𝑡}}{𝑠})_{𝑎3}^{} \\ & =\frac{𝑒^{3(2−𝑠)}−1}{2−𝑠}−\frac{1}{𝑠}⋅\underset{𝑎→∞}{lim}(𝑒^{−𝑎𝑠}−𝑒^{−3𝑠}) \\ & =\frac{𝑒^{3(2−𝑠)}−1}{2−𝑠}−\frac{1}{𝑠}⋅(0−𝑒^{−3𝑠}) \\ & =\frac{𝑒^{3(2−𝑠)}−1}{2−𝑠}+\frac{𝑒^{−3𝑠}}{𝑠}\end{aligned}


$$

valid for $s > 0.$

### Uniqueness of Laplace Transforms

Along with existence, the Laplace transform also satisfies an important **uniqueness** property.

Suppose $f$ and $g$ are *piecewise continuous* on $[0,\infty)$ and of exponential order $s_0,$ and that their Laplace transforms

$$


F(s)=\mathcal{L}\{f(t)\}, \qquad G(s)=\mathcal{L}\{g(t)\}, \qquad s>s_0,


$$

satisfy

$$


F(s)=G(s) \quad \text{for all } s>s_0.


$$

Then

$$


f(t)=g(t) \quad \text{for almost every } t\ge 0.


$$

Moreover, if $f$ and $g$ are continuous, then

$$


f(t)=g(t) \quad \text{for all } t\ge 0.


$$

To understand the meaning of *almost every*, consider the following piecewise continuous functions:

$$


\begin{aligned}0, & 𝑡<1, \\ 1, & 𝑡≥1,\end{aligned}


$$

These functions differ only at the single point $t=1.$ Nevertheless,

$$


\mathcal L\{f(t)\} = \mathcal L\{g(t)\} = \mathcal L\{h(t)\} = \dfrac{e^{-s}}{s}.


$$

Changing the value of a piecewise continuous function at finitely or countably many isolated points does not affect its Laplace transform, since the transform is defined using an integral.

In short, for piecewise continuous functions, the Laplace transform determines the function completely, except for its values at isolated jump points.
