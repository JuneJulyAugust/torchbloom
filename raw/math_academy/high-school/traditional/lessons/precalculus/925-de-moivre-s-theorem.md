# De Moivre's Theorem

Source: https://www.mathacademy.com/topics/925?courseId=43
Topic ID: 925

## Prerequisites

- [The Polar Form of a Complex Number](./894-the-polar-form-of-a-complex-number.md)
- [Describing Properties of the Sine Function](../algebra-ii/3540-describing-properties-of-the-sine-function.md)

## Lesson

### Introduction

**De Moivre's theorem** provides a simple way to compute powers of complex numbers in polar form. It states that

$$



\left[ \cos (\varphi) + \text{i}\sin(\varphi) \right]^n = \cos(n\varphi) + \text{i}\sin{(n\varphi)},



$$

where $n$ is an integer.

For example, let's use De Moivre's theorem to compute $\left[\cos (3\theta) +\text{i}\sin(3\theta) \right]^5.$ We get

$$



\begin{aligned}[cos⁡(3𝜃)+isin⁡(3𝜃)]^{5} & =cos⁡(5⋅3𝜃)+isin⁡(5⋅3𝜃) \\ & =cos⁡(15𝜃)+isin⁡(15𝜃).\end{aligned}



$$

### Example: Applying De Moivre's Theorem

#### Question

Simplify the expression $\left[\cos \left(\dfrac{\theta}{10} \right) + \text{i}\sin \left(\dfrac{\theta}{10}\right) \right]^4.$

#### Explanation

De Moivre's Theorem states that

$$



\left[ \cos(\varphi) + \text{i}\sin(\varphi) \right]^n = \cos(n\varphi) + \text{i}\sin{(n\varphi)}.



$$

In our expression, we have $n=4$ and $\varphi=\dfrac{\theta}{10}.$ Substituting in these values, we get

$$



\begin{aligned}[cos⁡(\frac{𝜃}{10})+isin⁡(\frac{𝜃}{10})]^{4} & =cos⁡(4⋅\frac{𝜃}{10})+isin⁡(4⋅\frac{𝜃}{10}) \\ & =cos⁡(\frac{2𝜃}{5})+isin⁡(\frac{2𝜃}{5}).\end{aligned}



$$

### Example: Applying De Moivre's Theorem to Fractions

#### Question

Simplify the expression $\dfrac{1}{\left[\cos (\theta) +\text{i}\sin(\theta) \right]^2}.$

#### Explanation

First, note that

$$



\dfrac{1}{\left[ \cos(\theta) +\text{i}\sin(\theta) \right]^2} = \left[ \cos(\theta) +\text{i}\sin(\theta) \right]^{-2} .



$$

De Moivre's Theorem states that

$$



\left[ \cos(\varphi) + \text{i}\sin(\varphi) \right]^n = \cos(n\varphi) + \text{i}\sin{(n\varphi)}.



$$

In our expression, we have $n=-2$ and $\varphi=\theta.$ Substituting in these values, we get

$$



\begin{aligned}\frac{1}{[cos⁡(𝜃)+isin⁡(𝜃)]^{2}} & =[cos⁡(𝜃)+isin⁡(𝜃)]^{−2} \\ & =cos⁡(−2𝜃)+isin⁡(−2𝜃).\end{aligned}



$$

Finally, using the fact that $\cos(-\varphi) = \cos (\varphi)$ and $\sin(-\varphi) = -\sin(\varphi)$ for any input $\varphi,$ we have

$$



\cos(-2\theta) + \text{i}\sin(-2\theta) = \cos(2\theta) - \text{i}\sin{(2\theta)}.



$$

### De Moivre's Theorem With a Negative Sine

We can also use De Moivre's theorem for an expression with a subtraction:

$$



\left[ \cos (\varphi) - \text{i}\sin(\varphi) \right]^n = \cos(n\varphi) - \text{i}\sin{(n\varphi)}.



$$

For example, with $n=5$ and $\varphi=3\theta,$ we have

$$



\begin{aligned}[cos⁡(3𝜃)−isin⁡(3𝜃)]^{5} & =cos⁡(5⋅3𝜃)−isin⁡(5⋅3𝜃) \\ & =cos⁡(15𝜃)−isin⁡(15𝜃).\end{aligned}



$$

To understand why we can also use De Moivre's theorem with subtraction, remember that $\cos\varphi = \cos(-\varphi)$ and $-\sin(\varphi) = \sin(-\varphi).$ Then, we have

$$



\begin{aligned}[cos⁡(𝜑)−isin⁡(𝜑)]^{𝑛} & =[cos⁡(−𝜑)+isin⁡(−𝜑)]^{𝑛} \\ & =cos⁡(−𝑛𝜑)+isin⁡(−𝑛𝜑) \\ & =cos⁡(𝑛𝜑)−isin⁡(𝑛𝜑).\end{aligned}



$$

### Example: Applying De Moivre's Theorem With a Negative Sine

#### Question

Simplify the expression $\dfrac{1}{\left[\cos (2\theta) -\text{i}\sin (2\theta) \right]^4}.$

#### Explanation

First, note that

$$



\begin{aligned}\frac{1}{[cos⁡(2𝜃)−isin⁡(2𝜃)]^{4}} & =[cos⁡(2𝜃)−isin⁡(2𝜃)]^{−4}.\end{aligned}



$$

For expressions involving subtraction, De Moivre's theorem states that

$$



\left[ \cos (\varphi) - \text{i}\sin(\varphi) \right]^n = \cos(n\varphi) - \text{i}\sin{(n\varphi)}.



$$

In our expression, we have $n=-4$ and $\varphi=2\theta.$ Substituting in these values, we get

$$



\begin{aligned}[cos⁡(2𝜃)−isin⁡(2𝜃)]^{−4} & =cos⁡(−4⋅2𝜃)−isin⁡(−4⋅2𝜃) \\ & =cos⁡(−8𝜃)−isin⁡(−8𝜃).\end{aligned}



$$

Finally, using the fact that $\cos(-\varphi) = \cos (\varphi)$ and $\sin(-\varphi) = -\sin(\varphi)$ for any input $\varphi,$ we have

$$



\begin{aligned}cos⁡(−8𝜃)−isin⁡(−8𝜃) & =cos⁡(8𝜃)−[−isin⁡(8𝜃)] \\ & =cos⁡(8𝜃)+isin⁡(8𝜃).\end{aligned}



$$
