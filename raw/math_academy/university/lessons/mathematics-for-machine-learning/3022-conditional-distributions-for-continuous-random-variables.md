# Conditional Distributions for Continuous Random Variables

Source: https://www.mathacademy.com/topics/3022?courseId=145
Topic ID: 3022

## Prerequisites

- [Conditional Distributions for Discrete Random Variables](./3003-conditional-distributions-for-discrete-random-variables.md)
- [Independence of Continuous Random Variables](./3863-independence-of-continuous-random-variables.md)

## Lesson

### Introduction

We can easily extend the notion of conditional probability distributions for discrete random variables to continuous random variables.

For continuous random variables $X$ and $Y,$ the **conditional probability density function of $X$ given $Y = y$** is given by

$$


f_{X|Y} (x|y) =\dfrac{f(x, y)}{f_Y (y)}, \qquad f_Y(y) \neq 0,


$$

and the conditional probability density function of $Y$ given $X = x$ is given by

$$


f_{Y|X} (y|x) =\dfrac{f(x, y)}{f_X (x)}, \qquad f_X(x) \neq 0.


$$

Notice that these definitions are analogous to those for discrete random variables.

To compute probabilities, we work directly with these conditional PDFs. For example, to calculate the **conditional probability of $X$ given $Y,$** we use

$$


P(X \in A|Y = y) =\int_A f_{X|Y} (x|y)\, \textrm dx.


$$

In general, the conditional distribution of $X$ given $Y$ does not equal the conditional distribution of $Y$ given $X$. That is

$$


f_{X|Y}(x|y) \ne f_{Y|X}(y|x).


$$

Finally, if $X$ and $Y$ are independent, then

$$


f_{X|Y}(x|y)=f_X(x),\qquad f_{Y|X}(y|x)=f_Y(y).


$$

### Example: Working With the Definition of a Conditional PDF

#### Question

$$


\begin{aligned}\frac{3(𝑥^{2}+𝑦^{2})}{3𝑥^{2}+1}, & 0≤𝑥≤1,\,0≤𝑦≤1 \\ 0, & otherwise\end{aligned}


$$

Consider the continuous random variables $X$ and $Y,$ for which the conditional probability density function $f_{Y \,|\, X}(y \,|\, x)$ and the marginal density function $f_X(x)$ are shown above. Find the expression of the joint probability density function $f(x,y)$ for $0 \leq x \leq 1, \: 0 \leq y \leq 1.$

#### Explanation

Recall that the conditional probability density function of $Y$ given $X=x$ for two continuous random variables $X$ and $Y$ is given by

$$


f_{Y \,|\, X}(y \,|\, x) =\dfrac{f(x, y)}{f_X (x)},


$$

where

- $f(x,y)$ is the joint probability density function for $X$ and $Y,$ and

- $f_X (x)$ is the marginal density function for $X.$

From the equation above, it follows that

$$


f(x,y) = f_{Y \,|\, X}(y \,|\, x) \cdot f_X (x).


$$

Now, for $0 \leq x \leq 1, \: 0 \leq y \leq 1,$ we have

$$


\begin{aligned}𝑓(𝑥,𝑦) & =𝑓_{𝑌\,|\,𝑋}(𝑦\,|\,𝑥)⋅𝑓_{𝑋}(𝑥) \\ & =\frac{3(𝑥^{2}+𝑦^{2})}{3𝑥^{2}+1}⋅\frac{3𝑥^{2}+1}{2} \\ & =\frac{3(𝑥^{2}+𝑦^{2})}{2}.\end{aligned}


$$

For other values of $x$ and $y,$ the function $f_{Y \,|\, X}(y \,|\, x)$ equals $0.$ As a result, the product will be equal to $0$ too.

Therefore, the joint probability density function is the following:

$$


\begin{aligned}\frac{3(𝑥^{2}+𝑦^{2})}{2}, & 0≤𝑥≤1,\,0≤𝑦≤1 \\ 0, & otherwise\end{aligned}


$$

### Example: Finding a Conditional PDF

#### Question

Let $X$ and $Y$ be two continuous random variables with the following joint probability density function:

$$


\begin{aligned}𝑥+𝑦, & \,0≤𝑥≤1,\,0≤𝑦≤1 \\ 0, & \,otherwise\end{aligned}


$$

Find the expression of the conditional probability density function $f_{X \,|\, Y} (x \,|\, y)$ for $0 \leq x \leq 1, \: 0 \leq y \leq 1.$

#### Explanation

Using the formula for the marginal density function for $Y,$ we have

$$


\begin{aligned}𝑓_{𝑌}(𝑦) & =∫_{∞−∞}𝑓(𝑥,𝑦)\,d𝑥 \\ & =∫_{10}(𝑥+𝑦)\,d𝑥 \\ & =[\frac{𝑥^{2}}{2}+𝑥𝑦]_{𝑥=1𝑥=0} \\ & =\frac{1}{2}+𝑦−0 \\ & =\frac{2𝑦+1}{2}.\end{aligned}


$$

