# Triple Integrals Over Rectangular Domains

Source: https://www.mathacademy.com/topics/2052?courseId=155
Topic ID: 2052

## Prerequisites

- [Volumes of Rectangular Solids](../geometry/1753-volumes-of-rectangular-solids.md)
- [Repeated Integrals in Three Dimensions](./4141-repeated-integrals-in-three-dimensions.md)

## Lesson

### Introduction

Recall that the double integral of a continuous function $f(x,y)$ over a rectangular region $R = [a,b]\times[c,d],$ denoted

$$


\iint\limits_{R}{ f(x,y) \, \mathrm{d}A},


$$

represents the total *signed* volume bounded between the surface $z=f(x,y)$ and the planes $x=a, x=b, y=c,$ and $y=d.$

We can extend the concept of multiple integrals to functions of three variables.

Now, suppose that $f(x,y,z)$ is a continuous function of three variables defined over the rectangular domain $R\subset \mathbb R^3,$ given by

$$


R = [a,b] \times [c,d] \times [e,f].


$$

Then, the **triple integral** of $f(x,y,z)$ over $R,$ denoted

$$


\iiint\limits_{R}{ f(x,y,z) \, \mathrm{d}V},


$$

can be interpreted as a four-dimensional signed *hypervolume* bounded by the function $f$ and the *hyperplanes* $x=a,$ $x=b,$ $y=c,$ $y=d,$ $z=e,$ and $z=f$ in four-dimensional space.

Similar to the case of double integrals, it can be shown that the triple integral

$$


\iiint\limits_R f(x,y,z) \: \mathrm{d}V


$$

can be evaluated using the repeated integral

$$


\int_a^b\int_c^d\int_e^f f(x,y,z) \: \mathrm{d}z\,\textrm{d} y\,\textrm{d} x.


$$

Note that when the domain $R$ is rectangular, we can freely change the order of integration. For example, we can write

$$


\int_{\color{red}a}^{\color{red}b}\int_c^d\int_{\color{blue}e}^{\color{blue}f} f(x,y,z) \: \mathrm{d}{\color{blue}z}\,\textrm d y\,\textrm d {\color{red}x} = \int_{\color{blue}e}^{\color{blue}f}\int_c^d \int_{\color{red}a}^{\color{red}b} f(x,y,z) \: \textrm d {\color{red}x}\,\textrm d y\,\mathrm{d}{\color{blue}z}.


$$

There are six possible orders in which we can evaluate a triple integral using a repeated integral:

$$


\begin{aligned} & d𝑥\,d𝑦\,d𝑧 & \, & d𝑦\,d𝑥\,d𝑧 & \, & d𝑧\,d𝑥\,d𝑦 \\ & d𝑥\,d𝑧\,d𝑦 & \, & d𝑦\,d𝑧\,d𝑥 & \, & d𝑧\,d𝑦\,d𝑥\end{aligned}


$$

### A Worked Example

Let's evaluate the triple integral

$$


\iiint\limits_R x + y + z \:\textrm d V


$$

where the integration domain $R = [0,1] \times [0,2] \times [0,2].$

First, we write our triple integral as a repeated integral. Let's integrate first with respect to $x,$ then $y,$ and then $z{:}$

$$


\int_0^2 \int_0^2 \int_0^1 x+ y +z \: \textrm{d}x\, \textrm{d}y\, \textrm{d}z


$$

Applying the sum rule, we get

$$


\begin{aligned}=∫_{20}^{}∫_{20}^{}∫_{10}^{}𝑥\,d𝑥\,d𝑦\,d𝑧+∫_{20}^{}∫_{20}^{}∫_{10}^{}𝑦\,d𝑥\,d𝑦\,d𝑧+∫_{20}^{}∫_{20}^{}∫_{10}^{}𝑧\,d𝑥\,d𝑦\,d𝑧.\end{aligned}


$$

Since $R$ is rectangular, we can apply the product rule, which gives

$$


\begin{aligned}∫_{10}^{}𝑥\,d𝑥∫_{20}^{}\,d𝑦\,∫_{20}^{}\,d𝑧+∫_{10}^{}\,d𝑥∫_{20}^{}𝑦\,d𝑦\,∫_{20}^{}\,d𝑧+∫_{10}^{}\,d𝑥∫_{20}^{}\,d𝑦\,∫_{20}^{}𝑧\,d𝑧.\end{aligned}


$$

Let's evaluate each of these separately:

- For the first product, we have

- For the second product, we have

- For the third product, we have

Therefore, we conclude that

$$


\iiint\limits_R x + y + z \:\textrm d V = 2+4+4 = 10.


$$

### Example: Writing a Triple Integral as a Repeated Integral

#### Question

Express the triple integral

$$


\displaystyle \iiint\limits_{R} (x+y+z)^2 \: \textrm{d}V


$$

over the box

$$


R = \bigg\{ (x,y,z) \: : \: 0 \leq x \leq 1, \: -1 \leq y \leq 2, \: 0\leq z \leq 2 \bigg\}


$$

as a repeated integral of the form

$$


\displaystyle \int_a^b \int_c^d \int_e^f \ldots \: \textrm{d}y\: \textrm{d}z\: \textrm{d}x .


$$

#### Explanation

Given the limits for $x,y,$ and $z,$ we can express our triple integral as a repeated integral as follows:

$$


