# Conditional Variance for Discrete Random Variables

Source: https://www.mathacademy.com/topics/3926?courseId=145
Topic ID: 3926

## Prerequisites

- [Variance of Discrete Random Variables](./1388-variance-of-discrete-random-variables.md)
- [Conditional Expectation for Discrete Random Variables](./3053-conditional-expectation-for-discrete-random-variables.md)

## Lesson

### Introduction

Suppose that $X$ and $Y$ are discrete random variables, where the conditional expected value of $X$ given $Y=y$ is given by $\mu_{X|y}.$ In other words,

$$


\textrm{E}[X\,|\,Y=y] = \mu_{X|y}.


$$

The **conditional variance of $X$ given $Y=y$** is defined as

$$


\textrm{Var}[X\,|\,Y=y] = \textrm{E}\big[(X - \mu_{X|y} \big)^2 \,|\, Y=y].


$$

This is similar to the definition of $\textrm{Var}[X]$ in that it represents the average (squared) distance of the random variable $X$ from the mean. The difference here is that the expected values are now dependent on the outcome of $Y.$

Similarly to the case of $\textrm{Var}[X],$ this often isn't the easiest formula to use in practice. However, it can be shown that the definition of conditional variance is equivalent to

$$


\begin{aligned}Var[𝑋\,|\,𝑌=𝑦] & =E[𝑋^{2}\,|\,𝑌=𝑦]−𝜇_{2𝑋|𝑦}^{} \\ & =[\underset{𝑥}{∑}𝑥^{2}\,𝑓_{𝑋|𝑌}(𝑥\,|\,𝑦)]−𝜇_{2𝑋|𝑦}^{},\end{aligned}


$$

where $f_{X|Y}(x \,|\, y)$ is the conditional PMF of $X$ given $Y.$ Note that these formulas are analogous to those for $\textrm{Var}[X].$

Finally, we have an analogous definition for the conditional variance of $Y$ given $X=x\mathbin{:}$

$$


\begin{aligned}Var[𝑌\,|\,𝑋=𝑥] & =E[(𝑌−𝜇_{𝑌|𝑥})^{2}\,|\,𝑋=𝑥] \\ & =E[𝑌^{2}\,|\,𝑋=𝑥]−𝜇_{2𝑌|𝑥}^{} \\ & =[\underset{𝑦}{∑}𝑦^{2}\,𝑓_{𝑌|𝑋}(𝑦\,|\,𝑥)]−𝜇_{2𝑌|𝑥}^{}\end{aligned}


$$

### Example: Calculating a Conditional Variance Given a Conditional Mass Function

#### Question

Suppose $X$ and $Y$ are discrete random variables. Find $\textrm{Var}\big[Y \,|\, X=3\big]$ given that the conditional probability mass function $f_{Y|X}(y \,|\, 3)$ is shown in the table above and the corresponding conditional expected value is $\mu_{Y|3} = \dfrac{8}{3}.$

#### Explanation

Recall that the conditional variance of $Y$ given $X=x$ is defined by

$$


\begin{aligned}Var[𝑌\,|\,𝑋=𝑥] & =E[(𝑌−𝜇_{𝑌|𝑥})^{2}\,|\,𝑋=𝑥] \\ & =E[𝑌^{2}\,|\,𝑋=𝑥]−𝜇_{2𝑌|𝑥}^{} \\ & =[\underset{𝑦}{∑}𝑦^{2}\,𝑓_{𝑌|𝑋}(𝑦\,|\,𝑥)]−𝜇_{2𝑌|𝑥}^{}.\end{aligned}


$$

Therefore, we obtain

$$


\begin{aligned}Var[𝑌\,|\,𝑋=3] & =[\underset{𝑦}{∑}𝑦^{2}\,𝑓_{𝑌|𝑋}(𝑦\,|\,3)]−𝜇_{2𝑌|3}^{} \\ & =[(1)^{2}⋅\frac{1}{3}+(2)^{2}⋅\frac{1}{6}+(4)^{2}⋅\frac{1}{2}]−(\frac{8}{3})^{2} \\ & =\frac{1}{3}+\frac{2}{3}+8−\frac{64}{9} \\ & =\frac{17}{9}.\end{aligned}