So, the full expression for $f_Y(y)$ is the following:

$$


\begin{aligned}\frac{2𝑦+1}{2}, & \,0≤𝑦≤1 \\ 0, & \,otherwise\end{aligned}


$$

Now recall that the conditional probability density function of $X$ given $Y=y$ for two continuous random variables $X$ and $Y$ is given by

$$


f_{X \,|\, Y} (x \,|\, y) = \dfrac{f(x, y)}{f_Y (y)},


$$

where

- $f(x,y)$ is the joint probability density function for $X$ and $Y,$ and

- $f_Y(y)$ is the marginal density function for $Y.$

Now, for $0 \leq x \leq 1, \: 0 \leq y \leq 1,$ we have

$$


\begin{aligned}𝑓_{𝑋\,|\,𝑌}(𝑥\,|\,𝑦) & =\frac{𝑓(𝑥,𝑦)}{𝑓_{𝑌}(𝑦)} \\ & =\frac{𝑥+𝑦}{(\frac{2𝑦+1}{2})} \\ & =\frac{2(𝑥+𝑦)}{2𝑦+1}.\end{aligned}


$$

For other values of $x$ and $y,$ the function $f(x,y)$ equals $0.$ As a result, $f_{X \,|\, Y}(x \,|\, y)$ will be equal to $0$ too.

Therefore, the conditional probability density function is the following:

$$


\begin{aligned}\frac{2(𝑥+𝑦)}{2𝑦+1}, & \,0≤𝑥≤1,\,0≤𝑦≤1 \\ 0, & \,otherwise\end{aligned}


$$

### Example: Computing a Conditional Probability

#### Question

Let $X$ and $Y$ be two continuous random variables with the following joint probability density function:

$$


\begin{aligned}8𝑥^{2}𝑦, & \,0<𝑥≤1,\,0≤𝑦≤\sqrt{𝑥} \\ 0, & \,otherwise\end{aligned}


$$

Find $P \left(Y < \dfrac{1}{2} \,\bigg|\, X=1\right).$

#### Explanation

Recall that

$$


P(Y \in A \,|\, X = x) = \int_A f_{Y \,|\, X} (y \,|\, x) \, \text{d}y,


$$

where $f_{Y \,|\, X} (y \,|\,x)$ is the conditional probability density function.

Using the formula for the marginal density function for $X,$ we have

$$


\begin{aligned}𝑓_{𝑋}(𝑥) & =∫_{∞−∞}𝑓(𝑥,𝑦)\,d𝑦 \\ & =∫_{\sqrt{𝑥}0}^{}8𝑥^{2}𝑦\,d𝑦 \\ & =8𝑥^{2}∫_{\sqrt{𝑥}0}^{}𝑦\,d𝑦 \\ & =8𝑥^{2}[\frac{1}{2}𝑦^{2}]_{\sqrt{𝑥}0}^{} \\ & =4𝑥^{2}(\sqrt{𝑥})^{2}−0 \\ & =4𝑥^{3}.\end{aligned}


$$

So, the full expression for $f_X(x)$ is the following:

$$


\begin{aligned}4𝑥^{3}, & \,0<𝑥≤1 \\ 0, & \,otherwise\end{aligned}


$$

Now recall that the conditional probability density function for two continuous random variables $X$ and $Y$ is given by

$$


f_{Y \,|\, X} (y \,|\, x) =\dfrac{f(x, y)}{f_X (x)}


$$

where

- $f(x,y)$ is the joint probability density function for $X$ and $Y,$ and

- $f_X (x)$ is the marginal density function for $X.$

Now, for $0< x \leq 1, \: 0 \leq y \leq \sqrt{x},$ we have

$$


\begin{aligned}𝑓_{𝑌\,|\,𝑋}(𝑦\,|\,𝑥) & =\frac{𝑓(𝑥,𝑦)}{𝑓_{𝑋}(𝑥)} \\ & =\frac{8𝑥^{2}𝑦}{4𝑥^{3}} \\ & =\frac{2𝑦}{𝑥}.\end{aligned}


$$

For other values of $x$ and $y,$ the function $f(x,y)$ equals $0.$ As a result, $f_{Y \,|\, X} (y \,|\, x)$ will be equal to $0$ too.

Therefore, the conditional probability density function is the following:

$$


\begin{aligned}\frac{2𝑦}{𝑥}, & \,0<𝑥≤1,\,0≤𝑦≤\sqrt{𝑥} \\ 0, & \,otherwise\end{aligned}


$$

Finally, we compute our probability:

$$


\begin{aligned}𝑃(𝑌<\frac{1}{2}\,\,𝑋=1) & =∫_{1/20}𝑓_{𝑌\,|\,𝑋}(𝑦\,\,𝑥=1)d𝑦 \\ & =∫_{1/20}\frac{2𝑦}{1}d𝑦 \\ & =∫_{1/20}2𝑦\,d𝑦 \\ & =[𝑦^{2}]_{1/20} \\ & =\frac{1}{4}−0 \\ & =\frac{1}{4}.\end{aligned}


$$
