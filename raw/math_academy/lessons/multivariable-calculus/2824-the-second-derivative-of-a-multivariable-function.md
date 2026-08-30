# The Second Derivative of a Multivariable Function

Source: https://www.mathacademy.com/topics/2824?courseId=54
Topic ID: 2824

## Prerequisites

- [Equality of Mixed Partial Derivatives](./1957-equality-of-mixed-partial-derivatives.md)
- [Symmetric Matrices](../linear-algebra/3118-symmetric-matrices.md)
- [The Derivative of a Multivariable Function](./4169-the-derivative-of-a-multivariable-function.md)

## Lesson

### Introduction

We've seen how to calculate the total derivative of a function $f: \mathbb R^n \to \mathbb R.$ In this lesson, we will learn how to calculate its second derivative.

For a function $f: \mathbb R^n \to \mathbb R,$ given by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

the total derivative of $f$ is given by the matrix

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{1}} & \frac{𝜕𝑓}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑥_{𝑛}}\end{aligned}]


$$

To differentiate $f$ once more, we first need to take the transpose of the first derivative:

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{1}} \\ \frac{𝜕𝑓}{𝜕𝑥_{2}} \\ ⋮ \\ \frac{𝜕𝑓}{𝜕𝑥_{𝑛}}\end{aligned}


$$

To calculate the **second derivative** of $f,$ we simply apply the definition of the total derivative to $\left(\boldsymbol f'(\mathbf x)\right)^T.$ By doing this, we get the following $n\times n$ matrix:

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥_{21}^{}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{𝑛}} \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{22}^{}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2𝑛}^{}}\end{aligned}


$$

Notice that this matrix is *symmetric* due to the equality of mixed partial derivatives. This becomes important later.

The matrix $\boldsymbol{f}''(\mathbf x)$ is sometimes called the **Hessian matrix,** and its determinant,

$$


H(\mathbf x) = \det\big( \boldsymbol{f}''(\mathbf x) \big)


$$

is called the **Hessian determinant**.

Note that in the case of a two-variable function $f(x,y),$ the second derivative is given by

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}\end{aligned}


$$

In this lesson, we'll primarily focus on two-variable functions $f(x,y).$ However, we should remember that the techniques discussed here can be applied to scalar functions with an arbitrary number of variables.

### Example: Finding the Second Derivative of a Function Given Its First Derivative

#### Question

Find $\boldsymbol f''(\pi,0)$ for the function $f(x,y)$ given that $[\begin{aligned}𝑒^{𝑦}cos⁡𝑥 & 𝑒^{𝑦}sin⁡𝑥\end{aligned}]$

#### Explanation

For a function $f: \mathbb R^n \to \mathbb R,$ given by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

the second derivative of $f$ is given by the $n\times n$ matrix

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥_{21}^{}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{𝑛}} \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{22}^{}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2𝑛}^{}}\end{aligned}


$$

In our case, we have

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}\end{aligned}


$$

First, notice that since $[\begin{aligned}𝑒^{𝑦}cos⁡𝑥 & 𝑒^{𝑦}sin⁡𝑥\end{aligned}]$ we must have

$$


\dfrac{\partial f}{\partial x} = e^y\cos x , \qquad \dfrac{\partial f}{\partial y} =e^y\sin x .


$$

Now, we compute the second partial derivatives:

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & =\frac{𝜕}{𝜕𝑥}(𝑒^{𝑦}cos⁡𝑥)=−𝑒^{𝑦}sin⁡𝑥\, & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} & =\frac{𝜕}{𝜕𝑥}(𝑒^{𝑦}sin⁡𝑥)=𝑒^{𝑦}cos⁡𝑥 \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & =\frac{𝜕}{𝜕𝑦}(𝑒^{𝑦}cos⁡𝑥)=𝑒^{𝑦}cos⁡𝑥\, & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}} & =\frac{𝜕}{𝜕𝑦}(𝑒^{𝑦}sin⁡𝑥)=𝑒^{𝑦}sin⁡𝑥\end{aligned}


$$

So, the second derivative is

$$


\begin{aligned}𝒇^{″}(𝑥,𝑦) & =[\begin{aligned}−𝑒^{𝑦}sin⁡𝑥 & 𝑒^{𝑦}cos⁡𝑥 \\ 𝑒^{𝑦}cos⁡𝑥 & 𝑒^{𝑦}sin⁡𝑥\end{aligned}].\end{aligned}


$$

Finally, we evaluate this matrix at $(\pi,0).$ This gives

$$


[\begin{aligned}0 & −1 \\ −1 & 0\end{aligned}]


$$

### Example: Finding the Second Derivative of a Function

