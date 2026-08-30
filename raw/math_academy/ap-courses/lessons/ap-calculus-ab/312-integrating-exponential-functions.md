# Integrating Exponential Functions

Source: https://www.mathacademy.com/topics/312?courseId=24
Topic ID: 312

## Prerequisites

- [Integrating the Reciprocal Function](./1361-integrating-the-reciprocal-function.md)

## Lesson

### Introduction

Remember that the exponential function $e^x$ has the special property that the derivative of the exponential function is the exponential function itself. In other words, taking the derivative doesn't change anything, and we have

$$


\frac{\textrm{d}}{\textrm d x} \left(e^ x\right) = e^ x.


$$

Since integration is the opposite of differentiation, and differentiating the exponential function leaves it unchanged, integrating the exponential function also leaves it unchanged. So, the integral of the exponential function is

$$


\displaystyle \int e^x \, \textrm d x = e^x +C.


$$

### Example: Integrating the Exponential Function

#### Question

Calculate $\displaystyle \int 6e^x \textrm d x.$

#### Explanation

Factoring out the constant $6$ and taking the integral, we get

$$


\begin{aligned} \int 6e^x \textrm d x =6 \int e^x \, \textrm d x =6e^x +C. \end{aligned}


$$

### Integrating an Exponential Function With a General Base

Remember that if $a$ is a positive real number, then the derivative of $a^x$ is given by

$$


\frac{\textrm{d}}{\textrm d x}\left( a^ x\right) = a^ x \ln a.


$$

So, by "reversing" this process, we obtain the following formula for the integral of a general exponential function:

$$


\displaystyle \int a^x \, \textrm d x = \dfrac{a^ x }{\ln a} +C.


$$

For instance, suppose that we wish to calculate the integral

$$


\int 2^x \, \textrm d x


$$

To compute the integral of a general exponential function, we just need to divide by the natural logarithm of the base of the exponential function:

$$


\begin{aligned} \int 2^x \, \textrm d x &= \dfrac{2^x}{\ln 2} + C \end{aligned}


$$

### Example: Integrating an Exponential Function With a General Base

#### Question

Calculate $\displaystyle \int -6(7^x) \, \textrm d x.$

#### Explanation

First, we factor out the constant $-6.$ Then, we integrate the exponential function, and get

$$


\begin{aligned} \int (-6)7^x \, \textrm d x &= -6\int 7^x\,\textrm{d}x\\&=-6 \cdot \dfrac{7^x}{\ln 7} + C. \end{aligned}


$$

### Example: Integrating a Sum of Exponential Functions

#### Question

Calculate $\displaystyle \int 5 \cdot 9^x +3 e^x \, \textrm d x.$

#### Explanation

Here, we combine the sum rule and our exponential rules to get

$$


\begin{aligned} \displaystyle \int 5 \cdot 9^x +3 e^x \, \textrm d x &= \displaystyle 5\int 9^x \, \textrm{d}x+ 3 \displaystyle \int e^x \, \textrm{d}x\\&= 5\cdot \dfrac{9^x}{\ln 9} + 3 e^x +C. \end{aligned}


$$
