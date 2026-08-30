# Linear Differential Operators

Source: https://www.mathacademy.com/topics/6707?courseId=61
Topic ID: 6707

## Prerequisites

- [Differential Operators](./650-differential-operators.md)

## Lesson

### Introduction

Suppose that $D$ is an $n$th-order differential operator, and the functions $y, y_1,$ and $y_2$ are $n$-times differentiable in some domain of interest.

We say that a differential operator $D$ is **linear** if the following conditions hold:

1. $D(a y(x)) = a D(y(x)),$ where $a$ is a constant.

2. $D(y_1(x) + y_2(x)) = D(y_1(x)) + D(y_2(x)).$

We can combine these two conditions into a single condition as follows:

$$


D(ay_1(x) + by_2(x)) = aD(y_1(x)) + bD(y_2(x))


$$

where $a$ and $b$ are constants.

It's worth taking a moment to compare these conditions to those we used when defining a *linear transformation*

$$


\mathbf T: \mathbf v \rightarrow \mathbf w.


$$

For $\mathbf T$ to be linear, it must satisfy the following conditions:

- $\mathbf{T}(a\mathbf{v})=a\mathbf{T}(\mathbf{v})$ for any vector $\mathbf{v}$ and any scalar $a.$

- $\mathbf{T}(\mathbf{v}_1+\mathbf{v}_2)=\mathbf{T}(\mathbf{v}_1)+\mathbf{T}(\mathbf{v}_2)$ for any vectors $\mathbf{v}_1$ and $\mathbf{v}_2.$

The conditions are essentially the same in both cases! Only instead of a transformation $\mathbf T,$ we have a differential operator $D.$ And instead of vectors as our inputs and outputs, we have functions.

Next, we'll apply this definition to a specific differential operator to see if it is linear.

### The Linearity Condition

A differential operator $D$ is **linear** if the following linearity condition is satisfied.

$$


D(ay_1(x) + by_2(x)) = aD(y_1(x)) + bD(y_2(x))


$$

where $a$ and $b$ are constants.

Let's consider some examples:

- First, let's consider the following differential operator: This operator is indeed linear. To see this, we need to check that the linearity condition above holds. So we start by applying our operator to the function $y = a y_1(x) + b y_2(x){:}$ Since derivatives distribute over sums, and $a$ and $b$ are constants, we have Thus, since $D_1(ay_1 + by_2) = aD_1(y_1) + bD_1(y_2),$ the operator $D_1$ is linear.

- Now, let's consider the following differential operator: This operator is *not* linear. To see this, we need to check that the linearity condition above does not hold. So we start by applying our operator to the function $y = a y_1(x) + b y_2(x){:}$ Comparing this to $aD_2(y_1) + bD_2(y_2),$ we see that they are *not* the same: Therefore, the operator $D_2$ is *not* linear.

### Example: Using the Properties of Linear Differential Operators to Identify Them

#### Question

Show that the differential operator

$$


D(y) = y\dfrac{\textrm d^2 y}{\textrm d x^2} + \dfrac{\textrm d y}{\textrm d x}


$$

is nonlinear.

#### Explanation

For any linear differential operator $L,$ we have the linearity condition

$$


L(ay_1 + by_2) = aL(y_1) + bL(y_2)


$$

for functions $y_1(x), y_2(x),$ and where $a$ and $b$ are constants.

For the given differential operator, we have

$$


\begin{aligned}𝐷(𝑎𝑦_{1}+𝑏𝑦_{2}) & =(𝑎𝑦_{1}+𝑏𝑦_{2})\frac{d^{2}}{d𝑥^{2}}(𝑎𝑦_{1}+𝑏𝑦_{2})+\frac{d}{d𝑥}(𝑎𝑦_{1}+𝑏𝑦_{2}) \\ & =(𝑎𝑦_{1}+𝑏𝑦_{2})(𝑎\frac{d^{2}𝑦_{1}}{d𝑥^{2}}+𝑏\frac{d^{2}𝑦_{2}}{d𝑥^{2}})+𝑎\frac{d𝑦_{1}}{d𝑥}+𝑏\frac{d𝑦_{2}}{d𝑥} \\ & =+𝑎^{2}𝑦_{1}\frac{d^{2}𝑦_{1}}{d𝑥^{2}}+𝑎𝑏𝑦_{1}\frac{d^{2}𝑦_{2}}{d𝑥^{2}}+𝑎𝑏𝑦_{2}\frac{d^{2}𝑦_{1}}{d𝑥^{2}}+𝑏^{2}𝑦_{2}\frac{d^{2}𝑦_{2}}{d𝑥^{2}} \\ & =\,\,+𝑎\frac{d𝑦_{1}}{d𝑥}+𝑏\frac{d𝑦_{2}}{d𝑥} \\ & =𝑎^{2}𝑦_{1}\frac{d^{2}𝑦_{1}}{d𝑥^{2}}+𝑏^{2}𝑦_{2}\frac{d^{2}𝑦_{2}}{d𝑥^{2}}+𝑎\frac{d𝑦_{1}}{d𝑥}+𝑏\frac{d𝑦_{2}}{d𝑥} \\ & =\,\,+𝑎𝑏(𝑦_{1}\frac{d^{2}𝑦_{2}}{d𝑥^{2}}+𝑦_{2}\frac{d^{2}𝑦_{1}}{d𝑥^{2}}).\end{aligned}


