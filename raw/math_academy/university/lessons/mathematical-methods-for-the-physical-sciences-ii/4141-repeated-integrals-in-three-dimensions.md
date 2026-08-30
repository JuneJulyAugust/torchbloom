# Repeated Integrals in Three Dimensions

Source: https://www.mathacademy.com/topics/4141?courseId=155
Topic ID: 4141

## Prerequisites

- [Type I, II, and III Regions in Three-Dimensional Space](./2130-type-i-ii-and-iii-regions-in-three-dimensional-space.md)
- [Double Integrals Over Type II Regions](../mathematical-methods-for-the-physical-sciences-i/2152-double-integrals-over-type-ii-regions.md)

## Lesson

### Introduction

Repeated integrals can feature three or more variables. In this lesson, we'll learn how to evaluate repeated integrals containing three variables.

For example, let's consider the repeated integral below:

$$


\int_{1}^2 \int_0^2 \int_0^1 x(y+z)^2 \:\textrm{d}z\:\textrm{d}y\:\textrm{d}x


$$

To evaluate this integral, we first integrate with respect to the inner variable $(z),$ then with respect to the middle variable $(y),$ and finally with respect to the outer variable $(x).$

We can write the first step more explicitly as

$$


\%\int_{1}^2 \int_0^2 \int_0^1 x(y+z)^2 \:\textrm{d}z\:\textrm{d}y\:\textrm{d}x= \int_{1}^2 \int_0^2 \left[ \int_0^1 x(y+z)^2 \:\textrm{d}z\right] \textrm{d}y\:\textrm{d}x. \%= \int_{1}^2 \left[ \int_0^2 \left[ \int_0^1 x(y+z)^2 \:\textrm{d}z \right] \textrm{d}y \right] \textrm{d}x.


$$

We now carry out the integration. First, we integrate the inner integral by integrating with respect to $z,$ *treating $x$ and $y$ as constants:*

$$


\begin{aligned}∫_{21}^{}∫_{20}^{}[∫_{10}^{}𝑥(𝑦+𝑧)^{2}\,d𝑧]d𝑦\,d𝑥 & =∫_{21}^{}∫_{20}^{}𝑥[\frac{(𝑦+𝑧)^{3}}{3}]_{𝑧=1𝑧=0}^{}\,d𝑦\,d𝑥 \\ & =∫_{21}^{}∫_{20}^{}𝑥(\frac{(𝑦+1)^{3}}{3}−\frac{𝑦^{3}}{3})d𝑦\,d𝑥 \\ & =∫_{21}^{}∫_{20}^{}\frac{1}{3}𝑥((𝑦+1)^{3}−𝑦^{3})d𝑦\,d𝑥 \\ & =\frac{1}{3}∫_{21}^{}∫_{20}^{}𝑥((𝑦+1)^{3}−𝑦^{3})d𝑦\,d𝑥\end{aligned}


$$

The next step is to integrate with respect to $y,$ which we can write more explicitly as

$$


\dfrac13 \int_{1}^2 \left[ \int_0^2x \left( (y+1)^3 - y^3 \right) \textrm{d}y \right] \textrm{d}x.


$$

Evaluating the inner integral by integrating with respect to $y,$ *treating $x$ as a constant,* we get

$$


\begin{aligned}\frac{1}{3}∫_{21}^{}[∫_{20}^{}𝑥((𝑦+1)^{3}−𝑦^{3})d𝑦]d𝑥 & =\frac{1}{3}∫_{21}^{}𝑥[(\frac{(𝑦+1)^{4}}{4}−\frac{𝑦^{4}}{4})]_{𝑦=2𝑦=0}^{}\,d𝑥 \\ & =\frac{1}{3}∫_{21}^{}𝑥[(\frac{81}{4}−\frac{16}{4})−(\frac{1}{4}−0)]d𝑥 \\ & =\frac{1}{3}∫_{21}^{}𝑥⋅(\frac{64}{4})\,d𝑥 \\ & =\frac{1}{3}∫_{21}^{}16𝑥\,d𝑥.\end{aligned}


