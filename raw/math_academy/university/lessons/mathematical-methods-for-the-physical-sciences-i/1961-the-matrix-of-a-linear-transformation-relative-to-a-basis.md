# The Matrix of a Linear Transformation Relative to a Basis

Source: https://www.mathacademy.com/topics/1961?courseId=154
Topic ID: 1961

## Prerequisites

- [Expressing the Coordinates of a Vector in a Given Basis](./1864-expressing-the-coordinates-of-a-vector-in-a-given-basis.md)
- [The Standard Matrix of a Linear Transformation in Terms of the Standard Basis](./2211-the-standard-matrix-of-a-linear-transformation-in-terms-of-the-standard-basis.md)

## Lesson

### Introduction

What is the matrix of the linear transformation

$$


[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]


$$

relative to the basis

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

In other words, what is the matrix $[T]_{\mathcal{B}}$ such that

$$


[\mathbf{T}(\mathbf{x})]_{\mathcal{B}} = [T]_{\mathcal{B}} \cdot[\mathbf{x}]_{\mathcal{B}}?


$$

In fact, the answer is the matrix whose columns are the coordinates of the images of the basis vectors $\mathbf{b}_1, \mathbf{b}_2$ under the transformation relative to the basis:

$$


\begin{aligned}| & | \\ [𝑇(𝐛_{1})]_{B} & [𝑇(𝐛_{2})]_{B} \\ | & |\end{aligned}


$$

This matrix is called the **matrix for $\mathbf{T}$ relative to $\mathcal{B}$** or the **$\mathcal{B}$-matrix for $\mathbf{T}.$**

As a result, for the transformation $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$, with respect to the basis

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

we have

$$


[\begin{aligned}7 \\ −2\end{aligned}]


$$

Now, to write ${\color{red} \mathbf{T} \left(\mathbf{b}_1 \right)}$ and ${\color{blue} \mathbf{T} \left(\mathbf{b}_2 \right)}$ with respect to our basis $\mathcal{B},$ we assume that

$$


[\begin{aligned}𝛼_{1} \\ 𝛼_{2}\end{aligned}]


$$

where the components $\alpha_1,$ $\alpha_2,$ $\beta_1,$ and $\beta_2$ satisfy

$$


{\color{red}\alpha_1} \mathbf{b}_1+{\color{red}\alpha_2}\mathbf{b}_2 = {\color{red} \mathbf{T} \left( \mathbf{b}_1 \right)}\quad \text{and}\quad {\color{blue}\beta_1}\mathbf{b}_1+{\color{blue}\beta_2} \mathbf{b}_2 = {\color{blue} \mathbf{T} \left( \mathbf{b}_2 \right)}.


$$

Solving these two systems gives

$$


[\begin{aligned}𝛼_{1} \\ 𝛼_{2}\end{aligned}]


$$

Therefore,

$$


[\begin{aligned}16 & 25 \\ −9 & −14\end{aligned}]


$$

### Example: Calculating the Image of a Vector Given the Matrix of a Linear Transformation Relative to a Basis

#### Question

Let $\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2 \}$ be a basis of $\mathbb{R}^2$ and let $\mathbf{T}:\mathbb{R}^2 \rightarrow \mathbb{R}^2$ be a linear transformation. Find $[\mathbf{T}(\mathbf{x})]_{\mathcal{B}}$, given that

$$


[\begin{aligned}3 & 1 \\ −2 & 5\end{aligned}]


$$

#### Explanation

The image of $[\mathbf{x}]_{\mathcal{B}}$ relative to the basis $\mathcal{B}$ under the action of the linear transformation $\mathbf{T}$ is given by

$$


\begin{aligned}[𝐓(𝐱)]_{B} & =[𝐓]_{B}[𝐱]_{B} \\ & =[\begin{matrix}3 & 1 \\ −2 & 5\end{matrix}][\begin{matrix}−3 \\ 2\end{matrix}] \\ & =[\begin{matrix}−7 \\ 16\end{matrix}].\end{aligned}


$$

### The General Case

In general, consider a basis $\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2,\dots, \mathbf{b}_n \}$ of a vector space $V$ and a linear transformation $\mathbf{T}:V \rightarrow V$. For any $\mathbf{x}\in V$ we have that

$$


\mathbf{x} = x_1\mathbf{b}_1+x_2\mathbf{b}_2+\cdots + x_n\mathbf{b}_n


