# The Second Fundamental Theorem of Calculus

Source: https://www.mathacademy.com/topics/613?courseId=136
Topic ID: 613

## Prerequisites

- [The Integral as an Accumulation Function](./333-the-integral-as-an-accumulation-function.md)

## Lesson

### Introduction

The **second fundamental theorem of calculus** (abbreviated FTC II) states the following:

*If a function $f(x)$ is continuous on $[a,b]$ with $x\in(a,b),$ and the accumulation function $F(x)$ is defined as*

$$


F(x) = \int_a^x f(t)\,\textrm d t,


$$

*then the derivative of $F(x)$ is given by*

$$


F'(x) = \dfrac {\textrm d} {\textrm dx} \int_a^x f(t) \,\textrm d t = f(x).


$$

Loosely speaking, taking the derivative "cancels out" the integral and leaves us with the integrand. This happens because the derivative and the integral are *opposite* operations.

To demonstrate how this works, let's define the accumulation function $F(x)$ as

$$


F(x)=\int^{x}_{2} \sin(t^2)\,\textrm d t.


$$

Suppose that we want to differentiate this function to find $F'(x).$ Let's start by differentiating both sides with respect to $x,$ which gives

$$


F'(x) = \dfrac{\textrm{d}}{\textrm{d}x}\int^{x}_{2} \sin(t^2)\,\textrm d t.


$$

Evaluating the integral on the right-hand side is difficult. However, we can apply FTC II and get

$$


\begin{aligned}𝐹^{′}(𝑥)=sin⁡(𝑥^{2}).\end{aligned}


$$

And that's it! This theorem saves us a ton of work and is especially useful when the integral is hard to calculate.

**Note:** To gain further intuition for FTC II, it helps to work out an example in a simple case. Let's define the accumulation function $F(x)$ as an integral that we can actually compute:

$$


F(x)=\int^{x}_{2} t^2 \,\textrm d t


$$

Computing the integral, we have

$$


\begin{aligned}𝐹(𝑥) & =\frac{𝑡^{3}}{3}_{𝑥2}^{}=\frac{𝑥^{3}}{3}−\frac{8}{3},\end{aligned}


$$

and taking the derivative, we get

$$


\begin{aligned}𝐹^{′}(𝑥) & =\frac{d}{d𝑥}(\frac{𝑥^{3}}{3}−\frac{8}{3})=𝑥^{2},\end{aligned}


$$

which matches up with the original integrand. Taking the integral turned $t^2$ into $\dfrac{x^3}{3}$ minus a constant, and taking the derivative "reversed" the process to give us just $x^2.$

### Example: Applying the Second Fundamental Theorem of Calculus

#### Question

Calculate $\displaystyle\dfrac {\textrm d} {\textrm dx} \int_2^x \dfrac {t^3} {t-1}\,\textrm d t$ for $x>2.$

#### Explanation

The function $\dfrac {t^3} {t-1}$ is continuous on $[2,x],$ where $x>2.$ So FTC II applies, and we get

$$


\begin{aligned}\frac{d}{d𝑥}∫_{𝑥2}^{}\frac{𝑡^{3}}{𝑡−1}\,d𝑡=\frac{𝑥^{3}}{𝑥−1}.\end{aligned}


$$

### Example: Applying the Second Fundamental Theorem of Calculus by Interchanging the Limits of Integration

#### Question

Calculate $\displaystyle\dfrac {\textrm d} {\textrm dx} \int_x^0 \dfrac{t^3}{t^2 +1}\,\textrm d t.$

#### Explanation

In this example, the variable limit $x$ is located on the lower limit. To apply FTC II, we need the variable to be on the upper limit. Using the properties of definite integrals, we can write

$$


\displaystyle \int_x^0 \dfrac{t^3}{t^2 +1} \,\textrm d t = - \int_0^x \dfrac{t^3}{t^2 +1}\,\textrm d t.


$$

Therefore, by FTC II, we have

$$


\begin{aligned} \displaystyle\dfrac {\textrm d} {\textrm dx} \int_x^0 \dfrac{t^3}{t^2 +1} \,\textrm d t & \, \, = \, \, \dfrac {\textrm d} {\textrm dx} \left(-\int_0^x \dfrac{t^3}{t^2 +1} \,\textrm d t \right)\\& \, \, = \, \, -\dfrac {\textrm d} {\textrm dx} \left(\int_0^x \dfrac{t^3}{t^2 +1} \,\textrm d t \right)\\&= \, \, -\dfrac{x^3}{x^2 +1}.\end{aligned}


