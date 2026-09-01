# The Hadamard Product

Source: https://www.mathacademy.com/topics/5916?courseId=145
Topic ID: 5916

## Prerequisites

- [The Transpose of a Matrix](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/232-the-transpose-of-a-matrix.md)
- [Multiplying Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1196-multiplying-matrices.md)

## Lesson

### Introduction

In some situations, we want to combine two matrices (or vectors) by multiplying them element-wise. This leads us to the **Hadamard product**.

If two matrices $A$ and $B$ have the same size, we can define a new matrix where each entry is the product of the corresponding entries in $A$ and $B$.

We write the Hadamard product using the symbol $\odot.$ Suppose we have two $n \times m$ matrices

$$


\begin{aligned}𝑎_{11} & 𝑎_{12} & ⋯ & 𝑎_{1𝑚} \\ 𝑎_{21} & 𝑎_{22} & ⋯ & 𝑎_{2𝑚} \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 𝑎_{𝑛1} & 𝑎_{𝑛2} & ⋯ & 𝑎_{𝑛𝑚}\end{aligned}


$$

Then, the Hadamard product $A \odot B$ is

$$


\begin{aligned}𝑎_{11}𝑏_{11} & 𝑎_{12}𝑏_{12} & ⋯ & 𝑎_{1𝑚}𝑏_{1𝑚} \\ 𝑎_{21}𝑏_{21} & 𝑎_{22}𝑏_{22} & ⋯ & 𝑎_{2𝑚}𝑏_{2𝑚} \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 𝑎_{𝑛1}𝑏_{𝑛1} & 𝑎_{𝑛2}𝑏_{𝑛2} & ⋯ & 𝑎_{𝑛𝑚}𝑏_{𝑛𝑚}\end{aligned}


$$

To see how the Hadamard product works in practice, let’s take two column vectors

$$


\begin{aligned}2 \\ −5 \\ 4\end{aligned}


$$

Their Hadamard product is the element-wise product of corresponding entries

$$


\begin{aligned}𝐴⊙𝐵 & =\begin{matrix}2 \\ −5 \\ 4\end{matrix}⊙\begin{matrix}−3 \\ 2 \\ 1\end{matrix} \\ & =\begin{matrix}2⋅(−3) \\ −5⋅2 \\ 4⋅1\end{matrix} \\ & =\begin{matrix}−6 \\ −10 \\ 4\end{matrix}.\end{aligned}


$$

Now, let's go through some examples.

### Example: Calculating the Hadamard Product of Vectors and Matrices

#### Question

$\begin{aligned}4 & 3 \\ 6 & 5 \\ 2 & 1\end{aligned}$

#### Explanation

The Hadamard product of two matrices (or vectors) $A$ and $B,$ denoted $A \odot B,$ is computed by multiplying corresponding entries together elementwise:

$$


(A \odot B)_{ij} = a_{ij}b_{ij}


$$

Therefore, in this case, we have

$$


\begin{aligned}\begin{matrix}4 & 3 \\ 6 & 5 \\ 2 & 1\end{matrix}⊙\begin{matrix}2 & 3 \\ −1 & 2 \\ 5 & −8\end{matrix} & =\begin{matrix}4⋅2 & 3⋅3 \\ 6⋅(−1) & 5⋅2 \\ 2⋅5 & 1⋅(−8)\end{matrix} \\ & =\begin{matrix}8 & 9 \\ −6 & 10 \\ 10 & −8\end{matrix}.\end{aligned}


$$

### Conformability for the Hadamard Product

Before we can compute the Hadamard product $A \odot B$, we need to make sure the two matrices have the same shape. If the shapes don’t match, the Hadamard product is undefined.

Suppose $P$ is a $3\times9$ matrix, $Q$ is a $9\times5$ matrix, and $R$ is a $3\times5$ matrix.

For example, consider the expression

$$


P \odot RQ^T


$$

Notice that the dimensions of $P$ are $3\times9,$ and the dimensions of $RQ^T$ are $3\times9.$ Hence, the Hadamard product is well-defined.

In contrast, in the expression

$$


PQ \odot R^T


