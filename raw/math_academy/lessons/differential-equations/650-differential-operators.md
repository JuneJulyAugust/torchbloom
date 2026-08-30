# Differential Operators

Source: https://www.mathacademy.com/topics/650?courseId=61
Topic ID: 650

## Prerequisites

- [Second and Higher-Order Derivatives](../ap-calculus-ab/281-second-and-higher-order-derivatives.md)
- [Selecting Procedures for Calculating Derivatives](../ap-calculus-ab/1115-selecting-procedures-for-calculating-derivatives.md)
- [Affine Transformations](../multivariable-calculus/3387-affine-transformations.md)

## Lesson

### Introduction

A differential operator $D$ is an operator that acts on a function $y(x)$ by forming an expression involving $y$ and one or more of its derivatives.

For example, consider the following differential operator.

$$


D(y)=\dfrac{\textrm d^{2}y}{\textrm d x^{2}}+2\dfrac{\textrm dy}{\textrm d x} + y


$$

This is a **second-order differential operator** because the highest derivative is of order $2.$

We can apply $D$ to any function $y(x)$ that's twice-differentiable. For example, let's apply the operator to $y(x) = \sin x.$ We substitute this function into the operator and calculate the derivatives:

$$


\begin{aligned}𝐷(sin⁡𝑥) & =\frac{d^{2}}{d𝑥^{2}}(sin⁡𝑥)+2\frac{d}{d𝑥}(sin⁡𝑥)+sin⁡𝑥 \\ & =\frac{d}{d𝑥}(cos⁡𝑥)+2cos⁡𝑥+sin⁡𝑥 \\ & =−sin⁡𝑥+2cos⁡𝑥+sin⁡𝑥 \\ & =2cos⁡𝑥.\end{aligned}


$$

We can think of our operator $D$ as a transformation that takes a *function* $y(x)$ as input and produces *another function* as output. In this example, the operator $D$ took the function $\sin x$ and mapped it to the function $2\cos x$:

$$


D: \sin x \longrightarrow 2\cos x


$$

It's helpful to draw a parallel with a **linear transformation** in vector spaces,

$$


T: \mathbf v \longrightarrow \mathbf w


$$

which takes a vector $\mathbf v$ as input and produces another vector $\mathbf w$ as output. The analogies between operators on function spaces and transformations on vector spaces will become clearer as we progress.

### Notation

In the last example, we defined a *second-order differential operator* as

$$


D(y)=\dfrac{\textrm d^{2}y}{\textrm d x^{2}}+2\dfrac{\textrm dy}{\textrm d x} + y.


$$

Under this notation, it is assumed that the function $y(x)$ is passed as input to the operator.

We sometimes prefer not to specify which function is being used as input. In that case, we may write the operator itself as

$$


D=\dfrac{\textrm d^{2}}{\textrm d x^{2}}+2\dfrac{\textrm d}{\textrm d x} + 1.


$$

Using this notation, we can apply the operator to any suitable function. So, if $f(x)$ is a twice-differentiable function, then

$$


\begin{aligned}𝐷(𝑓) & =(\frac{d^{2}}{d𝑥^{2}}+2\frac{d}{d𝑥}+1)𝑓 \\ & =\frac{d^{2}𝑓}{d𝑥^{2}}+2\frac{d𝑓}{d𝑥}+𝑓.\end{aligned}


$$

Think of this as *applying* the operator $D$ *to* the function $f.$

For the first part of this lesson, we'll restrict our attention to differential operators that are of the form

$$


D(y) = a_n\dfrac{\textrm d^{n}y}{\textrm d x^{n}} + a_{n-1}\dfrac{\textrm d^{n-1}y}{\textrm d x^{n-1}} + \cdots + a_{1}\dfrac{\textrm dy}{\textrm d x} + a_0y


$$

where $a_0, a_1, \ldots, a_n$ are all constants. We'll encounter more general forms later in the lesson.

### Example: Applying Differential Operators With Constant Coefficients

#### Question

Given that $D=\dfrac{\textrm d^{2}}{\textrm d x^{2}}+3 \dfrac{\textrm d}{\textrm d x}+5,$ what is $D(y)$ for $y=e^{- x}?$

#### Explanation

The given operator is a second-order differential operator of the form

$$


