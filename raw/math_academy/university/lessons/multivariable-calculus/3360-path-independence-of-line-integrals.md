# Path Independence of Line Integrals

Source: https://www.mathacademy.com/topics/3360?courseId=54
Topic ID: 3360

## Prerequisites

- [The Fundamental Theorem for Line Integrals](./2110-the-fundamental-theorem-for-line-integrals.md)

## Lesson

### Introduction

The fundamental theorem of line integrals states that

$$


\int_{C} \nabla f \cdot \text{d}\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a))


$$

where $C$ is a piecewise-smooth curve $\mathbf r(t)$ for $t\in [a,b],$ and $f$ is differentiable function such that $\nabla f$ is continuous on $C.$

This theorem tells us that the line integral of a conservative vector field $\mathbf{F} = \nabla f$ is determined by the values of $f$ at the endpoints $A$ and $B$ of $C$ only. The integral does *not* depend on the path between $A$ and $B.$

In particular, if $\mathbf F$ is conservative, then we say that $\displaystyle\int_{C} \mathbf F \cdot \text{d}\mathbf r$ is **path-independent.**

### Example: Calculating a Line Integral Over an Arbitrary Path

#### Question

Consider the scalar field $f(x,y,z) = x^2 + y^2 + z^2.$ Calculate $\displaystyle{\int_C \nabla f \cdot \textrm d\mathbf r},$ where $C$ is any smooth path from $(-2, 1, 0)$ to $(-1, 0, -1)$ in $\mathbb R^3.$

#### Explanation

Let $C$ be a piecewise-smooth curve given by the vector-valued function $\mathbf r(t)$ for $t \in [a,b].$ Let $f$ be a differentiable function of two or three variables such that $\nabla f$ is continuous on $C.$ The fundamental theorem for line integrals states that

$$


\int_{C} \nabla f \cdot \text{d}\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a)).


$$

This theorem implies that the line integral of a conservative vector field depends only on the value of $f$ at the initial and terminal points $A$ and $B,$ and is independent of the path between them.

In our case, the coordinates of the endpoints of the path $C$ are $A(-2, 1, 0)$ and $B(-1, 0, -1).$

Applying the fundamental theorem for line integrals, we have

$$


\begin{aligned}∫_{𝐶}∇𝑓⋅d𝐫 & =𝑓(−1,0,−1)−𝑓(−2,1,0) \\ & =((−1)^{2}+0^{2}+(−1)^{2})−((−2)^{2}+1^{2}+0^{2}) \\ & =2−5 \\ & =−3.\end{aligned}


$$

### Example: Calculating a Line Integral Over an Arbitrary Path When the Potential Function Is Not Given

#### Question

Consider the vector field $\mathbf F(x, y) = -2x\,\mathbf i + 6y^2\,\mathbf j.$ Calculate $\displaystyle{\int_C \mathbf F \cdot \textrm d\mathbf r},$ where $C$ is any smooth path from $(-2, 0)$ to $(1, 2)$ in $\mathbb R^2.$

#### Explanation

Let $C$ be a piecewise-smooth curve given by the vector-valued function $\mathbf r(t)$ for $t \in [a,b].$ Let $f$ be a differentiable function of two or three variables such that $\nabla f$ is continuous on $C.$ The fundamental theorem for line integrals states that

$$


\int_{C} \nabla f \cdot \text{d}\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a)).


$$

This theorem implies that the line integral of a conservative vector field depends only on the value of $f$ at the initial and terminal points $A$ and $B,$ and is independent of the path between them.

In our case, the coordinates of the endpoints of the path $C$ are $A(-2,0)$ and $B(1, 2).$

Notice that $\mathbf F = P\,\mathbf i + Q\,\mathbf j$ is a vector field on $\mathbb R^2$ with domain $D = \mathbb R^2.$ Computing the partial derivatives, we get

$$


\dfrac{\partial P}{\partial y} = \dfrac{\partial Q}{\partial x} = 0.


$$

Since the partial derivatives exist and are continuous and equal everywhere on $\mathbb R^2,$ we conclude that $\mathbf F$ is conservative. Therefore, we know there exists a function $f$ such that $\nabla f = \mathbf F.$

Reconstructing $f$ from its gradient in the usual way, we get

$$


f = 2y^3 - x^2.


$$

Finally, applying the fundamental theorem for line integrals, we have

$$


\begin{aligned}∫_{𝐶}𝐅⋅d𝐫 & =∫_{𝐶}∇𝑓⋅d𝐫 \\ & =𝑓(1,2)−𝑓(−2,0) \\ & =(2(2)^{3}−1^{2})−(2(0)^{3}−(−2)^{2}) \\ & =16−1+4 \\ & =19.\end{aligned}


$$

### Example: Identifying Vector Fields That Are Independent of Path

#### Question

Consider the vector field $\mathbf F(x,y) = \left\langle ye^{xy},\, xe^{xy}\right\rangle$ and the points $A(1,1)$ and $B(2,2)$ in the $xy$-plane.

Which of the following statements are true?

1. $\mathbf F$ is conservative.

2. $\displaystyle\int\limits_{C_1} \mathbf F\cdot \textrm d \mathbf r = e^4-e,$ where $C_1$ is the path along the curve $y=\sqrt{2x},$ traversed from $A$ to $B.$

3. $\displaystyle\int\limits_{C_2} \mathbf F\cdot \textrm d \mathbf r = e^4-e,$ where $C_2$ is the path along along the line segment $\overline{AB},$ traversed from $A$ to $B.$

#### Explanation

Let $C$ be a piecewise-smooth curve given by the vector-valued function $\mathbf r(t)$ for $t\in [a,b].$ Let $f$ be a differentiable function of two or three variables such that $\nabla f$ is continuous on $C.$ The fundamental theorem for line integrals states that

$$


\int_{C} \nabla f \cdot \text{d}\mathbf r = f(\mathbf r(b)) - f(\mathbf r(a)).


$$

This theorem implies that the line integral of a conservative vector field depends only on the value of $f$ at the initial and terminal points $A$ and $B,$ and is independent of the path between them.

With that in mind, we consider each statement in turn.

- Statement I is true. Notice that $\mathbf F = P\,\mathbf i + Q\,\mathbf j$ is a vector field on $\mathbb R^2$ with domain $D = \mathbb R^2.$ Computing the partial derivatives, we get Since the partial derivatives exist and are continuous and equal everywhere on $\mathbb R^2,$ we conclude that $\mathbf F$ is conservative. Therefore, we know there exists a function $f$ such that $\nabla f = \mathbf F.$

- Statement II is true. Since $\mathbf F$ is conservative, there exists a function $f$ such that $\nabla f = \mathbf F.$ Reconstructing the function $f$ from its gradient in the usual way, we get Applying the fundamental theorem for line integrals, we get

- Statement III is true. Since $\mathbf F$ is conservative and $C_2$ has the same initial and terminal points as $C_1,$ we have

Therefore, the correct answer is "I, II, and III."
