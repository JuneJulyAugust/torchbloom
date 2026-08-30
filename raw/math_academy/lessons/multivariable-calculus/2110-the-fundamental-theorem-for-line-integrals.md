# The Fundamental Theorem for Line Integrals

Source: https://www.mathacademy.com/topics/2110?courseId=54
Topic ID: 2110

## Prerequisites

- [Calculating Potential Functions](./1951-calculating-potential-functions.md)
- [Line Integrals of Vector-Valued Functions Over General Curves](./3711-line-integrals-of-vector-valued-functions-over-general-curves.md)

## Lesson

### Introduction

Suppose that $f(x)$ is continuous on $[a,b].$ The fundamental theorem of calculus states that

$$


\int_a^b f'(x)\,\textrm d x = f(b) - f(a).


$$

A similar result, known as **the fundamental theorem for line integrals,** exists for line integrals of conservative vector fields. This theorem can be stated as follows:

*Let $C$ be a piecewise-smooth curve given by the vector-valued function $\mathbf r(t)$ for $t\in [a,b].$ Let $f$ be a differentiable function of two or three variables such that $\nabla f$ is continuous on $C.$ Then,*

$$


\int_{C} \nabla f \cdot \textrm{d}\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a)).


$$

We'll discuss how this theorem is proved in simple cases at the end of the lesson. But for now, let's take a look at a concrete example of how to apply this theorem.

### A Concrete Example

Let's apply the fundamental theorem for line integrals to evaluate

$$


\int_C \nabla f \cdot \textrm{d}\mathbf{r},


$$

where $f(x,y) = x^2y^3$ and $C$ is the path along the curve $y=x^2$ for $x \in [0,2].$

First, we must parameterize the curve $C.$ A suitable parametrization is

$$


\mathbf{r}(t) = \left\langle t, \: t^2\right\rangle, \qquad t \in [0,2].


$$

The position vectors of the endpoints of $C$ are given by

$$


\mathbf{r}(0) = \left\langle 0, 0\right\rangle, \qquad \mathbf{r}(2) = \left\langle 2, 4\right\rangle.


$$

Therefore, the coordinates of the path's endpoints defined by $C$ are $(0,0)$ and $(2,4).$

Finally, applying the fundamental theorem for line integrals, we have

$$


\begin{aligned}∫_{𝐶}∇𝑓⋅d𝐫 & =𝑓(𝐫(2))−𝑓(𝐫(0)) \\ & =𝑓(2,4)−𝑓(0,0) \\ & =2^{2}⋅4^{3}−0^{2}⋅0^{3} \\ & =4⋅64 \\ & =256.\end{aligned}


$$

Notice how much faster it is to evaluate a line integral when we can use the fundamental theorem.

### Example: Applying the Fundamental Theorem of Line Integrals Over Parametric Curves

#### Question

Let $f(x,y,z)=xy^2+ 2xz.$ Given that $C$ is the path along the curve $\mathbf r(t)= \langle e^{t}, t, e^{-t}\rangle$ for $t\in \left[0,1\right],$ evaluate $\displaystyle\int_{C} \nabla f\cdot \textrm{d}\mathbf r.$

#### Explanation

Let $C$ be a piecewise-smooth curve given by the vector function $\mathbf r(t)$ for $t\in [a,b].$ Let $f$ be a differentiable function of two or three variables such that $\nabla f$ is continuous on $C.$ The fundamental theorem for line integrals states that

$$


\int_{C} \nabla f \cdot \textrm{d}\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a)).


$$

In our case, the position vectors of the endpoints of the curve are given by

$$


\begin{aligned}𝐫(0) & =⟨1,0,1⟩ \\ 𝐫(1) & =⟨𝑒,1,\frac{1}{𝑒}⟩.\end{aligned}


$$

Therefore, the coordinates of the endpoints of the path defined by $C$ are $(1,0,1)$ and $\left(e, 1, \dfrac{1}{e}\right).$

Applying the fundamental theorem for line integrals, we have

$$


\begin{aligned}∫_{𝐶}∇𝑓⋅d𝐫 & =𝑓(𝐫(1))−𝑓(𝐫(0)) \\ & =𝑓(𝑒,1,\frac{1}{𝑒})−𝑓(1,0,1) \\ & =(𝑒(1)^{2}+2⋅𝑒⋅\frac{1}{𝑒})−(1(0)^{2}+2(1)(1)) \\ & =(𝑒+2)−2 \\ & =𝑒.\end{aligned}


$$

### Example: Applying the Fundamental Theorem of Line Integrals Over Cartesian Curves

#### Question

Let $f(x,y)= xe^{y}.$ Given that $C$ is the path along the curve $x + 2y=3$ for $x\in [-1,1],$ evaluate $\displaystyle\int_{C} \nabla f\cdot \textrm{d}\mathbf r.$

#### Explanation

Let $C$ be a piecewise-smooth curve given by the vector function $\mathbf r(t)$ for $t\in [a,b].$ Let $f$ be a differentiable function of two or three variables such that $\nabla f$ is continuous on $C.$ The fundamental theorem for line integrals states that

$$


\int_{C} \nabla f \cdot \textrm{d}\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a)).


$$

We start by parametrizing the curve $C.$ A suitable parametrization is

$$


