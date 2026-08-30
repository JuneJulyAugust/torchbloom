# Solving Many-Variable Nonlinear Equations

Source: https://www.mathacademy.com/topics/6294?courseId=120
Topic ID: 6294

## Prerequisites

- [Solving Radical Equations](../../../high-school/traditional/lessons/algebra-i/116-solving-radical-equations.md)
- [Solving Rational Equations Using the Flip Method](../../../high-school/traditional/lessons/algebra-i/266-solving-rational-equations-using-the-flip-method.md)
- [The Power Rule for Exponents With Algebraic Expressions](../../../high-school/traditional/lessons/algebra-i/362-the-power-rule-for-exponents-with-algebraic-expressions.md)
- [Solving Many-Variable Rational Equations](./6153-solving-many-variable-rational-equations.md)

## Lesson

### Introduction

In some cases, we might have to deal with a non-linear equation (e.g., an equation containing variable radicals or exponents) with more than one variable. A common task is to isolate one of the variables.

For example, the equation below relates the distinct positive real numbers $a,$ $b,$ and $x{:}$

$$


12\sqrt{15 - x} = \dfrac{b}{10a}.


$$

How can we expresses $x$ in terms of $a$ and $b?$

Expressing $x$ in terms of $a$ and $b$ means putting $x$ on one side of the equation (on its own) and everything else on the other. In this case, isolating $x$ means solving a radical equation containing multiple variables.

So, to express our equation in terms of $x,$ we first isolate the square root by dividing both sides by $12{:}$

$$


\begin{aligned}12\sqrt{√15−𝑥} & =\frac{𝑏}{10𝑎} \\ \frac{12\sqrt{√15−𝑥}}{12} & =\frac{𝑏}{10𝑎⋅12} \\ \frac{12\sqrt{√15−𝑥}}{12} & =\frac{𝑏}{10𝑎⋅12} \\ \sqrt{√15−𝑥} & =\frac{𝑏}{120𝑎}\end{aligned}


$$

Next, we square both sides:

$$


\begin{aligned}(\sqrt{√15−𝑥})^{2} & =(\frac{𝑏}{120𝑎})^{2} \\ 15−𝑥 & =(\frac{𝑏}{120𝑎})^{2}\end{aligned}


$$

Finally, we solve for $x{:}$

$$


\begin{aligned}15−𝑥 & =(\frac{𝑏}{120𝑎})^{2} \\ 15−𝑥−15 & =(\frac{𝑏}{120𝑎})^{2}−15 \\ −𝑥 & =(\frac{𝑏}{120𝑎})^{2}−15 \\ 𝑥 & =15−(\frac{𝑏}{120𝑎})^{2}\end{aligned}


$$

Therefore, we have

$$


x = 15 - \left(\dfrac{b}{120a}\right)^2.


$$

### Example: Isolating Variables in Multivariable Radical Equations

#### Question

The equation

$$


k = \sqrt{\dfrac{q\ell}{r}}


$$

relates the positive numbers $k,$ $q,$ $\ell,$ and $r.$ Which of the following equations correctly expresses $q$ in terms of $\ell,$ $r,$ and $k?$

#### Explanation

To get rid of the square root, we first square both sides:

$$


\begin{aligned}𝑘^{2} & =(\sqrt{√\frac{𝑞ℓ}{𝑟}})^{2} \\ 𝑘^{2} & =\frac{𝑞ℓ}{𝑟}\end{aligned}


$$

Next, we solve for $q.$ First, we multiply both sides by $r$ to remove the fraction:

$$


\begin{aligned}𝑘^{2} & =\frac{𝑞ℓ}{𝑟} \\ 𝑘^{2}⋅𝑟 & =\frac{𝑞ℓ}{𝑟}⋅𝑟 \\ 𝑘^{2}⋅𝑟 & =\frac{𝑞ℓ}{𝑟}⋅𝑟 \\ 𝑟𝑘^{2} & =𝑞ℓ\end{aligned}


$$

Finally, we divide both sides by $\ell$ to isolate $q{:}$

$$


\begin{aligned}\frac{𝑟𝑘^{2}}{ℓ} & =\frac{𝑞ℓ}{ℓ} \\ \frac{𝑟𝑘^{2}}{ℓ} & =\frac{𝑞ℓ}{ℓ} \\ \frac{𝑟𝑘^{2}}{ℓ} & =𝑞\end{aligned}


$$

Therefore, the correct answer is

$$


q = \dfrac{rk^2}{\ell}.


$$

### Example: Isolating Variables in Multivariable Quadratic Equations

#### Question

The equation

$$


n = 2(b - 5)^2


$$

