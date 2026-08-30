# Matrices Over the Complex Numbers

Source: https://www.mathacademy.com/topics/2015?courseId=55
Topic ID: 2015

## Prerequisites

- [Elementary Row Operations](./149-elementary-row-operations.md)
- [Multiplying Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1196-multiplying-matrices.md)
- [Vectors Over the Complex Numbers](./2703-vectors-over-the-complex-numbers.md)

## Lesson

### Matrices Over the Complex Numbers

It's possible to define matrices with complex entries, such as

$$


[\begin{aligned}−1+i & 4−i \\ 3+2i & 1\end{aligned}]


$$

In general, $\mathbb{C}^{m \times n}$ is the space of complex matrices with dimension $m \times n.$

Complex matrices work mostly the same as real matrices (we can add them, multiply them, etc). However, complex matrices have a few extra properties:

- We take the complex conjugate of a matrix by taking the complex conjugate of each component:

- Complex matrices also have a real part and an imaginary part. That means we can write any matrix in the form $A={\color{blue}B}+\text{i}\,{\color{red}C},$ where ${\color{blue}B} = {\color{blue}\text{Re}(A)}$ and ${\color{red}C} = {\color{red}\text{Im}(A)}.$ The real part of the matrix contains the real part of each entry, and the imaginary part of the matrix contains the imaginary part of each entry:

### Example: Calculating the Complex Conjugate of a Complex Matrix

#### Question

Find $B=\overline{A},$ where $\begin{aligned}4i & 3−i & 1+i \\ 2−2i & 2−i & 1+2i \\ i & 3i & 2i\end{aligned}$ What is the value of $b_{11} + b_{23}?$

#### Explanation

Taking the complex conjugate of each entry, we get

$$


\begin{aligned}\overset{𝐴}{} & =\overset{\begin{matrix}4i & 3−i & 1+i \\ 2−2i & 2−i & 1+2i \\ i & 3i & 2i\end{matrix}}{} \\ & =\begin{matrix}\overset{4i}{} & \overset{3−i}{} & \overset{1+i}{} \\ \overset{2−2i}{} & \overset{2−i}{} & \overset{1+2i}{} \\ \overset{i}{–} & \overset{3i}{} & \overset{2i}{}\end{matrix} \\ & =\begin{matrix}−4i & 3+i & 1−i \\ 2+2i & 2+i & 1−2i \\ −i & −3i & −2i\end{matrix}.\end{aligned}


$$

Therefore, $b_{11} + b_{23} = (-4\text{i}) + (1-2\text{i}) = 1-6\text{i}.$

### Example: Computing Components of the Real and Imaginary Parts of a Complex Matrix

#### Question

If $[\begin{aligned}𝑎 & 𝑏 \\ 𝑐 & 𝑑\end{aligned}]$ and $[\begin{aligned}𝑒 & 𝑓 \\ 𝑔 & ℎ\end{aligned}]$ are the real and imaginary parts of the matrix $[\begin{aligned}2−3i & −5−7i \\ 1−6i & 5−9i\end{aligned}]$ then what is the value of $ad+eh?$

#### Explanation

For the given matrix $A,$ we have that

$$


\begin{aligned}𝐴 & =[\begin{matrix}2−3i & −5−7i \\ 1−6i & 5−9i\end{matrix}] \\ & =\underset{Re(𝐴)}{\underset{}{[\begin{matrix}2 & −5 \\ 1 & 5\end{matrix}]}}+i\underset{Im(𝐴)}{\underset{}{[\begin{matrix}−3 & −7 \\ −6 & −9\end{matrix}]}}.\end{aligned}


$$

So we have $a=2,d=5,e=-3$ and $h=-9.$ Therefore,

$$


ad+eh=2 \cdot 5 + (-3) \cdot (-9) = 37.


$$

### Example: Multiplying Complex Matrices

#### Question

If $[\begin{aligned}−i & i \\ 1 & 2i\end{aligned}]$ and $[\begin{aligned}1+2i & 1−i \\ i & 2\end{aligned}]$, then what is $AB?$

#### Explanation

Multiplying the matrices using the usual method, we get

$$


\begin{aligned}𝐴𝐵 & =[\begin{matrix}−i & i \\ 1 & 2i\end{matrix}]⋅[\begin{matrix}1+2i & 1−i \\ i & 2\end{matrix}] \\ & =[\begin{matrix}(−i)⋅(1+2i)+i⋅i & (−i)⋅(1−i)+i⋅2 \\ 1⋅(1+2i)+2i⋅i & 1⋅(1−i)+2i⋅2\end{matrix}] \\ & =[\begin{matrix}(2−i)+(−1) & (−1−i)+2i \\ (1+2i)+(−2) & (1−i)+4i\end{matrix}] \\ & =[\begin{matrix}1−i & −1+i \\ −1+2i & 1+3i\end{matrix}].\end{aligned}


$$

### Example: Applying Row Operations to a Complex Matrix

#### Question

Given the matrix $[\begin{aligned}i & −i \\ 2+2i & 1\end{aligned}]$ find the result of applying to $A$ the following elementary row operations:

$$


R_1 := \dfrac{1}{\text{i}}R_1, \qquad R_2 := R_2 - 2\text{i}R_1


$$

#### Explanation

Let's apply the row operations to $A\mathbin{:}$

$$


\begin{aligned}𝐴 & =[\begin{matrix}i & −i \\ 2+2i & 1\end{matrix}]\, & & 𝑅_{1}:=\frac{1}{i}𝑅_{1} \\ & ∼[\begin{matrix}1 & −1 \\ 2+2i & 1\end{matrix}]\, & & 𝑅_{2}:=𝑅_{2}−2i𝑅_{1} \\ & ∼[\begin{matrix}1 & −1 \\ 2 & 1+2i\end{matrix}] & & \end{aligned}


$$

Therefore, the result is

$$


[\begin{aligned}1 & −1 \\ 2 & 1+2i\end{aligned}]


$$