\mathbf r(t) = \left\langle t, \dfrac{1}{2}(3-t)\right\rangle, \quad t\in[-1,1].


$$

Then, the position vectors of the endpoints of the curve are given by

$$


\begin{aligned}𝐫(−1) & =⟨−1,2⟩, \\ 𝐫(1) & =⟨1,1⟩.\end{aligned}


$$

Therefore, the coordinates of the endpoints of the path defined by $C$ are $(-1,2)$ and $(1,1).$

Applying the fundamental theorem for line integrals, we have

$$


\begin{aligned}∫_{𝐶}∇𝑓⋅d𝐫 & =𝑓(𝐫(1))−𝑓(𝐫(−1)) \\ & =𝑓(1,1)−𝑓(−1,2) \\ & =1⋅𝑒^{1}−(−1)⋅𝑒^{2} \\ & =𝑒+𝑒^{2} \\ & =𝑒(1+𝑒).\end{aligned}


$$

### Example: Applying the Fundamental Theorem of Line Integrals When the Potential Function Is Not Given

#### Question

Consider the curve $C,$ defined parametrically as

$$


\mathbf r(t) = \left\langle t, 1-t \right\rangle, \quad 0 \leq t \leq 1.


$$

Evaluate $\displaystyle{\int _C \mathbf F \cdot \textrm d\mathbf r}$ for $\mathbf F = ye^{xy}\,\mathbf i + xe^{xy}\,\mathbf j.$

**

#### Explanation

Let $C$ be a piecewise-smooth curve given by the vector function $\mathbf r(t)$ for $t\in [a,b].$ Let $f$ be a differentiable function of two or three variables such that $\nabla f$ is continuous on $C.$ The fundamental theorem for line integrals states that

$$


\int_{C} \nabla f \cdot \textrm{d}\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a)).


$$

To apply the fundamental theorem for line integrals, we must first find a potential function $f$ such that $\mathbf F = \nabla f.$ Since we're given that $\mathbf F$ is conservative, we know that such a function exists. Therefore, we must have

$$


\begin{aligned}𝑓_{𝑥}(𝑥,𝑦) & =𝑦𝑒^{𝑥𝑦}, \\ 𝑓_{𝑦}(𝑥,𝑦) & =𝑥𝑒^{𝑥𝑦}.\end{aligned}


$$

Reconstructing the function $f$ from its gradient in the usual way, we get

$$


f(x,y)= e^{xy}.


$$

Note that we set $C=0$ for the arbitrary constant since we can use any function $f$ that satisfies $\nabla f = \mathbf F.$

We're now ready to apply the fundamental theorem for line integrals. The position vectors of the endpoints of the curve are given by

$$


\begin{aligned}𝐫(0) & =⟨0,1⟩, \\ 𝐫(1) & =⟨1,0⟩.\end{aligned}


$$

Therefore, the coordinates of the endpoints of the path defined by $C$ are $(0,1)$ and $(1,0).$

Finally, applying the fundamental theorem for line integrals, we have

$$


\begin{aligned}∫_{𝐶}𝐅⋅d𝐫 & =∫_{𝐶}∇𝑓⋅d𝐫 \\ & =𝑓(1,0)−𝑓(0,1) \\ & =𝑒^{1⋅0}−𝑒^{0⋅1} \\ & =1−1 \\ & =0.\end{aligned}


$$

### Proof of the Fundamental Theorem for Smooth Curves

Here, we prove the fundamental theorem of line integrals in the two-dimensional case. The three-dimensional case is similar.

Let $C$ be a smooth curve $\mathbf r(t)$ for $t\in [a,b],$ and suppose that $f(x,y)$ is a differentiable function of two variables such that $\nabla f$ is continuous on $C.$ We wish to show that

$$


\int_C \nabla f \cdot \textrm d \mathbf r = f(\mathbf r(b)) - f(\mathbf r(a)).


$$

Using our usual formula for calculating line integrals, we can write the left-hand side as

$$


\begin{aligned}∫_{𝐶}∇𝑓⋅d𝐫 & =∫_{𝑏𝑎}^{}∇𝑓⋅𝐫^{′}(𝑡)\,d𝑡 \\ & =∫_{𝑏𝑎}^{}(\frac{𝜕𝑓}{𝜕𝑥}\,𝐢+\frac{𝜕𝑓}{𝜕𝑦}\,𝐣)⋅(\frac{d𝑥}{d𝑡}\,𝐢+\frac{d𝑦}{d𝑡}\,𝐣)\,d𝑡 \\ & =∫_{𝑏𝑎}^{}\frac{𝜕𝑓}{𝜕𝑥}\frac{d𝑥}{d𝑡}+\frac{𝜕𝑓}{𝜕𝑦}\frac{d𝑦}{d𝑡}\,d𝑡.\end{aligned}


$$

According to the chain rule, the integrand above is simply the derivative of $f(\mathbf r(t))$ with respect to $t.$ Thus, we can write this integral as

$$


\int_a^b \dfrac{\textrm d}{\textrm d t}(f(\mathbf r(t)))\,\textrm d t.


$$

Finally, by the fundamental theorem of calculus, this is equal to

$$


f(\mathbf r(b)) - f(\mathbf r(a)).


$$

This concludes the proof in the case where $C$ is smooth. It's easy to show that the theorem also holds for piecewise smooth curves.
