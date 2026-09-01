# Sums of Line Integrals With Respect to X and Y Over Parametric Curves

Source: https://www.mathacademy.com/topics/3705?courseId=54
Topic ID: 3705

## Prerequisites

- [Line Integrals With Respect to X and Y](./2109-line-integrals-with-respect-to-x-and-y.md)

## Lesson

### Introduction

Line integrals with respect to $x$ and $y$ often come in pairs. For example,

$$


\int\limits_C (x+y) \, \textrm dx + \int\limits_C (x-y) \, \textrm dy.


$$

We usually express a sum of line integrals with respect to $x$ and $y$ as a single integral. In the case above, we can write this sum as

$$


\int\limits_C (x+y) \, \textrm dx + (x-y) \, \textrm dy.


$$

Let's evaluate this integral in this case where $C$ is given by the line segment

$$


\mathbf{r}(t)=\underbrace{(6t+1)}_{x(t)} \,\mathbf{i} + \underbrace{(2t+1)}_{y(t)} \,\mathbf{j}, \qquad t\in\left[0,1\right].


$$

Along the path $C,$ we have

$$


x = 6t+1, \qquad y = 2t+1.


$$

Computing the derivative of $\mathbf r(t),$ we get

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d𝑥}{d𝑡}\,𝐢+\frac{d𝑦}{d𝑡}\,𝐣 \\ & =\frac{d}{d𝑡}(6𝑡+1)\,𝐢+\frac{d}{d𝑡}(2𝑡+1)\,𝐣 \\ & =6\,𝐢+2\,𝐣.\end{aligned}


$$

Now, we evaluate the line integral by applying a change of variables, as follows:

$$


\begin{aligned}\underset{𝐶}{∫}(𝑥+𝑦)\,d𝑥+(𝑥−𝑦)\,d𝑦 & =∫_{10}(𝑥+𝑦)⋅\frac{d𝑥}{d𝑡}\,d𝑡+(𝑥−𝑦)⋅\frac{d𝑦}{d𝑡}\,d𝑡 \\ & =∫_{10}((𝑥+𝑦)⋅\frac{d𝑥}{d𝑡}+(𝑥−𝑦)⋅\frac{d𝑦}{d𝑡})d𝑡 \\ & =∫_{10}(6𝑡+1+2𝑡+1)⋅6+(6𝑡+1−(2𝑡+1))⋅2\,d𝑡 \\ & =∫_{10}(8𝑡+2)⋅6+(4𝑡)⋅2\,d𝑡 \\ & =∫_{10}48𝑡+12+8𝑡\,d𝑡 \\ & =∫_{10}56𝑡+12\,d𝑡 \\ & =28𝑡^{2}+12𝑡_{10} \\ & =28+12 \\ & =40.\end{aligned}


$$

### Example: Constructing a Sum of Line Integrals With Respect to X and Y

#### Question

Construct a definite integral that is equivalent to $\displaystyle \int\limits_C (x^2+y)\,\mathrm{d}x + x\,\mathrm{d}y,$ where $C$ is parametrized by $\mathbf{r}(t) = t\,\mathbf{i} + t^2\,\mathbf{j}$ for $t\in\left[0,1\right].$

#### Explanation

Along the curve, we have

$$


x(t) = t, \qquad y(t) = t^2.


$$

The derivative of $\mathbf r(t)$ is given by

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d𝑥}{d𝑡}\,𝐢+\frac{d𝑦}{d𝑡}\,𝐣 \\ & =\frac{d}{d𝑡}(𝑡)\,𝐢+\frac{d}{d𝑡}(𝑡^{2})\,𝐣 \\ & =𝐢+2𝑡\,𝐣.\end{aligned}


$$

Therefore, we can write our line integral as follows:

$$


\begin{aligned}\underset{𝐶}{∫}(𝑥^{2}+𝑦)\,d𝑥+𝑥\,d𝑦 & =∫_{10}(𝑥^{2}+𝑦)\frac{d𝑥}{d𝑡}\,d𝑡+𝑥\frac{d𝑦}{d𝑡}\,d𝑡 \\ & =∫_{10}((𝑥^{2}+𝑦)\frac{d𝑥}{d𝑡}+𝑥\frac{d𝑦}{d𝑡})\,d𝑡 \\ & =∫_{10}(𝑡^{2}+𝑡^{2})⋅1+𝑡⋅2𝑡\,d𝑡 \\ & =∫_{10}2𝑡^{2}+2𝑡^{2}\,d𝑡 \\ & =∫_{10}4𝑡^{2}\,d𝑡 \\ & =4∫_{10}𝑡^{2}\,d𝑡\end{aligned}


$$

### Line Integrals With Respect to X, Y, and Z

Let $f(x,y,z)$ be a function of three variables and $C$ be a path in three-dimensional space. Suppose we want to calculate the following sum of line integrals:

$$


\int\limits_C f \, \textrm dx + \int\limits_C f \, \textrm dy + \int\limits_C f \, \textrm dz


$$

For notational simplicity, we can express this as a single integral, as follows:

$$


\int\limits_C f \, \textrm dx + f \, \textrm dy + f \, \textrm dz


$$

As before, we can evaluate this integral by parameterizing the curve $C$ using the parameter $t\in [a,b]$ and then rewriting the integral using a change of variables, as follows:

$$


