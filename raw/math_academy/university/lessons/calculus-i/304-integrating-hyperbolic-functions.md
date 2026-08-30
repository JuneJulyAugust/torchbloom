# Integrating Hyperbolic Functions

Source: https://www.mathacademy.com/topics/304?courseId=105
Topic ID: 304

## Prerequisites

- [Differentiating Reciprocal Hyperbolic Functions](./3251-differentiating-reciprocal-hyperbolic-functions.md)
- [The Sum Rule for Indefinite Integrals](./3769-the-sum-rule-for-indefinite-integrals.md)

## Lesson

### Introduction

$$

We know that the derivative of the hyperbolic sine is the hyperbolic cosine:

$$


\dfrac{\textrm d }{\textrm d x}(\sinh{x}) = \cosh{x}


$$

Since integration is the reverse of differentiation, we have

$$


\int \cosh{x}\,\textrm d x = \sinh{x} + C.


$$

Similarly, by considering the derivative of the hyperbolic cosine, we have

$$


\dfrac{\textrm d }{\textrm d x}(\cosh x) = \sinh{x} \qquad\Rightarrow\qquad \int \sinh x\ \text{d}x = \cosh x + C.


$$

### Example: Integrating the Hyperbolic Sine and the Hyperbolic Cosine

#### Question

$$

Calculate $\displaystyle \int 8\cosh t \,\text{d}t.$

#### Explanation

Recall that

$$


\dfrac{\textrm d}{\textrm d t}(\sinh t) = \cosh{t} \quad\Rightarrow\quad \int \cosh{t} \, \textrm dt = \sinh{t} + C.


$$

Therefore, we have

$$


\begin{aligned}∫8cosh⁡𝑡\,d𝑡=8∫cosh⁡𝑡\,d𝑡=8sinh⁡𝑡+𝐶.\end{aligned}


$$

### Integration Using Reciprocal Hyperbolic Functions

$$

By considering the derivatives of the hyperbolic tangent, secant, cosecant, and cotangent, we arrive at the following results:

$$


\begin{aligned}∫sech^{2}⁡𝑥 d𝑥 & =tanh⁡𝑥+𝐶 \\ ∫sech⁡𝑥tanh⁡𝑥 d𝑥 & =−sech⁡𝑥+𝐶 \\ ∫csch⁡𝑥coth⁡𝑥 d𝑥 & =−csch⁡𝑥+𝐶 \\ ∫csch^{2}⁡𝑥 d𝑥 & =−coth⁡𝑥+𝐶\end{aligned}


$$

### Example: Integrating Hyperbolic Secant-Tangent and Cosecant-Cotangent

#### Question

$$

$\displaystyle \int \left(-3\operatorname{sech} x \tanh x\right) \,\text{d}x =$

#### Explanation

$$

Recall that

$$


\dfrac{\textrm d}{\textrm d x}(\operatorname{sech} x) = -\operatorname{sech}{x}\tanh x \quad\Rightarrow\quad \int \operatorname{sech}{x}\tanh{x} \, \textrm dx = -\operatorname{sech}{x} + C.


$$

Therefore, we have

$$


\begin{aligned}∫(−3sech⁡𝑥tanh⁡𝑥)\,d𝑥 & =−3∫sech⁡𝑥tanh⁡𝑥\,d𝑥 \\ & =−3(−sech⁡𝑥)+𝐶 \\ & =3sech⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating the Square of the Hyperbolic Secant

#### Question

$$

$\displaystyle \int 6\operatorname{sech}^2 x \,\text{d}x =$

#### Explanation

$$

Recall that

$$


\dfrac{\textrm d}{\textrm d x}(\tanh x) = \operatorname{sech}^2{x} \quad\Rightarrow\quad \int \operatorname{sech}^2{x} \, \textrm dx = \tanh{x} + C.


$$

Therefore, we have

$$


\begin{aligned}∫6sech^{2}⁡𝑥\,d𝑥=6∫sech^{2}⁡𝑥\,d𝑥=6tanh⁡𝑥+𝐶.\end{aligned}


$$

### Example: Integrating the Square of the Hyperbolic Cosecant

#### Question

$$

$\displaystyle \int (-8\operatorname{csch}^2 x)\,\text{d}x =$

#### Explanation

$$

Recall that

$$


\dfrac{\textrm d}{\textrm d x}(\coth x) = -\operatorname{csch}^2{x} \quad\Rightarrow\quad \int \operatorname{csch}^2{x} \, \textrm dx = -\coth{x} + C.


$$

Therefore, we have

$$


\begin{aligned}∫(−8csch^{2}⁡𝑥)\,d𝑥 & =−8∫csch^{2}⁡𝑥\,d𝑥 \\ & =−(−8coth⁡𝑥)+𝐶 \\ & =8coth⁡𝑥+𝐶.\end{aligned}


$$
