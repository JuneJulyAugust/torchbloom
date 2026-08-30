# Linear Transformations of Points and Lines in the Plane

Source: https://www.mathacademy.com/topics/2706?courseId=136
Topic ID: 2706

## Prerequisites

- [Introduction to the Inverse of a Matrix](./863-introduction-to-the-inverse-of-a-matrix.md)
- [The Standard Matrix of a Linear Transformation](./1959-the-standard-matrix-of-a-linear-transformation.md)
- [Properties of Lines Given in Standard Form](../algebra-i/3725-properties-of-lines-given-in-standard-form.md)

## Lesson

### Introduction

Consider the linear transformation $\mathbf T$ with matrix representation $T,$ given by

$$


[\begin{aligned}−2 & 1 \\ 0 & −2\end{aligned}]


$$

Given a point $A(1,1),$ let $A'$ be the image of $A$ under the action of $\mathbf T.$ How can we find the coordinates of $A'?$

First, we create a column vector $\mathbf{x}$ containing the coordinates of $A{:}$

$$


[\begin{aligned}1 \\ 1\end{aligned}]


$$

Now, we compute the image of $\mathbf{x}$ under the action of $\mathbf T$ by calculating the matrix product $T\mathbf{x}\mathbin{:}$

$$


\begin{aligned}𝑇𝐱 & =[\begin{aligned}−2 & 1 \\ 0 & −2\end{aligned}][\begin{aligned}1 \\ 1\end{aligned}] \\ & =[\begin{aligned}−1 \\ −2\end{aligned}]\end{aligned}


$$

The result, $T \mathbf{x},$ contains the coordinates of $A'.$ Therefore, $A'(-1,-2).$

### Example: Computing the Image of a Point Under a Linear Transformation of a Plane

#### Question

Consider the linear transformation $\mathbf T$ with matrix representation $T,$ given by

$$


[\begin{aligned}3 & 1 \\ −4 & −1\end{aligned}]


$$

What are the coordinates of the point $B',$ the image of $B(2,-3)$ under the action of $\mathbf T?$

#### Explanation

To find the image of $B$ under the action of $\mathbf T,$ we first create a column vector $\mathbf{x}$ containing the coordinates of $B{:}$

$$


[\begin{aligned}2 \\ −3\end{aligned}]


$$

Now, we compute the image of $\mathbf{x}$ under the action of $\mathbf T$ by calculating the matrix product $T\mathbf{x}\mathbin{:}$

$$


\begin{aligned}𝑇𝐱 & =[\begin{aligned}3 & 1 \\ −4 & −1\end{aligned}][\begin{aligned}2 \\ −3\end{aligned}] \\ & =[\begin{aligned}3 \\ −5\end{aligned}].\end{aligned}


$$

The result, $T \mathbf{x},$ contains the coordinates of $B'.$ Therefore, $B'(3,-5).$

### The Image of a Line Under the Action of a Linear Transformation

Linear transformations of a plane have the following important property:

*A non-singular linear transformation in the plane maps a straight line into a straight line.*

Therefore, to find the image of a line $l$ under the action of a linear transformation $\mathbf{T}$ (represented by its standard matrix $T$), we do the following:

1. Find two distinct points $A$ and $B$ that lie on the line $l.$

2. Compute the images $A'$ and $B'$ of the points $A$ and $B$ under the action of $\mathbf{T}.$

3. Write down the equation of the line that passes through $A'$ and $B'.$

### Example: Computing the Image of a Line Given by an Equation in Slope-Intercept Form

#### Question

Consider the line $y=3x-2$ and linear transformation $\mathbf T$ with matrix representation $T,$ given by

$$


[\begin{aligned}−1 & 0 \\ 3 & 1\end{aligned}]


$$

What is the equation of the image of the line under the action of $\mathbf T?$

#### Explanation

First, let's find two points on the given line. Substituting $x=0$ and $x=1,$ we get

$$


\begin{aligned}𝑥=0\, & →\,𝑦=3(0)−2=−2, \\ 𝑥=1\, & →\,𝑦=3(1)−2=1.\end{aligned}


$$

So we have two points on the line, $P(0,-2)$ and $Q(1,1).$

To find the images of $P$ and $Q$ under the action of $\mathbf T,$ we first create a matrix $X$ containing the coordinates of $P$ and $Q$ in its columns:

$$


[\begin{aligned}0 & 1 \\ −2 & 1\end{aligned}]


$$

Now, we compute the image of $X$ under the action of $\mathbf T$ by calculating the matrix product $TX\mathbin{:}$

$$


