# The Dot Product in N-Dimensional Euclidean Space

Source: https://www.mathacademy.com/topics/2094?courseId=155
Topic ID: 2094

## Prerequisites

- [Linear Combinations of Vectors in N-Dimensional Euclidean Space](../linear-algebra/1851-linear-combinations-of-vectors-in-n-dimensional-euclidean-space.md)

## Lesson

### Introduction

Recall that for two vectors $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n,$ the **dot product** is defined as the sum of products of corresponding components:

$$


\begin{aligned}𝐮⋅𝐯 & =\begin{matrix}𝑢_{1} \\ 𝑢_{2} \\ ⋮ \\ 𝑢_{𝑛}\end{matrix}⋅\begin{matrix}𝑣_{1} \\ 𝑣_{2} \\ ⋮ \\ 𝑣_{𝑛}\end{matrix} \\ & =𝑢_{1}⋅𝑣_{1}+𝑢_{2}⋅𝑣_{2}+⋯+𝑢_{𝑛}⋅𝑣_{𝑛} \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑛}}𝑢_{𝑖}𝑣_{𝑖}\end{aligned}


$$

### Properties of the Dot Product

To help us easily carry out computations involving dot products, it is helpful to know some dot product properties. Let $\mathbf{a}, \mathbf{b},$ and $\mathbf{c}$ be any vectors in $\mathbb{R}^n,$ and let $\alpha$ be a scalar in $\mathbb{R}.$ Then, we have the following properties:

- The dot product is **linear in the first variable**, meaning

- The dot product is **symmetric**, meaning

- The dot product is **positive-definite**, meaning and $\mathbf{a} \cdot \mathbf{a} = 0$ if and only if $\mathbf{a}=\mathbf{0}.$

**Warning**: We cannot compute the dot product of more than two vectors. If we have three vectors $\mathbf{a}, \mathbf{b}, \mathbf{c}$ then the expression $\mathbf{a}\cdot\mathbf{b}\cdot\mathbf{c}$ makes no sense. It makes no sense because $\mathbf{a}\cdot\mathbf{b}=k$ is a real number, whereas the dot product is only defined for two vectors, so we cannot compute the dot product $k\cdot\mathbf{c}$ of a real number and a vector.

The dot product is also **linear in the second variable**, meaning that

$$


\mathbf{c} \cdot (\mathbf{a} + \mathbf{b}) = \mathbf{c} \cdot \mathbf{a} + \mathbf{c} \cdot \mathbf{b} \qquad \text{and} \qquad \mathbf{a} \cdot (\beta\mathbf{b}) = \beta (\mathbf{a} \cdot \mathbf{b}).


$$

We can prove these two identities using linearity in the first variable and the fact that the dot product is symmetric, as follows:

$$


\begin{aligned}𝐜⋅(𝐚+𝐛) & =(𝐚+𝐛)⋅𝐜 \\ & =𝐚⋅𝐜+𝐛⋅𝐜 \\ & =𝐜⋅𝐚+𝐜⋅𝐛 \\ 𝐚⋅(𝛽𝐛) & =(𝛽𝐛)⋅𝐚 \\ & =𝛽(𝐛⋅𝐚) \\ & =𝛽(𝐚⋅𝐛)\end{aligned}


$$

So, we can say that the dot product is linear in both variables.

### Example: Calculating a Dot Product

#### Question

If $\begin{aligned}7 \\ 5 \\ −9 \\ 3\end{aligned}$ $\begin{aligned}1 \\ 2 \\ −5 \\ −2\end{aligned}$ and $\mathbf{v} \cdot \mathbf{v} = 34,$ then what is $\dfrac{\mathbf{u}\cdot 2\mathbf{v}}{3\mathbf{v}\cdot \mathbf{v}}?$

#### Explanation

We will use the fact that the dot product is linear.

To quickly compute the numerator $\mathbf{u} \cdot 2\mathbf{v},$ we compute $\mathbf{u} \cdot \mathbf{v}$ first and then multiply the result by $2.$ Doing this, we get

$$


\begin{aligned}𝐮⋅2𝐯 & =2(𝐮⋅𝐯) \\ & =2(𝑢_{1}⋅𝑣_{1}+𝑢_{2}⋅𝑣_{2}+𝑢_{3}⋅𝑣_{3}+𝑢_{4}⋅𝑣_{4}) \\ & =2(7⋅1+5⋅2+(−9)⋅(−5)+3⋅(−2)) \\ & =2(7+10+45−6) \\ & =2⋅56 \\ & =112.\end{aligned}


