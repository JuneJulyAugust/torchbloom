# Orthogonal Sets in Euclidean Spaces

Source: https://www.mathacademy.com/topics/2103?courseId=55
Topic ID: 2103

## Prerequisites

- [Expressing the Coordinates of a Vector in a Given Basis](./1864-expressing-the-coordinates-of-a-vector-in-a-given-basis.md)
- [The Norm of a Vector in N-Dimensional Euclidean Space](./2095-the-norm-of-a-vector-in-n-dimensional-euclidean-space.md)
- [Orthogonal Vectors in Euclidean Spaces](./2099-orthogonal-vectors-in-euclidean-spaces.md)

## Lesson

### Introduction

A set of vectors ${U}=\{\mathbf{u}_1, \cdots, \mathbf{u}_p \}$ in $\mathbb{R}^n$ is an **orthogonal set** if each pair of distinct vectors from the set is orthogonal.

For example, let's consider the following set:

$$


\begin{aligned}3 \\ 1 \\ 1\end{aligned}


$$

If we denote the vectors in our set ${W}$ as $\{\mathbf{w}_1, \mathbf{w}_2, \mathbf{w}_3 \},$ we can check that ${W}$ is orthogonal by showing that

$$


\begin{aligned}𝐰_{1}⋅𝐰_{2}=0 \\ 𝐰_{1}⋅𝐰_{3}=0 \\ 𝐰_{2}⋅𝐰_{3}=0.\end{aligned}


$$

Let's compute each dot product:

$$


\begin{aligned}𝐰_{1}⋅𝐰_{2} & =\begin{aligned}3 \\ 1 \\ 1\end{aligned}⋅\begin{aligned}−1 \\ 2 \\ 1\end{aligned}=3⋅(−1)+1⋅2+1⋅1=0 & ✓ \\ 𝐰_{1}⋅𝐰_{3} & =\begin{aligned}3 \\ 1 \\ 1\end{aligned}⋅\begin{aligned}−1 \\ −4 \\ 7\end{aligned}=3⋅(−1)+1⋅(−4)+1⋅7=0 & ✓ \\ 𝐰_{2}⋅𝐰_{3} & =\begin{aligned}−1 \\ 2 \\ 1\end{aligned}⋅\begin{aligned}−1 \\ −4 \\ 7\end{aligned}=(−1)⋅(−1)+2⋅(−4)+1⋅7=0 & ✓\end{aligned}


$$

So indeed, ${W}$ is an orthogonal set.

If an orthogonal set is also a basis, then we call it an **orthogonal basis**. Here, $W$ is an orthogonal basis of $\mathbb{R}^3,$ because it contains three linearly independent (you can check this) orthogonal vectors.

### Example: Determining Whether Sets are Orthogonal

#### Question

Determine whether the following set is orthogonal:

$$


\begin{aligned}2 \\ 0 \\ 1\end{aligned}


$$

#### Explanation

If we denote the vectors in our set ${X}$ as $\{\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3 \},$ we can check that ${X}$ is orthogonal by showing that

$$


\begin{aligned}𝐱_{1}⋅𝐱_{2}=0 \\ 𝐱_{1}⋅𝐱_{3}=0 \\ 𝐱_{2}⋅𝐱_{3}=0.\end{aligned}


$$

Let's compute each dot product:

$$


\begin{aligned}𝐱_{1}⋅𝐱_{2} & =\begin{aligned}2 \\ 0 \\ 1\end{aligned}⋅\begin{aligned}−1 \\ 0 \\ 2\end{aligned}=2⋅(−1)+0⋅0+1⋅2=0 & ✓ \\ 𝐱_{1}⋅𝐱_{3} & =\begin{aligned}2 \\ 0 \\ 1\end{aligned}⋅\begin{aligned}1 \\ −2 \\ 0\end{aligned}=2⋅1+0⋅(−2)+1⋅0=2≠0 & × \\ 𝐱_{2}⋅𝐱_{3} & =\begin{aligned}−1 \\ 0 \\ 2\end{aligned}⋅\begin{aligned}1 \\ −2 \\ 0\end{aligned}=(−1)⋅1+0⋅(−2)+2⋅0=−1≠0 & ×\end{aligned}


