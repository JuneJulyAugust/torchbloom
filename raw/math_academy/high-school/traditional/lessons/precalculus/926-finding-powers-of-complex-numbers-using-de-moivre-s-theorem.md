# Finding Powers of Complex Numbers Using De Moivre's Theorem

Source: https://www.mathacademy.com/topics/926?courseId=43
Topic ID: 926

## Prerequisites

- [De Moivre's Theorem](./925-de-moivre-s-theorem.md)
- [The CIS Notation](./1236-the-cis-notation.md)

## Lesson

### Introduction

Remember that De Moivre's theorem provides a simple way to compute powers of complex numbers in polar form. It states that

$$



\left[ \cos(\theta) + \textrm{i}\sin(\theta) \right]^n = \cos(n\theta) + \textrm{i}\sin{(n\theta)}.



$$

For example, let's use De Moivre's theorem to calculate $(1+\sqrt{3}\,\textrm{i})^3.$

Let $z=1+\sqrt{3}\,\textrm{i}.$ First, we express $z$ in polar form. Computing the magnitude and argument, we get

$$



\begin{aligned}|𝑧| & =\sqrt{√1^{2}+(\sqrt{√3})^{2}}=2, \\ arg⁡(𝑧) & =arctan⁡(\frac{\sqrt{√3}}{1})=\frac{𝜋}{3}.\end{aligned}



$$

Now, we can write $z$ in polar form, as follows:

$$



z = 2\left[ \cos \left( \frac{\pi}{3} \right) + \textrm{i}\sin \left( \frac{\pi}{3}\right) \right]



$$

Finally, applying De Moivre's theorem, we get

$$



\begin{aligned}(1+\sqrt{√3}\,i)^{3} & =𝑧^{3} \\ & =[2[cos⁡(\frac{𝜋}{3})+isin⁡(\frac{𝜋}{3})]]^{3} \\ & =2^{3}[cos⁡(\frac{𝜋}{3})+isin⁡(\frac{𝜋}{3})]^{3} \\ & =8[cos⁡(3⋅\frac{𝜋}{3})+isin⁡(3⋅\frac{𝜋}{3})] \\ & =8[cos⁡(𝜋)+isin⁡(𝜋)] \\ & =8(−1+i⋅0) \\ & =−8.\end{aligned}



$$

### Example: Raising a Complex Number in Polar Form to a Power Using De Moivre’s Theorem

#### Question

Express $z$ in the form $x+\textrm{i}y,$ where

$$



z = \left[ \cos \left( \frac{\pi}{6} \right) +\textrm{i}\sin \left( \frac{\pi}{6}\right) \right]^5.



$$

#### Explanation

We use De Moivre's theorem,

$$



(\cos\theta + \textrm{i}\sin\theta)^n = \cos(n\theta) + \textrm{i}\sin{(n\theta)},



$$

with $n=5$ and $\theta = \dfrac{\pi}{6}.$ Therefore, we get

$$



\begin{aligned}𝑧 & =[cos⁡(\frac{𝜋}{6})+isin⁡(\frac{𝜋}{6})]^{5} \\ & =cos⁡(5⋅\frac{𝜋}{6})+isin⁡(5⋅\frac{𝜋}{6}) \\ & =cos⁡(\frac{5𝜋}{6})+isin⁡(\frac{5𝜋}{6}) \\ & =−\frac{\sqrt{√3}}{2}+\frac{1}{2}i.\end{aligned}



$$

### Example: Raising a Complex Number in Cartesian Form to a Power Using De Moivre's Theorem

#### Question

Use De Moivre's Theorem to express $(1+\textrm{i})^5$ in the form $x+\textrm{i}y.$

#### Explanation

Let $z=1+\textrm{i}.$ First, we express $z$ in polar form. Computing the magnitude and argument, we get

$$



\begin{aligned}|𝑧| & =\sqrt{√1^{2}+1^{2}}=2^{1/2}, \\ arg⁡(𝑧) & =arctan⁡(\frac{1}{1})=\frac{𝜋}{4}.\end{aligned}



$$

Now, we can write $z$ in polar form, as follows:

$$



z = 2^{1/2}\left[ \cos \left( \frac{\pi}{4} \right) +\textrm{i}\sin \left( \frac{\pi}{4} \right) \right]



$$

Finally, applying De Moivre's theorem, we get

$$



\begin{aligned}(1+i)^{5} & =𝑧^{5} \\ & =[2^{1/2}[cos⁡(\frac{𝜋}{4})+isin⁡(\frac{𝜋}{4})]]^{5} \\ & =(2^{1/2})^{5}[cos⁡(\frac{𝜋}{4})+isin⁡(\frac{𝜋}{4})]^{5} \\ & =2^{5/2}[cos⁡(\frac{5𝜋}{4})+isin⁡(\frac{5𝜋}{4})] \\ & =2^{5/2}(−\frac{\sqrt{√2}}{2}−\frac{\sqrt{√2}}{2}i) \\ & =2^{5/2}(−2^{−1/2}−2^{−1/2}i) \\ & =−2^{4/2}−2^{4/2}i \\ & =−2^{2}−2^{2}i \\ & =−4−4i.\end{aligned}



$$

### De Moivre's Theorem for Complex Numbers in CIS Notation

Remember that the $\textrm{cis}\left(\theta\right)$ notation is a compact notation for expressing complex numbers:

$$



\textrm{cis}\left(\theta\right) = \cos(\theta) + \textrm{i} \sin(\theta).



$$

We can write De Moivre's theorem in $\textrm{cis}\left(\theta\right)$ notation as follows:

$$



\begin{aligned}[cos⁡(𝜃)+isin⁡(𝜃)]^{𝑛} & =cos⁡(𝑛𝜃)+isin⁡(𝑛𝜃) \\ ⇓\,\,\,\,\, & \,\,\,\,⇓ \\ [cis(𝜃)]^{𝑛}\, & =\,\,\,cis(𝑛𝜃)\end{aligned}



$$

Therefore, to raise a complex number in the form $z=r\textrm{cis}\left(\theta\right)$ to the power of $n,$ we can use the identity

$$



\left[r\,\textrm{cis}\left(\theta\right)\right]^n = r^n\,\textrm{cis}\left(n\theta\right).



$$

### Example: Raising a Complex Number In CIS Notation to a Power Using De Moivre's Theorem

#### Question

Simplify $\left[3\,\textrm{cis}\left(\dfrac{\pi}{4}\right)\right]^3.$

#### Explanation

We use the identity

$$



\begin{aligned}[𝑟\,cis(𝜃)]^{𝑛} & =𝑟^{𝑛}\,cis(𝑛𝜃)\end{aligned}



$$

with $n=3,$ $r=3,$ and $\theta=\dfrac{\pi}{4}.$ Substituting in these values, we get

$$



\begin{aligned}[3\,cis(\frac{𝜋}{4})]^{3} & =3^{3}\,cis(3⋅\frac{𝜋}{4})=27\,cis(\frac{3𝜋}{4}).\end{aligned}



$$

Also, we know that $r\,\textrm{cis}(\theta) = r \left[\cos (\theta) +\textrm{i}\sin(\theta) \right].$ Therefore, we get

$$



\begin{aligned}27\,cis(\frac{3𝜋}{4}) & =27[cos⁡(\frac{3𝜋}{4})+isin⁡(\frac{3𝜋}{4})] \\ & =27(−\frac{\sqrt{√2}}{2}+i\frac{\sqrt{√2}}{2}) \\ & =−\frac{27\sqrt{√2}}{2}+\frac{27\sqrt{√2}}{2}i.\end{aligned}



$$
