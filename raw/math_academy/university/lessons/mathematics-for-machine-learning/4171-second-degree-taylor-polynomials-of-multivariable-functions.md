# Second-Degree Taylor Polynomials of Multivariable Functions

Source: https://www.mathacademy.com/topics/4171?courseId=145
Topic ID: 4171

## Prerequisites

- [Second-Degree Taylor Polynomials](../../../ap-courses/lessons/ap-calculus-bc/1177-second-degree-taylor-polynomials.md)
- [The Second Derivative of a Multivariable Function](./2824-the-second-derivative-of-a-multivariable-function.md)

## Lesson

### Introduction

Recall that the quadratic Taylor polynomial of a function $f(x)$ at the point $x=a$ is given by

$$


f(x) \approx \overbrace{f(a) + f'(a)(x-a)}^{\text{Linear approximation}} + \underbrace{\dfrac{1}{2}f''(a)(x-a)^2}_{\textrm{Quadratic part}}.


$$

We can extend the concept of Taylor polynomials to multivariable functions.

Given a twice-differentiable function $f(x,y),$ the **quadratic Taylor polynomial** of $f$ about the point $(a,b)$ is given by

$$


\begin{aligned}𝑓(𝑥,𝑦) & ≈\overset{\overset{𝑓(𝑎,𝑏)+𝑓_{𝑥}(𝑎,𝑏)⋅(𝑥−𝑎)+𝑓_{𝑦}(𝑎,𝑏)⋅(𝑦−𝑏)}{}}{Linear approximation} \\ & ≈\,\,+\underset{Quadratic part}{\underset{}{\frac{1}{2}(𝑓_{𝑥𝑥}(𝑎,𝑏)⋅(𝑥−𝑎)^{2}+2𝑓_{𝑥𝑦}(𝑎,𝑏)⋅(𝑥−𝑎)(𝑦−𝑏)+𝑓_{𝑦𝑦}(𝑎,𝑏)⋅(𝑦−𝑏)^{2})}}.\end{aligned}


$$

In particular, the quadratic Taylor polynomial of $f(x,y)$ about the origin $O$ is

$$


\begin{aligned}𝑓(𝑥,𝑦) & ≈𝑓(0,0)+𝑓_{𝑥}(0,0)⋅𝑥+𝑓_{𝑦}(0,0)⋅𝑦 \\ & ≈\,\,+\frac{1}{2}(𝑓_{𝑥𝑥}(0,0)⋅𝑥^{2}+2𝑓_{𝑥𝑦}(0,0)⋅𝑥𝑦+𝑓_{𝑦𝑦}(0,0)⋅𝑦^{2}).\end{aligned}


$$

Later in the lesson, we will develop some intuition for why the quadratic part looks the way it does. But before we do that, let's get some practice working with this formula.

### Example: Finding a Quadratic Taylor Polynomial

#### Question

Determine the quadratic Taylor polynomial for the function of two variables $f(x,y) = \cos(x+y)$ about the point $(0,0).$

#### Explanation

If the function $f(x,y)$ is twice differentiable at $(x,y) = (0,0),$ then the quadratic Taylor polynomial of $f$ about $(0,0)$ is given by

$$


\begin{aligned}𝑓(𝑥,𝑦) & ≈\overset{\overset{𝑓(0,0)+𝑓_{𝑥}(0,0)⋅𝑥+𝑓_{𝑦}(0,0)⋅𝑦}{}}{Linear approximation} \\ & ≈\,\,+\underset{Quadratic part}{\underset{}{\frac{1}{2}(𝑓_{𝑥𝑥}(0,0)⋅𝑥^{2}+2𝑓_{𝑥𝑦}(0,0)⋅𝑥𝑦+𝑓_{𝑦𝑦}(0,0)⋅𝑦^{2})}}.\end{aligned}


$$

Now, we compute the terms of our Taylor polynomial.

- Calculating the value of the function, we have

- Calculating the first derivatives, we have the following:

- Calculating the second derivatives, we have the following:

Therefore, the second-degree Taylor polynomial is given by

$$


\begin{aligned}𝑓(𝑥,𝑦) & ≈1+0⋅𝑥+0⋅𝑦+\frac{1}{2}((−1)⋅𝑥^{2}+2(−1)⋅𝑥𝑦+(−1)⋅𝑦^{2}) \\ & =1−\frac{1}{2}𝑥^{2}−𝑥𝑦−\frac{1}{2}𝑦^{2}.\end{aligned}


$$

### The Quadratic Taylor Polynomial in Matrix Form

It's possible to derive Taylor polynomials for functions of more than two variables. However, increasing the number of variables significantly increases the number of terms in the Taylor polynomial.

Ideally, we'd like a compact expression for the quadratic Taylor polynomial that works for all twice-differentiable functions $f:\mathbb R^n\to\mathbb R.$ This can be achieved using matrix notation.

To see how, let's consider the quadratic Taylor polynomial of $f(x,y)$ about $(a,b){:}$

$$


\begin{aligned}𝑓(𝑥,𝑦) & ≈\overset{\overset{𝑓(𝑎,𝑏)+𝑓_{𝑥}(𝑎,𝑏)⋅(𝑥−𝑎)+𝑓_{𝑦}(𝑎,𝑏)⋅(𝑦−𝑏)}{}}{Linear approximation} \\ & ≈\,\,+\underset{Quadratic part}{\underset{}{\frac{1}{2}(𝑓_{𝑥𝑥}(𝑎,𝑏)⋅(𝑥−𝑎)^{2}+2𝑓_{𝑥𝑦}(𝑎,𝑏)⋅(𝑥−𝑎)(𝑦−𝑏)+𝑓_{𝑦𝑦}(𝑎,𝑏)⋅(𝑦−𝑏)^{2})}}.\end{aligned}


$$

If we denote $[\begin{aligned}𝑥 \\ 𝑦\end{aligned}]$ and $[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]$ then the total derivative of $f(x,y)=f(\mathbf{x})$ at $(a,b)=\mathbf{a}$ is given by

$$


[\begin{aligned}𝑓_{𝑥}(𝑎,𝑏) & 𝑓_{𝑦}(𝑎,𝑏)\end{aligned}]


$$

With that in mind, we can rewrite the linear part of the approximation as follows:

$$


\begin{aligned}Linear approximation & =𝑓(𝑎,𝑏)+𝑓_{𝑥}(𝑎,𝑏)⋅(𝑥−𝑎)+𝑓_{𝑦}(𝑎,𝑏)⋅(𝑦−𝑏) \\ & =𝑓(𝐚)+[\begin{aligned}𝑓_{𝑥}(𝑎,𝑏) & 𝑓_{𝑦}(𝑎,𝑏)\end{aligned}]⋅[\begin{aligned}𝑥−𝑎 \\ 𝑦−𝑏\end{aligned}] \\ & =𝑓(𝐚)+[\begin{aligned}𝑓_{𝑥}(𝑎,𝑏) & 𝑓_{𝑦}(𝑎,𝑏)\end{aligned}]⋅([\begin{aligned}𝑥 \\ 𝑦\end{aligned}]−[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]) \\ & =𝑓(𝐚)+𝒇^{′}(𝐚)(𝐱−𝐚)\end{aligned}


$$

Notice that this is just our usual linear approximation of a function $f.$

The second derivative of $f$ at $\mathbf x = \mathbf a$ is given by

$$


[\begin{aligned}𝑓_{𝑥𝑥}(𝐚) & 𝑓_{𝑥𝑦}(𝐚) \\ 𝑓_{𝑦𝑥}(𝐚) & 𝑓_{𝑦𝑦}(𝐚)\end{aligned}]


$$

Therefore, using the fact that $f_{xy} = f_{yx},$ we can rewrite the quadratic part of the approximation using matrix multiplication as follows:

$$


\begin{aligned}Quadratic part & =\frac{1}{2}(𝑓_{𝑥𝑥}(𝑎,𝑏)⋅(𝑥−𝑎)^{2}+2𝑓_{𝑥𝑦}(𝑎,𝑏)⋅(𝑥−𝑎)(𝑦−𝑏)+𝑓_{𝑦𝑦}(𝑎,𝑏)⋅(𝑦−𝑏)^{2}) \\ & =\frac{1}{2}[\begin{aligned}𝑥−𝑎 & 𝑦−𝑏\end{aligned}]⋅[\begin{aligned}𝑓_{𝑥𝑥}(𝐚) & 𝑓_{𝑥𝑦}(𝐚) \\ 𝑓_{𝑦𝑥}(𝐚) & 𝑓_{𝑦𝑦}(𝐚)\end{aligned}]⋅[\begin{aligned}𝑥−𝑎 \\ 𝑦−𝑏\end{aligned}] \\ & =\frac{1}{2}([\begin{aligned}𝑥 & 𝑦\end{aligned}]−[\begin{aligned}𝑎 & 𝑏\end{aligned}])⋅[\begin{aligned}𝑓_{𝑥𝑥}(𝐚) & 𝑓_{𝑥𝑦}(𝐚) \\ 𝑓_{𝑦𝑥}(𝐚) & 𝑓_{𝑦𝑦}(𝐚)\end{aligned}]⋅([\begin{aligned}𝑥 \\ 𝑦\end{aligned}]−[\begin{aligned}𝑎 \\ 𝑏\end{aligned}]) \\ & =\frac{1}{2}(𝐱−𝐚)^{𝑇}𝒇^{″}(𝐚)(𝐱−𝐚)\end{aligned}


$$

Therefore, our quadratic Taylor polynomial can be written as

$$


\begin{aligned}𝑓(𝐱) & ≈\overset{\overset{𝑓(𝐚)+𝒇^{′}(𝐚)(𝐱−𝐚)}{}}{Linear approximation}+\underset{Quadratic part}{\underset{}{\frac{1}{2}(𝐱−𝐚)^{𝑇}𝒇^{″}(𝐚)(𝐱−𝐚)}}.\end{aligned}


$$

Notice that this formula is more compact and has clear similarity with the corresponding formula for functions with one variable:

$$


f(x) \approx \overbrace{f(a) + f'(a)(x-a)}^{\text{Linear approximation}} + \underbrace{\dfrac{1}{2}f''(a)(x-a)^2}_{\textrm{Quadratic part}}


$$

### General Formula For the Quadratic Taylor Polynomial in Matrix Form

The formula derived earlier works for multivariable functions with a finite number of variables.

Suppose that the function $f:\mathbb R^n\to\mathbb R$ is defined by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

and is twice differentiable at $\mathbf x = \mathbf a.$ Then, the quadratic Taylor approximation of $f$ about $\mathbf a$ is given by

$$


\begin{aligned}𝑓(𝐱) & ≈𝑓(𝐚)+𝒇^{′}(𝐚)(𝐱−𝐚)+\frac{1}{2}(𝐱−𝐚)^{𝑇}𝒇^{″}(𝐚)(𝐱−𝐚),\end{aligned}


$$

where the first derivative is

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{1}} & \frac{𝜕𝑓}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑥_{𝑛}}\end{aligned}]


