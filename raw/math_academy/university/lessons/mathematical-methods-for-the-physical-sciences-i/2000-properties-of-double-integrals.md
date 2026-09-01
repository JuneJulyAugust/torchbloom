# Properties of Double Integrals

Source: https://www.mathacademy.com/topics/2000?courseId=154
Topic ID: 2000

## Prerequisites

- [Double Integrals Over Non-Rectangular Domains](./2616-double-integrals-over-non-rectangular-domains.md)

## Lesson

### Introduction

Double integrals have properties that are similar to the properties of definite integrals of single-variable functions:

- **Linearity of Double Integrals.** Suppose that $f(x,y)$ and $g(x,y)$ are continuous functions on a domain $D$ and that $\alpha, \beta$ are constants. Then, we have

- **The Double Integral of Unity.** The integral of $f(x,y) = 1$ over a domain $D$ is simply the area of $D\mathbin{:}$

Other properties are more specific to double integrals.

- **The Multiplicative Property of Double Integrals.** If $f(x)$ is continuous on $[a,b]$ and $g(y)$ is continuous on $[c,d]$ then where $R= [a,b] \times [c,d].$

### Example: Evaluating a Double Integral Using the Multiplicative Property

#### Question

Evaluate the double integral $\displaystyle \iint\limits_{R} xy\ \!e^{x+y}\ \textrm d A$ over the rectangle $R= [0,1] \times [1,2].$

#### Explanation

We apply the multiplicative property of double integrals and then evaluate each of the integrals separately:

$$


\begin{aligned} \iint\limits_{R} xy\\e^{x+y}\: \textrm d A &= \iint\limits_{R} \Big( x\\\! e^x \Big)\Big( y\\\! e^{y} \Big) \textrm d A\\[5pt] &= \left(\int_0^1x\\e^{x} \\\textrm d x\right)\left( \int_1^2 y \\\!e^{y} \\\textrm d y\right)\\[5pt] &= \Big[x\\\!e^x-e^x\Big]_0^1 \cdot \Big[y\\\!e^y-e^y\Big]_1^2\\[5pt] &= \Big(e^1-e^1 - \left(0-e^0\right)\Big) \cdot \Big(2e^2-e^2 - \left(e^1-e^1\right) \Big)\\[5pt] &= 1\cdot e^2\\[5pt] &= e^2 \end{aligned}


$$

### Applying the Multiplicative Property when the Integrand Contains Only One Variable

We can also apply the multiplicative property when the integrand contains only one of the variables.

For example, suppose that $R= [a,b] \times [c,d].$ Then, we have the general result

$$


\begin{aligned}\underset{𝑅}{∬}𝑓(𝑥)\,d𝐴 & =\underset{𝑅}{∬}(𝑓(𝑥))(1)\,d𝐴 \\ & =(∫_{𝑏𝑎}𝑓(𝑥)\,d𝑥)(∫_{𝑑𝑐}1\,d𝑦) \\ & =(∫_{𝑏𝑎}𝑓(𝑥)\,d𝑥)(𝑑−𝑐) \\ & =(𝑑−𝑐)∫_{𝑏𝑎}𝑓(𝑥)\,d𝑥.\end{aligned}


$$

By the same reasoning, we also have

$$


\iint\limits_{R} g(y) \, \text{d}A = (b-a) \int_c^d g(y) \, \text{d}y.


$$

### Example: Evaluating a Double Integral When the Integrand Contains Only One Variable

#### Question

Calculate $\displaystyle \iint\limits_{R} \left(x^2-y^2 +3\right) \textrm d A,$ where $R= [-1,3] \times [2, 4].$

#### Explanation

Using the linearity property of double integrals, we can write

$$


\begin{aligned}\underset{𝑅}{∬}(𝑥^{2}−𝑦^{2}+3) d𝐴 & =\underset{𝑅}{∬}𝑥^{2} d𝐴−\underset{𝑅}{∬}𝑦^{2} d𝐴+\underset{𝑅}{∬}3\,d𝐴.\end{aligned}


$$

Now, let's evaluate each of the three integrals.

- The function under the first integral is independent of $y.$ So, we have

- The function under the second integral is independent of $x.$ So, we have

- The function under the third integral is a constant, so we have

Finally, combining our results, we obtain

$$


\begin{aligned}\underset{𝑅}{∬}(𝑥^{2}−𝑦^{2}+3)\,d𝐴=\frac{56}{3}−\frac{224}{3}+24=−32.\end{aligned}


$$

### Additivity of Double Integrals

Remember that the definite integral of a single-variable function can be split up over adjacent subintervals. That is to say,

$$


\int_a^c f(x) \, \textrm dx = \int_a^b f(x) \, \textrm dx + \int_b^c f(x) \, \textrm dx.


$$

In the same way, the definite integral of a two-variable function can be split up over adjacent sub-domains.

Suppose that a domain $D$ is the union of two adjacent sub-domains $D_1$ and $D_2$ (meaning that $D_1$ and $D_2$ are non-overlapping regions that could share a common border). Then, we have

