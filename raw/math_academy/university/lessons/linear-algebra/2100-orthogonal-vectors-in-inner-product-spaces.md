# Orthogonal Vectors in Inner Product Spaces

Source: https://www.mathacademy.com/topics/2100?courseId=55
Topic ID: 2100

## Prerequisites

- [Integrating Logarithmic Functions Using Substitution](../../../ap-courses/lessons/ap-calculus-ab/1161-integrating-logarithmic-functions-using-substitution.md)
- [Inner Product Spaces](./2096-inner-product-spaces.md)
- [Orthogonal Vectors in Euclidean Spaces](./2099-orthogonal-vectors-in-euclidean-spaces.md)

## Lesson

### Introduction

Let $\mathbf{x}$ and $\mathbf{y}$ be vectors in a vector space $V$ equipped with an inner product $\langle \cdot, \cdot \rangle.$

Two vectors $\mathbf{x}$ and $\mathbf{y}$ are **orthogonal with respect to the inner product** $\langle \cdot, \cdot \rangle$ in $V$ if their inner product is zero:

$$


\langle \mathbf{x} , \mathbf{y} \rangle = 0


$$

If the two vectors are orthogonal, then we denote this by $\mathbf{x} \perp \mathbf{y}.$ For instance, the vectors

$$


\begin{aligned}1 \\ 1 \\ 0\end{aligned}


$$

in $\mathbb{R}^3$ equipped with the inner product

$$


\langle \mathbf{x} , \mathbf{y} \rangle = x_1y_1 + 2x_2y_2 + x_3y_3


$$

are orthogonal, since

$$


\begin{aligned}⟨𝐱,𝐲⟩ & =1⋅2+2⋅(1⋅(−1))+0⋅3 \\ & =2−2+0 \\ & =0.\end{aligned}


$$

**Note:** The zero vector $\mathbf{0}$ in a vector space $V$ equipped with an inner product $\langle \cdot, \cdot \rangle$ is orthogonal to any vector $\mathbf{x} \in V$ since $\langle \mathbf{0}, \mathbf{x} \rangle = 0.$

### Example: Determining Components of Orthogonal Vectors in Inner Product Spaces

#### Question

Let $V = \mathbb{R}^3$ be the vector space equipped with the inner product

$$


\langle \mathbf{x}, \mathbf{y} \rangle = 3 x_1 y_1 + x_2 y_2 + 2 x_3 y_3.


$$

Given that $\begin{aligned}2 \\ 1 \\ 2\end{aligned}$ and $\begin{aligned}𝑘 \\ −2 \\ −1\end{aligned}$ are orthogonal with respect to the inner product $\langle \cdot, \cdot \rangle$ in $V,$ find the value of $k.$

#### Explanation

Since $\mathbf x$ and $\mathbf y$ are orthogonal, their inner product must be zero.

First, we compute the inner product using our definition:

$$


\begin{aligned}⟨𝐱,𝐲⟩ & =3𝑥_{1}𝑦_{1}+𝑥_{2}𝑦_{2}+2𝑥_{3}𝑦_{3} \\ & =3⋅(2⋅𝑘)+1⋅(−2)+2⋅(2⋅(−1)) \\ & =6𝑘−2−4 \\ & =6𝑘−6\end{aligned}


$$

Now, we set $\langle \mathbf{x}, \mathbf{y} \rangle = 0$ and solve for $k\mathbin{:}$

$$


\begin{aligned}⟨𝐱,𝐲⟩ & =0 \\ 6𝑘−6 & =0 \\ 6𝑘 & =6 \\ 𝑘 & =1\end{aligned}


$$

### Example: Determining Components of Orthogonal Vectors in Inner Product Spaces of Polynomials

#### Question

Let $V=\mathbb{R}_2[t]$ be the vector space of all polynomials of degree at most $2,$ equipped with the inner product

$$


\langle {x(t)}, {y(t)} \rangle = x(0)y(0) + x(1)y(1) + x(-1)y(-1).


$$

Given that $p(t) = 1 + t + t^2$ and $q(t) = kt - t^2$ are orthogonal with respect to the inner product $\langle \cdot, \cdot \rangle$ in $V,$ find the value of $k.$

#### Explanation

Since $p(t)$ and $q(t)$ are orthogonal, their inner product must be zero.

First, we compute the inner product using our definition:

$$


\begin{aligned}⟨𝑝(𝑡),𝑞(𝑡)⟩ & =𝑝(0)𝑞(0)+𝑝(1)𝑞(1)+𝑝(−1)𝑞(−1) \\ & =(1)(0)+(3)(𝑘−1)+(1)(−𝑘−1) \\ & =0+(3𝑘−3)+(−𝑘−1) \\ & =2𝑘−4\end{aligned}