D(y) = a_{2}\dfrac{\textrm d^{2}y}{\textrm d x^{2}} + a_{1}\dfrac{\textrm dy}{\textrm d x} + a_0y


$$

with constant coefficients $a_2 = 1, a_1 = 3,$ and $a_0 = 5.$

To compute $D(y),$ we apply the definition of the operator $D$ to the function $y\mathbin{:}$

$$


\begin{aligned}𝐷(𝑦) & =𝐷(𝑒^{−𝑥}) \\ & =(\frac{d^{2}}{d𝑥^{2}}+3\frac{d}{d𝑥}+5)𝑒^{−𝑥} \\ & =\frac{d^{2}}{d𝑥^{2}}(𝑒^{−𝑥})+3\frac{d}{d𝑥}(𝑒^{−𝑥})+5𝑒^{−𝑥} \\ & =\frac{d}{d𝑥}(−𝑒^{−𝑥})+3⋅(−𝑒^{−𝑥})+5𝑒^{−𝑥} \\ & =𝑒^{−𝑥}−3𝑒^{−𝑥}+5𝑒^{−𝑥} \\ & =3𝑒^{−𝑥}\end{aligned}


$$

### More Complex Differential Operators

Differential operators can be quite complex, involving products of the function $y(x)$, its derivatives, and the independent variable $x$.

For example, consider the following **third-order differential operator**:

$$


D(y)=y^2\dfrac{\textrm d^{3}y}{\textrm d x^{3}} + x^2y\dfrac{\textrm dy}{\textrm d x} + xy


$$

Let's apply this operator to the function $y(x) = x^2$.

**Step 1:** Substitute $y=x^2$ into the operator expression.

$$


\begin{aligned}𝐷(𝑦) & =𝑦^{2}\frac{d^{3}𝑦}{d𝑥^{3}}+𝑥^{2}𝑦\frac{d𝑦}{d𝑥}+𝑥𝑦 \\ & =(𝑥^{2})^{2}\frac{d^{3}}{d𝑥^{3}}(𝑥^{2})+𝑥^{2}(𝑥^{2})\frac{d}{d𝑥}(𝑥^{2})+𝑥(𝑥^{2}) \\ & =𝑥^{4}\frac{d^{3}}{d𝑥^{3}}(𝑥^{2})+𝑥^{4}\frac{d}{d𝑥}(𝑥^{2})+𝑥^{3}\end{aligned}


$$

**Step 2:** Calculate the required derivatives step-by-step.

$$


\begin{aligned}𝐷(𝑦) & =𝑥^{4}\frac{d^{2}}{d𝑥^{2}}(2𝑥)+𝑥^{4}(2𝑥)+𝑥^{3} \\ & =𝑥^{4}\frac{d}{d𝑥}(2)+2𝑥^{5}+𝑥^{3} \\ & =𝑥^{4}⋅(0)+2𝑥^{5}+𝑥^{3} \\ & =2𝑥^{5}+𝑥^{3}\end{aligned}


$$

Next, we'll give the general definition of the $n$-th order differential operator and explain the difference between linear and non-linear differential operators.

### A General n-th Order Linear Differential Operator.

The properties of a differential operator depend on its structure. A key distinction is whether an operator is **linear** or **non-linear**.

A general **$n$-th order linear differential operator** has the form:

$$


L(y) = f_{n}(x)\dfrac{\textrm d^{n}y}{\textrm d x^{n}} + f_{n-1}(x)\dfrac{\textrm d^{n-1}y}{\textrm d x^{n-1}} + \cdots + f_{1}(x)\dfrac{\textrm dy}{\textrm d x} + f_0(x)y,


$$

where the coefficients are functions of the independent variable $x$ only.

For example, the operator

$$


D(y) = x y''' - y


$$

is a *linear operator*, since its coefficients ($x$ and $-1$) depend only on $x$.

In contrast, the operator from our previous example,

$$


D(y)=y^2 y''' + x^2y y' + xy,


$$

