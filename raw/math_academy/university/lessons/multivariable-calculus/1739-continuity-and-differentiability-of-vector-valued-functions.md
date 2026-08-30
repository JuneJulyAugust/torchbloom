# Continuity and Differentiability of Vector-Valued Functions

Source: https://www.mathacademy.com/topics/1739?courseId=54
Topic ID: 1739

## Prerequisites

- [Defining Continuity at a Point](../../../ap-courses/lessons/ap-calculus-ab/314-defining-continuity-at-a-point.md)
- [Limits of Vector-Valued Functions](./1741-limits-of-vector-valued-functions.md)
- [Differentiating Vector-Valued Functions](../../../ap-courses/lessons/ap-calculus-bc/4139-differentiating-vector-valued-functions.md)

## Lesson

### Introduction

Determining the continuity of a vector function is very similar to determining the continuity of a scalar function. A vector function $\mathbf f (t)$ is **continuous** at a point $t_0$ (in its domain) if

$$


\displaystyle \lim_{t \rightarrow t_0} \mathbf f (t) = \mathbf f (t_0).


$$

For example, the vector function

$$


\mathbf f(t) = \left \langle e^t, \dfrac{1}{t} \right \rangle


$$

is continuous at $t=1$ because

$$


\begin{aligned}\underset{𝑡→1}{lim}𝐟(𝑡) & =⟨\underset{𝑡→1}{lim}(𝑒^{𝑡}),\,\underset{𝑡→1}{lim}(\frac{1}{𝑡})⟩ \\ & =⟨𝑒^{1},\,\frac{1}{1}⟩ \\ & =⟨𝑒,\,1⟩ \\ & =𝐟(1)\end{aligned}


$$

Since the limit of a vector function is determined by the limits of the components, a vector function is continuous at a point $t_0$ *if and only if* each of its components is continuous at that point.

We say that a vector function is **continuous on the interval** $t\in[a,b]$ if it is continuous at every point of this interval.

### Example: Determining the Continuity of a Vector Function

#### Question

Is the vector function $\mathbf f(t) = -\sin t \,\mathbf i + (t^2 + 1)\,\mathbf j + \tan t\,\mathbf k$ continuous at $t = 0?$

#### Explanation

Let's compute the limit of $\mathbf f (t)$ as $t$ approaches $0\mathbin{:}$

$$


\begin{aligned}\underset{𝑡→0}{lim}𝐟(𝑡) & =⟨\underset{𝑡→0}{lim}(−sin⁡𝑡),\,\underset{𝑡→0}{lim}(𝑡^{2}+1),\,\underset{𝑡→0}{lim}tan⁡𝑡⟩ \\ & =⟨−sin⁡0,\,0^{2}+1,\,tan⁡0⟩ \\ & =⟨0,1,0⟩ \\ & =𝐟(0)\end{aligned}


$$

So $\displaystyle \lim_{t \rightarrow t_0} \mathbf f (t) = \mathbf f (t_0)$ and therefore $\mathbf f (t)$ is continuous at $t=0.$

### Example: Finding the Value of a Vector Function Using Properties of Continuous Functions

#### Question

Find $\mathbf g(1)$ given that $\mathbf f(t)$ and $\mathbf g(t)$ are two continuous vector-valued functions for which $\mathbf f(1) = \left\langle 1, 1, -1 \right\rangle$ and

$$


\lim_\limits{t\rightarrow 1} \big[ 2\mathbf f(t)-\mathbf g(t) \big] = \left\langle 2, 1, -1 \right\rangle.


$$

#### Explanation

Using the constant multiple rule and the addition rule for limits, and the fact that both functions are continuous, we get

$$


\begin{aligned}\underset{𝑡→1}{lim}[2𝐟(𝑡)−𝐠(𝑡)] & =\underset{𝑡→1}{lim}2𝐟(𝑡)+\underset{𝑡→1}{lim}[−𝐠(𝑡)] \\ & =2\underset{𝑡→1}{lim}𝐟(𝑡)−\underset{𝑡→1}{lim}𝐠(𝑡) \\ & =2𝐟(1)−𝐠(1) \\ & =2\underset{𝐟(1)}{\underset{}{⟨1,1,−1⟩}}−𝐠(1) \\ & =⟨2,2,−2⟩−𝐠(1).\end{aligned}


$$

On the other hand, we are told that

$$


\lim_\limits{t\rightarrow 1} \big[ 2\mathbf f(t)-\mathbf g(t) \big] = \left\langle 2, 1, -1 \right\rangle.


$$

Therefore, we obtain the following equation which we can solve for $\mathbf{g} (1)\mathbin{:}$

$$


\begin{aligned}\underset{𝑡→1}{lim}[2𝐟(𝑡)−𝐠(𝑡)] & =⟨2,1,−1⟩ \\ ⟨2,2,−2⟩−𝐠(1) & =⟨2,1,−1⟩ \\ 𝐠(1) & =⟨2,2,−2⟩−⟨2,1,−1⟩ \\ 𝐠(1) & =⟨0,1,−1⟩\end{aligned}