$$

or, equivalently $\begin{aligned}𝑥_{1} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}$. Then the matrix for $\mathbf{T}$ relative to $\mathcal{B}$ is given by

$$


\begin{aligned}| & | & & | \\ [𝐓(𝐛_{1})]_{B} & [𝐓(𝐛_{2})]_{B} & ⋯ & [𝐓(𝐛_{𝑛})]_{B} \\ | & | & & |\end{aligned}


$$

Therefore

$$


\begin{aligned}| & | & & | \\ [𝐓(𝐛_{1})]_{B} & [𝐓(𝐛_{2})]_{B} & ⋯ & [𝐓(𝐛_{𝑛})]_{B} \\ | & | & & |\end{aligned}


$$

### Example: Finding the Matrix of a Linear Transformation Given the Images of the Basis Vectors

#### Question

Let $\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2,\mathbf{b}_3 \}$ be a basis of $\mathbb{R}^3.$ The matrix $[\,\mathbf{T}\,]_{\mathcal{B}}$ of the linear transformation $\mathbf{T}:\mathbb{R}^3 \rightarrow \mathbb{R}^3$ is given by

$$


\begin{aligned}1 & 1 & 𝑐 \\ 0 & 𝑏 & 1 \\ 𝑎 & 0 & 1\end{aligned}


$$

Find the value of $\,a+b+c,\,$ given that

$$


\begin{aligned}𝐓(𝐛_{1}) & =𝐛_{1}+𝐛_{3}, \\ 𝐓(𝐛_{2}) & =𝐛_{1}+𝐛_{2}, \\ 𝐓(𝐛_{3}) & =𝐛_{2}+𝐛_{3}.\end{aligned}


$$

#### Explanation

First, we write down the coordinates of the images relative to the basis $\mathcal{B}\mathbin{:}$

$$


\begin{aligned}1 \\ 0 \\ 1\end{aligned}


$$

Now, the $\mathcal{B}$-matrix for $\mathbf{T}$ is a matrix whose columns are the coordinates of the vectors $\mathbf{T}(\mathbf{b}_1),$ $\mathbf{T}(\mathbf{b}_2),$ and $\mathbf{T}(\mathbf{b}_3)$ relative to the basis $\mathcal{B}.$ Therefore, we obtain

$$


\begin{aligned}1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1\end{aligned}


$$

Finally, $a=1,$ $b=1,$ $c=0$ and

$$


a+b+c = 1+1+0 = 2.


$$

### Example: Finding the Matrix of a Linear Transformation Relative to a Basis in a Two-Dimensional Vector Space

#### Question

Let $\mathcal{B}$ be a basis of $\mathbb{R}^2$ and let $\mathbf{T}: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ be a linear transformation. Find $[\,\mathbf{T}\,]_{\mathcal{B}}$, given that

$$


[\begin{aligned}5 \\ −4\end{aligned}]


$$

#### Explanation

Let's denote the vectors of $\mathcal{B}$ as $\{\mathbf{b}_1,\mathbf{b}_2 \}.$ The $\mathcal{B}$-matrix for $\mathbf{T}$ is a matrix whose columns are the coordinates of the vectors $\mathbf{T}(\mathbf{b}_1)$ and $\mathbf{T}(\mathbf{b}_2)$ relative to the basis $\mathcal{B}.$

To find the coordinates of $\mathbf{T}(\mathbf{b}_1)$ and $\mathbf{T}(\mathbf{b}_2)$ relative to the basis $\mathcal{B}$, we consider the matrix

$$


\begin{aligned}| & | & | & | \\ 𝐛_{1} & 𝐛_{2} & 𝐓(𝐛_{1}) & 𝐓(𝐛_{2}) \\ | & | & | & |\end{aligned}


$$

Now, we reduce the left-hand side to reduced row echelon form using Gaussian elimination. Then, on the right-hand side, we will obtain the $\mathcal{B}$-matrix for $\mathbf{T}\mathbin{:}$

$$


