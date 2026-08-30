# The Multivariable Chain Rule in Vector Form

Source: https://www.mathacademy.com/topics/1936?courseId=54
Topic ID: 1936

## Prerequisites

- [The Gradient Vector](./1934-the-gradient-vector.md)
- [The Multivariable Chain Rule](./3173-the-multivariable-chain-rule.md)
- [Differentiating Vector-Valued Functions](../ap-calculus-bc/4139-differentiating-vector-valued-functions.md)

## Lesson

### Introduction

Suppose we have the function

$$


f(\mathbf{r}) = f(x,y) = xy^2,


$$

which takes a vector-valued function

$$


\mathbf{r}(t) = \left\langle x(t), y(t) \right\rangle = \left\langle \cos t, \sin t \right\rangle


$$

as input. How do we calculate $\dfrac{\textrm{d}}{\textrm{d}t}\left[f(\mathbf{r}(t))\right]?$

To do this, we use the **multivariable chain rule in vector form**, which states

$$


\dfrac{\textrm{d}}{\textrm{d}t}\left[f(\mathbf{r}(t))\right] = \nabla f(\mathbf{r}(t))\cdot \mathbf{r}'(t).


$$

Let's now apply this to our functions. First, we compute $\nabla f(x,y){:}$

$$


\begin{aligned}∇𝑓(𝑥,𝑦) & =⟨\frac{𝜕}{𝜕𝑥}(𝑓(𝑥,𝑦)),\frac{𝜕}{𝜕𝑦}(𝑓(𝑥,𝑦))⟩ \\ & =⟨\frac{𝜕}{𝜕𝑥}(𝑥𝑦^{2}),\frac{𝜕}{𝜕𝑦}(𝑥𝑦^{2})⟩ \\ & =⟨𝑦^{2},2𝑥𝑦⟩\end{aligned}


$$

Next, we substitute $x=\cos t$ and $y=\sin t$ into the above to find $\nabla f(\mathbf{r}(t)){:}$

$$


\begin{aligned}∇𝑓(𝐫(𝑡)) & =⟨(sin⁡𝑡)^{2},2(cos⁡𝑡)(sin⁡𝑡)⟩ \\ & =⟨sin^{2}⁡𝑡,2sin⁡𝑡cos⁡𝑡⟩\end{aligned}


$$

Now, we calculate the derivative of $\mathbf{r}(t),$ which is

$$


\begin{aligned}𝐫^{′}(𝑡) & =⟨\frac{d}{d𝑡}(cos⁡𝑡),\frac{d}{d𝑡}(sin⁡𝑡)⟩ \\ & =⟨−sin⁡𝑡,cos⁡𝑡⟩.\end{aligned}


$$

Finally, applying the chain rule, we get

$$


\begin{aligned}\frac{d}{d𝑡}[𝑓(𝐫(𝑡))] & =∇𝑓(𝐫(𝑡))⋅𝐫^{′}(𝑡) \\ & =⟨sin^{2}⁡𝑡,2sin⁡𝑡cos⁡𝑡⟩⋅⟨−sin⁡𝑡,cos⁡𝑡⟩ \\ & =−sin^{3}⁡𝑡+2sin⁡𝑡cos^{2}⁡𝑡.\end{aligned}


$$

### Example: Applying the Vector Form of the Chain Rule to a Function of Two Variables

#### Question

If $f(x,y) = x^2 + 2 y^3$ and $\mathbf r (t) = \sin t \ \mathbf i + e^{t} \ \mathbf j,$ compute $\dfrac {\textrm d}{\textrm d t} [f(\mathbf r(t))].$

#### Explanation

The chain rule in vector form states that

$$


\dfrac {\textrm d}{\textrm d t} [f(\mathbf r (t))] = \nabla f(\mathbf r(t)) \cdot \mathbf r'(t).


$$

First, we need to compute $\nabla f(x,y){:}$

$$


\begin{aligned}∇𝑓(𝑥,𝑦) & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}+2𝑦^{3})\,𝐢+\frac{𝜕}{𝜕𝑦}(𝑥^{2}+2𝑦^{3})\,𝐣 \\ & =2𝑥\,𝐢+6𝑦^{2}\,𝐣\end{aligned}


$$

Next, we substitute $x = \sin t$ and $y=e^{t}$ into the above to find $\nabla f(\mathbf{r}(t)){:}$

$$


\begin{aligned}∇𝑓(𝐫(𝑡)) & =2(sin⁡𝑡)\,𝐢+6(𝑒^{𝑡})^{2}\,𝐣 \\ & =2sin⁡𝑡\,𝐢+6𝑒^{2𝑡}\,𝐣\end{aligned}


$$

