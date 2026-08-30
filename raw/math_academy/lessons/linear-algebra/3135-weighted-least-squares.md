# Weighted Least-Squares

Source: https://www.mathacademy.com/topics/3135?courseId=55
Topic ID: 3135

## Prerequisites

- [The Least-Squares Solution of a Linear System (With Collinearity)](./2167-the-least-squares-solution-of-a-linear-system-with-collinearity.md)

## Lesson

### Introduction

Let's consider the least-squares problem $A\mathbf{x}=\mathbf{b},$ where

$$


\begin{aligned}1 & −1 \\ 1 & 0 \\ 2 & −1\end{aligned}


$$

Recall that the corresponding least-squares solution is a vector ${\hat{\mathbf{x}}}$ such that

$$


\Vert A{\hat{\mathbf{x}}} - \mathbf{b} \Vert


$$

is as small as possible.

In real-world problems, the coefficients stored in $A$ might come from sources that are not equally reliable. For example, the coefficients might be collected from population surveys with different sample sizes. As a result, we might want to assign a greater "weight" to the more reliable data.

For example, suppose we require the weight of the coefficients in the first row to be twice the weights of the other rows. Then, we can re-state our problem by saying that, for the matrix of weights $W,$ given by

$$


\begin{aligned}2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}


$$

we wish to find vectors ${\hat{\mathbf{x}}}$ such that

$$


\Vert W (A{\hat{\mathbf{x}}} - \mathbf{b}) \Vert


$$

is as small as possible.

Therefore, instead of solving $A\mathbf x = \mathbf{b},$ we now need to solve the least-squares problem

$$


W\!A\mathbf x = W\mathbf{b}.


$$

To get the normal equation corresponding to this least-squares problem, we pre-multiply both sides of the equation by $(W\!A)^T{:}$

$$


\begin{aligned}(𝑊\,𝐴)^{𝑇}⋅𝑊\,𝐴𝐱 & =(𝑊\,𝐴)^{𝑇}⋅𝑊𝐛 \\ 𝐴^{𝑇}(𝑊^{𝑇}𝑊)𝐴𝐱 & =𝐴^{𝑇}(𝑊^{𝑇}𝑊)𝐛\end{aligned}


$$

Now, since

$$


\begin{aligned}2^{2} & 0 & 0 \\ 0 & 1^{2} & 0 \\ 0 & 0 & 1^{2}\end{aligned}


$$

the normal equation can be written as follows:

$$


\begin{aligned}[\begin{aligned}1 & 1 & 2 \\ −1 & 0 & −1\end{aligned}]\begin{aligned}4 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}\begin{aligned}1 & −1 \\ 1 & 0 \\ 2 & −1\end{aligned}[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}1 & 1 & 2 \\ −1 & 0 & −1\end{aligned}]\begin{aligned}4 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{aligned}\begin{aligned}9 \\ 0 \\ 18\end{aligned} \\ [\begin{aligned}1 & 1 & 2 \\ −1 & 0 & −1\end{aligned}]\begin{aligned}4 & −4 \\ 1 & 0 \\ 2 & −1\end{aligned}[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}1 & 1 & 2 \\ −1 & 0 & −1\end{aligned}]\begin{aligned}36 \\ 0 \\ 18\end{aligned} \\ [\begin{aligned}9 & −6 \\ −6 & 5\end{aligned}][\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}72 \\ −54\end{aligned}]\end{aligned}


$$

Solving the final equation, we obtain the least-squares solution $[\begin{aligned}4 \\ −6\end{aligned}]$

### Example: Finding the Normal Equation for a Weighted Least-Squares Problem

#### Question

$$


\begin{aligned}1 & 0 \\ 0 & 1 \\ 1 & 2\end{aligned}


$$

Consider the matrices $A$ and $W,$ and the vector $\mathbf{b}$ above. If the normal equation for the corresponding weighted least-squares problem $W\!A \mathbf{x} = W\mathbf{b}$ is given by

$$


[\begin{aligned}𝑎 & 18 \\ 18 & 𝑏\end{aligned}]


$$

what is the value of $a+b+c?$

#### Explanation

To get the normal equation corresponding to $W\!A\mathbf{x}=W\mathbf{b},$ we pre-multiply both sides of the equation by $(W\!A)^T{:}$

$$


\begin{aligned}(𝑊\,𝐴)^{𝑇}⋅𝑊\,𝐴𝐱 & =(𝑊\,𝐴)^{𝑇}⋅𝑊𝐛 \\ 𝐴^{𝑇}(𝑊^{𝑇}𝑊)𝐴𝐱 & =𝐴^{𝑇}(𝑊^{𝑇}𝑊)𝐛\end{aligned}