$$

the dimensions of $PQ$ are $3\times5,$ and the dimensions of $R^T$ are $5\times3.$ Hence, the Hadamard product is *not* well-defined.

### The "Diag" Notation

Before we continue, note that the function $\text{diag}(\mathbf{v})$ is a **diagonal matrix** with the entries of the vector $\mathbf{v}\in\mathbb R^n$ on the diagonal:

$$


\begin{aligned}𝑣_{1} & 0 & ⋯ & 0 \\ 0 & 𝑣_{2} & ⋯ & 0 \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 0 & 0 & ⋯ & 𝑣_{𝑛}\end{aligned}


$$

Now, let's look at some concrete examples involving the Hadamard product.

### Example: Determining Whether a Matrix Expression Involving the Hadamard Product is Well-Defined

#### Question

Given the matrices

$$


\begin{aligned}3 & 6 \\ 1 & 1 \\ 5 & 3\end{aligned}


$$

in which of the following expressions is the Hadamard product well-defined?

1. $AB \odot BA$

2. $A\mathbf{v}^T \odot B^T \mathbf{v}^T$

3. $A^T \odot \,\text{diag}(\mathbf{v}) B$

#### Explanation

The Hadamard product of two matrices (or vectors) is only defined if they have the same dimensions.

First, notice that $A$ is a $3\times2$ matrix, $B$ is a $2\times3$ matrix, and $\mathbf{v}$ is a $1\times2$ row vector.

Now, let's consider each expression in turn:

- The dimensions of $AB$ are $3\times3,$ and the dimensions of $BA$ are $2\times2.$ Hence, the Hadamard product in expression I is ** well-defined.

- The dimensions of $A\mathbf{v}^T$ are $3\times1,$ and the dimensions of $B^T\mathbf{v}^T$ are $3\times1.$ Hence, the Hadamard product in expression II is well-defined.

- The dimensions of $A^T$ are $2\times3,$ and the dimensions of $\text{diag}(\mathbf{v}) B$ are $2\times3.$ Hence, the Hadamard product in expression III is well-defined.

Therefore, the correct answer is "II and III only".

### Properties of the Hadamard Product

Once we know how to compute the Hadamard product entry by entry, it’s helpful to understand how it behaves algebraically.

If $A, B, C \in \mathbb{R}^{n \times m}$ and $\alpha \in \mathbb{R}$, then the Hadamard product satisfies the following properties:

- **Commutativity** Element-wise multiplication doesn’t depend on order.

- **Associativity** We can group Hadamard products however we like.

- **Distributivity over Addition** This works just like normal multiplication, distributing over addition, but entry by entry.

- **Scalar Distributivity** Scaling before or after the Hadamard product gives the same result.

These properties make the Hadamard product easy to manipulate when working with elementwise operations.

Let's look at a concrete example.

Given that

$$


[\begin{aligned}1 & −2 \\ 0 & 4\end{aligned}]


$$

let's find $X \odot (Z^T + Y \odot Z).$

In this case, by distributing the Hadamard product over the addition, we have

$$


X \odot (Z^T + Y \odot Z) = X \odot Z^T + X \odot (Y \odot Z).


$$

Then, by the associativity of the Hadamard product, we get

$$


\begin{aligned}𝑋⊙𝑍^{𝑇}+𝑋⊙(𝑌⊙𝑍) & =𝑋⊙𝑍^{𝑇}+(𝑋⊙𝑌)⊙𝑍 \\ & =[\begin{matrix}1 & 3 \\ −1 & 0\end{matrix}]+[\begin{matrix}1 & −2 \\ 0 & 4\end{matrix}]⊙[\begin{matrix}1 & −1 \\ 3 & 0\end{matrix}] \\ & =[\begin{matrix}1 & 3 \\ −1 & 0\end{matrix}]+[\begin{matrix}1 & 2 \\ 0 & 0\end{matrix}] \\ & =[\begin{matrix}2 & 5 \\ −1 & 0\end{matrix}].\end{aligned}


$$

### Example: Applying the Properties of the Hadamard Product

#### Question

Given that

$$


