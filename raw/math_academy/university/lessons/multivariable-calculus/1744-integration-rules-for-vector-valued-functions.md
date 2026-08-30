# Integration Rules for Vector-Valued Functions

Source: https://www.mathacademy.com/topics/1744?courseId=54
Topic ID: 1744

## Prerequisites

- [Calculating the Cross Product Using Determinants](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/245-calculating-the-cross-product-using-determinants.md)
- [Properties of Definite Integrals Involving the Limits of Integration](../../../ap-courses/lessons/ap-calculus-ab/632-properties-of-definite-integrals-involving-the-limits-of-integration.md)
- [Integrating Vector-Valued Functions](../../../ap-courses/lessons/ap-calculus-bc/1085-integrating-vector-valued-functions.md)

## Lesson

### Introduction

Since the integration of vector functions is done component-by-component, the properties of integrals of vector functions are immediately inherited from those of the integrals of real-valued functions.

Suppose that $\mathbf f(t)$ and $\mathbf g(t)$ are vector-valued functions that are continuous on a closed interval $[a,b],$ and $\alpha$ is a scalar. Then, the *vector addition and scalar multiplication rules* are as follows:

$$


\begin{aligned}∫_{𝑏𝑎}(𝐟(𝑡)+𝐠(𝑡))d𝑡=∫_{𝑏𝑎}𝐟(𝑡)\,d𝑡\,+\,∫_{𝑏𝑎}𝐠(𝑡)\,d𝑡\, & vector addition rule \\ ∫_{𝑏𝑎}𝛼\,𝐟(𝑡)\,d𝑡=𝛼\,∫_{𝑏𝑎}𝐟(𝑡)\,d𝑡\, & scalar constant multiple rule\end{aligned}


$$

For example, if $\mathbf f(t) = \left\langle t, \: \cos t\right\rangle$ and $\mathbf g(t) = \left\langle -t^2, \: \sin t \right\rangle,$ then we have

$$


\begin{aligned}∫[𝐟(𝑡)+2𝐠(𝑡)]d𝑡 & =∫𝐟(𝑡)\,d𝑡+2∫𝐠(𝑡)\,d𝑡 \\ & =∫⟨𝑡,\,cos⁡𝑡⟩\,d𝑡+2∫⟨−𝑡^{2},\,sin⁡𝑡⟩\,d𝑡 \\ & =⟨∫𝑡\,d𝑡,\,∫cos⁡𝑡\,d𝑡⟩+⟨2∫−𝑡^{2}\,d𝑡,\,2∫sin⁡𝑡\,d𝑡⟩ \\ & =⟨\frac{𝑡^{2}}{2}+𝐶_{1},\,sin⁡𝑡+𝐶_{2}⟩+⟨−\frac{2𝑡^{3}}{3}+𝐶_{3},\,−2cos⁡𝑡+𝐶_{4}⟩ \\ & =⟨\frac{3𝑡^{2}−4𝑡^{3}}{6},\,sin⁡𝑡−2cos⁡𝑡⟩+𝐂\end{aligned}


$$

where $C_1, \, C_2, \, C_3, \, C_4$ are arbitrary real constants and ${\mathbf C} = \langle C_1+C_3, C_2+C_4 \rangle$ is a constant vector.

### Example: Applying the Vector Addition and Scalar Multiplication Rules

#### Question

Calculate $\displaystyle{\int_0^2} [3 \mathbf f(t)+\mathbf g(t)] \,\text{d}t$ given that $\displaystyle{\int_0^2} \mathbf f(t)\,\text{d}t=\left\langle 16, \: 2,\: -2\right\rangle$ and $\displaystyle{\int_0^2}\mathbf g(t)\,\text{d}t=\left\langle 2,-4,2\right\rangle.$

#### Explanation

From the vector addition and scalar multiplication rules, we have

$$


\displaystyle {\int_0^2 } \big[ \, 3 \mathbf f(t)+\mathbf g(t) \, \big] \, \textrm d t = \displaystyle {3\int_0^2 } \mathbf f(t) \, \textrm d t + \displaystyle {\int_0^2 } \mathbf g(t) \, \textrm d t.


$$

Therefore,

$$


\begin{aligned}∫_{20}[3𝐟(𝑡)+𝐠(𝑡)]\,d𝑡 & =3∫_{20}𝐟(𝑡)\,d𝑡+∫_{20}𝐠(𝑡)\,d𝑡 \\ & =3⟨16,\,2,\,−2⟩+⟨2,\,−4,\,2⟩ \\ & =⟨48,\,6,\,−6⟩+⟨2,\,−4,\,2⟩ \\ & =⟨50,2,−4⟩.\end{aligned}


$$

### The Rule for Reversal of Integration Limits

Given a vector-valued function $\mathbf f(t)$ that is continuous on a closed interval $[a,b],$ the *rule for reversal of integration limits* states the following:

$$


\begin{aligned}∫_{𝑎𝑏}𝐟(𝑡)\,d𝑡=−∫_{𝑏𝑎}𝐟(𝑡)\,d𝑡\end{aligned}


$$

### Example: Reversing the Limits of Integration

#### Question