is *non-linear* because some of its coefficients depend on $y$. For instance, the coefficient of $y'''$ is $y^2$.

Other operators are non-linear because they involve powers of derivatives or other non-linear functions of $y$. For example,

$$


D(y) = \left(y' \right)^2 + y


$$

is non-linear due to the $(y')^2$ term.

For the rest of this topic, we will focus primarily on linear operators, as non-linear cases are typically more complex.

### Example: Applying Differential Operators With Functions of X as Coefficients

#### Question

Given that $D=x^2\dfrac{\textrm d^{3}}{\textrm d x^{3}}-5x \dfrac{\textrm d^{2}}{\textrm d x^{2}} +9\dfrac{\textrm d}{\textrm d x},$ what is $D(y)$ for $y=\ln{x}?$

#### Explanation

The given operator is a third-order differential operator of the form

$$


D(y) = f_{3}(x)\dfrac{\textrm d^{3}y}{\textrm d x^{3}} + f_{2}(x)\dfrac{\textrm d^{2}y}{\textrm d x^{2}} + f_{1}(x)\dfrac{\textrm dy}{\textrm d x} + f_0(x)y.


$$

with $f_3 = x^2, f_2 = -5x, f_1 = 9,$ and $f_0 = 0.$

To compute $D(y),$ we apply the definition of the operator $D$ to the function $y\mathbin{:}$

$$


\begin{aligned}𝐷(𝑦) & =𝐷(ln⁡𝑥) \\ & =(𝑥^{2}\frac{d^{3}}{d𝑥^{3}}−5𝑥\frac{d^{2}}{d𝑥^{2}}+9\frac{d}{d𝑥})ln⁡𝑥 \\ & =𝑥^{2}\frac{d^{3}}{d𝑥^{3}}(ln⁡𝑥)−5𝑥\frac{d^{2}}{d𝑥^{2}}(ln⁡𝑥)+9\frac{d}{d𝑥}(ln⁡𝑥) \\ & =𝑥^{2}\frac{d^{2}}{d𝑥^{2}}(\frac{1}{𝑥})−5𝑥\frac{d}{d𝑥}(\frac{1}{𝑥})+9⋅(\frac{1}{𝑥}) \\ & =𝑥^{2}\frac{d}{d𝑥}(−\frac{1}{𝑥^{2}})−5𝑥(−\frac{1}{𝑥^{2}})+\frac{9}{𝑥} \\ & =𝑥^{2}(\frac{2}{𝑥^{3}})+\frac{5}{𝑥}+\frac{9}{𝑥} \\ & =\frac{2}{𝑥}+\frac{5}{𝑥}+\frac{9}{𝑥} \\ & =\frac{16}{𝑥}\end{aligned}


$$

### Example: Applying Differential Operators With Multivariable Functions as Coefficients

#### Question

If $D(y)=y\dfrac{\textrm d^{3}y}{\textrm d x^{3}} - \dfrac{\textrm d y}{\textrm d x} + y^3,$ then calculate $D(e^{3x}).$

#### Explanation

The given operator is a third-order differential operator of the form

$$


D(y) = f_{3}(x,y)\dfrac{\textrm d^{3}y}{\textrm d x^{3}} + f_{2}(x,y)\dfrac{\textrm d^{2}y}{\textrm d x^{2}} + f_{1}(x,y)\dfrac{\textrm dy}{\textrm d x} + f_0(x,y)y


$$

with $f_3 = y, f_2 = 0, f_1 = -1,$ and $f_0 = y^2.$

To compute $D(y),$ we apply the definition of the operator $D$ to the function $y = e^{3x}{:}$

$$


\begin{aligned}𝐷(𝑒^{𝑥}) & =𝑒^{3𝑥}\frac{d^{3}}{d𝑥^{3}}(𝑒^{3𝑥})−\frac{d}{d𝑥}(𝑒^{3𝑥})+(𝑒^{3𝑥})^{3} \\ & =𝑒^{3𝑥}\frac{d^{2}}{d𝑥^{2}}(3𝑒^{3𝑥})−3⋅𝑒^{3𝑥}+𝑒^{9𝑥} \\ & =𝑒^{3𝑥}\frac{d}{d𝑥}(9𝑒^{3𝑥})−3⋅𝑒^{3𝑥}+𝑒^{9𝑥} \\ & =27𝑒^{6𝑥}−3⋅𝑒^{3𝑥}+𝑒^{9𝑥} \\ & =𝑒^{3𝑥}(𝑒^{6𝑥}+27𝑒^{3𝑥}−3)\end{aligned}


$$
