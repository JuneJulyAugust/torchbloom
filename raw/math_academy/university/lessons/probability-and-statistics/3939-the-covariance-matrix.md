# The Covariance Matrix

Source: https://www.mathacademy.com/topics/3939?courseId=73
Topic ID: 3939

## Prerequisites

- [The Correlation Coefficient for Two Random Variables](./3050-the-correlation-coefficient-for-two-random-variables.md)
- [Positive-Definite and Negative-Definite Quadratic Forms](../linear-algebra/3127-positive-definite-and-negative-definite-quadratic-forms.md)

## Lesson

### Introduction

For a set of random variables $X_1, \ldots, X_n,$ the **covariance matrix** $\Sigma$ is defined as

$$


\begin{aligned}Var[𝑋_{1}] & Cov[𝑋_{1},𝑋_{2}] & ⋯ & Cov[𝑋_{1},𝑋_{𝑛}] \\ Cov[𝑋_{2},𝑋_{1}] & Var[𝑋_{2}] & ⋯ & Cov[𝑋_{2},𝑋_{𝑛}] \\ ⋮ & ⋮ & ⋱ & ⋮ \\ Cov[𝑋_{𝑛},𝑋_{1}] & Cov[𝑋_{𝑛},𝑋_{2}] & ⋯ & Var[𝑋_{𝑛}]\end{aligned}


$$

Note the following:

- The $i$th diagonal element is $\Sigma_{ii} = \text{Var}[X_i].$

- The element in the $i$th row and $j$th column for $i \neq j$ is $\Sigma_{ij} = \text{Cov}[X_i, X_j].$

Now, since $\text{Cov}[X_i,X_j] = \text{Cov}[X_j,X_i]$ for any pair of random variables $X_i, X_j$, we have the following theorem:

*The covariance matrix is always symmetric. Moreover, it is a positive semi-definite matrix.*

### Example: Determining Elements of a Covariance Matrix

#### Question

$$


\begin{aligned}4 & 2 & 0 \\ 𝑎 & 5 & 𝑏 \\ 𝑐 & 1 & 2\end{aligned}


$$

The covariance matrix $\Sigma$ for some random variables $X_1, X_2,$ and $X_3$ is given above. Find $a + b + c.$

#### Explanation

For random variables $X_1, \ldots, X_n,$ the covariance matrix $\Sigma$ is given by

$$


\begin{aligned}Var[𝑋_{1}] & Cov[𝑋_{1},𝑋_{2}] & ⋯ & Cov[𝑋_{1},𝑋_{𝑛}] \\ Cov[𝑋_{2},𝑋_{1}] & Var[𝑋_{2}] & ⋯ & Cov[𝑋_{2},𝑋_{𝑛}] \\ ⋮ & ⋮ & ⋱ & ⋮ \\ Cov[𝑋_{𝑛},𝑋_{1}] & Cov[𝑋_{𝑛},𝑋_{2}] & ⋯ & Var[𝑋_{𝑛}]\end{aligned}


$$

That is,

- the $i$th diagonal element is $\Sigma_{ii} = \text{Var}[X_i],$ and

- the element in the $i$th row and $j$th column for $i \neq j$ is $\Sigma_{ij} = \text{Cov}[X_i, X_j].$

Now, note that

$$


\text{Cov}[X,Y] = \text{Cov}[Y,X].


$$

As a result, the covariance matrix is always symmetric (moreover, it is a positive semi-definite matrix).

So, we can find the missing elements as follows:

- $a = \Sigma_{21} = \text{Cov}[X_2,X_1] = \text{Cov}[X_1,X_2] = \Sigma_{12} = 2$

- $b = \Sigma_{23} = \text{Cov}[X_2,X_3] = \text{Cov}[X_3,X_2] = \Sigma_{32} = 1$

- $c = \Sigma_{31} = \text{Cov}[X_3,X_1] = \text{Cov}[X_1,X_3] = \Sigma_{13} = 0$

Therefore, $a + b + c = 2 + 1 +0 = 3.$

### Example: Finding a Covariance Matrix Given Some Moments

#### Question

Consider two random variables $X$ and $Y$ with expectations $\text{E}[X] = 4,$ $\text{E}[Y] = 3,$ mixed moment $\text{E}[XY] = 9,$ and second raw moments $\text{E}[X^2] = 18$ and $\text{E}[Y^2] = 14.$ Find the covariance matrix for $X$ and $Y.$

#### Explanation

For two random variables $X$ and $Y,$ the covariance matrix $\Sigma$ is given by

$$


