# Conditional Variance for Continuous Random Variables

Source: https://www.mathacademy.com/topics/3929?courseId=145
Topic ID: 3929

## Prerequisites

- [Conditional Expectation for Continuous Random Variables](./3057-conditional-expectation-for-continuous-random-variables.md)
- [Conditional Variance for Discrete Random Variables](./3926-conditional-variance-for-discrete-random-variables.md)

## Lesson

### Introduction

Suppose $X$ and $Y$ are continuous random variables, where the conditional expected value of $X$ given $Y=y$ is given by $\mu_{X|y}.$ In other words,

$$


\textrm{E}[X\,|\,Y=y] = \mu_{X|y}.


$$

The **conditional variance of $X$ given $Y=y$** is defined as

$$


\textrm{Var}[X\,|\,Y] = \textrm{E}\big[(X - \mu_{X|y} \big)^2 \,|\, Y=y].


$$

As with the discrete case, this definition can be written as

$$


\begin{aligned}Var[𝑋\,|\,𝑌=𝑦] & =E[𝑋^{2}\,|\,𝑌=𝑦]−𝜇_{2𝑋|𝑦}^{}\end{aligned}


$$

where

$$


\displaystyle \textrm{E}\big[X^2 \,| \, Y=y \big] = \int_{-\infty}^{\infty} x^2 \, f_{X|Y}(x \,|\, y) \: \textrm{d}x,


$$

and $f_{X|Y}(x \,|\, y)$ is the conditional probability density function of $X$ given $Y=y.$ Note that these formulas are analogous to those for $\textrm{Var}[X]$ for continuous $X.$

When we select a particular value of $y,$ the conditional variance of $X$ given $Y=y$ returns a real number. However, if $y$ is not specified, then $\textrm {Var}[X | Y = y]$ gives us a *function* of $y.$

We have an analogous definition for the **conditional variance of $Y$ given $X=x{:}$**

$$


\begin{aligned}Var[𝑌\,|\,𝑋=𝑥] & =E[(𝑌−𝜇_{𝑌|𝑥})^{2}\,|\,𝑋=𝑥] \\ & =E[𝑌^{2}\,|\,𝑋=𝑥]−𝜇_{2𝑌|𝑥}^{}\end{aligned}


$$

where

- $\mu_{Y|x} = \textrm{E}\big[Y \,| \, X=x \big]$ is the conditional expected value of $Y$ given $X=x,$

- $\displaystyle \textrm{E}\big[Y^2 \,| \, X=x \big] = \int_{-\infty}^{\infty} y^2 \, f_{Y|X}(y \,|\, x) \: \textrm{d}y,$ and

- $f_{Y|X}(y \,|\, x)$ is the conditional probability density function of $Y$ given $X=x.$

### A Worked Example

Suppose that $X$ and $Y$ are continuous random variables. It is known that the conditional probability density function $f_{Y|X}(y \,|\, 1)$ is given by

$$


\begin{aligned}4𝑦^{3}, & \,0≤𝑦≤1 \\ 0, & \,otherwise\end{aligned}


$$

and that

$$


\mu_{Y|1}=\dfrac{4}{5}.


$$

What is the conditional variance $\textrm{Var}\big[Y \,|\, X=1\big]?$

The conditional variance of $Y$ given $X=x$ is defined by

$$


\begin{aligned}Var[𝑌\,|\,𝑋=𝑥] & =E[(𝑌−𝜇_{𝑌|𝑥})^{2}\,|\,𝑋=𝑥] \\ & =E[𝑌^{2}\,|\,𝑋=𝑥]−𝜇_{2𝑌|𝑥}^{},\end{aligned}


$$

where

$$


\textrm{E}\big[Y^2 \,| \, X=x \big] = \int_{-\infty}^{\infty} y^2 \, f_{Y|X}(y \,|\, x) \: \textrm{d}y.


$$

Therefore, we obtain

$$


\begin{aligned}E[𝑌^{2}\,|\,𝑋=1] & =∫_{∞−∞}^{}𝑦^{2}\,𝑓_{𝑌|𝑋}(𝑦\,|\,1)\,d𝑦 \\ & =∫_{10}^{}𝑦^{2}⋅4𝑦^{3}\,d𝑥 \\ & =∫_{10}^{}4𝑦^{5}\,d𝑦 \\ & =[\frac{2𝑦^{6}}{3}]_{10}^{} \\ & =\frac{2}{3}.\end{aligned}


