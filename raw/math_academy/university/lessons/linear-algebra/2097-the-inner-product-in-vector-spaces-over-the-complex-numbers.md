# The Inner Product in Vector Spaces Over the Complex Numbers

Source: https://www.mathacademy.com/topics/2097?courseId=55
Topic ID: 2097

## Prerequisites

- [The Norm of a Vector in N-Dimensional Euclidean Space](./2095-the-norm-of-a-vector-in-n-dimensional-euclidean-space.md)
- [Inner Product Spaces](./2096-inner-product-spaces.md)

## Lesson

### Introduction

The standard inner product of $\Bbb R^n,$ i.e. the dot product, does not meet the criteria of an inner product on $\Bbb C^n.$

For example, if $\langle \,\cdot\,, \,\cdot\, \rangle$ is a valid inner product on $\Bbb C^n,$ then for any vector $\mathbf a \in \Bbb C^n,$ we must have

$$


\langle\mathbf a, \, \mathbf a\rangle \ge 0.


$$

But for many vectors in $\Bbb C^n,$ such as $[\begin{aligned}i \\ 0\end{aligned}]$ in $\Bbb C^2,$ the dot product fails to satisfy this criterion:

$$


\begin{aligned}[\begin{matrix}i \\ 0\end{matrix}]⋅[\begin{matrix}i \\ 0\end{matrix}] & =i^{2}+0^{2} \\ & =−1 \\ & <0\,×\end{aligned}


$$

Thankfully, there is an elegant way to generalize the dot product to satisfy the desired criterion on $\Bbb C^n.$ We can just take the complex conjugate of each element in the right vector before carrying out the dot product.

More formally, for two vectors $\mathbf x, \mathbf y\in \mathbb C^n$ given by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

we define the **standard Hermitian inner product** as

$$


\begin{aligned}⟨𝐱,𝐲⟩ & =𝑥_{1}⋅\overset{𝑦_{1}}{}+𝑥_{2}⋅\overset{𝑦_{2}}{}+⋯+𝑥_{𝑛}⋅\overset{𝑦_{𝑛}}{} \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑥_{𝑖}⋅\overset{𝑦_{𝑖}}{},\end{aligned}


$$

where $\overline{y_i}$ is the complex conjugate of $y_i.$

Using the standard Hermitian inner product instead of the dot product, our desired criterion is satisfied:

$$


\begin{aligned}⟨[\begin{matrix}i \\ 0\end{matrix}],[\begin{matrix}i \\ 0\end{matrix}]⟩ & =i⋅\overset{\,i\,}{}+0⋅\overset{\,0\,}{} \\ & =i⋅(−i)+0⋅0 \\ & =1+0 \\ & =1 \\ & ≥0\,✓\end{aligned}


$$

It can be verified that the Hermitian inner product satisfies *all* the criteria of an inner product on $\Bbb C^n.$

Furthermore, since the complex conjugate leaves real numbers unchanged, the Hermitian inner product simplifies to the dot product on $\Bbb R^n.$ In other words, the dot product is just a special case of the Hermitian inner product!

### Example: Computing the Inner Product of Two Complex Vectors

#### Question

Given that $\mathbf x, \mathbf y\in\mathbb C^3,$ compute the standard Hermitian inner product $\langle \mathbf{x}, \mathbf{y} \rangle$ of the following two vectors.

$$


\begin{aligned}i \\ −2 \\ 0\end{aligned}


$$

#### Explanation

Using the definition of the standard Hermitian inner product, we obtain

$$


\begin{aligned}⟨𝐱,𝐲⟩ & =𝑥_{1}\overset{𝑦_{1}}{}+𝑥_{2}\overset{𝑦_{2}}{}+𝑥_{3}\overset{𝑦_{3}}{} \\ & =i⋅(\overset{−3}{})+(−2)⋅\overset{4+i}{}+0⋅\overset{5}{–} \\ & =i⋅(−3)+(−2)⋅(4−i)+0 \\ & =−3i−8+2i \\ & =−8−i.\end{aligned}


$$

### Properties of the Inner Product Over the Complex Numbers

A Hermitian inner product over $\mathbb{C}$ satisfies the following properties:

