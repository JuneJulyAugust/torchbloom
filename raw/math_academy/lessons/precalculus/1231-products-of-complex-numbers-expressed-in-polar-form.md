# Products of Complex Numbers Expressed in Polar Form

Source: https://www.mathacademy.com/topics/1231?courseId=43
Topic ID: 1231

## Prerequisites

- [The Sum and Difference Formulas for Sine](./270-the-sum-and-difference-formulas-for-sine.md)
- [The Sum and Difference Formulas for Cosine](./274-the-sum-and-difference-formulas-for-cosine.md)
- [The Polar Form of a Complex Number](./894-the-polar-form-of-a-complex-number.md)

## Lesson

### Introduction

Consider the following complex numbers $z_1$ and $z_2$ expressed in polar form:

$$



\begin{aligned}𝑧_{1} & =𝑟_{1}(cos⁡𝜃_{1}+isin⁡𝜃_{1}) \\ 𝑧_{2} & =𝑟_{2}(cos⁡𝜃_{2}+isin⁡𝜃_{2})\end{aligned}



$$

To compute the product $z_1\cdot z_2,$ we can use the following formula:

$$



z_1z_2 = r_1 r_2\left( \cos(\theta_1+\theta_2) + \textrm{i} \sin(\theta_1+\theta_2)\right)



$$

For example, let's use this formula to compute the product of the following two complex numbers:

$$



\begin{aligned}𝑧_{1} & =2[cos⁡(\frac{𝜋}{3})+isin⁡(\frac{𝜋}{3})] \\ 𝑧_{2} & =3[cos⁡(\frac{2𝜋}{3})+isin⁡(\frac{2𝜋}{3})]\end{aligned}



$$

Here, we have ${\color{black}r_1}={\color{black}2},$ ${\color{black}r_2}={\color{black}3},$ ${\color{black}\theta_1}={\color{black}\dfrac{\pi}{3}},$ and ${\color{black}\theta_2}={\color{black}\dfrac{2\pi}{3}}.$

Applying the formula, we get

$$



\begin{aligned}𝑧_{1}𝑧_{2} & =2⋅3[cos⁡(\frac{𝜋}{3}+\frac{2𝜋}{3})+isin⁡(\frac{𝜋}{3}+\frac{2𝜋}{3})] \\ & =6(cos⁡𝜋+isin⁡𝜋).\end{aligned}



$$

This is the final answer expressed on polar form. However, by evaluating the sine and cosine, we can get the expression in Cartesian form:

$$



\begin{aligned}𝑧_{1}𝑧_{2} & =6(cos⁡𝜋+isin⁡𝜋) \\ & =6((−1)+i(0)) \\ & =−6\end{aligned}



$$

So, we conclude that $z_1\cdot z_2 = -6.$

At the end of this lesson, we will show where the formula comes from. But for now, let's focus on using it.

### Example: Calculating the Product of Two Complex Numbers Expressed in Polar Form

#### Question

If $z_1=2\left[\cos \left(\dfrac{\pi}{2} \right) +\textrm{i}\sin \left(\dfrac{\pi}{2}\right) \right]$ and $z_2=4\left[\cos \left(\dfrac{5\pi}{6} \right) +\textrm{i}\sin \left(\dfrac{5\pi}{6}\right) \right],$ calculate the product $z_1z_2.$

#### Explanation

To compute the product of two complex numbers, we use the formula

$$



\begin{aligned} z_1z_2=r_1r_2[\cos(\theta_1+\theta_2)+\textrm{i}\sin(\theta_1+\theta_2)]. \end{aligned}



$$

Substituting in $r_1=2,$ $r_2 =4,$ $\theta_1=\dfrac{\pi}{2},$ and $\theta_2=\dfrac{5\pi}{6},$ we get

$$



\begin{aligned} z_1z_2&=2\cdot 4\left[\cos\left(\dfrac{\pi}{2}+\dfrac{5\pi}{6}\right)+\textrm{i}\sin\left(\dfrac{\pi}{2}+\dfrac{5\pi}{6}\right)\right]\\\[5pt] &=8\left[ \cos \left( \dfrac{4\pi}{3} \right) + \textrm{i} \sin \left( \dfrac{4\pi}{3} \right) \right] . \end{aligned}