#### Question

Find $\boldsymbol f''(1,0)$ for the function $f(x,y) = x^2 e^y.$

#### Explanation

For a function $f: \mathbb R^n \to \mathbb R,$ given by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

the second derivative of $f$ is given by the $n\times n$ matrix

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥_{21}^{}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{𝑛}} \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{22}^{}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2𝑛}^{}}\end{aligned}


$$

In our case, we have

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}\end{aligned}


$$

First, we compute the first derivative of $f(x,y),$ as follows:

$$


\begin{aligned}𝒇^{′}(𝑥,𝑦) & =[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & \frac{𝜕𝑓}{𝜕𝑦}\end{aligned}] \\ & =[\begin{aligned}\frac{𝜕}{𝜕𝑥}(𝑥^{2}𝑒^{𝑦}) & \frac{𝜕}{𝜕𝑦}(𝑥^{2}𝑒^{𝑦})\end{aligned}] \\ & =[\begin{aligned}2𝑥𝑒^{𝑦} & 𝑥^{2}𝑒^{𝑦}\end{aligned}]\end{aligned}


$$

Now, we compute the second partial derivatives:

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & =\frac{𝜕}{𝜕𝑥}(2𝑥 \,𝑒^{𝑦})=2 \,𝑒^{𝑦}\, & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}𝑒^{𝑦})=2𝑥 \,𝑒^{𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & =\frac{𝜕}{𝜕𝑦}(2𝑥 \,𝑒^{𝑦})=2𝑥 \,𝑒^{𝑦}\, & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}} & =\frac{𝜕}{𝜕𝑦}(𝑥^{2}𝑒^{𝑦})=𝑥^{2}𝑒^{𝑦}\end{aligned}


$$

So, the second derivative is

$$


\begin{aligned}𝒇^{″}(𝑥,𝑦) & =[\begin{aligned}2 \,𝑒^{𝑦} & 2𝑥 \,𝑒^{𝑦} \\ 2𝑥 \,𝑒^{𝑦} & 𝑥^{2}𝑒^{𝑦}\end{aligned}].\end{aligned}


$$

Finally, we evaluate this matrix at $\left(1,0\right).$ This gives

$$


\begin{aligned}𝒇^{″}(1,0)=[\begin{aligned}2 & 2 \\ 2 & 1\end{aligned}].\end{aligned}


$$

### Example: Evaluating a Hessian Determinant

#### Question

Given that $[\begin{aligned}ln⁡𝑦 & \frac{𝑥}{𝑦}\end{aligned}]$ evaluate the Hessian determinant of $f(x,y)$ at the point $(0,1).$

#### Explanation

For a function $f: \mathbb R^n \to \mathbb R,$ given by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

the second derivative of $f$ is given by the $n\times n$ matrix

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥_{21}^{}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{𝑛}} \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{22}^{}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2𝑛}^{}}\end{aligned}


$$

The Hessian determinant $H(x,y)$ is the determinant of the second derivative:

$$


H(\mathbf x) = \det \left( \boldsymbol{f}''(\mathbf x) \right)


$$

In our case, we have

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}\end{aligned}


$$

First, notice that since $[\begin{aligned}ln⁡𝑦 & \frac{𝑥}{𝑦}\end{aligned}]$ we must have

$$


\dfrac{\partial f}{\partial x} = \ln y, \qquad \dfrac{\partial f}{\partial y} = \dfrac xy.


$$

Now, we compute the second partial derivatives:

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & =\frac{𝜕}{𝜕𝑥}(ln⁡𝑦)=0\, & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} & =\frac{𝜕}{𝜕𝑥}(\frac{𝑥}{𝑦})=\frac{1}{𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & =\frac{𝜕}{𝜕𝑦}(ln⁡𝑦)=\frac{1}{𝑦}\, & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}} & =\frac{𝜕}{𝜕𝑦}(\frac{𝑥}{𝑦})=−\frac{𝑥}{𝑦^{2}}\end{aligned}


$$

So, the second derivative is

$$


\begin{aligned}𝒇^{″}(𝑥,𝑦) & =\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}\end{aligned}=\begin{aligned}0 & \frac{1}{𝑦} \\ \frac{1}{𝑦} & −\frac{𝑥}{𝑦^{2}}\end{aligned}.\end{aligned}


$$

Evaluating the second derivative at $(0,1),$ we obtain

$$


\begin{aligned}𝒇^{″}(0,1)=[\begin{aligned}0 & 1 \\ 1 & 0\end{aligned}].\end{aligned}


$$

Finally, we have

$$


H(0,1) = 0 \cdot 0 - 1\cdot 1 = -1.


$$
