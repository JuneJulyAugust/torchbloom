# Introduction to Curvature

Source: https://www.mathacademy.com/topics/1833?courseId=154
Topic ID: 1833

## Prerequisites

- [Parameterization by Arc Length](./1838-parameterization-by-arc-length.md)

## Lesson

### Introduction

The **curvature** of a curve measures how much the curve "bends" at a given point. It can also be thought of as a measure of how much the curve deviates from being a straight line. Curvature is denoted by the Greek letter $\kappa$ (pronounced "kappa").

If $\kappa=0$ at some point on a curve, then that curve looks like a straight line in some neighborhood of the point.

If the curve $\mathbf{r}(s)$ is parametrized by the arc length $s,$ then the curvature $\kappa$ is the magnitude of the change of direction of the unit tangent vector $\mathbf T$ per unit of arc length. That is,

$$


\kappa(s) = \left\| \dfrac{\textrm{d}\mathbf T}{\textrm{d}s} \right\|= \| \mathbf T'(s) \|.


$$

Note that $|| \mathbf v ||$ denotes the magnitude of the vector $\mathbf v.$

For example, suppose we are given the curve

$$


\mathbf r(s)= \left\langle \sin\left(\dfrac s2\right), \: \dfrac{\sqrt{3}s}{2}, \: -\cos\left(\dfrac s2\right)\right\rangle


$$

which is parametrized by arc length $s.$ Let's find the curvature of $\mathbf r(s)$ at the point where $s={\pi}.$

First, we find the unit tangent vector:

$$


\mathbf T(s) =\dfrac 12 \left\langle \cos\left( \dfrac s2\right), \: \sqrt{3}, \: \sin \left(\dfrac s2\right)\right\rangle


$$

Next, we differentiate $\mathbf{T}(s)$ and evaluate its absolute value at $s=\pi\mathbin{:}$

$$


\begin{aligned}𝐓^{′}(𝑠) & =\frac{1}{2}⟨\frac{d}{d𝑠}(cos⁡(\frac{𝑠}{2})),\,\frac{d}{d𝑠}(\sqrt{√3}),\,\frac{d}{d𝑠}(sin⁡(\frac{𝑠}{2}))⟩ \\ & =\frac{1}{4}⟨−sin⁡(\frac{𝑠}{2}),\,0,\,cos⁡(\frac{𝑠}{2})⟩ \\ 𝐓^{′}(𝜋) & =\frac{1}{4}⟨−sin⁡(\frac{𝜋}{2}),\,0,\,cos⁡(\frac{𝜋}{2})⟩ \\ & =\frac{1}{4}⟨−1,\,0,\,0⟩\end{aligned}


$$

Finally, we obtain the curvature by taking the magnitude:

$$


\begin{aligned}𝜅(𝜋) & =𝐓^{′}(𝜋)=\frac{1}{4}\sqrt{√(−1)^{2}+(0)^{2}+0^{2}}=\frac{1}{4}\end{aligned}


$$

**Note:** To calculate $\kappa,$ the function $\mathbf{r}(s)$ should be at least twice differentiable with respect to $s.$

### Example: Finding the Curvature Given the Arc Length Parametrization And the Unit Tangent

#### Question

Consider the curve $\mathbf r(s)$ parametrized by arc length $s.$ Find the curvature at the point where $s=\dfrac{\pi}{2}$ if the unit tangent vector of the curve is given by

$$


\mathbf T(s) = -\dfrac{4}{5}\sin{s}\,\mathbf i+\dfrac{3}{5} \sin{s}\, \mathbf j + \cos{s}\,\mathbf k.


$$

#### Explanation

Since we are given that $\mathbf{r}(s)$ and its unit tangent vector $\mathbf T(s)$ are both parametrized by the arc length $s,$ we will use the following formula for the curvature:

$$


\kappa(s) = \| \mathbf T'(s) \|


$$

Now, we differentiate $\mathbf T(s)$ with respect to $s$ and evaluate it at $s=\dfrac{\pi}{2}\mathbin{:}$