$$

To quickly compute the denominator $3\mathbf{v} \cdot \mathbf{v},$ we multiply $\mathbf{v} \cdot \mathbf{v}$ by $3.$ Doing this, we get

$$


\begin{aligned}3𝐯⋅𝐯 & =3(𝐯⋅𝐯) \\ & =3⋅34 \\ & =102.\end{aligned}


$$

Therefore,

$$


\dfrac{\mathbf{u}\cdot 2\mathbf{v}}{3\mathbf{v}\cdot\mathbf{v}} =\dfrac{112}{102}=\dfrac{56}{51}.


$$

### Example: Applying Properties of the Dot Product

#### Question

Find $(5\mathbf{a}+3\mathbf{b}) \cdot \mathbf{c}+(4\mathbf{b}+2\mathbf{c}) \cdot \mathbf{d},$ if $\mathbf{c} \cdot \mathbf{a} = 2,$ $\mathbf{b} \cdot \mathbf{c} = -1,$ $\mathbf{b} \cdot \mathbf{d} = 2,$ and $\mathbf{d} \cdot \mathbf{c}=3.$

#### Explanation

Using the fact that the dot product is linear in the first variable, we have

$$


\begin{aligned}(5𝐚+3𝐛)⋅𝐜+(4𝐛+2𝐜)⋅𝐝 & =(5𝐚)⋅𝐜+(3𝐛)⋅𝐜+(4𝐛)⋅𝐝+(2𝐜)⋅𝐝 \\ & =5(𝐚⋅𝐜)+3(𝐛⋅𝐜)+4(𝐛⋅𝐝)+2(𝐜⋅𝐝).\end{aligned}


$$

Next, we can substitute the values for $\mathbf{b} \cdot \mathbf{c}$ and $\mathbf{b} \cdot \mathbf{d},$ and use the fact that the dot product is symmetric to get

$$


\begin{aligned}5(𝐚⋅𝐜)+3(𝐛⋅𝐜)+4(𝐛⋅𝐝)+2(𝐜⋅𝐝) & =5(𝐜⋅𝐚)+3(−1)+4(2)+2(𝐝⋅𝐜) \\ & =5(𝐜⋅𝐚)−3+8+2(𝐝⋅𝐜) \\ & =5(𝐜⋅𝐚)+5+2(𝐝⋅𝐜).\end{aligned}


$$

Finally, substituting the values for $\mathbf{c} \cdot \mathbf{a}$ and $\mathbf{d} \cdot \mathbf{c},$ we find

$$


\begin{aligned}5(𝐜⋅𝐚)+5+2(𝐝⋅𝐜) & =5(2)+5+2(3) \\ & =10+5+6 \\ & =21.\end{aligned}


$$

Therefore, $(5\mathbf{a}+3\mathbf{b}) \cdot \mathbf{c}+(4\mathbf{b}+2\mathbf{c}) \cdot \mathbf{d} = 21.$

### Example: Identifying True Statements About the Dot Product

#### Question

Suppose $(4\mathbf{a} + 2\mathbf{b}) \cdot \mathbf{a} = {0},$ where $\mathbf{a} \neq \mathbf{0}.$ Which of the following statements are true?

1. $\mathbf{b} \cdot \mathbf{a} = -2(\mathbf{a} \cdot \mathbf{a})$

2. $\mathbf{a} \cdot \mathbf{a} = 0$

3. $\mathbf{b} \cdot \mathbf{a} = 1$

#### Explanation

Let's analyze each statement in turn.

- Statement I is true. Simplifying, we have

- Statement II is false. Since $\mathbf{a} \neq \mathbf{0},$ we must have $\mathbf{a} \cdot \mathbf{a} > 0.$

- Statement III is false since it leads to a contradiction. Simplifying $(4\mathbf{a} + 2\mathbf{b}) \cdot \mathbf{a} = {0}$ and substituting in $\mathbf{b} \cdot \mathbf{a} = 1,$ we get but this is a contradiction since $\mathbf{a} \neq \mathbf{0}$ implies that $\mathbf{a} \cdot \mathbf{a} > 0.$

Therefore, we conclude that the correct answer is "I only".
