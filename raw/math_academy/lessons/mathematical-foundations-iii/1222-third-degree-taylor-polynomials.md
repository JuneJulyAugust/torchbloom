# Third-Degree Taylor Polynomials

Source: https://www.mathacademy.com/topics/1222?courseId=136
Topic ID: 1222

## Prerequisites

- [Analyzing Second-Degree Taylor Polynomials](./3825-analyzing-second-degree-taylor-polynomials.md)

## Lesson

### Introduction

Recall that we can approximate a function $f(x)$ using a second-degree Taylor polynomial. To get this second-degree Taylor polynomial, we add a second term to the linear approximation:

$$


P_2(x) = \underbrace{f(a) + f'(a)(x-a)}_{\text{linear approximation}} + \underbrace{\dfrac{1}{2}f''(a)(x-a)^2}_{\textrm{new quadratic term}}.


$$

As it turns out, we can keep on adding more and more terms, each time getting better and better approximations. The **third-degree Taylor polynomial** approximation to $f(x),$ denoted $P_3(x),$ is given by

$$


P_3(x) = \underbrace{f(a) + f'(a)(x-a) + \dfrac{1}{2!}f''(a)(x-a)^2}_{\text{quadratic approximation}} + \underbrace{\dfrac{1}{3!}f^{(3)}(a)(x-a)^3}_{\text{new cubic term}}.


$$

Note that $f^{(3)}$ represents the third derivative of $f.$ In other words, $f^{(3)} = f'''.$

In general, $P_3(x)$ is a better approximation to $f(x)$ compared to $P_2(x),$ provided that $x$ is close to $a.$

**Note:** The phrase "Taylor polynomial" refers to a polynomial that's used to approximate a function.

- The first-degree Taylor polynomial is the linear approximation.

- The second-degree Taylor polynomial is the quadratic approximation.

- The third-degree Taylor polynomial is the cubic approximation.

### Example: Computing the Third-Degree Taylor Polynomial For a Function Given Some Derivatives

#### Question

Let $f(x)$ be a function with $f(-1)=-1, f'(-1)=3, f''(-1)=-6$ and $f'''(-1)=6.$ What is the third-degree Taylor polynomial for $f(x)$ about $x=-1?$

#### Explanation

The third-degree Taylor polynomial of $f(x)$ about $x=-1$ is

$$


\begin{aligned}𝑃_{3}(𝑥) & =𝑓(−1)+𝑓^{′}(−1)(𝑥+1)+\frac{𝑓^{″}(−1)}{2!}(𝑥+1)^{2}+\frac{𝑓^{‴}(−1)}{3!}(𝑥+1)^{3} \\ & =𝑓(−1)+𝑓^{′}(−1)(𝑥+1)+\frac{𝑓^{″}(−1)}{2}(𝑥+1)^{2}+\frac{𝑓^{‴}(−1)}{6}(𝑥+1)^{3}.\end{aligned}


$$

We have been given the following set of values:

$$


\begin{aligned}𝑓(−1) & =−1 \\ 𝑓^{′}(−1) & =3 \\ 𝑓^{″}(−1) & =−6 \\ 𝑓^{‴}(−1) & =6.\end{aligned}


$$

Substituting the given values into our Taylor polynomial, we get

$$


\begin{aligned}𝑃_{3}(𝑥) & =−1+3(𝑥+1)+\frac{(−6)}{2}(𝑥+1)^{2}+\frac{6}{6}(𝑥+1)^{3} \\ & =−1+3(𝑥+1)−3(𝑥+1)^{2}+(𝑥+1)^{3}.\end{aligned}


$$

### Example: Computing the Third-Degree Taylor Polynomial For a Given Function About a Given Point

#### Question

Find the third-degree Taylor polynomial of $f(x) = \ln(1+x)$ about $x=0.$

#### Explanation

To find the third-degree Taylor polynomial about $x=0,$ we plug $a=0$ into the general formula to give

$$


P_3(x) = f(0) + f'(0)(x-0) + \dfrac{1}{2!}f''(0)(x-0)^2 + \dfrac{1}{3!}f'''(0)(x-0)^3.


$$

We need to compute $f(0),$ $f'(0),$ $f''(0),$ and $f'''(0),$ as follows:

$$


\begin{aligned}𝑓(𝑥) & =ln⁡(1+𝑥) & ⟹ & & 𝑓(0) & =ln⁡(1+0)=0 \\ 𝑓^{′}(𝑥) & =(1+𝑥)^{−1} & ⟹ & & 𝑓^{′}(0) & =(1+0)^{−1}=1 \\ 𝑓^{″}(𝑥) & =−(1+𝑥)^{−2} & ⟹ & & 𝑓^{″}(0) & =−(1+0)^{−2}=−1 \\ 𝑓^{(3)}(𝑥) & =2(1+𝑥)^{−3} & ⟹ & & 𝑓^{‴}(0) & =2(1+0)^{−3}=2.\end{aligned}


$$

Finally, we plug the results for $f(0),$ $f'(0),$ $f''(0),$ and $f'''(0)$ into our third-degree Taylor polynomial. This gives

$$


\begin{aligned}𝑃_{3}(𝑥) & =0+(1)(𝑥−0)+\frac{1}{2!}(−1)(𝑥−0)^{2}+\frac{1}{3!}(2)(𝑥−0)^{3} \\ & =𝑥−\frac{𝑥^{2}}{2}+\frac{𝑥^{3}}{3}.\end{aligned}


$$

### Example: Finding the Coefficient of a Term In the Third-Degree Taylor Polynomial of a Given Function

#### Question

What is the coefficient of $(x-1)^3$ in the third-degree Taylor polynomial of $f(x) = e^{-2x}?$

#### Explanation

The coefficient of $(x-1)^3$ is $\dfrac{1}{3!}f^{(3)}(1).$ Let's compute the necessary derivatives:

$$


\begin{aligned}𝑓(𝑥) & =𝑒^{−2𝑥} \\ 𝑓^{′}(𝑥) & =−2𝑒^{−2𝑥} \\ 𝑓^{″}(𝑥) & =4𝑒^{−2𝑥} \\ 𝑓^{(3)}(𝑥) & =−8𝑒^{−2𝑥}.\end{aligned}


$$

Therefore,

$$


\dfrac{1}{3!}f^{(3)}(1) =\dfrac{1}{6} \left( -8e^{-2} \right) = -\dfrac{4}{3e^2}.


$$

So the coefficient of $(x-1)^3$ is $-\dfrac{4}{3e^2}.$