$$

Now, since

$$


\begin{aligned}1^{2} & 0 & 0 \\ 0 & 2^{2} & 0 \\ 0 & 0 & 3^{2}\end{aligned}


$$

our normal equation can be written as follows:

$$


\begin{aligned}[\begin{aligned}1 & 0 & 1 \\ 0 & 1 & 2\end{aligned}]\begin{aligned}1 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 9\end{aligned}\begin{aligned}1 & 0 \\ 0 & 1 \\ 1 & 2\end{aligned}[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}1 & 0 & 1 \\ 0 & 1 & 2\end{aligned}]\begin{aligned}1 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 9\end{aligned}\begin{aligned}2 \\ 0 \\ 3\end{aligned} \\ [\begin{aligned}1 & 0 & 1 \\ 0 & 1 & 2\end{aligned}]\begin{aligned}1 & 0 \\ 0 & 4 \\ 9 & 18\end{aligned}[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}1 & 0 & 1 \\ 0 & 1 & 2\end{aligned}]\begin{aligned}2 \\ 0 \\ 27\end{aligned} \\ [\begin{aligned}10 & 18 \\ 18 & 40\end{aligned}][\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}29 \\ 54\end{aligned}]\end{aligned}


$$

Therefore, we have

$$


a+b+c=10+40+54 = 104.


$$

### Example: Finding the Solution to a Weighted Least-Squares Problem

#### Question

$$


\begin{aligned}1 & −1 \\ −2 & 2 \\ −1 & 1\end{aligned}


$$

Consider the matrices $A$ and $W,$ and the vector $\mathbf{b}$ shown above. Find the general solution for the weighted least-squares problem $W\!A\mathbf{x}=W\mathbf{b}.$

#### Explanation

To get the normal equation corresponding to $W\!A\mathbf{x}=W\mathbf{b},$ we pre-multiply both sides of the equation by $(W\!A)^T{:}$

$$


\begin{aligned}(𝑊\,𝐴)^{𝑇}⋅𝑊\,𝐴𝐱 & =(𝑊\,𝐴)^{𝑇}⋅𝑊𝐛 \\ 𝐴^{𝑇}(𝑊^{𝑇}𝑊)𝐴𝐱 & =𝐴^{𝑇}(𝑊^{𝑇}𝑊)𝐛\end{aligned}


$$

Now, since

$$


\begin{aligned}1^{2} & 0 & 0 \\ 0 & 2^{2} & 0 \\ 0 & 0 & 2^{2}\end{aligned}


$$

our normal equation can be written as follows:

$$


\begin{aligned}[\begin{aligned}1 & −2 & −1 \\ −1 & 2 & 1\end{aligned}]\begin{aligned}1 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4\end{aligned}\begin{aligned}1 & −1 \\ −2 & 2 \\ −1 & 1\end{aligned}[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}1 & −2 & −1 \\ −1 & 2 & 1\end{aligned}]\begin{aligned}1 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 4\end{aligned}\begin{aligned}−3 \\ 0 \\ 9\end{aligned} \\ [\begin{aligned}1 & −2 & −1 \\ −1 & 2 & 1\end{aligned}]\begin{aligned}1 & −1 \\ −8 & 8 \\ −4 & 4\end{aligned}[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}1 & −2 & −1 \\ −1 & 2 & 1\end{aligned}]\begin{aligned}−3 \\ 0 \\ 36\end{aligned} \\ [\begin{aligned}21 & −21 \\ −21 & 21\end{aligned}][\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}−39 \\ 39\end{aligned}]\end{aligned}


$$

Now, we solve the system corresponding to the above matrix equation using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{aligned}21 & −21 & −39 \\ −21 & 21 & 39\end{aligned}] & 𝑅_{2}:=𝑅_{2}+𝑅_{1} \\ & ∼[\begin{aligned}21 & −21 & −39 \\ 0 & 0 & 0\end{aligned}] & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). Thus, $x_2$ is a free variable. From the first equation, we have

$$


x_1=-\dfrac{13}{7}+x_2.


$$

Hence, the general solution is

$$


\begin{aligned}−\frac{13}{7}+𝑥_{2} \\ 𝑥_{2}\end{aligned}


$$

### A Geometric Interpretation of the Weighted Least-Squares Solution

Recall that if the solution ${\hat{\mathbf{x}}}$ of the least-squares problem $A\mathbf x=\mathbf{b}$ is unique, then $A{\hat{\mathbf{x}}}$ lies in $\textrm{Col}(A).$ Furthermore, $A{\hat{\mathbf{x}}}$ is the vector in $\textrm{Col}(A)$ that's closest to $\mathbf b.$

