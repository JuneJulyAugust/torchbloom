# Integrating Vector-Valued Functions

Source: https://www.mathacademy.com/topics/1085?courseId=136
Topic ID: 1085

## Prerequisites

- [Integrating Trigonometric Functions Using Substitution](./478-integrating-trigonometric-functions-using-substitution.md)
- [Integrating Exponential Functions Using Substitution](./3770-integrating-exponential-functions-using-substitution.md)
- [Differentiating Vector-Valued Functions](./4139-differentiating-vector-valued-functions.md)

## Lesson

### Introduction

How do we integrate a vector-valued function? For example, if $\mathbf{r}(t) = \langle e^{2t}, \, \sin{t}\rangle,$ then how do we calculate

$$


\int \mathbf{r}(t) \,\textrm d t\,?


$$

Integrating vector-valued functions is similar to differentiating them, in the sense that we just integrate each component individually. Doing that, we get

$$


\begin{aligned}∫𝐫(𝑡)\,d𝑡 & =∫⟨𝑒^{2𝑡},\,sin⁡𝑡⟩\,d𝑡 \\ & =⟨∫𝑒^{2𝑡}\,d𝑡,\,∫sin⁡𝑡\,d𝑡⟩ \\ & =⟨\frac{1}{2}𝑒^{2𝑡}+𝑐_{1},\,−cos⁡𝑡+𝑐_{2}⟩ \\ & =⟨\frac{1}{2}𝑒^{2𝑡},\,−cos⁡𝑡⟩+⟨𝑐_{1},\,𝑐_{2}⟩ \\ & =⟨\frac{1}{2}𝑒^{2𝑡},\,−cos⁡𝑡⟩+𝐂,\end{aligned}


$$

where $\mathbf C = \langle c_1,\, c_2\rangle$ is an arbitrary (vector) constant of integration.

### Example: Finding the Antiderivative of a Vector-Valued Function

#### Question

Find $\mathbf F(t)$ given that $\mathbf F'(t)= \langle 6t^5+2t, \sec^2 t\rangle.$

#### Explanation

Note that

$$


\mathbf F(t)=\int \mathbf F'(t)\, \textrm d t=\int \left\langle 6t^5+2t,\, \sec^2 t\right\rangle \, \textrm d t.


$$

To integrate a vector-valued function, we integrate each component separately. So, we get

$$


\begin{aligned}∫⟨6𝑡^{5}+2𝑡,\,sec^{2}⁡𝑡⟩\,d𝑡 & =⟨∫(6𝑡^{5}+2𝑡)\,d𝑡,\,∫sec^{2}⁡𝑡\,d𝑡⟩ \\ & =⟨𝑡^{6}+𝑡^{2}+𝑐_{1},\,tan⁡𝑡+𝑐_{2}⟩ \\ & =⟨𝑡^{6}+𝑡^{2},\,tan⁡𝑡⟩+⟨𝑐_{1},\,𝑐_{2}⟩ \\ & =⟨𝑡^{6}+𝑡^{2},\,tan⁡𝑡⟩+𝐂,\end{aligned}


$$

where $\mathbf C$ is an arbitrary (vector) constant of integration.

### Example: Integrating a Vector-Valued Function

#### Question

Calculate $\displaystyle \int \left\langle\cos(2t+1), \, 4\right\rangle \,\textrm d t\,.$

#### Explanation

To integrate a vector-valued function, we integrate each component separately:

$$


\begin{aligned}∫⟨cos⁡(2𝑡+1),\,4⟩\,d𝑡=⟨∫cos⁡(2𝑡+1)\,d𝑡,\,∫4\,d𝑡⟩.\end{aligned}


$$

- For $x(t) =\cos(2t+1),$ we calculate its integral using substitution. So, we let $u= 2t +1.$ Then Therefore, we have

- For $y(t) =4,$ we have

Finally, we have

$$


\begin{aligned}∫⟨cos⁡(2𝑡+1),\,4⟩\,d𝑡 & =⟨\frac{1}{2}sin⁡(2𝑡+1)+𝑐_{1},\,4𝑡+𝑐_{2}⟩ \\ & =⟨\frac{1}{2}sin⁡(2𝑡+1),\,4𝑡⟩+⟨𝑐_{1},\,𝑐_{2}⟩ \\ & =⟨\frac{1}{2}sin⁡(2𝑡+1),\,4𝑡⟩+𝐂.\end{aligned}


$$

### Example: Finding the Definite Integral of a Vector-Valued Function

#### Question

Evaluate $\displaystyle \int_0^{2} \left\langle 2e^{t},\, 6t^2\right\rangle\, \textrm d t.$

#### Explanation

To integrate a vector-valued function, we integrate each component separately:

$$


\begin{aligned}∫_{20}^{}⟨2𝑒^{𝑡},\,6𝑡^{2}⟩\,d𝑡 & =⟨∫_{20}^{}2𝑒^{𝑡}\,d𝑡,\,∫_{20}^{}6𝑡^{2}\,d𝑡⟩. \\ & =⟨2𝑒^{𝑡}\,\,_{20}^{},\,2𝑡^{3}\,\,_{20}^{}⟩ \\ & =⟨[2𝑒^{2}−2𝑒^{0}],\,[2⋅2^{3}−0]⟩ \\ & =⟨2𝑒^{2}−2,\,16⟩\end{aligned}


$$

### Example: Finding the Antiderivative of a Vector-Valued Function That Satisfies a Given Initial Condition

#### Question

Calculate $\mathbf F(t)$ given that $\mathbf F'(t)= \left\langle \sec t \tan t, \, \sin(2t)\right\rangle$ and $\mathbf F(0)=\langle 0,\, 0\rangle.$

#### Explanation

Note that

$$


\mathbf F(t)=\int \mathbf F'(t)\, \textrm d t=\int \left\langle \sec t \tan t,\, \sin(2t)\right\rangle \, \textrm d t.


$$

To integrate a vector-valued function, we integrate each component separately. So, we have

$$


\begin{aligned}∫⟨sec⁡𝑡tan⁡𝑡,\,sin⁡(2𝑡)⟩\,d𝑡 & =⟨∫sec⁡𝑡tan⁡𝑡\,d𝑡,∫sin⁡(2𝑡)\,d𝑡⟩ \\ & =⟨sec⁡𝑡+𝑐_{1},\,−\frac{1}{2}cos⁡(2𝑡)+𝑐_{2}⟩.\end{aligned}


$$

The initial condition $\mathbf F(0)=\left\langle 0,\, 0 \right\rangle$ gives

$$


\begin{aligned}𝐅(0)=⟨sec⁡0+𝑐_{1},\,−\frac{1}{2}cos⁡(2⋅0)+𝑐_{2}⟩ & =⟨0,\,0⟩ \\ ⟨1+𝑐_{1},\,−\frac{1}{2}+𝑐_{2}⟩ & =⟨0,\,0⟩.\end{aligned}


$$

Therefore, $c_1=-1$ and $c_2=\dfrac 12.$ Consequently,

$$


\mathbf F(t)=\left\langle \sec t - 1 , \, -\dfrac 1 2\cos(2t)+ \dfrac12\right\rangle.


$$
