# The CIS Notation

Source: https://www.mathacademy.com/topics/1236?courseId=101
Topic ID: 1236

## Prerequisites

- [Quotients of Complex Numbers Expressed in Polar Form](./1232-quotients-of-complex-numbers-expressed-in-polar-form.md)

## Lesson

### Introduction

The notation $\text{cis}\,\theta$ is a compact way of writing complex numbers given in polar form. Under this notation, the number $\text{cis}\,\theta$ corresponds to

$$


\text{cis}\,\theta = \cos\theta+ \text{i} \sin \theta.


$$

For example, consider the following complex number:

$$


z =\cos \left(\dfrac{\pi}{3}\right) + \text{i} \sin \left(\dfrac{\pi}{3} \right)


$$

Let's write this number using $\text{cis} \, \theta$ notation. Here, $\theta = \text{arg}\,(z)= \dfrac{\pi}{3}.$ Therefore, we get

$$


z = \text{cis} \left(\dfrac{\pi}{3}\right).


$$

Similarly, consider the complex number

$$


w = 5\left[\cos \left(\dfrac{5\pi}{6}\right) + \text{i} \sin \left(\dfrac{5\pi}{6} \right)\right].


$$

Let's write this number using $\text{cis} \, \theta$ notation as well. In this case, $\theta = \text{arg}\,(w)= \dfrac{5\pi}{6}.$ Therefore, we get

$$


w = 5\,\text{cis} \left(\dfrac{5\pi}{6}\right).


$$

### Example: Converting a Complex Number From CIS Notation to Cartesian Notation

#### Question

Express the complex number $4\,\text{cis}\left(\dfrac{\pi}{6}\right)$ in the form $a+\textrm i b.$

#### Explanation

The number $\text{cis}\,\theta$ corresponds to

$$


\text{cis}\,\theta = \cos \theta + \text{i}\sin \theta.


$$

Therefore, we get

$$


\begin{aligned}4\,cis(\frac{𝜋}{6}) & =4[cos⁡(\frac{𝜋}{6})+isin⁡(\frac{𝜋}{6})] \\ & =4[\frac{\sqrt{3}}{2}+i(\frac{1}{2})] \\ & =2\sqrt{3}+2i.\end{aligned}


$$

### Example: Expressing a Complex Number in CIS Notation

#### Question

Express $z=-\sqrt{3}+\text{i}$ using the $\text{cis}$ notation.

#### Explanation

Computing the magnitude $|z|,$ we get

$$


\begin{aligned}|𝑧| & =\sqrt{(−\sqrt{3})^{2}+1^{2}} \\ & =\sqrt{3+1} \\ & =\sqrt{4} \\ & =2.\end{aligned}


$$

Now, since $z$ lies in the second quadrant, we can find the argument $\text{arg}(z)$ as follows:

$$


\begin{aligned}arg⁡(𝑧) & =𝜋−arctan⁡\frac{𝑦}{𝑥} \\ & =𝜋−arctan⁡\frac{1}{−\sqrt{3}} \\ & =𝜋−arctan⁡(\frac{1}{\sqrt{3}}) \\ & =𝜋−\frac{𝜋}{6} \\ & =\frac{5𝜋}{6}\end{aligned}


$$

Therefore,

$$


z = -\sqrt{3}+\text{i}= 2\,\text{cis}\left(\dfrac{5\pi}{6}\right).


$$

### Computing Products of Complex Numbers Given In CIS Notation

Consider the following two complex numbers:

$$


z_1 = r_1\,\text{cis}\,\theta_1, \qquad z_2 = r_2\,\text{cis}\,\theta_2.


$$

To compute the product $z_1\cdot z_2,$ we compute the product of the moduli and add the arguments:

$$


z_1\cdot z_2 = r_1r_2\,\text{cis}\,(\theta_1+\theta_2).


$$

Let's get some practice doing this with concrete examples.