$$

and the second derivative is

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥_{21}^{}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{𝑛}} \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{22}^{}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2𝑛}^{}}\end{aligned}


$$

### Example: Finding a Quadratic Taylor Polynomial in Matrix Form

#### Question

For the function $f:\mathbb R^2\to\mathbb R,$ defined as

$$


f\left(x,y \right) = x^2y-xy^3,


$$

determine the quadratic Taylor polynomial of $f$ about $[\begin{aligned}1 \\ 1\end{aligned}]$ Give your answer in matrix form.

#### Explanation

Suppose that the function $\mathbf{f}:\mathbb R^n\to\mathbb R$ is defined by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

and is twice differentiable at $\mathbf x = \mathbf a.$ Then, the quadratic Taylor polynomial of $f$ about $\mathbf a$ is given by

$$


\begin{aligned}𝑓(𝐱) & ≈𝑓(𝐚)+𝒇^{′}(𝐚)(𝐱−𝐚)+\frac{1}{2}(𝐱−𝐚)^{𝑇}𝒇^{″}(𝐚)(𝐱−𝐚),\end{aligned}


$$

where

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{1}} & \frac{𝜕𝑓}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑥_{𝑛}}\end{aligned}]


$$

and

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥_{21}^{}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{𝑛}} \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{22}^{}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2𝑛}^{}}\end{aligned}


