# Partial Differentiability of Multivariable Functions

Source: https://www.mathacademy.com/topics/1932?courseId=145
Topic ID: 1932

## Prerequisites

- [Computing Partial Derivatives Using the Rules of Differentiation](./4096-computing-partial-derivatives-using-the-rules-of-differentiation.md)

## Lesson

### Introduction

The partial derivative of a function exists where the original function is defined *and* the partial derivative is defined.

For example, let's consider the function $f(x,y) = \ln(xy).$ We wish to determine the set of values $(x,y)$ on which the partial derivative $\dfrac{\partial f}{\partial x}$ exists.

First, we need to find the domain of $f$ since we cannot differentiate $f$ at any point that lies outside of its domain. The natural logarithm is defined only for positive inputs, so the domain of $f$ is

$$


D_f = \{ (x,y)\, : \, xy > 0 \}.


$$

Next, we compute the partial derivative:

$$


\dfrac{\partial f}{\partial x} = \dfrac{1}{x}


$$

The partial derivative $\dfrac{\partial f}{\partial x}$ (also denoted $f_x$) is not defined at $x=0.$ So, the domain of $f_x$ is

$$


D_{f_x} = \{ (x,y)\, : \, x \ne 0 \}.


$$

To compute the set where $\dfrac{\partial f}{\partial x}$ exists, we take the intersection of the domain of the original function $(D_f)$ with the domain of the partial derivative $(D_{f_x})$ as follows:

$$


\begin{aligned}𝐷_{𝑓}∩𝐷_{𝑓_{𝑥}} & ={(𝑥,𝑦)\,:\,𝑥𝑦>0}∩{(𝑥,𝑦)\,:\,𝑥≠0} \\ & ={(𝑥,𝑦)\,:\,𝑥𝑦>0}\end{aligned}


$$

Therefore, we conclude that $\dfrac{\partial f}{\partial x}$ exists on the set $\{(x,y)\,: \, xy \gt 0 \}.$

### Example: Finding the Domain Where a Partial Derivative Exists

#### Question

Given that $f(x,y)=\dfrac yx,$ find the set of values $(x,y)$ on which $\dfrac{\partial f}{\partial y}$ exists.

#### Explanation

Remember that the partial derivative of a function exists where the original function is defined ** the partial derivative is defined.

First, notice that $f(x,y)$ is not defined when $x=0.$ So, the domain of $f$ is

$$


D_f = \{(x,y) \, : \, x\ne 0 \}.


$$

Now, we compute the partial derivative of $f(x,y)$ with respect to $y\mathbin{:}$

$$


\begin{aligned}𝑓_{𝑦}(𝑥,𝑦) & =\frac{𝜕}{𝜕𝑦}(\frac{𝑦}{𝑥}) \\ & =\frac{1}{𝑥}\end{aligned}


$$

The partial derivative $f_y(x,y)$ is also not defined for $x=0.$ So, the domain of $f_y$ is

$$


D_{f_y} = \{(x,y) \, : \, x\ne 0 \}.


$$

To compute the set where $\dfrac{\partial f}{\partial y}$ exists, we take the intersection of the domain of the original function $(D_f)$ with the domain of the partial derivative $(D_{f_y})$ as follows:

$$


\begin{aligned}𝐷_{𝑓}∩𝐷_{𝑓_{𝑦}} & ={(𝑥,𝑦)\,:\,𝑥≠0}∩{(𝑥,𝑦)\,:\,𝑥≠0} \\ & ={(𝑥,𝑦)\,:\,𝑥≠0}\end{aligned}


$$

Therefore, we conclude that $\dfrac{\partial f}{\partial y}$ exists on the set $\{(x,y)\,: \, x \neq 0 \}.$

### Example: Finding the Domain Where All Partial Derivatives Exist

#### Question

Given that $f(x,y)= \ln\left(\dfrac{x}{y^2}\right)$ and

$$


\dfrac{\partial f}{\partial x} = \dfrac{1}{x}, \qquad \dfrac{\partial f}{\partial y} = -\dfrac{2}{y},


$$

find the set of values $(x,y)$ on which all partial derivatives of $f$ exist.

#### Explanation

Remember that the partial derivatives of a function exist where the original function is defined and the partial derivatives are defined.

First, notice that $f(x,y) = \ln\left(\dfrac{x}{y^2}\right)$ is defined only when $\dfrac{x}{y^2}>0.$ So, the domain of $f$ is

$$


D_f = \{(x,y) \, : \, x > 0, \: y \neq 0 \}.


$$

As for the partial derivatives, we have the following:

- The partial derivative $f_x(x,y) = \dfrac{1}{x}$ is defined only when $x \neq 0.$ So, the domain of $f_x$ is

- The partial derivative $f_y(x,y) = -\dfrac{2}{y}$ is defined only when $y \neq 0.$ So, the domain of $f_y$ is

Finally, we conclude that the partial derivatives of $f$ exist on the set

$$