$$

### Example: Applying the Second Fundamental Theorem of Calculus Using the Chain Rule

#### Question

Find $f'(x)$ for $f(x) = \displaystyle \int_2^{x^2}\arctan t\,\textrm d t.$

#### Explanation

To compute $f'(x),$ we first make the substitution $u=x^2$ and then we apply the chain rule, as follows:

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}∫_{𝑥^{2}2}^{}arctan⁡𝑡\,d𝑡 \\ & =\frac{du}{d𝑥}⋅\frac{d}{d𝑢}∫_{𝑢2}^{}arctan⁡𝑡\,d𝑡.\end{aligned}


$$

The integrand is continuous for all $t,$ so by FTC II we get

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d𝑢}{d𝑥}⋅arctan⁡(𝑢) \\ & =\frac{d}{d𝑥}(𝑥^{2})⋅arctan⁡(𝑢) \\ & =2𝑥arctan⁡(𝑥^{2}).\end{aligned}


$$

### Example: Applying the Second Fundamental Theorem of Calculus With Two Variable Limits

#### Question

Find $f'(1)$ if $\displaystyle f(x) = \int_x^{x^2} (t^2 + 2t) \,\, \textrm d t.$

#### Explanation

Here, both the lower and upper limits contain a variable. However, to apply FTC II, we need the variable to be on the upper limit only. So, we can split the integral into two integrals, and rewrite them so that in both cases the variable is on the upper limit. We get

$$


\begin{aligned}\begin{aligned}∫_{𝑥^{2}𝑥}^{}(𝑡^{2}+2𝑡)\,d𝑡 & =∫_{𝑎𝑥}^{}(𝑡^{2}+2𝑡)\,d𝑡+∫_{𝑥^{2}𝑎}^{}(𝑡^{2}+2𝑡)\,d𝑡 \\ & =−∫_{𝑥𝑎}^{}(𝑡^{2}+2𝑡)\,d𝑡+∫_{𝑥^{2}𝑎}^{}(𝑡^{2}+2𝑡)\,d𝑡,\end{aligned}\end{aligned}


$$

where $a$ is any constant number between $x$ and $x^2.$

The integrand $t^2 + 2t$ is continuous for all $t,$ so applying FTC II gives

$$


\begin{aligned}𝑓^{′}(𝑥) & =\frac{d}{d𝑥}(−∫_{𝑥𝑎}^{}(𝑡^{2}+2𝑡)\,d𝑡+∫_{𝑥^{2}𝑎}^{}(𝑡^{2}+2𝑡)\,d𝑡) \\ & =−\frac{d}{d𝑥}(∫_{𝑥𝑎}^{}(𝑡^{2}+2𝑡)\,d𝑡)+\frac{d}{d𝑥}(∫_{𝑥^{2}𝑎}^{}(𝑡^{2}+2𝑡)\,d𝑡) \\ & =−(𝑥^{2}+2𝑥)+\frac{d𝑢}{d𝑥}\frac{d}{d𝑢}(∫_{𝑢𝑎}^{}(𝑡^{2}+2𝑡)\,d𝑡) \\ & =−𝑥^{2}−2𝑥+2𝑥(𝑢^{2}+2𝑢) \\ & =−𝑥^{2}−2𝑥+2𝑥((𝑥^{2})^{2}+2𝑥^{2}) \\ & =−𝑥^{2}−2𝑥+2𝑥(𝑥^{4}+2𝑥^{2}) \\ & =−𝑥^{2}−2𝑥+2𝑥^{5}+4𝑥^{3} \\ & =2𝑥^{5}+4𝑥^{3}−𝑥^{2}−2𝑥.\end{aligned}


$$

Note that we used the substitution $u=x^2,$ as before.

Finally, we can compute $f'(1).$ We get

$$


\begin{aligned}𝑓^{′}(1) & =2(1)^{5}+4(1)^{3}−(1)^{2}−2(1) \\ & =2+4−1−2 \\ & =3.\end{aligned}


$$
