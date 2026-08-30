# Newton's Method for Optimizing Single-Variable Functions

Source: https://www.mathacademy.com/topics/2926?courseId=105
Topic ID: 2926

## Prerequisites

- [Newton's Method](./912-newton-s-method.md)

## Lesson

### Introduction

In a previous lesson, we learned how to *find the roots* of a function using *Newton’s method*. That is, we solved equations of the form

$$


f(x) = 0,


$$

by starting with an initial guess and refining it step by step using the update rule

$$


x_{n+1} = x_n - \dfrac{f(x_n)}{f'(x_n)}.


$$

Now, we turn to a closely related problem of *finding a local minimum or maximum* of a function $f(x)$. Recall that these may occur at points where the derivative $f'(x)$ is equal to zero. In other words, we are looking for the roots of the function's derivative.

Earlier, we approximated the function by a straight line near our current guess. Here, instead of using a linear approximation, we assume that the function $f(x)$ behaves like a *parabola* near our current guess. That’s a reasonable assumption if $f$ is smooth.

To make this idea precise, we use a second-order Taylor approximation, $F(x){:}$

$$


F(x) = f(x_n) + f'(x_n)(x - x_n) + \dfrac{1}{2} f''(x_n)(x - x_n)^2


$$

To find the minimum or maximum, we first need to take the derivative of this approximation, which is

$$


F'(x) = f'(x_n) + f''(x_n)(x - x_n).


$$

We then need to set $F'(x) =0$:

$$


f'(x_n) + f''(x_n)(x - x_n) = 0


$$

Finally, we solve for $x,$ as follows:

$$


\begin{aligned}𝑓^{″}(𝑥_{𝑛})(𝑥−𝑥_{𝑛}) & =−𝑓^{′}(𝑥_{𝑛}) \\ 𝑥−𝑥_{𝑛} & =−\frac{𝑓^{′}(𝑥_{𝑛})}{𝑓^{″}(𝑥_{𝑛})} \\ 𝑥 & =𝑥_{𝑛}−\frac{𝑓^{′}(𝑥_{𝑛})}{𝑓^{″}(𝑥_{𝑛})}\end{aligned}


$$

So, just like in root-finding, we start with an initial guess and improve it step by step. But this time, we apply Newton’s method to the derivative $f'(x)$ instead of the function $f(x)$ itself:

$$


x_{n+1} = x_n - \dfrac{f'(x_n)}{f''(x_n)}


$$

**Note**: The second derivative $f''(x_n)$ must not be zero. If it is zero, or even very close to zero, the update step can become extremely large, leading us far away from the solution.

Just like in root-finding, Newton’s method works best when the function is smooth, and our initial guess is already close to the minimum or maximum.

### A Worked Example

Suppose we wish to find a critical point of the function

$$


f(x)= \ln(x+1)+\dfrac{2}{x+1}


$$

in the interval $[0,2].$ Let's calculate one iteration of the Newton-Raphson process for optimization starting at the point $x_0=0.8.$

The Newton-Raphson process for optimization is

$$


x_{n+1} = x_n - \dfrac{f'(x_n)}{f''(x_n)},


$$

where $f'(x_n)$ and $f''(x_n)$ are the first and second derivatives of $f(x)$ evaluated at $x_n,$ respectively.

In our case, we have

$$


\begin{aligned}𝑓^{′}(𝑥) & =(ln⁡(𝑥+1)+\frac{2}{𝑥+1})^{′} \\ & =\frac{1}{𝑥+1}−\frac{2}{(𝑥+1)^{2}} \\ & =\frac{𝑥−1}{(𝑥+1)^{2}}, \\ 𝑓^{″}(𝑥) & =(\frac{1}{𝑥+1}−\frac{2}{(𝑥+1)^{2}})^{′} \\ & =−\frac{1}{(𝑥+1)^{2}}+\frac{4}{(𝑥+1)^{3}} \\ & =\frac{3−𝑥}{(𝑥+1)^{3}}.\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


\begin{aligned}𝑥_{𝑛+1} & =𝑥_{𝑛}−\frac{\frac{𝑥_{𝑛}−1}{(𝑥_{𝑛}+1)^{2}}}{(𝑥_{𝑛}+1)^{2}} \\ & =𝑥_{𝑛}−\frac{𝑥_{2𝑛}−1}{3−𝑥_{𝑛}}.\end{aligned}


$$

Starting with $x_0=0.8,$ we have

$$


\begin{aligned}𝑥_{1} & =𝑥_{0}−\frac{𝑥_{20}−1}{3−𝑥_{0}} \\ & =0.8−\frac{(0.8)^{2}−1}{3−0.8} \\ & ≈0.964,\end{aligned}


$$

rounded to three decimal places.

### Example: Computing One Iteration of the Newton-Raphson Method for Optimization

#### Question

Suppose we wish to find a critical point of the function $f(x)=x^2 + e^{-2x}$ in the interval $[0,1].$ Calculate one iteration of the Newton-Raphson process for optimization starting at the point $x_0=0.5.$ Round your final answer to $3$ decimal places if needed.

#### Explanation

The Newton-Raphson process for optimization is

$$


x_{n+1} = x_n - \dfrac{f'(x_n)}{f''(x_n)},


$$

where $f'(x_n)$ and $f''(x_n)$ are the first and second derivatives of $f(x)$ evaluated at $x_n,$ respectively.

In our case, we have

$$


\begin{aligned}𝑓^{′}(𝑥) & =(𝑥^{2}+𝑒^{−2𝑥})^{′} \\ & =2𝑥−2𝑒^{−2𝑥}, \\ 𝑓^{″}(𝑥) & =(2𝑥−2𝑒^{−2𝑥})^{′} \\ & =2+4𝑒^{−2𝑥}.\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


\begin{aligned}𝑥_{𝑛+1}=𝑥_{𝑛}−\frac{2𝑥_{𝑛}−2𝑒^{−2𝑥_{𝑛}}}{2+4𝑒^{−2𝑥_{𝑛}}}.\end{aligned}


$$

Starting with $x_0=0.5,$ we have

$$


\begin{aligned}𝑥_{1} & =𝑥_{0}−\frac{2𝑥_{0}−2𝑒^{−2𝑥_{0}}}{2+4𝑒^{−2𝑥_{0}}} \\ & =0.5−\frac{2(0.5)−2𝑒^{−2(0.5)}}{2+4𝑒^{−2(0.5)}} \\ & ≈0.424,\end{aligned}


$$

rounded to three decimal places.

### Example: Computing Two Iterations of the Newton-Raphson Method for Optimization

#### Question

Suppose we wish to find a critical point of the function $f(x)=x^3-6x^2+9x$ in the interval $[0,2].$ Calculate the first two iterations of the Newton-Raphson process for optimization starting at the point $x_0=0.$

#### Explanation

The Newton-Raphson process for optimization is

$$


x_{n+1} = x_n - \dfrac{f'(x_n)}{f''(x_n)},


$$

where $f'(x_n)$ and $f''(x_n)$ are the first and second derivatives of $f(x)$ evaluated at $x_n,$ respectively.

In our case, we have

$$


\begin{aligned}𝑓^{′}(𝑥) & =(𝑥^{3}−6𝑥^{2}+9𝑥)^{′}=3𝑥^{2}−12𝑥+9, \\ 𝑓^{″}(𝑥) & =(3𝑥^{2}−12𝑥+9)^{′}=6𝑥−12.\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


\begin{aligned}𝑥_{𝑛+1} & =𝑥_{𝑛}−\frac{3𝑥_{2𝑛}−12𝑥_{𝑛}+9}{6𝑥_{𝑛}−12}.\end{aligned}


$$

Starting with $x_0=0,$ we have

$$


\begin{aligned}𝑥_{1} & =𝑥_{0}−\frac{3𝑥_{20}−12𝑥_{0}+9}{6𝑥_{0}−12} \\ & =0−\frac{3(0)^{2}−12(0)+9}{6(0)−12} \\ & =\frac{9}{12} \\ & =0.75\end{aligned}


$$

For the second iteration, we have

$$


\begin{aligned}𝑥_{2} & =𝑥_{1}−\frac{3𝑥_{21}−12𝑥_{1}+9}{6𝑥_{1}−12} \\ & =0.75−\frac{3(0.75)^{2}−12(0.75)+9}{6(0.75)−12} \\ & =0.975\end{aligned}


$$

Therefore, $x_1 = 0.75$ and $x_2 = 0.975.$

### Example: Finding the Critical Points of a Function Using the Newton-Raphson Method for Optimization

#### Question

Given that the function $f(x)=x^4-3x+1$ has a critical point in the interval $[0,2],$ use the Newton-Raphson process for optimization starting from $x_0=1$ to estimate the critical point. Round your final answer to two decimal places.

#### Explanation

The Newton-Raphson process for optimization is

$$


x_{n+1} = x_n - \dfrac{f'(x_n)}{f''(x_n)},


$$

where $f'(x_n)$ and $f''(x_n)$ are the first and second derivatives of $f(x)$ evaluated at $x_n,$ respectively.

In our case, we have

$$


\begin{aligned}𝑓^{′}(𝑥) & =(𝑥^{4}−3𝑥+1)^{′}=4𝑥^{3}−3, \\ 𝑓^{″}(𝑥) & =(4𝑥^{3}−3)^{′}=12𝑥^{2}.\end{aligned}


$$

Therefore, our Newton-Raphson formula is

$$


\begin{aligned}𝑥_{𝑛+1} & =𝑥_{𝑛}−\frac{4𝑥_{3𝑛}−3}{12𝑥_{2𝑛}} \\ & =\frac{12𝑥_{3𝑛}−(4𝑥_{3𝑛}−3)}{12𝑥_{2𝑛}} \\ & =\frac{8𝑥_{3𝑛}+3}{12𝑥_{2𝑛}}\end{aligned}


$$

Starting with $x_0 = 1,$ we have

$$


\begin{aligned}𝑥_{1} & =\frac{8𝑥_{30}+3}{12𝑥_{20}} \\ & =\frac{8(1)^{3}+3}{12(1)^{2}} \\ & =0.916\,666….\end{aligned}


$$

Similarly, we have

$$


\begin{aligned}𝑥_{2} & =\frac{8𝑥_{31}+3}{12𝑥_{21}} \\ & =\frac{8(0.916\,666…)^{3}+3}{12(0.916\,666…)^{2}} \\ & =0.908\,631…, \\ 𝑥_{3} & =\frac{8𝑥_{32}+3}{12𝑥_{22}} \\ & =\frac{8(0.908\,631…)^{3}+3}{12(0.908\,631…)^{2}} \\ & =0.908\,560….\end{aligned}


$$

Notice that the last two approximations $x_2 \approx0.91$ and $x_3 \approx 0.91$ are the same when rounded to two decimal places.

Therefore, the critical point of the function is $x \approx 0.91,$ rounded to two decimal places.
