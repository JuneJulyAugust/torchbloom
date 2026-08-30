# Matrix Gradients

Source: https://www.mathacademy.com/topics/5869?courseId=145
Topic ID: 5869

## Prerequisites

- [Further Vector Gradients](./6007-further-vector-gradients.md)

## Lesson

### Introduction

In previous lessons, we defined the gradient of a scalar-valued function with respect to a vector. In this lesson, we extend this idea to functions where the input is a *matrix* and the output is a scalar.

Suppose we have a function $f: \mathbb{R}^{m \times n} \to \mathbb{R}$ that maps a matrix $A \in \mathbb{R}^{m \times n}$ to a scalar value $f(A)$. Just like with vector inputs, we define the **gradient of $f$ with respect to $A$** as the matrix of partial derivatives of $f$ with respect to each individual entry of $A{:}$

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑎_{11}} & \frac{𝜕𝑓}{𝜕𝑎_{12}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑎_{1𝑛}} \\ \frac{𝜕𝑓}{𝜕𝑎_{21}} & \frac{𝜕𝑓}{𝜕𝑎_{22}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑎_{2𝑛}} \\ ⋮ & ⋮ & ⋱ & ⋮ \\ \frac{𝜕𝑓}{𝜕𝑎_{𝑚1}} & \frac{𝜕𝑓}{𝜕𝑎_{𝑚2}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑎_{𝑚𝑛}}\end{aligned}


$$

This gradient has the same shape as the matrix $A.$ It tells us how sensitive the output $f(A)$ is to changes in each element $a_{ij}$.

Let’s apply this to a concrete example. Suppose we define the function

$$


f(X) = \ln(\det(X))


$$

for a square matrix $X \in \mathbb{R}^{2 \times 2}$. Let's find the gradient of $f$ with respect to $X$ and evaluate it at a specific point.

First, we write the matrix $X$ as

$$


[\begin{aligned}𝑥_{11} & 𝑥_{12} \\ 𝑥_{21} & 𝑥_{22}\end{aligned}]


$$

Then, the determinant of $X$ is

$$


\det(X) = x_{11}x_{22} - x_{12}x_{21}.


$$

So, the function becomes

$$


f(X) = \ln(x_{11}x_{22} - x_{12}x_{21}).


$$

To find the gradient, we differentiate $f$ with respect to each element of $X.$ This gives

$$


\begin{aligned}∇_{𝑋}𝑓(𝑋) & =\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{11}} & \frac{𝜕𝑓}{𝜕𝑥_{12}} \\ \frac{𝜕𝑓}{𝜕𝑥_{21}} & \frac{𝜕𝑓}{𝜕𝑥_{22}}\end{aligned} \\ & =\begin{aligned}\frac{𝜕}{𝜕𝑥_{11}}(ln⁡(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})) & \frac{𝜕}{𝜕𝑥_{12}}(ln⁡(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})) \\ \frac{𝜕}{𝜕𝑥_{21}}(ln⁡(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})) & \frac{𝜕}{𝜕𝑥_{22}}(ln⁡(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21}))\end{aligned} \\ & =\begin{aligned}\frac{𝑥_{22}}{𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21}} & −\frac{𝑥_{21}}{𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21}} \\ −\frac{𝑥_{12}}{𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21}} & \frac{𝑥_{11}}{𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21}}\end{aligned} \\ & =\frac{1}{𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21}}[\begin{aligned}𝑥_{22} & −𝑥_{21} \\ −𝑥_{12} & 𝑥_{11}\end{aligned}] \\ & =\frac{1}{det(𝑋)}[\begin{aligned}𝑥_{22} & −𝑥_{21} \\ −𝑥_{12} & 𝑥_{11}\end{aligned}].\end{aligned}


$$

Now, suppose we wish to evaluate this gradient at

$$


[\begin{aligned}3 & 1 \\ 5 & −2\end{aligned}]


$$