$$

By evaluating the sine and cosine, we can get the expression in Cartesian form:

$$



\begin{aligned}𝑧_{1}𝑧_{2} & =8[(−\frac{1}{2})+i(−\frac{\sqrt{√3}}{2})] \\ & =−4−4\sqrt{√3}\,i\end{aligned}



$$

### Example: Calculating the Product of Two Complex Numbers With Negative Arguments

#### Question

If $z_1=2\left[\cos\left(-\dfrac{\pi}{6}\right)+\textrm{i}\sin\left(-\dfrac{\pi}{6}\right)\right]$ and $z_2=6\left[\cos \left(\dfrac{2\pi}{3} \right) +\textrm{i}\sin \left(\dfrac{2\pi}{3}\right) \right],$ find the the product $z_1z_2.$

#### Explanation

To compute the product of two complex numbers, we use the formula

$$



\begin{aligned} z_1z_2=r_1r_2[\cos(\theta_1+\theta_2)+\textrm{i}\sin(\theta_1+\theta_2)]. \end{aligned}



$$

Substituting in $r_1=2,$ $r_2 =6,$ $\theta_1=-\dfrac{\pi}{6},$ and $\theta_2=\dfrac{2\pi}{3},$ we get

$$



\begin{aligned} z_1z_2&=12\left[\cos\left(-\dfrac{\pi}{6}+\dfrac{2\pi}{3}\right)+\textrm{i}\sin\left(-\dfrac{\pi}{6}+\dfrac{2\pi}{3}\right)\right]\\\[5pt] &=12\left[\cos\left(\dfrac{\pi}{2}\right)+\textrm{i}\sin\left(\dfrac{\pi}{2}\right)\right]. \end{aligned}



$$

By evaluating the sine and cosine, we can get the expression in Cartesian form:

$$



\begin{aligned}𝑧_{1}𝑧_{2} & =12[(0)+i(1)] \\ & =12i\end{aligned}



$$

### Justification of the Formula

To compute the product of the complex numbers

$$



\begin{aligned}𝑧_{1} & =𝑟_{1}(cos⁡𝜃_{1}+isin⁡𝜃_{1}) \\ 𝑧_{2} & =𝑟_{2}(cos⁡𝜃_{2}+isin⁡𝜃_{2}),\end{aligned}



$$

we have been using the formula

$$



z_1z_2 = r_1 r_2\left( \cos(\theta_1+\theta_2) + \textrm{i} \sin(\theta_1+\theta_2)\right).



$$

To see why the formula works, let's compute the product manually:

$$



\begin{aligned}𝑧_{1}𝑧_{2} & =𝑟_{1}(cos⁡𝜃_{1}+isin⁡𝜃_{1})⋅𝑟_{2}(cos⁡𝜃_{2}+isin⁡𝜃_{2}) \\ & =𝑟_{1}𝑟_{2}(cos⁡𝜃_{1}+isin⁡𝜃_{1})(cos⁡𝜃_{2}+isin⁡𝜃_{2}) \\ & =𝑟_{1}𝑟_{2}[(cos⁡𝜃_{1}cos⁡𝜃_{2}−sin⁡𝜃_{1}sin⁡𝜃_{2})+i(sin⁡𝜃_{1}cos⁡𝜃_{2}+cos⁡𝜃_{1}sin⁡𝜃_{2})]\end{aligned}



$$

We now recall the addition formulas for cosine and sine:

$$



\begin{aligned}cos⁡(𝜃_{1}+𝜃_{2}) & =cos⁡𝜃_{1}cos⁡𝜃_{2}−sin⁡𝜃_{1}sin⁡𝜃_{2} \\ sin⁡(𝜃_{1}+𝜃_{2}) & =sin⁡𝜃_{1}cos⁡𝜃_{2}+cos⁡𝜃_{1}sin⁡𝜃_{2}\end{aligned}



$$

Substituting the above into our expression for $z_1z_2,$ we finally arrive at

$$



z_1z_2 = r_1 r_2\left( \cos(\theta_1+\theta_2) + \textrm{i} \sin(\theta_1+\theta_2)\right).



$$