$$

In this case, we have the following:

$$


\begin{aligned}𝒇^{′}(𝐱) & =[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & \frac{𝜕𝑓}{𝜕𝑦}\end{aligned}], & \,𝒇^{″}(𝐱) & =\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}\end{aligned}\end{aligned}


$$

Now, we compute the terms of our Taylor polynomial:

- Calculating the value of the function, we have

- Calculating the first derivatives, we have the following:

- Calculating the second derivative, we have the following:

Therefore, the second-degree Taylor polynomial (in matrix form) is given by

$$


[\begin{aligned}1 & −2\end{aligned}]


$$

### Example: Approximating a Multivariable Function at a Point Using a Quadratic Taylor Polynomial

#### Question

For the twice-differentiable function $f:\mathbb R^3\to\mathbb R,$ we have the following data:

$$


\begin{aligned}𝑓(1,0,0) & =−1, & \,𝒇^{′}(1,0,0) & =[\begin{aligned}1 & 0 & 1\end{aligned}], & \,𝒇^{″}(1,0,0) & =\begin{aligned}3 & 0 & −1 \\ 0 & 1 & 0 \\ −1 & 0 & 2\end{aligned}\end{aligned}


$$

Use the quadratic Taylor polynomial of $f$ about $\begin{aligned}1 \\ 0 \\ 0\end{aligned}$ to approximate the value of $f(1,1,1).$

