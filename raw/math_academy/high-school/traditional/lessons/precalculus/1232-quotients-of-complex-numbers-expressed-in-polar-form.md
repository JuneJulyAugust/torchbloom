# Quotients of Complex Numbers Expressed in Polar Form

Source: https://www.mathacademy.com/topics/1232?courseId=43
Topic ID: 1232

## Prerequisites

- [Products of Complex Numbers Expressed in Polar Form](./1231-products-of-complex-numbers-expressed-in-polar-form.md)

## Lesson

### Introduction

To compute the quotient of two complex numbers $z_1 = {\color{blue}r_1} \left[\cos({\color{blue}\theta_1}) + \text{i} \sin({\color{blue}\theta_1}) \right]$ and $z_2 = {\color{red}r_2} \left[\cos({\color{red}\theta_2}) + \text{i} \sin({\color{red}\theta_2}) \right]$ expressed in polar form, we can use the following formula:

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}}=\frac{𝑟_{1}}{𝑟_{2}}[cos⁡(𝜃_{1}−𝜃_{2})+isin⁡(𝜃_{1}−𝜃_{2})]\end{aligned}



$$

For example, let's use the above formula to compute the quotient of the following two complex numbers:

$$



\begin{aligned}𝑧_{1} & =4[cos⁡(\frac{2𝜋}{3})+isin⁡(\frac{2𝜋}{3})] \\ 𝑧_{2} & =2[cos⁡(\frac{𝜋}{3})+isin⁡(\frac{𝜋}{3})]\end{aligned}



$$

Here, we have ${\color{blue}r_1}={\color{blue}4},$ ${\color{red}r_2}={\color{red}2},$ ${\color{blue}\theta_1}={\color{blue}\dfrac{2\pi}{3}},$ and ${\color{red}\theta_2}={\color{red}\dfrac{\pi}{3}}.$ So, the formula gives

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}} & =\frac{4}{2}[cos⁡(\frac{2𝜋}{3}−\frac{𝜋}{3})+isin⁡(\frac{2𝜋}{3}−\frac{𝜋}{3})] \\ & =2[cos⁡(\frac{𝜋}{3})+isin⁡(\frac{𝜋}{3})].\end{aligned}



$$

By evaluating the sine and cosine, we can get the expression in Cartesian form:

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}} & =2[(\frac{1}{2})+i(\frac{\sqrt{3}}{2})] \\ & =1+\sqrt{3}\,i\end{aligned}



$$

**Note:** At the end of this lesson, we will show where the formula comes from. But for now, let's focus on using it.

### Example: Calculating the Quotient of Two Complex Numbers Expressed in Polar Form

#### Question

If $z_1=2\left[\cos \left(\dfrac{5\pi}{6} \right) +\text{i}\sin \left(\dfrac{5\pi}{6} \right) \right]$ and $z_2=4\left[\cos \left(\dfrac{\pi}{2} \right) +\text{i}\sin \left(\dfrac{\pi}{2} \right) \right],$ find the quotient $\dfrac{z_1}{z_2}.$

#### Explanation

To compute the quotient of two complex numbers, we use the formula

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}}=\frac{𝑟_{1}}{𝑟_{2}}[cos⁡(𝜃_{1}−𝜃_{2})+isin⁡(𝜃_{1}−𝜃_{2})].\end{aligned}



$$

Substituting in $r_1=2,$ $r_2=4,$ $\theta_1=\dfrac{5\pi}{6},$ and $\theta_2=\dfrac{\pi}{2},$ we get

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}} & =\frac{2}{4}[cos⁡(\frac{5𝜋}{6}−\frac{𝜋}{2})+isin⁡(\frac{5𝜋}{6}−\frac{𝜋}{2})] \\ & =\frac{1}{2}[cos⁡(\frac{𝜋}{3})+isin⁡(\frac{𝜋}{3})].\end{aligned}



$$

By evaluating the sine and cosine, we can get the expression in Cartesian form:

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}} & =\frac{1}{2}[\frac{1}{2}+i(\frac{\sqrt{3}}{2})] \\ & =\frac{1}{4}+\frac{\sqrt{3}}{4}i\end{aligned}



$$

### Example: Calculating the Quotient of Two Complex Numbers Expressed in Polar Form With Negative Angles

