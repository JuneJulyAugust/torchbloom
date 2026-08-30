# The Zero Product Rule for Solving Polynomial Equations

Source: https://www.mathacademy.com/topics/6103?courseId=120
Topic ID: 6103

## Prerequisites

- [Multiplying Polynomials](../../../high-school/traditional/lessons/algebra-i/361-multiplying-polynomials.md)
- [The Zero Product Rule for Solving Quadratic Equations](../../../high-school/traditional/lessons/algebra-i/1424-the-zero-product-rule-for-solving-quadratic-equations.md)

## Lesson

### Introduction

Recall that the *zero product rule* states that if $ab = 0,$ then $a=0$ or $b=0.$ A similar rule also works for three or more factors.

In particular, if

$$


a\cdot b \cdot c = 0,


$$

then

$$


a=0 \qquad\text{or}\qquad b=0 \qquad\text{or}\qquad c=0.


$$

In other words, if we know that the product of several expressions is zero, then at least one of these expressions must be zero.

Let's see how this can be used to solve polynomial equations. For example, let's consider the equation

$$


(x + 12)(x - 10)(x - 11) = 0.


$$

To solve it, we apply the zero product rule. So, we set each factor equal to zero:

$$


x + 12 = 0 \qquad \text{or} \qquad x - 10 = 0 \qquad \text{or} \qquad x - 11 = 0


$$

Now, we solve each of these equations:

- For the first factor:

- For the second factor:

- For the third factor:

Therefore, in ascending order, the solutions are

$$


x = -12,\ 10,\ 11.


$$

### Example: Solving a Factored Polynomial Equation

#### Question

Solve the equation $\left(\dfrac{3}{2}x - 1\right)\left(2x + \dfrac{1}{4}\right)(x - 7) = 0.$

#### Explanation

We apply the zero product rule, which tells us that if the product of several expressions is zero, then at least one of the expressions must be zero.

So, we set each factor equal to zero:

$$


\dfrac{3}{2}x - 1 = 0 \qquad \text{or} \qquad 2x + \dfrac{1}{4} = 0 \qquad \text{or} \qquad x - 7 = 0


$$

Now, we solve each of these equations:

- For the $1$st factor:

- For the $2$nd factor:

- For the $3$rd factor:

Therefore, in ascending order, the solutions are the following:

$$


x = \boxed{\color{blue}-\dfrac{1}{8}},\ \boxed{\color{blue}\dfrac{2}{3}},\ \boxed{\color{blue}7}


$$

### Example: Solving a Factored Polynomial Equation Containing Monomials

#### Question

Solve the equation $x^2(x + \sqrt{6}) = 0.$

#### Explanation

We apply the zero product rule, which tells us that if the product of several expressions is zero, then at least one of the expressions must be zero.

So, we set each factor equal to zero:

$$


x^2 = 0 \qquad \text{or} \qquad x + \sqrt{6} = 0


$$

Now, we solve each of these equations:

- For the $1$st factor:

- For the $2$nd factor:

Therefore, in ascending order, the solutions are the following:

$$


x = -\sqrt{6},\ 0


$$

### Constructing Polynomial Equations

The zero product rule can also be used in reverse. Suppose we would like to find a cubic equation that has solutions

$$


x = -1, \qquad x = 3, \qquad x = 10.


$$

Notice that the given roots can be obtained as solutions to the following linear equations:

- $x + 1 = 0$

- $x - 3 = 0$

- $x - 10 = 0$

So, according to the zero product rule, they are also the solutions of the product

$$


(x + 1)(x - 3)(x - 10) = 0.


$$

To find our cubic equation, we expand the left-hand side:

$$


\begin{aligned}(𝑥+1)(𝑥−3)(𝑥−10) & =(𝑥+1)(𝑥(𝑥−10)−3(𝑥−10)) \\ & =(𝑥+1)(𝑥^{2}−10𝑥−3𝑥+30) \\ & =(𝑥+1)(𝑥^{2}−13𝑥+30) \\ & =𝑥(𝑥^{2}−13𝑥+30)+(𝑥^{2}−13𝑥+30) \\ & =𝑥^{3}−13𝑥^{2}+30𝑥+𝑥^{2}−13𝑥+30 \\ & =𝑥^{3}−12𝑥^{2}+17𝑥+30\end{aligned}


$$

Therefore, a cubic equation that has the required solutions is

$$


x^3 - 12x^2 + 17x + 30 = 0.


$$

### Example: Constructing a Cubic Equation With Specified Roots

#### Question

Find a cubic equation with a leading coefficient of $3$ that has solutions $x = -1,$ $x = \dfrac{4}{3},$ and $x = 6.$

#### Explanation

The given solutions $x = -1,$ $x = \dfrac{4}{3},$ and $x = 6$ are the solutions to the following equations:

- $x + 1 = 0$

- $x - \dfrac{4}{3} = 0$

- $x - 6 = 0$

So, according to the zero product rule, they are also the solutions of the product

$$


(x + 1)\left(x - \dfrac{4}{3}\right)(x - 6) = 0.


$$

To eliminate fractions, we multiply both sides of the equation by $3{:}$

$$


\begin{aligned}3(𝑥+1)(𝑥−\frac{4}{3})(𝑥−6) & =3⋅0 \\ (3𝑥−4)(𝑥+1)(𝑥−6) & =0\end{aligned}


$$

Now, we expand the left-hand side:

$$


\begin{aligned}(3𝑥−4)(𝑥+1)(𝑥−6) & =(3𝑥−4)((𝑥+1)(𝑥−6)) \\ & =(3𝑥−4)(𝑥^{2}−6𝑥+𝑥−6) \\ & =(3𝑥−4)(𝑥^{2}−5𝑥−6) \\ & =3𝑥(𝑥^{2}−5𝑥−6)−4(𝑥^{2}−5𝑥−6) \\ & =3𝑥^{3}−15𝑥^{2}−18𝑥−4𝑥^{2}+20𝑥+24 \\ & =3𝑥^{3}−19𝑥^{2}+2𝑥+24\end{aligned}


$$

Therefore, a cubic equation that has the required solutions is

$$


3x^3 - 19x^2 + 2x + 24 = 0.


$$
