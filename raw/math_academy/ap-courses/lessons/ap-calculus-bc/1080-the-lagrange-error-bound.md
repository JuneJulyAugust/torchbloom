# The Lagrange Error Bound

Source: https://www.mathacademy.com/topics/1080?courseId=21
Topic ID: 1080

## Prerequisites

- [Higher-Degree Taylor Polynomials](./3771-higher-degree-taylor-polynomials.md)

## Lesson

### Introduction

Suppose that we want to *approximate* $f(x) = e^x$ for some value of $x.$ We can do this using the second-degree Taylor polynomial about a point $x=a.$ For example, the second-degree Taylor polynomial for $e^x$ about the point $x=1$ is shown below:

$$


e^x \approx P_2(x) = e + e(x-1) + \dfrac 1 2 e(x-1)^2


$$

In general, the polynomial $P_2(x)$ is only an approximation to the function $f(x),$ which means that there will usually be some error whenever we use $P_2$ to approximate $f.$ We want to know how bad this error can get. Can we find an upper bound for the error?

Let $R_2(x)$ be the **error** (or **remainder**) that we get when we use $P_2$ to approximate $f(x)=e^x,$ so

$$


R_2(x) = e^x - P_2(x).


$$

The **Lagrange error bound** states that an upper bound for $R_2$ is given by,

$$


|R_2| \leq \dfrac{M}{3!}|x-a|^{3},


$$

where $M$ the maximum value of $|f^{(3)}(x)|$ on the interval between $a$ and $x.$

In our case, since our Taylor polynomial is taken about the point $a=1,$ the Lagrange error bound becomes

$$


|R_2| \leq \dfrac{M}{3!}|x-1|^{3}.


$$

Notice that the Lagrange error bound looks a lot like the last term of the *next* Taylor polynomial, $P_3(x).$

The tricky part is finding the value of $M.$ We'll learn how to do that in the following example.

### Example: Finding an Upper Bound for the Error Using the Second-Degree Taylor Polynomial

#### Question

Let $f(x)=e^{x}$ and let $P_2(x)$ be the second-degree Taylor polynomial of $f(x)$ about $x=1.$ Use the Lagrange error bound to find an upper bound for the error when $P_2(x)$ is used to approximate $e^{1.1}.$

#### Explanation

The Lagrange error bound states that an upper bound for the error $R_2$ obtained when using the second-degree Taylor polynomial $P_2$ to approximate $f(x)$ is given by

$$


|R_2| \leq \dfrac{M}{3!}|x-1|^{3},


$$

where $M$ is the maximum value of $|f^{(3)}(x)|$ on the interval between $a=1$ and $x=1.1.$ Plugging $x=1.1$ into the above gives

$$


\begin{aligned}|𝑅_{2}| & ≤\frac{𝑀}{3!}|1.1−1|^{3} \\ |𝑅_{2}| & ≤\frac{𝑀}{6}|0.1|^{3}.\end{aligned}


$$

To find $M,$ we need to compute $|f^{(3)}(x)|$ and then maximize it on the interval $[1,1.1].$ Taking the derivatives, we get

$$


\begin{aligned}𝑓(𝑥) & =𝑒^{𝑥} \\ 𝑓^{′}(𝑥) & =𝑒^{𝑥} \\ 𝑓^{″}(𝑥) & =𝑒^{𝑥} \\ 𝑓^{(3)}(𝑥) & =𝑒^{𝑥} \\ |𝑓^{(3)}(𝑥)| & =|𝑒^{𝑥}| \\ & =𝑒^{𝑥}\end{aligned}


$$

Since $|f^{(3)}(x)|=e^x$ is an increasing function on the interval $[1,1.1],$ its value is greatest at $x=1.1.$ So

$$


M = |f^{(3)}(1.1)| =e^{1.1},


$$

and therefore, the upper bound is

$$


|R_2| \leq \dfrac{e^{1.1}}{6}|0.1|^{3} \approx 0.000\,501,


$$

rounded to six decimal places.

### The General Result of the Lagrange Error Bound

The Lagrange error bound that we've discussed so far is valid only for the error associated with a second-degree Taylor polynomial. But we can generalize the result to higher-order Taylor polynomials.

Let $R_n(x)$ be the error involved in approximating a function $f(x)$ by its $n$th-degree Taylor polynomial $P_n(x)$ about $x=a.$ So, we have

$$


R_n(x) = f(x) - P_n(x).


$$

Then the Lagrange error bound for $R_n$ is given by

$$


|R_n(x)| \leq \dfrac{M}{(n+1)!}|x-a|^{n+1},


$$

where $M$ is the maximum value of $|f^{(n+1)}|$ on the interval between $a$ and $x.$

### Example: Finding an Upper Bound for the Error Using the Third-Degree Taylor Polynomial

#### Question

Let $f(x)=\ln(1-x)$ and let $P_3(x)$ be the third-degree Taylor polynomial of $f(x)$ about $x=0.$ Use the Lagrange error bound to find an upper bound for the error when $P_3(x)$ is used to approximate $\ln(0.9)$

#### Explanation

The Lagrange error bound states that an upper bound for the error $R_3$ obtained when using the third-degree Taylor polynomial $P_3$ to approximate $f(x)$ is given by

$$


|R_3| \leq \dfrac{M}{4!}|x-0|^{4},


$$

where $M$ is the maximum value of $|f^{(4)}(x)|$ on the interval between $a=0$ and $x=0.1.$ Plugging $x=0.1$ into the above gives

$$


\begin{aligned}|𝑅_{3}| & ≤\frac{𝑀}{4!}|0.1−0|^{4} \\ |𝑅_{3}| & ≤\frac{𝑀}{24}|0.1|^{4}.\end{aligned}


$$

To find $M,$ we need to compute $|f^{(4)}(x)|$ and then maximize it on the interval $[0,0.1].$ Taking the derivatives, we get

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{1}{𝑥−1} \\ 𝑓^{″}(𝑥) & =−\,\frac{1}{(𝑥−1)^{2}} \\ 𝑓^{‴}(𝑥) & =\frac{2}{(𝑥−1)^{3}} \\ 𝑓^{(4)}(𝑥) & =−\,\frac{6}{(𝑥−1)^{4}} \\ |𝑓^{(4)}(𝑥)| & =−\,\frac{6}{(𝑥−1)^{4}} \\ & =\frac{6}{(𝑥−1)^{4}}\end{aligned}


$$

Since $|f^{(4)}(x)|=\dfrac{6}{(x-1)^4}$ is an increasing function on the interval $[0,0.1],$ its value is greatest at $x=0.1.$ So

$$


M = |f^{(4)}(0.1)| =\dfrac{6}{(0.1-1)^4} = \dfrac{6}{(0.9)^4},


$$

and therefore, the upper bound is

$$


|R_3| \leq \dfrac{ \left( \dfrac{6}{(0.9)^4} \right) }{24}|0.1|^{4} \approx 0.000\,038,


$$

rounded to six decimal places.