Now, we calculate the derivative of $\mathbf{r}(t),$ which is

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d}{d𝑡}(sin⁡𝑡)\,𝐢+\frac{d}{d𝑡}(𝑒^{𝑡})\,𝐣 \\ & =cos⁡𝑡\,𝐢+𝑒^{𝑡}\,𝐣.\end{aligned}


$$

Finally, applying the chain rule, we get

$$


\begin{aligned}\frac{d}{d𝑡}[𝑓(𝐫(𝑡))] & =∇𝑓(𝐫(𝑡))⋅𝐫^{′}(𝑡) \\ & =(2sin⁡𝑡 𝐢+6𝑒^{2𝑡} 𝐣)⋅(cos⁡𝑡 𝐢+𝑒^{𝑡} 𝐣) \\ & =2sin⁡𝑡cos⁡𝑡+6𝑒^{2𝑡}⋅𝑒^{𝑡} \\ & =sin⁡2𝑡+6𝑒^{3𝑡}.\end{aligned}


$$

### Example: Applying the Vector Form of the Chain Rule to a Function of Three Variables

#### Question

If $f(x,y,z) = xz\ln{y}$ and $\mathbf r (t) = t^2 \, \mathbf i + t \, \mathbf j +t^3 \, \mathbf k,$ compute $\dfrac {\textrm d}{\textrm d t} [f(\mathbf r(t))].$

#### Explanation

The chain rule in vector form states that

$$


\dfrac {\textrm d}{\textrm d t} [f(\mathbf r (t))] = \nabla f(\mathbf r(t)) \cdot \mathbf r'(t).


$$

First, we need to compute $\nabla f(x,y,z){:}$

$$


\begin{aligned}∇𝑓(𝑥,𝑦,𝑧) & =\frac{𝜕}{𝜕𝑥}(𝑥𝑧ln⁡𝑦)\,𝐢+\frac{𝜕}{𝜕𝑦}(𝑥𝑧ln⁡𝑦)\,𝐣+\frac{𝜕}{𝜕𝑧}(𝑥𝑧ln⁡𝑦)\,𝐤 \\ & =𝑧ln⁡𝑦\,𝐢+\frac{𝑥𝑧}{𝑦}\,𝐣+𝑥ln⁡𝑦\,𝐤\end{aligned}


$$

Next, we substitute $x= t^2,$ $y = t$ and $z= t^3$ into the above to find $\nabla f(\mathbf{r}(t)){:}$

$$


\begin{aligned}∇𝑓(𝐫(𝑡)) & =𝑡^{3}ln⁡𝑡\,𝐢+𝑡^{4}\,𝐣+𝑡^{2}ln⁡𝑡\,𝐤\end{aligned}


$$

Now, we calculate the derivative of $\mathbf{r}(t),$ which is

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d}{d𝑡}(𝑡^{2})\,𝐢+\frac{d}{d𝑡}(𝑡)\,𝐣+\frac{d}{d𝑡}(𝑡^{3})\,𝐤 \\ & =2𝑡\,𝐢+\,𝐣+3𝑡^{2}\,𝐤.\end{aligned}


$$

Finally, applying the chain rule, we get

$$


\begin{aligned}\frac{d}{d𝑡}[𝑓(𝐫(𝑡))] & =∇𝑓(𝐫(𝑡))⋅𝐫^{′}(𝑡) \\ & =(𝑡^{3}ln⁡𝑡\,𝐢+𝑡^{4}\,𝐣+𝑡^{2}ln⁡𝑡\,𝐤)⋅(2𝑡\,𝐢+\,𝐣+3𝑡^{2}\,𝐤) \\ & =(𝑡^{3}ln⁡𝑡)⋅2𝑡+(𝑡^{4})⋅1+(𝑡^{2}ln⁡𝑡)⋅3𝑡^{2} \\ & =2𝑡^{4}ln⁡𝑡+𝑡^{4}+3𝑡^{4}ln⁡𝑡 \\ & =𝑡^{4}(5ln⁡𝑡+1).\end{aligned}


$$

### Example: Evaluating the Derivative at a Point Using the Chain Rule

#### Question

Evaluate $\dfrac {\textrm d}{\textrm d t}[f(\mathbf r(t))]$ at $t = \pi$ given that $\nabla f(x,y) = (2y - 1) \, \mathbf i + (2x-1) \, \mathbf j$ and $\mathbf r (t) = \sin{t} \, \mathbf i + \cos{t} \, \mathbf j.$

#### Explanation

The chain rule in vector form states that

$$


\dfrac {\textrm d}{\textrm d t} [f(\mathbf r (t))] = \nabla f(\mathbf r(t)) \cdot \mathbf r'(t).


$$

In addition, we've been given that

$$


\nabla f(x,y) = (2y - 1) \, \mathbf i + (2x - 1) \, \mathbf j.


$$

