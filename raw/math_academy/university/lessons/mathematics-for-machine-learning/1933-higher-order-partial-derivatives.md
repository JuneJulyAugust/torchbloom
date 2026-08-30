# Higher-Order Partial Derivatives

Source: https://www.mathacademy.com/topics/1933?courseId=145
Topic ID: 1933

## Prerequisites

- [Computing Partial Derivatives Using the Rules of Differentiation](./4096-computing-partial-derivatives-using-the-rules-of-differentiation.md)

## Lesson

### Introduction

Just like we can compute second derivatives of single-variable functions, we can also compute second derivatives of multivariable functions.

For example, consider the two-variable function

$$


f (x, y)= x y^2 + e^{xy}.


$$

Its two first-order partial derivatives are

$$


\begin{aligned}𝑓_{𝑥}(𝑥,𝑦) & =𝑦^{2}+𝑦𝑒^{𝑥𝑦}, \\ 𝑓_{𝑦}(𝑥,𝑦) & =2𝑥𝑦+𝑥𝑒^{𝑥𝑦}.\end{aligned}


$$

Since $f_x(x,y)$ and $f_y(x,y)$ are themselves functions that are differentiable with respect to both $x$ and $y,$ we can compute the **second-order partial derivatives** as well.

- The partial derivatives of $f_x(x,y)$ with respect to $x$ and $y,$ denoted $f_{xx}$ and $f_{xy}$ respectively, are

- The partial derivatives of $f_y(x,y)$ with respect to $x$ and $y,$ denoted $f_{yx}$ and $f_{yy}$ respectively, are

The partial derivatives $f_{xy}$ and $f_{yx}$ are called **mixed partial derivatives** because they involve taking the partial derivatives with respect to different variables, $x$ and $y.$

The following alternative notations are also widely used to represent second-order partial derivatives:

$$


\begin{aligned}\frac{𝜕^{2}}{𝜕𝑥^{2}}(𝑓) & =\frac{𝜕^{2}𝑓}{𝜕𝑥^{2}}=𝑓_{𝑥𝑥}\,\,\,\,\,\frac{𝜕^{2}}{𝜕𝑦^{2}}(𝑓)=\frac{𝜕^{2}𝑓}{𝜕𝑦^{2}}=𝑓_{𝑦𝑦} \\ \frac{𝜕^{2}}{𝜕𝑦\,𝜕𝑥}(𝑓) & =\frac{𝜕^{2}𝑓}{𝜕𝑦\,𝜕𝑥}=𝑓_{𝑥𝑦}\,\frac{𝜕^{2}}{𝜕𝑥\,𝜕𝑦}(𝑓)=\frac{𝜕^{2}𝑓}{𝜕𝑥\,𝜕𝑦}=𝑓_{𝑦𝑥}\end{aligned}


$$

**Note:** In our example, the two mixed partial derivatives were equal:

$$


f_{xy}(x,y) = 2y + xye^{xy} + e^{xy} = f_{yx}(x,y)


$$

Later, we will see that under rather mild conditions on $f,$ we almost always have that $f_{xy}=f_{yx}.$

### Example: Finding Mixed Second-Order Partial Derivatives

#### Question

Find $\dfrac {\partial^2 f}{\partial x\partial y}$ given that $\dfrac {\partial f}{\partial y} = \dfrac {2y} {x + y^2}.$

#### Explanation

To find $\dfrac {\partial^2 f}{\partial x\partial y},$ we differentiate the given first-order partial derivative $\dfrac {\partial f}{\partial y}$ with respect to $x\mathbin{:}$

$$


\begin{aligned}\frac{𝜕^{2}𝑓}{𝜕𝑥𝜕𝑦} & =\frac{𝜕}{𝜕𝑥}(\frac{𝜕𝑓}{𝜕𝑦}) \\ & =\frac{𝜕}{𝜕𝑥}(\frac{2𝑦}{𝑥+𝑦^{2}}) \\ & =2𝑦⋅\frac{𝜕}{𝜕𝑥}((𝑥+𝑦^{2})^{−1}) \\ & =−2𝑦(𝑥+𝑦^{2})^{−2}⋅1 \\ & =−\frac{2𝑦}{(𝑥+𝑦^{2})^{2}}\end{aligned}


$$

### Example: Computing Expressions Involving Second-Order Partial Derivatives

#### Question

Find $f_{xy}(x,y)+f_{yx}(x,y)$ given that $f_x(x,y)=y\cos(xy)$ and $f_y(x,y)=x\cos(xy).$

#### Explanation

To find $f_{xy}(x,y),$ we differentiate the given first-order partial derivative $f_{x}(x,y)$ with respect to $y\mathbin{:}$