[\begin{aligned}Var[𝑋] & Cov[𝑋,𝑌] \\ Cov[𝑌,𝑋] & Var[𝑌]\end{aligned}]


$$

Recall that the variance of a random variable $X$ is determined by the formula

$$


\text{Var}[X] = \text{E}[X^2] - \text{E}[X]^2,


$$

and the covariance of two random variables $X$ and $Y$ is given by the formula

$$


\text{Cov}[X,Y] = \text{E}[XY] - \text{E}[X] \cdot \text{E}[Y].


$$

First, let's find $\text{Var}[X]{:}$

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =18−4^{2} \\ & =2\end{aligned}


$$

Similarly,

$$


\begin{aligned}Var[𝑌] & =E[𝑌^{2}]−E[𝑌]^{2} \\ & =14−3^{2} \\ & =5.\end{aligned}


$$

Now lets find $\text{Cov}[X,Y]{:}$

$$


\begin{aligned}Cov[𝑋,𝑌] & =E[𝑋𝑌]−E[𝑋]⋅E[𝑌] \\ & =9−4⋅3 \\ & =−3\end{aligned}


$$

Therefore, the covariance matrix is given by

$$


[\begin{aligned}Var[𝑋] & Cov[𝑋,𝑌] \\ Cov[𝑌,𝑋] & Var[𝑌]\end{aligned}]


$$

### Example: Finding a Covariance Matrix Given a Discrete Bivariate Distribution

#### Question

The joint probability mass function $f(x,y)$ for the discrete random variables $X$ and $Y$ is given below.

Given that $\text{E}[X] = 3$ and $\text{E}[Y] = 2.2,$ find the covariance matrix for $X$ and $Y.$

#### Explanation

For two random variables $X$ and $Y,$ the covariance matrix $\Sigma$ is given by

$$


[\begin{aligned}Var[𝑋] & Cov[𝑋,𝑌] \\ Cov[𝑌,𝑋] & Var[𝑌]\end{aligned}]


$$

Recall that the variance of a random variable $X$ is determined by the formula

$$


\text{Var}[X] = \text{E}[X^2] - \text{E}[X]^2,


$$

and the covariance of two random variables $X$ and $Y$ is given by the formula

$$


\text{Cov}[X,Y] = \text{E}[XY] - \text{E}[X] \cdot \text{E}[Y].


$$

First, let's find the marginal mass functions for $X$ and $Y.$ These are given by the row and column totals, respectively.

Now, we can find $\text{Var}[X].$ If $X$ is defined on a support $S_X,$ then

$$


\begin{aligned}E[𝑋^{2}] & =\underset{𝑥∈𝑆_{𝑋}}{∑}𝑥^{2}⋅𝑓_{𝑋}(𝑥) \\ & =2^{2}⋅0.5+4^{2}⋅0.5 \\ & =10.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =10−3^{2} \\ & =1.\end{aligned}


$$

Similarly, if $Y$ is defined on a support $S_Y,$ then

$$


\begin{aligned}E[𝑌^{2}] & =\underset{𝑦∈𝑆_{𝑦}}{∑}𝑦^{2}⋅𝑓_{𝑌}(𝑦) \\ & =1^{2}⋅0.4+3^{2}⋅0.6 \\ & =5.8.\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑌] & =E[𝑌^{2}]−E[𝑌]^{2} \\ & =5.8−2.2^{2} \\ & =0.96.\end{aligned}


$$

Finally, let's find $\text{Cov}[X,Y].$ By the rule of the lazy statistician, we find $\text{E}[XY]{:}$

$$


\begin{aligned}E[𝑋𝑌] & =\underset{(𝑥,𝑦)∈𝑆}{∑}𝑥𝑦⋅𝑓(𝑥,𝑦) \\ & =(2)(1)𝑓(2,1)+(4)(1)𝑓(4,1)+(2)(3)𝑓(2,3)+(4)(3)𝑓(4,3) \\ & =2⋅0.3+4⋅0.1+6⋅0.2+12⋅0.4 \\ & =7\end{aligned}


$$

Then, using the covariance formula, we have

$$


\begin{aligned}Cov[𝑋,𝑌] & =E[𝑋𝑌]−E[𝑋]⋅E[𝑌] \\ & =7−3⋅2.2 \\ & =0.4.\end{aligned}


$$

Therefore, the covariance matrix is given by

$$


[\begin{aligned}Var[𝑋] & Cov[𝑋,𝑌] \\ Cov[𝑌,𝑋] & Var[𝑌]\end{aligned}]


$$

### Example: Finding a Covariance Matrix Given a Continuous Bivariate Distribution

