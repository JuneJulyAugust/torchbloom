# The Inverse Hyperbolic Functions

Source: https://www.mathacademy.com/topics/969?courseId=105
Topic ID: 969

## Prerequisites

- [Solving Equations Containing the Exponential Function](../../../high-school/traditional/lessons/algebra-ii/870-solving-equations-containing-the-exponential-function.md)
- [The Hyperbolic Functions](./967-the-hyperbolic-functions.md)
- [Properties of Transformed Logarithmic Functions](../../../high-school/traditional/lessons/algebra-ii/1610-properties-of-transformed-logarithmic-functions.md)
- [Inverses of Quadratic Functions](../../../high-school/traditional/lessons/algebra-ii/3830-inverses-of-quadratic-functions.md)

## Lesson

### Introduction

The hyperbolic functions have inverse functions that are easy to define. The **inverse hyperbolic functions** are the following: $$

- The **inverse hyperbolic sine**, defined as The graph of the inverse hyperbolic sine function is given below.

- The **inverse hyperbolic cosine**, defined as The graph of the inverse hyperbolic cosine function is given below.

- The **inverse hyperbolic tangent**, defined as The graph of the inverse hyperbolic tangent function is given below.

For example, to calculate $\operatorname{arcosh}(\sqrt2)$ we substitute $x$ for $\sqrt2$ in the formula for $\operatorname{arcosh}$ and get

$$


\begin{aligned}arcosh⁡(\sqrt{2}) & =ln⁡(\sqrt{2}+\sqrt{(\sqrt{2})^{2}−1}) \\ & =ln⁡(\sqrt{2}+\sqrt{2−1}) \\ & =ln⁡(\sqrt{2}+1).\end{aligned}


$$

### Example: Applying the Definition of Inverse Hyperbolic Sine

#### Question

$$

$\operatorname{arsinh}{2} =$

#### Explanation

$$

The definition of $\operatorname{arsinh} x$ is

$$


\operatorname{arsinh}{x} =\ln\left(x+\sqrt{x^2+1}\right).


$$

Therefore,

$$


\begin{aligned} \operatorname{arsinh}{2} & = \ln\left(2 + \sqrt{2^2+1}\right)\\[5pt] & = \ln\left(2 + \sqrt{4+1}\right)\\[5pt] &=\ln\left(2 + \sqrt 5\right). \end{aligned}


$$

### Example: Applying the Definition of Inverse Hyperbolic Cosine

#### Question

$$

$\operatorname{arcosh}{3} =$

#### Explanation

$$

The definition of $\operatorname{arcosh}{x}$ is

$$


\operatorname{arcosh}{x} = \ln\left(x+\sqrt{x^2-1}\right).


$$

Therefore,

$$


\begin{aligned} \operatorname{arcosh}{3} & = \ln\left(3+\sqrt{3^2-1}\right)\\[3pt] & = \ln\left(3+\sqrt{9-1}\right)\\[3pt] & = \ln\left(3+\sqrt{8}\right)\\[3pt] &=\ln{\left(3+2\sqrt{2}\right)}. \end{aligned}


$$

### Example: Applying the Definition of Inverse Hyperbolic Tangent

#### Question

$$

$\operatorname{artanh}\left (\dfrac{1}{2} \right) =$

#### Explanation

$$

The definition of $\operatorname{artanh}{x}$ is

$$


\operatorname{artanh}{x} = \dfrac{1}{2}\ln\left(\dfrac{1+x}{1-x}\right).


$$

Therefore,

$$


\begin{aligned} \operatorname{artanh}\left ( \dfrac{1}{2} \right ) & = \dfrac{1}{2}\ln\left(\dfrac{1+\dfrac{1}{2}}{1-\dfrac{1}{2}}\right)\\[5pt] &=\dfrac{1}{2}\ln\left(\dfrac{\dfrac{3}{2}}{\dfrac{1}{2}}\right)\\[5pt] &=\dfrac{1}{2}\ln{3}. \end{aligned}


$$

### Deriving the Formulas for the Inverse Hyperbolic Functions

We can derive the formulas from inverse hyperbolic sine, cosine, and tangent from the definition of these base functions.

For example, let's show that $$

$$


\cosh^{-1}{x} = \operatorname{arcosh}{x} = \ln\big(x+\sqrt{x^2-1}\big), \qquad x \in [1, \infty).


$$

Recall that

$$


\cosh{x} = \dfrac12 \left( e^x + e^{-x} \right).


$$

First, let $y = \cosh{x}$ and $x \geq 0.$ Then we have $y\geq 1.$

To find the inverse function we swap $x$ and $y{:}$

$$


\begin{aligned}𝑥 & =cosh⁡𝑦\end{aligned}


$$

So, now we have that $x \geq 1$ and $y \geq 0.$

Next, we use the definition of $\cosh x$ and bring everything to the left-hand side:

$$


\begin{aligned}𝑥 & =\frac{1}{2}(𝑒^{𝑦}+𝑒^{−𝑦}) \\ 2𝑥 & =𝑒^{𝑦}+𝑒^{−𝑦} \\ 2𝑥𝑒^{𝑦} & =𝑒^{2𝑦}+1 \\ 𝑒^{2𝑦}−2𝑥𝑒^{𝑦}+1 & =0 \\ (𝑒^{𝑦})^{2}−2𝑥(𝑒^{𝑦})+1 & =0.\end{aligned}


$$

Letting $Y = e^{y},$ we form a quadratic equation in $Y$ and solve it by completing the square:

$$


\begin{aligned}𝑌^{2}−2𝑥𝑌+1 & =0 \\ (𝑌−𝑥)^{2}−𝑥^{2}+1 & =0 \\ (𝑌−𝑥)^{2} & =𝑥^{2}−1 \\ 𝑌−𝑥 & =±\sqrt{𝑥^{2}−1} \\ 𝑌 & =𝑥±\sqrt{𝑥^{2}−1} \\ 𝑒^{𝑦} & =𝑥±\sqrt{𝑥^{2}−1} \\ 𝑦 & =ln⁡(𝑥±\sqrt{𝑥^{2}−1})\end{aligned}


$$

Note that for $x\ge 1,$ we have $x-\sqrt{x^{2}-1}\leq 1$ and $x+\sqrt{x^{2}-1}\geq 1.$ Since $y \ge 0,$ the logarithm in the above equality must be positive, so we reject the alternative with the negative sign. This gives

$$


\begin{aligned}𝑦 & =ln⁡(𝑥+\sqrt{𝑥^{2}−1}).\end{aligned}


$$

So, we obtain our formula for $\operatorname{arcosh}{:}$

$$


f^{-1}(x)= \operatorname{arcosh}{x} = \ln\big(x+\sqrt{x^2-1}\big).


$$

### Example: Calculating an Inverse Hyperbolic Function From First-Principles

#### Question

$$

Using the definition of the hyperbolic sine, calculate $f^{-1}(x)$ given that $f(x) = \sinh{\left(x^2\right)}$ and $x \geq 0.$

#### Explanation

$$

Let $y = \sinh{\left(x^2\right)}.$ Since $x \geq 0,$ we have $y \geq 0.$

To find the inverse function we swap $x$ and $y{:}$

$$


x = \sinh{\left(y^2\right)},


$$

where $x\in[0,\infty)$ and $y\in[0,\infty).$

Next, we apply the definition of $\sinh x{:}$

$$


\begin{aligned}𝑥 & =\frac{1}{2}(𝑒^{𝑦^{2}}−𝑒^{−𝑦^{2}}) \\ 2𝑥 & =𝑒^{𝑦^{2}}−𝑒^{−𝑦^{2}} \\ 2𝑥𝑒^{𝑦^{2}} & =𝑒^{2𝑦^{2}}−1\end{aligned}


$$

Bringing everything to the left-hand side, we get

$$


\begin{aligned}𝑒^{2𝑦^{2}}−2𝑥𝑒^{𝑦^{2}}−1 & =0 \\ (𝑒^{𝑦^{2}})^{2}−2𝑥(𝑒^{𝑦^{2}})−1 & =0.\end{aligned}


$$

Let $Y = e^{y^2}.$ We can form a quadratic equation in $Y$ and solve it by completing the square, as follows:

$$


\begin{aligned}𝑌^{2}−2𝑥𝑌−1 & =0 \\ (𝑌−𝑥)^{2}−𝑥^{2}−1 & =0 \\ (𝑌−𝑥)^{2} & =𝑥^{2}+1 \\ 𝑌−𝑥 & =±\sqrt{𝑥^{2}+1} \\ 𝑌 & =𝑥±\sqrt{𝑥^{2}+1} \\ 𝑒^{𝑦^{2}} & =𝑥±\sqrt{𝑥^{2}+1}\end{aligned}


$$

Since $e^{y^2} >0$ for all real $y,$ and $x -\sqrt{x^2+1} <0,$ we must select the positive branch:

$$


\begin{aligned}𝑒^{𝑦^{2}} & =𝑥+\sqrt{𝑥^{2}+1} \\ ln⁡(𝑒^{𝑦^{2}}) & =ln⁡(𝑥+\sqrt{𝑥^{2}+1}) \\ 𝑦^{2} & =ln⁡(𝑥+\sqrt{𝑥^{2}+1}) \\ 𝑦 & =±\sqrt{ln⁡(𝑥+\sqrt{𝑥^{2}+1})}\end{aligned}


$$

Finally, since we require $y\ge 0,$ we select the positive solution. Therefore,

$$


f^{-1}(x) = \sqrt{\ln\left(x+\sqrt{x^2+1}\right)}.


$$