- It is **linear in the first argument.** For any $\mathbf{a}, \mathbf{b}, \mathbf{c} \in \mathbb{C}^n$ and any $\alpha \in \mathbb{C},$ we have $\qquad$ $\langle \mathbf{a} + \mathbf{b}, \mathbf{c} \rangle = \langle \mathbf{a}, \mathbf{c} \rangle + \langle \mathbf{b}, \mathbf{c} \rangle \quad$ and $\quad \langle \alpha \mathbf{a}, \mathbf{b} \rangle = \alpha \langle \mathbf{a}, \mathbf{b} \rangle.$

- It is **antilinear in the second argument.** For any $\mathbf{a}, \mathbf{b}, \mathbf{c} \in \mathbb{C}^n$ and any $\alpha \in \mathbb{C},$ we have $\qquad$ $\langle \mathbf{a}, \mathbf{b} + \mathbf{c} \rangle = \langle \mathbf{a}, \mathbf{b} \rangle + \langle \mathbf{a}, \mathbf{c} \rangle \quad$ and $\quad \langle \mathbf{a}, \alpha\mathbf{b} \rangle = \overline{\alpha} \langle \mathbf{a}, \mathbf{b} \rangle.$

- It has **conjugate symmetry.** For any $\mathbf{a}, \mathbf{b} \in \mathbb{C}^n,$ we have $\qquad$ $\langle \mathbf{a}, \mathbf{b} \rangle = \overline{\langle \mathbf{b}, \mathbf{a} \rangle}.$

- It is **positive-definite.** For any $\mathbf{a}\in \mathbb{C}^n,$ we have $\qquad$ $\langle \mathbf{a}, \mathbf{a} \rangle$ is a non-negative real number, and $\langle \mathbf{a}, \mathbf{a} \rangle = 0$ if and only if $\mathbf{a} = \mathbf{0}.$

### Example: Identifying True Statements Regarding the Hermitian Inner Product

#### Question

Consider the standard Hermitian inner product $\langle \,\cdot\,, \,\cdot\, \rangle$ over $\mathbb{C}.$ Which of the following statements are true?

1. $\langle \mathbf{a}, \mathbf{b} \rangle\in\mathbb R$ for any $\mathbf{a}, \mathbf{b} \in \mathbb{C}^n$

2. $\langle \mathrm{i}\mathbf{a}, \mathbf{b} \rangle = \langle \mathbf{a}, -\mathrm{i} \mathbf{b} \rangle$ for any $\mathbf{a}, \mathbf{b} \in \mathbb{C}^n$

3. $\langle\mathrm{i} \mathbf{a},\mathrm{i} \mathbf{a} \rangle$ is a non-negative real number for any $\mathbf{a}\in \mathbb{C}^n$

#### Explanation

Recall that the standard Hermitian inner product over $\mathbb{C}$ satisfies the following properties:

- It is linear in the first argument. For any $\mathbf{a}, \mathbf{b}, \mathbf{c} \in \mathbb{C}^n$ and any $\alpha \in \mathbb{C},$ we have $\qquad$ $\langle \mathbf{a} + \mathbf{b}, \mathbf{c} \rangle = \langle \mathbf{a}, \mathbf{c} \rangle + \langle \mathbf{b}, \mathbf{c} \rangle \quad$ and $\quad \langle \alpha \mathbf{a}, \mathbf{b} \rangle = \alpha \langle \mathbf{a}, \mathbf{b} \rangle.$

- It is antilinear in the second argument. For any $\mathbf{a}, \mathbf{b}, \mathbf{c} \in \mathbb{C}^n$ and any $\alpha \in \mathbb{C},$ we have $\qquad$ $\langle \mathbf{a}, \mathbf{b} + \mathbf{c} \rangle = \langle \mathbf{a}, \mathbf{b} \rangle + \langle \mathbf{a}, \mathbf{c} \rangle \quad$ and $\quad \langle \mathbf{a}, \alpha\mathbf{b} \rangle = \overline{\alpha} \langle \mathbf{a}, \mathbf{b} \rangle.$

- It has conjugate symmetry. For any $\mathbf{a}, \mathbf{b} \in \mathbb{C}^n,$ we have $\qquad$ $\langle \mathbf{a}, \mathbf{b} \rangle = \overline{\langle \mathbf{b}, \mathbf{a} \rangle}.$

- It is positive-definite. For any $\mathbf{a}\in \mathbb{C}^n,$ we have $\qquad$ $\langle \mathbf{a}, \mathbf{a} \rangle$ is a non-negative real number, and $\langle \mathbf{a}, \mathbf{a} \rangle = 0$ if and only if $\mathbf{a} = \mathbf{0}.$

