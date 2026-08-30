# The Coordinates of a Vector Relative to a Basis in Abstract Vector Spaces

Source: https://www.mathacademy.com/topics/3212?courseId=55
Topic ID: 3212

## Prerequisites

- [Writing Vectors in Different Bases](./1865-writing-vectors-in-different-bases.md)
- [Bases in Abstract Vector Spaces](./1909-bases-in-abstract-vector-spaces.md)

## Lesson

### Introduction

We've already seen how to write the coordinates of a vector $\mathbf v\in \mathbb R^n$ relative some general basis $\mathcal B$ of $\mathbb R^n.$ In this lesson, we will generalize this concept to abstract vector spaces.

As an example, consider the matrices $A_1$ and $A_2,$ given by

$$


[\begin{aligned}3 & −1 \\ 0 & 5\end{aligned}]


$$

The set $\mathcal{B}=\big\{A_1, A_2 \big\}$ is a basis of the vector space $V = \textrm{Span}\big\{A_1, A_2 \big\}.$ Now, suppose that the coordinates of the matrix $C$ relative to $\mathcal{B}$ are

$$


[\begin{aligned}2 \\ 4\end{aligned}]


$$

Let's find the matrix $C$ using this information.

As usual, any vector in $\textrm{Span}\big\{A_1, A_2 \big\}$ can be written as

$$


x_1 A_1 + x_2 A_2,


$$

where $x_1,x_2$ are the coordinates of the vector relative to the basis.

In our case, we have

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

Therefore,

$$


\begin{aligned}𝐶 & =2⋅[\begin{aligned}3 & −1 \\ 0 & 5\end{aligned}]+4⋅[\begin{aligned}0 & 3 \\ 2 & −2\end{aligned}] \\ & =[\begin{aligned}6 & −2 \\ 0 & 10\end{aligned}]+[\begin{aligned}0 & 12 \\ 8 & −8\end{aligned}] \\ & =[\begin{aligned}6 & 10 \\ 8 & 2\end{aligned}].\end{aligned}


$$

### Example: Calculating a Vector Given Its Coordinates Relative to a Basis

#### Question

Consider the polynomials $p_1(t)$ and $p_2(t),$ given by

$$


p_1(t)=3+2t, \qquad p_2(t)=-t+t^2.


$$

Find $p(t)$ given that $\mathcal{B}=\big\{p_1(t), p_2(t) \big\}$ is a basis of $\textrm{Span}\big\{p_1, p_2 \big\},$ and the coordinates of $p(t)$ relative to $\mathcal{B}$ are $[\begin{aligned}4 \\ −3\end{aligned}]$

#### Explanation

Any vector in $\textrm{Span}\big\{p_1, p_2 \big\}$ can be written as

$$


\begin{aligned}𝑥_{1}𝑝_{1}(𝑡)+𝑥_{2}𝑝_{2}(𝑡).\end{aligned}


$$

In our case, we have

$$


[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]


$$

Therefore,

$$


\begin{aligned}𝑝(𝑡) & =4⋅(3+2𝑡)+(−3)⋅(−𝑡+𝑡^{2}) \\ & =12+8𝑡+3𝑡−3𝑡^{2} \\ & =12+11𝑡−3𝑡^{2}.\end{aligned}


$$

### Example: Finding the Coordinates of a Vector With Respect to a Given Basis in a Matrix Vector Space

#### Question

Consider the following matrices:

$$


[\begin{aligned}2 & 0 \\ 8 & −4\end{aligned}]


$$

If $\mathcal B = \{B_1,B_2\}$ is a basis of $\textrm{Span}\{B_1, B_2 \},$ calculate $[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}]$

#### Explanation

We need to find $x_1$ and $x_2$ such that

$$


x_1 B_1 +x_2 B_2 = A.


$$

Substituting the given information into the above equation, we get

$$


\begin{aligned}𝑥_{1}[\begin{aligned}2 & 0 \\ 8 & −4\end{aligned}]+𝑥_{2}[\begin{aligned}−1 & 0 \\ −2 & 1\end{aligned}] & =[\begin{aligned}−5 & 0 \\ −2 & 1\end{aligned}] \\ [\begin{aligned}2𝑥_{1}−𝑥_{2} & 0 \\ 8𝑥_{1}−2𝑥_{2} & −4𝑥_{1}+𝑥_{2}\end{aligned}] & =[\begin{aligned}−5 & 0 \\ −2 & 1\end{aligned}].\end{aligned}


$$

Equating the corresponding entries, we obtain

$$


\begin{aligned}2𝑥_{1}−𝑥_{2}=−5 \\ 8𝑥_{1}−2𝑥_{2}=−2 \\ −4𝑥_{1}+𝑥_{2}=1.\end{aligned}


$$

The equations above give a linear system with the augmented matrix

$$


\begin{aligned}2 & −1 & −5 \\ 8 & −2 & −2 \\ −4 & 1 & 1\end{aligned}


$$

Row-reducing the matrix using Gaussian elimination, we obtain the following:

$$