[\begin{aligned}4 & 0 \\ −1 & 6\end{aligned}]


$$

find $P \odot Q - (\alpha P) \odot Q +R.$

#### Explanation

For compatible matrices $A,$ $B,$ and $C,$ and scalar $\alpha,$ the Hadamard product has the following properties:

- Commutativity:

- Associativity:

- Distributivity over Addition:

- Scalar Distributivity:

In this case, by the scalar distributivity of the Hadamard product, we have

$$


P \odot Q - (\alpha P) \odot Q +R = P \odot Q - \alpha( P \odot Q) +R.


$$

Then, by the commutativity of the Hadamard product, we have

$$


\begin{aligned}𝑃⊙𝑄−𝛼(𝑃⊙𝑄)+𝑅 & =𝑄⊙𝑃−𝛼(𝑄⊙𝑃)+𝑅 \\ & =[\begin{matrix}4 & 0 \\ −1 & 6\end{matrix}]−2[\begin{matrix}4 & 0 \\ −1 & 6\end{matrix}]+[\begin{matrix}−2 & 3 \\ −1 & −4\end{matrix}] \\ & =[\begin{matrix}4 & 0 \\ −1 & 6\end{matrix}]−[\begin{matrix}8 & 0 \\ −2 & 12\end{matrix}]+[\begin{matrix}−2 & 3 \\ −1 & −4\end{matrix}] \\ & =[\begin{matrix}4−8−2 & 0−0+3 \\ −1−(−2)−1 & 6−12−4\end{matrix}] \\ & =[\begin{matrix}−6 & 3 \\ 0 & −10\end{matrix}].\end{aligned}


$$

### Connections Between the Hadamard Product and Matrix Product

In machine learning and linear algebra, it’s often convenient to express the Hadamard product of two vectors using matrix multiplication. If $\mathbf{v}, \mathbf{u} \in \mathbb{R}^n$, then

$$


\mathbf{v} \odot \mathbf{u} = \text{diag}(\mathbf{v}) \mathbf{u} = \text{diag}(\mathbf{u}) \mathbf{v}.


$$

For example, given the matrix product

$$


[\begin{aligned}1 & 0 \\ 0 & 2\end{aligned}]


$$

we notice that the left matrix is diagonal. So, we can write it as a Hadamard product:

$$


\begin{aligned}[\begin{matrix}1 & 0 \\ 0 & 2\end{matrix}][\begin{matrix}−1 \\ 3\end{matrix}] & =diag([\begin{matrix}1 \\ 2\end{matrix}])[\begin{matrix}−1 \\ 3\end{matrix}] \\ & =[\begin{matrix}1 \\ 2\end{matrix}]⊙[\begin{matrix}−1 \\ 3\end{matrix}]\end{aligned}


$$

Now let's see a concrete example of expressing a Hadamard product as a matrix product in the next slide.

### Example: Converting Between the Hadamard Product and Matrix Product

#### Question

$$


[\begin{aligned}2 & −1 \\ 3 & 4\end{aligned}]


$$

Given the matrices above, write $M\mathbf{u}^T \odot (\mathbf{v} - \mathbf{u}^T)$ as a matrix product.

#### Explanation

The Hadamard product of two compatible vectors $\mathbf{a}$ and $\mathbf{b}$ can be expressed as the matrix product

$$


\mathbf{a} \odot \mathbf{b} = \text{diag}(\mathbf{a})\mathbf{b}.


$$

In our case, we have

$$


[\begin{aligned}2 & −1 \\ 3 & 4\end{aligned}]


$$

and

$$


[\begin{aligned}1 \\ 3\end{aligned}]


$$

Notice that they are of the same size; hence, their Hadamard product is well-defined. We conclude that

$$


\begin{aligned}𝑀𝐮^{𝑇}⊙(𝐯−𝐮^{𝑇}) & =diag(𝑀𝐮^{𝑇})(𝐯−𝐮^{𝑇}) \\ & =[\begin{matrix}−9 & 0 \\ 0 & 14\end{matrix}][\begin{matrix}3 \\ −2\end{matrix}].\end{aligned}


$$
