# The Curvature of a Plane Curve

Source: https://www.mathacademy.com/topics/1839?courseId=154
Topic ID: 1839

## Prerequisites

- [Radius of Curvature](./1834-radius-of-curvature.md)
- [Relating Concavity to the Second Derivative](../ap-calculus-ab/3846-relating-concavity-to-the-second-derivative.md)

## Lesson

### Introduction

For a plane curve $C$ defined by the vector-valued function

$$


\mathbf r(t) = \langle x(t), \: y(t) \rangle,


$$

the *curvature* of $C$ at an arbitrary point can be found using the following formula:

$$


\kappa(t) = \dfrac{|x'(t)y''(t) - y'(t)x''(t)|}{ (x'(t)^2 + y'(t)^2)^{3/2}}


$$

Additionally, the **signed curvature** $k$ is given by

$$


k(t) = \dfrac{x'(t)y''(t) - y'(t)x''(t)}{ (x'(t)^2 + y'(t)^2)^{3/2}}.


$$

For example, consider a curve defined by the parametric equations

$$


x(t) = 2t, \qquad y(t) = 1+t^2.


$$

Let's find the curvature of this curve at the point where $t=1.$

First, we calculate the first and second derivatives of the components:

$$


\begin{aligned} & 𝑥^{′}(𝑡)=2,\, & 𝑦^{′}(𝑡)=2𝑡 \\ & 𝑥^{″}(𝑡)=0,\, & 𝑦^{″}(𝑡)=2\end{aligned}


$$

Substituting these expressions into our curvature formula, we get the following:

$$


\begin{aligned}𝜅(𝑡) & =\frac{|2⋅2−2𝑡⋅0|}{[2^{2}+(2𝑡)^{2}]^{3/2}} \\ & =\frac{|\,4\,|}{2^{3}[1+𝑡^{2}]^{3/2}} \\ & =\frac{1}{2(𝑡^{2}+1)^{3/2}}.\end{aligned}


$$

Therefore, the curvature at $t =1$ is

$$


\begin{aligned}𝜅(1) & =\frac{1}{2(1^{2}+1)^{3/2}} \\ & =\frac{1}{4\sqrt{√2}} \\ & =\frac{\sqrt{√2}}{8}.\end{aligned}


$$

### Example: Finding the Curvature of a Plane Curve Given in Parametric Form

#### Question

The signed curvature of the plane curve $\mathbf r(t) = \big\langle t, \: \sin t \big\rangle$ is given by

$$


k (t) = \dfrac{\boxed{\phantom{AA}}}{\sqrt{ (1+\cos^2 t)^3 } }, \quad t\neq 0.


$$

What is the missing part of the expression?

#### Explanation

The signed curvature $k(t)$ of a plane curve $\mathbf r(t) = \left \langle x(t), y(t) \right \rangle$ is given by

$$


k (t) = \dfrac {x'(t) y''(t) - y'(t) x''(t)} {\big([x'(t)]^2 + [y'(t)]^2\big)^{3/2}}.


$$

Along our curve, we have

$$


x(t) = t, \qquad y(t) = \sin t.


$$

First, we calculate the derivatives of the components:

$$


\begin{aligned}𝑥^{′}(𝑡) & =1,\, & 𝑦^{′}(𝑡) & =cos⁡𝑡 \\ 𝑥^{″}(𝑡) & =0,\, & 𝑦^{″}(𝑡) & =−sin⁡𝑡\end{aligned}


$$

Substituting these into the formula for the signed curvature, we get:

$$


\begin{aligned}𝑘(𝑡) & =\frac{1⋅(−sin⁡𝑡)−0⋅cos⁡𝑡}{(1^{2}+(cos⁡𝑡)^{2})^{3/2}} \\ & =\frac{−sin⁡𝑡}{(1+cos^{2}⁡𝑡)^{3/2}} \\ & =\frac{−sin⁡𝑡}{\sqrt{√(1+cos^{2}⁡𝑡)^{3}}}\end{aligned}


$$

