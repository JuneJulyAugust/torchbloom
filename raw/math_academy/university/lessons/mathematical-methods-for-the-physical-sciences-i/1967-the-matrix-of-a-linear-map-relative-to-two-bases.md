# The Matrix of a Linear Map Relative to Two Bases

Source: https://www.mathacademy.com/topics/1967?courseId=154
Topic ID: 1967

## Prerequisites

- [Linear Maps Between Two Different Vector Spaces](./907-linear-maps-between-two-different-vector-spaces.md)
- [The Matrix of a Linear Transformation Relative to a Basis](./1961-the-matrix-of-a-linear-transformation-relative-to-a-basis.md)

## Lesson

### Introduction

Let's suppose we have the linear map

$$


\mathbf T: {\color{blue}V} \to {\color{red}W}


$$

where the bases of the vector spaces $\color{blue}V$ and ${\color{red}W}$ respectively are given by

$$


{\color{blue}\mathcal{B}}=\{ {\color{blue}\mathbf{b}_1},{\color{blue}\mathbf{b}_2}, {\color{blue}\mathbf{b}_3} \}, \qquad \qquad {\color{red}\mathcal{C}} = \{ {\color{red}\mathbf{c}_1},{\color{red}\mathbf{c}_2} \}.


$$

The **matrix of $\mathbf{T}$ with respect to the bases $\color{blue}\mathcal{B}$ and $\color{red}\mathcal{C}$** is the matrix whose columns are the coordinates of the vectors $\mathbf{T}({\color{blue}\mathbf{b}_1}),$ $\mathbf{T}(\color{blue}{\mathbf{b}_2}),$ and $\mathbf{T}({\color{blue}\mathbf{b}_3})$ relative to the basis ${\color{red}\mathcal{C}}\mathbin{:}$

$$


\begin{aligned}[𝐓]_{B|C} & =\begin{matrix}| & | & | \\ [𝐓(𝐛_{1})]_{C} & [𝐓(𝐛_{2})]_{C} & [𝐓(𝐛_{3})]_{C} \\ | & | & |\end{matrix}\end{aligned}


$$

For example, if

$$


[\begin{aligned}3 \\ 1\end{aligned}]


$$

then

$$


\begin{aligned}[𝐓]_{B|C} & =[\begin{matrix}3 & 10 & −12 \\ 1 & −1 & 0\end{matrix}].\end{aligned}


$$

### Example: Finding the Matrix of a Linear Map Relative to Two Bases Using the Definition

#### Question

Suppose $\mathbf{T}: V \rightarrow W$ is a linear map and $\mathcal{B}=\{\mathbf{b}_1,\mathbf{b}_2, \mathbf{b}_3 \}$ and $\mathcal{C} = \{\mathbf{c}_1,\mathbf{c}_2 \}$ are the bases of the vector spaces $V$ and $W,$ respectively. Find the matrix $[\mathbf{T}]_{\mathcal{B}|\mathcal{C}}$ of the map $\mathbf{T}$ relative to these bases, if

$\mathbf{T}(\mathbf{b}_1)=-3\mathbf{c}_1+5\mathbf{c}_2,\quad$ $\mathbf{T}(\mathbf{b}_2)=\mathbf{c}_2-2\mathbf{c}_1\quad$ and $\quad\mathbf{T}(\mathbf{b}_3)=\mathbf{c}_1+5\mathbf{c}_2.$

#### Explanation

First, we write the images of vectors in $\mathcal{B}$ relative to the basis $\mathcal{C} \mathbin{:}$

$$


\begin{aligned}𝐓(𝐛_{1})=−3𝐜_{1}+5𝐜_{2} & \,⟹\,[𝐓(𝐛_{1})]_{C}=[\begin{matrix}−3 \\ 5\end{matrix}] \\ 𝐓(𝐛_{2})=𝐜_{2}−2𝐜_{1} & \,⟹\,[𝐓(𝐛_{2})]_{C}=[\begin{matrix}−2 \\ 1\end{matrix}] \\ 𝐓(𝐛_{3})=𝐜_{1}+5𝐜_{2} & \,⟹\,[𝐓(𝐛_{3})]_{C}=[\begin{matrix}1 \\ 5\end{matrix}]\end{aligned}


$$