\begin{aligned}𝑀= & \begin{aligned}2 & −1 & −5 \\ 8 & −2 & −2 \\ −4 & 1 & 1\end{aligned} & & \begin{aligned}𝑅_{2}:=𝑅_{2}+(−4)𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}+2𝑅_{1}\end{aligned} \\ ∼ & \begin{aligned}2 & −1 & −5 \\ 0 & 2 & 18 \\ 0 & −1 & −9\end{aligned} & & \end{aligned}


$$

The system is now

$$


\begin{aligned}2𝑥_{1}−𝑥_{2}=−5 \\ 2𝑥_{2}=18 \\ −𝑥_{2}=−9.\end{aligned}


$$

From the second and third equations, we get $x_2 =9.$ From the first equation, we get

$$


\begin{aligned}2𝑥_{1}−9 & =−5 \\ 2𝑥_{1} & =4 \\ 𝑥_{1} & =2.\end{aligned}


$$

Therefore, $[\begin{aligned}2 \\ 9\end{aligned}]$

### Example: Finding the Coordinates of a Vector With Respect to a Given Basis in a Polynomial Vector Space

#### Question

Consider the following polynomials:

$$


p_1(t)=5+t^2, \quad p_2(t)=3t-2t^2, \quad q(t)=5-3t+3t^2.


$$

If $\mathcal{B}=\{p_1(t), p_2(t) \}$ is a basis of $\textrm{Span}\big\{p_1(t), p_2(t) \big\},$ find $[q(t)]_{\mathcal{B}}.$

#### Explanation

We need to find $x_1$ and $x_2$ such that

$$


x_1 p_1(t)+x_2 p_2(t) = q(t)


$$

Substituting the given information into the above equation, we get

$$


\begin{aligned}𝑥_{1}(5+𝑡^{2})+𝑥_{2}(3𝑡−2𝑡^{2}) & =5−3𝑡+3𝑡^{2} \\ 5𝑥_{1}+3𝑥_{2}𝑡+(𝑥_{1}−2𝑥_{2})𝑡^{2} & =5−3𝑡+3𝑡^{2}.\end{aligned}


$$

Equating the coefficients of $t$, we obtain

$$


\begin{aligned}5𝑥_{1}=5 \\ 3𝑥_{2}=−3 \\ 𝑥_{1}−2𝑥_{2}=3.\end{aligned}


$$

The equations above give a linear system with the augmented matrix

$$


\begin{aligned}5 & 0 & 5 \\ 0 & 3 & −3 \\ 1 & −2 & 3\end{aligned}


$$

Row-reducing the matrix using Gaussian elimination, we obtain the following:

$$


\begin{aligned}𝑀= & \begin{aligned}5 & 0 & 5 \\ 0 & 3 & −3 \\ 1 & −2 & 3\end{aligned} & 𝑅_{3} & :=𝑅_{3}+(−\frac{1}{5})𝑅_{1} \\ ∼ & \begin{aligned}5 & 0 & 5 \\ 0 & 3 & −3 \\ 0 & −2 & 2\end{aligned} & 𝑅_{3} & :=𝑅_{3}+\frac{2}{3}𝑅_{2} \\ ∼ & \begin{aligned}5 & 0 & 5 \\ 0 & 3 & −3 \\ 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

The system is now

$$


\begin{aligned}5𝑥_{1}=5 \\ 3𝑥_{2}=−3.\end{aligned}


$$

From the first and second equations, we get $x_1=1$ and $x_2 =-1.$ Therefore, $[\begin{aligned}1 \\ −1\end{aligned}]$

### Isomorphisms of Vector Spaces

Suppose we fix a basis $\mathcal{B}=\{\mathbf{b}_1, \mathbf{b}_2, \ldots, \mathbf{b}_n \}$ of a finite-dimensional vector space $V$ with scalars from $\mathbb{R}$ (note that "finite-dimensional" means that the basis contains a finite number of elements). Then, we can represent any element $\mathbf{v} \in V$ using the coordinates of $\mathbf{v}$ relative to the basis $\mathcal{B} \mathbin{:}$

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

This defines a bijective mapping $\phi: V\to \mathbb{R}^n.$ Moreover, this particular mapping has some nice properties:

- $\phi(\mathbf{u}+\mathbf{v}) = \phi(\mathbf{u}) + \phi(\mathbf{v})$ for any $\mathbf{u}, \mathbf{v} \in V,$ and

- $\phi(\alpha \mathbf{v}) = \alpha \phi(\mathbf{v})$ for any $\mathbf{v} \in V$ and any $\alpha \in \mathbb{R}.$

Because of this, we say that $V$ is **isomorphic** to $\mathbb{R}^n.$ Intuitively, this means that $V$ and $\mathbb R^n$ have identical structures.

So, any finite-dimensional vector space is isomorphic to $\mathbb{R}^n$ for some particular $n.$ This means that instead of studying all possible vector spaces, we can simply study only one family of vector spaces, namely $\mathbb{R}^n$ for $n\geq 1.$