$$

So ${X}$ is ** an orthogonal set.

### Orthonormal Sets and Orthonormal Bases

A set of vectors is an **orthonormal set** if it is an orthogonal set of *unit* vectors. Remember that is a unit vector if or equivalently,

An orthonormal set that is also a basis, like the standard basis, is called an **orthonormal basis**. For instance, the standard basis of is an orthonormal basis because the vectors are orthogonal to each other and each vector in the set is a unit vector.

There are two more things to note about orthogonal sets:

- Any orthogonal set of non-zero vectors is linearly independent.

- An orthogonal set in cannot contain more than vectors. More precisely, if is an orthogonal set of non-zero vectors and then we must have that

**Note:** To remember that an orthogonal set of non-zero vectors in cannot contain more than vectors, you can use the following intuitive mnemonic. There are only dimensions in and each non-zero orthogonal vector has a -dimensional span, meaning that it "takes up" dimension of So, you can't "fit" more than orthogonal vectors in

### Example: Determining Whether Sets are Orthonormal

#### Question

Determine whether the following set is orthonormal:

$$


\begin{aligned}\frac{1}{\sqrt{√2}} \\ −\frac{1}{\sqrt{√2}}\end{aligned}


$$

#### Explanation

Let's denote the vectors of the given set as $\{\mathbf{w}_1,\mathbf{w}_2\},$ respectively.

The set $W$ is orthonormal if the following conditions hold:

$$


\begin{aligned}𝐰_{1}⋅𝐰_{1}=1 \\ 𝐰_{2}⋅𝐰_{2}=1\end{aligned}


$$

With that in mind, let's examine our set:

$$


\begin{aligned}𝐰_{1}⋅𝐰_{2} & =\begin{aligned}\frac{1}{\sqrt{√2}} \\ −\frac{1}{\sqrt{√2}}\end{aligned}⋅[\begin{aligned}4 \\ 4\end{aligned}]=\frac{4}{\sqrt{√2}}−\frac{4}{\sqrt{√2}}=0 & ✓ \\ 𝐰_{1}⋅𝐰_{1} & =\begin{aligned}\frac{1}{\sqrt{√2}} \\ −\frac{1}{\sqrt{√2}}\end{aligned}⋅\begin{aligned}\frac{1}{\sqrt{√2}} \\ −\frac{1}{\sqrt{√2}}\end{aligned}=\frac{1}{2}+\frac{1}{2}=1 & ✓ \\ 𝐰_{2}⋅𝐰_{2} & =[\begin{aligned}4 \\ 4\end{aligned}]⋅[\begin{aligned}4 \\ 4\end{aligned}]=16+16=32≠1 & ×\end{aligned}


$$

We see that $\mathbf w_1$ and $\mathbf w_2$ are orthogonal, and $\mathbf w_1$ is a unit vector, but $\mathbf w_2$ is ** a unit vector.

Therefore, ${W}$ is ** an orthonormal set.

### Example: Extending a Set to Form an Orthogonal Basis

#### Question

Consider the orthogonal set $U$ below. By adding a new vector $\mathbf x = [x_1,\,x_2,\,x_3]^T,$ extend the set so that it forms an orthogonal basis of $\mathbb{R}^3.$

$$


\begin{aligned}−1 \\ −1 \\ 2\end{aligned}


$$

#### Explanation

Let's denote the vectors of ${U}$ as $\mathbf{u}_1,\, \mathbf{u}_2.$ To extend the given set to an orthogonal basis of $\mathbb{R}^3,$ we need to find a third vector $\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}$ such that

$$


\begin{aligned}𝐮_{1}⋅𝐱=0 \\ 𝐮_{2}⋅𝐱=0\end{aligned}


$$

So, we consider the augmented matrix $M$ of the system above and reduce it to row echelon form, as follows:

$$