### Example: Finding the Radius of Curvature of a Plane Curve Given in Parametric Form

#### Question

Find the radius of curvature for the curve $\mathbf r(t) = t \, \mathbf i + \sin t\, \mathbf j$ at $t = \dfrac \pi 2.$

#### Explanation

The curvature $\kappa(t)$ of a plane curve $\mathbf r(t) = x(t) \, \mathbf i + y(t)\,\mathbf j$ is given by

$$


\kappa (t) = \dfrac {|x'(t) y''(t) - y'(t) x''(t)|} {\big([x'(t)]^2 + [y'(t)]^2\big)^{3/2}}.


$$

The radius of curvature $R$ is defined as $R(t) = \dfrac 1 {\kappa(t)}.$

Along our curve, we have

$$


x(t) = t, \qquad y(t) = \sin t.


$$

First, we calculate the derivatives of the components:

$$


\begin{aligned}𝑥^{′}(𝑡) & =1,\, & 𝑦^{′}(𝑡) & =cos⁡𝑡 \\ 𝑥^{″}(𝑡) & =0,\, & 𝑦^{″}(𝑡) & =−sin⁡𝑡\end{aligned}


$$

Substituting these into the formula for the curvature, we get the following:

$$


\begin{aligned}𝜅(𝑡) & =\frac{|1⋅(−sin⁡𝑡)−cos⁡𝑡⋅0|}{(1^{2}+(cos⁡𝑡)^{2})^{3/2}} \\ & =\frac{|sin⁡𝑡|}{(1+cos^{2}⁡𝑡)^{3/2}}\end{aligned}


$$

Therefore, the curvature at $t = \dfrac{\pi}2$ is

$$


\begin{aligned}𝜅(\frac{𝜋}{2}) & =\frac{sin⁡(\frac{𝜋}{2})}{2} \\ & =\frac{1}{(1+0^{2})^{3/2}} \\ & =1.\end{aligned}


$$

Finally, the radius of curvature at $t = \dfrac{\pi}2$ is

$$


\begin{aligned}𝑅(\frac{𝜋}{2}) & =\frac{1}{𝜅(\frac{𝜋}{2})}=1.\end{aligned}


$$

### The Curvature of a Plane Curve Given in Cartesian Form

Suppose we have a plane curve defined by the explicit equation

$$


y = y(x).


$$

In this case, we can parametrize this curve as follows:

$$


\mathbf r(t) = \langle t, \: y(t) \rangle.


$$

Now, using the fact that $x=t,$ we calculate the first and second derivatives of the components:

$$


\begin{aligned}𝑥^{′}(𝑡) & =1,\, & 𝑦^{′}(𝑡) & =𝑦^{′}(𝑥) \\ 𝑥^{″}(𝑡) & =0,\, & 𝑦^{″}(𝑡) & =𝑦^{″}(𝑥)\end{aligned}


$$

Substituting these into the formula for the (unsigned) curvature, we get

$$


\begin{aligned}𝜅(𝑥) & =\frac{|𝑥^{′}(𝑡)𝑦^{″}(𝑡)−𝑦^{′}(𝑡)𝑥^{″}(𝑡)|}{([𝑥^{′}(𝑡)]^{2}+[𝑦^{′}(𝑡)]^{2})^{3/2}} \\ & =\frac{|1⋅𝑦^{″}(𝑥)−𝑦^{′}(𝑥)⋅0|}{(1^{2}+[𝑦^{′}(𝑥)]^{2})^{3/2}} \\ & =\frac{|𝑦^{″}(𝑥)|}{(1+[𝑦^{′}(𝑥)]^{2})^{3/2}}\,.\end{aligned}


$$

Therefore, the unsigned curvature for $y=y(x)$ is given by

$$


