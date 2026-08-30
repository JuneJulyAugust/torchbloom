# Special Properties of the Complex Conjugate

Source: https://www.mathacademy.com/topics/905?courseId=136
Topic ID: 905

## Prerequisites

- [Multiplying Complex Numbers](../../../high-school/traditional/lessons/algebra-ii/33-multiplying-complex-numbers.md)
- [The Complex Conjugate](./892-the-complex-conjugate.md)

## Lesson

### Introduction

When we add a complex number and its conjugate, the result is always twice the real part of the complex number. That is to say,

$$


z + \overline{z} = 2\operatorname{Re}(z),


$$

where $\operatorname{Re}(z)$ is the real part of $z.$

For example, suppose we have a complex number $z = 3+4\text{i}.$ To obtain the conjugate, we just flip the sign of the imaginary part and get $\overline{z} = 3 - 4 \text{i}.$

Now, adding $z$ and its conjugate $\overline{z},$ we find that the real part $(3)$ is doubled while the imaginary part $(4)$ is canceled out:

$$


\begin{aligned}𝑧+\overset{𝑧}{–} & =(3+4i)+(3−4i) \\ & =(3+3)+(4i−4i) \\ & =6+0i \\ & =6\end{aligned}


$$

This result holds in general. For any complex number $z=x+\text{i}y,$ the conjugate is $\overline{z} = x-\text{i}y,$ and when we add, we find that the real part $(x)$ is doubled while the imaginary part $(y)$ is canceled out:

$$


\begin{aligned}𝑧+\overset{𝑧}{–} & =(𝑥+i𝑦)+(𝑥−i𝑦) \\ & =(𝑥+𝑥)+(i𝑦−i𝑦) \\ & =2𝑥+i0 \\ & =2𝑥 \\ & =2Re(𝑧).\end{aligned}


$$

### Example: Calculating the Sum of a Complex Number and Its Conjugate

#### Question

If $z=7-3\text{i}$, calculate $z+\overline{z}.$

#### Explanation

**

When we add a complex number and its conjugate, the result is always twice the real part of the complex number.

For the given complex number $z=7-3\text{i},$ the real part is $\operatorname{Re}(z) = 7,$ so we have

$$


\begin{aligned}𝑧+\overset{𝑧}{–} & =2Re(𝑧) \\ & =2(7) \\ & =14.\end{aligned}


$$

**

Alternatively, we can actually carry out the process of adding the complex number and its conjugate.

To obtain the conjugate of the complex number $z=7-3\text{i},$ we flip the sign of the imaginary part and get $\overline{z} = 7 + 3 \text{i}.$

Adding, we get

$$


\begin{aligned}𝑧+\overset{𝑧}{–} & =(7−3i)+(7+3i) \\ & =(7+7)+(−3i+3i) \\ & =14+i0 \\ & =14.\end{aligned}


$$

### Calculating the Product of a Complex Number and its Conjugate

When we multiply a complex number and its conjugate, the result is always the sum of squares of the real part and the imaginary part. That is to say,

$$


z\overline{z} = x^2 + y^2 = (\operatorname{Re}(z))^2 + (\operatorname{Im}(z))^2.


$$

For example, suppose we have a complex number $z=3+4\text{i}.$ To obtain the conjugate, we just flip the sign of the imaginary part and get $\overline{z} = 3 - 4 \text{i}.$

Now, multiplying $z$ and its conjugate $\overline{z},$ we find that the result is the sum of squares of the real part $(3^2=9)$ and the imaginary part $(4^2=16)\mathbin{:}$

$$


\begin{aligned}𝑧\overset{𝑧}{–} & =(3+4i)(3−4i) \\ & =3^{2}−3(4i)+3(4i)−4^{2}i^{2} \\ & =9−12i+12i−16(−1) \\ & =9+16 \\ & =25\end{aligned}


$$

This result holds in general. For any complex number $z=x+\text{i}y,$ the conjugate is $\overline{z} = x-\text{i}y,$ and when we multiply, we find that the result is the sum of squares of the real part $(x^2)$ and the imaginary part $(y^2)\mathbin{:}$

$$


\begin{aligned}𝑧\overset{𝑧}{–} & =(𝑥+i𝑦)(𝑥−i𝑦) \\ & =𝑥^{2}−i𝑥𝑦+i𝑥𝑦−i^{2}𝑦^{2} \\ & =𝑥^{2}−(−1)𝑦^{2} \\ & =𝑥^{2}+𝑦^{2} \\ & =(Re(𝑧))^{2}+(Im(𝑧))^{2}\end{aligned}


$$

### Example: Calculating the Product of a Complex Number and Its Conjugate

#### Question

Given that $z=7-4\text{i},$ calculate $z\overline{z}.$

#### Explanation

**

When we multiply a complex number and its conjugate, the result is always the sum of squares of the real part and the imaginary part.

For the given complex number $z=7-4\text{i},$ the real part is $\text{Re}(z)=7,$ and the imaginary part is $\text{Im}(z)=-4,$ so we have

$$


\begin{aligned}𝑧\overset{𝑧}{–} & =(Re(𝑧))^{2}+(Im(𝑧))^{2} \\ & =7^{2}+(−4)^{2} \\ & =49+16 \\ & =65.\end{aligned}


$$

**

Alternatively, we can actually carry out the process of multiplying the complex number and its conjugate.

To obtain the conjugate of the complex number $z=7-4\text{i},$ we flip the sign of the imaginary part and get $\overline{z} = 7 + 4 \text{i}.$

Multiplying, we get

$$


\begin{aligned}𝑧\overset{𝑧}{–} & =(7−4i)(7+4i) \\ & =7^{2}+(7)(4)i+(−4)(7)i−(4)^{2}i^{2} \\ & =49+28i−28i−(16)(−1) \\ & =49+16 \\ & =65.\end{aligned}


$$

### Some Other Properties of the Complex Conjugate

The complex conjugate has a few other useful properties. These are used less often, but it's worth being aware of them.

- We can distribute the complex conjugate over individual terms.

- The conjugate of a square is equal to the square of a conjugate:

- If $z$ is a complex number and $a$ is a real number, then
