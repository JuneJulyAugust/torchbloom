# Calculating Moments Using Moment-Generating Functions

Source: https://www.mathacademy.com/topics/3287?courseId=73
Topic ID: 3287

## Prerequisites

- [Moment-Generating Functions](./3401-moment-generating-functions.md)

## Lesson

### Introduction

Let $X$ be a random variable. The moment-generating function (or MGF) of $X$ is defined as the expected value of $e^{tX}\mathbin{:}$

$$


M(t) = \textrm E\left[e^{tX}\right]


$$

We can use the moment-generating function of $X$ to compute the raw moments of $X.$ Recall that the raw moments are

$$


\textrm E[X],\qquad \textrm E[X^2],\qquad \textrm E[X^3],\qquad \textrm E[X^4], \qquad \ldots\,.


$$

Let's show how to compute $\textrm E[X]$ using an MGF.

Taking the first derivative of $M(t)$ with respect to $t,$ treating $X$ as a parameter, we have

$$


\begin{aligned}𝑀^{′}(𝑡) & =\frac{d}{d𝑡}(E[𝑒^{𝑡𝑋}]) \\ & =E[\frac{d}{d𝑡}(𝑒^{𝑡𝑋})] \\ & =E[𝑋𝑒^{𝑡𝑋}].\end{aligned}


$$

**Note**: We are using here the fact that differentiation with respect to the parameter $t$ can be interchanged with the calculation of the expectation value. The proof of this property for the arbitrary probability distribution goes beyond the scope of our course.

Therefore, for $t=0,$ we have

$$


M'(0)=\textrm E[X].


$$

In other words, we can find the expected value of $X$ by evaluating the first derivative of the MGF at $t=0$.

As an example, let the random variable $X$ have the following probability distribution:

$$


\begin{aligned}\frac{2}{3},\, & 𝑥=0 \\ \frac{1}{3},\, & 𝑥=1\end{aligned}


$$

Then, the MGF of $X$ is given by

$$


\begin{aligned}𝑀(𝑡) & =𝑓(0)𝑒^{0𝑡}+𝑓(1)𝑒^{𝑡} \\ & =\frac{2}{3}+\frac{1}{3}𝑒^{𝑡}.\end{aligned}


$$

Taking the first derivative of the MGF with respect to $t,$ we get

$$


\begin{aligned}𝑀^{′}(𝑡) & =\frac{d}{d𝑡}(\frac{2}{3}+\frac{1}{3}𝑒^{𝑡}) \\ & =\frac{1}{3}𝑒^{𝑡}.\end{aligned}


$$

Therefore,

$$


\textrm E[X] = M'(0) =\dfrac{1}{3}e^{0} = \dfrac13.


$$

### Example: Computing a First Moment Using a Moment-Generating Function

#### Question

Given that the moment-generating function of the random variable $X$ is given by

$$


\% Note: This is an MGF for X~N(1,4) M(t) =e^{t+2t^2},


$$

compute $\textrm E[X].$

#### Explanation

We will use the fact that

$$


\textrm E[X] = M'(0).


$$

Computing the derivative of $M(t),$ we get

$$


\begin{aligned}𝑀^{′}(𝑡) & =(1+4𝑡)𝑒^{𝑡+2𝑡^{2}}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}E[𝑋] & =𝑀^{′}(0) \\ & =(1+4⋅0)𝑒^{0+2⋅0^{2}} \\ & =(1+0)𝑒^{0} \\ & =1.\end{aligned}


$$

### Calculating Second Moments From Moment-Generating Functions

Earlier, we established that

$$


M'(t) = \textrm E\left[Xe^{tX}\right].


$$

Taking the second derivative, we get

$$


\begin{aligned}𝑀^{″}(𝑡) & =\frac{d}{d𝑡}(𝑀^{′}(𝑡)) \\ & =\frac{d}{d𝑡}(E[𝑋𝑒^{𝑡𝑋}]) \\ & =E[\frac{d}{d𝑡}(𝑋𝑒^{𝑡𝑋})] \\ & =E[𝑋^{2}𝑒^{𝑡𝑋}].\end{aligned}


