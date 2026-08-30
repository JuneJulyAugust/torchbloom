# Constrained Optimization of Quadratic Forms: Determining Where Extrema are Attained

Source: https://www.mathacademy.com/topics/4238?courseId=145
Topic ID: 4238

## Prerequisites

- [Diagonalization of 3x3 Symmetric Matrices](./3119-diagonalization-of-3x3-symmetric-matrices.md)
- [Change of Variables in Quadratic Forms](./3122-change-of-variables-in-quadratic-forms.md)
- [Constrained Optimization of Quadratic Forms](./3171-constrained-optimization-of-quadratic-forms.md)

## Lesson

### Introduction

If $A$ is the matrix corresponding to the quadratic form $Q(\mathbf{x}),$ then:

- The maximum value of $Q(\mathbf{x}),$ when $\| \mathbf{x} \|=1,$ is equal to the largest eigenvalue $\lambda_{\textrm{max}}$ of $A,$ and the maximum is attained on the corresponding unit eigenvector $\mathbf{u}_{\textrm{max}}.$

- The minimum value of $Q(\mathbf{x}),$ when $\| \mathbf{x} \|=1,$ is equal to the smallest eigenvalue $\lambda_{\textrm{min}}$ of $A,$ and the minimum is attained on the corresponding unit eigenvector $\mathbf{u}_{\textrm{min}}.$

We'll prove this result at the end of the lesson.

Suppose we're given that the maximum value of the quadratic form

$$


Q(\mathbf{x})=x_1^2-10\: \! x_1x_2+x_2^2


$$

when $\| \mathbf{x} \| = 1$ is $6.$ Let's use this to find a unit vector $\mathbf{u}_{\textrm{max}}$ where this maximum value is attained.

So first, we write down the matrix of our quadratic form:

$$


[\begin{aligned}1 & −5 \\ −5 & 1\end{aligned}]


$$

Next, we find the unit eigenvector that corresponds to the eigenvalue $\lambda_{\textrm{max}}=6{:}$

$$


\begin{aligned}𝐴−6𝐼 & =[\begin{aligned}1 & −5 \\ −5 & 1\end{aligned}]−6[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}]=[\begin{aligned}−5 & −5 \\ −5 & −5\end{aligned}]\end{aligned}


$$