Calculate $\displaystyle\int_0^2\mathbf f(t) + \langle 1,\:-1,\:1\rangle\,\text{d}t$ given that $\displaystyle\int_2^0\mathbf f(t) \,\text{d}t= \left\langle -3, \: 2, \: 1 \right\rangle.$

#### Explanation

Let's reverse the limits of integration on the known result:

$$


\begin{aligned}∫_{20}𝐟(𝑡)\,d𝑡 & =−∫_{02}𝐟(𝑡)\,d𝑡 \\ & =−⟨−3,\,2,\,1⟩ \\ & =⟨3,\,−2,\,−1⟩.\end{aligned}


$$

Therefore, applying the vector addition rule, we get

$$


\begin{aligned}∫_{20}𝐟(𝑡)+⟨1,\,−1,\,1⟩\,d𝑡 & =∫_{20}𝐟(𝑡)\,d𝑡+∫_{20}⟨1,\,−1,\,1⟩\,d𝑡 \\ & =⟨3,\,−2,\,−1⟩+⟨𝑡,\,−𝑡,\,𝑡⟩_{20} \\ & =⟨3,\,−2,\,−1⟩+⟨2,\,−2,\,2⟩ \\ & =⟨5,\,−4,\,1⟩.\end{aligned}


$$

### The Adjacent Intervals Rule

Given a vector-valued function $\mathbf f(t)$ that is continuous on a closed interval $[a,b]$ and $p \in (a,b),$ the *adjacent intervals rule* states the following:

$$


\begin{aligned}∫_{𝑏𝑎}𝐟(𝑡)\,d𝑡=∫_{𝑝𝑎}𝐟(𝑡)\,d𝑡+∫_{𝑏𝑝}𝐟(𝑡)\,d𝑡\end{aligned}


$$

### Example: Applying the Adjacent Intervals Rule

#### Question

Calculate $\displaystyle\int_{-1}^0\mathbf f(t)\,\text{d}t$ given that $\displaystyle\int_0^1\mathbf f(t)\,\text{d}t= \left\langle \dfrac{3}{2}, \: 1, \: 3 \right\rangle$ and $\displaystyle\int_{-1}^1\mathbf f(t)\,\text{d}t=\left\langle 0, \: 2, \: 6 \right\rangle.$

#### Explanation

Using the adjacent intervals, we get

$$


\int_{-1}^1\mathbf f(t)\,\text{d}t=\int_{-1}^0\mathbf f(t)\,\text{d}t+\int_0^1\mathbf f(t)\,\text{d}t .


$$

We can rearrange the above as follows:

$$


\int_{-1}^0\mathbf f(t)\,\text{d}t = \int_{-1}^1\mathbf f(t)\,\text{d}t - \int_0^1\mathbf f(t)\,\text{d}t


$$

Finally, using the given information, we get

$$


\begin{aligned}∫_{0−1}𝐟(𝑡)\,d𝑡 & =∫_{1−1}𝐟(𝑡)\,d𝑡−∫_{10}𝐟(𝑡)\,d𝑡 \\ & =⟨0,\,2,\,6⟩−⟨\frac{3}{2},\,1,\,3⟩ \\ & =⟨−\frac{3}{2},\,1,\,3⟩.\end{aligned}


$$

### The Product Rules

Suppose that $\mathbf f(t)$ is a vector-valued function that is continuous on a closed interval $[a,b]$ and $\mathbf c$ is a constant vector. Then, the *products rules* are as follows:

$$


\begin{aligned}∫_{𝑏𝑎}[𝐜⋅𝐟(𝑡)]d𝑡=𝐜⋅(∫_{𝑏𝑎}𝐟(𝑡)\,d𝑡)\, & dot product rule \\ ∫_{𝑏𝑎}[𝐜×𝐟(𝑡)]d𝑡=𝐜×∫_{𝑏𝑎}𝐟(𝑡)\,d𝑡\, & cross product rule\end{aligned}


$$

### Example: Applying the Product Rules

#### Question

Find $\displaystyle {\int_0^1} \mathbf c \times \mathbf f(t) \, \textrm d t$ given that $\displaystyle\int_0^1\mathbf f(t)\,\textrm d t = \mathbf i-3\,\mathbf j-4\,\mathbf k$ and $\mathbf c=\mathbf j-\mathbf k.$

#### Explanation

The cross-product rule states that

$$


{\int_0^1 } \mathbf c \times \mathbf f(t) \, \textrm d t = \mathbf c \times {\int_0^1 } \mathbf f(t) \, \textrm d t .


$$

Applying the cross-product rule, we have

$$


\begin{aligned}∫_{10}𝐜×𝐟(𝑡)\,d𝑡 & =𝐜×∫_{10}𝐟(𝑡)\,d𝑡 \\ & =(𝐣−𝐤)×(𝐢−3\,𝐣−4\,𝐤) \\ & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 0 & 1 & −1 \\ 1 & −3 & −4\end{matrix} \\ & =\begin{matrix}1 & −1 \\ −3 & −4\end{matrix}𝐢−\begin{matrix}0 & −1 \\ 1 & −4\end{matrix}𝐣+\begin{matrix}0 & 1 \\ 1 & −3\end{matrix}𝐤 \\ & =(−4−3)𝐢−(0+1)𝐣+(0−1)𝐤 \\ & =−7\,𝐢−\,𝐣−\,𝐤.\end{aligned}


$$
