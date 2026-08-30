# Solving First-Order ODEs by Substitution

Source: https://www.mathacademy.com/topics/3179?courseId=61
Topic ID: 3179

## Prerequisites

- [Integration by Substitution With Inverse Trigonometric Functions](../../../ap-courses/lessons/ap-calculus-ab/315-integration-by-substitution-with-inverse-trigonometric-functions.md)
- [Solving First-Order ODEs Using Separation of Variables](./466-solving-first-order-odes-using-separation-of-variables.md)
- [Using Integration by Parts to Calculate Integrals With Logarithms](../../../ap-courses/lessons/ap-calculus-bc/1140-using-integration-by-parts-to-calculate-integrals-with-logarithms.md)

## Lesson

### Introduction

Suppose we have a differential equation of the form

$$


y ' = f ( a x + b y ),


$$

where $a$ and $b$ are real constants. In this case, we can rewrite the equation as a separable differential equation using the substitution $z= ax+by.$ We then proceed to solve this separable equation.

To see how we apply this method, let's consider the following example:

$$


y' = (x+y)^2


$$

First, we make the substitution

$$


z = x+y.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = 1 + \,\dfrac{\text{d}y}{\text{d}x} \quad\Longrightarrow\quad \dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{d}z}{\text{d}x} - 1.


$$

Therefore, the original equation can be written in terms of $z$ as follows:

$$


\begin{aligned}\frac{d𝑧}{d𝑥}−1 & =𝑧^{2}\end{aligned}


$$

Expressing this equation in the form $z'(x) = g(z)$ gives

$$


\dfrac{\text{d}z}{\text{d}x} = z^2+ 1.


$$

Notice that this differential equation is separable. So, we separate the variables and integrate both sides with respect to $x\mathbin{:}$

$$


\begin{aligned}\frac{1}{𝑧^{2}+1}\,\frac{d𝑧}{d𝑥} & =1 \\ ∫\frac{1}{𝑧^{2}+1}\,d𝑧 & =∫\,d𝑥 \\ arctan⁡𝑧 & =𝑥+𝐶\end{aligned}


$$

Finally, we write the general solution to the equation in terms of $x$ using our original substitution, as follows:

$$


\arctan {(x+y)} = x + C


$$

### Example: Reducing a First-Order ODE to a Simpler Form Using a Linear Substitution

#### Question

Consider the differential equation

$$


\dfrac{\text{d}y}{\text{d}x} = \ln(x + y).


$$

Using a substitution of the form $z= x + y,$ transform the differential equation into an equation of the form $z'(x) = f(z).$ What is the function $f(z)?$

#### Explanation

First, we make the substitution

$$


z = x + y.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = 1 + \dfrac{\text{d}y}{\text{d}x} \quad\Longrightarrow\quad \dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{d}z}{\text{d}x} - 1.


$$

Therefore, the original equation can be written in terms of $z$ as follows:

$$


\begin{aligned}\frac{d𝑧}{d𝑥}−1 & =ln⁡𝑧\end{aligned}


$$

Expressing this equation in the form $z'(x) = f(z),$ we get

$$


\dfrac{\text{d}z}{\text{d}x} = \ln z+1.


$$

Therefore, $f(z) = \ln z + 1.$

### Example: Solving a First-Order ODE Using a Linear Substitution

#### Question

Consider the differential equation

$$


\dfrac{\text{d}y}{\text{d}x} = x + y.


$$

The general solution to this equation can be expressed in the form

$$


g(x,y) = x+C,


$$

where $C$ is a constant. What is $g(x,y)?$

#### Explanation

First, we make the substitution

$$


z = x+y.


$$

Differentiating $z(x)$ using the chain rule, we get

$$


\dfrac{\text{d}z}{\text{d}x} = 1 + \,\dfrac{\text{d}y}{\text{d}x} \quad\Longrightarrow\quad \dfrac{\text{d}y}{\text{d}x} = \dfrac{\text{d}z}{\text{d}x} - 1.


$$

Therefore, the original equation can be written in terms of $z$ as follows:

$$


\begin{aligned}\frac{d𝑧}{d𝑥}−1 & =𝑧\end{aligned}


$$

Expressing this equation in the form $z'(x) = f(z)$ gives

$$


\dfrac{\text{d}z}{\text{d}x} = z+1.


$$

This differential equation is separable. So, we separate the variables and integrate both sides with respect to $x\mathbin{:}$

$$


\begin{aligned}\frac{1}{𝑧+1}\,\frac{d𝑧}{d𝑥} & =1 \\ ∫\frac{1}{𝑧+1}\,d𝑧 & =∫\,d𝑥 \\ ln⁡|𝑧+1| & =𝑥+𝐶\end{aligned}


$$

Finally, we write the equation in terms of $y$ and $x$ using our original substitution, as follows:

$$


\ln{|x+y+1|} = x + C


$$

Therefore, $g(x,y) = \ln{|x+y+1|}.$
