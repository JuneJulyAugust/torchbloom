# Applying the Integration By Parts Twice

Source: https://www.mathacademy.com/topics/416?courseId=136
Topic ID: 416

## Prerequisites

- [Using Integration by Parts to Calculate Integrals With Logarithms](./1140-using-integration-by-parts-to-calculate-integrals-with-logarithms.md)

## Lesson

### Introduction

We know that we can use the method of integration by parts to evaluate $\displaystyle \int xe^{4x} \text{d}x.$ Now, suppose that we want to calculate $\displaystyle \int x^2e^{4x} \text{d}x.$ Can we use integration by parts in this case?

Let's try. We define $u$ and $v$ as follows:

$$


\begin{aligned}𝑢=𝑥^{2} & \,⟹\,\frac{d𝑢}{d𝑥}=2𝑥\,, \\ \frac{d𝑣}{d𝑥}=𝑒^{4𝑥} & \,⟹\,𝑣=∫𝑒^{4𝑥}d𝑥=\frac{1}{4}\,𝑒^{4𝑥}\,.\end{aligned}


$$

So the formula for integration by parts leads to

$$


\begin{aligned}∫𝑥^{2}𝑒^{4𝑥}d𝑥 & =∫𝑢\frac{d𝑣}{d𝑥}d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}d𝑥 \\ & =𝑥^{2}(\frac{1}{4}\,𝑒^{4𝑥})−∫(\frac{1}{4}\,𝑒^{4𝑥})2𝑥\,d𝑥 \\ & =\frac{1}{4}\,𝑥^{2}𝑒^{4𝑥}−\frac{1}{2}∫𝑥𝑒^{4𝑥}d𝑥.\end{aligned}


$$

We still don't have an answer, but the problem is reduced to the calculation of a simpler integral $\displaystyle \int xe^{4x} \text{d}x.$ To compute this integral, we just need to apply the integration by parts formula again. For this second integral, we take

$$


\begin{aligned}𝑢=𝑥 & \,⟹\,\frac{d𝑢}{d𝑥}=1\,, \\ \frac{d𝑣}{d𝑥}=𝑒^{4𝑥} & \,⟹\,𝑣=∫𝑒^{4𝑥}d𝑥=\frac{1}{4}\,𝑒^{4𝑥}\,.\end{aligned}


$$

Now, integration by parts gives

$$


\begin{aligned}∫𝑥𝑒^{4𝑥}d𝑥 & =∫𝑢\frac{d𝑣}{d𝑥}d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}d𝑥 \\ & =𝑥(\frac{1}{4}\,𝑒^{4𝑥})−∫(\frac{1}{4}\,𝑒^{4𝑥})⋅1\,d𝑥 \\ & =\frac{1}{4}\,𝑥𝑒^{4𝑥}−\frac{1}{4}(\frac{1}{4}\,𝑒^{4𝑥})+𝐶_{1} \\ & =\frac{1}{4}\,𝑥𝑒^{4𝑥}−\frac{1}{16}\,𝑒^{4𝑥}+𝐶_{1}\,,\end{aligned}


$$

where $C_1$ is a constant of integration. So we have

$$


\begin{aligned}∫𝑥^{2}𝑒^{4𝑥}d𝑥 & =\frac{1}{4}\,𝑥^{2}𝑒^{4𝑥}−\frac{1}{2}∫𝑥𝑒^{4𝑥}d𝑥 \\ & =\frac{1}{4}\,𝑥^{2}𝑒^{4𝑥}−\frac{1}{2}(\frac{1}{4}\,𝑥𝑒^{4𝑥}−\frac{1}{16}\,𝑒^{4𝑥}+𝐶_{1}) \\ & =\frac{1}{4}\,𝑥^{2}𝑒^{4𝑥}−\frac{1}{8}\,𝑥𝑒^{4𝑥}+\frac{1}{32}\,𝑒^{4𝑥}−\frac{𝐶_{1}}{2} \\ & =\frac{1}{32}\,𝑒^{4𝑥}(8𝑥^{2}−4𝑥+1)+𝐶\end{aligned}


$$

where $C = -\dfrac{C_1}{2}.$

### Example: Computing the Integral of an Exponential Expression Using Integration by Parts Twice