#### Question

The random variables $X$ and $Y$ have the joint probability density function

$$


\begin{aligned}𝑥+\frac{3}{2}𝑦^{2},\, & 0≤𝑥≤1,\,\,0≤𝑦≤1, \\ 0,\, & otherwise.\end{aligned}


$$

If $\text{E}[X] = \dfrac{7}{12},$ $\text{E}[Y] = \dfrac{5}{8},$ and $\text{E}[XY]=\dfrac{17}{48},$ find the covariance matrix for $X$ and $Y.$

#### Explanation

For two random variables $X$ and $Y,$ the covariance matrix $\Sigma$ is given by

$$


[\begin{aligned}Var[𝑋] & Cov[𝑋,𝑌] \\ Cov[𝑌,𝑋] & Var[𝑌]\end{aligned}]


$$

Recall that the variance of a random variable $X$ is determined by the formula

$$


\text{Var}[X] = \text{E}[X^2] - \text{E}[X]^2,


$$

and the covariance of two random variables $X$ and $Y$ is given by the formula

$$


\text{Cov}[X,Y] = \text{E}[XY] - \text{E}[X] \cdot \text{E}[Y].


$$

First, we find $\text{Var}[X].$ We compute $\text{E}[X^2]$ using the rule of the lazy statistician:

$$


\begin{aligned}E[𝑋^{2}] & =∫_{10}∫_{10}𝑥^{2}⋅𝑓(𝑥,𝑦)\,d𝑥d𝑦 \\ & =∫_{10}∫_{10}𝑥^{2}(𝑥+\frac{3}{2}𝑦^{2})\,d𝑥d𝑦 \\ & =∫_{10}∫_{10}(𝑥^{3}+\frac{3}{2}𝑥^{2}𝑦^{2})d𝑥d𝑦 \\ & =∫_{10}[\frac{1}{4}𝑥^{4}+\frac{1}{2}𝑥^{3}𝑦^{2}]_{𝑥=1𝑥=0}\,d𝑦 \\ & =∫_{10}(\frac{1}{4}+\frac{1}{2}𝑦^{2})d𝑦 \\ & =[\frac{1}{4}𝑦+\frac{1}{6}𝑦^{3}]_{10} \\ & =\frac{1}{4}+\frac{1}{6} \\ & =\frac{5}{12}\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑋] & =E[𝑋^{2}]−E[𝑋]^{2} \\ & =\frac{5}{12}−(\frac{7}{12})^{2} \\ & =\frac{11}{144}.\end{aligned}


$$

Similarly, we compute $\text{E}[Y^2]$ using the rule of the lazy statistician:

$$


\begin{aligned}E[𝑌^{2}] & =∫_{10}∫_{10}𝑦^{2}⋅𝑓(𝑥,𝑦)\,d𝑥d𝑦 \\ & =∫_{10}∫_{10}𝑦^{2}(𝑥+\frac{3}{2}𝑦^{2})\,d𝑥d𝑦 \\ & =∫_{10}∫_{10}(𝑥𝑦^{2}+\frac{3}{2}𝑦^{4})d𝑥d𝑦 \\ & =∫_{10}[\frac{1}{2}𝑥^{2}𝑦^{2}+\frac{3}{2}𝑥𝑦^{4}]_{𝑥=1𝑥=0}\,d𝑦 \\ & =∫_{10}(\frac{1}{2}𝑦^{2}+\frac{3}{2}𝑦^{4})d𝑦 \\ & =[\frac{1}{6}𝑦^{3}+\frac{3}{10}𝑦^{5}]_{10} \\ & =\frac{1}{6}+\frac{3}{10} \\ & =\frac{7}{15}\end{aligned}


$$

Therefore,

$$


\begin{aligned}Var[𝑌] & =E[𝑌^{2}]−E[𝑌]^{2} \\ & =\frac{7}{15}−(\frac{5}{8})^{2} \\ & =\frac{73}{960}.\end{aligned}


$$

Finally, let's find $\text{Cov}[X,Y].$ Using the given results, we have

$$


\begin{aligned}Cov[𝑋,𝑌] & =E[𝑋𝑌]−E[𝑋]⋅E[𝑌] \\ & =\frac{17}{48}−(\frac{7}{12})⋅(\frac{5}{8}) \\ & =−\frac{1}{96}.\end{aligned}


$$

Therefore, the covariance matrix is given by

$$


[\begin{aligned}Var[𝑋] & Cov[𝑋,𝑌] \\ Cov[𝑌,𝑋] & Var[𝑌]\end{aligned}]


$$