$$


\iint\limits_{D} f(x,y)\ \text{d}A = \iint\limits_{D_1} f(x,y)\ \text{d}A + \iint\limits_{D_2} f(x,y)\ \text{d}A.


$$

This property can be generalized if $D$ is split into a finite number $n$ of sub-domains (where $n>2$):

$$


\iint\limits_{D} f(x,y)\ \text{d}A = \iint\limits_{D_1} f(x,y)\ \text{d}A + \iint\limits_{D_2} f(x,y)\ \text{d}A + \cdots + \iint\limits_{D_n} f(x,y)\ \text{d}A


$$

### Example: Using Additivity of Double Integrals

#### Question

Given that $C$ and $D$ are finite, non-overlapping regions and that

$$


\iint\limits_{C} f(x,y)\ \text{d}A = 8, \qquad \iint\limits_{D} f(x,y)\ \text{d}A = -5,


$$

find the value of

$$


\iint\limits_{C \cup D} 3f(x,y)\ \text{d}A.


$$

#### Explanation

Using the linearity and additivity of double integrals, we get the following:

$$


\begin{aligned}\underset{𝐶∪𝐷}{∬}3𝑓(𝑥,𝑦) d𝐴 & =3\underset{𝐶∪𝐷}{∬}𝑓(𝑥,𝑦) d𝐴 \\ & =3(\underset{𝐶}{∬}𝑓(𝑥,𝑦) d𝐴+\underset{𝐷}{∬}𝑓(𝑥,𝑦) d𝐴) \\ & =3(8+(−5)) \\ & =3⋅3 \\ & =9\end{aligned}


$$

### Open and Closed Regions of Integration

Suppose that we're integrating a single-variable function over a region $R.$ The definite integral of $f(x)$ over $R$ is not affected by whether the region $R$ is open or closed.

For example, consider the function $f(x) = 1,$ and define the regions $R = [0,1]$ and $R' = (0,1).$ Integrating $f(x)$ over $R$ and $R'$ gives the same result:

$$


\int_R f(x) \,\textrm d x = \int_{R'} f(x) \,\textrm d x = \int_{0}^1 \,\textrm d x = 1


$$

Intuitively, this is true because the rectangles formed by $f(x),$ namely $[0, 1]\times [0,1]$ and $(0, 1)\times (0,1),$ have the same area.

We have a similar property for double integrals too. We can either include or exclude the boundaries of the integration regions without affecting the result.

For example, the double integral of $f(x,y)=x^2+y^2$ over both $R=[0,1] \times [0,1]$ and over $R'=(0,1) \times (0,1)$ will give the same result:

$$


\iint\limits_{\large R} (x^2+y^2) \ \text{d}A = \iint\limits_{\large R'} (x^2+y^2) \ \text{d}A= \int_{0}^{1} \int_{0}^{1} (x^2+y^2) \ \text{d}A


$$

Intuitively, this is true because the *volumes* of the shapes formed by $f(x,y)$ over the regions $R$ and $R'$ are the same.

Moreover, we'd get the same result if we were to integrate $f(x,y)$ over any of the following regions:

$$


(0,1] \times [0,1], \quad [0,1) \times [0,1], \quad (0,1) \times [0,1], \quad \ldots


$$

The same idea applies to double-integrals over non-rectangular boundaries, too.

### Example: Evaluating a Double Integral Using the Additivity Over a Rectangular Domain

#### Question

Evaluate the double integral $\displaystyle \iint\limits_{R} f(x,y)\ \textrm d A$, where

$$


\begin{aligned}2,\, & if\,0<𝑥<2,\,\,−1<𝑦<0 \\ \frac{1}{𝑥𝑦+𝑥+𝑦+1},\, & if\,0<𝑥<2,\,\,\,0<𝑦<1,\end{aligned}


$$

and $R$ is the domain of $f.$

#### Explanation

First, notice that we have $R = R_1 \cup R_2,$ where $R_1= (0,2) \times (-1,0)$ and $R_2= (0,2) \times (0,1).$ So, we can write

$$


\begin{aligned} \iint\limits_{R} f(x,y)\\\textrm d A &= \iint\limits_{R_1} 2 \\\textrm d A + \iint\limits_{R_2} \dfrac{1}{xy+x+y+1} \\\textrm d A\\[5pt] &= 2\iint\limits_{R_1} \textrm d A + \iint\limits_{R_2} \dfrac{1}{(x+1)(y+1)} \\\textrm d A\\[5pt] &= 2(2-0)(0-(-1)) + \Bigg( \int_0^2 \dfrac{1}{x+1} \\\textrm d x \Bigg) \Bigg( \int_0^1 \dfrac{1}{y+1}\\\textrm d y \Bigg) \\[5pt] &= 4 + \Big[\ln(x+1)\Big]_0^2 \cdot \Big[\ln(y+1)\Big]_0^1\\[5pt] &= 4+ \ln 3\ln 2. \end{aligned}


$$