$$

Setting $t=0,$ we have

$$


M''(0)=\textrm E\left[X^2\right].


$$

Therefore, to compute the second raw moment of a random variable $X,$ we evaluate the second derivative of the MGF at $t=0.$

For example, let the random variable $X$ have the following probability distribution:

$$


\begin{aligned}\frac{1}{3}, & 𝑥=0 \\ \frac{1}{3}, & 𝑥=1 \\ \frac{1}{3}, & 𝑥=2\end{aligned}


$$

Then, the MGF is given by

$$


\begin{aligned}𝑀(𝑡) & =𝑓(0)𝑒^{0𝑡}+𝑓(1)𝑒^{1𝑡}+𝑓(2)𝑒^{2𝑡} \\ & =\frac{1}{3}+\frac{1}{3}𝑒^{𝑡}+\frac{1}{3}𝑒^{2𝑡}.\end{aligned}


$$

Taking the first derivative of the MGF, we get

$$


\begin{aligned}𝑀^{′}(𝑡) & =\frac{d}{d𝑡}(\frac{1}{3}+\frac{1}{3}𝑒^{𝑡}+\frac{1}{3}𝑒^{2𝑡}) \\ & =\frac{1}{3}𝑒^{𝑡}+\frac{2}{3}𝑒^{2𝑡}.\end{aligned}


$$

Then, taking the second derivative of the MGF, we get

$$


\begin{aligned}𝑀^{″}(𝑡) & =\frac{d}{d𝑡}(\frac{1}{3}𝑒^{𝑡}+\frac{2}{3}𝑒^{2𝑡}) \\ & =\frac{1}{3}𝑒^{𝑡}+\frac{4}{3}𝑒^{2𝑡}.\end{aligned}


$$

Therefore,

$$


\begin{aligned}E[𝑋^{2}] & =𝑀^{″}(0) \\ & =\frac{1}{3}𝑒^{0}+\frac{4}{3}𝑒^{0} \\ & =\frac{1}{3}+\frac{4}{3} \\ & =\frac{5}{3}.\end{aligned}


$$

### Example: Computing the Second Moment Given a Moment-Generating Function

#### Question

Given that the moment-generating function (MGF) of the random variable $X$ is given by

$$


\% Note: This is an MGF for X~NB(3,1/2) M(t) = \left(\dfrac{e^t}{2 - e^t}\right)^3, \qquad t < \ln 2 ,


$$

compute $\textrm E[X^2].$

#### Explanation

We will use the fact that

$$


\textrm E[X^2] = M''(0).


$$

First, let's rewrite the function $M(t)$ as follows:

$$


M(t) = \dfrac{e^{3t}}{\left(2 - e^t\right)^3}


$$

We compute the derivatives of $M(t)$ using the quotient rule.

Computing $M'(t),$ we get

$$


\begin{aligned}𝑀^{′}(𝑡) & =\frac{(𝑒^{3𝑡})^{′}(2−𝑒^{𝑡})^{3}−(𝑒^{3𝑡})[(2−𝑒^{𝑡})^{3}]^{′}}{[(2−𝑒^{𝑡})^{3}]^{2}} \\ & =\frac{3𝑒^{3𝑡}(2−𝑒^{𝑡})^{3}−(𝑒^{3𝑡})⋅3(−𝑒^{𝑡})(2−𝑒^{𝑡})^{2}}{(2−𝑒^{𝑡})^{6}} \\ & =\frac{3𝑒^{3𝑡}(2−𝑒^{𝑡})−(𝑒^{3𝑡})⋅3(−𝑒^{𝑡})}{(2−𝑒^{𝑡})^{4}} \\ & =\frac{6𝑒^{3𝑡}−3𝑒^{4𝑡}+3𝑒^{4𝑡}}{(2−𝑒^{𝑡})^{4}} \\ & =\frac{6𝑒^{3𝑡}}{(2−𝑒^{𝑡})^{4}}.\end{aligned}


$$