\begin{aligned}𝑀 & =[\begin{aligned}−1 & −1 & 2 & 0 \\ 1 & 1 & 1 & 0\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+𝑅_{1} \\ & ∼[\begin{aligned}−1 & −1 & 2 & 0 \\ 0 & 0 & 3 & 0\end{aligned}] & & \end{aligned}


$$

In the reduced matrix above, there are two pivot columns ($1$st and $3$rd). This means $x_2$ is a free variable. From the second equation, we get $x_3=0.$ Substituting this into the first equation, we obtain

$$


\begin{aligned}−𝑥_{1}−𝑥_{2}+2(0)=0\,⟹\,𝑥_{1}=−𝑥_{2}.\end{aligned}


$$

So, the general solution is

$$


\begin{aligned}−𝑥_{2} \\ 𝑥_{2} \\ 0\end{aligned}


$$

Setting $x_2=1,$ we obtain the vector

$$


\begin{aligned}−1 \\ 1 \\ 0\end{aligned}


$$

Therefore, an orthogonal basis of $\mathbb{R}^3$ is

$$


\begin{aligned}−1 \\ −1 \\ 2\end{aligned}


$$

### Example: Extending a Set to Form an Orthonormal Basis

#### Question

Consider the **** set $U$ below. By adding a new vector $\mathbf x = [x_1,\,x_2,\,x_3]^T,$ extend the set so that it forms an **** basis of $\mathbb{R}^3.$

$$


\begin{aligned}−\frac{1}{\sqrt{√2}} \\ 0 \\ \frac{1}{\sqrt{√2}}\end{aligned}


$$

#### Explanation

Let's denote the vectors of ${U}$ as $\mathbf{u}_1,\, \mathbf{u}_2.$ To extend the given set to an orthonormal basis of $\mathbb{R}^3,$ we need to find a third vector $\mathbf{x}$ such that $\| \mathbf{x} \|=1$ and

$$


\begin{aligned}𝐮_{1}⋅𝐱=0 \\ 𝐮_{2}⋅𝐱=0\end{aligned}


$$

So, we consider the augmented matrix $M$ of the system above and reduce it to row echelon form, as follows:

$$


\begin{aligned}𝑀 & =\begin{aligned}−\frac{1}{\sqrt{√2}} & 0 & \frac{1}{\sqrt{√2}} & 0 \\ \frac{1}{\sqrt{√6}} & \frac{2}{\sqrt{√6}} & \frac{1}{\sqrt{√6}} & 0\end{aligned} & & \begin{aligned}𝑅_{1}:=\sqrt{√2}⋅𝑅_{1} \\ 𝑅_{2}:=\sqrt{√6}⋅𝑅_{2}\end{aligned} \\ & ∼[\begin{aligned}−1 & 0 & 1 & 0 \\ 1 & 2 & 1 & 0\end{aligned}] & & \begin{aligned}𝑅_{2}:=𝑅_{2}+𝑅_{1}\end{aligned} \\ & ∼[\begin{aligned}−1 & 0 & 1 & 0 \\ 0 & 2 & 2 & 0\end{aligned}] & & \end{aligned}


$$

In the reduced matrix above, there are two pivot columns ($1$st and $2$nd). This means $x_3$ is a free variable. From the second equation, we get $x_2=-x_3,$ and from the first equation, we obtain $x_1=x_3.$

So, the general solution is

$$


\begin{aligned}𝑥_{3} \\ −𝑥_{3} \\ 𝑥_{3}\end{aligned}


$$

Setting $x_3=1,$ we obtain the vector $\begin{aligned}1 \\ −1 \\ 1\end{aligned}$

Now, we need to normalize $\mathbf{x}.$ Notice that $\| \mathbf{x} \| = \sqrt{1^2+(-1)^2+1^2} = \sqrt{3}.$ So, we normalize $\mathbf x$ as follows:

$$


\begin{aligned}\frac{1}{\sqrt{√3}} \\ −\frac{1}{\sqrt{√3}} \\ \frac{1}{\sqrt{√3}}\end{aligned}


$$

Therefore, an orthonormal basis of $\mathbb{R}^3$ is

$$


\begin{aligned}−\frac{1}{\sqrt{√2}} \\ 0 \\ \frac{1}{\sqrt{√2}}\end{aligned}


$$