$$

Finally, we integrate with respect to $x{:}$

$$


\begin{aligned}\frac{1}{3}∫_{21}^{}16𝑥\,d𝑥 & =\frac{1}{3}[8𝑥^{2}]_{𝑥=2𝑥=1}^{} \\ & =\frac{1}{3}(32−8) \\ & =\frac{1}{3}⋅24 \\ & =8\end{aligned}


$$

Therefore, we conclude that

$$


\int_{1}^2 \int_0^2 \int_0^1 x(y+z)^2 \:\textrm{d}z\:\textrm{d}y\:\textrm{d}x = 8.


$$

### Example: Evaluating Repeated Integrals

#### Question

Evaluate $\displaystyle \int_{1}^{2} \int_{-1}^{2} \int_{0}^{1} x^2y+xz^2 \: \mathrm{d}z \: \mathrm{d}x \: \mathrm{d}y.$

#### Explanation

First, we evaluate the inner integral by integrating with respect to $z$, treating $x$ and $y$ as constants:

$$


\begin{aligned}∫_{21}^{}∫_{2−1}^{}∫_{10}^{}𝑥^{2}𝑦+𝑥𝑧^{2}\,d𝑧\,d𝑥\,d𝑦 & =∫_{21}^{}∫_{2−1}^{}[∫_{10}^{}𝑥^{2}𝑦+𝑥𝑧^{2}\,d𝑧]d𝑥\,d𝑦 \\ & =∫_{21}^{}∫_{2−1}^{}[𝑥^{2}𝑦𝑧+\frac{𝑥𝑧^{3}}{3}]_{𝑧=1𝑧=0}^{}\,d𝑥\,d𝑦 \\ & =∫_{21}^{}∫_{2−1}^{}𝑥^{2}𝑦(1−0)+𝑥(\frac{1}{3}−0)\,d𝑥\,d𝑦 \\ & =∫_{21}^{}∫_{2−1}^{}𝑥^{2}𝑦+\frac{1}{3}𝑥\,d𝑥\,d𝑦\end{aligned}


$$

Next, we evaluate the inner integral by integrating with respect to $x$, treating $y$ as a constant:

$$


\begin{aligned}∫_{21}^{}∫_{2−1}^{}𝑥^{2}𝑦+\frac{1}{3}𝑥\,d𝑥\,d𝑦 & =∫_{21}^{}[∫_{2−1}^{}𝑥^{2}𝑦+\frac{1}{3}𝑥\,d𝑥]d𝑦 \\ & =∫_{21}^{}[\frac{1}{3}𝑥^{3}𝑦+\frac{1}{6}𝑥^{2}]_{𝑥=2𝑥=−1}^{}\,d𝑦 \\ & =∫_{21}^{}\frac{1}{3}𝑦(2^{3}−(−1)^{3})+\frac{1}{6}(2^{2}−(−1)^{2}))\,d𝑦 \\ & =∫_{21}^{}3𝑦+\frac{1}{2}\,d𝑦\end{aligned}


$$

Finally, we integrate with respect to $y{:}$

$$


\begin{aligned}∫_{21}^{}3𝑦+\frac{1}{2}\,d𝑥 & =[\frac{3𝑦^{2}}{2}+\frac{𝑦}{2}]_{𝑦=2𝑦=1}^{} \\ & =(6+1)−(\frac{3}{2}+\frac{1}{2}) \\ & =5\end{aligned}


$$

### Example: Evaluating Repeated Integrals Over Non-Rectangular Domains

#### Question

Evaluate $\displaystyle \int_{0}^{2} \int_{0}^{x} \int_{0}^{3-x-y} x \: \mathrm{d}z \: \mathrm{d}y \: \mathrm{d}x.$

#### Explanation

First, we evaluate the inner integral by integrating with respect to $z,$ treating $x$ and $y$ as constants:

$$