First, we compute the determinant:

$$


\begin{aligned}det(𝑋) & =3⋅(−2)−1⋅5 \\ & =−6−5 \\ & =−11\end{aligned}


$$

Then, we substitute our values into our gradient. This gives

$$


\begin{aligned}∇_{𝑋}𝑓(𝑋) & =−\frac{1}{11}[\begin{aligned}−2 & −5 \\ −1 & 3\end{aligned}] \\ & =\frac{1}{11}[\begin{aligned}2 & 5 \\ 1 & −3\end{aligned}].\end{aligned}


$$

This result tells us how the scalar output $f(X) = \ln(\det(X))$ would change with respect to small changes in each entry of the matrix $X$. Each element in the gradient matrix captures that local rate of change.

### Example: Computing the Gradient of a Function With Respect to a Matrix

#### Question

Consider the function $f: \mathbb{R}^{2 \times 2} \rightarrow \mathbb{R}$ defined by

$$


f(X) = (\det(X))^2.


$$

What is the gradient of $f$ with respect to $X$ at $\begin{aligned}−\frac{1}{2} & \frac{3}{2} \\ −4 & 10\end{aligned}$

#### Explanation

The gradient of a function $f: \mathbb{R}^{m \times n} \rightarrow \mathbb{R}$ with respect to a matrix $X \in \mathbb{R}^{m \times n}$ is

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{11}} & \frac{𝜕𝑓}{𝜕𝑥_{12}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑥_{1𝑛}} \\ \frac{𝜕𝑓}{𝜕𝑥_{21}} & \frac{𝜕𝑓}{𝜕𝑥_{22}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑥_{2𝑛}} \\ ⋮ & ⋮ & ⋱ & ⋮ \\ \frac{𝜕𝑓}{𝜕𝑥_{𝑚1}} & \frac{𝜕𝑓}{𝜕𝑥_{𝑚2}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑥_{𝑚𝑛}}\end{aligned}


$$

In our case, writing out the function $f(X)$ where $[\begin{aligned}𝑥_{11} & 𝑥_{12} \\ 𝑥_{21} & 𝑥_{22}\end{aligned}]$, we get

$$


f(X) = (\det(X))^2 = (x_{11}x_{22} - x_{12}x_{21})^2.


$$

So, the gradient is

$$


\begin{aligned}\,\,\,∇_{𝑋}𝑓(𝑋) & =\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{11}} & \frac{𝜕𝑓}{𝜕𝑥_{12}} \\ \frac{𝜕𝑓}{𝜕𝑥_{21}} & \frac{𝜕𝑓}{𝜕𝑥_{22}}\end{aligned} \\ & =\begin{aligned}\frac{𝜕}{𝜕𝑥_{11}}(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})^{2} & \frac{𝜕}{𝜕𝑥_{12}}(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})^{2} \\ \frac{𝜕}{𝜕𝑥_{21}}(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})^{2} & \frac{𝜕}{𝜕𝑥_{22}}(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})^{2}\end{aligned} \\ & =[\begin{aligned}2(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})⋅𝑥_{22} & 2(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})⋅(−𝑥_{21}) \\ 2(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})⋅(−𝑥_{12}) & 2(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})⋅𝑥_{11}\end{aligned}] \\ & =2(𝑥_{11}𝑥_{22}−𝑥_{12}𝑥_{21})[\begin{aligned}𝑥_{22} & −𝑥_{21} \\ −𝑥_{12} & 𝑥_{11}\end{aligned}] \\ & =2det(𝑋)[\begin{aligned}𝑥_{22} & −𝑥_{21} \\ −𝑥_{12} & 𝑥_{11}\end{aligned}].\end{aligned}


$$

Evaluating at $\begin{aligned}−\frac{1}{2} & \frac{3}{2} \\ −4 & 10\end{aligned}$ we get

$$