$$

### Differentiability of Vector Functions

Similar to scalar-valued functions, the vector function $\mathbf{f}(t)$ is **differentiable** at a point $t = t_0$ in the domain of the function if the following limit exists:

$$


\lim_{h \to 0} \dfrac{\mathbf{f}(t_0+h) - \mathbf{f}(t_0)}{h}


$$

The value of the limit is then called the **derivative** of $\mathbf{f}(t)$ at $t = t_0$ and is denoted as $\mathbf{f}'(t_0)$. In general, a vector function is differentiable *if and only if* all of its components are differentiable.

For example, is the following vector function $\mathbf{g}(t)$ differentiable at $t=0$?

$$


\mathbf{g}(t) = \big\langle t, \: |\,t\,|, \: \sin t \big\rangle


$$

Notice that the second component, $|\,t\,|,$ is not differentiable at $t=0.$ Since one of the component functions is not differentiable at $t=0,$ we conclude that the overall vector function $\mathbf{g}(t)$ is not differentiable at $t=0.$

We say that a vector function is **differentiable on an open interval** $t \in (a,b)$ if it is differentiable at *every* point $t \in (a,b).$ This means that each component of the function must be differentiable at every point of $(a,b).$

Our function $\mathbf{g}(t)$, mentioned above, is differentiable on $(-\infty, 0) \cup (0, \infty)$ since all of its components are differentiable there.

Finally, a function is said to be **continuously differentiable** if it is differentiable and its derivative is continuous.

### Example: Determining the Differentiability of a Vector Function

#### Question

Is the vector function $\mathbf{f}(t) = \left\langle 2e^t, \: \dfrac{\pi}{t-3}, \: \sqrt{t} \right\rangle$ differentiable with respect to $t$ on $t \in [0, 2]?$

#### Explanation

The function is defined on $t \in [0, 2].$ Remember that a function is differentiable on the interval $[0, 2]$ if and only if all of its component functions are differentiable on that interval.

Let's now differentiate $\mathbf f(t)$ to find $\mathbf f'(t)\mathbin{:}$

$$


\begin{aligned}𝐟^{′}(𝑡) & =⟨\frac{d}{d𝑡}(2𝑒^{𝑡}),\,\frac{d}{d𝑡}(\frac{𝜋}{𝑡−3}),\,\frac{d}{d𝑡}(\sqrt{√𝑡})⟩ \\ & =⟨2𝑒^{𝑡},\,−\frac{𝜋}{(𝑡−3)^{2}},\,\frac{1}{2\sqrt{√𝑡}}⟩\end{aligned}


$$

Notice that the third component of this vector, $\dfrac{1}{2\sqrt{t}}$ is undefined at $t = 0.$ Therefore, we conclude that the function $\mathbf f(t)$ is **** differentiable on $[0,2].$

### Example: Finding the Interval on Which a Product of Functions is Differentiable

#### Question

Find the interval where the function $\mathbf g(t)\cdot\mathbf h(t)$ is differentiable, given the following functions $\mathbf g(t)$ and $\mathbf h(t)\mathbin{:}$

$$


\begin{aligned}𝐠(𝑡) & =3sin⁡𝑡\,𝐢−cos⁡(2𝑡)\,𝐣−\sqrt{√𝑡}\,𝐤 \\ 𝐡(𝑡) & =2𝑡\,𝐢+𝑡^{2}\,𝐣−3cos⁡𝑡\,𝐤\end{aligned}


$$

#### Explanation

The function $\mathbf F(t) = \mathbf g(t)\cdot\mathbf h(t)$ is differentiable over the common domain where both $\mathbf g(t)$ and $\mathbf h(t)$ are differentiable. Remember that a vector function is differentiable if and only if each component is differentiable.

So, let's start by finding the intervals where each of the functions $\mathbf g(t)$ and $\mathbf h(t)$ are differentiable.

For the function $\mathbf g(t)\mathbin{:}$

- The first component, $3\sin t,$ and the second component, $-\cos(2t),$ are differentiable over $(-\infty, \infty).$

- The third component $- \sqrt t$ is differentiable on $(0, \infty).$ Its derivative is not defined at $t=0$ and the function is not defined for $t <0.$

The intersection of the intervals of differentiability of all three components of $\mathbf g(t)$ is $(0,\infty).$ So, $\mathbf g(t)$ is differentiable on $(0,\infty).$

For the function $\mathbf h(t)\mathbin{:}$

- All three component functions are defined and are differentiable for all values of $t \in (-\infty, \infty).$ So, $\mathbf h(t)$ is differentiable on $(-\infty, \infty).$

Finally, the common domain of differentiability for $\mathbf g(t)$ and $\mathbf h(t)$ is $(0, \infty) \cap (-\infty, \infty) = (0,\infty).$