\begin{aligned}∫_{20}^{}∫_{𝑥0}^{}∫_{3−𝑥−𝑦0}^{}𝑥\,d𝑧\,d𝑦\,d𝑥 & =∫_{20}^{}∫_{𝑥0}^{}[∫_{3−𝑥−𝑦0}^{}𝑥\,d𝑧]d𝑦\,d𝑥 \\ & =∫_{20}^{}∫_{𝑥0}^{}𝑥⋅[𝑧]_{𝑧=3−𝑥−𝑦𝑧=0}^{}\,d𝑦\,d𝑥 \\ & =∫_{20}^{}∫_{𝑥0}^{}𝑥(3−𝑥−𝑦)\,d𝑦\,d𝑥 \\ & =∫_{20}^{}∫_{𝑥0}^{}3𝑥−𝑥^{2}−𝑥𝑦\,d𝑦\,d𝑥\end{aligned}


$$

Next, we evaluate the inner integral by integrating with respect to $y,$ treating $x$ as a constant:

$$


\begin{aligned}∫_{20}^{}∫_{𝑥0}^{}3𝑥−𝑥^{2}−𝑥𝑦\,d𝑦\,d𝑥 & =∫_{20}^{}[∫_{𝑥0}^{}3𝑥−𝑥^{2}−𝑥𝑦\,d𝑦]d𝑥 \\ & =∫_{20}^{}[(3𝑥−𝑥^{2})𝑦−\frac{1}{2}𝑥𝑦^{2}]_{𝑦=𝑥𝑦=0}^{}\,d𝑥 \\ & =∫_{20}^{}(3𝑥−𝑥^{2})(𝑥−0)−\frac{1}{2}𝑥(𝑥^{2}−0)\,d𝑥 \\ & =∫_{20}^{}3𝑥^{2}−𝑥^{3}−\frac{1}{2}𝑥^{3}\,d𝑥 \\ & =∫_{20}^{}3𝑥^{2}−\frac{3}{2}𝑥^{3}\,d𝑥\end{aligned}


$$

Finally, we integrate with respect to $x{:}$

$$


\begin{aligned}∫_{20}^{}3𝑥^{2}−\frac{3}{2}𝑥^{3}\,d𝑥 & =[𝑥^{3}−\frac{3}{8}𝑥^{4}]_{𝑥=2𝑥=0}^{} \\ & =8−6 \\ & =2\end{aligned}


$$

### Properties of Repeated Integrals

Repeated integrals with multiple variables obey similar rules to those we've seen before.

**The Sum Rule**

Suppose that $f(x,y,z)$ and $g(x,y,z)$ are continuous functions on a domain

$$


R = \big\{ (x,y,z) \: | \: a \leq x \leq b, \:\: \alpha(x) \leq y \leq \beta(x), \:\: \gamma(x,y) \leq z \leq \psi(x,y) \big\}.


$$

Then, we can write the integral

$$


\displaystyle \int_{a}^{b} \int_{\alpha(x)}^{\beta(x)} \int_{\gamma(x,y)}^{\psi(x,y)} f(x,y,z) + g(x,y,z) \:\textrm{d}z\:\textrm{d}y\:\textrm{d}x


$$

as

$$


\int_{a}^{b} \int_{\alpha(x)}^{\beta(x)} \int_{\gamma(x,y)}^{\psi(x,y)} f(x,y,z) \:\textrm{d}z\:\textrm{d}y\:\textrm{d}x + \int_{a}^{b} \int_{\alpha(x)}^{\beta(x)} \int_{\gamma(x,y)}^{\psi(x,y)} g(x,y,z) \:\textrm{d}z\:\textrm{d}y\:\textrm{d}x.


$$

**The Multiplicative Property**

Suppose that $f(x)$ is continuous on $[a,b],$ $g(y)$ is continuous on $[\alpha,\beta],$ and $h(z)$ is continuous on $[\gamma,\psi].$ Then, we have

$$


\int_{a}^{b} \int_{\alpha}^{\beta} \int_{\gamma}^{\psi} f(x) \cdot g(y) \cdot h(z) \:\textrm{d}z\:\textrm{d}y\:\textrm{d}x = \left( \int_{a}^{b} f(x) \:\textrm{d}x \right) \left( \int_{\alpha}^{\beta} g(y) \:\textrm{d}y \right) \left( \int_{\gamma}^{\psi} h(z) \:\textrm{d}z \right).