relates the positive numbers $n$ and $b.$ Which of the following gives $b$ in terms of $n,$ where $b > 5?$

#### Explanation

First, we isolate $(b - 5)^2$ by dividing both sides by $2{:}$

$$


\begin{aligned}𝑛 & =2(𝑏−5)^{2} \\ \frac{𝑛}{2} & =\frac{2(𝑏−5)^{2}}{2} \\ \frac{𝑛}{2} & =(𝑏−5)^{2}\end{aligned}


$$

Next, we solve for $(b-5)$ by finding the square root of both sides. Notice that since $b > 5,$ we have that $(b-5)>0.$ So, we consider only the positive square root:

$$


\begin{aligned}𝑏−5 & =\sqrt{√\frac{𝑛}{2}}\end{aligned}


$$

Finally, we solve for $b$:

$$


\begin{aligned}𝑏 & =\sqrt{√\frac{𝑛}{2}}+5\end{aligned}


$$

Therefore, the correct answer is

$$


b = \sqrt{\dfrac{n}{2}} + 5.


$$

### Example: Isolating Variables in Multivariable Radical Equations Using the Laws of Exponents

#### Question

Consider the equation

$$


\sqrt[6]{x^7}=\sqrt[5]{y^3},


$$

where $x,$ and $y$ are all positive numbers. Which equation expresses $x$ in terms of $y?$

#### Explanation

Let's recall the rules of exponents:

- Negative exponents: $x^{-n} = \dfrac{1}{x^n}$

- Radicals as fractional exponents: $\sqrt[n]{x} = x^{1/n}$

- The product rule: $a^n \cdot a^m = a^{n+m}$

- The quotient rule: $\dfrac{a^n}{a^m} = a^{n-m}$

- The power rule: $\left(a^m \right)^n = a^{mn}$

- The power of product rule: $(ab)^n = a^nb^n$

- The power of quotient rule: $\left(\dfrac a b \right)^n = \dfrac{a^n}{b^n}$

First, let us convert our radicals to fractional exponents. Our equation becomes

$$


x^{7/6}=y^{3/5}.


$$

Now, since we would like to isolate $x,$ we take both sides to the power of $\dfrac{6}{7}$ and apply the power rule:

$$


\begin{aligned}𝑥^{7/6} & =𝑦^{3/5} \\ (𝑥^{7/6})^{6/7} & =(𝑦^{3/5})^{6/7} \\ 𝑥^{(7/6)⋅(6/7)} & =𝑦^{(3/5)⋅(6/7)} \\ 𝑥 & =𝑦^{18/35}\end{aligned}


$$

### Example: Isolating Variables In Rational Expressions

#### Question

The following equation relates the positive variables $a,$ $b,$ $c,$ and $d{:}$

$$


\dfrac{20}{a} = \dfrac{20}{b} - \dfrac{20}{c} - \dfrac{20}{d}


$$

Which of the following is equivalent to $b?$

#### Explanation

First, we factor out the common factor of $20$ on the right-hand side:

$$


\dfrac{20}{a} = 20\left(\dfrac{1}{b} - \dfrac{1}{c} - \dfrac{1}{d}\right)


$$

Then, we divide both sides by $20.$ This yields the equation

$$


\dfrac{1}{a} = \dfrac{1}{b} - \dfrac{1}{c} - \dfrac{1}{d}.


$$

To isolate $\dfrac{1}{b},$ we add $\dfrac{1}{c}$ and $\dfrac{1}{d}$ to both sides:

$$


\begin{aligned}\frac{1}{𝑎}+\frac{1}{𝑐}+\frac{1}{𝑑} & =\frac{1}{𝑏} \\ \frac{1}{𝑏} & =\frac{1}{𝑎}+\frac{1}{𝑐}+\frac{1}{𝑑}\end{aligned}


$$

We now combine the terms on the right-hand side using a common denominator of $acd$:

$$


\begin{aligned}\frac{1}{𝑏} & =\frac{1}{𝑎}+\frac{1}{𝑐}+\frac{1}{𝑑} \\ \frac{1}{𝑏} & =\frac{1}{𝑎}⋅\frac{𝑐𝑑}{𝑐𝑑}+\frac{1}{𝑐}⋅\frac{𝑎𝑑}{𝑎𝑑}+\frac{1}{𝑑}⋅\frac{𝑎𝑐}{𝑎𝑐} \\ \frac{1}{𝑏} & =\frac{𝑐𝑑+𝑎𝑑+𝑎𝑐}{𝑎𝑐𝑑}\end{aligned}


$$

Taking the reciprocal of both sides gives the desired relation:

$$


b = \dfrac{acd}{ac + ad + cd}


$$
