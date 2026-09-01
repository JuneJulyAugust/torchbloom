# Line Integrals of Vector-Valued Functions Over General Curves

Source: https://www.mathacademy.com/topics/3711?courseId=54
Topic ID: 3711

## Prerequisites

- [Line Integrals of Vector-Valued Functions Over Parametric Curves](./2108-line-integrals-of-vector-valued-functions-over-parametric-curves.md)
- [Simple, Closed, and Oriented Curves](./3356-simple-closed-and-oriented-curves.md)
- [Line Integrals of Scalar Functions Over Paths Expressed as Functions of Y](./3689-line-integrals-of-scalar-functions-over-paths-expressed-as-functions-of-y.md)
- [Line Integrals of Scalar Functions Over Ellipses](./3690-line-integrals-of-scalar-functions-over-ellipses.md)
- [Line Integrals of Scalar Functions Over Line Segments](./3699-line-integrals-of-scalar-functions-over-line-segments.md)

## Lesson

### Introduction

The line integral of a vector-valued function $\mathbf F$ along a piecewise smooth curve $C$ is denoted

$$


\int\limits_C \mathbf F \cdot \textrm d\mathbf r .


$$

This integral represents the total work done by $\mathbf F$ in moving a particle from an initial point $A$ to a terminal point $B$ along the curve.

If the curve can be parameterized by the function $\mathbf r(t)$ for $t\in [a,b],$ then we can calculate the line integral using the following formula:

$$


\int\limits_C \mathbf F \cdot \textrm d\mathbf r= \int_a^b \mathbf F(\mathbf r(t)) \cdot \mathbf r'(t)\,\textrm dt


$$

Often, the trickiest part is finding a parameterization for $C.$ In this lesson, we'll consider several different cases

### Example: Line Integrals Over Line Segments

#### Question

Evaluate $\displaystyle \int\limits_{C} \mathbf{F} \cdot \text{d}\mathbf{r},$ where $\mathbf F(x, y) =(1-y)^2\,\mathbf{i} + x\,\mathbf{j}$ and $C$ is the line segment traversed from the point $A(0, 2)$ to the point $B(1,0).$

#### Explanation

We will use the formula

$$


\int\limits_C \mathbf{F} \cdot \text{d}\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) \,\text{d}t.


$$

First, we need to parameterize the line segment. The position vectors of the endpoints of our line segment are $\mathbf{a} = 2\mathbf{j}$ and $\mathbf{b} = \mathbf{i}.$ So, the parametrization of the line segment is given by

$$


\begin{aligned}𝐫(𝑡) & =𝐚+𝑡(𝐛−𝐚) \\ & =2𝐣+𝑡[𝐢−2𝐣] \\ & =𝑡\,𝐢+(2−2𝑡)\,𝐣,\end{aligned}


$$

where $t$ varies from $t=0$ (at the point $A$) to $t = 1$ (at the point $B$). Thus, along the curve $C,$ we have

$$


x = t, \qquad y = 2-2t.


$$

As a result,

$$


\begin{aligned}𝐅(𝐫(𝑡)) & =(1−𝑦)^{2}\,𝐢+𝑥\,𝐣 \\ & =(1−(2−2𝑡))^{2}\,𝐢+𝑡\,𝐣 \\ & =(2𝑡−1)^{2}\,𝐢+𝑡\,𝐣 \\ & =(4𝑡^{2}−4𝑡+1)\,𝐢+𝑡\,𝐣.\end{aligned}


$$

Computing $\mathbf{r}'(t),$ we get

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d𝑥}{d𝑡}\,𝐢+\frac{d𝑦}{d𝑡}\,𝐣 \\ & =\frac{d}{d𝑡}(𝑡)𝐢+\frac{d}{d𝑡}(2−2𝑡)𝐣 \\ & =𝐢−2𝐣.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝐅(𝐫(𝑡))⋅𝐫^{′}(𝑡) & =((4𝑡^{2}−4𝑡+1)\,𝐢+𝑡\,𝐣)⋅(𝐢−2𝐣) \\ & =(4𝑡^{2}−4𝑡+1)⋅(1)+(𝑡)⋅(−2) \\ & =4𝑡^{2}−6𝑡+1.\end{aligned}


$$

Finally, we evaluate the integral, as follows:

$$


\begin{aligned}\underset{𝐶}{∫}𝐅⋅d𝐫 & =∫_{10}𝐅(𝐫(𝑡))⋅𝐫^{′}(𝑡)\,d𝑡 \\ & =∫_{10}4𝑡^{2}−6𝑡+1\,d𝑡 \\ & =(\frac{4}{3}𝑡^{3}−3𝑡^{2}+𝑡)_{10} \\ & =(\frac{4}{3}−3+1)−0 \\ & =−\frac{2}{3}\end{aligned}


$$

### Example: Line Integrals Over Cartesian Curves

#### Question

Evaluate $\displaystyle \int\limits_{C} \mathbf{F} \cdot \text{d}\mathbf{r},$ where $\mathbf F(x, y) = y\,\mathbf{i} + x\,\mathbf{j}$ and $C$ is the curve $y^3 = x-5$ traversed from the point $A(5,0)$ to the point $B(6,1).$