First, we substitute $x = \sin{t}$ and $y = \cos{t}$ into $\nabla f(x,y)$ to find $\nabla f(\mathbf{r}(t)){:}$

$$


\begin{aligned}∇𝑓(𝐫(𝑡)) & =(2cos⁡𝑡−1)\,𝐢+(2sin⁡𝑡−1)\,𝐣\end{aligned}


$$

Now, we calculate the derivative of $\mathbf{r}(t),$ which is

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d}{d𝑡}(sin⁡𝑡)\,𝐢+\frac{d}{d𝑡}(cos⁡𝑡)\,𝐣 \\ & =cos⁡𝑡\,𝐢+(−sin⁡𝑡)\,𝐣.\end{aligned}


$$

Applying the chain rule, we get

$$


\begin{aligned}\frac{d}{d𝑡}[𝑓(𝐫(𝑡))] & =∇𝑓(𝐫(𝑡))⋅𝐫^{′}(𝑡) \\ & =(2cos⁡𝑡−1\,𝐢+(2sin⁡𝑡−1)\,𝐣)⋅(cos⁡𝑡\,𝐢+(−sin⁡𝑡)\,𝐣) \\ & =(2cos⁡𝑡−1)⋅cos⁡𝑡+(2sin⁡𝑡−1)⋅(−sin⁡𝑡) \\ & =2cos^{2}⁡𝑡−cos⁡𝑡−2sin^{2}⁡𝑡+sin⁡𝑡 \\ & =2(cos^{2}⁡𝑡−sin^{2}⁡𝑡)+sin⁡𝑡−cos⁡𝑡 \\ & =2cos⁡2𝑡+sin⁡𝑡−cos⁡𝑡.\end{aligned}


$$

Finally, evaluating the above at $t = \pi,$ we obtain

$$


\begin{aligned}\frac{d}{d𝑡}[𝑓(𝐫(𝜋))] & =2cos⁡2𝜋+sin⁡𝜋−cos⁡𝜋 \\ & =2(1)+0−(−1) \\ & =3.\end{aligned}


$$

### The Derivative as a Rate of Change

We can consider $f(\mathbf{r}(t))$ as the values taken by the function $f$ along the curve $\mathbf{r}(t).$ So, the derivative

$$


\dfrac {\textrm d}{\textrm d t} [f(\mathbf r (t))]


$$

can be interpreted as the **rate of change of $f$ with respect to $t$ along the curve $\mathbf{r}(t).$**

Furthermore, if $\mathbf{r}(t)$ is a level curve $f(x,y)=c,$ then by the chain rule we have

$$


\begin{aligned}𝑓(𝐫(𝑡)) & =𝑐 \\ \frac{d}{d𝑡}(𝑓(𝐫(𝑡))) & =\frac{d}{d𝑡}(𝑐) \\ ∇𝑓(𝐫(𝑡))⋅𝐫^{′}(𝑡) & =0.\end{aligned}


$$

From this, we can conclude that the gradient vector $\nabla f$ is orthogonal to every level curve of $f.$

### Example: Computing the Rate of Change of a Multivariable Function at a Point Using the Chain Rule

#### Question

Compute the rate of change of the function $f(x,y,z)=x^2-y^2-z$ with respect to $t$ along the curve $\mathbf r (t) = \left \langle \sin t, \cos t, t \right \rangle$ at the point $t=\dfrac \pi 4.$

#### Explanation

The rate of change of $f(x,y,z)$ with respect to $t$ along the curve $\mathbf r (t)$ is given by $\dfrac {\textrm d}{\textrm d t} [f(\mathbf r (t))].$ To calculate this, we can use the chain rule.

The chain rule in vector form states that

$$


\dfrac {\textrm d}{\textrm d t} [f(\mathbf r (t))] = \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t).


$$

First, we need to compute $\nabla f(x,y){:}$

$$


\begin{aligned}∇𝑓(𝑥,𝑦) & =⟨\frac{𝜕}{𝜕𝑥}(𝑥^{2}−𝑦^{2}−𝑧),\frac{𝜕}{𝜕𝑦}(𝑥^{2}−𝑦^{2}−𝑧),\frac{𝜕}{𝜕𝑧}(𝑥^{2}−𝑦^{2}−𝑧)⟩ \\ & =⟨2𝑥,−2𝑦,−1⟩\end{aligned}


$$

Next, we substitute $x = \sin t, y=\cos t,$ and $z=t$ into the above to find $\nabla f(\mathbf r(t)){:}$

$$


\begin{aligned}∇𝑓(𝐫(𝑡)) & =⟨2sin⁡𝑡,−2cos⁡𝑡,−1⟩\end{aligned}


$$

Now, we calculate the derivative of $\mathbf{r}(t),$ which is

$$