With that in mind, let's examine our statements.

- Statement I is false. The inner product over $\mathbb{C}$ is a complex number in general.

- Statement II is true. Indeed, by the linearity in the first argument and the antilinearity in the second argument, we have for any $\mathbf{a}, \mathbf{b} \in \mathbb{C}^n.$

- Statement III is true. Indeed, by the linearity in the first argument and the antilinearity in the second argument, we have for any $\mathbf{a}\in \mathbb{C}^n.$ But by positive-definiteness, this is a nonnegative real number.

Therefore, the correct answer is "II and III only."

### Example: Applying Properties of the Hermitian Inner Product

#### Question

Given that $\langle \,\cdot\,, \,\cdot\, \rangle$ is the standard Hermitian inner product over $\mathbb{C},$ find $\big\langle -2\mathbf{a}+3\mathbf{b}, \: \mathbf{c} \big\rangle$ if

$$


\langle \mathbf{a}, \mathbf{c} \rangle = 3+5\text{i}, \quad \quad \langle \mathbf{c}, \mathbf{b} \rangle = 2-4\text{i}.


$$

#### Explanation

Recall that the inner product over $\mathbb{C}$ satisfies the following properties.

- It is linear in the first argument. For any $\mathbf{a}, \mathbf{b}, \mathbf{c} \in \mathbb{C}^n$ and any $\alpha \in \mathbb{C},$ we have $\qquad$ $\langle \mathbf{a} + \mathbf{b}, \mathbf{c} \rangle = \langle \mathbf{a}, \mathbf{c} \rangle + \langle \mathbf{b}, \mathbf{c} \rangle \quad$ and $\quad \langle \alpha \mathbf{a}, \mathbf{b} \rangle = \alpha \langle \mathbf{a}, \mathbf{b} \rangle.$

- It is antilinear in the second argument. For any $\mathbf{a}, \mathbf{b}, \mathbf{c} \in \mathbb{C}^n$ and any $\alpha \in \mathbb{C},$ we have $\qquad$ $\langle \mathbf{a}, \mathbf{b} + \mathbf{c} \rangle = \langle \mathbf{a}, \mathbf{b} \rangle + \langle \mathbf{a}, \mathbf{c} \rangle \quad$ and $\quad \langle \mathbf{a}, \alpha\mathbf{b} \rangle = \overline{\alpha} \langle \mathbf{a}, \mathbf{b} \rangle.$

- It has conjugate symmetry. For any $\mathbf{a}, \mathbf{b} \in \mathbb{C}^n,$ we have $\qquad$ $\langle \mathbf{a}, \mathbf{b} \rangle = \overline{\langle \mathbf{b}, \mathbf{a} \rangle}.$

- It is positive-definite. For any $\mathbf{a}\in \mathbb{C}^n,$ we have $\qquad$ $\langle \mathbf{a}, \mathbf{a} \rangle$ is a non-negative real number, and $\langle \mathbf{a}, \mathbf{a} \rangle = 0$ if and only if $\mathbf{a} = \mathbf{0}.$

First, we use the fact that the inner product over $\mathbb{C}$ is linear in the first argument:

$$


\begin{aligned}⟨−2𝐚+3𝐛,\,𝐜⟩ & =⟨−2𝐚,𝐜⟩+⟨3𝐛,𝐜⟩ \\ & =−2⟨𝐚,𝐜⟩+3⟨𝐛,𝐜⟩\end{aligned}


$$

Next, we use the fact that the inner product over $\mathbb{C}$ has conjugate symmetry:

$$


\begin{aligned}−2⟨𝐚,𝐜⟩+3⟨𝐛,𝐜⟩ & =−2⟨𝐚,𝐜⟩+3\overset{⟨𝐜,𝐛⟩}{}\end{aligned}


$$

Finally, we substitute the values for $\langle \mathbf{a}, \mathbf{c} \rangle$ and $\langle \mathbf{c}, \mathbf{b} \rangle \mathbin{:}$

$$


\begin{aligned}−2⟨𝐚,𝐜⟩+3\overset{⟨𝐜,𝐛⟩}{} & =−2(3+5i)+3\overset{(2−4i)}{} \\ & =−2(3+5i)+3(2+4i) \\ & =−6−10i+6+12i \\ & =2i\end{aligned}


$$