Computing $M''(t),$ we get

$$


\begin{aligned}𝑀^{″}(𝑡) & =\frac{(6𝑒^{3𝑡})^{′}(2−𝑒^{𝑡})^{4}−6𝑒^{3𝑡}[(2−𝑒^{𝑡})^{4}]^{′}}{[(2−𝑒^{𝑡})^{4}]^{2}} \\ & =\frac{18𝑒^{3𝑡}(2−𝑒^{𝑡})^{4}−6𝑒^{3𝑡}⋅4(−𝑒^{𝑡})(2−𝑒^{𝑡})^{3}}{(2−𝑒^{𝑡})^{8}} \\ & =\frac{18𝑒^{3𝑡}(2−𝑒^{𝑡})−6𝑒^{3𝑡}⋅4(−𝑒^{𝑡})}{(2−𝑒^{𝑡})^{5}} \\ & =\frac{18𝑒^{3𝑡}(2−𝑒^{𝑡})+24𝑒^{4𝑡}}{(2−𝑒^{𝑡})^{5}} \\ & =\frac{6𝑒^{3𝑡}[3(2−𝑒^{𝑡})+4𝑒^{𝑡}]}{(2−𝑒^{𝑡})^{5}} \\ & =\frac{6𝑒^{3𝑡}(6+𝑒^{𝑡})}{(2−𝑒^{𝑡})^{5}}.\end{aligned}


$$

Finally,

$$


\begin{aligned}E[𝑋^{2}] & =𝑀^{″}(0) \\ & =\frac{6𝑒^{0}(6+𝑒^{0})}{(2−𝑒^{0})^{5}} \\ & =\frac{6(6+1)}{(2−1)^{5}} \\ & =42.\end{aligned}


$$

### Calculating General Moments From Moment-Generating Functions

In general, we can find the $k$th moment raw moment of the random variable $X$ by evaluating the $k$th derivative of the moment-generating function of $X$ at $t=0.$

$$


\textrm E\left[X^k\right] = M^{(k)}(0).


$$

Sometimes, we can find a general formula for the $k$th moment. Let's see an example.

### Example: Computing the General Moment Given a Moment-Generating Function

#### Question

Given that the moment-generating function (MGF) of the random variable $X$ is given by

$$


\% Note: This is an MGF for X~B(2, 1/2) M(t) = \left( \dfrac{3}{4} + \dfrac{1}{4} e^t \right)^2,


$$

compute $\textrm E[X^k],$ where $k$ is a positive integer.

#### Explanation

In general, if $M(t)$ is the moment-generating function of a random variable $X,$ we have

$$


\textrm E[X^k] = M^{(k)}(0).


$$

First, we express $M(t)$ in a form that is easy to differentiate:

$$


M(t) = \dfrac{1}{16} ( 9 + 6 e^t + e^{2t})


$$

Computing the first few derivatives of $M(t),$ we get

$$


\begin{aligned}𝑀^{′}(𝑡) & =\frac{1}{8}(3𝑒^{𝑡}+𝑒^{2𝑡}) \\ 𝑀^{″}(𝑡) & =\frac{1}{8}(3𝑒^{𝑡}+2𝑒^{2𝑡}) \\ 𝑀^{(3)}(𝑡) & =\frac{1}{8}(3𝑒^{𝑡}+2^{2}𝑒^{2𝑡}) \\ 𝑀^{(4)}(𝑡) & =\frac{1}{8}(3𝑒^{𝑡}+2^{3}𝑒^{2𝑡}).\end{aligned}


$$

So for $k\geq 1,$ we have the following pattern:

$$


M^{(k)}(t) =\dfrac{1}{8}(3 e^t+2^{k-1} e^{2t})


$$

Finally, then,

$$


\begin{aligned}E[𝑋^{𝑘}] & =𝑀^{(𝑘)}(0) \\ & =\frac{1}{8}(3𝑒^{0}+2^{𝑘−1}𝑒^{0}) \\ & =\frac{1}{8}(3+2^{𝑘−1}).\end{aligned}


$$