$$

Finally,

$$


\begin{aligned}Var[𝑌\,|\,𝑋=1] & =E[𝑌^{2}\,|\,𝑋=1]−𝜇_{2𝑌|1}^{} \\ & =\frac{2}{3}−(\frac{4}{5})^{2} \\ & =\frac{2}{3}−\frac{16}{25} \\ & =\frac{2}{75}.\end{aligned}


$$

### Example: Calculating a Conditional Variance Given a Conditional PDF

#### Question

$$


\begin{aligned}3𝑥^{2}, & \,0≤𝑥≤1 \\ 0, & \,otherwise\end{aligned}


$$

Let $X$ and $Y$ be continuous random variables. Find the conditional variance $\textrm{Var}\big[X \,|\, Y=-2\big]$ given that the conditional probability density function $f_{X|Y}(x \,|\, -2)$ is shown above and the corresponding expected value is $\mu_{X|-2}=\dfrac{3}{4}.$

#### Explanation

Recall that the conditional variance of $X$ given $Y=y$ is defined by

$$


\begin{aligned}Var[𝑋\,|\,𝑌=𝑦] & =E[(𝑋−𝜇_{𝑋|𝑦})^{2}\,|\,𝑌=𝑦] \\ & =E[𝑋^{2}\,|\,𝑌=𝑦]−𝜇_{2𝑋|𝑦}^{},\end{aligned}


$$

where

$$


\textrm{E}\big[X^2 \,| \, Y=y \big] = \int_{-\infty}^{\infty} x^2 \, f_{X|Y}(x \,|\, y) \: \textrm{d}x.


$$

Therefore, we obtain

$$


\begin{aligned}E[𝑋^{2}\,|\,𝑌=−2] & =∫_{∞−∞}^{}𝑥^{2}\,𝑓_{𝑋|𝑌}(𝑥\,|\,−2)\,d𝑥 \\ & =∫_{10}^{}𝑥^{2}⋅3𝑥^{2}\,d𝑥 \\ & =∫_{10}^{}3𝑥^{4}\,d𝑥 \\ & =[\frac{3𝑥^{5}}{5}]_{10}^{} \\ & =\frac{3}{5}−0 \\ & =\frac{3}{5}.\end{aligned}


$$

Finally,

$$


\begin{aligned}Var[𝑋\,|\,𝑌=−2] & =E[𝑋^{2}\,|\,𝑌=−2]−𝜇_{2𝑋|−2}^{} \\ & =\frac{3}{5}−(\frac{3}{4})^{2} \\ & =\frac{3}{5}−\frac{9}{16} \\ & =\frac{3}{80}.\end{aligned}


$$

### Example: Calculating a Conditional Variance Given a Conditional PDF Using Improper Integrals

#### Question

$$


\begin{aligned}\frac{3}{𝑦^{4}}, & \,𝑦≥1 \\ 0, & \,otherwise\end{aligned}


$$

Let $X$ and $Y$ be continuous random variables. Find the conditional variance $\textrm{Var}\big[Y \,|\, X=3\big]$ given that the conditional probability density function $f_{Y|X}(y \,|\, 3)$ is shown above and the corresponding expected value is $\mu_{Y|3}=\dfrac{3}{2}.$

#### Explanation

Recall that the conditional variance of $Y$ given $X=x$ is defined by

$$


\begin{aligned}Var[𝑌\,|\,𝑋=𝑥] & =E[(𝑌−𝜇_{𝑌|𝑥})^{2}\,|\,𝑋=𝑥] \\ & =E[𝑌^{2}\,|\,𝑋=𝑥]−𝜇_{2𝑌|𝑥}^{},\end{aligned}


$$

where

$$


\textrm{E}\big[Y^2 \,| \, X=x \big] = \int_{-\infty}^{\infty} y^2 \, f_{Y|X}(y \,|\, x) \: \textrm{d}y.


$$

Therefore, we obtain

$$


