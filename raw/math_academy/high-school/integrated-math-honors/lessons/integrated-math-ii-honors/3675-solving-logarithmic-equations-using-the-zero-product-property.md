# Solving Logarithmic Equations Using the Zero-Product Property

Source: https://www.mathacademy.com/topics/3675?courseId=128
Topic ID: 3675

## Prerequisites

- [Solving Quadratic Equations Using a Difference of Squares](../../../traditional/lessons/algebra-i/394-solving-quadratic-equations-using-a-difference-of-squares.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../../../traditional/lessons/algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)
- [Properties of Transformed Logarithmic Functions](../../../traditional/lessons/algebra-ii/1610-properties-of-transformed-logarithmic-functions.md)

## Lesson

### Introduction

We can use the zero product property to solve equations involving logarithms. The only catch is that we need to discard any extraneous solutions that are not in the domain of the logarithm (we can only take the logarithm of a positive number).

For example, suppose we want to find all of the solutions to the equation

$$


x \cdot \ln x + 3 \ln x = 0.


$$

First, we factor the equation:

$$


\begin{aligned}𝑥⋅ln⁡𝑥+3ln⁡𝑥 & =0 \\ (𝑥+3)ln⁡𝑥 & =0\end{aligned}


$$

We can now apply the zero product property, which states that $ab=0$ if and only if $a=0$ or $b=0.$ This gives us two equations,

$$


x+3 = 0 \quad \text{and} \quad \ln x =0.


$$

We now solve each of these equations separately.

- The equation $x+3=0$ has the solution $x=-3.$

- The equation $\ln x =0$ has the solution $x=e^0 = 1.$

So, we have two candidate solutions, $x=-3,1.$ However, we need to check whether these equations are in the domain of the logarithm in the original equation.

The original equation contains the logarithm $\ln x,$ and the domain is $(0, \infty).$

- The candidate $x=-3$ does not lie in the domain, so we discard it.

- The candidate $x=1$ lies in the domain, so we keep it.

Therefore, the original equation has a single solution, $x=1.$

### Example: Solving a Logarithmic Equation by Factoring

#### Question

What is the sum of solutions of the equation $x^2 \log_2 (x+1) - x \log_2 (x+1) - 2 \log_2 (x+1) = 0?$

#### Explanation

First, we factor the equation:

$$


\begin{aligned}𝑥^{2}log_{2}⁡(𝑥+1)−𝑥log_{2}⁡(𝑥+1)−2log_{2}⁡(𝑥+1) & =0 \\ (𝑥^{2}−𝑥−2)log_{2}⁡(𝑥+1) & =0\end{aligned}


$$

We can now apply the zero product property, which states that $ab=0$ if and only if $a=0$ or $b=0.$ This gives us two equations,

$$


x^2 - x - 2 = 0 \quad \text{and} \quad \log_2 (x+1) =0.


$$

We now solve each of these equations separately.

- The equation $x^2- x-2 = 0$ can be factored as which gives the solutions $x=-1,2.$

- The equation $\log_2 (x+1) =0$ can be solved as follows:

So we have three candidate solutions, $x=-1, 0, 2.$ However, we need to check whether these solutions are in the domain of the logarithm in the original equation.

The original equation contains the logarithm $\log_2 (x+1),$ and its domain is $(-1, \infty).$

- The candidate $x=-1$ does not lie in the domain, so we discard it.

- The candidates $x=0,2$ lie in the domain, so we keep them.

Therefore, the original equation has two solutions $x=0, 2.$ The sum of these solutions is $0+2=2.$

### Example: Solving a Logarithmic Equation by Rearranging the Equation and Then Factoring

#### Question

What is the sum of solutions of the equation $3x^2 \log_3 (4x) = 12\log_3 (4x)?$

#### Explanation

First, we factor the equation:

$$


\begin{aligned}3𝑥^{2}log_{3}⁡(4𝑥) & =12log_{3}⁡(4𝑥) \\ 3𝑥^{2}log_{3}⁡(4𝑥)−12log_{3}⁡(4𝑥) & =0 \\ (3𝑥^{2}−12)log_{3}⁡(4𝑥) & =0\end{aligned}


$$

We can now apply the zero product property, which states that $ab=0$ if and only if $a=0$ or $b=0.$ This gives us two equations,

$$


3x^2 -12 = 0 \quad \text{and} \quad \log_3 (4x) =0.


$$

We now solve each of these equations separately.

- The equation $3x^2 -12=0$ can be factored as which gives the solutions $x=-2,2.$

- The equation $\log_3 (4x) = 0$ can be solved as follows:

So we have three candidate solutions, $x=-2,\frac{1}{4},2.$ However, we need to check whether these solutions are in the domain of the logarithm in the original equation.

The original equation contains the logarithm $\log_3(4x),$ and its domain is $(0, \infty).$

- The candidate $x=-2$ lies outside the domain, so we discard it.

- The candidates $x=\dfrac{1}{4},2$ lie within the domain, so we accept them as solutions.

Therefore, the original equation has two solutions $x=\dfrac{1}{4},2.$ The sum of these solutions is $\dfrac{1}{4}+2=\dfrac{9}{4}.$
