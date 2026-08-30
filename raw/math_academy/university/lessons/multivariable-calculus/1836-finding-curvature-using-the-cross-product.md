# Finding Curvature Using the Cross Product

Source: https://www.mathacademy.com/topics/1836?courseId=54
Topic ID: 1836

## Prerequisites

- [Calculating the Cross Product Using Determinants](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/245-calculating-the-cross-product-using-determinants.md)
- [Introduction to Curvature](./1833-introduction-to-curvature.md)

## Lesson

### Introduction

Recall that if the curve $\mathbf r(s)$ is parametrized by arc length $s,$ then the curvature of $\mathbf{r}$ is defined as

$$


\kappa(s) = \left\| \dfrac{\text{d}\mathbf T}{\text{d}s} \right\|.


$$

Moreover, if $\mathbf r(t)$ is parametrized by a general parameter $t,$ we have the following formula for the curvature:

$$


\kappa(t) = \dfrac{\|\mathbf T'(t)\|}{\|\mathbf r'(t)\|}


$$

where $\mathbf T(t) = \dfrac{\mathbf r'(t)}{\|\mathbf r'(t)\|}$ is the unit tangent vector to the curve.

It can be shown that the curvature of $\mathbf r(t)$ can also be found using the following cross product formula:

$$


\kappa(t) = \dfrac{\|\mathbf r'(t) \times \mathbf r''(t)\|}{\|\mathbf r'(t)\|^3}


$$

We'll derive this formula at the end of the lesson. For now, let's get some practice at applying it.

### Example: Finding the Curvature of a Curve at a Point

#### Question

Using the cross product curvature formula, find the curvature of $\mathbf r(t) = \langle t, -2t, t^2 \rangle$ at the point where $t = 1.$

#### Explanation

To compute the curvature $\kappa (t),$ we will use the following formula:

$$


\kappa(t) = \dfrac{\| \mathbf r'(t) \times \mathbf r''(t) \|}{\|\mathbf r'(t)\|^3}


$$

First, we calculate $\mathbf r'(t),$ $\mathbf r'(1),$ and $\|\mathbf r'(1)\|\mathbin{:}$

$$


\begin{aligned}𝐫^{′}(𝑡) & =⟨\frac{d}{d𝑡}(𝑡),\frac{d}{d𝑡}(−2𝑡),\frac{d}{d𝑡}(𝑡^{2})⟩ \\ & =⟨1,\,−2,\,2𝑡⟩ \\ 𝐫^{′}(1) & =⟨1,−2,2⟩ \\ ‖𝐫^{′}(1)‖ & =\sqrt{1^{2}+(−2)^{2}+2^{2}} \\ & =\sqrt{9} \\ & =3\end{aligned}


$$

Now, we find $\mathbf r''(t)$ and $\mathbf r''(1)\mathbin{:}$

$$


\begin{aligned}𝐫^{″}(𝑡) & =⟨\frac{d}{d𝑡}(1),\frac{d}{d𝑡}(−2),2\frac{d}{d𝑡}(𝑡)⟩ \\ & =⟨0,0,2⟩ \\ 𝐫^{″}(1) & =⟨0,0,2⟩\end{aligned}


$$

Next, we compute the cross product and its magnitude:

$$


\begin{aligned}𝐫^{′}(1)×𝐫^{″}(1) & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 1 & −2 & 2 \\ 0 & 0 & 2\end{matrix} \\ & =\begin{matrix}−2 & 2 \\ 0 & 2\end{matrix}𝐢−\begin{matrix}1 & 2 \\ 0 & 2\end{matrix}𝐣+\begin{matrix}1 & −2 \\ 0 & 0\end{matrix}𝐤 \\ & =−4\,𝐢−2\,𝐣 \\ ‖𝐫^{′}(1)×𝐫^{″}(1)‖ & =\sqrt{(−4)^{2}+(−2)^{2}+0^{2}} \\ & =\sqrt{20} \\ & =2\sqrt{5}\end{aligned}


$$

Therefore, the curvature at $t=1$ is

$$


\begin{aligned}𝜅(1) & =\frac{‖𝐫^{′}(1)×𝐫^{″}(1)‖}{‖𝐫^{′}(1)‖^{3}}=\frac{2\sqrt{5}}{3^{3}}=\frac{2\sqrt{5}}{27}.\end{aligned}


$$

### Example: Finding the Curvature of a Curve at a General Point

#### Question

Given the curve $\mathbf r(t)=\left\langle t^2, \: 2t, \: 1 \right\rangle$, use the cross product curvature formula to find the curvature of this curve as a function of $t.$

#### Explanation

The curvature $\kappa (t)$ is given by

$$


\kappa(t) = \dfrac{\| \mathbf r'(t) \times \mathbf r''(t) \|}{\|\mathbf r'(t)\|^3} .


$$

First, we calculate $\mathbf r'(t)$ and $\| \mathbf r'(t) \|\mathbin{:}$

