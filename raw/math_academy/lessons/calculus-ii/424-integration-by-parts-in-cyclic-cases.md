# Integration by Parts in Cyclic Cases

Source: https://www.mathacademy.com/topics/424?courseId=106
Topic ID: 424

## Prerequisites

- [Applying the Integration By Parts Twice](./416-applying-the-integration-by-parts-twice.md)

## Lesson

### Introduction

In some cases, applying integration by parts can lead to a cyclic pattern, where the original integral reappears after a few steps. This cyclic behavior allows us to solve the integral by forming an equation that can be solved algebraically.

To illustrate, let's consider the following example:

$$


I = \int \dfrac{\ln x}{x} \textrm{d}x


$$

Let's try using the method of integration by parts. We suppose that

$$


\begin{aligned}𝑢=ln⁡𝑥 & \,⇒\,\frac{d𝑢}{d𝑥}=\frac{1}{𝑥}\,, \\ \frac{d𝑣}{d𝑥}=\frac{1}{𝑥} & \,⇒\,𝑣=∫\frac{1}{𝑥}d𝑥=ln⁡𝑥\,.\end{aligned}


$$

Using the integration by parts formula, we get

$$


\begin{aligned}𝐼 & =∫𝑢\frac{d𝑣}{d𝑥}d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}d𝑥 \\ & =ln⁡𝑥(ln⁡𝑥)−∫(ln⁡𝑥)(\frac{1}{𝑥})d𝑥 \\ & =ln^{2}⁡𝑥−∫\frac{ln⁡𝑥}{𝑥}d𝑥 \\ & =ln^{2}⁡𝑥−𝐼\,.\end{aligned}


$$

We now have the same integral $I$ on both sides of the equality. Thinking about $I$ as some unknown variable, we can easily solve this equation:

$$


\begin{aligned}𝐼 & =ln^{2}⁡𝑥−𝐼 \\ 𝐼+𝐼 & =ln^{2}⁡𝑥 \\ 2𝐼 & =ln^{2}⁡𝑥 \\ 𝐼 & =\frac{ln^{2}⁡𝑥}{2}+𝐶\,.\end{aligned}


$$

Notice that we added a constant of integration right at the very end of the calculation.

### Example: Integrating a Logarithmic Expression Using Cyclic Integration by Parts

#### Question

Calculate $\displaystyle \int \dfrac{\ln^2{x}}{x} \textrm{d}x$ using integration by parts.

#### Explanation

First, we let

$$


I = \int \dfrac{\ln^2 x}{x} \, \textrm{d}x.


$$

To use integration by parts, let's suppose that

$$


\begin{aligned}𝑢=ln^{2}⁡𝑥 & \,⇒\,\frac{d𝑢}{d𝑥}=\frac{2ln⁡𝑥}{𝑥}\,, \\ \frac{d𝑣}{d𝑥}=\frac{1}{𝑥} & \,⇒\,𝑣=∫\frac{1}{𝑥}d𝑥=ln⁡𝑥\,.\end{aligned}


$$

Using the integration by parts formula, we get

$$


\begin{aligned}𝐼 & =∫\frac{ln^{2}⁡𝑥}{𝑥}\,d𝑥 \\ & =∫𝑢\frac{d𝑣}{d𝑥}\,d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}\,d𝑥 \\ & =(ln^{2}⁡𝑥)(ln⁡𝑥)−∫(ln⁡𝑥)(\frac{2ln⁡𝑥}{𝑥})d𝑥 \\ & =ln^{3}⁡𝑥−2∫\frac{ln^{2}⁡𝑥}{𝑥}\,d𝑥 \\ & =ln^{3}⁡𝑥−2𝐼.\end{aligned}


$$

Finally, we solve for $I,$ remembering to add a constant of integration $C$ at the very end:

$$


\begin{aligned}𝐼 & =ln^{3}⁡𝑥−2𝐼 \\ 3𝐼 & =ln^{3}⁡𝑥 \\ 𝐼 & =\frac{ln^{3}⁡𝑥}{3}+𝐶\end{aligned}


$$

### Example: Finding the Indefinite Integral of an Exponential-Trigonometric Expression Using Integration by Parts

