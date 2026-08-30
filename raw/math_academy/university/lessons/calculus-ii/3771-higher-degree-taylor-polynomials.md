# Higher-Degree Taylor Polynomials

Source: https://www.mathacademy.com/topics/3771?courseId=106
Topic ID: 3771

## Prerequisites

- [Third-Degree Taylor Polynomials](./1222-third-degree-taylor-polynomials.md)

## Lesson

### Introduction

The $n$th-degree Taylor polynomial of a function $f(x)$ around the point $x=a$ is

$$


P_n(x) = f(a) + f'(a)(x-a) + \dfrac{f''(a)}{2!}(x-a)^2 + \cdots + \dfrac{f^{(n)}(a)}{n!}(x-a)^n.


$$

In particular, the coefficient of the $k$th-degree term is

$$


\dfrac{f^{(k)}(a)}{k!}.


$$

### Example: Computing a Higher-Degree Taylor Polynomial Of a Given Function About a Given Point

#### Question

Let $f(x) = \sin{x}.$ Calculate the fourth-degree Taylor polynomial for $f(x)$ about $x=\dfrac{\pi}{2}.$

#### Explanation

The fourth-degree Taylor polynomial of $f(x)$ about $x=a$ is given by

$$


P_4(x) = f(a) + f'(a)(x-a) + \dfrac{f''(a)}{2!}(x-a)^2 + \dfrac{f'''(a)}{3!}(x-a)^3 + \dfrac{f^{(4)}(a)}{4!}(x-a)^4.


$$

Here, we have $a=\dfrac{\pi}{2},$ so

$$


\begin{aligned}𝑃_{4}(𝑥) & =𝑓(\frac{𝜋}{2})+𝑓^{′}(\frac{𝜋}{2})(𝑥−\frac{𝜋}{2})+\frac{𝑓^{″}(\frac{𝜋}{2})}{2}(𝑥−\frac{𝜋}{2})^{2} \\ & \,\,\,\,+\frac{𝑓^{‴}(\frac{𝜋}{2})}{2}(𝑥−\frac{𝜋}{2})^{3}+\frac{𝑓^{(4)}(\frac{𝜋}{2})}{2}(𝑥−\frac{𝜋}{2})^{4}.\end{aligned}


$$

So we need to work out $f\left(\dfrac{\pi}{2}\right),$ $f'\left(\dfrac{\pi}{2}\right),$ $f''\left(\dfrac{\pi}{2}\right),$ $f'''\left(\dfrac{\pi}{2}\right)$ and $f^{(4)}\left(\dfrac{\pi}{2}\right),$ as follows:

$$


\begin{aligned}𝑓(𝑥) & =sin⁡𝑥 & ⟹ & & 𝑓(\frac{𝜋}{2}) & =1 \\ 𝑓^{′}(𝑥) & =cos⁡𝑥 & ⟹ & & 𝑓^{′}(\frac{𝜋}{2}) & =0 \\ 𝑓^{″}(𝑥) & =−sin⁡𝑥 & ⟹ & & 𝑓^{″}(\frac{𝜋}{2}) & =−1 \\ 𝑓^{‴}(𝑥) & =−cos⁡𝑥 & ⟹ & & 𝑓^{‴}(\frac{𝜋}{2}) & =0 \\ 𝑓^{(4)}(𝑥) & =sin⁡𝑥 & ⟹ & & 𝑓^{(4)}(\frac{𝜋}{2}) & =1.\end{aligned}


$$

Therefore, $P_4(x)$ is given by

$$


\begin{aligned}𝑃_{4}(𝑥) & =1−\frac{1}{2!}(𝑥−\frac{𝜋}{2})^{2}+\frac{1}{4!}(𝑥−\frac{𝜋}{2})^{4} \\ & =1−\frac{1}{2}(𝑥−\frac{𝜋}{2})^{2}+\frac{1}{24}(𝑥−\frac{𝜋}{2})^{4}.\end{aligned}


$$

### Example: Obtaining a Higher-Order Derivative Of a Function Given its Higher-Degree Taylor Polynomial

#### Question

The fourth-degree Taylor polynomial of $f(x)$ about $x=0$ is given by

$$


P_4(x) = 1+2x-3x^2+4x^3-5x^4.


$$

What is $f^{(4)}(0)?$

#### Explanation

The coefficient of $x^4$ is given by $\dfrac{f^{(4)}(0)}{4!}.$ Therefore,

$$


\begin{aligned}\frac{𝑓^{(4)}(0)}{4!} & =−5 \\ \frac{𝑓^{(4)}(0)}{24} & =−5 \\ 𝑓^{(4)}(0) & =−120.\end{aligned}


$$