#### Explanation

Suppose that the function $\mathbf{f}:\mathbb R^n\to\mathbb R$ is defined by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

and is twice differentiable at $\mathbf x = \mathbf a.$ Then, the quadratic Taylor polynomial of $f$ about $\mathbf a$ is given by

$$


\begin{aligned}𝑓(𝐱) & ≈𝑓(𝐚)+𝒇^{′}(𝐚)(𝐱−𝐚)+\frac{1}{2}(𝐱−𝐚)^{𝑇}𝒇^{″}(𝐚)(𝐱−𝐚),\end{aligned}


$$

where

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{1}} & \frac{𝜕𝑓}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑥_{𝑛}}\end{aligned}]


$$

and

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥_{21}^{}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{1}𝜕𝑥_{𝑛}} \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{22}^{}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2}𝜕𝑥_{𝑛}} \\ ⋮ & ⋮ & ⋮ & ⋮ \\ \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{1}} & \frac{𝜕^{2}𝑓}{𝜕𝑥_{𝑛}𝜕𝑥_{2}} & ⋯ & \frac{𝜕^{2}𝑓}{𝜕𝑥_{2𝑛}^{}}\end{aligned}


$$

In this case, we have $\begin{aligned}1 \\ 0 \\ 0\end{aligned}$ and the following data:

$$


\begin{aligned}𝑓(𝐚) & =−1, & \,𝒇^{′}(𝐚) & =[\begin{aligned}1 & 0 & 1\end{aligned}], & \,𝒇^{″}(𝐚) & =\begin{aligned}3 & 0 & −1 \\ 0 & 1 & 0 \\ −1 & 0 & 2\end{aligned}\end{aligned}


$$

Therefore, the second-degree Taylor polynomial is given by

$$


[\begin{aligned}1 & 0 & 1\end{aligned}]


$$

Finally, evaluating the polynomial at $\begin{aligned}1 \\ 1 \\ 1\end{aligned}$ we obtain

$$


