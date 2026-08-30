# Calculating Derivatives From Data and Tables

Source: https://www.mathacademy.com/topics/1249?courseId=111
Topic ID: 1249

## Prerequisites

- [The Quotient Rule for Differentiation](./1110-the-quotient-rule-for-differentiation.md)

## Lesson

### Introduction

Let's suppose we only know the values of the functions $f(x)$ and $g(x)$ at $x=0$ along with their derivatives, as given in the table below.

Can we calculate $\dfrac{\text{d}}{\text{d}x}\Big(f(x)g(x)\Big)$ at $x=0?$

Using the product rule, we have

$$


\dfrac{\text{d}}{\text{d}x}\Big( f(x)g(x)\Big) = f'(x)g(x)+f(x)g'(x).


$$

At the point where $x=0,$ this gives

$$


\left.\dfrac{\text{d}}{\text{d}x}\Big( f(x)g(x)\Big) \right|_{x=0} = f'(0)g(0)+f(0)g'(0).


$$

All of these values are given in the table! So, substituting the values from the table into the formula, we conclude that

$$


\begin{aligned}\frac{d}{d𝑥}(𝑓(𝑥)𝑔(𝑥))_{𝑥=0} & =𝑓^{′}(0)𝑔(0)+𝑓(0)𝑔^{′}(0) \\ & =4⋅3+2⋅5 \\ & =22.\end{aligned}


$$

### Example: Computing the Derivative of a Product Given the Necessary Data

#### Question

The values of functions $f(x)$ and $g(x)$ and their derivatives at $x=0$ are given in the table below.

Compute $\dfrac{\text{d}}{\text{d}x}\big(f(x)g(x)\big)$ at $x=0.$

#### Explanation

Using the product rule, we get

$$


\dfrac{\text{d}}{\text{d}x}\big(f(x)g(x)\big) = f(x)g'(x)+f'(x)g(x).


$$

At the point where $x=0$, this gives

$$


\begin{aligned}\frac{d}{d𝑥}(𝑓(𝑥)𝑔(𝑥))_{𝑥=0} & =𝑓(0)𝑔^{′}(0)+𝑓^{′}(0)𝑔(0) \\ & =1⋅0+3⋅(−2) \\ & =−6.\end{aligned}


$$

### Example: Computing the Derivative of a Quotient Given the Necessary Data

#### Question

The values of functions $h(x)$ and $z(x)$ and their derivatives at $x=-1$ are given in the table below.

Compute $\dfrac{\text{d}}{\text{d}x}\left(\dfrac{h(x)}{z(x)}\right)$ at $x=-1.$

#### Explanation

Using the quotient rule, we get

$$


\dfrac{\text{d}}{\text{d}x}\left(\dfrac{h(x)}{z(x)}\right) = \dfrac{h'(x)z(x)-h(x)z'(x)}{(z(x))^2}.


$$

At the point where $x=-1$, this gives

$$


\begin{aligned}\frac{d}{d𝑥}(\frac{ℎ(𝑥)}{𝑧(𝑥)})_{𝑥=−1} & =\frac{ℎ^{′}(−1)𝑧(−1)−ℎ(−1)𝑧^{′}(−1)}{(𝑧(−1))^{2}} \\ & =\frac{6⋅2−(−4)⋅3}{2^{2}} \\ & =\frac{24}{4} \\ & =6.\end{aligned}


$$

### Example: Computing the Derivative of a Linear Combination of Functions Given the Necessary Data

#### Question

The values of functions $p(x)$ and $q(x)$ and their derivatives at $x=-3$ are given in the table below.

Compute $\dfrac{\text{d}}{\text{d}x}\big(p(x) + 5q(x) \big)$ at $x=-3.$

#### Explanation

Using the sum and constant multiple rules, we get

$$


\dfrac{\text{d}}{\text{d}x}\left( p(x) + 5q(x) \right) = p'(x) + 5q'(x).


$$

At the point where $x=-3$, this gives

$$


\begin{aligned}\frac{d}{d𝑥}(𝑝(𝑥)+5𝑞(𝑥))_{𝑥=−3} & =𝑝^{′}(−3)+5𝑞^{′}(−3) \\ & =0+5⋅(−2) \\ & =−10.\end{aligned}


$$

### Example: Computing the Derivative of the Product or Quotient of a Composition of Functions Given the Necessary Data

#### Question

For the functions $f(x)$ and $g(x),$ we have

$$


f(1)=2, \quad f'(1)=2, \quad g(1)=-1, \quad g'(1)=3.


$$

If $h(x) = \left(f(x)-1 \right)\left(2g(x)+1\right),$ compute $h'(1).$

#### Explanation

The product rule states that

$$


\dfrac{\text{d}}{\text{d}x}\Big(uv\Big) = u \dfrac{\textrm d v}{\textrm d x} +v \dfrac{\textrm du}{\textrm d x}.


$$

Let $u=f(x)-1$ and $v=2g(x)+1.$ Differentiating each, we get

$$


\dfrac{\textrm d u}{\textrm d x} = f'(x) \qquad \text{and}\qquad \dfrac{\textrm d v}{\textrm d x} = 2g'(x).


$$

Substituting this into the product rule gives

$$


\begin{aligned}ℎ^{′}(𝑥) & =𝑢\frac{d𝑣}{d𝑥}+𝑣\frac{d𝑢}{d𝑥} \\ & =(𝑓(𝑥)−1)⋅2𝑔^{′}(𝑥)+(2𝑔(𝑥)+1)⋅𝑓^{′}(𝑥) \\ & =2𝑔^{′}(𝑥)(𝑓(𝑥)−1)+𝑓^{′}(𝑥)(2𝑔(𝑥)+1).\end{aligned}


$$

At $x=1$, this gives

$$


\begin{aligned}ℎ^{′}(1) & =2𝑔^{′}(1)(𝑓(1)−1)+𝑓^{′}(1)(2𝑔(1)+1) \\ & =2⋅3⋅(2−1)+2⋅(2⋅(−1)+1) \\ & =4.\end{aligned}


$$
