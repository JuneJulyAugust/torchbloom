# Line Integrals of Scalar Functions Over Polar Curves

Source: https://www.mathacademy.com/topics/2638?courseId=54
Topic ID: 2638

## Prerequisites

- [Further Properties of Line Integrals of Scalar Functions](./3354-further-properties-of-line-integrals-of-scalar-functions.md)

## Lesson

### Introduction

Suppose that we want to evaluate the line integral with respect to arc length

$$


\int\limits_Cf(x,y)\:\text{d}s


$$

for some function $f(x,y),$ where $C$ is a curve in the $xy$-plane defined using plane polar coordinates as

$$


r = r(\theta),\qquad \theta_1 \leq \theta \leq \theta_2.


$$

To calculate this line integral, we need to recall the following facts:

- A polar curve is just a special type of parametric curve in the parameter $\theta,$ where

- The arc length element $\textrm d s$ in plane polar coordinates is given by

Substituting the above formulas into our line integral, we get the following result:

$$


\int\limits_C f(x,y) \, \text{d}s = \int_{\theta_1}^{\theta_2} f(r\cos\theta,r\sin\theta) \,\sqrt{r^2 + \left(\dfrac{\textrm d r}{\textrm d \theta}\right)^2}\,\textrm d \theta\,.


$$

Let's go through an example in which we apply this result.

### Example: Reducing the Line Integral of a Scalar Function Along a Curve to a Definite Integral

#### Question

Find a definite integral with respect to $\theta$ that is equivalent to $\displaystyle \int \limits_{C} (y^2-x) \, \textrm ds,$ where $C$ is the section of the polar curve $r = \cos{\theta}\:$ for $0 \le \theta \le\dfrac{\pi}4.$

#### Explanation

In polar coordinates, the formula for the line integral is given by

$$


\int\limits_C f(x,y) \, \text{d}s = \int_{\theta_1}^{\theta_2} f(r\cos\theta,r\sin\theta) \,\sqrt{r^2 + \left(\dfrac{\textrm d r}{\textrm d \theta}\right)^2}\,\textrm d \theta\,.


$$

The connection between polar and Cartesian coordinates gives

$$


\begin{aligned}𝑥 & =𝑟cos⁡𝜃 \\ & =cos⁡𝜃⋅cos⁡𝜃 \\ & =cos^{2}⁡𝜃, \\ 𝑦 & =𝑟sin⁡𝜃 \\ & =cos⁡𝜃⋅sin⁡𝜃 \\ & =cos⁡𝜃sin⁡𝜃.\end{aligned}


$$

So, along our curve, we have $x=\cos^2\theta$ and $y=\cos\theta \sin{\theta}$, where $0 \leq \theta \leq \dfrac{\pi}4.$

Now, if $f(x,y) =y^2-x$, we obtain

$$


\begin{aligned}𝑓(𝑟cos⁡𝜃,𝑟sin⁡𝜃) & =(cos⁡𝜃sin⁡𝜃)^{2}−cos^{2}⁡𝜃 \\ & =cos^{2}⁡𝜃 sin^{2}⁡𝜃−cos^{2}⁡𝜃 \\ & =cos^{2}⁡𝜃(sin^{2}⁡𝜃−1) \\ & =cos^{2}⁡𝜃(−cos^{2}⁡𝜃) \\ & =−cos^{4}⁡𝜃.\end{aligned}


$$

Next, we have

$$


\begin{aligned}\frac{d𝑟}{d𝜃} & =\frac{d}{d𝜃}(cos⁡𝜃)=−sin⁡𝜃,\end{aligned}


$$

and therefore

$$


\begin{aligned}\sqrt{𝑟^{2}+(\frac{d𝑟}{d𝜃})^{2}}\,d𝜃 & =\sqrt{(cos⁡𝜃)^{2}+(−sin⁡𝜃)^{2}} \\ & =\sqrt{cos^{2}⁡𝜃+sin^{2}⁡𝜃} \\ & =\sqrt{1} \\ & =1.\end{aligned}


$$

Finally, we can write the integral as

$$


\begin{aligned}\underset{𝐶}{∫}(𝑦^{2}−𝑥)\,d𝑠 & =∫_{𝜋/40}𝑓(𝑟cos⁡𝜃,𝑟sin⁡𝜃)\,\sqrt{𝑟^{2}+(\frac{d𝑟}{d𝜃})^{2}}\,d𝜃 \\ & =∫_{𝜋/40}−cos^{4}⁡𝜃⋅1⋅d𝜃 \\ & =−∫_{𝜋/40}cos^{4}⁡𝜃\,d𝜃.\end{aligned}


$$

### Example: Finding the Line Integral of a Scalar Function Along a Curve Given in Polar Form

#### Question

Evaluate the integral of the function $f(x,y)=\dfrac{x^2+y^2}{y^2}$ along the polar curve $r=1$ for $\dfrac{\pi}{6}\leq \theta \leq \dfrac\pi 2.$

#### Explanation

In polar coordinates, the formula for the line integral is given by

$$


\int\limits_C f(x,y) \, \text{d}s = \int_{\theta_1}^{\theta_2} f(r\cos\theta,r\sin\theta) \,\sqrt{r^2 + \left(\dfrac{\textrm d r}{\textrm d \theta}\right)^2}\,\textrm d \theta\,.


$$

The connection between polar and Cartesian coordinates gives

$$


\begin{aligned}𝑥 & =𝑟cos⁡𝜃=cos⁡𝜃, \\ 𝑦 & =𝑟sin⁡𝜃=sin⁡𝜃.\end{aligned}


$$

So, along our curve, we have $x=\cos\theta$ and $y=\sin\theta$, where $\dfrac{\pi}{6} \leq \theta \leq \dfrac{\pi}2.$