#### Question

Calculate $\displaystyle \int e^{x}\sin{x} \, \textrm{d}x.$

#### Explanation

To use integration by parts, let's suppose that

$$


\begin{aligned}𝑢=𝑒^{𝑥}\, & ⇒\,\frac{d𝑢}{d𝑥}=𝑒^{𝑥}\,, \\ \frac{d𝑣}{d𝑥}=sin⁡𝑥\, & ⇒\,𝑣=∫sin⁡𝑥\,d𝑥=−cos⁡𝑥.\end{aligned}


$$

Using the integration by parts formula, we get

$$


\begin{aligned}𝐼 & =∫𝑒^{𝑥}sin⁡𝑥\,d𝑥 \\ & =∫𝑢\frac{d𝑣}{d𝑥}\,d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}\,d𝑥 \\ & =𝑒^{𝑥}(−cos⁡𝑥)−∫(−cos⁡𝑥)(𝑒^{𝑥})d𝑥 \\ & =−𝑒^{𝑥}cos⁡𝑥+∫𝑒^{𝑥}cos⁡𝑥\,d𝑥 \\ & =−𝑒^{𝑥}cos⁡𝑥+𝐽.\end{aligned}


$$

Again, we can use integration by parts to evaluate

$$


J = \int e^{x}\cos{x}\,\textrm{d}x.


$$

To do this, let's suppose that

$$


\begin{aligned}𝑢=𝑒^{𝑥}\, & ⇒\,\frac{d𝑢}{d𝑥}=𝑒^{𝑥}\,, \\ \frac{d𝑣}{d𝑥}=cos⁡𝑥\, & ⇒\,𝑣=∫cos⁡𝑥\,d𝑥=sin⁡𝑥.\end{aligned}


$$

Using the integration by parts formula once more, we get

$$


\begin{aligned}𝐽 & =∫𝑒^{𝑥}cos⁡𝑥\,d𝑥 \\ & =∫𝑢\frac{d𝑣}{d𝑥}\,d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}\,d𝑥 \\ & =𝑒^{𝑥}(sin⁡𝑥)−∫(sin⁡𝑥)(𝑒^{𝑥})d𝑥 \\ & =𝑒^{𝑥}sin⁡𝑥−∫𝑒^{𝑥}sin⁡𝑥\,d𝑥 \\ & =𝑒^{𝑥}sin⁡𝑥−𝐼.\end{aligned}


$$

Finally, substituting this back into our equation for $I,$ we can subsequently solve for $I.$ We remember to add a constant of integration $C$ at the end.

$$


\begin{aligned}𝐼 & =−𝑒^{𝑥}cos⁡𝑥+𝐽 \\ 𝐼 & =−𝑒^{𝑥}cos⁡𝑥+𝑒^{𝑥}sin⁡𝑥−𝐼 \\ 2𝐼 & =−𝑒^{𝑥}cos⁡𝑥+𝑒^{𝑥}sin⁡𝑥 \\ 𝐼 & =\frac{𝑒^{𝑥}}{2}(sin⁡𝑥−cos⁡𝑥)+𝐶\end{aligned}


$$

### Example: Finding the Definite Integral of an Exponential-Trigonometric Expression Using Integration by Parts

#### Question

Evaluate $\displaystyle \int_0^{\pi/2} e^x\sin(2x) \, \textrm{d}x.$

#### Explanation

Let's denote the indefinite integral by $I = \displaystyle \int e^{x}\sin(2x)\, \textrm{d}x.$

To use integration by parts, let's suppose that

$$


\begin{aligned}𝑢=𝑒^{𝑥}\, & ⇒\,\frac{d𝑢}{d𝑥}=𝑒^{𝑥}\,, \\ \frac{d𝑣}{d𝑥}=sin⁡(2𝑥)\, & ⇒\,𝑣=∫sin⁡(2𝑥)\,d𝑥=−\frac{cos⁡(2𝑥)}{2}.\end{aligned}


$$

Using the integration by parts formula, we get

$$