#### Explanation

We will use the formula

$$


\int\limits_C \mathbf{F} \cdot \text{d}\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) \,\text{d}t.


$$

First, we need to parameterize the curve. Making $x$ the subject of the equation, we have

$$


y^3 = x-5 \qquad \Longrightarrow \qquad x = y^3 + 5.


$$

So, we can parametrize the curve using

$$


\begin{aligned}𝐫(𝑡) & =(𝑡^{3}+5)\,𝐢+𝑡\,𝐣,\,0≤𝑡≤1.\end{aligned}


$$

Thus, along the curve $C,$ we have

$$


x = t^3+5, \qquad y = t.


$$

As a result,

$$


\begin{aligned}𝐅(𝐫(𝑡)) & =𝑦\,𝐢+𝑥\,𝐣 \\ & =𝑡\,𝐢+(𝑡^{3}+5)\,𝐣.\end{aligned}


$$

Computing $\mathbf{r}'(t),$ we get

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d𝑥}{d𝑡}\,𝐢+\frac{d𝑦}{d𝑡}\,𝐣 \\ & =\frac{d}{d𝑡}(𝑡^{3}+5)𝐢+\frac{d}{d𝑡}(𝑡)𝐣 \\ & =3𝑡^{2}\,𝐢+𝐣.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝐅(𝐫(𝑡))⋅𝐫^{′}(𝑡) & =(𝑡\,𝐢+(𝑡^{3}+5)\,𝐣)⋅(3𝑡^{2}\,𝐢+𝐣) \\ & =𝑡⋅3𝑡^{2}+(𝑡^{3}+5)⋅1 \\ & =3𝑡^{3}+𝑡^{3}+5 \\ & =4𝑡^{3}+5.\end{aligned}


$$

Finally, we evaluate the integral, as follows:

$$


\begin{aligned}\underset{𝐶}{∫}𝐅⋅d𝐫 & =∫_{10}𝐅(𝐫(𝑡))⋅𝐫^{′}(𝑡)\,d𝑡 \\ & =∫_{10}4𝑡^{3}+5\,d𝑡 \\ & =[𝑡^{4}+5𝑡]_{10} \\ & =1+5−0 \\ & =6\end{aligned}


$$

### Example: Line Integrals Over Circles and Ellipses

#### Question

Evaluate $\displaystyle \oint\limits_{C} \mathbf{F}(\mathbf{r}) \cdot \text{d}\mathbf{r},$ where $\mathbf F(x, y) = y\,\mathbf{i} + x\,\mathbf{j}$ and $C$ is a circle of radius $1$ centered at the origin, traversed once in the counterclockwise direction.

#### Explanation

The notation $\displaystyle\oint$ is used to remind us that we're dealing with a line integral over a ** curve.

We will use the formula

$$


\oint\limits_C \mathbf{F} \cdot \text{d}\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t)) \cdot \mathbf{r}'(t) \,\text{d}t.


$$

First, we need to parameterize a circle of radius $1$ centered at the origin. It can be parameterized as

$$


\mathbf{r}(t) = \cos{t}\,\mathbf{i} + \sin{t}\,\mathbf{j}, \qquad 0 \leq t \lt 2\pi.


$$

So, along the curve $C,$ we have

$$


x = \cos{t}, \qquad y = \sin{t}.


$$

As a result,

$$


\begin{aligned}𝐅(𝐫(𝑡)) & =𝑦\,𝐢+𝑥\,𝐣=sin⁡𝑡\,𝐢+cos⁡𝑡\,𝐣.\end{aligned}


$$

Computing $\mathbf{r}'(t),$ we get

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d𝑥}{d𝑡}\,𝐢+\frac{d𝑦}{d𝑡}\,𝐣 \\ & =\frac{d}{d𝑡}(cos⁡𝑡)𝐢+\frac{d}{d𝑡}(sin⁡𝑡)𝐣 \\ & =−sin⁡𝑡\,𝐢+cos⁡𝑡\,𝐣.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝐅(𝐫(𝑡))⋅𝐫^{′}(𝑡) & =(sin⁡𝑡\,𝐢+cos⁡𝑡\,𝐣)⋅(−sin⁡𝑡\,𝐢+cos⁡𝑡\,𝐣) \\ & =−sin^{2}⁡𝑡+cos^{2}⁡𝑡 \\ & =−(1−cos^{2}⁡𝑡)+cos^{2}⁡𝑡 \\ & =2cos^{2}⁡𝑡−1 \\ & =cos⁡2𝑡.\end{aligned}


$$

Finally, we can evaluate the integral, as follows:

$$


\begin{aligned}\underset{𝐶}{∮}𝐅(𝐫)⋅d𝐫 & =∫_{2𝜋0}𝐅(𝐫(𝑡))⋅𝐫^{′}(𝑡)\,d𝑡 \\ & =∫_{2𝜋0}cos⁡2𝑡\,d𝑡 \\ & =[\frac{1}{2}sin⁡2𝑡]_{2𝜋0} \\ & =\frac{1}{2}sin⁡4𝜋−\frac{1}{2}sin⁡(0) \\ & =0.\end{aligned}


$$