$$

Now, we set $\langle p(t), q(t) \rangle = 0$ and solve for $k\mathbin{:}$

$$


\begin{aligned}⟨𝑝(𝑡),𝑞(𝑡)⟩ & =0 \\ 2𝑘−4 & =0 \\ 2𝑘 & =4 \\ 𝑘 & =2\end{aligned}


$$

### Example: Determining Components of Orthogonal Vectors in Inner Product Spaces of Continuous Functions

#### Question

Let $V=\mathcal{C}\left[0,1\right]$ be the vector space of all functions that are continuous on $\left[0,1\right],$ equipped with the inner product

$$


\langle x(t),y(t) \rangle = \displaystyle\int_{0}^{1} x(t) y(t) \, \text{d}t.


$$

Given that $x(t) = kt^2+3t$ and $y(t) = t$ are orthogonal with respect to the inner product $\langle \cdot, \cdot \rangle$ in $V,$ find the value of $k.$

#### Explanation

Since $x(t)$ and $y(t)$ are orthogonal, their inner product must be zero.

First, we compute the inner product using our definition:

$$


\begin{aligned}⟨𝑥(𝑡),𝑦(𝑡)⟩ & =∫_{10}𝑥(𝑡)𝑦(𝑡)\,d𝑡 \\ & =∫_{10}(𝑘𝑡^{2}+3𝑡)(𝑡)\,d𝑡 \\ & =∫_{10}(𝑘𝑡^{3}+3𝑡^{2})\,d𝑡 \\ & =(\frac{𝑘𝑡^{4}}{4}+𝑡^{3})_{10} \\ & =\frac{𝑘}{4}+1.\end{aligned}


$$

Now, we set $\langle x(t), y(t) \rangle = 0$ and solve for $k\mathbin{:}$

$$


\begin{aligned}⟨𝑥(𝑡),𝑦(𝑡)⟩ & =0 \\ \frac{𝑘}{4}+1 & =0 \\ \frac{𝑘}{4} & =−1 \\ 𝑘 & =−4\end{aligned}


$$

### Example: Identifying True Statements About Orthogonal Vectors in Inner Product Spaces

#### Question

Let $V=\mathcal{C}\left[0,2\pi\right]$ be the vector space of all functions that are continuous on $\left[0,2\pi\right],$ equipped with the inner product

$$


\langle f(t),g(t) \rangle = \displaystyle\int_{0}^{2\pi} f(t) g(t) \, \text{d}t.


$$

Given the functions $f(t) = \cos t$ and $g(t)=\sin 2t,$ which of the following statements are true?

1. $\langle f(t), g(t) \rangle = 0$

2. $\langle f(t), g(t) \rangle = \dfrac{\pi}{2}$

3. $f(t) \perp g(t)$ with respect to the inner product $\langle \cdot, \cdot \rangle$ in $V$

** $\sin\alpha\cos\beta=\dfrac12(\sin(\alpha-\beta)+\sin(\alpha+\beta)).$

#### Explanation

We need to evaluate

$$


\langle f(t), g(t) \rangle = \int_{0}^{2\pi}\cos{t} \sin2t \,\text{d}t.


$$

We can evaluate this integral using the given identity, as follows:

$$


\begin{aligned}∫_{2𝜋0}sin⁡2𝑡\,cos⁡𝑡\,d𝑡 & =\frac{1}{2}∫_{2𝜋0}(sin⁡(2𝑡−𝑡)+sin⁡(2𝑡+𝑡))\,d𝑡 \\ & =\frac{1}{2}∫_{2𝜋0}(sin⁡𝑡+sin⁡3𝑡)\,d𝑡 \\ & =\frac{1}{2}(−cos⁡𝑡−\frac{cos⁡3𝑡}{3})_{2𝜋0} \\ & =\frac{1}{2}[−cos⁡(2𝜋)−\frac{cos⁡(6𝜋)}{3}]−\frac{1}{2}[−cos⁡0−\frac{cos⁡0}{3}] \\ & =\frac{1}{2}[−1−\frac{1}{3}]−\frac{1}{2}[−1−\frac{1}{3}] \\ & =\frac{1}{2}⋅(−\frac{4}{3})−\frac{1}{2}⋅(−\frac{4}{3}) \\ & =−\frac{2}{3}+\frac{2}{3} \\ & =0\end{aligned}


$$

Let's now examine the statements:

- Statement I is true, while statement II is false.

- Statement III is true. Since the inner product is zero, our vectors are orthogonal.

Therefore, the correct answer is "I and III only."
