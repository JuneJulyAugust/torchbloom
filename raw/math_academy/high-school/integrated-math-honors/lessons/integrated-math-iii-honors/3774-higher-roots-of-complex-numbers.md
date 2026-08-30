# Higher Roots of Complex Numbers

Source: https://www.mathacademy.com/topics/3774?courseId=101
Topic ID: 3774

## Prerequisites

- [Square Roots of Complex Numbers](./1234-square-roots-of-complex-numbers.md)

## Lesson

### Introduction

Any complex number $z$ can be written in polar form as

$$


z = r\left(\cos\theta+\textrm i\sin\theta\right)


$$

where

$$


r = |z|, \qquad \theta = \arg(z).


$$

Recall that the $n$th roots of $z$ are given by

$$


z_{k}^{1/n} = \sqrt[n]{r}\left[\cos\left(\dfrac{\theta + 2\pi{k}}{n}\right) + \textrm{i}\sin\left(\dfrac{\theta + 2\pi{k}}{n}\right)\right], \qquad k=0, 1, 2,..., n-1.


$$

We've seen how to compute the square roots of complex numbers. In this lesson, we'll apply the same method to compute higher roots.

### Example: Finding a Formula for the Roots of a Number With Unit Magnitude

#### Question

The complex $6$th roots of the number $z=\cos\left(\dfrac{3\pi}{2}\right)+\textrm{i}\sin\left(\dfrac{3\pi}{2}\right)$ are given by

$$


z_k^{1/6} = \cos\left(\dfrac{\pi}{\boxed{a}}+\boxed{b}\cdot{k}\right)+\textrm{i}\sin\left(\dfrac{\pi}{\boxed{a}}+\boxed{b}\cdot{k}\right),


$$

where $k=0,\,1,\,2,\,3,\,4,\,5.$ What are the values of $a$ and $b?$

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


r=1, \qquad \theta=\dfrac{3\pi}{2}, \qquad n=6.


$$

Substituting these values into the formula, we obtain

$$


\begin{aligned}𝑧_{1/6𝑘}^{} & =\sqrt[√1]{6}cos⁡\frac{\frac{3𝜋}{2}+2𝜋𝑘}{2}+isin⁡\frac{\frac{3𝜋}{2}+2𝜋𝑘}{2} \\ & =cos⁡(\frac{𝜋}{4}+\frac{𝜋}{3}⋅𝑘)+isin⁡(\frac{𝜋}{4}+\frac{𝜋}{3}⋅𝑘).\end{aligned}


$$

Therefore, $a={\color{blue}4}$ and $b={\color{red}\dfrac{\pi}{3}}.$

### Example: Finding a Formula for the Roots of a Number

#### Question

The complex $4$th roots of the number $z=256\left[\cos\left(\dfrac{\pi}{2}\right)+\textrm{i}\sin\left(\dfrac{\pi}{2}\right)\right]$ are given by

$$


z_k^{1/4} = \boxed{a} \left[ \cos\left(\dfrac{\pi}{\boxed{b}}+\boxed{c}\cdot{k}\right)+ \textrm{i} \sin\left(\dfrac{\pi}{\boxed{b}}+\boxed{c}\cdot{k}\right) \right],


$$

where $k=0,\,1,\,2,\,3.$ What are the values of $a,$ $b,$ and $c?$

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


r=256, \qquad \theta=\dfrac{\pi}{2}, \qquad n=4.


$$

Substituting these values into the formula, we obtain

$$


\begin{aligned}𝑧_{1/4𝑘}^{} & =\sqrt[√256]{4}cos⁡\frac{\frac{𝜋}{2}+2𝜋𝑘}{2}+isin⁡\frac{\frac{𝜋}{2}+2𝜋𝑘}{2} \\ & =4[cos⁡(\frac{𝜋}{8}+\frac{𝜋}{2}⋅𝑘)+isin⁡(\frac{𝜋}{8}+\frac{𝜋}{2}⋅𝑘)].\end{aligned}


$$

Therefore, $a={\color{purple}4},$ $b={\color{blue}8},$ and $c={\color{red}\dfrac{\pi}{2}}.$

### Example: Finding the Roots of a Complex Number

#### Question

The fourth roots of the number $z=\cos\left(\dfrac{\pi}{3}\right)+\textrm{i}\sin\left(\dfrac{\pi}{3}\right)$ are as follows:

$$


\begin{aligned}𝑧_{1/40}^{}=cos⁡𝜙_{0}+isin⁡𝜙_{0} \\ 𝑧_{1/41}^{}=cos⁡𝜙_{1}+isin⁡𝜙_{1} \\ 𝑧_{1/42}^{}=cos⁡𝜙_{2}+isin⁡𝜙_{2} \\ 𝑧_{1/43}^{}=cos⁡𝜙_{3}+isin⁡𝜙_{3}\end{aligned}


$$

Find possible values of $\phi_0,$ $\phi_1,\phi_2$ and $\phi_3.$

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


r=1, \qquad \theta=\dfrac{\pi}{3}, \qquad n=4.


$$

Substituting these values into the formula, we obtain

$$


\begin{aligned}𝑧_{1/4𝑘}^{} & =\sqrt[√1]{3}cos⁡\frac{\frac{𝜋}{3}+2𝜋⋅𝑘}{3}+isin⁡\frac{\frac{𝜋}{3}+2𝜋⋅𝑘}{3} \\ & =[cos⁡(\frac{𝜋}{12}+\frac{2𝜋⋅𝑘}{4})+isin⁡(\frac{𝜋}{12}+\frac{2𝜋⋅𝑘}{4})] \\ & =[cos⁡(\frac{𝜋}{12}+\frac{𝜋⋅𝑘}{2})+isin⁡(\frac{𝜋}{12}+\frac{𝜋⋅𝑘}{2})].\end{aligned}


$$

Finally, setting $k=0, 1, 2,3$ gives the required roots:

$$


\begin{aligned}𝑘=0:\,𝑧_{1/40}^{} & =[cos⁡(\frac{𝜋}{12}+\frac{𝜋⋅0}{2})+isin⁡(\frac{𝜋}{12}+\frac{𝜋⋅0}{2})] \\ & =cos⁡(\frac{𝜋}{12})+isin⁡(\frac{𝜋}{12}) \\ 𝑘=1:\,𝑧_{1/41}^{} & =[cos⁡(\frac{𝜋}{12}+\frac{𝜋⋅1}{2})+isin⁡(\frac{𝜋}{12}+\frac{𝜋⋅1}{2})] \\ & =cos⁡(\frac{7𝜋}{12})+isin⁡(\frac{7𝜋}{12}) \\ 𝑘=2:\,𝑧_{1/42}^{} & =[cos⁡(\frac{𝜋}{12}+\frac{𝜋⋅2}{2})+isin⁡(\frac{𝜋}{12}+\frac{𝜋⋅2}{2})] \\ & =cos⁡(\frac{13𝜋}{12})+isin⁡(\frac{13𝜋}{12}) \\ 𝑘=3:\,𝑧_{1/43}^{} & =[cos⁡(\frac{𝜋}{12}+\frac{𝜋⋅3}{2})+isin⁡(\frac{𝜋}{12}+\frac{𝜋⋅3}{2})] \\ & =cos⁡(\frac{19𝜋}{12})+isin⁡(\frac{19𝜋}{12})\end{aligned}


$$

Therefore,

$$


\phi_0 = \dfrac{\pi}{12}, \qquad \phi_1 = \dfrac{7\pi}{12}, \qquad \phi_2 = \dfrac{13\pi}{12}\qquad \phi_3 = \dfrac{19\pi}{12}.


$$
