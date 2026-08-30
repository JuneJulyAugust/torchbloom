# Limits of Vector-Valued Functions

Source: https://www.mathacademy.com/topics/1741?courseId=54
Topic ID: 1741

## Prerequisites

- [Calculating the Cross Product Using Determinants](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/245-calculating-the-cross-product-using-determinants.md)
- [L'Hopital's Rule](../../../ap-courses/lessons/ap-calculus-ab/463-l-hopital-s-rule.md)
- [Special Limits Involving Sine](../../../ap-courses/lessons/ap-calculus-ab/606-special-limits-involving-sine.md)
- [The Domain of a Vector-Valued Function](./1737-the-domain-of-a-vector-valued-function.md)
- [Limits Involving the Exponential Function](../../../ap-courses/lessons/ap-calculus-bc/2610-limits-involving-the-exponential-function.md)

## Lesson

### Introduction

To find the limit of a vector function, we compute the limit of each component individually. So, if $\mathbf f (t) = x(t) \ \mathbf {i} + y(t) \ \mathbf {j} +z(t) \ \mathbf {k}$ is our vector function, then the limit is computed as follows:

$$


\displaystyle \lim_{t\to a} \mathbf f (t) = \bigg[ \lim_{t \to a} x(t) \bigg] \mathbf {i} + \bigg[ \lim_{t \to a}y(t) \bigg] \mathbf {j} +\bigg[ \lim_{t \to a}z(t) \bigg] \mathbf {k}


$$

The limit on the left exists *if and only if* all the limits on the right exist too.

For example, suppose we are given the vector function

$$


\mathbf f (t) = \left( 5+t \right) \ \mathbf {i} + (t^{2}-1) \ \mathbf {j} + \sin{t} \ \mathbf {k},


$$

and we want to compute the limit $\lim\limits_{t \to 0} \mathbf f (t).$ To do this, we find the limit of each component function as follows:

$$


\begin{aligned}\underset{𝑡→0}{lim}𝐟(𝑡) & =[\,\underset{=\,5}{\underset{}{\underset{𝑡→0}{lim}(5+𝑡)}}\,]𝐢+[\,\underset{=\,−1}{\underset{}{\underset{𝑡→0}{lim}(𝑡^{2}−1)\,}}]𝐣+[\,\underset{=\,0}{\underset{}{\underset{𝑡→0}{lim}sin⁡𝑡\,}}]𝐤 \\ & =5 𝐢+(−1) 𝐣+0 𝐤 \\ & =⟨5,\,−1,\,0⟩\end{aligned}


$$

### Example: Finding the Limit of a Vector Function

#### Question

Calculate $\lim\limits_{t \to 0} \mathbf{f}(t),$ given that

$$


\mathbf f (t) = \dfrac{1- e^{t}}{\sin t} \ \mathbf {i}+ \dfrac{\sin t}{t+t^2} \ \mathbf {j} + \dfrac{ e^{t} - e^{-t}}{\sin t} \ \mathbf {k}.


$$

#### Explanation

To find the limit of our vector function, we compute the limit of each component individually:

$$


\lim_{t \to 0}\mathbf f(t) = \left(\lim_{t \to 0} \dfrac{1-e^t}{\sin t}\right)\,\mathbf i + \left( \lim_{t \to 0} \dfrac{\sin t}{t+t^2}\right)\,\mathbf j + \left( \lim_{t \to 0} \dfrac{e^t-e^{-t}}{\sin t} \right)\,\mathbf k


$$

Now, we find the limits one-by-one.

- The first component can be found using L'Hopital's Rule:

- The second component can be found using a special limit:

- The third component can be found using L'Hopital's Rule:

Therefore,

$$


\lim\limits_{t \to 0}\mathbf f(t) = -\mathbf i + \mathbf j +2\,\mathbf k.


$$

### Basic Properties of Limits of Vector Functions