$$

### Using the Properties of Repeated Integrals

Let's evaluate the following repeated integral using the rules we just discussed.

$$


\displaystyle \int_{-1}^{1} \int_{0}^{1} \int_{0}^{2} (x+y+z) \: \textrm{d}x \: \textrm{d}y \: \textrm{d}z


$$

First, we apply the sum rule:

$$


\int_{-1}^{1} \int_{0}^{1} \int_{0}^{2} x \: \textrm{d}x \: \textrm{d}y \: \textrm{d}z + \int_{-1}^{1} \int_{0}^{1} \int_{0}^{2} y \: \textrm{d}x \: \textrm{d}y \: \textrm{d}z + \int_{-1}^{1} \int_{0}^{1} \int_{0}^{2} z \: \textrm{d}x \: \textrm{d}y \: \textrm{d}z


$$

Now, notice that the domain of integration $R = [0,2] \times [0,1] \times [-1,1]$ is a rectangular box, and each integrand can be expressed as $f(x) \cdot g(y) \cdot h(z).$ So, we can rewrite our sum of repeated integrals as follows:

$$


\int_{0}^{2} x \, \textrm{d}x \int_{0}^{1} \textrm{d}y \int_{-1}^{1} \textrm{d}z + \int_{0}^{2} \textrm{d}x \int_{0}^{1} y \, \textrm{d}y \int_{-1}^{1} \textrm{d}z + \int_{0}^{2} \textrm{d}x \int_{0}^{1} \textrm{d}y \int_{-1}^{1} z \, \textrm{d}z


$$

Let's evaluate each of these separately:

- For the first product, we have

- For the second product, we have

- For the third product, we have

Therefore, we conclude that

$$


\begin{aligned}∫_{1−1}^{}∫_{10}^{}∫_{20}^{}(𝑥+𝑦+𝑧)\,d𝑥\,d𝑦\,d𝑧=4+2+0=6\end{aligned}


$$

### Example: Evaluating Repeated Integrals Using the Sum and Product Rules

#### Question

Evaluate $\displaystyle \int_{1}^{2}\int_{0}^{\pi/2} \int_{1}^{4} \dfrac{\sin{y}}{x} \: \textrm{d}z \: \textrm{d}y \: \textrm{d}x.$

#### Explanation

Since the domain of integration $R = [1,2] \times \left[0,\pi/2\right] \times [1,4]$ is a rectangular box and the integrand can be expressed as $f(x)\cdot g(y)\cdot h(z),$ we can rewrite our repeated integral as follows:

$$


\begin{aligned}∫_{21}^{}∫_{𝜋/20}^{}∫_{41}^{}\frac{sin⁡𝑦}{𝑥}\,d𝑧\,d𝑦\,d𝑥 & =∫_{21}^{}\frac{d𝑥}{𝑥}∫_{𝜋/20}^{}sin⁡𝑦\,d𝑦∫_{41}^{}d𝑧\end{aligned}


$$

Evaluating each integral separately, we get

$$


\begin{aligned}∫_{21}^{}\frac{1}{𝑥}\,d𝑥∫_{𝜋/20}^{}sin⁡𝑦\,d𝑦\,∫_{41}^{}d𝑧 & =[ln⁡|𝑥|]_{21}^{}⋅[−cos⁡𝑦]_{𝜋/20}^{}⋅(4−1) \\ & =(ln⁡2−ln⁡1)⋅(−cos⁡(\frac{𝜋}{2})+cos⁡(0))⋅3 \\ & =(ln⁡2−0)⋅(0+1)⋅3 \\ & =3ln⁡2.\end{aligned}


$$

Therefore, we conclude that

$$


\int_{1}^{2}\int_{0}^{\pi/2} \int_{1}^{4} \dfrac{\sin{y}}{x} \: \textrm{d}z \: \textrm{d}y \: \textrm{d}x = 3\ln 2.


$$
