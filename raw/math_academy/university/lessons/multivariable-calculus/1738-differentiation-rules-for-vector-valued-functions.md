# Differentiation Rules for Vector-Valued Functions

Source: https://www.mathacademy.com/topics/1738?courseId=54
Topic ID: 1738

## Prerequisites

- [Calculating the Dot Product Using Components](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/177-calculating-the-dot-product-using-components.md)
- [Differentiating Vector-Valued Functions](../../../ap-courses/lessons/ap-calculus-bc/4139-differentiating-vector-valued-functions.md)

## Lesson

### Introduction

Many of the known properties of derivatives of scalar functions extend naturally to derivatives of vector functions.

Suppose that $\mathbf f(t)$ and $\mathbf g(t)$ are vector-valued functions, $u(t)$ is a scalar function, and $\alpha$ and $\mathbf c$ are scalar and vector constants, respectively.

The **sum and multiple rules** for differentiating vector-valued functions are as follows:

$$


\begin{aligned}(𝐟+𝐠)^{′}(𝑡)=𝐟^{′}(𝑡)+𝐠^{′}(𝑡)\, & sum rule \\ (𝛼𝐟)^{′}(𝑡)=𝛼𝐟^{′}(𝑡),\,(𝑢𝐜)^{′}(𝑡)=𝑢^{′}(𝑡)𝐜\, & constant multiple rules \\ (𝑢𝐟)^{′}(𝑡)=𝑢^{′}(𝑡)𝐟(𝑡)+𝑢(𝑡)𝐟^{′}(𝑡)\, & scalar function multiple rule\end{aligned}


$$

### Example: Using the Sum and Constant Multiple Rules for Differentiation

#### Question

Find the derivative of $\mathbf f(t) + 2\mathbf g(t)$ with respect to $t,$ where $\mathbf f(t)$ and $\mathbf g(t)$ are defined as follows:

$$


\begin{aligned}𝐟(𝑡) & =(4𝑡^{2}+9)\,𝐢−(\frac{1}{𝑡−2})\,𝐣+cos⁡2𝑡\,𝐤 \\ 𝐠(𝑡) & =(4𝑡−1)\,𝐢+𝑒^{3𝑡}\,𝐣+cos⁡2𝑡\,𝐤\end{aligned}


$$

#### Explanation

Using the constant multiple rule and the sum rule, we have

$$


(\mathbf f(t) + 2\mathbf g(t))' = \mathbf f'(t) + 2\mathbf g'(t).


$$

Now, let's find the derivative of each function:

$$


\begin{aligned}𝐟^{′}(𝑡) & =\frac{d}{d𝑡}(4𝑡^{2}+9)\,𝐢+\frac{d}{d𝑡}(−\frac{1}{𝑡−2})\,𝐣+\frac{d}{d𝑡}(cos⁡2𝑡)\,𝐤 \\ & =8𝑡\,𝐢+\frac{1}{(𝑡−2)^{2}}\,𝐣−2sin⁡2𝑡\,𝐤, \\ 𝐠^{′}(𝑡) & =\frac{d}{d𝑡}(4𝑡−1)\,𝐢+\frac{d}{d𝑡}(𝑒^{3𝑡})𝐣+\frac{d}{d𝑡}(cos⁡2𝑡)𝐤 \\ & =4\,𝐢+3𝑒^{3𝑡}\,𝐣−2sin⁡2𝑡\,𝐤.\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}(𝐟(𝑡)+2𝐠(𝑡))^{′} & =𝐟^{′}(𝑡)+2𝐠^{′}(𝑡) \\ & =(8𝑡\,𝐢+\frac{1}{(𝑡−2)^{2}}\,𝐣−2sin⁡2𝑡\,𝐤)+2(4\,𝐢+3𝑒^{3𝑡}\,𝐣−2sin⁡2𝑡\,𝐤) \\ & =8(𝑡+1)\,𝐢+(\frac{1}{(𝑡−2)^{2}}+6𝑒^{3𝑡})\,𝐣−6sin⁡2𝑡\,𝐤.\end{aligned}