\begin{aligned}𝑇𝑋 & =[\begin{aligned}−1 & 0 \\ 3 & 1\end{aligned}][\begin{aligned}0 & 1 \\ −2 & 1\end{aligned}] \\ & =[\begin{aligned}0 & −1 \\ −2 & 4\end{aligned}]\end{aligned}


$$

Therefore, the coordinates of the respective image points are $P'(0,-2)$ and $Q'(-1,4).$

Finally, we write the equation of the line that passes through $P'$ and $Q'\mathbin{:}$

$$


\begin{aligned}𝑦−𝑦_{1} & =\frac{𝑦_{2}−𝑦_{1}}{𝑥_{2}−𝑥_{1}}(𝑥−𝑥_{1}) \\ 𝑦−(−2) & =\frac{4−(−2)}{−1−0}(𝑥−0) \\ 𝑦+2 & =−6𝑥 \\ 6𝑥+𝑦+2 & =0\end{aligned}


$$

### Example: Computing the Image of a Line Given by an Equation in Standard Form

#### Question

Consider the line $5x-y-3=0$ and linear transformation $\mathbf T$ with matrix representation $T,$ given by

$$


[\begin{aligned}−3 & 1 \\ −1 & 2\end{aligned}]


$$

What is the equation of the image of the line under the action of $\mathbf T?$

#### Explanation

First, let's find two points on the given line. Solving for $y,$ we get $y=5x-3,$ and substituting $x=0$ and $x=1,$ we get

$$


\begin{aligned}𝑥=0\, & →\,𝑦=5(0)−3=−3, \\ 𝑥=1\, & →\,𝑦=5(1)−3=2.\end{aligned}


$$

So we have two points on the line, $P(0,-3)$ and $Q(1,2).$

To find the images of $P$ and $Q$ under the action of $\mathbf T,$ we first create a matrix $X$ containing the coordinates of $P$ and $Q$ in its columns:

$$


[\begin{aligned}0 & 1 \\ −3 & 2\end{aligned}]


$$

Now, we compute the image of $X$ under the action of $\mathbf T$ by calculating the matrix product $TX\mathbin{:}$

$$


\begin{aligned}𝑇𝑋 & =[\begin{aligned}−3 & 1 \\ −1 & 2\end{aligned}][\begin{aligned}0 & 1 \\ −3 & 2\end{aligned}] \\ & =[\begin{aligned}−3 & −1 \\ −6 & 3\end{aligned}]\end{aligned}


$$

Therefore, the coordinates of the respective image points are $P'(-3,-6)$ and $Q'(-1,3).$

Finally, we write the equation of the line that passes through $P'$ and $Q'\mathbin{:}$

$$


\begin{aligned}𝑦−𝑦_{1} & =\frac{𝑦_{2}−𝑦_{1}}{𝑥_{2}−𝑥_{1}}(𝑥−𝑥_{1}) \\ 𝑦−(−6) & =\frac{3−(−6)}{−1−(−3)}(𝑥−(−3)) \\ 𝑦+6 & =\frac{9}{2}(𝑥+3) \\ 2𝑦+12 & =9𝑥+27 \\ 9𝑥−2𝑦+15 & =0\end{aligned}


$$

### The Proof That a Linear Transformation Maps a Straight Line Onto a Straight Line

Consider a non-singular linear transformation $\mathbf{T}$ and a line that is given by the vector equation

$$


\mathbf{r} = \mathbf{p}+\mathbf{d}t, \qquad t \in (-\infty,\infty).


$$

Note that, for the above equation to represent a line (and not just a point), we must have $\mathbf{d} \neq \mathbf{0}.$

Now, using the linearity of the transformation, we obtain

$$


\begin{aligned}𝐓(𝐫) & =𝐓(𝐩+𝐝𝑡) \\ & =𝐓(𝐩)+𝐓(𝑡𝐝) \\ & =𝐓(𝐩)+𝑡𝐓(𝐝) \\ & =𝐩^{′}+𝑡𝐝^{′},\end{aligned}


$$

where $\mathbf{T}(\mathbf{p})=\mathbf{p}'$ and $\mathbf{T}(\mathbf{d})=\mathbf{d}'.$

Because $\mathbf{T}$ is non-singular and $\mathbf{d} \neq \mathbf{0},$ we know that $\mathbf{T}(\mathbf{d}) \neq \mathbf{0},$ which means $\mathbf{d}' \neq \mathbf{0}.$

Therefore, the equation $\mathbf{p}'+t\mathbf{d}'$ represents a straight line, and we can make the following conclusion:

*A non-singular linear transformation maps a straight line onto a straight line.*