\begin{aligned}𝐫^{′}(𝑡) & =⟨\frac{d}{d𝑡}(sin⁡𝑡),\frac{d}{d𝑡}(cos⁡𝑡),\frac{d}{d𝑡}(𝑡)⟩ \\ & =⟨cos⁡𝑡,−sin⁡𝑡,1⟩.\end{aligned}


$$

Applying the chain rule, we get

$$


\begin{aligned}\frac{d}{d𝑡}[𝑓(𝐫(𝑡))] & =∇𝑓(𝐫(𝑡))⋅𝐫^{′}(𝑡) \\ & =⟨2sin⁡𝑡,−2cos⁡𝑡,−1⟩⋅⟨cos⁡𝑡,−sin⁡𝑡,1⟩ \\ & =2sin⁡𝑡⋅cos⁡𝑡−2cos⁡𝑡⋅(−sin⁡𝑡)−1⋅1 \\ & =2sin⁡𝑡cos⁡𝑡+2sin⁡𝑡cos⁡𝑡−1 \\ & =4sin⁡𝑡cos⁡𝑡−1.\end{aligned}


$$

Therefore, the rate of change of $f$ along the curve $\mathbf{r}(t)$ at $t=\dfrac{\pi}{4}$ is

$$


\begin{aligned}\frac{d}{d𝑡}[𝑓(𝐫(\frac{𝜋}{4}))] & =4sin⁡(\frac{𝜋}{4})cos⁡(\frac{𝜋}{4})−1 \\ & =4⋅\frac{\sqrt{√2}}{2}⋅\frac{\sqrt{√2}}{2}−1 \\ & =1.\end{aligned}


$$

### Intuition Behind the Vector Form of the Multivariable Chain Rule

The chain rule for a function $f(\mathbf{r}),$ where $\mathbf{r}(t) = \left\langle x_1(t), x_2(t), \ldots, x_m(t) \right\rangle$ is a vector-valued function of $m$ variables, is the same as before:

$$


\dfrac{\textrm{d}f}{\textrm{d}t} = \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)


$$

How does this chain rule in vector form relate to the chain rule we have seen before, which states that

$$


\dfrac {\textrm d f} {\textrm d t} = \dfrac {\partial f}{\partial x_1} \cdot \dfrac {\textrm d x_1}{\textrm d t} + \dfrac {\partial f}{\partial x_2} \cdot \dfrac {\textrm d x_2}{\textrm d t} + \dots + \dfrac {\partial f}{\partial x_m} \cdot \dfrac {\textrm d x_m}{\textrm d t}?


$$

Let's expand $\nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t)$ to see. Recall that

$$


\begin{aligned}∇𝑓(𝐫(𝑡))=⟨\frac{𝜕𝑓}{𝜕𝑥_{1}},\frac{𝜕𝑓}{𝜕𝑥_{2}},…,\frac{𝜕𝑓}{𝜕𝑥_{𝑚}}⟩\end{aligned}


$$

and

$$


\begin{aligned}𝐫^{′}(𝑡)=⟨\frac{d𝑥_{1}}{𝑑𝑡},\frac{d𝑥_{2}}{𝑑𝑡},…,\frac{d𝑥_{𝑚}}{𝑑𝑡}⟩.\end{aligned}


$$

Then

$$


\begin{aligned}∇𝑓(𝐫(𝑡))⋅𝐫^{′}(𝑡) & =⟨\frac{𝜕𝑓}{𝜕𝑥_{1}},\frac{𝜕𝑓}{𝜕𝑥_{2}},…,\frac{𝜕𝑓}{𝜕𝑥_{𝑚}}⟩⋅⟨\frac{d𝑥_{1}}{𝑑𝑡},\frac{d𝑥_{2}}{𝑑𝑡},…,\frac{d𝑥_{𝑚}}{𝑑𝑡}⟩ \\ & =\frac{𝜕𝑓}{𝜕𝑥_{1}}⋅\frac{d𝑥_{1}}{d𝑡}+\frac{𝜕𝑓}{𝜕𝑥_{2}}⋅\frac{d𝑥_{2}}{d𝑡}+⋯+\frac{𝜕𝑓}{𝜕𝑥_{𝑚}}⋅\frac{d𝑥_{𝑚}}{d𝑡}.\end{aligned}


$$

They are exactly the same, just different notations!

**Note**: If we replace $\mathbf{r}$ with a single-valued function $g(t),$ we get back the chain rule from single-variable calculus:

$$


\begin{aligned}\frac{d}{d𝑡}[𝑓(𝑔(𝑡))] & =∇𝑓(𝑔(𝑡))⋅𝑔^{′}(𝑡) \\ & =\frac{d𝑓}{d𝑔}⋅\frac{d𝑔}{d𝑡}.\end{aligned}


$$