\kappa (x) = \dfrac{|y''(x)|}{ (1 + [y'(x)]^2)^{3/2}}


$$

and the signed curvature is

$$


k(x) = \dfrac {y''(x)} {(1+[y'(x)]^2)^{3/2}} .


$$

Note that the signed curvature $k(x)$ has the same sign as $y''(x).$ Therefore,

- if $k(x) > 0,$ the curve is concave up, and

- if $k(x) < 0,$ the curve is concave down.

### Example: Finding the Curvature of a Plane Curve Given in Cartesian Form

#### Question

Find the curvature of the curve $y = x^3$ at $x=-1.$

#### Explanation

The curvature $\kappa(x)$ of a plane curve $y = y(x)$ is given by

$$


\kappa(x) = \dfrac {|y''(x)|} {(1+[y'(x)]^2)^{3/2}}.


$$

First, we calculate $y'(x)$ and $y''(x){:}$

$$


\begin{aligned}𝑦^{′}(𝑥) & =3𝑥^{2},\, & 𝑦^{″}(𝑥) & =6𝑥\end{aligned}


$$

Substituting these into the formula for the curvature, we get the following:

$$


\begin{aligned}𝜅(𝑥) & =\frac{|6𝑥|}{[1+(3𝑥^{2})^{2}]^{3/2}} \\ & =\frac{|6𝑥|}{(1+9𝑥^{4})^{3/2}}\end{aligned}


$$

Therefore, the curvature at $x=-1$ is

$$


\begin{aligned}𝜅(−1) & =\frac{|6(−1)|}{(1+9(−1)^{4})^{3/2}} \\ & =\frac{|−6|}{(1+9)^{3/2}} \\ & =\frac{6}{10^{3/2}} \\ & =\frac{6}{10\sqrt{√10}} \\ & =\frac{3\sqrt{√10}}{50}.\end{aligned}


$$

### Deriving the Formula for the Curvature of a Plane Parametric Curve

We've been using the following formula for unsigned curvature:

$$


\kappa (t) = \dfrac{|x'(t)y''(t) - y'(t)x''(t)|}{ (x'(t)^2 + y'(t)^2)^{3/2}}


$$

To see where this formula comes from, remember that for a curve $\mathbf r(t) = \langle x(t), y(t), z(t)\rangle,$ the unsigned curvature formula is

$$


\kappa(t) = \dfrac{\|\mathbf r'(t) \times \mathbf r''(t)\|}{\|\mathbf r'(t)\|^3}.


$$

If a curve does not have a $z$-component, then we may consider $z(t) = 0.$ Thus, any plane curve $\mathbf r(t) = \langle x(t), \: y(t) \rangle$ can be represented as

$$


\mathbf r(t) = \langle x(t), \: y(t), \: 0\rangle.


$$

First, we calculate $\mathbf r'(t)$ and $\mathbf r''(t)\mathbin{:}$

$$


\mathbf r'(t) = \langle x'(t), y'(t),0 \rangle, \qquad \mathbf r''(t) = \langle x''(t), y''(y),0 \rangle


$$

Substituting these expressions into our cross-product formula, we find that the curvature $\kappa(t)$ is given by

$$


\begin{aligned}𝜅(𝑡) & =\frac{‖𝐫^{′}(𝑡)×𝐫^{″}(𝑡)‖}{‖𝐫^{′}(𝑡)‖^{3}} \\ & =\frac{‖⟨𝑥^{′}(𝑡),𝑦^{′}(𝑡),0⟩×⟨𝑥^{″}(𝑡),𝑦^{″}(𝑡),0⟩‖}{‖⟨𝑥^{′}(𝑡),𝑦^{′}(𝑡)⟩‖^{3}} \\ & =\frac{‖⟨0,0,𝑥^{′}(𝑡)𝑦^{″}(𝑡)−𝑦^{′}(𝑡)𝑥^{″}(𝑡)⟩‖}{(\sqrt{√𝑥^{′}(𝑡)^{2}+𝑦^{′}(𝑡)^{2}})^{3}} \\ & =\frac{|𝑥^{′}(𝑡)𝑦^{″}(𝑡)−𝑦^{′}(𝑡)𝑥^{″}(𝑡)|}{(𝑥^{′}(𝑡)^{2}+𝑦^{′}(𝑡)^{2})^{3/2}}.\end{aligned}


$$
