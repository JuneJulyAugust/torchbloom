# Laplace Transforms of Derivatives

Source: https://www.mathacademy.com/topics/2538?courseId=155
Topic ID: 2538

## Prerequisites

- [Introduction to Laplace Transforms](./2529-introduction-to-laplace-transforms.md)

## Lesson

### Introduction

The Laplace transform is a powerful tool for studying differential equations because it converts differentiation of a function $f(t)$ with respect to $t$ into algebraic operations in the variable $s$.

In this topic, we study how the Laplace transform interacts with derivatives of a function. This leads to another fundamental result, called the **derivative property** of the Laplace transform.

Let's assume that:

- $f(t)$ is *continuous* on $[0,\infty)$,

- $f'(t)$ is *piecewise continuous* on $[0,\infty)$, and

- $f(t)$ is of exponential order $a$.

Then the Laplace transform

$$


F(s) = \mathcal L\{f(t)\}


$$

exists for all $s>a.$

Under these assumptions, the Laplace transform of the *first derivative* of $f$ satisfies a simple and extremely useful formula:

$$


\mathcal L\{f'(t)\} = sF(s) - f(0).


$$

This formula shows that differentiating with respect to $t$ corresponds to multiplying by $s$ *and subtracting an initial-value term*.

For example, let $f(t) = t.$ We know $\mathcal L\{t\} = \dfrac{1}{s^2}$ and we also have $f(0)=0.$ Using our formula, we get

$$


\begin{aligned}L{𝑓^{′}(𝑡)} & =𝑠𝐹(𝑠)−𝑓(0) \\ & =𝑠(\frac{1}{𝑠^{2}})−0 \\ & =\frac{1}{𝑠}.\end{aligned}


$$

On the other hand, we know $f'(t) = 1$ and $\mathcal L\{1\} = \dfrac{1}{s}.$ So, we have

$$


\mathcal L\{f'(t)\} = \mathcal L\{1\} = \dfrac{1}{s},


$$

which means that our formula gives the correct result in this case.

We can derive this formula from the definition of the Laplace transform. Let's see how.

### Deriving the Derivative Formula

Assume that $f(t)$ is continuous on $[0,\infty)$ and of exponential order $s_0$, and that $f'(t)$ is piecewise continuous on $[0,\infty)$.

The Laplace transform of $f$ is defined by

$$


\mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t)\,\textrm{d}t.


$$

Replacing $f(t)$ with $f'(t)$ in this definition gives

$$


\mathcal{L}\{f'(t)\} = \int_{0}^{\infty} e^{-st} f'(t)\,\textrm{d}t.


$$

Writing the improper integral as a limit of proper integrals, we have

$$


\begin{aligned}L{𝑓^{′}(𝑡)} & =∫_{∞0}^{}𝑒^{−𝑠𝑡}𝑓^{′}(𝑡)\,d𝑡 \\ & =\underset{𝑎→∞}{lim}∫_{𝑎0}^{}𝑒^{−𝑠𝑡}𝑓^{′}(𝑡)\,d𝑡.\end{aligned}


$$

We now apply integration by parts on $[0,a]$, choosing

$$


u = e^{-st}, \qquad \textrm{d}v = f'(t)\,\textrm{d}t.


$$

Then

$$


\textrm{d}u = -s e^{-st}\,\textrm{d}t, \qquad v = f(t).


$$

Using the integration-by-parts formula, we obtain

$$


\begin{aligned}∫_{𝑎0}^{}𝑒^{−𝑠𝑡}𝑓^{′}(𝑡)\,d𝑡 & =𝑒^{−𝑠𝑡}𝑓(𝑡)_{𝑎0}^{}−∫_{𝑎0}^{}(−𝑠𝑒^{−𝑠𝑡})𝑓(𝑡)\,d𝑡 \\ & =𝑒^{−𝑠𝑎}𝑓(𝑎)−𝑓(0)+𝑠∫_{𝑎0}^{}𝑒^{−𝑠𝑡}𝑓(𝑡)\,d𝑡.\end{aligned}


$$

Substituting this into the previous expression gives

$$


\begin{aligned}L{𝑓^{′}(𝑡)} & =\underset{𝑎→∞}{lim}(𝑒^{−𝑠𝑎}𝑓(𝑎)−𝑓(0)+𝑠∫_{𝑎0}^{}𝑒^{−𝑠𝑡}𝑓(𝑡)\,d𝑡) \\ & =𝑠∫_{∞0}^{}𝑒^{−𝑠𝑡}𝑓(𝑡)\,d𝑡−𝑓(0)+\underset{𝑎→∞}{lim}𝑒^{−𝑠𝑎}𝑓(𝑎).\end{aligned}


$$

Since $f$ is of exponential order $s_0$, there exist constants $K>0$ and $T>0$ such that

$$


|f(t)| \le K e^{s_0 t} \qquad \text{for all } t>T.


$$

Therefore, for $s>s_0$,

$$


|e^{-sa} f(a)| \le K e^{-(s-s_0)a} \longrightarrow 0 \quad \text{as } a\to\infty.


$$

Thus, we have established the **derivative property**:

$$


\mathcal{L}\{f'(t)\} = s\,\mathcal{L}\{f(t)\} - f(0), \qquad s>s_0.


$$

### Example: Calculating the Laplace Transform of the Derivative of a Function

#### Question

Find the Laplace transform of $f'(t)$ for $s > 3$ given that the function $f(t)$ is continuous over $[0,\infty),$ $f(0)=0,$ and

$$


\mathcal{L}\left\{f(t)\right\} = \dfrac{6}{s^2-5s+6}, \quad s>3.


$$

Assume that $f'$ is piecewise continuous on $[0,\infty).$

#### Explanation

Suppose $F(s) = \mathcal L \{f(t)\}$ where $f(t)$ is a continuous function of exponential order $a$ on $[0,\infty).$ If $f'(t)$ is piecewise continuous on $[0,\infty),$ then

$$


\mathcal{L}\left\{ f'(t) \right\} = s \mathcal{L}\left\{ f(t) \right\} - f(0).


$$

Therefore, we can calculate the Laplace transform of $f'(t)$ as follows:

$$


\begin{aligned}L{𝑓^{′}(𝑡)} & =𝑠L{𝑓(𝑡)}−𝑓(0) \\ & =𝑠⋅\frac{6}{𝑠^{2}−5𝑠+6}−0 \\ & =\frac{6𝑠}{𝑠^{2}−5𝑠+6}\end{aligned}


$$

valid for $s > 3.$

### Laplace Transforms of Second Derivatives

In differential equations, second derivatives arise naturally when modeling acceleration, curvature, or restoring forces. To use Laplace transforms effectively in these settings, we need to understand how the transform handles *higher-order derivatives*.

As with the first derivative, the key idea is that differentiation with respect to $t$ becomes an algebraic operation in $s$, together with terms that depend on initial values. We now derive the corresponding formula for the second derivative.

Assume that

- $y(t)$ is *continuous* on $[0,\infty)$ and of exponential order $s_0$,

- $y'(t)$ is *continuous* on $[0,\infty)$,

- $y''(t)$ is *piecewise continuous* on $[0,\infty)$.

Then the Laplace transform of $y''(t)$ exists for all $s>s_0$, and

$$


\mathcal{L}\{y''(t)\} = s^2 \mathcal{L}\{y(t)\} - s y(0) - y'(0).


$$

To derive this result, recall the formula for the Laplace transform of a first derivative:

$$


\mathcal{L}\{y'(t)\} = s \mathcal{L}\{y(t)\} - y(0), \qquad s > s_0.


$$

Since $y'(t)$ is continuous and $y''(t)$ is piecewise continuous, we may apply this formula to $y'(t)$:

$$


\mathcal{L}\{y''(t)\} = s \mathcal{L}\{y'(t)\} - y'(0).


$$

Substituting $\mathcal{L}\{y'(t)\} = s \mathcal{L}\{y(t)\} - y(0)$, we obtain

$$


\begin{aligned}L{𝑦^{″}(𝑡)} & =𝑠[𝑠L{𝑦(𝑡)}−𝑦(0)]−𝑦^{′}(0) \\ & =𝑠^{2}L{𝑦(𝑡)}−𝑠𝑦(0)−𝑦^{′}(0),\end{aligned}


$$

as claimed.

### Example: Calculating the Laplace Transform of the Second Derivative of a Function

#### Question

Find the Laplace transform $\mathcal{L}\left\{f''(t) \right\}$ for $s > 0,$ given that the function $f(t)$ is continuous on $[0,\infty),$ $f'(0)=2,$ $f(0)=-1,$ and

$$


\mathcal{L}\left\{f(t)\right\} = \dfrac{2 - s}{s^2+4}, \quad s>0.


$$

Assume that $f'$ is continuous and $f''$ piecewise continuous on $[0,\infty).$

#### Explanation

Suppose $F(s) = \mathcal L \{f(t)\}$ where $f(t)$ is a continuous function of exponential order $a$ on $[0,\infty).$ If $f'(t)$ is continuous and $f''(t)$ is piecewise continuous on $[0,\infty),$ then

$$


\begin{aligned}L{𝑓^{″}(𝑡)} & =𝑠^{2}L{𝑓(𝑡)}−𝑠𝑓(0)−𝑓^{′}(0).\end{aligned}


$$

Therefore, we can calculate the Laplace transform of $f''(t)$ as follows:

$$


\begin{aligned}L{𝑓^{″}(𝑡)} & =𝑠^{2}L{𝑓(𝑡)}−𝑠𝑓(0)−𝑓^{′}(0) \\ & =𝑠^{2}⋅\frac{2−𝑠}{𝑠^{2}+4}−𝑠⋅(−1)−2 \\ & =\frac{𝑠^{2}(2−𝑠)}{𝑠^{2}+4}+𝑠−2 \\ & =−\frac{𝑠^{2}(𝑠−2)}{𝑠^{2}+4}+(𝑠−2) \\ & =(𝑠−2)(−\frac{𝑠^{2}}{𝑠^{2}+4}+1) \\ & =(𝑠−2)(\frac{4}{𝑠^{2}+4}) \\ & =\frac{4(𝑠−2)}{𝑠^{2}+4}\end{aligned}


$$

valid for $s > 0.$

### The General Result

If $f(t)$ is piecewise continuous on $[0,\infty)$, of exponential order $a$, and

$$


F(s)=\mathcal L\{f(t)\},


$$

then for any integer $n\ge 1$ and all $s>a$,

$$


\mathcal L\{f^{(n)}(t)\} = s^n F(s) - s^{n-1} f(0) - s^{n-2} f'(0) - \cdots - f^{(n-1)}(0).


$$

This formula is the key tool for systematically solving linear differential equations with given initial conditions using Laplace transforms.