\begin{aligned}𝑓(1,1,1) & ≈−1+[\begin{aligned}1 & 0 & 1\end{aligned}]\begin{aligned}1−1 \\ 1 \\ 1\end{aligned}+\frac{1}{2}\begin{aligned}1−1 \\ 1 \\ 1\end{aligned}^{𝑇}\begin{aligned}3 & 0 & −1 \\ 0 & 1 & 0 \\ −1 & 0 & 2\end{aligned}\begin{aligned}1−1 \\ 1 \\ 1\end{aligned} \\ & =−1+[\begin{aligned}1 & 0 & 1\end{aligned}]\begin{aligned}0 \\ 1 \\ 1\end{aligned}+\frac{1}{2}\begin{aligned}0 \\ 1 \\ 1\end{aligned}^{𝑇}\begin{aligned}3 & 0 & −1 \\ 0 & 1 & 0 \\ −1 & 0 & 2\end{aligned}\begin{aligned}0 \\ 1 \\ 1\end{aligned} \\ & =−1+1+\frac{1}{2}[\begin{aligned}0 & 1 & 1\end{aligned}]\begin{aligned}−1 \\ 1 \\ 2\end{aligned} \\ & =\frac{1}{2}(3) \\ & =\frac{3}{2}.\end{aligned}


$$

### Deriving the Quadratic Taylor Polynomial in Matrix Form

Here, we derive the formula for the second-degree Taylor polynomial of a multivariable function in vector form.

Suppose that the function $f: \mathbb{R}^n \to \mathbb{R}$ is defined by

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ ⋮ \\ 𝑥_{𝑛}\end{aligned}


$$

and is twice differentiable at $\mathbf{x} = \mathbf{a}.$ By restricting $\mathbf x$ to a line through $\mathbf{a},$ we can consider $f$ as a function of one variable. Then, we'll use the second-degree Taylor polynomial of a single-variable function to derive the formula.

Let $\mathbf{x}_0$ be a constant vector in $\mathbb{R}^n.$ Then, the line through $\mathbf{a}$ and $\mathbf{x}_0$ is given by

$$


\mathbf{x}(t) = \mathbf{a} + t(\mathbf{x}_0 - \mathbf{a}), \qquad t \in (-\infty, \infty),


$$

where $\mathbf{x}(0) = \mathbf{a}$ and $\mathbf{x}(1) = \mathbf{x}_0.$

Now, we define a function $F: \mathbb{R} \to \mathbb{R}$ by restricting the domain of $f$ to this line:

$$


F(t) = f(\mathbf{x}(t)) \%= f(\mathbf{a} + t(\mathbf{x}_0 - \mathbf{a}))


$$

The second-degree Taylor polynomial of this single-variable function about $t=0$ is given by

$$


F(t) \approx F(0) + F'(0)t + \dfrac12F''(0)t^2.


$$

We can find the first derivative of $F$ using the chain rule:

$$


\begin{aligned}\frac{d𝐹}{d𝑡} & =\frac{d𝑓}{d𝐱}⋅\frac{d𝐱}{d𝑡} \\ & =\frac{d𝑓}{d𝐱}⋅\frac{d}{d𝑡}(𝐚+𝑡(𝐱_{0}−𝐚)) \\ & =\frac{d𝑓}{d𝐱}⋅(𝐱_{0}−𝐚)\end{aligned}


$$

Since $\dfrac{\textrm{d}f}{\textrm{d}\mathbf{x}}$ is a row vector and $(\mathbf{x}_0 - \mathbf{a})$ is a column vector, this is a scalar quantity and, hence, equal to its transpose:

$$


\begin{aligned}\frac{d𝐹}{d𝑡} & =\frac{d𝑓}{d𝐱}⋅(𝐱_{0}−𝐚) \\ & =(\frac{d𝑓}{d𝐱}⋅(𝐱_{0}−𝐚))^{𝑇} \\ & =(𝐱_{0}−𝐚)^{𝑇}(\frac{d𝑓}{d𝐱})^{𝑇}\end{aligned}


$$

With this, we can find the second derivative of $F{:}$

$$