\begin{aligned}∇_{𝑋}𝑓(𝑋) & =2(−\frac{1}{2}⋅10−(−4)⋅\frac{3}{2})\begin{aligned}10 & 4 \\ −\frac{3}{2} & −\frac{1}{2}\end{aligned} \\ & =2(−5−(−6))\begin{aligned}10 & 4 \\ −\frac{3}{2} & −\frac{1}{2}\end{aligned} \\ & =[\begin{aligned}20 & 8 \\ −3 & −1\end{aligned}].\end{aligned}


$$

### Component-Wise Differentiation

Suppose we have a scalar-valued function defined by

$$


f = \mathbf{y}^T A \mathbf{x},


$$

where $\mathbf{y} \in \mathbb{R}^m$, $\mathbf{x} \in \mathbb{R}^n$, and $A \in \mathbb{R}^{m \times n}$.

We want to compute the gradient of $f$ with respect to the matrix $A$. The result turns out to be

$$


\nabla_A f = \mathbf{y} \cdot \mathbf{x}^T.


$$

Let’s verify this by working component-wise.

First, note that we can write the product $\mathbf y^T A \mathbf x$ as a double summation as follows:

$$


f = \mathbf y^T A \mathbf x = \sum_{k=1}^m \sum_{l=1}^n y_k A_{kl} x_l.


$$

In a previous lesson, we saw how to do this for $\mathbf x^T A \mathbf x$. The idea here is similar.

Now, we differentiate this summation with respect to $A_{ij}{:}$

$$


\frac{\partial f}{\partial A_{ij}} = \frac{\partial}{\partial A_{ij}} \left( \sum_{k=1}^m \sum_{l=1}^n y_k A_{kl} x_l \right)


$$

Since only the term where $k = i$ and $l = j$ depends on $A_{ij}$, all other terms vanish. So, we get

$$


\frac{\partial f}{\partial A_{ij}} = y_i x_j.


$$

This tells us that the entry in the $i$th row and $j$th column of the gradient matrix is $y_i x_j$. Hence, the full gradient matrix is

$$


\nabla_A f = \mathbf{y} \cdot \mathbf{x}^T.


$$

This result is an example of an outer product. The gradient of $\mathbf{y}^T A \mathbf{x}$ with respect to the matrix $A$ is given by multiplying the column vector $\mathbf{y}$ by the row vector $\mathbf{x}^T$, resulting in a matrix of the same shape as $A$.

Let’s look at a few examples to see this in action.

### Example: Computing the Gradient of a Function Component-Wise

#### Question

Consider the function $L: \mathbb{R}^{2 \times 3} \rightarrow \mathbb{R}$ defined by $L(\mathbf{A}) = \mathbf{y}^T\mathbf{A}\mathbf{x}$ where

$$


\begin{aligned}1 \\ 2 \\ 3\end{aligned}


$$

What is $\nabla_{\mathbf{A}} L$ at $[\begin{aligned}2 & 1 & 0 \\ −1 & 4 & 3\end{aligned}]$

#### Explanation

The gradient of $L$ with respect to $\mathbf{A}$ is a matrix of the same shape as $\mathbf{A}$, with $(i,j)$th entry given by

$$


\dfrac{\partial L}{\partial a_{ij}},


$$

the partial derivative of $L$ with respect to the $(i,j)$th entry of $\mathbf{A}.$

Writing out $L$ in component-wise notation as

$$


L = \sum\limits_{i=1}^2 \sum\limits_{j=1}^3 a_{ij} y_i x_j,


$$

we have

$$


\dfrac{\partial L}{\partial a_{ij}} = y_i x_j.


$$

Thus, $\nabla_{\mathbf{A}} L = \mathbf{y} \cdot \mathbf{x}^T.$

Evaluating at the given values $\begin{aligned}1 \\ 2 \\ 3\end{aligned}$ and $[\begin{aligned}4 \\ 5\end{aligned}]$ we get

$$