$$


\begin{aligned}𝐓^{′}(𝑠) & =\frac{d}{d𝑠}(−\frac{4}{5}sin⁡𝑠)𝐢+\frac{d}{d𝑠}(\frac{3}{5}sin⁡𝑠)𝐣+\frac{d}{d𝑠}(cos⁡𝑠)𝐤 \\ & =−\frac{4}{5}cos⁡𝑠\,𝐢+\frac{3}{5}cos⁡𝑠\,𝐣−sin⁡𝑠\,𝐤 \\ 𝐓^{′}(\frac{𝜋}{2}) & =−\frac{4}{5}cos⁡(\frac{𝜋}{2})\,𝐢+\frac{3}{5}cos⁡(\frac{𝜋}{2})\,𝐣−sin⁡(\frac{𝜋}{2})\,𝐤 \\ & =0\,𝐢+0\,𝐣−𝐤 \\ & =−𝐤\end{aligned}


$$

Finally, we obtain the curvature at the point where $s=\dfrac{\pi}{2}\mathbin{:}$

$$


\begin{aligned}𝜅(\frac{𝜋}{2}) & =𝐓^{′}(\frac{𝜋}{2})=‖−𝐤‖=\sqrt{√0^{2}+0^{2}+(−1)^{2}}=1\end{aligned}


$$

### Example: Finding the Curvature Given the Arc Length Parametrization

#### Question

Find the curvature at an arbitrary point on the curve $\mathbf r(s)$ parametrized by its arc length $s$, where

$$


\mathbf r(s) = \left\langle \dfrac{\sqrt{2}}{2}\cos s , \: -\dfrac{\sqrt{2}}{2}\cos s, \: \sin s \right\rangle, \quad 0\leq s \lt 2\pi.


$$

#### Explanation

Let $\mathbf T(s)$ denote the unit tangent to the given curve as a function of the arc length $s.$ Since we are given the curve $\mathbf{r}(s)$ parametrized by the arc length $s,$ we will use the following formula for the curvature:

$$


\kappa(s) = \| \mathbf T'(s) \| = \| \mathbf{r}''(s) \|


$$

Now, we calculate $\mathbf r'(s)$ and $\mathbf r''(s)\mathbin{:}$

$$


\begin{aligned}𝐫^{′}(𝑠) & =⟨\frac{d}{d𝑠}(\frac{\sqrt{√2}}{2}cos⁡𝑠),\,\frac{d}{d𝑠}(−\frac{\sqrt{√2}}{2}cos⁡𝑠),\,\frac{d}{d𝑠}(sin⁡𝑠)⟩ \\ & =⟨−\frac{\sqrt{√2}}{2}sin⁡𝑠,\,\frac{\sqrt{√2}}{2}sin⁡𝑠,\,cos⁡𝑠⟩ \\ 𝐫^{″}(𝑠) & =⟨\frac{d}{d𝑠}(−\frac{\sqrt{√2}}{2}sin⁡𝑠),\,\frac{d}{d𝑠}(\frac{\sqrt{√2}}{2}sin⁡𝑠),\,\frac{d}{d𝑠}(cos⁡𝑠)⟩ \\ & =⟨−\frac{\sqrt{√2}}{2}cos⁡𝑠,\,\frac{\sqrt{√2}}{2}cos⁡𝑠,\,−sin⁡𝑠⟩\end{aligned}


$$

Finally, the curvature is

$$


\begin{aligned}𝜅(𝑠) & =𝐫^{″}(𝑠) \\ & =\sqrt{(−\frac{\sqrt{√2}}{2}cos⁡𝑠)^{2}+(\frac{\sqrt{√2}}{2}cos⁡𝑠)^{2}+(−sin⁡𝑠)^{2}} \\ & =\sqrt{√\frac{1}{2}cos^{2}⁡𝑠+\frac{1}{2}cos^{2}⁡𝑠+sin^{2}⁡𝑠} \\ & =\sqrt{√cos^{2}⁡𝑠+sin^{2}⁡𝑠} \\ & =1.\end{aligned}