In terms of vector spaces, the vector $A{\hat{\mathbf{x}}}$ is the orthogonal projection of $\mathbf{b}$ onto the subspace spanned by the columns of $A.$ Therefore, the error vector $A{\hat{\mathbf{x}}} - \mathbf{b}$ is orthogonal to $\textrm{Col}(A).$

![Instructional graphic](../../lesson-assets/linear-algebra/topic-3135/75a21e631ad67f07.png)

A similar property holds for weighted least-squares solutions:

*If the solution ${\hat{\mathbf{x}}}$ of the least-squares problem $W\!A\mathbf x=W\mathbf{b}$ is unique, then $A{\hat{\mathbf{x}}} - \mathbf{b}$ is orthogonal to $\textrm{Col}(A)$ with respect to the weighted dot product defined as where the $w_i$'s are the weights from the main diagonal of the weight matrix $W.$*

We previously considered the weighted least-squares problem $W\!Ax=W\mathbf{b},$ where

$$


\begin{aligned}1 & −1 \\ 1 & 0 \\ 2 & −1\end{aligned}


$$

It's easy to show (using the usual techniques) that the unique weighted least-squares solution is given by

$$


[\begin{aligned}4 \\ −6\end{aligned}]


$$

Computing our error vector $\boldsymbol{\varepsilon} = A{\hat{\mathbf{x}}} - \mathbf{b},$ we get

$$


\begin{aligned}𝜺 & =𝐴\overset{𝐱}{^}−𝐛 \\ & =\begin{aligned}1 & −1 \\ 1 & 0 \\ 2 & −1\end{aligned}⋅[\begin{aligned}4 \\ −6\end{aligned}]−\begin{aligned}9 \\ 0 \\ 18\end{aligned} \\ & =\begin{aligned}10 \\ 4 \\ 14\end{aligned}−\begin{aligned}9 \\ 0 \\ 18\end{aligned} \\ & =\begin{aligned}1 \\ 4 \\ −4\end{aligned}.\end{aligned}


$$

Now, let $\mathbf a_1$ and $\mathbf a_2$ denote the columns of $A\mathbin{:}$

$$


\begin{aligned}| & | \\ 𝐚_{1} & 𝐚_{𝟐} \\ | & |\end{aligned}


$$

Notice that the error vector $\boldsymbol{\varepsilon}$ is *not* orthogonal to the columns of $A\mathbin{:}$

- Computing $\boldsymbol{\varepsilon} \cdot \mathbf a_1,$ we have

- Computing $\boldsymbol{\varepsilon} \cdot \mathbf a_2,$ we have

However, if we check the orthogonality with respect to the *weighted* dot product

$$


\langle \mathbf{x}, \mathbf{y} \rangle_W = \sum_{i=1}^n w_i^2 x_i y_i = 4x_1y_1 + x_2y_2 + x_3y_3, \quad


$$

we obtain the following:

$$


\begin{aligned}⟨𝜺,𝐚_{1}⟩_{𝑊} & =⟨\begin{aligned}1 \\ 4 \\ −4\end{aligned},\begin{aligned}1 \\ 1 \\ 2\end{aligned}⟩_{𝑊} \\ & =4(1)(1)+(4)(1)+(−4)(2) \\ & =0\,✓ \\ ⟨𝜺,𝐚_{2}⟩_{𝑊} & =⟨\begin{aligned}1 \\ 4 \\ −4\end{aligned},\begin{aligned}−1 \\ 0 \\ −1\end{aligned}⟩_{𝑊} \\ & =4(1)(−1)+(4)(0)+(−4)(−1) \\ & =0\,✓\end{aligned}


$$

This means that $A{\hat{\mathbf{x}}} - \mathbf{b}$ is orthogonal to $\textrm{Col}(A)$ with respect to the weighted dot product. We can write this as

$$


A{\hat{\mathbf{x}}} - \mathbf{b} \perp_W \textrm{Col}(A).


$$

In terms of vector spaces, the vector $A{\hat{\mathbf{x}}}$ is the orthogonal projection with respect to $\langle \mathbf{x}, \mathbf{y} \rangle_W$ of the vector $\mathbf{b}$ onto the subspace spanned by the columns of $A.$

Furthermore, the weighted least-squares problem with weight matrix $W$ is equivalent to finding a vector ${\hat{\mathbf{x}}}$ such that

$$


\Vert A{\hat{\mathbf{x}}} - \mathbf{b} \Vert_W


$$

is as small as possible.