$$

### Example: Using the Scalar Function Multiple Rule for Differentiation

#### Question

Find $\big(u(t) \mathbf g(t) \big)'$ where $\begin{aligned}ln⁡𝑡 \\ −𝑡 \\ 𝑒^{2𝑡}\end{aligned}$ and $u(t) = t.$

#### Explanation

Using the scalar function multiple rule, we have

$$


\big( u(t) \mathbf g(t) \big)' = u'(t) \mathbf{g}(t) + u(t) \mathbf{g}'(t).


$$

Let's find $\mathbf g'(t)$ and $u'(t),$ as follows:

$$


\begin{aligned}𝐠^{′}(𝑡) & =\begin{matrix}\frac{d}{d𝑡}(ln⁡𝑡) \\ \frac{d}{d𝑡}(−𝑡) \\ \frac{d}{d𝑡}𝑒^{2𝑡}\end{matrix}=\begin{matrix}\frac{1}{𝑡} \\ −1 \\ 2𝑒^{2𝑡}\end{matrix} \\ 𝑢^{′}(𝑡) & =\frac{d}{d𝑡}(𝑡)=1\end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}(𝑢(𝑡)𝐠(𝑡))^{′} & =𝑢^{′}(𝑡)𝐠(𝑡)+𝑢(𝑡)𝐠^{′}(𝑡) \\ & =1⋅\begin{matrix}ln⁡𝑡 \\ −𝑡 \\ 𝑒^{2𝑡}\end{matrix}+𝑡⋅\begin{matrix}\frac{1}{𝑡} \\ −1 \\ 2𝑒^{2𝑡}\end{matrix} \\ & =\begin{matrix}ln⁡𝑡 \\ −𝑡 \\ 𝑒^{2𝑡}\end{matrix}+\begin{matrix}1 \\ −𝑡 \\ 2𝑡𝑒^{2𝑡}\end{matrix} \\ & =\begin{matrix}1+ln⁡𝑡 \\ −2𝑡 \\ (2𝑡+1)𝑒^{2𝑡}\end{matrix}.\end{aligned}


$$

### The Chain Rule for Differentiation

The **chain rule** for differentiating vector-valued functions states that

where is a vector-valued function while is a scalar function.

### Example: Using the Chain Rule for Differentiation

#### Question

Find $(\mathbf f \circ u)'(t),$ if $\mathbf f(u) = \ln u \, \mathbf i + (u^2+5) \, \mathbf j + 4u \, \mathbf k$ and $u(t) =2t^3.$

#### Explanation

By the chain rule, we have

$$


(\mathbf f \circ u)'(t) = \mathbf{f}'(u(t)) u'(t).


$$

Now, let's find the derivative of each function:

$$


\begin{aligned}𝐟^{′}(𝑢) & =\frac{d}{d𝑢}(ln⁡𝑢)\,𝐢+\frac{d}{d𝑢}(𝑢^{2}+5)\,𝐣+\frac{d}{d𝑢}(4𝑢)𝐤 \\ & =\frac{1}{𝑢}\,𝐢+2𝑢\,𝐣+4\,𝐤, \\ 𝑢^{′}(𝑡) & =\frac{d}{d𝑡}(2𝑡^{3})=6𝑡^{2}.\end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}(𝐟∘𝑢)^{′}(𝑡) & =𝐟^{′}(𝑢(𝑡))𝑢^{′}(𝑡) \\ & =(\frac{1}{𝑢(𝑡)}\,𝐢+2𝑢(𝑡)\,𝐣+4\,𝐤)𝑢^{′}(𝑡) \\ & =(\frac{1}{2𝑡^{3}}\,𝐢+2(2𝑡^{3})\,𝐣+4\,𝐤)⋅6𝑡^{2} \\ & =\frac{3}{𝑡}\,𝐢+24𝑡^{5}\,𝐣+24𝑡^{2}\,𝐤.\end{aligned}


$$

### The Product Rules for Differentiation

