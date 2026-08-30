# Bilinear Forms

Source: https://www.mathacademy.com/topics/3121?courseId=55
Topic ID: 3121

## Prerequisites

- [The Transpose of a Matrix](../integrated-math-iii-honors/232-the-transpose-of-a-matrix.md)
- [Multiplying Matrices](../integrated-math-iii-honors/1196-multiplying-matrices.md)
- [Vectors in N-Dimensional Euclidean Space](./1849-vectors-in-n-dimensional-euclidean-space.md)
- [Sets and Functions](./3334-sets-and-functions.md)
- [Visualizing Cartesian Products](./4387-visualizing-cartesian-products.md)

## Lesson

### Introduction

Let $n$ be a positive integer. A function

$$


f: \Bbb R^n \to \Bbb R


$$

is a **linear form** (or *linear functional*) if there is a row-vector

$$


[\begin{aligned}𝑎_{1} & 𝑎_{2} & ⋯ & 𝑎_{𝑛}\end{aligned}]


$$

such that for any $\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}$ we have

$$


\begin{aligned}𝑓(𝐱) & =𝐚𝐱 \\ & =[\begin{aligned}𝑎_{1} & 𝑎_{2} & ⋯ & 𝑎_{𝑛}\end{aligned}]⋅\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned} \\ & =𝑎_{1}𝑥_{1}+𝑎_{2}𝑥_{2}+…+𝑎_{𝑛}𝑥_{𝑛}.\end{aligned}


$$

For example, let $f(\mathbf{x})$ be the linear form defined on $\Bbb R^2$ by $f(\mathbf{x}) = \mathbf{a} \mathbf{x},$ where $[\begin{aligned}3 & −2\end{aligned}]$

Suppose we want to evaluate $f(\mathbf{x})$ at $[\begin{aligned}\,1 \\ \,\,−1\end{aligned}]$ Then, we simply substitute $[\begin{aligned}\,1 \\ \,\,−1\end{aligned}]$ and obtain

$$


\begin{aligned}𝑓(𝐱) & =𝐚𝐱 \\ & =[\begin{aligned}3 & −2\end{aligned}]⋅[\begin{aligned}\,1 \\ \,\,−1\end{aligned}] \\ & =3⋅1+(−2)⋅(−1) \\ & =3+2 \\ & =5.\end{aligned}


$$

### Example: Evaluating a Linear Form

#### Question

The linear form $f(\mathbf{x})$ is defined as $f(\mathbf{x}) = \mathbf{a} \mathbf{x},$ where $[\begin{aligned}3 & 0 & 4\end{aligned}]$ Evaluate the function when $\begin{aligned}−5 \\ 8 \\ 5\end{aligned}$

#### Explanation

Substituting $\begin{aligned}−5 \\ 8 \\ 5\end{aligned}$ we obtain

$$


\begin{aligned}𝑓(𝐱) & =𝐚𝐱 \\ & =[\begin{aligned}3 & 0 & 4\end{aligned}]⋅\begin{aligned}−5 \\ 8 \\ 5\end{aligned} \\ & =3⋅(−5)+0⋅8+4⋅5 \\ & =−15+0+20 \\ & =5.\end{aligned}


$$

### Bilinear Forms

Let $n$ be a positive integer. A function $B: \Bbb R^n\times \Bbb R^n \to \Bbb R$ is said to be a **bilinear form** if there is an $n\times n$ matrix $A$ such that

$$


B(\mathbf{x}, \mathbf{y}) = \mathbf{x}^T \! A\mathbf{y}, \qquad \mathbf{x}, \mathbf{y} \in \Bbb R^n.


$$

Suppose, for example, that $[\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}]$ To evaluate the bilinear form $B(\mathbf{x},\mathbf{y}) = \mathbf{x}^T \! A \mathbf{y}$ when $[\begin{aligned}1 \\ 2\end{aligned}]$ and $[\begin{aligned}−1 \\ 1\end{aligned}]$ we substitute these vectors in the above expression as follows

$$


\begin{aligned}𝐵(𝐱,𝐲) & =𝐱^{𝑇}\,𝐴𝐲 \\ & =[\begin{aligned}1 & 2\end{aligned}][\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}][\begin{aligned}−1 \\ 1\end{aligned}] \\ & =[\begin{aligned}7 & 10\end{aligned}][\begin{aligned}−1 \\ 1\end{aligned}] \\ & =3.\end{aligned}


$$

To write down our bilinear form $B(\mathbf{x},\mathbf{y})$ above in terms of vector components

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

we proceed as follows:

$$


\begin{aligned}𝐵(𝐱,𝐲) & =𝐱^{𝑇}\,𝐴𝐲 \\ & =[\begin{aligned}𝑥_{1} & 𝑥_{2}\end{aligned}][\begin{aligned}1 & 2 \\ 3 & 4\end{aligned}][\begin{aligned}𝑦_{1} \\ 𝑦_{2}\end{aligned}] \\ & =[\begin{aligned}𝑥_{1} & 𝑥_{2}\end{aligned}][\begin{aligned}𝑦_{1}+2𝑦_{2} \\ 3𝑦_{1}+4𝑦_{2}\end{aligned}] \\ & =𝑥_{1}(𝑦_{1}+2𝑦_{2})+𝑥_{2}(3𝑦_{1}+4𝑦_{2}) \\ & =𝑥_{1}𝑦_{1}+2𝑥_{1}𝑦_{2}+3𝑥_{2}𝑦_{1}+4𝑥_{2}𝑦_{2}\end{aligned}