\begin{aligned}\frac{d^{2}𝐹}{d𝑡^{2}} & =\frac{d}{d𝑡}(\frac{d𝐹}{d𝑡}) \\ & =\frac{d}{d𝑡}((𝐱_{0}−𝐚)^{𝑇}(\frac{d𝑓}{d𝐱})^{𝑇}) \\ & =(𝐱_{0}−𝐚)^{𝑇}\frac{d}{d𝑡}(\frac{d𝑓}{d𝐱})^{𝑇} \\ & =(𝐱_{0}−𝐚)^{𝑇}\frac{d}{d𝐱}(\frac{d𝑓}{d𝐱})^{𝑇}⋅\frac{d𝐱}{d𝑡} \\ & =(𝐱_{0}−𝐚)^{𝑇}\frac{d^{2}𝑓}{d𝐱^{2}}(𝐱_{0}−𝐚)\end{aligned}


$$

Therefore, the first and second derivatives are given by

$$


\begin{aligned}𝐹^{′}(𝑡)=𝒇^{′}(𝐱(𝑡))(𝐱_{0}−𝐚) \\ 𝐹^{″}(𝑡)=(𝐱_{0}−𝐚)^{𝑇}𝒇^{″}(𝐱(𝑡))(𝐱_{0}−𝐚).\end{aligned}


$$

Evaluating the function and its derivatives at $t=0$ and using the fact that $\mathbf{x}(0) = \mathbf{a},$ we have

$$


\begin{aligned}𝐹(0)=𝑓(𝐱(0)) \\ 𝐹^{′}(0)=𝒇^{′}(𝐱(0))(𝐱_{0}−𝐚) \\ 𝐹^{″}(0)=(𝐱_{0}−𝐚)^{𝑇}𝒇^{″}(𝐱(0))(𝐱_{0}−𝐚)\end{aligned}


$$

Putting these values into the second-degree Taylor polynomial of a single-variable function about $t=0,$ we get

$$


\begin{aligned}𝐹(𝑡) & ≈𝐹(0)+𝐹^{′}(0)𝑡+\frac{1}{2}𝐹^{″}(0)𝑡^{2} \\ & ≈𝑓(𝐚)+𝒇^{′}(𝐚)(𝐱_{0}−𝐚)𝑡+\frac{1}{2}(𝐱_{0}−𝐚)^{𝑇}𝒇^{″}(𝐚)(𝐱_{0}−𝐚)𝑡^{2}\end{aligned}


$$

Finally, using this polynomial to approximate the value of $F(1),$ and the fact that $F(1) = f(\mathbf{x}(1)) = f(\mathbf{x}_0),$ we conclude that

$$


\begin{aligned}𝐹(1) & ≈𝑓(𝐚)+𝒇^{′}(𝐚)(𝐱_{0}−𝐚)⋅1+\frac{1}{2}(𝐱_{0}−𝐚)^{𝑇}𝒇^{″}(𝐚)(𝐱_{0}−𝐚)⋅1^{2} \\ 𝑓(𝐱_{0}) & ≈𝑓(𝐚)+𝒇^{′}(𝐚)(𝐱_{0}−𝐚)+\frac{1}{2}(𝐱_{0}−𝐚)^{𝑇}𝒇^{″}(𝐚)(𝐱_{0}−𝐚).\end{aligned}


$$

However, $\mathbf{x}_0 \in \mathbb{R}^n$ is an arbitrary constant. Therefore, we can relax the assumption that $\mathbf{x}_0$ is fixed and replace it with a general point $\mathbf{x} \in \mathbb{R}^n$ near $\mathbf{a}$ to obtain the formula for the second-degree Taylor polynomial of a multivariable function in vector form:

$$


f(\mathbf{x}) \approx f(\mathbf{a}) + \boldsymbol{f}'(\mathbf{a})(\mathbf{x} - \mathbf{a}) + \dfrac{1}{2} (\mathbf{x} - \mathbf{a})^T \boldsymbol{f}''(\mathbf{a}) (\mathbf{x} - \mathbf{a})


$$
