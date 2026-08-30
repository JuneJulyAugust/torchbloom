# Vectors Over the Complex Numbers

Source: https://www.mathacademy.com/topics/2703?courseId=154
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

- Complex vectors have a real and imaginary part. This means that we can write a vector in the form $\mathbf{x} = \mathbf{\color{blue}a} + \textrm{i}\mathbf{\color{red}b},$ where ${\color{blue}\mathbf{a}} = {\color{blue}\textrm{Re}(\mathbf{x})}$ and ${\color{red}\mathbf{b}} = {\color{red}\textrm{Im}(\mathbf{x})}.$

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


\begin{aligned}\overset{𝐱}{} & =\overset\begin{aligned}−2+5i \\ 5−9i \\ −7+8i\end{aligned}}{} \\ & =\begin{aligned}\overset{−2+5i}{} \\ \overset{5−9i}{} \\ \overset{−7+8i}{}\end{aligned} \\ & =\begin{aligned}−2−5i \\ 5+9i \\ −7−8i\end{aligned}.\end{aligned}


$$

### Example: Computing Components of the Real and Imaginary Parts of a Complex Vector

#### Question

If $[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]$ and $[\begin{aligned}𝑐 \\ 𝑑\end{aligned}]$ are the real and imaginary parts of the vector $[\begin{aligned}−3+7i \\ 5−2i\end{aligned}]$ what is the value of $ab+cd?$

#### Explanation

For the given vector $[\begin{aligned}−3+7i \\ 5−2i\end{aligned}]$ we have that

$$


\begin{aligned}𝐱 & =[\begin{aligned}−3+7i \\ 5−2i\end{aligned}] \\ & =\underset{Re(𝐱)}{\underset{}{[\begin{aligned}−3 \\ 5\end{aligned}]}}+i\,\underset{Im(𝐱)}{\underset{}{[\begin{aligned}7 \\ −2\end{aligned}]}}.\end{aligned}


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

Find $\textrm{Im}(k)$ given that $[\begin{aligned}−4i \\ 0\end{aligned}]$ and $[\begin{aligned}8i−12 \\ 0\end{aligned}]$

#### Explanation

Since $\overline{k\mathbf{v}} = \overline{k} \, \overline{\mathbf{v}},$ we get the following equation:

$$


\begin{aligned}\overset{𝑘𝐯}{} & =\overset{𝑘}{–}\,\overset{𝐯}{} \\ [\begin{aligned}8i−12 \\ 0\end{aligned}] & =\overset{𝑘}{–}\,\overset{[\begin{aligned}−4i \\ 0\end{aligned}]}{} \\ [\begin{aligned}8i−12 \\ 0\end{aligned}] & =\overset{𝑘}{–}\,[\begin{aligned}\overset{−4i}{} \\ \overset{0}{–}\end{aligned}] \\ [\begin{aligned}8i−12 \\ 0\end{aligned}] & =\overset{𝑘}{–}\,[\begin{aligned}4i \\ 0\end{aligned}] \\ [\begin{aligned}8i−12 \\ 0\end{aligned}] & =[\begin{aligned}4i\,\overset{𝑘}{–} \\ 0\end{aligned}]\end{aligned}


$$

So, we obtain that

$$


4\textrm{i}\,\overline{k} = 8\textrm{i}-12 \qquad\Longrightarrow\qquad \overline{k}=\dfrac{8\textrm{i}-12}{4\textrm i} = 2+3\textrm{i}.


$$

Therefore, $k=\overline{2+3\textrm{i}}=2-3\textrm{i}.$

Finally, $\textrm{Im}(k)=-3.$