\begin{aligned}𝑀 & =[\begin{matrix}1 & 1 & 5 & 3 \\ −1 & 1 & −4 & −7\end{matrix}] & & \begin{matrix}𝑅_{2}:=𝑅_{2}+𝑅_{1}\end{matrix} \\ & ∼[\begin{matrix}1 & 1 & 5 & 3 \\ 0 & 2 & 1 & −4\end{matrix}] & & \begin{matrix}𝑅_{2}:=\frac{1}{2}𝑅_{2}\end{matrix} \\ & ∼\begin{matrix}1 & 1 & 5 & 3 \\ 0 & 1 & \frac{1}{2} & −2\end{matrix} & & \begin{matrix}𝑅_{1}:=𝑅_{1}−𝑅_{2}\end{matrix} \\ & ∼\begin{matrix}1 & 0 & \frac{9}{2} & 5 \\ 0 & 1 & \frac{1}{2} & −2\end{matrix} & & \end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}\frac{9}{2} & 5 \\ \frac{1}{2} & −2\end{aligned}


$$

### Example: Finding the Matrix of a Linear Transformation Relative to a Basis in a Three-Dimensional Vector Space

#### Question

The basis $\mathcal{B}$ of $\mathbb{R}^3$ and the matrix $[\,\mathbf{T}\,]_{\mathcal{B}}$ of the linear transformation $\mathbf{T}: \mathbb{R}^3 \rightarrow \mathbb{R}^3$ relative to $\mathcal{B}$ are given by

$$


\begin{aligned}1 \\ 0 \\ 0\end{aligned}


$$

What is the value of $\,a+b+c,\,$ given that

$$


\begin{aligned}−9 \\ 0 \\ 4\end{aligned}


$$

#### Explanation

Let's denote the vectors of $\mathcal{B}$ as $\{\mathbf{b}_1,\mathbf{b}_2,\mathbf{b}_3 \}.$ The $\mathcal{B}$-matrix for $\mathbf{T}$ is a matrix whose columns are the coordinates of the vectors $\mathbf{T}(\mathbf{b}_1),$ $\mathbf{T}(\mathbf{b}_2),$ and $\mathbf{T}(\mathbf{b}_3)$ relative to the basis $\mathcal{B}.$

To find the coordinates of $\mathbf{T}(\mathbf{b}_1),$ $\mathbf{T}(\mathbf{b}_2),$ and $\mathbf{T}(\mathbf{b}_3)$ relative to the basis $\mathcal{B}$, we consider the matrix

$$


\begin{aligned}| & | & | & | & | & | \\ 𝐛_{1} & 𝐛_{2} & 𝐛_{3} & 𝐓(𝐛_{1}) & 𝐓(𝐛_{2}) & 𝐓(𝐛_{3}) \\ | & | & | & | & | & |\end{aligned}


$$

Now, we reduce the left-hand side to reduced row echelon form using Gaussian elimination. Then, on the right-hand side, we will obtain the $\mathcal{B}$-matrix for $\mathbf{T}\mathbin{:}$

$$


\begin{aligned}𝑀 & =\begin{matrix}1 & −3 & 0 & −9 & 7 & 10 \\ 0 & 1 & −3 & 0 & −2 & −10 \\ 0 & 0 & 4 & 4 & 0 & 8\end{matrix} & & \begin{matrix}𝑅_{3}:=\frac{1}{4}𝑅_{3}\end{matrix} \\ & ∼\begin{matrix}1 & −3 & 0 & −9 & 7 & 10 \\ 0 & 1 & −3 & 0 & −2 & −10 \\ 0 & 0 & 1 & 1 & 0 & 2\end{matrix} & & \begin{matrix}𝑅_{2}:=𝑅_{2}+3𝑅_{3}\end{matrix} \\ & ∼\begin{matrix}1 & −3 & 0 & −9 & 7 & 10 \\ 0 & 1 & 0 & 3 & −2 & −4 \\ 0 & 0 & 1 & 1 & 0 & 2\end{matrix} & & \begin{matrix}𝑅_{1}:=𝑅_{1}+3𝑅_{2}\end{matrix} \\ & ∼\begin{matrix}1 & 0 & 0 & 0 & 1 & −2 \\ 0 & 1 & 0 & 3 & −2 & −4 \\ 0 & 0 & 1 & 1 & 0 & 2\end{matrix} & & \end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}0 & 1 & −2 \\ 3 & −2 & −4 \\ 1 & 0 & 2\end{aligned}


$$

Finally, $a=1,$ $b=-2,$ $c=-2$ and

$$


a+b+c = 1+(-2)+(-2) = -3.


$$