\begin{aligned}𝐼 & =∫𝑒^{𝑥}sin⁡(2𝑥)\,d𝑥 \\ & =∫𝑢\frac{d𝑣}{d𝑥}\,d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}\,d𝑥 \\ & =𝑒^{𝑥}(−\frac{cos⁡(2𝑥)}{2})−∫(−\frac{cos⁡(2𝑥)}{2})(𝑒^{𝑥})d𝑥 \\ & =−\frac{𝑒^{𝑥}cos⁡(2𝑥)}{2}+\frac{1}{2}∫𝑒^{𝑥}cos⁡(2𝑥)\,d𝑥 \\ & =−\frac{𝑒^{𝑥}cos⁡(2𝑥)}{2}+\frac{1}{2}𝐽.\end{aligned}


$$

Again, we can use integration by parts to evaluate

$$


J = \int e^{x}\cos(2x)\,\textrm{d}x.


$$

To do this, let's suppose that

$$


\begin{aligned}𝑢=𝑒^{𝑥}\, & ⇒\,\frac{d𝑢}{d𝑥}=𝑒^{𝑥}\,, \\ \frac{d𝑣}{d𝑥}=cos⁡(2𝑥)\, & ⇒\,𝑣=∫cos⁡(2𝑥)\,d𝑥=\frac{sin⁡(2𝑥)}{2}.\end{aligned}


$$

Using the integration by parts formula once more, we get

$$


\begin{aligned}𝐽 & =∫𝑒^{𝑥}cos⁡(2𝑥)\,d𝑥 \\ & =∫𝑢\frac{d𝑣}{d𝑥}\,d𝑥 \\ & =𝑢𝑣−∫𝑣\frac{d𝑢}{d𝑥}\,d𝑥 \\ & =𝑒^{𝑥}(\frac{sin⁡(2𝑥)}{2})−∫(\frac{sin⁡(2𝑥)}{2})(𝑒^{𝑥})d𝑥 \\ & =\frac{𝑒^{𝑥}sin⁡(2𝑥)}{2}−\frac{1}{2}∫𝑒^{𝑥}sin⁡(2𝑥)\,d𝑥 \\ & =\frac{𝑒^{𝑥}sin⁡(2𝑥)}{2}−\frac{1}{2}𝐼.\end{aligned}


$$

So, substituting this into our equation for $I,$ we can subsequently solve for $I\mathbin.$ We can ignore the constant of integration in this case, because it is insignificant for further evaluation of the definite integral.

$$


\begin{aligned}𝐼 & =−\frac{𝑒^{𝑥}cos⁡(2𝑥)}{2}+\frac{1}{2}𝐽 \\ 𝐼 & =−\frac{𝑒^{𝑥}cos⁡(2𝑥)}{2}+\frac{1}{2}(\frac{𝑒^{𝑥}sin⁡(2𝑥)}{2}−\frac{1}{2}𝐼) \\ 𝐼 & =−\frac{𝑒^{𝑥}cos⁡(2𝑥)}{2}+\frac{𝑒^{𝑥}sin⁡(2𝑥)}{4}−\frac{1}{4}𝐼 \\ \frac{5}{4}𝐼 & =\frac{𝑒^{𝑥}sin⁡(2𝑥)−2𝑒^{𝑥}cos⁡(2𝑥)}{4} \\ 𝐼 & =\frac{𝑒^{𝑥}(sin⁡(2𝑥)−2cos⁡(2𝑥))}{5}\end{aligned}


$$

Finally, we evaluate our definite integral, as follows:

$$


\begin{aligned}∫_{𝜋/20}^{}𝑒^{𝑥}sin⁡(2𝑥)\,d𝑥 & =(\frac{𝑒^{𝑥}(sin⁡(2𝑥)−2cos⁡(2𝑥))}{5})_{𝜋/20}^{} \\ & =\frac{𝑒^{𝜋/2}(sin⁡(2⋅\frac{𝜋}{2})−2cos⁡(2⋅\frac{𝜋}{2}))}{2}−\frac{𝑒^{0}(sin⁡(2⋅0)−2cos⁡(2⋅0))}{5} \\ & =\frac{2𝑒^{𝜋/2}}{5}+\frac{2}{5} \\ & =\frac{2}{5}(𝑒^{𝜋/2}+1)\end{aligned}


$$