\begin{aligned}E[𝑌^{2}\,|\,𝑋=3] & =∫_{∞−∞}^{}𝑦^{2}\,𝑓_{𝑌|𝑋}(𝑦\,|\,3)\,d𝑦 \\ & =∫_{∞1}^{}𝑦^{2}⋅\frac{3}{𝑦^{4}}\,d𝑦 \\ & =∫_{∞1}^{}\frac{3}{𝑦^{2}}\,d𝑦 \\ & =∫_{∞1}^{}3𝑦^{−2}\,d𝑦 \\ & =[3⋅\frac{𝑦^{−1}}{(−1)}]_{∞1}^{} \\ & =[−\frac{3}{𝑦}]_{∞1}^{} \\ & =0−(−3) \\ & =3.\end{aligned}


$$

Finally,

$$


\begin{aligned}Var[𝑌\,|\,𝑋=3] & =E[𝑌^{2}\,|\,𝑋=3]−𝜇_{2𝑌|3}^{} \\ & =3−(\frac{3}{2})^{2} \\ & =3−\frac{9}{4} \\ & =\frac{3}{4}.\end{aligned}


$$

### Example: Calculating a Conditional Variance Given Joint and Marginal Density Functions

#### Question

$$


\begin{aligned}𝑓(𝑥,𝑦)=\begin{aligned}2𝑦ln⁡(𝑥), & 1≤𝑥≤𝑒,\,0≤𝑦≤1, \\ 0, & otherwise\end{aligned}\,𝑓_{𝑋}(𝑥)=\begin{aligned}ln⁡(𝑥), & 1≤𝑥≤𝑒, \\ 0, & otherwise\end{aligned}\end{aligned}


$$

Let $X$ and $Y$ be continuous random variables. Their joint probability density function and the marginal probability density function of $X$ are shown above. Find the conditional variance $\textrm{Var}\big[Y \,\big|\, X=1 \big]$ given that the corresponding expected value is $\mu_{Y|1}=\dfrac{2}{3}.$

#### Explanation

Recall that the conditional variance of $Y$ given $X=x$ is defined by

$$


\begin{aligned}Var[𝑌\,|\,𝑋=𝑥] & =E[(𝑌−𝜇_{𝑌|𝑥})^{2}\,|\,𝑋=𝑥] \\ & =E[𝑌^{2}\,|\,𝑋=𝑥]−𝜇_{2𝑌|𝑥}^{},\end{aligned}


$$

where

$$


\textrm{E}\big[Y^2 \,| \, X=x \big] = \int_{-\infty}^{\infty} y^2 \, f_{Y|X}(y \,|\, x) \: \textrm{d}y.


$$

Note that $\textrm E\big[Y \,|\, X = x \big]$ is a function of $x.$

The conditional density function of $Y$ given $X=x$ can be computed as

$$


\begin{aligned}𝑓_{𝑌|𝑋}(𝑦\,|\,𝑥) & =\frac{𝑓(𝑥,𝑦)}{𝑓_{𝑋}(𝑥)} \\ & =\frac{2𝑦ln⁡(𝑥)}{ln⁡(𝑥)} \\ & =2𝑦,\end{aligned}


$$

where $1 \leq x \leq e, \: 0 \leq y \leq 1.$ Outside this domain, we have $f_{Y|X} (y \,|\, x) = 0.$

Notice that $f_{Y|X} (y \,|\, x)$ does not depend on $x.$ Therefore, we obtain

$$


\begin{aligned}E[𝑌^{2}\,\,𝑋=1] & =∫_{∞−∞}^{}𝑦^{2}\,𝑓_{𝑌|𝑋}(𝑦\,\,1)\,d𝑦 \\ & =∫_{10}^{}𝑦^{2}⋅2𝑦\,d𝑦 \\ & =∫_{10}^{}2𝑦^{3}d𝑦 \\ & =[\frac{𝑦^{4}}{2}]_{10}^{} \\ & =\frac{1}{2}.\end{aligned}


$$

Finally,

$$


\begin{aligned}Var[𝑌\,\,𝑋=1] & =E[𝑌^{2}\,\,𝑋=1]−𝜇_{2𝑌|1}^{} \\ & =\frac{1}{2}−(\frac{2}{3})^{2} \\ & =\frac{1}{2}−\frac{4}{9} \\ & =\frac{1}{18}.\end{aligned}


$$
