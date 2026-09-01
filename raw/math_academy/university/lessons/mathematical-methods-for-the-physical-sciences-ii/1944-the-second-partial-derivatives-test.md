# The Second Partial Derivatives Test

Source: https://www.mathacademy.com/topics/1944?courseId=155
Topic ID: 1944

## Prerequisites

- [Global vs. Local Extrema and Critical Points of Multivariable Functions](./1945-global-vs-local-extrema-and-critical-points-of-multivariable-functions.md)

## Lesson

### Introduction

The **critical points** of a function $f(\mathbf x)$ are the points $\mathbf x = \mathbf a$ in the domain of $f$ such that $\boldsymbol f'(\mathbf a) =\mathbf 0^T$ or $\boldsymbol f'(\mathbf a)$ does not exist. A critical point such that $\boldsymbol f'(\mathbf a) = \mathbf 0^T$ is called a **stationary point**.

For example, consider the function $f(x,y) = x^2 - 2x + y^2+6y.$ The domain of $f$ is $\mathbb{R}^2,$ and the first partial derivatives of $f$ are

$$


\dfrac {\partial f}{\partial x} = 2x-2, \qquad \dfrac {\partial f}{\partial y} = 2y+6.


$$

So, the first derivative of $f$ is

$$


[\begin{aligned}2𝑥−2 & 2𝑦+6\end{aligned}]


$$

To find the critical points, we need to find the points $(x,y) \in \mathbb{R}^2$ such that $[\begin{aligned}0 & 0\end{aligned}]$ or $\boldsymbol f'(x,y)$ does not exist:

- Setting $\boldsymbol f'(x,y) = \mathbf{0}^T,$ we obtain the following system: This system has the solution $x=1$ and $y=-3.$ Consequently, $(1,-3)$ is a critical point of $f.$

- $\boldsymbol f'(x,y)$ exists everywhere, so there are no more critical points to be found.

Therefore, the only critical point of $f$ is $(1,-3).$

### Example: Finding the Critical Points of a Function

#### Question

Determine the critical points of $f(x,y) = x^3+y^3-3x^2y+9y.$

#### Explanation

The critical points of a multivariable function $f$ are the points $\mathbf a$ in the domain of $f$ such that $\boldsymbol f'(\mathbf a) =\mathbf 0^T$ or $\boldsymbol f'(\mathbf a)$ does not exist, where

$$


[\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥_{1}} & \frac{𝜕𝑓}{𝜕𝑥_{2}} & ⋯ & \frac{𝜕𝑓}{𝜕𝑥_{𝑛}}\end{aligned}]


$$

In this case, the domain of $f$ is $\mathbb{R}^2,$ and the first partial derivatives of $f$ are

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =3𝑥^{2}−6𝑥𝑦=3𝑥(𝑥−2𝑦) \\ \frac{𝜕𝑓}{𝜕𝑦} & =3𝑦^{2}−3𝑥^{2}+9.\end{aligned}


$$

So, the first derivative of $f$ is

$$


[\begin{aligned}3𝑥(𝑥−2𝑦) & 3𝑦^{2}−3𝑥^{2}+9\end{aligned}]


$$

To find the critical points, we need to find the points $(x,y) \in \mathbb{R}^2$ such that $\boldsymbol f'(x,y) = \mathbf{0}^T$ or $\boldsymbol f'(x,y)$ does not exist. Note that, in our case, $\boldsymbol f'(x,y)$ exists everywhere, so we just need to find the points where $\boldsymbol f'(x,y) = \mathbf{0}^T.$

Setting $\boldsymbol f'(x,y) = \mathbf{0}^T,$ we have the following system:

$$


\begin{aligned}3𝑥(𝑥−2𝑦)=0 \\ 3𝑦^{2}−3𝑥^{2}+9=0\end{aligned}


$$

From the first equation, we obtain $x=0$ or $x=2y.$ Now, we substitute these values into the second equation.

- For $x=0,$ we get but this last equation has no real solution.

- For $x = 2y,$ we obtain Substituting these values into $x = 2y,$ we get

Therefore, our system has two solutions, $(-2,-1)$ and $(2,1).$

In conclusion, $f$ has two critical points, $(-2,-1)$ and $(2,1).$ Note that since $\boldsymbol f'(\mathbf{x}) = \mathbf 0^T$ at these two points, they are also both stationary points.

### Classifying Stationary Points

Recall that, for functions of two variables $f(x,y)$, there are typically three possible types of critical points that can occur:

- Local minimum points. For example, the elliptic paraboloid $z = f(x,y) = x^2+y^2$ has a minimum point at $(0,0),$ as shown below.

- Local maximum points. For example, the elliptic paraboloid $z = f(x,y) = -x^2-y^2$ has a maximum point at $(0,0),$ as shown below.

- Saddle points. For example, the hyperbolic paraboloid $z = f(x,y) = y^2-x^2$ has a saddle point at $(0,0),$ as shown below.

Local maximum and local minimum points are analogous to what you would have seen in single-variable calculus.