\begin{aligned}\underset{𝐶}{∫}𝑓\,d𝑥+𝑓\,d𝑦+𝑓\,d𝑧 & =∫_{𝑏𝑎}𝑓\frac{d𝑥}{d𝑡}\,d𝑡+𝑓\frac{d𝑦}{d𝑡}\,d𝑡+𝑓\frac{d𝑧}{d𝑡}\,d𝑡 \\ & =∫_{𝑏𝑎}(𝑓\frac{d𝑥}{d𝑡}+𝑓\frac{d𝑦}{d𝑡}+𝑓\frac{d𝑧}{d𝑡})\,d𝑡\end{aligned}


$$

Note that we often omit the large parentheses and simply write

$$


\int_a^b f\dfrac{\textrm d x}{\textrm d t} + f \dfrac{\textrm d y}{\textrm d t} + f \dfrac{\textrm d z}{\textrm d t} \,\textrm d t.


$$

Finally, it can be helpful to switch to prime notation for the derivatives when dealing with complex integrands. In this case, the above formula becomes

$$


\int_a^b f x'+ f y' + f z' \,\textrm d t,


$$

where the primes denote differentiation with respect to $t.$

### Example: Constructing a Sum of Line Integrals With Respect to X, Y, and Z

#### Question

Construct a definite integral that is equivalent to $\displaystyle \int\limits_C x^3\,\mathrm{d}x + z\,\mathrm{d}y + y\,\mathrm{d}z,$ where $C$ is a portion of the helix $\mathbf{r}(t)=2t\,\mathbf{i} + \cos t\,\mathbf{j} + \sin t\,\mathbf{k}$ for $t\in[0,\pi]?$

#### Explanation

Along the curve, we have

$$


x(t) =2t, \qquad y(t) = \cos t , \qquad z(t) = \sin t.


$$

The derivative of $\mathbf r(t)$ is given by

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d𝑥}{d𝑡}\,𝐢+\frac{d𝑦}{d𝑡}\,𝐣+\frac{d𝑧}{d𝑡}\,𝐤 \\ & =\frac{d}{d𝑡}(2𝑡)\,𝐢+\frac{d}{d𝑡}(cos⁡𝑡)\,𝐣+\frac{d}{d𝑡}(sin⁡𝑡)\,𝐤 \\ & =2\,𝐢−sin⁡𝑡\,𝐣+cos⁡𝑡\,𝐤.\end{aligned}


$$

Therefore, we can write our line integral as follows:

$$


\begin{aligned}\underset{𝐶}{∫}𝑥^{3}\,d𝑥+𝑧\,d𝑦+𝑦\,d𝑧 & =∫_{𝜋0}𝑥^{3}\frac{d𝑥}{d𝑡}\,d𝑡+𝑧\frac{d𝑦}{d𝑡}\,d𝑡+𝑦\frac{d𝑧}{d𝑡}\,d𝑡 \\ & =∫_{𝜋0}(𝑥^{3}\frac{d𝑥}{d𝑡}+𝑧\frac{d𝑦}{d𝑡}+𝑦\frac{d𝑧}{d𝑡})d𝑡 \\ & =∫_{𝜋0}(2𝑡)^{3}⋅(2)+sin⁡𝑡⋅(−sin⁡𝑡)+cos⁡𝑡⋅(cos⁡𝑡)\,d𝑡 \\ & =∫_{𝜋0}16𝑡^{3}−sin^{2}⁡𝑡+cos^{2}⁡𝑡\,d𝑡 \\ & =∫_{𝜋0}16𝑡^{3}+(cos^{2}⁡𝑡−sin^{2}⁡𝑡)\,d𝑡 \\ & =∫_{𝜋0}16𝑡^{3}+cos⁡2𝑡\,d𝑡\end{aligned}


$$

### Example: Evaluating a Line Integral

#### Question

Evaluate $\displaystyle \int\limits_C y\,\mathrm{d}x -x\,\mathrm{d}y,$ where $C$ is a portion of the ellipse parametrized by $\mathbf{r}(t)=\cos t\,\mathbf{i} + 3\sin t\,\mathbf{j}$ for $t\in[0,\pi].$

#### Explanation

Along the curve, we have

$$


x(t) = \cos t, \qquad y(t) = 3\sin t.


$$

The derivative of $\mathbf r(t)$ is given by

$$


\begin{aligned}𝐫^{′}(𝑡) & =\frac{d𝑥}{d𝑡}\,𝐢+\frac{d𝑦}{d𝑡}\,𝐣 \\ & =\frac{d}{d𝑡}(cos⁡𝑡)\,𝐢+\frac{d}{d𝑡}(3sin⁡𝑡)\,𝐣 \\ & =−sin⁡𝑡\,𝐢+3cos⁡𝑡\,𝐣.\end{aligned}


$$

We can now evaluate the line integral:

$$


\begin{aligned}\underset{𝐶}{∫}𝑦\,d𝑥−𝑥\,d𝑦 & =∫_{𝜋0}𝑦⋅\frac{d𝑥}{d𝑡}\,d𝑡−𝑥⋅\frac{d𝑦}{d𝑡}\,d𝑡 \\ & =∫_{𝜋0}(𝑦⋅\frac{d𝑥}{d𝑡}−𝑥⋅\frac{d𝑦}{d𝑡})\,d𝑡 \\ & =∫_{𝜋0}3sin⁡𝑡⋅(−sin⁡𝑡)−(cos⁡𝑡)⋅3cos⁡𝑡\,d𝑡 \\ & =∫_{𝜋0}−3sin^{2}⁡𝑡−3cos^{2}⁡𝑡\,d𝑡 \\ & =−3∫_{𝜋0}sin^{2}⁡𝑡+cos^{2}⁡𝑡\,d𝑡 \\ & =−3∫_{𝜋0}\,d𝑡 \\ & =−3𝑡|_{𝜋0} \\ & =−3𝜋\end{aligned}


$$