[\begin{aligned}4 \\ 5\end{aligned}]


$$

### Differentiation Using the Multivariable Chain Rule

When working with scalar-valued functions defined on matrices, it's often helpful to compute gradients using component-wise differentiation and the chain rule. This approach breaks down the computation into simpler intermediate steps and allows us to clearly see the dependencies.

Consider a *scalar* function $L(\mathbf A),$ defined as

$$


L(\mathbf{A}) = \frac{1}{2} \left( \mathbf{A}\mathbf{x} - \mathbf{b} \right)^T \left( \mathbf{A}\mathbf{x} - \mathbf{b} \right)


$$

where $\mathbf{A} \in \mathbb{R}^{2 \times 3}$, $\mathbf{x} \in \mathbb{R}^3$, and $\mathbf{b} \in \mathbb{R}^2.$

Suppose we want to compute the gradient $\nabla_{\mathbf{A}} L$, which is a matrix of the same shape as $\mathbf{A}$. The entry in the $i$th row and $j$th column of the gradient matrix is given by

$$


\dfrac{\partial L}{\partial a_{ij}}.


$$

To simplify the differentiation, we define $\mathbf y \in\mathbb R^{2\times 1}$ as

$$


[\begin{aligned}𝑦_{1} \\ 𝑦_{2}\end{aligned}]


$$

Then, we can write $L$ in terms of $\mathbf y$ as

$$


L = \frac{1}{2} \mathbf{y}^T \mathbf{y}.


$$

To compute $\dfrac{\partial L}{\partial a_{ij}}$, we apply the multivariable chain rule:

$$


\frac{\partial L}{\partial a_{ij}} = \sum_{k=1}^2 \frac{\partial L}{\partial y_k} \cdot \frac{\partial y_k}{\partial a_{ij}}


$$

Note that the summation is from $k=1$ to $k=2$ because $\mathbf y$ has two components, and we're differentiating with respect to each of them.

Now, let's analyze the two factors of the product that appear in this summation.

- We know that Therefore, we have

- Writing $\mathbf{y} = \mathbf{A} \mathbf{x} - \mathbf{b}$ in component form we have Only the $k$th row of $\mathbf{A}$ affects $y_k$.

Putting our two results together gives

$$


\begin{aligned}\frac{𝜕𝐿}{𝜕𝑎_{𝑖𝑗}} & =\underset{\underset{𝑘=1}{∑}}{\overset{}{2}}\frac{𝜕𝐿}{𝜕𝑦_{𝑘}}⋅\frac{𝜕𝑦_{𝑘}}{𝜕𝑎_{𝑖𝑗}} \\ & =\frac{𝜕𝐿}{𝜕𝑦_{𝑖}}⋅\frac{𝜕𝑦_{𝑖}}{𝜕𝑎_{𝑖𝑗}} \\ & =𝑦_{𝑖}𝑥_{𝑗},\end{aligned}


$$

because all terms vanish except the one where $k=i$.

Therefore, we conclude that

$$


\nabla_{\mathbf{A}} L = \mathbf{y} \cdot \mathbf{x}^T.


$$

In the next example, we will use this formula to compute the gradient for specific vectors.

### Example: Applying the Chain Rule to Calculate Gradients

#### Question

Consider the function $L: \mathbb{R}^{2 \times 3} \rightarrow \mathbb{R}$ defined by $L(\mathbf{A}) = \dfrac{1}{2}(\mathbf{A}\mathbf{x} - \mathbf{b})^T(\mathbf{A}\mathbf{x} - \mathbf{b}),$ where

$$


\begin{aligned}1 \\ 2 \\ 3\end{aligned}


$$

What is $\nabla_{\mathbf{A}} L$ at $[\begin{aligned}1 & 0 & 2 \\ 0 & 1 & 1\end{aligned}]$

#### Explanation

The gradient of $L$ with respect to $\mathbf{A}$ is a matrix of the same shape as $\mathbf{A}$, with $(i,j)$th entry given by