\begin{aligned}\underset{𝑅}{∭}(𝑥+𝑦+𝑧)^{2}\,d𝑉 & =∫_{10}^{}∫_{20}^{}∫_{2−1}^{}(𝑥+𝑦+𝑧)^{2}\,\,d𝑦\,d𝑧\,d𝑥\end{aligned}


$$

### Example: Evaluating a Triple Integral Using the Product Rule

#### Question

Evaluate the triple integral

$$


\displaystyle \iiint\limits_{R} y \cos{x} \sin{z} \: \textrm{d}V


$$

over the box $R = \bigg\{(x,y,z) \:: \: 0 \leq x \leq \dfrac{\pi}{2}, \: 0 \leq y \leq 1, \: 0 \leq z \leq \pi \bigg\}.$

#### Explanation

First, we express our triple integral as a repeated integral:

$$


\begin{aligned}\underset{𝑅}{∭}𝑦cos⁡𝑥sin⁡𝑧\,d𝑉 & =∫_{𝜋0}^{}∫_{10}^{}∫_{𝜋/20}^{}𝑦cos⁡𝑥sin⁡𝑧\,d𝑥\,d𝑦\,d𝑧\end{aligned}


$$

Since the domain of integration $R = \left[0,\pi/2\right]\times[0,1]\times\left[0,\pi\right]$ is a rectangular box, and the integrand can be expressed as $f(x)\cdot g(y)\cdot h(z),$ we can rewrite our repeated integral as follows:

$$


\begin{aligned}∫_{𝜋/20}^{}cos⁡𝑥\,d𝑥\,∫_{10}^{}𝑦\,d𝑦\,∫_{𝜋0}^{}sin⁡𝑧\,d𝑧\end{aligned}


$$

Evaluating each integral separately, we get

$$


\begin{aligned}∫_{𝜋/20}^{}cos⁡𝑥\,d𝑥\,∫_{10}^{}𝑦\,d𝑦\,∫_{𝜋0}^{}sin⁡𝑧\,d𝑧 & =[sin⁡𝑥]_{𝜋/20}^{}⋅[\frac{𝑦^{2}}{2}]_{10}^{}⋅[−cos⁡𝑧]_{𝜋0}^{} \\ & =(1−0)⋅(\frac{1}{2}−0)⋅(1−(−1)) \\ & =1⋅\frac{1}{2}⋅2 \\ & =1.\end{aligned}


$$

### Example: Evaluating a Triple Integral

#### Question

By integrating first with respect to $z,$ then $x,$ and then $y,$ evaluate the triple integral

$$


\displaystyle \iiint\limits_R z-xy \: \mathrm{d}V


$$

over the rectangular box $R = \left\{(x,y,z) \:: \:0 \leq x \leq 2, \: -1 \leq y \leq 1, \: 1 \leq z \leq 3 \right\}.$

#### Explanation

First, we express our triple integral as a repeated integral:

$$


\displaystyle \iiint \limits_{R} z-xy \: \textrm{d}V = \int_{-1}^{1} \int_{0}^{2} \int_{1}^{3} z-xy \: \mathrm{d}z \: \mathrm{d}x \: \mathrm{d}y


$$

Since we're integrating first with respect to $z,$ then $x,$ and then $y,$ we write $\textrm d V = \textrm d z\:\textrm d x\:\textrm d y.$

First, we evaluate the inner integral with respect to $z,$ treating $x$ and $y$ as constants:

$$


\begin{aligned}∫_{1−1}^{}∫_{20}^{}∫_{31}^{}𝑧−𝑥𝑦\,d𝑧\,d𝑥\,d𝑦 & =∫_{1−1}^{}∫_{20}^{}[∫_{31}^{}𝑧−𝑥𝑦\,d𝑧]d𝑥\,d𝑦 \\ & =∫_{1−1}^{}∫_{20}^{}[\frac{1}{2}𝑧^{2}−𝑥𝑦𝑧]_{𝑧=3𝑧=1}^{}\,d𝑥\,d𝑦 \\ & =∫_{1−1}^{}∫_{20}^{}\frac{1}{2}(9−1)−𝑥𝑦(3−1)\,d𝑥\,d𝑦 \\ & =∫_{1−1}^{}∫_{20}^{}4−2𝑥𝑦\,d𝑥\,d𝑦\end{aligned}


$$

Next, we evaluate the inner integral with respect to $x,$ treating $y$ as a constant:

$$


\begin{aligned}∫_{1−1}^{}∫_{20}^{}4−2𝑥𝑦\,d𝑥\,d𝑦 & =∫_{1−1}^{}[∫_{20}^{}4−2𝑦𝑥\,d𝑥]d𝑦 \\ & =∫_{1−1}^{}[4𝑥−𝑦𝑥^{2}]_{𝑥=2𝑥=0}^{}\,d𝑦 \\ & =∫_{1−1}^{}4(2−0)−𝑦(2^{2}−0)\,d𝑦 \\ & =∫_{1−1}^{}8−4𝑦\,d𝑦\end{aligned}


$$

Finally, we integrate with respect to $y{:}$

$$


\begin{aligned}∫_{1−1}^{}8−4𝑦\,d𝑦 & =[8𝑦−2𝑦^{2}]_{𝑦=1𝑦=−1}^{} \\ & =8(1−(−1))−2(1^{2}−(−1)^{2}) \\ & =8⋅2−2(1−1) \\ & =16−0 \\ & =16\end{aligned}


$$