A saddle point occurs when the slopes are zero in all directions, yet it is not a local maximum or minimum. The hyperbolic paraboloid shown above reaches a local maximum at $(0,0)$ along the $xz$-plane, yet this is a local minimum along the $yz$-plane.

### The Second Partial Derivatives Test

The **second partial derivatives test** helps to determine whether a stationary point of a function of two variables gives rise to a local maximum, a local minimum, or a saddle point.

Suppose that $\mathbf x = \mathbf{a}$ is a critical point of $f(\mathbf x),$ and let $H(\mathbf{a})$ denote the determinant of $\boldsymbol f''(x,y)$ evaluated at $\mathbf{a}$ (recall that $H(\mathbf a)$ is called the *Hessian determinant* of $f$ at $\mathbf a$).

The second partial derivative test states the following:

- If $H(\mathbf{a}) > 0,$ then: if $\dfrac{\partial^2 f}{\partial x^2}(\mathbf{a}) < 0,$ then $f$ has a local maximum at $\mathbf{a},$ and if $\dfrac{\partial^2 f}{\partial x^2}(\mathbf{a}) > 0,$ then $f$ has a local minimum at $\mathbf{a}.$

- If $H(\mathbf{a}) < 0,$ then $f$ has a saddle point at $\mathbf{a}.$

- If $H(\mathbf{a}) = 0,$ then the second partial derivatives test is inconclusive, and we need to classify the point using some other method.

As an example, consider the function $f (x, y) = 3 + 2x^2 - x y + y^2.$ Let's find the critical points of this function and then classify them using the second partial derivatives test.

We start by computing the partial derivatives:

$$


\dfrac{\partial f}{\partial x} = 4x -y, \qquad \dfrac{\partial f}{\partial y} = 2y -x


$$

The first derivative exists for any $(x,y)$ in the domain of the function, so we only need to find the stationary points. Setting $\boldsymbol f'(x,y) = \mathbf{0}^T,$ we obtain the following system:

$$


\begin{aligned}4𝑥−𝑦=0 \\ 2𝑦−𝑥=0,\end{aligned}


$$

The solution to this system is $x=0, y=0.$ Hence, $(0,0)$ is the only stationary point.

To classify this stationary point, we use the second partial derivative test.

First, we compute the second partial derivatives:

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & =\frac{𝜕}{𝜕𝑥}(4𝑥−𝑦)=4 \\ \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}} & =\frac{𝜕}{𝜕𝑦}(2𝑦−𝑥)=2 \\ \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} & =\frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥}=\frac{𝜕}{𝜕𝑥}(2𝑦−𝑥)=−1\end{aligned}


$$

So, the second derivative is

$$


\begin{aligned}𝒇^{″}(𝑥,𝑦) & =\begin{matrix}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}\end{matrix}=[\begin{matrix}4 & −1 \\ −1 & 2\end{matrix}].\end{aligned}


$$

Finally, we evaluate the second derivative at each of the stationary points and use it to categorize them:

- Evaluating the second derivative at $(0,0),$ we obtain Computing the determinant $H(0,0),$ we get Finally, since $H(0,0) > 0$ and $\dfrac{\partial^2 f}{\partial x^2}(0,0) = (\boldsymbol f''(0,0))_{11}= 4 >0,$ the function $f$ has a local minimum at $(0,0).$

In conclusion, $f(x,y)$ has a local minimum at $(0,0).$

### Example: Classifying a Critical Point Using the Second Partial Derivatives Test

#### Question

The function $f(x,y) \%= 2x + 2y - x^2 + y^2 + 2$ has the first derivative

$$


[\begin{aligned}2−2𝑥 & 2+2𝑦\end{aligned}]


$$

and has a stationary point at $(1,-1).$ If $H$ denotes the Hessian determinant of $f,$ which of the following statements are true?

1. $H(1,-1) > 0$

2. $\dfrac{\partial^2 f}{\partial x^2}(1,-1) < 0$

3. The point $(1,-1)$ is a saddle point of $f$

#### Explanation

The second partial derivative test states that if $\mathbf{a}\in\mathbb{R}^2$ is a stationary point of $f(x,y)$ with Hessian determinant $H(\mathbf a),$ we have the following:

- If $H(\mathbf{a}) > 0,$ then: if $\dfrac{\partial^2 f}{\partial x^2}(\mathbf{a}) < 0,$ then $f$ has a local maximum at $\mathbf{a}$ if $\dfrac{\partial^2 f}{\partial x^2}(\mathbf{a}) >0,$ then $f$ has a local minimum at $\mathbf{a}$

- If $H(\mathbf{a}) < 0,$ then $f$ has a saddle point at $\mathbf{a}$

- If $H(\mathbf{a}) = 0,$ then the second partial derivatives test is inconclusive.

First, we notice that since $[\begin{aligned}2−2𝑥 & 2+2𝑦\end{aligned}]$ we must have

$$


\dfrac{\partial f}{\partial x} = 2-2x, \qquad \dfrac{\partial f}{\partial y} =2+2y.


$$