Many properties of limits of scalar functions extend naturally to limits of vector functions. For instance, if $\mathbf f(t)$ and $\mathbf g(t)$ are vector functions and $p,q$ are constants, then

$$


\lim_{t \to a}\left[p \ \mathbf f(t) + q \ \mathbf g(t)\right] = p \ \lim_{t \to a}\mathbf f(t) + q \ \lim_{t \to a}\mathbf g(t).


$$

We also have the following property for the magnitude:

$$


\begin{aligned}\underset{𝑡→𝑎}{lim}∥𝐟(𝑡)∥ & =\underset{𝑡→𝑎}{lim}𝐟(𝑡),\end{aligned}


$$

where $\left\| \mathbf f(t) \right\|$ denotes the magnitude of the vector $\mathbf f(t)$.

### Example: Finding the Limit of the Magnitude of a Vector Function

#### Question

Calculate $\lim\limits_{t \to \infty} \| \mathbf f(t) \|$ if $\mathbf f(t) = \left\langle t^{-1}, \: \left(1+\dfrac{3}{t}\right)^t, \: \dfrac{t^2}{1-t^2} \right\rangle.$

#### Explanation

To find the limit of our vector function, we compute the limit of each component individually:

$$


\begin{aligned}\underset{𝑡→∞}{lim}𝐟(𝑡) & =⟨\underset{𝑡→∞}{lim}𝑡^{−1},\,\underset{𝑡→∞}{lim}(1+\frac{3}{𝑡})^{𝑡},\,\underset{𝑡→∞}{lim}\frac{𝑡^{2}}{1−𝑡^{2}}⟩\end{aligned}


$$

Now, we find the limits one-by-one.

- For the first component, we have

- The second component can be found using a special limit:

- For the third component, we have

Therefore,

$$


\lim\limits_{t \to \infty}\mathbf f(t) = \left\langle 0, \: e^3, \: -1\right\rangle.


$$

Finally, the limit of $\left\| \mathbf f(t) \right\|$ as $t$ approaches $\infty$ is

$$


\begin{aligned}\underset{𝑡→∞}{lim}∥𝐟(𝑡)∥ & =\underset{𝑡→∞}{lim}𝐟(𝑡) \\ & =⟨0,\,𝑒^{3},\,−1⟩ \\ & =\sqrt{√0^{2}+(𝑒^{3})^{2}+(−1)^{2}} \\ & =\sqrt{√𝑒^{6}+1}.\end{aligned}


$$

### Example: Finding the Limit of a Sum of Vector Functions

#### Question

Find $\displaystyle \lim_{t \to 0} \big[\mathbf f(t) - 2 \mathbf g(t) \big]$ given that $\mathbf f(t)$ and $\mathbf g(t)$ are defined as:

$$


\begin{aligned}𝐟(𝑡)=\begin{aligned}sin⁡𝑡 \\ 𝑒^{𝑡} \\ 𝑡\end{aligned},\,𝐠(𝑡)=\begin{aligned}cos⁡𝑡 \\ 1 \\ 2𝑡\end{aligned}\end{aligned}


$$

#### Explanation

First, we find the limit of each function:

$$


\begin{aligned}\underset{𝑡→0}{lim}𝐟(𝑡)=\begin{aligned}\underset{𝑡→0}{lim}sin⁡𝑡 \\ \underset{𝑡→0}{lim}𝑒^{𝑡} \\ \underset{𝑡→0}{lim}𝑡\end{aligned}=\begin{aligned}sin⁡0 \\ 𝑒^{0} \\ 0\end{aligned}=\begin{aligned}0 \\ 1 \\ 0\end{aligned} \\ \underset{𝑡→0}{lim}𝐠(𝑡)=\begin{aligned}\underset{𝑡→0}{lim}cos⁡𝑡 \\ \underset{𝑡→0}{lim}1 \\ \underset{𝑡→0}{lim}2𝑡\end{aligned}=\begin{aligned}cos⁡0 \\ 1 \\ 2(0)\end{aligned}=\begin{aligned}1 \\ 1 \\ 0\end{aligned}\end{aligned}


