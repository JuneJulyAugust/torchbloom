# Second and Higher-Order Derivatives

Source: https://www.mathacademy.com/topics/281?courseId=24
Topic ID: 281

## Prerequisites

- [Differentiating Trigonometric Functions](./280-differentiating-trigonometric-functions.md)
- [Differentiating Logarithmic Functions](./1116-differentiating-logarithmic-functions.md)

## Lesson

### Introduction

The **second derivative** is the derivative of a function's first derivative. It is written as $f''(x).$

To calculate the second derivative of a function $f(x)$, we first need to calculate the first derivative $f'(x).$ After that, we calculate the derivative of $f'(x).$ So using prime $\left('\right)$ notation, we can define the second derivative of a function $f(x)$ as

$$


f''(x) = (f'(x))'.


$$

Let's try it out with the function $f(x) = 4x^2 + 3x.$ The first derivative is given by

$$


\begin{aligned}𝑓^{′}(𝑥) & =(4𝑥^{2}+3𝑥)^{′} \\ & =4(2)𝑥+3 \\ & =8𝑥+3.\end{aligned}


$$

We can now calculate the derivative of $f'(x)$ to give us $f''(x).$ We get

$$


\begin{aligned}𝑓^{″}(𝑥) & =(𝑓^{′}(𝑥))^{′} \\ & =(8𝑥+3)^{′} \\ & =8+0 \\ & =8.\end{aligned}


$$

Therefore, the second derivative of $f(x)$ is $8.$

### Example: Computing Second Order Derivatives

#### Question

Find $f''(x)$ for $f(x) = 2x^3 + \dfrac 1 x.$

#### Explanation

Computing the first derivative, we have

$$


\begin{aligned}𝑓^{′}(𝑥) & =(2𝑥^{3}+\frac{1}{𝑥})^{′} \\ & =(2𝑥^{3}+𝑥^{−1})^{′} \\ & =2(3)𝑥^{2}−𝑥^{−2} \\ & =6𝑥^{2}−𝑥^{−2}.\end{aligned}


$$

Computing the second derivative, we have

$$


\begin{aligned}𝑓^{″}(𝑥) & =(6𝑥^{2}−𝑥^{−2})^{′} \\ & =6(2)𝑥−(−2)𝑥^{−3} \\ & =12𝑥+2𝑥^{−3}.\end{aligned}


$$

### Using Leibniz Notation

We can also express the second derivative using $\dfrac{\text{d}}{\text{d} x}$ notation, also known as Leibniz notation. If we have a function $f(x),$ then the second derivative $f''(x)$ can be written as

$$


f''(x) = \dfrac {\textrm d^2 f}{\textrm d x^2} = \dfrac {\textrm d} {\textrm d x}\left(\dfrac {\textrm df} {\textrm d x}\right).


$$

Sometimes, we define a function as $y=f(x),$ in which case we could also express the second derivative as $\dfrac {\textrm d^2 y}{\textrm d x^2}.$

### Example: Computing Second Order Derivatives Using Leibniz Notation

#### Question

Calculate $\dfrac {\textrm d^2 y}{\textrm d x^2}$ for $y = 3 x^4 + 5x+ \sqrt x.$

#### Explanation

Computing the first derivative, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(3𝑥^{4}+5𝑥+\sqrt{𝑥}) \\ & =\frac{d}{d𝑥}(3𝑥^{4}+5𝑥+𝑥^{1/2}) \\ & =3(4)𝑥^{3}+5+\frac{1}{2}𝑥^{−1/2} \\ & =12𝑥^{3}+5+\frac{1}{2}𝑥^{−1/2}.\end{aligned}


$$

Computing the second derivative, we get

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑥^{2}} & =\frac{d}{d𝑥}(12𝑥^{3}+5+\frac{1}{2}𝑥^{−1/2}) \\ & =12(3)𝑥^{2}+0+\frac{1}{2}(−\frac{1}{2})𝑥^{−3/2} \\ & =36𝑥^{2}−\frac{1}{4}𝑥^{−3/2}.\end{aligned}


$$

### Higher Order Derivatives

To calculate the third derivative of the function $f(x)=2x^4+3x,$ we need to differentiate it three times.

Computing the first derivative, we get

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(2𝑥^{4}+3𝑥) \\ & =2⋅4𝑥^{4−1}+1⋅3𝑥^{1−1} \\ & =8𝑥^{3}+3𝑥^{0} \\ & =8𝑥^{3}+3.\end{aligned}


$$

Computing the second derivative, we get

$$


\begin{aligned}𝑓^{″}(𝑥) & =\frac{d}{d𝑥}(8𝑥^{3}+3) \\ & =8⋅3𝑥^{3−1}+0 \\ & =24𝑥^{2}.\end{aligned}


$$

Finally, computing the third derivative, we get

$$


\begin{aligned}𝑓^{‴}(𝑥) & =\frac{d}{d𝑥}(24𝑥^{2}) \\ & =24⋅2𝑥^{2−1} \\ & =48𝑥.\end{aligned}


$$

So, the third derivative of $f(x)$ is $f'''(x)=48x.$

Using Leibniz notation, the third derivative of a function $f(x)$ can also be written as

$$


f'''(x)=\dfrac {\textrm d}{\textrm d x}\left(\dfrac {\textrm d}{\textrm d x}\left(\dfrac {\textrm d}{\textrm d x}(f(x))\right)\right)=\dfrac {\textrm d^3}{\textrm d x^3}f(x).


$$

In general, if we want to calculate the $n$-th order derivative of a function, we need to differentiate it $n$ times:

$$


f^{(n)}(x)=\dfrac {\textrm d^n}{\textrm d x^n}f(x).


$$

**Note**: The parenthesis in the superscript of $f^{(n)}(x)$ means that it is the the $n$-th derivative of $f(x).$ This is to distinguish it from $f^n(x)$ with no parenthesis, which indicates the $n$-th power of $f(x).$

### Example: Computing Higher Order Derivatives

#### Question

Given $y = \dfrac {3 x^2 + x - 1} x$, find $\dfrac {\textrm d^{3} y} {\textrm d x^3}.$

#### Explanation

First, notice that we can rewrite the function as the sum of powers of $x,$ as follows:

$$


\begin{aligned}𝑦 & =\frac{3𝑥^{2}+𝑥−1}{𝑥} \\ & =\frac{3𝑥^{2}}{𝑥}+\frac{𝑥}{𝑥}−\frac{1}{𝑥} \\ & =3𝑥+1−𝑥^{−1}\end{aligned}


$$

Now, computing the first derivative, we get

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(3𝑥+1−𝑥^{−1}) \\ & =3+0−(−1)𝑥^{−2} \\ & =3+𝑥^{−2}.\end{aligned}


$$

Computing the second derivative, we get

$$


\begin{aligned}\frac{d^{2}𝑦}{d𝑥^{2}} & =\frac{d}{d𝑥}(3+𝑥^{−2}) \\ & =0+(−2)𝑥^{−3} \\ & =−2𝑥^{−3}.\end{aligned}


$$

Finally, computing the third derivative, we get

$$


\begin{aligned}\frac{d^{3}𝑦}{d𝑥^{3}} & =\frac{d}{d𝑥}(−2𝑥^{−3}) \\ & =−2(−3)𝑥^{−4} \\ & =6𝑥^{−4}.\end{aligned}


$$