When working with vector functions, there are two types of products: the dot product and the cross product. So, there are two **product rules** for derivatives:

$$


\begin{aligned}(𝐟⋅𝐠)^{′}(𝑡)=𝐟(𝑡)⋅𝐠^{′}(𝑡)+𝐟^{′}(𝑡)⋅𝐠(𝑡)\, & dot product rule \\ (𝐟×𝐠)^{′}(𝑡)=𝐟^{′}(𝑡)×𝐠(𝑡)+𝐟(𝑡)×𝐠^{′}(𝑡)\, & cross product rule\end{aligned}


$$

**Watch out!** Remember that the cross product is anticommutative, meaning that $\mathbf f \times \mathbf g = - \mathbf g \times \mathbf f.$ Therefore,

$$


\dfrac{\textrm d}{\textrm dt} (\mathbf f \times \mathbf g)(t) = -\dfrac{\textrm d}{\textrm dt} (\mathbf g \times \mathbf f)(t).


$$

When applying the cross product rule, the order in which the operations are applied is important.

### Example: Using the Product Rules for Differentiation

#### Question

Find $\dfrac{\textrm d}{\textrm dt} (\mathbf f \cdot \mathbf g)(t),$ given the following functions $\mathbf f(t)$ and $\mathbf g(t)\mathbin{:}$

$$


\begin{aligned}𝐟(𝑡) & =\sqrt{𝑡}\,𝐢+𝑡^{2}𝐣 \\ 𝐠(𝑡) & =\frac{1}{𝑡}𝐢+𝑒^{𝑡}𝐣\end{aligned}


$$

#### Explanation

Using the dot product rule, we have

$$


\dfrac{\textrm d}{\textrm dt}(\mathbf{f} \cdot \mathbf{g})(t) = \dfrac{\textrm d}{\textrm dt}(\mathbf{f}(t)) \cdot \mathbf{g}(t) + \mathbf{f}(t) \cdot \dfrac{\textrm d}{\textrm dt}(\mathbf{g}(t))


$$

Let's now find the derivatives of each function:

$$


\begin{aligned}\frac{d}{d𝑡}𝐟(𝑡) & =\frac{d}{d𝑡}(\sqrt{𝑡})𝐢+\frac{d}{d𝑡}(𝑡^{2})𝐣 \\ & =\frac{1}{2\sqrt{𝑡}}\,𝐢+2𝑡\,𝐣, \\ \frac{d}{d𝑡}𝐠(𝑡) & =\frac{d}{d𝑡}(\frac{1}{𝑡})𝐢+\frac{d}{d𝑡}(𝑒^{𝑡})𝐣 \\ & =−\frac{1}{𝑡^{2}}\,𝐢+𝑒^{𝑡}\,𝐣.\end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned} \dfrac{\textrm d}{\textrm dt} (\mathbf f \cdot \mathbf g)(t) &= \dfrac{\textrm d}{\textrm dt}(\mathbf{f}(t)) \cdot \mathbf{g}(t) + \mathbf{f}(t) \cdot \dfrac{\textrm d}{\textrm dt}(\mathbf{g}(t)) \\[3pt] &= \left(\dfrac{1}{2\sqrt{t}} \,\mathbf i +2t \, \mathbf j \right) \cdot \left(\dfrac{1}{t} \, \mathbf i + e^t \, \mathbf j \right) + \left(\sqrt{t} \, \mathbf i + t^2 \, \mathbf j \right) \cdot \left(-\dfrac{1}{t^2} \, \mathbf i + e^t \, \mathbf j \right) \\[3pt] &=\dfrac{1}{2t\sqrt{t}} +2te^t + \left(-\dfrac{\sqrt{t}}{t^2}\right) + t^2e^t \\[3pt] &=\dfrac{\sqrt{t}}{2t^2} - \dfrac{\sqrt{t}}{t^2} +2te^t + t^2e^t \\[3pt] &= -\dfrac{\sqrt{t}}{2t^2} +\left(2t+t^2\right)e^t. \end{aligned}


$$
