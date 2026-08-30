# Solving Logarithmic Equations Containing the Natural Logarithm

Source: https://www.mathacademy.com/topics/1551?courseId=51
Topic ID: 1551

## Prerequisites

- [Solving Logarithmic Equations](./226-solving-logarithmic-equations.md)

## Lesson

### Introduction

To solve logarithmic equations containing the natural logarithm $(\ln),$ we can use the same method as usual: first isolate the logarithm, and then exponentiate both sides of the equation using the same base as the logarithm.

The key is to remember that the base of the natural logarithm is $e.$

To demonstrate, let's solve for $x$ in the equation $\ln x = 2.$

To remove the logarithm, we exponentiate both sides of the equation. The logarithm is a natural logarithm, which means its base is $e.$ So, we use a base of $e$ for the exponentiation as well:

$$


\begin{aligned}ln⁡𝑥 & =2 \\ 𝑒^{ln⁡𝑥} & =𝑒^{2}\end{aligned}


$$

Since exponentiation is the inverse function of the logarithm, we know that $e^{\ln x} = x.$

Therefore, we get

$$


\begin{aligned}𝑥 & =𝑒^{2}.\end{aligned}


$$

So, the solution is $x=e^2.$

### Example: Solving Natural Logarithmic Equations

#### Question

Solve for $x$ if $\ln(4x+5)=3.$

#### Explanation

To remove the logarithm, we exponentiate both sides of the equation. The logarithm is a natural logarithm, which means its base is $e.$ So, we use a base of $e$ for the exponentiation as well:

$$


\begin{aligned}ln⁡(4𝑥+5) & =3 \\ 𝑒^{ln⁡(4𝑥+5)} & =𝑒^{3}\end{aligned}


$$

Since exponentiation is the inverse function of the logarithm, we know that $e^{\ln(4x+5)} = 4x+5.$

Therefore, we get

$$


\begin{aligned}4𝑥+5 & =𝑒^{3} \\ 4𝑥 & =𝑒^{3}−5 \\ 𝑥 & =\frac{𝑒^{3}−5}{4}.\end{aligned}


$$

### Example: Solving Natural Logarithmic Equations by First Rearranging the Equation

#### Question

Find the exact solution to $3\ln (5x+1)-2 = 13.$

#### Explanation

First, we rearrange our equation to isolate the logarithmic term, as follows:

$$


\begin{aligned}3ln⁡(5𝑥+1)−2 & =13 \\ 3ln⁡(5𝑥+1) & =15 \\ ln⁡(5𝑥+1) & =5\end{aligned}


$$

To remove the natural logarithm, we exponentiate both sides of the equation. The base of the natural logarithm is $e,$ so we use a base of $e$ for the exponentiation as well:

$$


\begin{aligned}ln⁡(5𝑥+1) & =5 \\ 𝑒^{ln⁡(5𝑥+1)} & =𝑒^{5}\end{aligned}


$$

Since exponentiation is the inverse function of the logarithm, we know that $e^{\ln (5x+1)} = 5x+1.$

Therefore, we get

$$


\begin{aligned}5𝑥+1 & =𝑒^{5} \\ 5𝑥 & =𝑒^{5}−1 \\ 𝑥 & =\frac{𝑒^{5}−1}{5}.\end{aligned}


$$

### Example: Solving Natural Logarithmic Equations by Combining Logarithmic Terms

#### Question

Find the values of $x$ such that $\ln(1-2x) + 5\ln(1-2x) = 4.$

#### Explanation

First, we rearrange our equation by collecting the like logarithmic terms, as follows:

$$


\begin{aligned}ln⁡(1−2𝑥)+5ln⁡(1−2𝑥) & =4 \\ (1+5)ln⁡(1−2𝑥) & =4 \\ 6ln⁡(1−2𝑥) & =4 \\ ln⁡(1−2𝑥) & =\frac{2}{3}\end{aligned}


$$

To remove the natural logarithm, we exponentiate both sides of the equation. The base of the natural logarithm is $e,$ so we use a base of $e$ for the exponentiation as well:

$$


\begin{aligned}ln⁡(1−2𝑥) & =\frac{2}{3} \\ 𝑒^{ln⁡(1−2𝑥)} & =𝑒^{2/3}\end{aligned}


$$

Since exponentiation is the inverse function of the logarithm, we know that $e^{\ln(1-2x)} = 1-2x.$

Therefore, we get

$$


\begin{aligned}1−2𝑥 & =𝑒^{2/3} \\ 1−2𝑥 & =\sqrt[√𝑒^{2}]{3} \\ −2𝑥 & =\sqrt[√𝑒^{2}]{3}−1 \\ 𝑥 & =−\frac{\sqrt[√𝑒^{2}]{3}−1}{2} \\ 𝑥 & =\frac{−\sqrt[√𝑒^{2}]{3}+1}{2} \\ 𝑥 & =\frac{1−\sqrt[√𝑒^{2}]{3}}{2}.\end{aligned}


$$