$$

### The Curvature of Curves Parametrized Using a General Parameter

If the curve $\mathbf r(t)$ is parametrized by a general parameter $t,$ then

$$


\kappa(t) = \dfrac{\|\mathbf T'(t)\|}{\|\mathbf r'(t)\|}.


$$

To understand why this is, remember that the arc length $s$ and the parameter $t$ are related by the formula

$$


\displaystyle s(t)= \int_0^t\left\| \mathbf r'(x)\right\|\, \textrm dx.


$$

By the chain rule and the fundamental theorem of calculus, then, we have

$$


\dfrac{\textrm d \mathbf T}{\textrm d t} = \dfrac{\textrm d \mathbf T}{\textrm d s} \dfrac{\textrm d s}{\textrm d t}= \dfrac{\textrm d \mathbf T}{\textrm d s} \left\| \mathbf r'(t)\right\|.


$$

Therefore,

$$


\begin{aligned}\frac{d𝐓}{d𝑡} & =\frac{d𝐓}{d𝑠}𝐫^{′}(𝑡) \\ ‖𝐓^{′}(𝑡)‖ & =𝜅(𝑡)𝐫^{′}(𝑡) \\ 𝜅(𝑡) & =\frac{‖𝐓^{′}(𝑡)‖}{‖𝐫^{′}(𝑡)‖}.\end{aligned}


$$

### Example: Finding the Curvature Given a General Parametrization

#### Question

Find the curvature at an arbitrary point on the curve $\mathbf r(t) = \left\langle 2\sin t, \:2\cos t \right\rangle.$

#### Explanation

Let $\mathbf T(t)$ denote the unit tangent to the given curve as a function of the parameter $t.$ Since we are given the curve $\mathbf{r}(t)$ parametrized by the parameter $t$ (not the arc length $s$), we will use the following formula for the curvature:

$$


\mathbf \kappa(t) = \dfrac{\left\| \mathbf T'(t) \right\|}{\| \mathbf r'(t) \|}


$$

First, we calculate $\mathbf r'(t)$ and find its magnitude:

$$


\begin{aligned}𝐫^{′}(𝑡) & =⟨\frac{d}{d𝑡}(2sin⁡𝑡),\,\frac{d}{d𝑡}(2cos⁡𝑡)⟩ \\ & =⟨2cos⁡𝑡,\,−2sin⁡𝑡⟩ \\ ‖𝐫^{′}(𝑡)‖ & =\sqrt{√(2cos⁡𝑡)^{2}+(−2sin⁡𝑡)^{2}} \\ & =\sqrt{√4(cos^{2}⁡𝑡+sin^{2}⁡𝑡)} \\ & =2\end{aligned}


$$

So, the corresponding unit tangent vector is

$$


\begin{aligned}𝐓(𝑡) & =\frac{𝐫^{′}(𝑡)}{‖𝐫^{′}(𝑡)‖} \\ & =\frac{1}{2}⟨2cos⁡𝑡,\,−2sin⁡𝑡⟩ \\ & =⟨cos⁡𝑡,\,−sin⁡𝑡⟩.\end{aligned}


$$

Next, we calculate $\mathbf T'(t)$ and find its magnitude:

$$


\begin{aligned}𝐓^{′}(𝑡) & =⟨\frac{d}{d𝑡}(cos⁡𝑡),\,\frac{d}{d𝑡}(−sin⁡𝑡)⟩ \\ & =⟨−sin⁡𝑡,\,−cos⁡𝑡⟩ \\ ‖𝐓^{′}(𝑡)‖ & =\sqrt{√(−sin⁡𝑡)^{2}+(−cos⁡𝑡)^{2}} \\ & =1\end{aligned}


$$

Finally, the curvature is

$$


\begin{aligned}𝜅(𝑡) & =\frac{∥𝐓^{′}(𝑡)∥}{‖𝐫^{′}(𝑡)‖}=\frac{1}{2}.\end{aligned}


$$