#### Question

Evaluate the integral $\displaystyle \int_0^1 (t^2+1)e^{2t+1} \, \text{d} t.$

#### Explanation

We need to use integration by parts. We'll work out the indefinite integral first, and then proceed to work out the definite integral.

In this case, we define

$$


\begin{aligned}𝑢=𝑡^{2}+1\, & ⟹\,\frac{d𝑢}{d𝑡}=2𝑡, \\ \frac{d𝑣}{d𝑡}=𝑒^{2𝑡+1}\, & ⟹\,𝑣=∫\frac{d𝑣}{d𝑡}\,d𝑡=∫𝑒^{2𝑡+1}\,d𝑡=\frac{𝑒^{2𝑡+1}}{2}.\end{aligned}


$$

Using the formula of integration by parts, we get

$$


\begin{aligned}∫(𝑡^{2}+1)𝑒^{2𝑡+1}\,d𝑡 & =∫𝑢\frac{d𝑣}{d𝑡}\,d𝑡 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑡}\,d𝑡 \\ & =(𝑡^{2}+1)(\frac{𝑒^{2𝑡+1}}{2})−∫(\frac{𝑒^{2𝑡+1}}{2})(2𝑡)\,d𝑡 \\ & =\frac{(𝑡^{2}+1)𝑒^{2𝑡+1}}{2}−∫𝑡\,𝑒^{2𝑡+1}\,d𝑡.\end{aligned}


$$

We use integration by parts once again to evaluate $\displaystyle\int t\,e^{2t+1}\,\text{d}t.$ We take

$$


\begin{aligned}𝑢=𝑡\, & ⟹\,\frac{d𝑢}{d𝑡}=1 \\ \frac{d𝑣}{d𝑡}=𝑒^{2𝑡+1}\, & ⟹\,𝑣=∫\frac{d𝑣}{d𝑡}\,d𝑡=∫𝑒^{2𝑡+1}\,d𝑡=\frac{𝑒^{2𝑡+1}}{2}.\end{aligned}


$$

In this case, the formula for integration by parts gives

$$


\begin{aligned}∫𝑡\,𝑒^{2𝑡+1}\,d𝑡 & =∫𝑢\frac{d𝑣}{d𝑡}\,d𝑡 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑡}\,d𝑡 \\ & =(𝑡)(\frac{𝑒^{2𝑡+1}}{2})−∫(\frac{𝑒^{2𝑡+1}}{2})(1)\,d𝑡 \\ & =\frac{𝑡\,𝑒^{2𝑡+1}}{2}−\frac{1}{2}∫𝑒^{2𝑡+1}\,d𝑡 \\ & =\frac{𝑡\,𝑒^{2𝑡+1}}{2}−\frac{𝑒^{2𝑡+1}}{4}+𝐷,\end{aligned}


$$

where $D$ is a constant.

So, we get that the indefinite integral is

$$


\begin{aligned}∫(𝑡^{2}+1)𝑒^{2𝑡+1}\,d𝑡 & =\frac{(𝑡^{2}+1)𝑒^{2𝑡+1}}{2}−∫𝑡\,𝑒^{2𝑡+1}\,d𝑡 \\ & =\frac{(𝑡^{2}+1)𝑒^{2𝑡+1}}{2}−(\frac{𝑡\,𝑒^{2𝑡+1}}{2}−\frac{𝑒^{2𝑡+1}}{4}+𝐷) \\ & =\frac{(𝑡^{2}+1)𝑒^{2𝑡+1}}{2}−\frac{𝑡\,𝑒^{2𝑡+1}}{2}+\frac{𝑒^{2𝑡+1}}{4}−𝐷 \\ & =\frac{𝑒^{2𝑡+1}}{4}(2𝑡^{2}−2𝑡+3)+𝐶,\end{aligned}


$$

where $C = -{D}.$

Finally then, we can work out the definite integral:

$$