$$


\begin{aligned}𝐫^{′}(𝑡) & =⟨\frac{d}{d𝑡}(𝑡^{2}),\,\frac{d}{d𝑡}(2𝑡),\,\frac{d}{d𝑡}(1)⟩ \\ & =⟨2𝑡,\,2,\,0⟩ \\ ‖𝐫^{′}(𝑡)‖ & =\sqrt{(2𝑡)^{2}+(2)^{2}+0^{2}} \\ & =\sqrt{4𝑡^{2}+4} \\ & =\sqrt{4(𝑡^{2}+1)} \\ & =2\sqrt{𝑡^{2}+1}\end{aligned}


$$

Next, we find the second derivative $\mathbf{r}''(t)\mathbin{:}$

$$


\begin{aligned}𝐫^{″}(𝑡) & =⟨\frac{d}{d𝑡}(2𝑡),\,\frac{d}{d𝑡}(2),\,\frac{d}{d𝑡}(0)⟩=⟨2,\,0,\,0⟩\end{aligned}


$$

Now, we compute the cross-product:

$$


\begin{aligned}𝐫^{′}(𝑡)×𝐫^{″}(𝑡) & =⟨2𝑡,2,0⟩×⟨2,0,0⟩ \\ & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 2𝑡 & 2 & 0 \\ 2 & 0 & 0\end{matrix} \\ & =\begin{matrix}2 & 0 \\ 0 & 0\end{matrix}𝐢−\begin{matrix}2𝑡 & 0 \\ 2 & 0\end{matrix}𝐣+\begin{matrix}2𝑡 & 2 \\ 2 & 0\end{matrix}𝐤 \\ & =−4\,𝐤\end{aligned}


$$

Then, we compute the magnitude of the above:

$$


\begin{aligned}‖𝐫^{′}(𝑡)×𝐫^{″}(𝑡)‖ & =4\end{aligned}


$$

Therefore, the curvature is

$$


\begin{aligned}𝜅(𝑡) & =\frac{‖𝐫^{′}(𝑡)×𝐫^{″}(𝑡)‖}{‖𝐫^{′}(𝑡)‖^{3}}=\frac{4}{8(𝑡^{2}+1)^{3/2}}=\frac{1}{2(𝑡^{2}+1)^{3/2}}.\end{aligned}


$$

### Applying the Cross Product Formula to Plane Curves

Suppose we have a plane curve $C$ that is parametrized by the vector-valued function

$$


\mathbf{r}(t) = \langle x(t), \: y(t) \rangle.


$$

At first glance, it looks as though the cross product curvature formula cannot be applied since cross products apply to three-dimensional vectors, whereas the given vector $\mathbf{r}(t)$ has only two dimensions.

However, this curve can also be viewed as a curve in three-dimensional space that lies on the plane $z=0.$ In this case, $\mathbf{r}(t)$ can be considered as a vector-valued function with $z$-component equal to zero:

$$


\mathbf r(t)= \langle x(t), \: y(t), \: 0 \rangle


$$

As a result, the curvature $\kappa$ of our plane curve $C$ can be calculated using our cross product formula:

$$


\kappa(t)=\dfrac{\|{\mathbf{r}^{\prime}(t)}\times {\mathbf{r}^{\prime\prime}(t)}\|}{\|{\mathbf{r}^{\prime}(t)}\|^3}


$$

### Example: Finding the Curvature of a Plane Curve

#### Question

Using the cross product formula for curvature, find the curvature of $\mathbf r(t) = \langle 2t, 1+t^2\rangle$ as a function of $t.$

#### Explanation

To compute the curvature $\kappa (t),$ we will use the following formula:

$$


\kappa(t) = \dfrac{\| \mathbf r'(t) \times \mathbf r''(t) \|}{\|\mathbf r'(t)\|^3}


$$

First, we calculate $\mathbf r'(t)$ and $\|\mathbf r'(t)\|\mathbin{:}$

$$


\begin{aligned}𝐫^{′}(𝑡) & =⟨\frac{d}{d𝑡}(2𝑡),\,\frac{d}{d𝑡}(1+𝑡^{2})⟩ \\ & =⟨2,\,2𝑡⟩ \\ ‖𝐫^{′}(𝑡)‖ & =\sqrt{2^{2}+(2𝑡)^{2}} \\ & =\sqrt{4+4𝑡^{2}} \\ & =2\sqrt{1+𝑡^{2}}\end{aligned}


$$

Now, we find the second derivative:

$$


\begin{aligned}𝐫^{″}(𝑡) & =⟨\frac{d}{d𝑡}(2),\,\frac{d}{d𝑡}(2𝑡)⟩=⟨0,2⟩\end{aligned}


$$

Next, we compute the cross product by considering $\mathbf r'(t)$ and $\mathbf r''(t)$ as $3$-dimensional vectors with zero $z$-components:

$$


