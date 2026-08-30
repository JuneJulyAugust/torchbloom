# Introduction to Laplace Transforms

Source: https://www.mathacademy.com/topics/2529?courseId=155
Topic ID: 2529

## Prerequisites

- [Euler's Formula](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/898-euler-s-formula.md)
- [Big-O Notation](./2854-big-o-notation.md)
- [Improper Integrals Involving Exponential Functions](../../../ap-courses/lessons/ap-calculus-bc/4004-improper-integrals-involving-exponential-functions.md)
- [Piecewise Continuity and Piecewise Smoothness](./6669-piecewise-continuity-and-piecewise-smoothness.md)

## Lesson

### Introduction

The **Laplace transform** of the function $f(t),$ denoted $\mathcal{L}\left\{f(t)\right\},$ takes a function of $t$ and transforms it into a new function of $s$ as follows:

$$


\mathcal{L}\left\{f(t)\right\} = F(s) = \int_{0}^{\infty} e^{-st} f(t)\,\textrm d t,


$$

provided that the improper integral is finite.

To build intuition, focus on the factor $e^{-st}.$ For $s>0,$ this factor decays to $0$ as $t\to\infty,$ so it “discounts” the contribution of $f(t)$ at large values of $t.$

This means the Laplace transform behaves like a *weighted average* of the values of $f(t)$ on $[0,\infty),$ where values of $f(t)$ near $t=0$ are counted more heavily than values far in the future.

Also, notice how the parameter $s$ affects the discounting:

- If $s$ is larger, then $e^{-st}$ decays faster, so $F(s)$ depends mostly on the behavior of $f(t)$ near $t=0.$

- If $s$ is smaller (but still positive), then $e^{-st}$ decays more slowly, so values of $f(t)$ for larger $t$ have a larger influence on $F(s).$

Laplace transforms are especially useful in differential equations because they convert derivatives into algebraic expressions, which often makes it much easier to solve an initial value problem.

**Note.** When dealing with Laplace transforms, we're only interested in functions defined on $t \ge 0.$ So for all functions $f(t), g(t),$ etc., we will assume $t \ge 0$ even when it is not stated explicitly.

Let's begin by calculating the Laplace transform of a constant function.

### Example: Evaluating Laplace Transforms of Constant Functions

#### Question

Find the Laplace transform of $f(t) = 2.$

#### Explanation

For a function $f(t)$ defined on $[0,\infty),$ the Laplace transform of $f,$ denoted $\mathcal L\{f(t)\}$ or $F(s),$ is a function of the variable $s$ defined as

$$


F(s) = \mathcal L \{f(t)\} = \int_0^\infty e^{-st} f(t) \,\textrm d t


$$

provided that this integral exists and is finite.

For the function $f(t)=2,$ we have

$$


\begin{aligned}𝐹(𝑠)=∫_{∞0}^{}2𝑒^{−𝑠𝑡}d𝑡.\end{aligned}


$$

We calculate our integral as follows:

$$


\begin{aligned}𝐹(𝑠) & =∫_{∞0}^{}2𝑒^{−𝑠𝑡}d𝑡 \\ & =2\underset{𝑎→∞}{lim}∫_{𝑎0}^{}𝑒^{−𝑠𝑡}d𝑡\end{aligned}


$$

To evaluate the last integral, we must consider whether $s \neq 0$ or $s = 0.$

- If $s \neq 0,$ we have Let's evaluate the limit. We have

- If $s = 0,$ we have

Therefore:

- For $s = 0,$ we have that $\displaystyle \int_{0}^{\infty} 2e^{-st} \textrm{d} t$ is divergent

- For $s > 0,$ we have that $\displaystyle \int_{0}^{\infty} 2e^{-st} \textrm{d} t$ is convergent

- For $s < 0,$ we have that $\displaystyle \int_{0}^{\infty} 2e^{-st} \textrm{d} t$ is divergent

Evaluating our integral for $s > 0,$ we have

$$


\begin{aligned}𝐹(𝑠) & =−\frac{2}{𝑠}(\underset{𝑎→∞}{lim}𝑒^{−𝑠𝑎}−1) \\ & =−\frac{2}{𝑠}(0−1) \\ & =\frac{2}{𝑠}.\end{aligned}


$$

So, the Laplace transform of $f(t)=2$ is $F(s) =\dfrac{2}{s},$ defined for $s > 0.$

### Laplace Transforms of Exponential Functions

Exponential functions appear frequently in differential equations, especially when modeling growth, decay, or oscillations. Because of this, being able to compute the Laplace transform of an exponential function is a key skill that we will use many times throughout this course.

Suppose we want to find the **Laplace transform of an exponential function**

$$


f(t)=e^{kt},


$$

where $k$ is a real constant.

We start from the definition:

$$


\mathcal L\left\{e^{kt}\right\}=\int_{0}^{\infty} e^{-st}e^{kt}\,\textrm d t.


$$

Next, we combine the exponentials:

$$


e^{-st}e^{kt}=e^{-(s-k)t},


$$

so the Laplace transform becomes

$$


\mathcal L\left\{e^{kt}\right\}=\int_{0}^{\infty} e^{-(s-k)t}\,\textrm d t.


$$

From here, we evaluate this improper integral by writing it as a limit,

$$


\int_{0}^{\infty} e^{-(s-k)t}\,\textrm d t = \lim_{a\to\infty}\int_{0}^{a} e^{-(s-k)t}\,\textrm d t,


$$

and then checking which values of $s$ make the limit finite.

### When Does a Laplace Transform Converge?

Many Laplace transforms in this lesson reduce to an integral of the form

$$


\int_{0}^{\infty} e^{(a-s)t}\,\textrm d t,


$$

where $a$ and $s$ are real numbers.

To decide whether this improper integral is finite, we look at the exponent $(a-s)t.$

- If $s>a,$ then $a-s<0,$ so $e^{(a-s)t}$ decays to $0$ as $t\to\infty.$ In this case, the integral is *convergent*.

- If $s=a,$ then $e^{(a-s)t}=e^{0t}=1,$ so the integral becomes $\displaystyle\int_{0}^{\infty} 1\,\textrm d t,$ which is *divergent*.

- If $s < a,$ then $a-s>0,$ so $e^{(a-s)t}$ grows without bound as $t\to\infty,$ and the integral is *divergent*.

So, a common rule of thumb is that $\displaystyle\int_{0}^{\infty} e^{(a-s)t}\,\textrm d t$ converges exactly when $s>a.$

We will use this idea repeatedly when finding Laplace transforms and determining which values of $s$ make the transform exist.

### Example: Evaluating Laplace Transforms of Real Exponential Functions

#### Question

Find the Laplace transform of $f(t) = e^{-2t}.$

#### Explanation

For a function $f(t)$ defined on $[0,\infty),$ the Laplace transform of $f,$ denoted $\mathcal L\{f(t)\}$ or $F(s),$ is a function of the variable $s$ defined as

$$


F(s) = \mathcal L \{f(t)\} = \int_0^\infty e^{-st} f(t) \,\textrm d t


$$

provided that this integral exists and is finite.

For the function $f(t)=e^{-2t},$ we have

$$


\begin{aligned}𝐹(𝑠) & =∫_{∞0}^{}𝑒^{−𝑠𝑡}⋅𝑒^{−2𝑡}d𝑡 \\ & =∫_{∞0}^{}𝑒^{−𝑠𝑡−2𝑡}d𝑡 \\ & =∫_{∞0}^{}𝑒^{(−2−𝑠)𝑡}d𝑡.\end{aligned}


$$

We calculate our integral as follows:

$$


\begin{aligned}𝐹(𝑠) & =∫_{∞0}^{}𝑒^{(−2−𝑠)𝑡}d𝑡 \\ & =\underset{𝑎→∞}{lim}∫_{𝑎0}^{}𝑒^{(−2−𝑠)𝑡}d𝑡\end{aligned}


$$

To evaluate the last integral, we must consider whether $s \neq -2$ or $s = -2.$

- If $s \neq -2,$ we have Let's evaluate the limit. We have

- If $s = -2,$ we have

Therefore:

- For $s \leq -2$ the integral is divergent.

- For $s > -2$ the integral is convergent.

Evaluating for $s > -2,$ we have

$$


\begin{aligned}𝐹(𝑠) & =\frac{1}{𝑠+2}−\frac{1}{𝑠+2}⋅\underset{𝑎→∞}{lim}𝑒^{(−2−𝑠)𝑎} \\ & =\frac{1}{𝑠+2}−\frac{1}{𝑠+2}⋅0 \\ & =\frac{1}{𝑠+2}.\end{aligned}


$$

So the Laplace transform of $f(t)=e^{-2t}$ is $F(s) =\dfrac{1}{s+2},$ defined for $s > -2.$

### Laplace Transforms as Functions of a Complex Variable

So far, we have considered Laplace transforms of real-valued functions $f(t).$ However, the definition still makes sense for **complex-valued functions**.

If $f(t)$ is complex-valued, we can write

$$


f(t)=u(t)+\mathrm{i} v(t),


$$

where $u(t)$ and $v(t)$ are real-valued functions.

Then, the Laplace transform is defined by the same integral:

$$


\mathcal L\left\{f(t)\right\}=\int_{0}^{\infty} e^{-st}f(t)\,\mathrm{d} t,


$$

and the result $F(s)$ may be a complex number.

In this lesson, we will keep $s$ real. Even with $s\in\mathbb R,$ it is possible for $\mathcal L\left\{f(t)\right\}$ to be complex-valued.

For example, if $f(t)=e^{\mathrm{i}\omega t}$ for a real constant $\omega,$ then

$$


\mathcal L\left\{e^{\mathrm{i}\omega t}\right\} = \int_{0}^{\infty} e^{-st}e^{\mathrm{i}\omega t}\,\mathrm{d} t.


$$

We won't prove this rigorously, but it can be shown that the usual methods of integration apply to integrals like this.

In the next example, we will compute the Laplace transforms of complex exponential functions, such as this one.

### Example: Evaluating Laplace Transforms of Complex Exponentials

#### Question

What is the Laplace transform of $f(t) = e^{2\textrm i t},$ where $t, s \in\mathbb R?$

#### Explanation

We apply the definition of the Laplace transform:

$$


\begin{aligned}L{𝑓(𝑡)} & =𝐹(𝑠)=∫_{∞0}^{}𝑒^{−𝑠𝑡}𝑓(𝑡)d𝑡\end{aligned}


$$

For the function $f(t)=e^{2\textrm i t},$ we have

$$


\begin{aligned}𝐹(𝑠) & =∫_{∞0}^{}𝑒^{−𝑠𝑡}𝑒^{2i𝑡}d𝑡=∫_{∞0}^{}𝑒^{(2i−𝑠)𝑡}d𝑡.\end{aligned}


$$

Evaluating in the usual way, we have

$$


\begin{aligned}𝐹(𝑠) & =∫_{∞0}^{}𝑒^{(2i−𝑠)𝑡}d𝑡 \\ & =\underset{𝑎→∞}{lim}∫_{𝑎0}^{}𝑒^{(2i−𝑠)𝑡}d𝑡 \\ & =\underset{𝑎→∞}{lim}(\frac{1}{2i−𝑠}𝑒^{(2i−𝑠)𝑡})_{𝑎0}^{} \\ & =\frac{1}{2i−𝑠}(\underset{𝑎→∞}{lim}𝑒^{(2i−𝑠)𝑎}−1) \\ & =\frac{1}{𝑠−2i}(1−\underset{𝑎→∞}{lim}𝑒^{(2i−𝑠)𝑎}) \\ & =\frac{1}{𝑠−2i}−\frac{1}{𝑠−2i}(\underset{𝑎→∞}{lim}𝑒^{−𝑠𝑎}⋅𝑒^{2i𝑎}).\end{aligned}


$$

Now, we recall Euler's formula:

$$


e^{\textrm i\theta} = \cos\theta + \textrm i \sin\theta


$$

Therefore, we have

$$


F(s)= \dfrac{1}{s-2\textrm i} - \dfrac{1}{s-2\textrm i}\left[\lim_{a\to \infty}e^{ -sa}\cdot \left(\cos(2a) + \textrm i\sin(2a)\right) \right].


$$

Now, we have the following cases:

- For $s < 0,$ the term $e^{-sa}$ increases without bound while $\cos(2a) + \textrm i\sin(2a)$ oscillates rapidly as $a\to\infty.$ Therefore, the limit does not exist for $s < 0.$

- For $s = 0,$ we have simply $\cos(2a) + \textrm i\sin(2a),$ which oscillates rapidly as $a\to\infty.$ Therefore, the limit does not exist for $s = 0.$

- For $s > 0,$ the term $e^{-sa}$ decays to zero while $\cos(2a) + \textrm i\sin(2a)$ oscillates rapidly as $a\to\infty.$ Therefore, the limit of their product equals zero.

Therefore, for $s > 0,$ we have

$$


\begin{aligned}𝐹(𝑠) & =\frac{1}{𝑠−2i}−\frac{1}{𝑠−2i}[\underset{𝑎→∞}{lim}𝑒^{−𝑠𝑎}⋅(cos⁡(2𝑎)+isin⁡(2𝑎))] \\ & =\frac{1}{𝑠−2i}−0 \\ & =\frac{1}{𝑠−2i}.\end{aligned}


$$

So, the Laplace transform of $e^{2\textrm i t}$ is $F(s) =\dfrac{1}{s-2\textrm i},$ defined for $s>0.$

### Key Results

The following Laplace transforms have been computed in this lesson.

As we make progress, we will study properties of Laplace transforms. This will allow us to gradually build our table of transforms.

### Existence of Laplace Transforms

In this lesson, we found that the Laplace transform of $f(t)$ is defined by

$$


\mathcal{L}\left\{f(t)\right\} = \int_{0}^{\infty} e^{-st} f(t)\,\textrm d t,


$$

whenever this improper integral is finite.

In practice, Laplace transforms exist for *most* of the functions we will use in differential equations. Two common conditions that guarantee existence are listed below.

We say that $f(t)$ is **piecewise continuous** on $[0,\infty)$ if it is continuous except for finitely many jump discontinuities on any interval $[0,T].$

A function $f(t)$ is of **exponential order** $a$ if there exist constants $K>0$ and $T>0$ such that

$$


|f(t)| \le Ke^{at}, \qquad t>T.


$$

Equivalently, $f(t)$ is of exponential order $a$ if

$$


f(t)=\mathcal O\left(e^{at}\right)\textrm{ as }t\to\infty.


$$

It can be shown that if $f(t)$ is piecewise continuous on $[0,\infty)$ and $f(t)$ is of exponential order $a,$ then the Laplace transform $\mathcal{L}\left\{f(t)\right\}$ exists for all $s>a.$