Now, we compute the second partial derivatives:

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & =\frac{𝜕}{𝜕𝑥}(2−2𝑥)=−2 \\ \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}} & =\frac{𝜕}{𝜕𝑦}(2+2𝑦)=2 \\ \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} & =\frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥}=\frac{𝜕}{𝜕𝑥}(2+2𝑦)=0\end{aligned}


$$

So, the second derivative is

$$


\begin{aligned}𝒇^{″}(𝑥,𝑦) & =\begin{matrix}\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}} & \frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} \\ \frac{𝜕^{2}𝑓}{𝜕𝑦𝜕𝑥} & \frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}\end{matrix}=[\begin{matrix}−2 & 0 \\ 0 & 2\end{matrix}].\end{aligned}


$$

Evaluating the second derivative at $(1,-1),$ we obtain

$$


\begin{aligned}𝒇^{″}(1,−1)=[\begin{matrix}−2 & 0 \\ 0 & 2\end{matrix}].\end{aligned}


$$

With that in mind, let's examine our statements in turn.

- Statement I is false. Computing the determinant of $\boldsymbol f''(1,-1),$ we get

- Statement II is true. Indeed, we have $\dfrac{\partial^2 f}{\partial x^2}(1,-1) = (\boldsymbol f''(1,-1))_{11} = -2 \lt 0.$

- Statement III is true. Indeed, since $H(1,-1) < 0,$ the point $(1,-1)$ is a saddle point by the second partial derivative test.

Therefore, the correct answer is "II and III only."

### Example: Finding and Classifying All Critical Points Using the Second Partial Derivatives Test

#### Question

Find and categorize all the local extrema of the function given that

#### Explanation

The local extrema of occurs at its critical points. A point in the domain of is a critical point of if (for stationary points) or doesn't exist.

The second partial derivative test states that if is a stationary point of with Hessian determinant we have the following:

- If then: if then has a local maximum at if then has a local minimum at

- If then has a saddle point at

- If then the second partial derivatives test is inconclusive.

First, notice that since we must have

The first derivative exists for any in the domain of the function, so we only need to find the stationary points. Setting we obtain the following system:

Solving the first equation for we get

Solving the second equation for we get

Hence, and are stationary points of

To classify these stationary points, we use the second partial derivative test.

First, we compute the second partial derivatives:

So, the second derivative is

Finally, we evaluate the second derivative at each of the stationary points and use it to categorize them:

- Evaluating the second derivative at we obtain Computing the determinant we get Now, since and the function has a local minimum at

- Evaluating the second derivative at we obtain Computing the determinant we get Therefore, is a saddle point.

In conclusion, has a local minimum at and a saddle point at

### Relating the Second Partial Derivatives Test to the Taylor Polynomial Classification

Suppose $\mathbf{a} \in \mathbb{R}^2$ is a stationary point of a function $f(\mathbf x).$

In a previous lesson, we saw that if $H(\mathbf{a}) = \det(\boldsymbol{f}''(\mathbf{a})) \neq 0$, then we can classify $\mathbf{a}$ as follows:

- if $\boldsymbol{f}''(\mathbf{a})$ is positive definite, then $\mathbf{a}$ is a local minimum

- if $\boldsymbol{f}''(\mathbf{a})$ is negative definite, then $\mathbf{a}$ is a local maximum

- if $\boldsymbol{f}''(\mathbf{a})$ is neither positive-definite nor negative-definite, then $\mathbf{a}$ is a saddle point

The second derivatives test follows from these facts. To see why, we first recall Sylvester's criterion:

The quadratic form $\mathbf{x}^TA\mathbf{x}$ (as well as the $2\times 2$ matrix $A$) is

- positive definite if and only if $\Delta_1 > 0$ and $\Delta_2 > 0,$ and

- negative definite if and only if $\Delta_1 < 0$ and $\Delta_2 > 0,$

where $\Delta_1$ and $\Delta_2$ are the first and second principle minors of $A,$ respectively.

First, notice the following:

- The first principal minor of $\boldsymbol f''(\mathbf a)$ is

- The second principal minor of $\boldsymbol f''(\mathbf a)$ is the Hessian determinant

Knowing this, we can go through each case:

- If $H(\mathbf a) < 0,$ then $\Delta_2 < 0.$ Hence, by Sylvester's criterion, the Hessian matrix $\boldsymbol f''(\mathbf{a})$ is neither positive definite nor negative definite, and we conclude that $f$ has a saddle point at $\mathbf{a}.$

- If $H(\mathbf a) > 0,$ then $\Delta_2 > 0.$ Then: If $\Delta_1 = \dfrac{\partial^2 f}{\partial x^2} < 0,$ then $\boldsymbol f''(\mathbf{a})$ is negative definite by Sylvester's criterion, and we conclude that $f$ has a local maximum at $\mathbf{a}.$ If $\Delta_1 = \dfrac{\partial^2 f}{\partial x^2} > 0,$ then $\boldsymbol f''(\mathbf{a})$ is positive definite by Sylvester's criterion, and we conclude that $f$ has a local minimum at $\mathbf{a}.$