Seeking a non-zero solution of $(A-6I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $[\begin{aligned}−1 \\ 1\end{aligned}]$

Finally, dividing $\mathbf{v}$ by its norm $\| \mathbf{v} \| = \sqrt{2},$ we get

$$


[\begin{aligned}−1 \\ 1\end{aligned}]


$$

Let's check that this is indeed the vector we were looking for:

$$


\begin{aligned}𝑄(𝐮_{max}) & =(\frac{−1}{\sqrt{√2}})^{2}−10(\frac{−1}{\sqrt{√2}})(\frac{1}{\sqrt{√2}})+(\frac{1}{\sqrt{√2}})^{2} \\ & =\frac{1}{2}+\frac{10}{2}+\frac{1}{2} \\ & =6\,✓\end{aligned}


$$

### Example: Finding Where the Extrema of a Quadratic Form Is Attained on the Unit Circle

#### Question

The minimum value of the quadratic form $Q(\mathbf{x})=9x_1^2-24x_1x_2+16x_2^2,$ when $\| \mathbf{x} \| = 1,$ is equal to $0.$ Find a vector $\mathbf{x}$ at which the minimum is attained.

#### Explanation

Let $A$ be the matrix corresponding to our quadratic form. Recall that:

- The maximum value of $Q(\mathbf{x}),$ when $\| \mathbf{x} \|=1,$ is equal to the largest eigenvalue of $A{:}$ The maximum is attained on the corresponding unit eigenvector $\mathbf{u}_{\textrm{max}}.$

- The minimum value of $Q(\mathbf{x}),$ when $\| \mathbf{x} \|=1,$ is equal to the smallest eigenvalue of $A{:}$ The minimum is attained on the corresponding unit eigenvector $\mathbf{u}_{\textrm{min}}.$

First, we write down the matrix of our quadratic form:

$$


[\begin{aligned}9 & −12 \\ −12 & 16\end{aligned}]


$$

Now, we need the unit eigenvector that corresponds to the eigenvalue $\lambda_{\textrm{min}}=0{:}$

$$


\begin{aligned}𝐴−0𝐼 & =[\begin{aligned}9 & −12 \\ −12 & 16\end{aligned}]−[\begin{aligned}0 & 0 \\ 0 & 0\end{aligned}]=[\begin{aligned}9 & −12 \\ −12 & 16\end{aligned}]\end{aligned}


$$

Seeking a non-zero solution of $(A-0I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $[\begin{aligned}4 \\ 3\end{aligned}]$

Finally, dividing $\mathbf{v}$ by its norm $\| \mathbf{v} \| = 5,$ we get

$$


[\begin{aligned}4 \\ 3\end{aligned}]


$$

### Example: Finding Where the Extrema of a Quadratic Form Are Attained on the Unit Sphere

#### Question

The maximum value of the quadratic form $Q(\mathbf{x})= -x_1^2+2x_2^2+6x_3^2+4x_1x_2,$ when $\| \mathbf{x} \| = 1,$ is equal to $6.$ Find a vector $\mathbf{x}$ at which the maximum is attained.

#### Explanation

Let $A$ be the matrix corresponding to our quadratic form. Recall that:

- The maximum value of $Q(\mathbf{x}),$ when $\| \mathbf{x} \|=1,$ is equal to the largest eigenvalue of $A{:}$ The maximum is attained on the corresponding unit eigenvector $\mathbf{u}_{\textrm{max}}.$

- The minimum value of $Q(\mathbf{x}),$ when $\| \mathbf{x} \|=1,$ is equal to the smallest eigenvalue of $A{:}$ The minimum is attained on the corresponding unit eigenvector $\mathbf{u}_{\textrm{min}}.$

First, we write down the matrix of our quadratic form:

$$


\begin{aligned}−1 & 2 & 0 \\ 2 & 2 & 0 \\ 0 & 0 & 6\end{aligned}


$$

Now, we need the unit eigenvector that corresponds to the eigenvalue $\lambda_{\textrm{max}}=6{:}$

$$


\begin{aligned}𝐴−6𝐼 & =\begin{aligned}−1 & 2 & 0 \\ 2 & 2 & 0 \\ 0 & 0 & 6\end{aligned}−6\begin{aligned}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}=\begin{aligned}−7 & 2 & 0 \\ 2 & −4 & 0 \\ 0 & 0 & 0\end{aligned}\end{aligned}


$$

Seeking a non-zero solution of $(A-6I)\mathbf{x}=\mathbf{0}$ gives the eigenvector $\begin{aligned}0 \\ 0 \\ 1\end{aligned}$

Since $\mathbf{v}$ is already normalized ($\|\mathbf{v}\|=1$), we conclude that, $\begin{aligned}0 \\ 0 \\ 1\end{aligned}$

### Constrained Optimization of Quadratic Forms Over Ellipses

Suppose we're given that the maximum value of the quadratic form

$$


Q(\mathbf{x})=x_1^2-2x_1x_2+x_2^2,


$$

over the ellipse $4x_1^2+x_2^2=4$ equals $5.$ How can we find a vector $\mathbf{x}$ at which this maximum is attained?

We can find this vector by applying a suitable change of variable. This change of variable should transform our problem into one where we need to maximize a related quadratic form $Q'$ on the unit circle. Let's see how this is done.

First, we write down the matrix of our quadratic form:

$$


[\begin{aligned}1 & −1 \\ −1 & 1\end{aligned}]


$$

Notice that we can write the constraint equation as follows:

$$


{x_1^2}+ \dfrac{x_2^2}{2^2}=1


$$

which represents an ellipse with semiaxes $a=1$ (along the $x_1$-axis) and $b=2$ (along the $x_2$-axis).

If we introduce new variables

$$


y_1={x_1}, \qquad y_2 = \dfrac{x_2}{2},


$$

the equation of the ellipse will transform into $y_1^2+y_2^2 = 1,$ or $\|\mathbf{y}\|=1.$

So, introducing a change-of-coordinate matrix

$$


[\begin{aligned}1 & 0 \\ 0 & 2\end{aligned}]


$$

we obtain that $\mathbf{x} = P \mathbf{y}.$ Substituting this into the expression of the quadratic form, we get

$$


Q(\mathbf{x}) = \mathbf{x}^T \! A \mathbf{x} = (P\mathbf{y})^T A \, (P\mathbf{y}) = \mathbf{y}^T \! (P^TAP) \mathbf{y}=Q'(\mathbf{y}).


$$

As a result, since $P^T=P,$ the matrix of our quadratic form in the new coordinates is

$$


\begin{aligned}𝐵 & =𝑃^{𝑇}\,𝐴𝑃 \\ & =𝑃𝐴𝑃 \\ & =[\begin{aligned}1 & 0 \\ 0 & 2\end{aligned}][\begin{aligned}1 & −1 \\ −1 & 1\end{aligned}][\begin{aligned}1 & 0 \\ 0 & 2\end{aligned}] \\ & =[\begin{aligned}1 & −1 \\ −2 & 2\end{aligned}][\begin{aligned}1 & 0 \\ 0 & 2\end{aligned}] \\ & =[\begin{aligned}1 & −2 \\ −2 & 4\end{aligned}].\end{aligned}


$$

Now, the goal is to maximize $Q'(\mathbf{y})$ when $\| \mathbf{y} \|=1,$ which we do using our usual methods.

Since we are told that the maximum value of the quadratic form is $5,$ we have

$$


\max \{ Q'(\mathbf{y}) \: | \: \| \mathbf{y} \|=1 \} = \lambda_{\max} = 5.


$$

Next, we find the unit eigenvector that corresponds to the eigenvalue $\lambda_{\textrm{max}}=5{:}$

$$


\begin{aligned}𝐵−5𝐼 & =[\begin{aligned}1 & −2 \\ −2 & 4\end{aligned}]−5[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}]=[\begin{aligned}−4 & −2 \\ −2 & −1\end{aligned}]\end{aligned}


$$

Seeking a non-zero solution of $(B-5I)\mathbf{y}=\mathbf{0}$ gives the eigenvector $[\begin{aligned}−1 \\ 2\end{aligned}]$ Dividing $\mathbf{v}$ by its norm $\| \mathbf{v} \| = \sqrt{5},$ we get

$$


[\begin{aligned}−1 \\ 2\end{aligned}]


$$

Finally, we map this vector back to the initial coordinate system using the change-of-coordinates matrix:

$$


\begin{aligned}𝐱_{max} & =𝑃𝐮_{max} \\ & =[\begin{aligned}1 & 0 \\ 0 & 2\end{aligned}]⋅\frac{1}{\sqrt{√5}}[\begin{aligned}−1 \\ 2\end{aligned}] \\ & =\frac{1}{\sqrt{√5}}[\begin{aligned}−1 \\ 4\end{aligned}]\end{aligned}


$$

### Example: Finding Where the Extrema of a Quadratic Form Is Attained Over an Ellipse

#### Question

Find the minimum value of $Q(\mathbf{x})=16x_1^2+16x_1x_2+x_2^2$ given that $16x_1^2 + x_2^2=16,$ and find the vector $\mathbf{x}$ at which the minimum is obtained.

#### Explanation

First, we write down the matrix of our quadratic form:

$$


[\begin{aligned}16 & 8 \\ 8 & 1\end{aligned}]


$$

Notice that we can write the constraint equation as follows:

$$


\dfrac{x_1^2}{1^2}+\dfrac{x_2^2}{4^2}=1


$$

This is an ellipse with semiaxes $a=1$ (along the $x_1$-axis) and $b=4$ (along the $x_2$-axis).

If we introduce new variables

$\qquad$ $y_1={x_1} \quad$ and $\quad y_2 = \dfrac{x_2}{4},$

the equation of the ellipse will transform into $y_1^2+y_2^2 = 1,$ or $\|\mathbf{y}\|=1.$

So, introducing a change-of-coordinates matrix

$$


[\begin{aligned}1 & 0 \\ 0 & 4\end{aligned}]


$$

we obtain that $\mathbf{x} = P \mathbf{y}.$ Substituting this into the expression of the quadratic form, we get

$$


Q(\mathbf{x}) = \mathbf{x}^T \! A \mathbf{x} = (P\mathbf{y})^T A \, (P\mathbf{y}) = \mathbf{y}^T \! (P^TAP) \mathbf{y}= Q'(\mathbf{y}).


$$

As a result, since $P^T=P,$ the matrix of our quadratic form in new coordinates is

$$


\begin{aligned}𝐵 & =𝑃^{𝑇}\,𝐴𝑃 \\ & =𝑃𝐴𝑃 \\ & =[\begin{aligned}1 & 0 \\ 0 & 4\end{aligned}][\begin{aligned}16 & 8 \\ 8 & 1\end{aligned}][\begin{aligned}1 & 0 \\ 0 & 4\end{aligned}] \\ & =[\begin{aligned}16 & 8 \\ 32 & 4\end{aligned}][\begin{aligned}1 & 0 \\ 0 & 4\end{aligned}] \\ & =[\begin{aligned}16 & 32 \\ 32 & 16\end{aligned}].\end{aligned}


$$

Now, we minimise $Q'(\mathbf{y})$ when $\| \mathbf{y} \|=1,$ as usual. Calculating the eigenvalues $B,$ we obtain the following:

$$


\begin{aligned}|𝐵−𝜆𝐼| & =0 \\ \begin{aligned}16−𝜆 & 32 \\ 32 & 16−𝜆\end{aligned} & =0 \\ (16−𝜆)(16−𝜆)−1\,024 & =0 \\ 𝜆^{2}−32𝜆−768 & =0 \\ (𝜆−48)(𝜆+16) & =0 \\ 𝜆 & =48,\,−16\end{aligned}


$$

Therefore, we have

$$


\min \{ Q'(\mathbf{y}) \: | \: \| \mathbf{y} \|=1 \} = \lambda_{\textrm{min}} = -16.


$$

Next, we need the unit eigenvector that corresponds to the eigenvalue $\lambda_{\textrm{min}}=-16{:}$

$$


\begin{aligned}𝐵−(−16𝐼) & =[\begin{aligned}16 & 32 \\ 32 & 16\end{aligned}]+16[\begin{aligned}1 & 0 \\ 0 & 1\end{aligned}]=[\begin{aligned}32 & 32 \\ 32 & 32\end{aligned}]\end{aligned}


$$

Seeking a non-zero solution of $(B-(-16I))\mathbf{y}=\mathbf{0}$ gives the eigenvector $[\begin{aligned}−1 \\ 1\end{aligned}]$ Dividing $\mathbf{v}$ by its norm $\| \mathbf{v} \| = \sqrt{2},$ we get

$$


[\begin{aligned}−1 \\ 1\end{aligned}]


$$

Finally, we map this vector back to the initial coordinate system using the change-of-coordinates matrix:

$$


\begin{aligned}𝐱_{min} & =𝑃𝐮_{min} \\ & =[\begin{aligned}1 & 0 \\ 0 & 4\end{aligned}]⋅\frac{1}{\sqrt{√2}}[\begin{aligned}−1 \\ 1\end{aligned}] \\ & =\frac{1}{\sqrt{√2}}[\begin{aligned}−1 \\ 4\end{aligned}]\end{aligned}


$$

### Proof of the Main Theorem

To complete the picture, let's prove the main theorem of this lesson:

*The maximum value of a quadratic form $Q(\mathbf{x})=\mathbf{x}^T A \mathbf{x},$ when $\| \mathbf{x} \|=1,$ is equal to the largest eigenvalue of $A{:}$*

$$


\max \{ Q(\mathbf{x}) \: | \: \| \mathbf{x} \| = 1 \} = \lambda_{\textrm{max}}


$$

*The maximum is attained on the corresponding unit eigenvector $\mathbf{u}_{\textrm{max}}.$*

**Note:** We'll show only the first part (about the maximum value) since a similar argument can be used to prove the second part (about the minimum value).

Let $A$ be a real $n \times n$ symmetric matrix corresponding to a quadratic form $Q(\mathbf x)\mathbin.$ As a result, there must be an *orthonormal* matrix $P$ such that

- $D=P^{-1}AP=P^TAP,$ where $D$ is a diagonal matrix.

- The diagonal entries of $D$ are the eigenvalues of $A$. Without loss of generality, we can assume that the eigenvalues are $\lambda_1 \geq \lambda_2 \geq \ldots \geq \lambda_n,$ where $\lambda_{\textrm{max}} = \lambda_1.$

- The columns $\mathbf{u}_1,\mathbf{u}_2, \ldots, \mathbf{u}_n$ of $P$ form an orthonormal set of unit eigenvectors of $A.$ So, $\mathbf{u}_{\textrm{max}} = \mathbf{u}_1.$

Take $\mathbf x=P\mathbf y.$ Since, $P$ is orthonormal, we have

$$


\|\mathbf x\| = \|P \mathbf y \| = \|\mathbf y\|


$$

and

$$


Q(\mathbf x) = \mathbf x^T\!A\mathbf x = (P\mathbf y)^T\!A(P\mathbf y) = \mathbf{y}^T (P^T\!AP) \mathbf{y} = \mathbf{y}^T D \mathbf{y}


$$

for all $\mathbf{y} \in \mathbb{R}^n.$

Therefore, we can conclude the following:

- $\|\mathbf x\| =1 \Longleftrightarrow \|\mathbf y\| =1$ for all $\mathbf y$ such that $\mathbf x=P\mathbf y$

- Restricted to the unit sphere of $\Bbb R^n,$ the images of the quadratic forms $Q(\mathbf x)$ and $Q'(\mathbf y)= \mathbf y^T D\mathbf y$ coincide:

Now, for any unit vector $\mathbf{y} \in \mathbb{R}^n,$ we obtain

$$


\begin{aligned}𝑄(𝐱) & =𝑄^{′}(𝐲) \\ & =𝜆_{1}𝑦_{21}^{}+𝜆_{2}𝑦_{22}^{}+⋯+𝜆_{𝑛}𝑦_{2𝑛}^{} \\ & ≤𝜆_{max}\,𝑦_{21}^{}+𝜆_{max}\,𝑦_{22}^{}+⋯+𝜆_{max}\,𝑦_{2𝑛}^{} \\ & =𝜆_{max}(𝑦_{21}^{}+𝑦_{22}^{}+⋯+𝑦_{2𝑛}^{}) \\ & =𝜆_{max}\,‖𝐲‖^{2} \\ & =𝜆_{max}.\end{aligned}


$$

So, we have that that

$$


M = \max \{ Q(\mathbf{x}) \: | \: \| \mathbf{x} \| = 1 \} = \max \{ Q'(\mathbf{y}) \: | \: \| \mathbf{y} \| = 1 \} \le \lambda_{\textrm{max}}.


$$

On the other hand, if we take $[\begin{aligned}1 & 0 & … & 0\end{aligned}]$ then $Q(P\mathbf{e}_1) = Q'(\mathbf{e}_1) = \lambda_{\textrm{max}}.$ So, we conclude that $M = \lambda_{\textrm{max}}.$

Finally, since $\mathbf{u}_1 = P\mathbf{e}_1$ we have that $Q(\mathbf u_1) = \mathbf e_1^T D \mathbf e_1 = \lambda_{\textrm{max}}.$ Therefore, the maximum value is attained at $\mathbf u_{\textrm{max}}.$