Now, $[\mathbf{T}]_{\mathcal{B}|\mathcal{C}}$ is the matrix whose columns are the coordinates of the vectors $\mathbf{T}(\mathbf{b}_1),$ $\mathbf{T}(\mathbf{b}_2)$ and $\mathbf{T}(\mathbf{b}_3)$ relative to the basis $\mathcal{C}\mathbin{:}$

$$


[\begin{aligned}−3 & −2 & 1 \\ 5 & 1 & 5\end{aligned}]


$$

### Example: Finding the Matrix of a Linear Map Relative to Two Bases Given One Basis

#### Question

Consider the basis $\mathcal{B}=\{\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3\}$ of the vector space $V$ and the basis $\mathcal{C}$ of $\mathbb{R}^2$ given by

$$


[\begin{aligned}−1 \\ 1\end{aligned}]


$$

Find the matrix $[\mathbf{T}]_{\mathcal{B}|\mathcal{C}}$ of the map $\mathbf{T}:V \to \mathbb{R}^2$ relative to these bases if

$$


[\begin{aligned}1 \\ 2\end{aligned}]


$$

#### Explanation

Recall that $[\mathbf{T}]_{\mathcal{B}|\mathcal{C}}$ is the matrix whose columns are the coordinates of the vectors $\mathbf{T}(\mathbf{b}_1),$ $\mathbf{T}(\mathbf{b}_2),$ and $\mathbf{T}(\mathbf{b}_3)$ relative to the basis $\mathcal{C}.$

First, we need to find the coordinates of $\mathbf{T}(\mathbf{b}_i)$ relative to the basis $\mathcal{C}$ for each $i=1,2,3.$ We can do this simultaneously by considering the following matrix:

$$


\begin{aligned}| & | & | & | & | \\ 𝐜_{1} & 𝐜_{2} & 𝐓(𝐛_{1}) & 𝐓(𝐛_{2}) & 𝐓(𝐛_{3}) \\ | & | & | & | & |\end{aligned}


$$

We reduce the left-hand side to reduced row echelon form using Gaussian elimination:

$$


\begin{aligned}𝑀 & =[\begin{matrix}−1 & 4 & 1 & −3 & 7 \\ 1 & −3 & 2 & −5 & 1\end{matrix}] & & \begin{matrix}𝑅_{1}:=(−1)𝑅_{1}\end{matrix} \\ & ∼[\begin{matrix}1 & −4 & −1 & 3 & −7 \\ 1 & −3 & 2 & −5 & 1\end{matrix}] & & \begin{matrix}𝑅_{2}:=𝑅_{2}+(−1)𝑅_{1}\end{matrix} \\ & ∼[\begin{matrix}1 & −4 & −1 & 3 & −7 \\ 0 & 1 & 3 & −8 & 8\end{matrix}] & & \begin{matrix}𝑅_{1}:=𝑅_{1}+4𝑅_{2}\end{matrix} \\ & ∼[\begin{matrix}1 & 0 & 11 & −29 & 25 \\ 0 & 1 & 3 & −8 & 8\end{matrix}] & & \end{aligned}


$$

Finally, the right-hand side gives the matrix of the linear transformation relative to the bases $\mathcal{B}$ and $\mathcal{C} \mathbin{:}$

$$


[\begin{aligned}11 & −29 & 25 \\ 3 & −8 & 8\end{aligned}]


$$

### The Image of a Vector Under a Linear Map Given by a Matrix Relative to Two Bases

Given the matrix $[\mathbf{T}]_{\mathcal{B}|\mathcal{C}}$ of a linear map $\mathbf{T}:V \to W$ relative to the bases $\mathcal{B}$ and $\mathcal{C},$ and the coordinates $[\mathbf{x}]_{\mathcal{B}}$ of a vector $\mathbf{x}$ relative to $\mathcal{B},$ the image of $\mathbf{x}$ under $\mathbf{T}$ with respect to the basis $\mathcal{C}$ can be found as

$$


[\mathbf{T}(\mathbf{x})]_{\mathcal{C}} = [\mathbf{T}]_{{\mathcal{B}}|{\mathcal{C}}}\cdot [\mathbf{x}]_{\mathcal{B}}


$$

For example, if

$$


[\begin{aligned}1 & 3 & −2 \\ 1 & 2 & 0\end{aligned}]


$$

then the image of $\mathbf x$ under $\mathbf T$ relative to $\mathcal C$ is given by

$$