#### Question

Calculate the quotient $\dfrac{z_1}{z_2}$ given that $z_1=6\left[\cos \left(\dfrac{\pi}{12} \right) +\text{i}\sin \left(\dfrac{\pi}{12}\right) \right]$ and $z_2=4\left[\cos\left(-\dfrac{\pi}{6}\right)+\text{i}\sin\left(-\dfrac{\pi}{6}\right)\right].$

#### Explanation

To compute the quotient of two complex numbers, we use the formula

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}}=\frac{𝑟_{1}}{𝑟_{2}}[cos⁡(𝜃_{1}−𝜃_{2})+isin⁡(𝜃_{1}−𝜃_{2})].\end{aligned}



$$

Substituting in $r_1=6,$ $r_2=4,$ $\theta_1=\dfrac{\pi}{12},$ and $\theta_2=-\dfrac{\pi}{6},$ we get

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}} & =\frac{6}{4}[cos⁡(\frac{𝜋}{12}−(−\frac{𝜋}{6}))+isin⁡(\frac{𝜋}{12}−(−\frac{𝜋}{6}))] \\ & =\frac{3}{2}[cos⁡(\frac{𝜋}{4})+isin⁡(\frac{𝜋}{4})].\end{aligned}



$$

By evaluating the sine and cosine, we can get the expression in Cartesian form:

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}} & =\frac{3}{2}[\frac{\sqrt{2}}{2}+i(\frac{\sqrt{2}}{2})] \\ & =\frac{3\sqrt{2}}{4}+\frac{3\sqrt{2}}{4}i\end{aligned}



$$

### Justification for the Formula

To compute the quotient of two complex numbers $z_1 = r_1 \left[\cos(\theta_1) + \text{i} \sin(\theta_1) \right]$ and $z_2 = r_2 \left[\cos(\theta_2) + \text{i} \sin(\theta_2) \right]$ expressed in polar form, we have been using the following formula:

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}}=\frac{𝑟_{1}}{𝑟_{2}}[cos⁡(𝜃_{1}−𝜃_{2})+isin⁡(𝜃_{1}−𝜃_{2})].\end{aligned}



$$

To see why the formula works, let's compute the quotient manually:

$$



\begin{aligned}\frac{𝑧_{1}}{𝑧_{2}} & =\frac{𝑟_{1}[cos⁡(𝜃_{1})+isin⁡(𝜃_{1})]}{𝑟_{2}[cos⁡(𝜃_{2})+isin⁡(𝜃_{2})]} \\ & =\frac{𝑟_{1}}{𝑟_{2}}⋅\frac{cos⁡(𝜃_{1})+isin⁡(𝜃_{1})}{cos⁡(𝜃_{2})+isin⁡(𝜃_{2})}⋅\frac{cos⁡(𝜃_{2})−isin⁡(𝜃_{2})}{cos⁡(𝜃_{2})−isin⁡(𝜃_{2})} \\ & =\frac{𝑟_{1}}{𝑟_{2}}⋅\frac{\overset{[cos⁡(𝜃_{1})cos⁡(𝜃_{2})+sin⁡(𝜃_{1})sin⁡(𝜃_{2})]}{}}{cos⁡(𝜃_{1}−𝜃_{2})}+i\overset{[sin⁡(𝜃_{1})cos⁡(𝜃_{2})−cos⁡(𝜃_{1})sin⁡(𝜃_{2})]}{}}{sin⁡(𝜃_{1}−𝜃_{2})}}{cos^{2}⁡(𝜃_{2})+sin^{2}⁡(𝜃_{2})} \\ & =\frac{𝑟_{1}}{𝑟_{2}}⋅\frac{cos⁡(𝜃_{1}−𝜃_{2})+isin⁡(𝜃_{1}−𝜃_{2})}{1} \\ & =\frac{𝑟_{1}}{𝑟_{2}}[cos⁡(𝜃_{1}−𝜃_{2})+isin⁡(𝜃_{1}−𝜃_{2})]\end{aligned}



$$

So, this formula is a consequence of the difference formulas for cosine and sine!

By working out the product manually, we get the same result, but with a lot more effort and calculations. The formula is the quickest way to go.
