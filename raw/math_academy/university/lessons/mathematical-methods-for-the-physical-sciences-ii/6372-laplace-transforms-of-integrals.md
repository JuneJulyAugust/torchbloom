# Laplace Transforms of Integrals

Source: https://www.mathacademy.com/topics/6372?courseId=155
Topic ID: 6372

## Prerequisites

- [Introduction to Integration by Parts](../../../ap-courses/lessons/ap-calculus-bc/317-introduction-to-integration-by-parts.md)
- [The Integral as an Accumulation Function](../../../ap-courses/lessons/ap-calculus-ab/333-the-integral-as-an-accumulation-function.md)
- [Inverse Laplace Transforms](./2530-inverse-laplace-transforms.md)

## Lesson

### Introduction

Suppose a quantity increases over time at a rate proportional to its current value, such as the balance of a bank account growing with continuous interest. The Laplace transform can be used to analyze how such exponential growth behaves, especially when the function is **integrated over time** to represent total accumulation.

To illustrate this, we’ll find the Laplace transform of a function defined as the integral of an exponential function. This shows how *integration in the time domain* corresponds to *division by $s$* in the $s$-domain.

Suppose we are given that

$$


\mathcal{L}\{e^{at}\} = \dfrac{1}{s-a}, \qquad s>a.


$$

Let's find the Laplace transform of

$$


g(t) = \int_{0}^{t} e^{\tau/2}\,\mathrm{d}\tau, \qquad s > \dfrac{1}{2}.


$$

We apply the **Integration in Time Property**: if $\mathcal{L}\{f(t)\} = F(s)$, then

$$


\mathcal{L}\!\left\{\int_{0}^{t} f(\tau)\,\mathrm{d}\tau \right\} = \frac{F(s)}{s}.


$$

In our case, $f(t)=e^{t/2}$. Thus, for $s>\dfrac{1}{2},$

$$


\begin{aligned}𝐹(𝑠) & =L{𝑓(𝑡)} \\ & =L{𝑒^{𝑡/2}} \\ & =\frac{1}{(𝑠−\frac{1}{2})}.\end{aligned}


$$

Therefore, applying the integral identity above, we have for $s>\dfrac{1}{2},$

$$


\begin{aligned}L{𝑔(𝑡)} & =L\,{∫_{𝑡0}𝑒^{𝜏/2}\,d𝜏} \\ & =\frac{𝐹(𝑠)}{𝑠} \\ & =\frac{1}{𝑠\,(𝑠−\frac{1}{2})} \\ & =\frac{2}{𝑠(2𝑠−1)}.\end{aligned}


$$

### The General Result

Assume that

- $f(t)$ is *piecewise continuous* on $[0,\infty)$, and

- $f(t)$ is of exponential order $a$.

Then the Laplace transform

$$


F(s)=\mathcal L\{f(t)\}


$$

exists for all $s>a$, and we have the **Integration Property**:

$$


\mathcal L\!\left\{\int_0^t f(\tau)\,\text{d}\tau\right\} = \frac{F(s)}{s}, \qquad s>a.


$$

This result shows that *integrating a function with respect to time* corresponds to *dividing its Laplace transform by $s$*.

This result allows us to handle accumulated quantities without re-integrating from scratch.

Next, we will apply this property to a concrete example.

### Example: Finding the Laplace Transform of an Integral

#### Question

Given that $\mathcal{L}\{\cos(\omega t)\} = \dfrac{s}{s^2+\omega^2}$ for $s>0,$ find the Laplace transform of

$$


\displaystyle g(t)= \int_{0}^{t} \cos\big(\pi\tau\big) \, \text{d}\tau, \quad s>0.


$$

#### Explanation

We know that if $\mathcal{L}\{f(t)\} = F(s)$, then

$$


\mathcal{L}\left\{\int_{0}^{t} f(\tau) \, \text{d}\tau \right\} = \frac{F(s)}{s}.


$$

In our case, $f(t) = \cos(\pi t).$ Thus, for $s > 0,$

$$


\begin{aligned}𝐹(𝑠) & =L{𝑓(𝑡)} \\ & =L{cos⁡(𝜋𝑡)} \\ & =\frac{𝑠}{𝑠^{2}+𝜋^{2}}.\end{aligned}


$$

Therefore, applying the integral identity above, we have that for $s > 0,$

$$


\begin{aligned}L{𝑔(𝑡)} & =L{∫_{𝑡0}cos⁡(𝜋𝜏)\,d𝜏} \\ & =\frac{𝐹(𝑠)}{𝑠} \\ & =\frac{1}{𝑠^{2}+𝜋^{2}}.\end{aligned}