$$

Now, we use properties of limits to calculate the final result:

$$


\begin{aligned}\underset{𝑡→0}{lim}[𝐟(𝑡)−2𝐠(𝑡)] & =\underset{𝑡→0}{lim}𝐟(𝑡)−2\underset{𝑡→0}{lim}𝐠(𝑡) \\ & =\begin{aligned}0 \\ 1 \\ 0\end{aligned}−2\begin{aligned}1 \\ 1 \\ 0\end{aligned} \\ & =\begin{aligned}−2 \\ −1 \\ 0\end{aligned}\end{aligned}


$$

### Limits of Vector Products

For two vector functions, the limit of a product is equal to the product of the limits:

$$


\begin{aligned}\underset{𝑡→𝑎}{lim}[𝐟(𝑡)⋅𝐠(𝑡)] & =\underset{𝑡→𝑎}{lim}𝐟(𝑡)⋅\underset{𝑡→𝑎}{lim}𝐠(𝑡) \\ \underset{𝑡→𝑎}{lim}[𝐟(𝑡)×𝐠(𝑡)] & =\underset{𝑡→𝑎}{lim}𝐟(𝑡)×\underset{𝑡→𝑎}{lim}𝐠(𝑡)\end{aligned}


$$

Here, $\mathbf f(t)\cdot \mathbf g(t)$ and $\mathbf f(t) \times \mathbf g(t)$ are the dot product and the cross product of $\mathbf f(t)$ and $\mathbf g(t),$ respectively.

### Example: Finding the Limit of a Product of Vector Functions

#### Question

Find $\displaystyle \lim_{t \to 2} \left[\mathbf f(t) \cdot \mathbf g(t)\right]$ given that $\mathbf f(t)$ and $\mathbf g(t)$ are defined as follows:

$$


\begin{aligned}𝐟(𝑡) & =ln⁡𝑡\,𝐢+𝑡\,𝐣+𝑡^{2}\,𝐤 \\ 𝐠(𝑡) & =(2−𝑡)\,𝐢+\frac{6}{𝑡}\,𝐣−4\,𝐤\end{aligned}


$$

#### Explanation

First, we find the limit of each function:

$$


\begin{aligned}\underset{𝑡→2}{lim}𝐟(𝑡) & =(\underset{𝑡→2}{lim}ln⁡𝑡)\,𝐢+(\underset{𝑡→2}{lim}𝑡)\,𝐣+(\underset{𝑡→2}{lim}𝑡^{2})\,𝐤 \\ & =(ln⁡2)\,𝐢+2\,𝐣+2^{2}\,𝐤 \\ & =ln⁡2\,𝐢+2\,𝐣+4\,𝐤, \\ \underset{𝑡→2}{lim}𝐠(𝑡) & =(\underset{𝑡→2}{lim}(2−𝑡))\,𝐢+(\underset{𝑡→2}{lim}\frac{6}{𝑡})\,𝐣+(\underset{𝑡→2}{lim}(−4))\,𝐤 \\ & =(2−2)\,𝐢+\frac{6}{2}\,𝐣+(−4)\,𝐤 \\ & =0\,𝐢+3\,𝐣−4\,𝐤 \\ & =3\,𝐣−4\,𝐤.\end{aligned}


$$

Now, we use properties of limits to calculate the final result:

$$


\begin{aligned}\underset{𝑡→2}{lim}[𝐟(𝑡)⋅𝐠(𝑡)] & =\underset{𝑡→2}{lim}𝐟(𝑡)⋅\underset{𝑡→2}{lim}𝐠(𝑡) \\ & =(ln⁡2\,𝐢+2\,𝐣+4\,𝐤)⋅(3\,𝐣−4\,𝐤) \\ & =ln⁡2⋅0+2⋅3+4⋅(−4) \\ & =−10\end{aligned}


$$
