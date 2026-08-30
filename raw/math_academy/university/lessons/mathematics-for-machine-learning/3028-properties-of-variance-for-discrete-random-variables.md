# Properties of Variance for Discrete Random Variables

Source: https://www.mathacademy.com/topics/3028?courseId=145
Topic ID: 3028

## Prerequisites

- [Variance of Discrete Random Variables](./1388-variance-of-discrete-random-variables.md)

## Lesson

### Introduction

There are several important properties of the variance of a random variable that we can use to simplify expressions.

Firstly, the variance of a constant is always zero. That is, for any constant $a,$ we have

$$


\text{Var}[a] = 0.


$$

Intuitively, this makes sense. A constant does not vary, so the mean deviation from its expected value should be zero.

### Example: Computing the Variance of a Constant

#### Question

Calculate $\text{Var}[4k^2-1]$ where $k$ is a constant.

#### Explanation

Recall that for any constant $a,$ we have

$$


\text{Var}[a] = 0.


$$

Therefore, since $k$ is a constant, $4k^2-1$ is also a constant, and we have

$$


\text{Var}[4k^2-1] = 0.


$$

### The Variance of a Scaled Random Variable

Suppose that $X$ is a random variable and $a$ is a constant. Then,

$$


\text{Var}[aX] = a^2\text{Var}[X].


$$

So, for example, if we know that $\text{Var}[X] = 2,$ then

$$


\begin{aligned}Var[3𝑋] & =3^{2}⋅Var[𝑋] \\ & =9⋅Var[𝑋] \\ & =9⋅2 \\ & =18.\end{aligned}


$$

Similarly,

$$


\begin{aligned}Var[−4𝑋] & =(−4)^{2}⋅Var[𝑋] \\ & =16⋅Var[𝑋] \\ & =16⋅2 \\ & =32.\end{aligned}


$$

**Note:** To understand why we have to square the constant when we factor it outside the variance, it's helpful to remember that the variance is defined as the expected *squared* deviation from the mean:

$$


\text{Var}[X] = \textrm E [ (X - \textrm E[X])^2 ]


$$

So, we have

$$


\begin{aligned}Var[𝑎𝑋] & =E[(𝑎𝑋−E[𝑎𝑋])^{2}] \\ & =E[(𝑎𝑋−𝑎E[𝑋])^{2}] \\ & =E[𝑎^{2}(𝑋−E[𝑋])^{2}] \\ & =𝑎^{2}E[(𝑋−E[𝑋])^{2}] \\ & =𝑎^{2}Var[𝑋].\end{aligned}


$$

### Example: Computing the Variance of a Scaled Random Variable

#### Question

The probability distribution of the random variable $X$ is given below. Given that $\textrm E[X] = 2.3,$ calculate $\text{Var}[-10X].$

#### Explanation

Recall that for any random variable $X$ and constant $a,$ we have

$$


\text{Var}[aX] = a^2\cdot\text{Var}[X].


$$

In our case, $a=-10.$ Therefore,

$$


\begin{aligned}Var[−10𝑋] & =(−10)^{2}⋅Var[𝑋] \\ & =100⋅Var[𝑋].\end{aligned}


$$

We can compute the variance of $X$ using the following formula:

$$


\text{Var}[X] = \textrm E[X^2] - \textrm E[X]^2


$$

Additionally, we're given that $\textrm E [X] =2.3.$

We start by computing $\textrm E[X^2].$ Summing up the products of each value of $X^2$ and its associated probability, we get

$$


\begin{aligned}E[𝑋^{2}] & =1^{2}⋅𝑓(1)+2^{2}⋅𝑓(2)+3^{2}⋅𝑓(3) \\ & =1(0.2)+4(0.3)+9(0.5) \\ & =5.9.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =5.9−(2.3)^{2} \\ & =0.61.\end{aligned}


$$

Finally,

$$


\begin{aligned}Var[−10𝑋] & =100⋅Var[𝑋] \\ & =100⋅0.61 \\ & =61.\end{aligned}


$$

### The Variance of a Transformed Random Variable

Suppose that $X$ is a random variable and $a$ and $b$ are constants. It can be shown that

$$


\text{Var}[aX+b] = a^2\text{Var}[X].


$$

A proof of this result is given at the end of this lesson.

Therefore, when a random variable is scaled by a factor of $a$ and shifted by a constant $b\mathbin{:}$

- the variance is scaled by a factor of $a^2$ as before, and

- the variance is unaffected by the shift.

The fact that shifting a random variable leaves the variance unaltered makes intuitive sense. Shifting all values of $X$ by a fixed amount does not change how far apart those values are from each other.

For example, if we know that $\text{Var}[X] = 3,$ then

$$


\begin{aligned}Var[2𝑋+1] & =2^{2}⋅Var[𝑋] \\ & =2^{2}⋅3 \\ & =4⋅3 \\ & =12.\end{aligned}


$$

### Example: Computing the Variance of a Transformed Random Variable

#### Question

If $\text{Var}[X] = 10,$ calculate $\text{Var}[1-2X].$

#### Explanation

Recall that for any random variable $X$ and constants $a$ and $b,$ we have

$$


\text{Var}[aX+b] = a^2\cdot\text{Var}[X].


$$

In our case, $a=-2$ and $b=1.$ Therefore,

$$


\begin{aligned}Var[1−2𝑋] & =(−2)^{2}⋅Var[𝑋] \\ & =4⋅10 \\ & =40.\end{aligned}


$$

### Proof of the General Formula

We wish to prove the following result:

$$


\text{Var}[aX+b] = a^2\text{Var}[X]


$$

Recall that, by definition,

$$


\text{Var}[X] = \textrm E [ (X - \textrm E[X])^2 ].


$$

Therefore,

$$


\begin{aligned}Var[𝑎𝑋+𝑏] & =E[(𝑎𝑋+𝑏−E[𝑎𝑋+𝑏])^{2}].\end{aligned}


$$

Using the properties of expected value, we can simplify this as follows:

$$


\begin{aligned}E[(𝑎𝑋+𝑏−E[𝑎𝑋+𝑏])^{2}] & =E[(𝑎𝑋+𝑏−𝑎E[𝑋]−𝑏)^{2}] \\ & =E[(𝑎𝑋−𝑎E[𝑋])^{2}] \\ & =E[(𝑎(𝑋−E[𝑋]))^{2}] \\ & =E[𝑎^{2}(𝑋−E[𝑋])^{2}] \\ & =𝑎^{2}E[(𝑋−E[𝑋])^{2}] \\ & =𝑎^{2}Var[𝑋]\end{aligned}


$$