$$

### Example: Finding an Inverse Laplace Transform Using the Integral Rule

#### Question

For the function

$$


G(s) = \dfrac{1}{s(s-1)}, \qquad s > 1


$$

find the inverse Laplace transform of $G(s),$ given that $\mathcal{L}\{e^{at}\}=\dfrac{1}{s-a},\ s>a.$

#### Explanation

Notice that we can write $G(s)$ as

$$


G(s) = \frac{1}{s(s-1)} = \frac{F(s)}{s},


$$

where $F(s) = \dfrac{1}{s-1}.$ Also, we know that

$$


\mathcal{L}\{e^{at}\}=\frac{1}{s-a}.


$$

Thus, we get

$$


\begin{aligned}L^{−1}{𝐹(𝑠)} & =L^{−1}{\frac{1}{𝑠−1}} \\ & =𝑒^{𝑡}.\end{aligned}


$$

Additionally, we know that if $\mathcal{L}\{f(t)\} = F(s)$, then

$$


\mathcal{L}\left\{\int_{0}^{t} f(\tau)\, \text{d}\tau \right\} = \frac{F(s)}{s}.


$$

Using the property above in reverse, we obtain

$$


\begin{aligned}L^{−1}{𝐺(𝑠)} & =L^{−1}{\frac{𝐹(𝑠)}{𝑠}} \\ & =∫_{𝑡0}𝑓(𝜏)\,d𝜏 \\ & =∫_{𝑡0}𝑒^{𝜏}\,d𝜏 \\ & =𝑒^{𝜏}\,_{𝑡0} \\ & =𝑒^{𝑡}−1.\end{aligned}


$$

### Example: Proving the Formula for Laplace Transforms of Integrals

#### Question

Prove that if $\mathcal{L}\{f(t)\} = F(s)$, then

$$


\mathcal{L}\left\{\int_{0}^{t} f(\tau)\, d\tau \right\} = \frac{F(s)}{s}.


$$

#### Explanation

Let $A(t)$ be the anti-derivative of $f(t)$ such that $A'(t) = f(t)$ and $A(0) ={0}.$ Then,

$$


\begin{aligned}∫_{𝑡0}𝑓(𝜏)\,𝑑𝜏 & =𝐴(𝜏)\,_{𝑡0} \\ & =𝐴(𝑡)−𝐴(0) \\ & =𝐴(𝑡).\end{aligned}


$$

By definition of the Laplace transform, we can write

$$


\begin{aligned}L{∫_{𝑡0}𝑓(𝜏)\,d𝜏} & =L{𝐴(𝑡)}=∫_{∞0}𝑒^{−𝑠𝑡}𝐴(𝑡)\,d𝑡.\end{aligned}


$$

Now, let's use integration by parts:

$$


\begin{aligned}𝑢=𝐴(𝑡) & \,⇒\, & d𝑢=𝐴^{′}(𝑡)\,d𝑡 \\ d𝑣=𝑒^{−𝑠𝑡}\,d𝑡 & ⇒ & 𝑣=−\frac{1}{𝑠}𝑒^{−𝑠𝑡}\end{aligned}


$$

Substituting into the integration by parts formula, we get

$$


\begin{aligned}∫_{∞0}𝑒^{−𝑠𝑡}𝐴(𝑡)\,d𝑡 & =𝐴(𝑡)(−\frac{1}{𝑠}𝑒^{−𝑠𝑡})\,_{∞0}−∫_{∞0}(−\frac{1}{𝑠}𝑒^{−𝑠𝑡})𝐴^{′}(𝑡)\,d𝑡.\end{aligned}


$$

Since $A(0)=0$ and $\dfrac{1}{s}e^{-st} \to 0$ as $t \to \infty,$ we have $-\dfrac{1}{s}A(t)e^{-st}\bigg|_0^{\infty} = {0}$ and

$$


\int_0^{\infty} e^{-st}A(t)\,\mathrm{d}t = \dfrac{1}{s}\int_0^{\infty}{ e^{-st} A'(t)} \,\mathrm{d}t.


$$

Finally, using that $A'(t) = f(t),$ we obtain

$$


\begin{aligned}\frac{1}{𝑠}∫_{∞0}𝑒^{−𝑠𝑡}𝐴^{′}(𝑡)\,d𝑡 & =\frac{1}{𝑠}∫_{∞0}𝑒^{−𝑠𝑡}𝑓(𝑡)\,d𝑡 \\ & =\frac{1}{𝑠}⋅𝐹(𝑠) \\ & =\frac{𝐹(𝑠)}{𝑠}.\end{aligned}


$$