\begin{aligned}[𝐓(𝐱)]_{C} & =[\begin{matrix}1 & 3 & −2 \\ 1 & 2 & 0\end{matrix}]\begin{matrix}3 \\ 0 \\ 1\end{matrix} \\ & =[\begin{matrix}1 \\ 3\end{matrix}].\end{aligned}


$$

### Example: Finding the Image of a Vector Under a Linear Map Given the Matrix Relative to Two Bases

#### Question

$$


[\begin{aligned}1 & 4 & −2 \\ 3 & 7 & 1\end{aligned}]


$$

Suppose $\mathcal{B}$ and $\mathcal{C}$ are bases of the vector spaces $V$ and $W,$ respectively. The matrix $[\mathbf{T}]_{\mathcal{B}|\mathcal{C}}$ of the linear map $\mathbf{T}:V \rightarrow W$ relative to these bases, and the coordinates of the vector $\mathbf{x} \in V$ relative to $\mathcal{B}$ are shown above. Find $[\mathbf{T}(\mathbf{x})]_{\mathcal{C}}.$

#### Explanation

The coordinates of the image of $\mathbf{x}$ under $\mathbf{T}$ relative to the basis $\mathcal{C}$ can be found as follows:

$$


\begin{aligned}[𝐓(𝐱)]_{C} & =[𝐓]_{B|C}⋅[𝐱]_{B} \\ & =[\begin{matrix}1 & 4 & −2 \\ 3 & 7 & 1\end{matrix}]\begin{matrix}3 \\ −2 \\ 1\end{matrix} \\ & =[\begin{matrix}−7 \\ −4\end{matrix}]\end{aligned}


$$

### Example: Finding the Image of a Vector Given With Respect to the Standard Basis Under a Linear Map

#### Question

$$


[\begin{aligned}1 \\ 4\end{aligned}]


$$

Consider the basis $\mathcal{B}$ of $\mathbb{R}^2$ (shown above) and a basis $\mathcal{C}$ of $\mathbb{R}^3.$ The matrix $[\mathbf{T}]_{\mathcal{B}|\mathcal{C}}$ of the linear map $\mathbf{T}:\mathbb{R}^2 \rightarrow \mathbb{R}^3$ relative to these bases, and the vector $\mathbf{x} \in \mathbb{R}^2,$ are also given. Find $[\mathbf{T}(\mathbf{x})]_{\mathcal{C}}.$

#### Explanation

We can find the coordinates of the image of $\mathbf{x}$ under $\mathbf{T}$ relative to the basis $\mathcal{C}$ as follows:

$$


\begin{aligned}[𝐓(𝐱)]_{C} & =[𝐓]_{B|C}⋅[𝐱]_{B}\end{aligned}


$$

First, we need to find $[\mathbf{x}]_{\mathcal{B}},$ the coordinates of $\mathbf{x}$ relative to $\mathcal{B}.$ So, let

$$


[\begin{aligned}5 \\ 2\end{aligned}]


$$

This gives us the system

$$


\begin{aligned}𝑥_{1}−2𝑥_{2}=5 \\ 4𝑥_{1}−5𝑥_{2}=2.\end{aligned}


$$

We now row-reduce the corresponding augmented matrix using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{matrix}1 & −2 & 5 \\ 4 & −5 & 2\end{matrix}] & & \begin{matrix}𝑅_{2}:=𝑅_{2}+(−4)𝑅_{1}\end{matrix} \\ & ∼[\begin{matrix}1 & −2 & 5 \\ 0 & 3 & −18\end{matrix}] & & \begin{matrix}𝑅_{2}:=\frac{1}{3}𝑅_{2}\end{matrix} \\ & ∼[\begin{matrix}1 & −2 & 5 \\ 0 & 1 & −6\end{matrix}] & & \begin{matrix}𝑅_{1}:=𝑅_{1}+2𝑅_{2}\end{matrix} \\ & ∼[\begin{matrix}1 & 0 & −7 \\ 0 & 1 & −6\end{matrix}] & & \end{aligned}


$$

Therefore, $[\begin{aligned}−7 \\ −6\end{aligned}]$

Finally, we obtain

$$


\begin{aligned}[𝐓(𝐱)]_{C} & =[𝐓]_{B|C}⋅[𝐱]_{B} \\ & =\begin{matrix}1 & −4 \\ 3 & −2 \\ 0 & 1\end{matrix}[\begin{matrix}−7 \\ −6\end{matrix}] \\ & =\begin{matrix}17 \\ −9 \\ −6\end{matrix}.\end{aligned}


$$