$$


\begin{aligned}𝑓_{𝑥𝑦}(𝑥,𝑦) & =\frac{𝜕}{𝜕𝑦}(𝑓_{𝑥}(𝑥,𝑦)) \\ & =\frac{𝜕}{𝜕𝑦}(𝑦cos⁡(𝑥𝑦)) \\ & =1⋅cos⁡(𝑥𝑦)+𝑦(−sin⁡(𝑥𝑦)⋅𝑥) \\ & =cos⁡(𝑥𝑦)−𝑥𝑦sin⁡(𝑥𝑦)\end{aligned}


$$

Similarly, to find $f_{yx}(x,y),$ we differentiate the given first-order partial derivative $f_{y}(x,y)$ with respect to $x\mathbin{:}$

$$


\begin{aligned}𝑓_{𝑦𝑥}(𝑥,𝑦) & =\frac{𝜕}{𝜕𝑥}(𝑓_{𝑦}(𝑥,𝑦)) \\ & =\frac{𝜕}{𝜕𝑥}(𝑥cos⁡(𝑥𝑦)) \\ & =1⋅cos⁡(𝑥𝑦)+𝑥(−sin⁡(𝑥𝑦)⋅𝑦) \\ & =cos⁡(𝑥𝑦)−𝑥𝑦sin⁡(𝑥𝑦)\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}𝑓_{𝑥𝑦}(𝑥,𝑦)+𝑓_{𝑦𝑥}(𝑥,𝑦) & =cos⁡(𝑥𝑦)−𝑥𝑦sin⁡(𝑥𝑦)+cos⁡(𝑥𝑦)−𝑥𝑦sin⁡(𝑥𝑦) \\ & =2(cos⁡(𝑥𝑦)−𝑥𝑦sin⁡(𝑥𝑦)).\end{aligned}


$$

### Higher-Order Partial Derivatives for Functions of More Than Two Variables

We can also define other **higher order partial derivatives** such as $f_{xxy}, \, f_{xxyy}, \, f_{xyxy},$ etc.

For instance, the function $f(x,y,z)= z\cos(xy)$ has the first-order partial derivative

$$


f_y(x,y,z) = -xz \sin(xy)


$$

and the second-order partial derivative

$$


f_{yx}(x,y,z)= -x yz \cos{\left(x y \right)} - z\sin{\left(x y \right)}.


$$

If we differentiate again, with respect to $x,$ then we get the **third-order partial derivative** $f_{yxx}\mathbin{:}$

$$


\begin{aligned}𝑓_{𝑦𝑥𝑥}(𝑥,𝑦,𝑧) & =\frac{𝜕}{𝜕𝑥}(𝑓_{𝑦𝑥}(𝑥,𝑦)) \\ & =\frac{𝜕}{𝜕𝑥}(−𝑥𝑦𝑧cos⁡(𝑥𝑦)−𝑧sin⁡(𝑥𝑦)) \\ & =−𝑦𝑧cos⁡(𝑥𝑦)−𝑥𝑦𝑧(−sin⁡(𝑥𝑦)⋅𝑦)−𝑧cos⁡(𝑥𝑦)⋅𝑦 \\ & =𝑥𝑦^{2}𝑧sin⁡(𝑥𝑦)−2𝑦𝑧cos⁡(𝑥𝑦)\end{aligned}


$$

In general, to compute a $n$th-order partial derivative, we need to compute a sequence of $n$ individual derivatives.

### Example: Finding Higher-Order Derivatives

#### Question

Evaluate $g_{xyz}(x,y,z)$ at $(1,2,3)$ if $g_x(x,y,z) = 2x y z + y^3.$

#### Explanation

First, we find $g_{xy}(x,y,z)$ by differentiating $g_{x}(x,y,z)$ with respect to $y\mathbin{:}$

$$


\begin{aligned}𝑔_{𝑥𝑦}(𝑥,𝑦,𝑧) & =\frac{𝜕}{𝜕𝑦}(2𝑥𝑦𝑧+𝑦^{3}) \\ & =2𝑥𝑧+3𝑦^{2}\end{aligned}


$$

Next, we find $g_{xyz}(x,y,z)$ by differentiating $g_{xy}(x,y,z)$ with respect to $z\mathbin{:}$

$$


\begin{aligned}𝑔_{𝑥𝑦𝑧}(𝑥,𝑦,𝑧) & =\frac{𝜕}{𝜕𝑧}(2𝑥𝑧+3𝑦^{2}) \\ & =2𝑥\end{aligned}


$$

Finally, we obtain

$$


\begin{aligned}𝑔_{𝑥𝑦𝑧}(1,2,3) & =2(1) \\ & =2.\end{aligned}


$$