$$

### Example: Evaluating a Bilinear Form

#### Question

Consider the the bilinear form $B(\mathbf{x},\mathbf{y}),$ given by

$$


B(\mathbf{x},\mathbf{y})= 2 x_1y_2 - x_2y_2 +3 x_2y_3-x_3y_1


$$

Evaluate $B(\mathbf{x},\mathbf{y})$ when $\begin{aligned}1 \\ 1 \\ −1\end{aligned}$ and $\begin{aligned}−2 \\ 2 \\ 1\end{aligned}$

#### Explanation

We are given that

$\qquad$ $\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}$ and $\begin{aligned}𝑦_{1} \\ 𝑦_{2} \\ 𝑦_{3}\end{aligned}$

Substituting these into the bilinear expression, we obtain

$$


\begin{aligned}𝐵(𝐱,𝐲) & =2𝑥_{1}𝑦_{2}−𝑥_{2}𝑦_{2}+3𝑥_{2}𝑦_{3}−𝑥_{3}𝑦_{1} \\ & =2⋅1⋅2−1⋅2+3⋅1⋅1−(−1)⋅(−2) \\ & =4−2+3−2 \\ & =3.\end{aligned}


$$

### Example: Writing Down a Bilinear Form Given Its Matrix

#### Question

Consider the matrix above. Write down a bilinear form in terms of the components of and

#### Explanation

****

Each entry of corresponds to the term in the expression of the bilinear form:

****

To write down a bilinear form in terms of vector components, we compute the following expression:

### Example: Finding the Matrix of a Bilinear Form

#### Question

The matrix of the bilinear form $B(\mathbf{x},\mathbf{y}) = 2x_1y_1 + 2x_2y_1 - x_3 y_2+2x_3y_3$ is given below. What is the value of $a+b+c?$

$$


\begin{aligned}𝑎 & 0 & 0 \\ 𝑏 & 0 & 0 \\ 0 & 𝑐 & 2\end{aligned}


$$

#### Explanation

Each term $a_{ij}x_i y_j$ in the expression of the bilinear form corresponds to the entry $a_{ij}$ of the matrix:

$$


\begin{aligned}𝐵(𝐱,𝐲) & =2𝑥_{1}𝑦_{1}+2𝑥_{2}𝑦_{1}−𝑥_{3}𝑦_{2}+2𝑥_{3}𝑦_{3} \\ & =2𝑥_{1}𝑦_{1}+0𝑥_{1}𝑦_{2}+0𝑥_{1}𝑦_{3} \\ & +\,2𝑥_{2}𝑦_{1}+0𝑥_{2}𝑦_{2}+0𝑥_{2}𝑦_{3} \\ & +\,0𝑥_{3}𝑦_{1}+(−1)𝑥_{3}𝑦_{2}+2𝑥_{3}𝑦_{3}\end{aligned}


$$

Then, the corresponding matrix of the bilinear form is

$$


\begin{aligned}2 & 0 & 0 \\ 2 & 0 & 0 \\ 0 & \,\,−1 & 2\end{aligned}


$$

Therefore, $a=2,$ $b=2,$ and $c=-1.$ Finally,

$$


a+b+c=2+2+(-1) = 3.


$$

### Properties of Bilinear Forms

Suppose $A$ is an $n\times n$ matrix. Then, it readily follows that the function $B: \Bbb R^n\times \Bbb R^n \to \Bbb R$ defined as

$$


B(\mathbf{x}, \mathbf{y}) = \mathbf{x}^T \! A \, \mathbf{y}, \qquad \mathbf{x}, \mathbf{y} \in \Bbb R^n,


$$

is **linear in each argument** separately. That's the reason why we call them *bilinear*.

- For $\mathbf{y}$ fixed, all $\mathbf{u}, \mathbf{v} \in \Bbb R^n,$ and any real constant $c$, linearity in the first argument means the following:

$$


\begin{aligned}𝐵(𝐮+𝐯,𝐲) & =𝐵(𝐮,𝐲)+𝐵(𝐯,𝐲) \\ 𝐵(𝑐𝐮,𝐲) & =𝑐\,𝐵(𝐮,𝐲)\end{aligned}


$$

- For $\mathbf{x}$ fixed, all $\mathbf{w}, \mathbf{z} \in \Bbb R^n,$ and any real constant $c$, linearity in the second argument means the following:

$$


\begin{aligned}𝐵(𝐱,𝐰+𝐳) & =𝐵(𝐱,𝐰)+𝐵(𝐱,𝐳) \\ 𝐵(𝐱,𝑐𝐰) & =𝑐\,𝐵(𝐱,𝐰)\end{aligned}


$$
