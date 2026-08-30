# Square Roots of Complex Numbers

Source: https://www.mathacademy.com/topics/1234?courseId=101
Topic ID: 1234

## Prerequisites

- [Finding Powers of Complex Numbers Using De Moivre's Theorem](./926-finding-powers-of-complex-numbers-using-de-moivre-s-theorem.md)

## Lesson

### Introduction

In this lesson, we'll learn how to calculate the roots of complex numbers. Let's start by considering the complex number

$$


z = \textrm i.


$$

Our goal is to calculate $z^{1/n} = \sqrt[n]{\textrm i},$ where $n$ is a positive integer.

The first step is to write $z$ in polar form. Since $|z| = 1$ and $\arg(z) = \dfrac\pi2,$ we have

$$


z = \cos\left(\dfrac{\pi}{2}\right) + \textrm i\sin\left(\dfrac{\pi}{2}\right).


$$

Now, here's a trick. We take advantage of the periodicity of sine and cosine and write $z$ as

$$


z = \cos\left(\dfrac{\pi}{2} + 2\pi k\right) + \textrm i\sin\left(\dfrac{\pi}{2} + 2\pi k\right)


$$

where $k$ is an integer.

Taking the $n$th root of the above expression and applying De Moivre's theorem, we have

$$


\begin{aligned}𝑧_{1/𝑛𝑘}^{} & =[cos⁡(\frac{𝜋}{2}+2𝜋𝑘)+isin⁡(\frac{𝜋}{2}+2𝜋𝑘)]^{1/𝑛} \\ & =cos⁡[\frac{1}{𝑛}(\frac{𝜋}{2}+2𝜋𝑘)]+isin⁡[\frac{1}{𝑛}(\frac{𝜋}{2}+2𝜋𝑘)] \\ & =cos⁡(\frac{𝜋}{2𝑛}+\frac{2𝜋𝑘}{𝑛})+isin⁡(\frac{𝜋}{2𝑛}+\frac{2𝜋𝑘}{𝑛}).\end{aligned}


$$

This formula allows us to compute the $n$th roots of $\textrm i.$ We write $z_k^{1/n}$ because different values of $k$ will give different roots.

**Important**: Any nonzero complex number $z$ will have precisely $n$ *distinct* $n$th roots.

### Computing the Square Roots of i

We found that the $n$th roots of $z=\textrm i$ are given by

$$


\begin{aligned}𝑧_{1/𝑛𝑘}^{} & =cos⁡(\frac{𝜋}{2𝑛}+\frac{2𝜋𝑘}{𝑛})+isin⁡(\frac{𝜋}{2𝑛}+\frac{2𝜋𝑘}{𝑛}).\end{aligned}


$$

Let's use this formula to compute the square roots of $\textrm i.$ To do this, we substitute $n=2$ into the above, and we get

$$


z^{1/2}_k = \cos\left(\dfrac{\pi}{4} + \pi k\right) + \textrm i\sin\left(\dfrac{\pi}{4} + \pi k\right).


$$

Finally, setting $k=0, 1$ gives the square roots:

$$


\begin{aligned}𝑘=0:\,\,𝑧_{1/20}^{} & =cos⁡(\frac{𝜋}{4}+𝜋⋅0)+isin⁡(\frac{𝜋}{4}+𝜋⋅0) \\ & =cos⁡(\frac{𝜋}{4})+isin⁡(\frac{𝜋}{4}) \\ & =\frac{\sqrt{√2}}{2}+i\frac{\sqrt{√2}}{2} \\ 𝑘=1:\,\,𝑧_{1/21}^{} & =cos⁡(\frac{𝜋}{4}+𝜋⋅1)+isin⁡(\frac{𝜋}{4}+𝜋⋅1) \\ & =cos⁡(\frac{5𝜋}{4})+isin⁡(\frac{5𝜋}{4}) \\ & =−\frac{\sqrt{√2}}{2}−i\frac{\sqrt{√2}}{2}\end{aligned}


$$

We can stop here because we have found two distinct roots. Note that substituting $k=2,3,4\ldots$ will give roots equal to the ones found above.

Therefore, we conclude that

$$


\sqrt{\textrm i} = \pm \left(\dfrac{\sqrt 2}{2} + \textrm i\dfrac{\sqrt 2}{2}\right).


$$

### A General Formula for the Roots of a Number

Any complex number $z$ can be written in polar form as

$$


z = r\left(\cos\theta+\textrm i\sin\theta\right)


$$

where $r = |z|$ and $\theta = \arg(z).$

Using techniques similar to those we've just seen, we can show that the $n$th roots of $z$ are given by

$$


z_{k}^{1/n} = \sqrt[n]{r}\left[\cos\left(\dfrac{\theta + 2\pi{k}}{n}\right) + \textrm{i}\sin\left(\dfrac{\theta + 2\pi{k}}{n}\right)\right], \qquad k=0, 1, 2,..., n-1.


$$

In this lesson, we will focus on computing the *square* roots of numbers. In a future lesson, we'll look at higher roots.

### Example: Finding a Formula for the Square Roots of a Number With Unit Magnitude

#### Question

The complex square roots of the number $z = \cos\left(\dfrac{4\pi}{5}\right) + \textrm{i}\sin\left(\dfrac{4\pi}{5}\right)$ are given by

$$


z_k^{1/2} = \cos\left(\dfrac{2\pi}{\boxed{a}}+\boxed{b}\cdot{k}\right)+\textrm{i}\sin\left(\dfrac{2\pi}{\boxed{a}}+\boxed{b}\cdot{k}\right),


$$

where $k=0,\,1.$ What are the values of $a$ and $b?$

#### Explanation

Any nonzero complex number $z$ has exactly $n$ distinct $n$th roots. Using de Moivre's theorem, we can write down these roots as

$$


z_{k}^{1/n} = \sqrt[n]{r}\left[\cos\left(\dfrac{\theta + 2\pi{k}}{n}\right) + \textrm{i}\sin\left(\dfrac{\theta + 2\pi{k}}{n}\right)\right],


$$

where

$$


r = |z|, \qquad \theta = \arg(z), \qquad k=0, 1, 2,..., n-1.


$$

In our case, we have

$$


r = 1, \qquad \theta = \dfrac{4\pi}{5}, \qquad n = 2.


$$

Substituting these values into the formula, we obtain

$$


\begin{aligned}𝑧_{1/2𝑘}^{} & =\sqrt{√1}cos⁡\frac{\frac{4𝜋}{5}+2𝜋𝑘}{5}+isin⁡\frac{\frac{4𝜋}{5}+2𝜋𝑘}{5} \\ & =cos⁡(\frac{2𝜋}{5}+𝜋⋅𝑘)+isin⁡(\frac{2𝜋}{5}+𝜋⋅𝑘).\end{aligned}


$$

Therefore, $a={\color{blue}5}$ and $b={\color{red}\pi}.$

### Example: Finding a Formula for the Square Roots of a Number

#### Question

The complex square roots of the number $z = 9\left[\cos\left(\dfrac{5\pi}{3}\right) + \textrm{i}\sin\left(\dfrac{5\pi}{3}\right)\right]$ are given by

$$


z_k^{1/2} = \boxed{a} \left[ \cos\left(\dfrac{5\pi}{\boxed{b}} + \boxed{c}\cdot{k}\right) + \textrm{i} \sin\left(\dfrac{5\pi}{\boxed{b}} + \boxed{c}\cdot{k}\right) \right],


$$

where $k = 0, \, 1.$ What are the values of $a,$ $b,$ and $c?$

#### Explanation

Any nonzero complex number $z$ has exactly $n$ distinct $n$th roots. Using de Moivre's theorem, we can write down these roots as

$$


z_{k}^{1/n} = \sqrt[n]{r}\left[\cos\left(\dfrac{\theta + 2\pi{k}}{n}\right) + \textrm{i}\sin\left(\dfrac{\theta + 2\pi{k}}{n}\right)\right],


$$

where

$$


r = |z|, \qquad \theta = \arg(z), \qquad k=0, 1, 2,..., n-1.


$$

In our case, we have

$$


r = 9, \qquad \theta = \dfrac{5\pi}{3}, \qquad n = 2.


$$

Substituting these values into the formula, we obtain

$$


\begin{aligned}𝑧_{1/2𝑘}^{} & =\sqrt{√9}cos⁡\frac{\frac{5𝜋}{3}+2𝜋𝑘}{3}+isin⁡\frac{\frac{5𝜋}{3}+2𝜋𝑘}{3} \\ & =3[cos⁡(\frac{5𝜋}{6}+𝜋⋅𝑘)+isin⁡(\frac{5𝜋}{6}+𝜋⋅𝑘)].\end{aligned}


$$

Therefore, $a = {\color{purple}3},$ $b = {\color{blue}6},$ and $c = {\color{red}\pi}.$

### Example: Finding the Square Roots of a Complex Number

#### Question

Find the square roots of $z=9\left[\cos\left(\dfrac{\pi}{5}\right)+\textrm{i}\sin\left(\dfrac{\pi}{5}\right)\right].$

#### Explanation

Any nonzero complex number $z$ has exactly $n$ distinct $n$th roots. Using de Moivre's theorem, we can write down these roots as

$$


z_{k}^{1/n} = \sqrt[n]{r}\left[\cos\left(\dfrac{\theta+2\pi{k}}{n}\right)+\textrm{i}\sin\left(\dfrac{\theta+2\pi{k}}{n}\right)\right],


$$

where

$$


r = |z|, \qquad \theta = \arg(z), \qquad k=0, 1, 2,..., n-1.


$$

In our case, we have

$$


r=9, \qquad \theta=\dfrac{\pi}{5}, \qquad n=2.


$$

Substituting these values into the formula, we obtain

$$


\begin{aligned}𝑧_{1/2𝑘}^{} & =\sqrt{√9}cos⁡\frac{\frac{𝜋}{5}+2𝜋⋅𝑘}{5}+isin⁡\frac{\frac{𝜋}{5}+2𝜋⋅𝑘}{5} \\ & =3[cos⁡(\frac{𝜋}{10}+𝜋⋅𝑘)+isin⁡(\frac{𝜋}{10}+𝜋⋅𝑘)].\end{aligned}


$$

Finally, setting $k=0, 1$ gives the square roots:

$$


\begin{aligned}𝑘=0:\,𝑧_{1/20}^{} & =3[cos⁡(\frac{𝜋}{10}+𝜋⋅0)+isin⁡(\frac{𝜋}{10}+𝜋⋅0)] \\ & =3[cos⁡(\frac{𝜋}{10})+isin⁡(\frac{𝜋}{10})] \\ 𝑘=1:\,𝑧_{1/21}^{} & =3[cos⁡(\frac{𝜋}{10}+𝜋⋅1)+isin⁡(\frac{𝜋}{10}+𝜋⋅1)] \\ & =3[cos⁡(\frac{11𝜋}{10})+isin⁡(\frac{11𝜋}{10})]\end{aligned}


$$

### De Moivre’s Theorem for Non-Integer Powers

Let's recall De Moivre's theorem:

$$


(\cos\theta + \textrm i \sin\theta)^n = \cos n\theta + \textrm i \sin n\theta


$$

De Moivre's theorem is *not* valid when $n$ is not an integer. This is because the left-hand side is multi-valued (since every complex number has multiple roots), while the right-hand side is single-valued.

However, De Moivre's theorem can be adapted to take these multiple values into account for non-integer $n$ as follows:

$$


(\cos\theta + \textrm i \sin\theta)^n = \cos\left( n(\theta+2\pi k)\right) + \textrm i \sin \left(n(\theta+2\pi k)\right)


$$

where $k$ is an integer. In this instance, each possible value of $z^n$ on the left-hand side corresponds to some value(s) of $k$ on the right-hand side. It's this idea that allows us to use De Moivre's theorem to compute the roots of complex numbers.