\begin{aligned}𝐫^{′}(𝑡)×𝐫^{″}(𝑡) & =⟨2,\,2𝑡,0⟩×⟨0,\,2,\,0⟩ \\ & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 2 & 2𝑡 & 0 \\ 0 & 2 & 0\end{matrix} \\ & =\begin{matrix}2 & 2𝑡 \\ 0 & 2\end{matrix}\,𝐤 \\ & =4\,𝐤\end{aligned}


$$

So, the magnitude of the cross product is

$$


\| \mathbf r'(t) \times \mathbf r''(t) \| = 4,


$$

and therefore, the curvature is

$$


\begin{aligned}𝜅(𝑡) & =\frac{‖𝐫^{′}(𝑡)×𝐫^{″}(𝑡)‖}{‖𝐫^{′}(𝑡)‖^{3}}=\frac{4}{(2\sqrt{1+𝑡^{2}})^{3}}=\frac{1}{2(1+𝑡^{2})^{3/2}}\,.\end{aligned}


$$

### Deriving the Cross Product Formula

Recall that if the curve $\mathbf r(t)$ is parametrized by a general parameter $t,$ then the curvature of $\mathbf{r}$ is given by

$$


\kappa(t) = \dfrac{\|\mathbf T'(t)\|}{\|\mathbf r'(t)\|},


$$

where $\mathbf T(t) = \dfrac{\mathbf r'(t)}{\|\mathbf r'(t)\|}$ is the unit tangent vector to the curve.

Here, $\mathbf r'(t)$ is a vector function and $\|\mathbf r'(t)\|$ is a scalar function. So, we differentiate $\mathbf T(t)$ by using the chain rule:

$$


\begin{aligned}𝐓^{′}(𝑡) & =\frac{𝜕}{𝜕𝑡}(𝐓) \\ & =\frac{𝜕}{𝜕𝑡}(\frac{𝐫^{′}(𝑡)}{‖𝐫^{′}(𝑡)‖}) \\ & =\frac{𝜕}{𝜕𝑡}(\frac{1}{‖𝐫^{′}(𝑡)‖}⋅𝐫^{′}(𝑡)) \\ & =\frac{𝜕}{𝜕𝑡}(\frac{1}{‖𝐫^{′}(𝑡)‖})⋅𝐫^{′}(𝑡)+\frac{1}{‖𝐫^{′}(𝑡)‖}⋅\frac{𝜕}{𝜕𝑡}(𝐫^{′}(𝑡)) \\ & =\frac{𝜕}{𝜕𝑡}(\frac{1}{‖𝐫^{′}(𝑡)‖})⋅𝐫^{′}(𝑡)+\frac{1}{‖𝐫^{′}(𝑡)‖}⋅𝐫^{″}(𝑡)\end{aligned}


$$

Now, since the cross product of a vector with itself equals $\mathbf{0},$ we get

$$


\begin{aligned}𝐓(𝑡)×𝐓^{′}(𝑡) & =\frac{𝐫^{′}(𝑡)}{‖𝐫^{′}(𝑡)‖}×(\frac{𝜕}{𝜕𝑡}(\frac{1}{‖𝐫^{′}(𝑡)‖})⋅𝐫^{′}(𝑡)+\frac{1}{‖𝐫^{′}(𝑡)‖}⋅𝐫^{″}(𝑡)) \\ & =\frac{1}{‖𝐫^{′}(𝑡)‖^{2}}\,(𝐫^{′}(𝑡)×𝐫^{″}(𝑡)).\end{aligned}


$$

Next, we find the magnitude of both sides and use the fact that $\mathbf T$ is a unit vector:

$$


\begin{aligned}‖𝐓(𝑡)×𝐓^{′}(𝑡)‖ & =\frac{1}{‖𝐫^{′}(𝑡)‖^{2}}\,𝐫^{′}(𝑡)×𝐫^{″}(𝑡) \\ ‖𝐓(𝑡)‖⋅‖𝐓^{′}(𝑡)‖ & =\frac{1}{‖𝐫^{′}(𝑡)‖^{2}}\,𝐫^{′}(𝑡)×𝐫^{″}(𝑡) \\ 1⋅‖𝐓^{′}(𝑡)‖ & =\frac{1}{‖𝐫^{′}(𝑡)‖^{2}}\,𝐫^{′}(𝑡)×𝐫^{″}(𝑡) \\ ‖𝐓^{′}(𝑡)‖ & =\frac{∥𝐫^{′}(𝑡)×𝐫^{″}(𝑡)∥}{‖𝐫^{′}(𝑡)‖^{2}}\end{aligned}


$$

Therefore,

$$


\kappa(t) = \dfrac{\|\mathbf T'(t)\|}{\|\mathbf r'(t)\|} = \dfrac{\left\| \mathbf r'(t) \times \mathbf r''(t) \right\|}{\|\mathbf r'(t)\|^3}.


$$