\begin{aligned}∫_{10}(𝑡^{2}+1)𝑒^{2𝑡+1}\,d𝑡 & =[\frac{𝑒^{2𝑡+1}}{4}(2𝑡^{2}−2𝑡+3)]_{10} \\ & =(\frac{𝑒^{2(1)+1}}{4}(2(1)^{2}−2(1)+3))−(\frac{𝑒^{2(0)+1}}{4}(2(0)^{2}−2(0)+3)) \\ & =\frac{𝑒^{3}}{4}(2−2+3)−\frac{𝑒}{4}(0−0+3) \\ & =\frac{3𝑒^{3}}{4}−\frac{3𝑒}{4} \\ & =\frac{3𝑒^{3}−3𝑒}{4}\end{aligned}


$$

### Example: Computing the Integral of a Trigonometric Expression Using Integration by Parts Twice

#### Question

Evaluate the integral $\displaystyle \int x^2\cos(3x) \text{d}x.$

#### Explanation

In this case, we define

$$


\begin{aligned}𝑢=𝑥^{2} & \,⟹\,\frac{d𝑢}{d𝑥}=2𝑥\,, \\ \frac{d𝑣}{d𝑥}=cos⁡(3𝑥) & \,⟹\,𝑣=∫cos⁡(3𝑥)d𝑥=\frac{1}{3}\,sin⁡(3𝑥)\,.\end{aligned}


$$

Using the formula for integration by parts, we get

$$


\begin{aligned}∫𝑥^{2}cos⁡(3𝑥)d𝑥 & =∫𝑢\frac{d𝑣}{d𝑥}d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}d𝑥 \\ & =(𝑥^{2})(\frac{1}{3}\,sin⁡(3𝑥))−∫(\frac{1}{3}\,sin⁡(3𝑥))2𝑥\,d𝑥 \\ & =\frac{1}{3}𝑥^{2}sin⁡(3𝑥)−\frac{2}{3}∫𝑥sin⁡(3𝑥)d𝑥.\end{aligned}


$$

Again, we use integration by parts to evaluate $\displaystyle \int x\sin(3x) \text{d}x.$ We take

$$


\begin{aligned}𝑢=𝑥 & \,⟹\,\frac{d𝑢}{d𝑥}=1\,, \\ \frac{d𝑣}{d𝑥}=sin⁡(3𝑥) & \,⟹\,𝑣=∫sin⁡(3𝑥)d𝑥=−\,\frac{1}{3}\,cos⁡(3𝑥)\,.\end{aligned}


$$

In this case, the formula for integration by parts gives

$$


\begin{aligned}∫𝑥sin⁡(3𝑥)d𝑥 & =∫𝑢\frac{d𝑣}{d𝑥}d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}d𝑥 \\ & =𝑥(−\,\frac{1}{3}\,cos⁡(3𝑥))−∫(−\,\frac{1}{3}\,cos⁡(3𝑥))⋅1\,d𝑥 \\ & =−\,\frac{1}{3}\,𝑥cos⁡(3𝑥)+\frac{1}{3}∫cos⁡(3𝑥)d𝑥 \\ & =−\,\frac{1}{3}\,𝑥cos⁡(3𝑥)+\frac{1}{3}(\frac{1}{3}\,sin⁡(3𝑥))+𝐶_{1} \\ & =−\,\frac{1}{3}\,𝑥cos⁡(3𝑥)+\frac{1}{9}\,sin⁡(3𝑥)+𝐶_{1}\,\end{aligned}


$$

where $C_1$ is a constant of integration. So we have

$$


\begin{aligned}∫𝑥^{2}cos⁡(3𝑥)d𝑥 & =\frac{1}{3}𝑥^{2}sin⁡(3𝑥)−\frac{2}{3}∫𝑥sin⁡(3𝑥)d𝑥 \\ & =\frac{1}{3}𝑥^{2}sin⁡(3𝑥)−\frac{2}{3}(−\,\frac{1}{3}\,𝑥cos⁡(3𝑥)+\frac{1}{9}\,sin⁡(3𝑥)+𝐶_{1}) \\ & =\frac{1}{3}𝑥^{2}sin⁡(3𝑥)+\frac{2}{9}𝑥cos⁡(3𝑥)−\frac{2}{27}sin⁡(3𝑥)−\frac{2𝐶_{1}}{3} \\ & =\frac{1}{27}((9𝑥^{2}−2)sin⁡(3𝑥)+6𝑥cos⁡(3𝑥))+𝐶,\end{aligned}


