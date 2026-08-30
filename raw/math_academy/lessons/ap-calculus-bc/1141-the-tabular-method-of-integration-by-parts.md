# The Tabular Method of Integration by Parts

Source: https://www.mathacademy.com/topics/1141?courseId=21
Topic ID: 1141

## Prerequisites

- [Applying the Integration By Parts Twice](./416-applying-the-integration-by-parts-twice.md)

## Lesson

### Introduction

Suppose we want to evaluate $\displaystyle \int x^3e^{x/2} \textrm{d}x.$ We can do it by applying integration by parts three times, but the calculation is pretty long. How can we speed it up?

Multiple applications of integration by parts become quick and easy if we use the **tabular method**.

Let's start by picking our $u$ and $\dfrac{\textrm{d}v}{\textrm{d}x}$ as normal:

$$


u = x^3\,,\quad \dfrac{\textrm{d}v}{\textrm{d}x} = e^{x/2}\,.


$$

We put this in a table, as shown below:

To fill in the second row of the table, we differentiate the function in the first column and integrate the function in the second column. Doing this, we find

$$


\dfrac{\textrm{d}}{\textrm{d}x}\left(x^3\right) = 3x^2\,,\quad \int e^{x/2} \textrm{d}x = 2e^{x/2}\,.


$$

Filling in our table, we get the following:

At this step, we begin filling the third column. It always starts with a "$+$" and then the signs alternate at each subsequent step.

We continue by differentiating the expression in the first column and integrating the expression in the second column until we get zero in the first column.

Now we multiply the same-colored terms along with the same-colored sign. Specifically we multiply $ x^3$ with ${ 2e^{x/2}},$ $3x^2$ with $4e^{x/2},$ and so on. We get

Finally, we add up all the terms of the last column to get the answer for our integral. We get

$$


\begin{aligned}∫𝑥^{3}𝑒^{𝑥/2}d𝑥 & =2𝑥^{3}𝑒^{𝑥/2}−12𝑥^{2}𝑒^{𝑥/2}+48𝑥𝑒^{𝑥/2}−96𝑒^{𝑥/2}+𝐶 \\ & =𝑒^{𝑥/2}(2𝑥^{3}−12𝑥^{2}+48𝑥−96)+𝐶.\end{aligned}


$$

### Example: Integrating a Trigonometric Expression Using the Tabular Method of Integration by Parts

#### Question

Evaluate $\displaystyle \int (x^4-3x) \cos(x) \textrm{d}x.$

#### Explanation

For this integral we choose $u = x^4-3x$ and $\dfrac{\textrm{d}v}{\textrm{d}x} = \cos(x).$ Filling in the table gives the following:

We add up all the terms of the last column to get the answer for our integral.

$$


\begin{aligned}∫(𝑥^{4}−3𝑥)cos⁡(𝑥)d𝑥 & =(𝑥^{4}−3𝑥)sin⁡(𝑥)+(4𝑥^{3}−3)cos⁡(𝑥) \\ & =\,\,−12𝑥^{2}sin⁡(𝑥)−24𝑥cos⁡(𝑥)+24sin⁡(𝑥)+𝐶 \\ & =(𝑥^{4}−12𝑥^{2}−3𝑥+24)sin⁡(𝑥) \\ & =\,\,+(4𝑥^{3}−24𝑥−3)cos⁡(𝑥)+𝐶\end{aligned}


$$

### Example: Integrating Algebraic and Exponential Expressions Using the Tabular Method of Integration by Parts

#### Question

Evaluate $\displaystyle \int (x^2-1)(x+2)^5 \textrm{d}x.$

#### Explanation

For this integral, we choose $u = x^2-1$ and $\dfrac{\textrm{d}v}{\textrm{d}x} =(x+2)^5.$ Filling in our table gives the following:

We add up all the terms of the last column to get the answer for our integral.

$$


\begin{aligned}∫(𝑥^{2}−1)(𝑥+2)^{5}d𝑥 & =\frac{(𝑥^{2}−1)(𝑥+2)^{6}}{6}−\frac{𝑥(𝑥+2)^{7}}{21}+\frac{(𝑥+2)^{8}}{168}+𝐶 \\ & =\frac{(𝑥+2)^{6}}{168}(28(𝑥^{2}−1)−8𝑥(𝑥+2)+(𝑥+2)^{2})+𝐶 \\ & =\frac{(𝑥+2)^{6}}{168}(21𝑥^{2}−12𝑥−24)+𝐶\end{aligned}


$$