### Example: Evaluating a Product of Complex Numbers Expressed in CIS Notation

#### Question

If $z_1=5\text{cis}\left(\dfrac{5\pi}{6}\right)$ and $z_2=3\text{cis}\left(\dfrac{\pi}{3}\right),$ calculate the product $z_1z_2.$

#### Explanation

To compute the product of two complex numbers $z_1 = r_1\text{cis}\,\theta_1$ and $z_2 = r_2\text{cis}\,\theta_2,$ we use the formula

$$


z_1z_2 = r_1 r_2\,\text{cis}\left(\theta_1 + \theta_2\right).


$$

Substituting $r_1 = 5,$ $r_2 = 3,$ $\theta_1 = \dfrac{5\pi}{6},$ and $\theta_2 = \dfrac{\pi}{3},$ we get

$$


\begin{aligned}𝑧_{1}𝑧_{2} & =5⋅3⋅cis(\frac{5𝜋}{6}+\frac{𝜋}{3}) \\ & =15\,cis(\frac{7𝜋}{6}).\end{aligned}


$$

By expanding the $\text{cis}$ notation and evaluating the sine and cosine, we can get the expression in Cartesian form:

$$


\begin{aligned}𝑧_{1}𝑧_{2} & =15\,cis(\frac{7𝜋}{6}) \\ & =15\,[cos⁡(\frac{7𝜋}{6})+isin⁡(\frac{7𝜋}{6})] \\ & =15[−\frac{\sqrt{3}}{2}+i(−\frac{1}{2})] \\ & =−\frac{15}{2}(\sqrt{3}+i)\end{aligned}


$$

### Computing Quotients of Complex Numbers Given In CIS Notation

Consider the following two complex numbers:

$$


z_1 = r_1\,\text{cis}\,\theta_1, \qquad z_2 = r_2\,\text{cis}\,\theta_2.


$$

To compute the quotient $\dfrac{z_1}{z_2},$ we compute the quotient of the moduli and subtract the arguments:

$$


\dfrac{z_1}{z_2} = \dfrac{r_1}{r_2}\,\text{cis}\,(\theta_1-\theta_2).


$$

Let's get some practice doing this with concrete examples.

### Example: Evaluating a Quotient of Complex Numbers Expressed in CIS Notation

#### Question

If $z_1=3\text{cis}\left(\dfrac{3\pi}{4}\right)$ and $z_2=9\text{cis}\left(\dfrac{\pi}{2}\right),$ calculate the quotient $\dfrac{z_1}{z_2}.$

#### Explanation

To compute the quotient of two complex numbers $z_1 = r_1\text{cis}\,\theta_1$ and $z_2 = r_2\text{cis}\,\theta_2,$ we use the formula

$$


\dfrac{z_1}{z_2} = \dfrac{r_1}{r_2}\,\text{cis}\left(\theta_1 - \theta_2\right).


$$

Substituting $r_1 = 3,$ $r_2 = 9,$ $\theta_1 = \dfrac{3\pi}{4},$ and $\theta_2 = \dfrac{\pi}{2},$ we get

$$


\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}} & =\frac{3}{9}cis(\frac{3𝜋}{4}−\frac{𝜋}{2}) \\ & =\frac{1}{3}cis(\frac{𝜋}{4}).\end{aligned}


$$

By expanding the $\text{cis}$ notation and evaluating the sine and cosine, we can get the expression in Cartesian form:

$$


\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}} & =\frac{1}{3}cis(\frac{𝜋}{4}) \\ & =\frac{1}{3}\,[cos⁡(\frac{𝜋}{4})+isin⁡(\frac{𝜋}{4})] \\ & =\frac{1}{3}[\frac{\sqrt{2}}{2}+i\frac{\sqrt{2}}{2}] \\ & =\frac{1}{6}(\sqrt{2}+\sqrt{2}i)\end{aligned}


$$