$$

where $C = -\dfrac{2C_1}{3}.$

### Example: Computing the Integral of a Logarithmic Expression Using Integration by Parts Twice

#### Question

Evaluate the integral $\displaystyle \int_1^e 32x^3(\ln x)^2 \text{d}x.$

#### Explanation

We'll work out the indefinite integral first, and then proceed to work out the definite integral.

In this case, we define

$$


\begin{aligned}𝑢=(ln⁡𝑥)^{2} & \,⟹\,\frac{d𝑢}{d𝑥}=\frac{2ln⁡𝑥}{𝑥}\,, \\ \frac{d𝑣}{d𝑥}=32𝑥^{3} & \,⟹\,𝑣=∫32𝑥^{3}d𝑥=8𝑥^{4}\,.\end{aligned}


$$

Using the formula of integration by parts, we get

$$


\begin{aligned}∫32𝑥^{3}(ln⁡𝑥)^{2}d𝑥 & =∫𝑢\frac{d𝑣}{d𝑥}d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}d𝑥 \\ & =(ln⁡𝑥)^{2}(8𝑥^{4})−∫(8𝑥^{4})(\frac{2ln⁡𝑥}{𝑥})d𝑥 \\ & =8𝑥^{4}(ln⁡𝑥)^{2}−16∫𝑥^{3}ln⁡(𝑥)d𝑥.\end{aligned}


$$

We use integration by parts once again to evaluate $\displaystyle\int {x^3\ln(x)} \text{d}x.$ We take

$$


\begin{aligned}𝑢=ln⁡(𝑥) & \,⟹\,\frac{d𝑢}{d𝑥}=\frac{1}{𝑥}\,, \\ \frac{d𝑣}{d𝑥}=𝑥^{3} & \,⟹\,𝑣=∫𝑥^{3}d𝑥=\frac{𝑥^{4}}{4}\,.\end{aligned}


$$

In this case, the formula for integration by parts gives

$$


\begin{aligned}∫𝑥^{3}ln⁡(𝑥)d𝑥 & =∫𝑢\frac{d𝑣}{d𝑥}d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}d𝑥 \\ & =ln⁡(𝑥)(\frac{𝑥^{4}}{4})−∫(\frac{𝑥^{4}}{4})(\frac{1}{𝑥})d𝑥 \\ & =\frac{𝑥^{4}ln⁡(𝑥)}{4}−\frac{1}{4}∫𝑥^{3}d𝑥 \\ & =\frac{𝑥^{4}ln⁡(𝑥)}{4}−\frac{𝑥^{4}}{16}+𝐶_{1}\end{aligned}


$$

where $C_1$ is an integral constant. So, we get that the indefinite integral is

$$


\begin{aligned}∫32𝑥^{3}(ln⁡𝑥)^{2}d𝑥 & =8𝑥^{4}(ln⁡𝑥)^{2}−16∫𝑥^{3}ln⁡(𝑥)d𝑥 \\ & =8𝑥^{4}(ln⁡𝑥)^{2}−16(\frac{𝑥^{4}ln⁡(𝑥)}{4}−\frac{𝑥^{4}}{16}+𝐶_{1}) \\ & =8𝑥^{4}(ln⁡𝑥)^{2}−4𝑥^{4}ln⁡(𝑥)+𝑥^{4}−16𝐶_{1} \\ & =𝑥^{4}(8(ln⁡𝑥)^{2}−4ln⁡(𝑥)+1)+𝐶\,\end{aligned}


$$

where $C = -4C_1.$ Finally then, we can work out the definite integral:

$$


\begin{aligned}∫_{𝑒1}32𝑥^{3}ln⁡(𝑥)d𝑥 & =𝑥^{4}(8(ln⁡𝑥)^{2}−4ln⁡(𝑥)+1)_{𝑒1} \\ & =[(𝑒)^{4}(8(ln⁡(𝑒))^{2}−4ln⁡(𝑒)+1)]−[(1)^{4}(8(ln⁡(1))^{2}−4ln⁡(1)+1)] \\ & =[𝑒^{4}(8−4+1)]−1 \\ & =5𝑒^{4}−1.\end{aligned}


$$