Now, since $f(x,y) = \dfrac{x^2+y^2}{y^2}$, we obtain

$$


\begin{aligned}𝑓(𝑟cos⁡𝜃,𝑟sin⁡𝜃) & =\frac{cos^{2}⁡𝜃+sin^{2}⁡𝜃}{sin^{2}⁡𝜃} \\ & =\frac{1}{sin^{2}⁡𝜃} \\ & =csc^{2}⁡𝜃.\end{aligned}


$$

Next, we have

$$


\begin{aligned}\frac{d𝑟}{d𝜃} & =\frac{d}{d𝜃}(1)=0,\end{aligned}


$$

and therefore

$$


\begin{aligned}\sqrt{𝑟^{2}+(\frac{d𝑟}{d𝜃})^{2}}\,d𝜃=\sqrt{1^{2}+0^{2}}=1.\end{aligned}


$$

Finally, we now evaluate the integral, as follows:

$$


\begin{aligned}\underset{𝐶}{∫}\frac{𝑥^{2}+𝑦^{2}}{𝑦^{2}}\,d𝑠 & =∫_{𝜋/2𝜋/6}𝑓(𝑟cos⁡𝜃,𝑟sin⁡𝜃)\,\sqrt{𝑟^{2}+(\frac{d𝑟}{d𝜃})^{2}}\,d𝜃 \\ & =∫_{𝜋/2𝜋/6}csc^{2}⁡𝜃⋅1⋅d𝜃 \\ & =∫_{𝜋/2𝜋/6}csc^{2}⁡𝜃\,d𝜃 \\ & =−cot⁡𝜃\,_{𝜋/2𝜋/6} \\ & =−(0−\sqrt{3}) \\ & =\sqrt{3}\end{aligned}


$$

### Example: Finding the Line Integral of a Scalar Function Along a Curve Using Substitution

#### Question

Evaluate the integral $\displaystyle\int\limits_{C} xy(1-x^2) \,\text{d}s$, where $C$ is the polar curve $r=\cos{\theta}\:$ for $0 \leq \theta \leq \dfrac{\pi}{2}.$

#### Explanation

In polar coordinates, the formula for the line integral is given by

$$


\int\limits_C f(x,y) \, \text{d}s = \int_{\theta_1}^{\theta_2} f(r\cos\theta,r\sin\theta) \,\sqrt{r^2 + \left(\dfrac{\textrm d r}{\textrm d \theta}\right)^2}\,\textrm d \theta\,.


$$

The connection between polar and Cartesian coordinates gives

$$


\begin{aligned}𝑥 & =𝑟cos⁡𝜃 \\ & =cos⁡𝜃⋅cos⁡𝜃 \\ & =cos^{2}⁡𝜃, \\ 𝑦 & =𝑟sin⁡𝜃 \\ & =cos⁡𝜃⋅sin⁡𝜃 \\ & =cos⁡𝜃sin⁡𝜃.\end{aligned}


$$

So, along our curve, we have $x=\cos^2\theta$ and $y=\cos\theta\sin\theta$, where $0 \leq \theta \leq \dfrac{\pi}{2}.$

Now, if $f(x,y) = xy(1-x^2)$, we obtain

$$


\begin{aligned}𝑓(𝑟cos⁡𝜃,𝑟sin⁡𝜃) & =cos^{2}⁡𝜃⋅cos⁡𝜃sin⁡𝜃(1−(cos^{2}⁡𝜃)^{2}) \\ & =cos^{3}⁡𝜃sin⁡𝜃(1−cos^{4}⁡𝜃).\end{aligned}


$$

Next, we have

$$


\begin{aligned}\frac{d𝑟}{d𝜃}=\frac{d}{d𝜃}(cos⁡𝜃)=−sin⁡𝜃\end{aligned}


$$

and therefore

$$


\begin{aligned}\sqrt{𝑟^{2}+(\frac{d𝑟}{d𝜃})^{2}}\,d𝜃 & =\sqrt{(cos⁡𝜃)^{2}+(−sin⁡𝜃)^{2}} \\ & =\sqrt{cos^{2}⁡𝜃+sin^{2}⁡𝜃} \\ & =1.\end{aligned}


$$

We can now write the integral as

$$


\begin{aligned}\underset{𝐶}{∫}𝑥𝑦(1−𝑥^{2})\,d𝑠 & =∫_{𝜋/20}𝑓(𝑟cos⁡𝜃,𝑟sin⁡𝜃)\,\sqrt{𝑟^{2}+(\frac{d𝑟}{d𝜃})^{2}}\,d𝜃 \\ & =∫_{𝜋/20}cos^{3}⁡𝜃sin⁡𝜃(1−cos^{4}⁡𝜃)⋅1⋅d𝜃 \\ & =∫_{𝜋/20}cos^{3}⁡𝜃sin⁡𝜃(1−cos^{4}⁡𝜃)\,d𝜃.\end{aligned}


$$

We can solve this using the substitution $u=\cos\theta,$ $\textrm d u=-\sin\theta\,\textrm d \theta$ as follows:

$$


\begin{aligned}∫_{𝜋/20}cos^{3}⁡𝜃sin⁡𝜃(1−cos^{4}⁡𝜃)\,d𝜃 & =∫_{01}−𝑢^{3}(1−𝑢^{4})\,d𝑢 \\ & =∫_{10}(𝑢^{3}−𝑢^{7})\,d𝑢 \\ & =[\frac{𝑢^{4}}{4}−\frac{𝑢^{8}}{8}]_{10} \\ & =(\frac{1}{4}−\frac{1}{8})−0 \\ & =\frac{1}{8}\end{aligned}


$$