$$


\dfrac{\partial L}{\partial a_{ij}},


$$

the partial derivative of $L$ with respect to the $(i,j)$th entry of $\mathbf{A}.$

We can compute $\dfrac{\partial L}{\partial a_{ij}}$ by applying the chain rule.

Let $\mathbf{y} = \mathbf{A}\mathbf{x} - \mathbf{b} \in \mathbb{R}^2.$ Then, $L(\mathbf{A}) = \dfrac{1}{2}\mathbf{y}^T\mathbf{y}$ and

$$


\dfrac{\partial L}{\partial a_{ij}} = \sum_{k=1}^2 \dfrac{\partial L}{\partial y_k} \cdot \dfrac{\partial y_k}{\partial a_{ij}}


$$

Now, since

$$


\nabla_{\mathbf{y}} L = \nabla_{\mathbf{y}} \bigg( \dfrac{1}{2}\mathbf{y}^T\mathbf{y} \bigg) = \mathbf{y},


$$

we have that

$$


\dfrac{\partial L}{\partial y_k} = y_k.


$$

Writing out $\mathbf{y} = \mathbf{A}\mathbf{x} - \mathbf{b}$ in component-wise notation as

$$


y_i = \sum\limits_{j=1}^3 (a_{ij} x_j - b_i),


$$

we have

- $\dfrac{\partial y_k}{\partial a_{ij}} = x_j$ if $i = k$, and

- $\dfrac{\partial y_k}{\partial a_{ij}} = 0$ if $i \neq k.$

This means that

$$


\begin{aligned}\frac{𝜕𝐿}{𝜕𝑎_{𝑖𝑗}} & =\underset{\underset{𝑘=1}{∑}}{\overset{}{2}}\frac{𝜕𝐿}{𝜕𝑦_{𝑘}}⋅\frac{𝜕𝑦_{𝑘}}{𝜕𝑎_{𝑖𝑗}} \\ & =\frac{𝜕𝐿}{𝜕𝑦_{𝑖}}⋅\frac{𝜕𝑦_{𝑖}}{𝜕𝑎_{𝑖𝑗}} \\ & =𝑦_{𝑖}⋅\frac{𝜕𝑦_{𝑖}}{𝜕𝑎_{𝑖𝑗}} \\ & =𝑦_{𝑖}𝑥_{𝑗}.\end{aligned}


$$

The $(i,j)$th entry of $\nabla_{\mathbf{A}} L$ is the $i$th entry of $\mathbf{y}$ multiplied by the $j$th entry of $\mathbf{x}$, so

$$


\nabla_{\mathbf{A}} L = \mathbf{y} \cdot \mathbf{x}^T.


$$

Finally, evaluating $\nabla_{\mathbf{A}} L$ at $\begin{aligned}1 \\ 2 \\ 3\end{aligned}$ we get

$$


\begin{aligned}∇_{𝐀}𝐿 & =𝐲⋅𝐱^{𝑇} \\ & =(𝐀𝐱−𝐛)⋅𝐱^{𝑇} \\ & =[\begin{aligned}1 & 0 & 2 \\ 0 & 1 & 1\end{aligned}]\begin{aligned}1 \\ 2 \\ 3\end{aligned}−[\begin{aligned}4 \\ 5\end{aligned}]⋅[\begin{aligned}1 & 2 & 3\end{aligned}] \\ & =([\begin{aligned}7 \\ 5\end{aligned}]−[\begin{aligned}4 \\ 5\end{aligned}])⋅[\begin{aligned}1 & 2 & 3\end{aligned}] \\ & =[\begin{aligned}3 \\ 0\end{aligned}]⋅[\begin{aligned}1 & 2 & 3\end{aligned}] \\ & =[\begin{aligned}3 & 6 & 9 \\ 0 & 0 & 0\end{aligned}].\end{aligned}


$$