$$

### Example: Calculating a Conditional Variance Using Row Totals

#### Question

Suppose $X$ and $Y$ are discrete random variables. Find $\textrm{Var}\big[Y \,|\, X=1\big]$ given that $X$ and $Y$ have the joint probability mass function $f(x,y)$ shown in the table above and the corresponding conditional expected value is $\mu_{Y|1} = \dfrac{9}{4}.$

#### Explanation

Recall that the conditional variance of $Y$ given $X=x$ is defined by

$$


\begin{aligned}Var[𝑌\,|\,𝑋=𝑥] & =E[(𝑌−𝜇_{𝑌|𝑥})^{2}\,|\,𝑋=𝑥] \\ & =E[𝑌^{2}\,|\,𝑋=𝑥]−𝜇_{2𝑌|𝑥}^{} \\ & =[\underset{𝑦}{∑}𝑦^{2}\,𝑓_{𝑌|𝑋}(𝑦\,|\,𝑥)]−𝜇_{2𝑌|𝑥}^{}.\end{aligned}


$$

In order to find $f_{Y | X}(y \,|\, x),$ let's first find the marginal distribution for $X,$ corresponding to the row totals:

The conditional probability mass function of $Y$ given that $X=x$ is

$$


f_{Y | X}(y \,|\, x) = \dfrac{f(x,y)}{f_X(x)}.


$$

Therefore, dividing each joint probability by the corresponding row total, we obtain the conditional probability mass function of $Y$ given that $X=x{:}$

Finally, we obtain

$$


\begin{aligned}Var[𝑌\,|\,𝑋=1] & =[\underset{𝑦}{∑}𝑦^{2}\,𝑓_{𝑌|𝑋}(𝑦\,|\,1)]−𝜇_{2𝑌|1}^{} \\ & =[1^{2}⋅\frac{1}{4}+2^{2}⋅\frac{1}{4}+3^{2}⋅\frac{1}{2}]−(\frac{9}{4})^{2} \\ & =\frac{1}{4}+1+\frac{9}{2}−\frac{81}{16} \\ & =\frac{11}{16}.\end{aligned}


$$

### Example: Calculating a Conditional Variance Using Column Totals

#### Question

Suppose $X$ and $Y$ are discrete random variables. Find $\textrm{Var}\big[X \,|\, Y=2\big]$ given that the random variables $X$ and $Y$ have the joint probability mass function $f(x,y)$ shown in the table above and the corresponding conditional expected value is $\mu_{X|2}=\dfrac{10}{9}.$

#### Explanation

Recall that the conditional variance of $X$ given $Y=y$ is defined by

$$


\begin{aligned}Var[𝑋\,|\,𝑌=𝑦] & =E[(𝑋−𝜇_{𝑋|𝑦})^{2}\,|\,𝑌=𝑦] \\ & =E[𝑋^{2}\,|\,𝑌=𝑦]−𝜇_{2𝑋|𝑦}^{} \\ & =[\underset{𝑥}{∑}𝑥^{2}\,𝑓_{𝑋|𝑌}(𝑥\,|\,𝑦)]−𝜇_{2𝑋|𝑦}^{}.\end{aligned}


$$

In order to find $f_{X | Y}(x \,|\, y),$ let's first find the marginal distribution of $Y,$ corresponding to the column totals:

The conditional probability mass function of $X$ given that $Y=y$ is

$$


f_{X | Y}(x \,|\, y) = \dfrac{f(x,y)}{f_Y(y)}.


$$

Therefore, dividing each joint probability by the corresponding column total, we obtain the conditional probability mass function of $X$ given that $Y=y{:}$

Finally, we obtain

$$


\begin{aligned}Var[𝑋\,|\,𝑌=2] & =[\underset{𝑥}{∑}𝑥^{2}\,𝑓_{𝑋|𝑌}(𝑥\,|\,2)]−𝜇_{2𝑋|2}^{} \\ & =[1^{2}⋅\frac{8}{9}+2^{2}⋅\frac{1}{9}]−(\frac{10}{9})^{2} \\ & =\frac{8}{9}+\frac{4}{9}−\frac{100}{81} \\ & =\frac{8}{81}.\end{aligned}


$$