$$

This is ** the same as the right-hand side, because

$$


\begin{aligned}𝑎𝐷(𝑦_{1})+𝑏𝐷(𝑦_{2}) & =𝑎[𝑦_{1}\frac{d^{2}𝑦_{1}}{d𝑥^{2}}+\frac{d𝑦_{1}}{d𝑥}]+𝑏[𝑦_{2}\frac{d^{2}𝑦_{2}}{d𝑥^{2}}+\frac{d𝑦_{2}}{d𝑥}] \\ & =𝑎𝑦_{1}\frac{d^{2}𝑦_{1}}{d𝑥^{2}}+𝑏𝑦_{2}\frac{d^{2}𝑦_{2}}{d𝑥^{2}}+𝑎\frac{d𝑦_{1}}{d𝑥}+𝑏\frac{d𝑦_{2}}{d𝑥}.\end{aligned}


$$

Therefore, since $D(ay_1+by_2) \neq aD(y_1) + bD(y_2),$ the operator $D$ is nonlinear.

### The General Form of a Linear Differential Operator

An **$n$th-order linear differential operator**, denoted $L$, has the general form:

$$


L(y) = f_{n}(x)\dfrac{\textrm d^{n}y}{\textrm d x^{n}} + f_{n-1}(x)\dfrac{\textrm d^{n-1}y}{\textrm d x^{n-1}} + \cdots + f_{1}(x)\dfrac{\textrm dy}{\textrm d x} + f_0(x)y.


$$

The functions $f_i(x)$ are called the **coefficient functions**. They must depend only on the variable $x$ and be continuous on the domain of interest. The **order** of the operator is the order of the highest derivative whose coefficient is not zero.

If all the coefficient functions $f_i(x)$ are constants, we call the operator a **linear operator with constant coefficients**.

Let's look at two examples:

1. The operator $L(y) = x^2 y'' - (\sin x) y' + 2y$ is a 2nd-order *linear differential operator*. Its coefficient functions are $f_2(x) = x^2$, $f_1(x) = -\sin x$, and $f_0(x) = 2$.

2. The operator $L(y) = 4y''' + 7y'' - y$ is a 3rd-order *linear operator with constant coefficients*. Its coefficient functions are $f_3(x) = 4$, $f_2(x) = 7$, $f_1(x) = 0$, and $f_0(x) = -1$.

### Example: Identifying Linear Differential Operators Using the General Form

#### Question

Which of the following are linear differential operators?

1. $D_1(y)=\dfrac{\textrm dy}{\textrm d x}+x\cos(y)\,y$

2. $D_2(y)=\dfrac{1}{1+x^2}\dfrac{\textrm d^{2}y}{\textrm d x^{2}}-\sin(x)\dfrac{\textrm dy}{\textrm d x}+3y$

3. $D_3(y)=\dfrac{\textrm d^{3}y}{\textrm d x^{3}}+e^{x}\dfrac{\textrm d^{2}y}{\textrm d x^{2}}-\ln(x)\,y$

#### Explanation

An $n$th-order differential operator $L$ is linear if it is of the following form:

$$


L(y) = f_{n}(x)\dfrac{\textrm d^{n}y}{\textrm d x^{n}} + f_{n-1}(x)\dfrac{\textrm d^{n-1}y}{\textrm d x^{n-1}} + \cdots + f_{1}(x)\dfrac{\textrm dy}{\textrm d x} + f_0(x)y


$$

where each $f_i$ is a function of $x$ only.

With that in mind, let's check each operator.

- Operator $D_1$ is ** linear. The coefficient of the second term is $x\cos(y),$ which depends on $y$ and therefore fails linearity.

- Operator $D_2$ is linear. It is a second-order linear differential operator of the form with $f_2(x) = \dfrac{1}{1+x^2}, f_1(x) = -\sin(x),$ and $f_0(x) = 3.$

- Operator $D_3$ is linear. It is a third-order linear differential operator of the form with $f_3(x) = 1, f_2(x) = e^{x}, f_1(x) = 0,$ and $f_0(x) = -\ln(x).$

Therefore, the correct answer is "II and III only."

### Example: Using Linearity Properties of Linear Differential Operators

#### Question

Suppose that $L$ is a linear differential operator such that $L(y_1) = \tan^2{x}$ and $L(y_2) =2 \sec^2{x}$ for some functions $y_1(x)$ and $y_2(x).$ What is $L(2y_1 -y_2)?$

**

#### Explanation

For any linear differential operator $L,$ we have

$$


L(ay_1(x) + by_2(x)) = aL(y_1(x)) + bL(y_2(x))


$$

where $a$ and $b$ are constants.

In our case, we have

$$


\begin{aligned}𝐿(2𝑦_{1}−𝑦_{2}) & =2𝐿(𝑦_{1})−𝐿(𝑦_{2}) \\ & =2tan^{2}⁡𝑥−2sec^{2}⁡𝑥.\end{aligned}


$$

Using the trigonometric identity $1+\tan^2 x = \sec^2 x,$ we can simplify this even further, as follows:

$$


\begin{aligned}𝐿(2𝑦_{1}−𝑦_{2}) & =2tan^{2}⁡𝑥−2(1+tan^{2}⁡𝑥) \\ & =−2.\end{aligned}


$$

Therefore,

$$


L(2y_1 -y_2)=-2.


$$