\begin{aligned}𝐷_{𝑓}∩𝐷_{𝑓_{𝑥}}∩𝐷_{𝑓_{𝑦}} & ={(𝑥,𝑦)\,:\,𝑥>0,\,𝑦≠0}∩{(𝑥,𝑦)\,:\,𝑥≠0}∩{(𝑥,𝑦)\,:\,𝑦≠0} \\ & ={(𝑥,𝑦)\,:\,𝑥>0,\,𝑦≠0}.\end{aligned}


$$

### Example: Identifying Points Where Partial Derivatives Exist

#### Question

Which of the following statements are true regarding the function $f(x,y,z)=xz\ln{(x+y+z)}?$

1. $f_x(-1,-1,-1)$ is defined

2. $f_y(1,0,-1)$ is defined

3. $f_z(1,1,1)$ is defined

#### Explanation

First, we compute the partial derivatives of $f(x,y,z)\mathbin{:}$

$$


\begin{aligned}\frac{𝜕𝑓}{𝜕𝑥} & =𝑧ln⁡(𝑥+𝑦+𝑧)+\frac{𝑥𝑧}{𝑥+𝑦+𝑧} \\ \frac{𝜕𝑓}{𝜕𝑦} & =\frac{𝑥𝑧}{𝑥+𝑦+𝑧} \\ \frac{𝜕𝑓}{𝜕𝑧} & =𝑥ln⁡(𝑥+𝑦+𝑧)+\frac{𝑥𝑧}{𝑥+𝑦+𝑧}\end{aligned}


$$

Now, let's examine the statement one-by-one.

- Statement I is false. If we substitute $(-1,-1,-1)$ into $f,$ we get which is undefined since the logarithm exists only for positive arguments. Therefore, $f_x$ cannot exist at this point.

- Statement II is false. If we substitute $(1,0,-1)$ into $f_y,$ we get which is undefined since we have division by zero. Since the function is not defined at the point, the derivative is also undefined.

- Statement III is true. Indeed, the function $f$ is defined at $(1,1,1)\mathbin{:}$ Likewise $f_z$ is also defined at $(1,1,1)\mathbin{:}$

Therefore, the correct answer is "III only".

### Partial Differentiability Does Not Imply Continuity

From single-variable calculus, if a function $y=f(x)$ is differentiable at a point, then it is continuous at that point.

But for a multivariable function, even if all partial derivatives are defined at a certain point, it **does not mean** that the function is continuous at that point!

The reason why partial differentiability does not imply continuity in the case of a multivariable function is that

- the existence of the partial derivatives $f_x$ and $f_y$ depend only on the behavior of $f$ parallel to the $x$- and $y$-axes, whereas

- the continuity of $f$ depends on its behavior as we approach $(x_0,y_0)$ from any direction.

For example, let's consider the following multivariable function:

$$


\begin{aligned}\frac{𝑥𝑦}{𝑥^{2}+𝑦^{2}},\, & (𝑥,𝑦)≠(0,0) \\ 0, & (𝑥,𝑦)=(0,0)\end{aligned}


$$

The function $f$ is defined at the point $(0,0)\mathbin{:}$

$$


f(0,0)=0


$$

Likewise, the partial derivatives $f_x$ and $f_y$ are both defined at the point $(0,0).$ We can compute them using the limit definition of the partial derivative, as follows:

$$


\begin{aligned}𝑓_{𝑥}(0,0) & =\underset{ℎ→0}{lim}\frac{1}{ℎ}[𝑓(0+ℎ,0)−𝑓(0,0)] \\ & =\underset{ℎ→0}{lim}\frac{1}{ℎ}[\frac{(ℎ)(0)}{ℎ^{2}+0^{2}}−0] \\ & =\underset{ℎ→0}{lim}\frac{1}{ℎ}[0−0] \\ & =0 \\ 𝑓_{𝑦}(0,0) & =\underset{ℎ→0}{lim}\frac{1}{ℎ}[𝑓(0,0+ℎ)−𝑓(0,0)] \\ & =\underset{ℎ→0}{lim}\frac{1}{ℎ}[\frac{(0)(ℎ)}{0^{2}+ℎ^{2}}−0] \\ & =\underset{ℎ→0}{lim}\frac{1}{ℎ}[0−0] \\ & =0\end{aligned}


$$

So the partial derivatives both exist at $(0,0).$ We will now show that the function is not continuous at $(0,0).$

For the function $f$ to be continuous at $(0,0),$ the limit of the function must be equal to the function value, regardless of the path taken. So, we must have

$$


\lim\limits_{(x,y) \to (0,0)} f(x,y) = f(0,0) =0.


$$

However, this is not the case here. When we evaluate the limit along the path $y=x,$ we get

$$


\begin{aligned}\underset{(𝑥,𝑦)→(0,0)\,\,𝑦=𝑥}{lim}𝑓(𝑥,𝑦) & =\underset{𝑦→0}{lim}\frac{𝑥⋅𝑥}{𝑥^{2}+𝑥^{2}} \\ & =\underset{𝑦→0}{lim}\frac{𝑥^{2}}{2𝑥^{2}} \\ & =\underset{𝑦→0}{lim}\frac{1}{2} \\ & =\frac{1}{2} \\ & ≠0.\end{aligned}


$$

Therefore, our function $f(x,y)$ is *not* continuous at the point $(0,0),$ even though both of its partial derivatives exist there.
