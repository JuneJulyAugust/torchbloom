# Vectors Over the Complex Numbers

Source: https://www.mathacademy.com/topics/2703?courseId=55
Topic ID: 2703

## Prerequisites

- [Addition and Scalar Multiplication of Cartesian Vectors in 3D](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/175-addition-and-scalar-multiplication-of-cartesian-vectors-in-3d.md)
- [Dividing Complex Numbers](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/227-dividing-complex-numbers.md)

## Lesson

### Introduction

**Complex vectors** are vectors whose entries are *complex numbers*, such as

$$


[\begin{aligned}−1+i \\ 3+2i\end{aligned}]


$$

In general, $\mathbb{C}^n$ is the space of complex vectors with $n$ entries.

Complex vectors work mostly the same as real vectors (we can add them, multiply them by a scalar, etc). However, complex vectors have a few extra properties:

- We can take the complex conjugate of a vector by taking the complex conjugate of each component:

- Complex vectors have a real and imaginary part. This means that we can write a vector in the form $\mathbf{x} = \mathbf{\color{blue}a} + \text{i}\mathbf{\color{red}b},$ where ${\color{blue}\mathbf{a}} = {\color{blue}\text{Re}(\mathbf{x})}$ and ${\color{red}\mathbf{b}} = {\color{red}\text{Im}(\mathbf{x})}.$

The real part of the vector contains the real part of each entry, and the imaginary part of the vector contains the imaginary part of each entry:

$$


[\begin{aligned}−1+i \\ 3+2i\end{aligned}]


$$

### Example: Calculating the Complex Conjugate of a Complex Vector

#### Question

If $\begin{aligned}−2+5i \\ 5−9i \\ −7+8i\end{aligned}$ find $\,\overline{\mathbf{x}}.$

#### Explanation

To find the complex conjugate of a vector, we take the complex conjugate of the entries of the vector. So, we have

$$


\begin{aligned}\overset{𝐱}{} & =\overset{\begin{matrix}−2+5i \\ 5−9i \\ −7+8i\end{matrix}}{} \\ & =\begin{matrix}\overset{−2+5i}{} \\ \overset{5−9i}{} \\ \overset{−7+8i}{}\end{matrix} \\ & =\begin{matrix}−2−5i \\ 5+9i \\ −7−8i\end{matrix}.\end{aligned}


$$

### Example: Computing Components of the Real and Imaginary Parts of a Complex Vector

#### Question

If $[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]$ and $[\begin{aligned}𝑐 \\ 𝑑\end{aligned}]$ are the real and imaginary parts of the vector $[\begin{aligned}−3+7i \\ 5−2i\end{aligned}]$ what is the value of $ab+cd?$

#### Explanation

For the given vector $[\begin{aligned}−3+7i \\ 5−2i\end{aligned}]$ we have that

$$


\begin{aligned}𝐱 & =[\begin{matrix}−3+7i \\ 5−2i\end{matrix}] \\ & =\underset{Re(𝐱)}{\underset{}{[\begin{matrix}−3 \\ 5\end{matrix}]}}+i\,\underset{Im(𝐱)}{\underset{}{[\begin{matrix}7 \\ −2\end{matrix}]}}.\end{aligned}


$$

Therefore $a=-3, b=5, c=7$ and $d=-2,$ which implies that

$$


ab+cd=(-3) \cdot 5 + 7 \cdot (-2) = -29.


$$

### Properties of Vectors Over the Complex Numbers

The complex conjugate of vectors has a few useful properties:

- We can distribute the complex conjugate over individual vectors in a sum:

- We can distribute the complex conjugate over the scalar and the corresponding vector:

### Example: Finding the Real or Imaginary Part of a Scalar Given the Conjugate of a Scaled Vector

#### Question

Find $\text{Im}(k)$ given that $[\begin{aligned}−4i \\ 0\end{aligned}]$ and $[\begin{aligned}8i−12 \\ 0\end{aligned}]$

#### Explanation

Since $\overline{k\mathbf{v}} = \overline{k} \, \overline{\mathbf{v}},$ we get the following equation:

$$


\begin{aligned}\overset{𝑘𝐯}{} & =\overset{𝑘}{–}\,\overset{𝐯}{} \\ [\begin{matrix}8i−12 \\ 0\end{matrix}] & =\overset{𝑘}{–}\,\overset{[\begin{matrix}−4i \\ 0\end{matrix}]}{} \\ [\begin{matrix}8i−12 \\ 0\end{matrix}] & =\overset{𝑘}{–}\,[\begin{matrix}\overset{−4i}{} \\ \overset{0}{–}\end{matrix}] \\ [\begin{matrix}8i−12 \\ 0\end{matrix}] & =\overset{𝑘}{–}\,[\begin{matrix}4i \\ 0\end{matrix}] \\ [\begin{matrix}8i−12 \\ 0\end{matrix}] & =[\begin{matrix}4i\,\overset{𝑘}{–} \\ 0\end{matrix}]\end{aligned}


$$

So, we obtain that

$$


4\text{i}\,\overline{k} = 8\text{i}-12 \qquad\Longrightarrow\qquad \overline{k}=\dfrac{8\text{i}-12}{4\textrm i} = 2+3\text{i}.


$$

Therefore, $k=\overline{2+3\text{i}}=2-3\text{i}.$

Finally, $\text{Im}(k)=-3.$
