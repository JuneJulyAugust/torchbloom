# Vieta's Formulas

Source: https://www.mathacademy.com/topics/729?courseId=128
Topic ID: 729

## Prerequisites

- [Solving Linear Equations by Clearing a Rational Expression](../../../../middle-school/lessons/grade-7/651-solving-linear-equations-by-clearing-a-rational-expression.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../../../traditional/lessons/algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)
- [Evaluating Rational Expressions](../../../../middle-school/lessons/grade-7/2183-evaluating-rational-expressions.md)

## Lesson

### Introduction

Suppose we want to find the sum and the product of the solutions of the following quadratic equation:

$$


2x^2 - 160x - 6\,882 = 0


$$

One way is to find the roots and then compute their sum and product. However, this method might be cumbersome because some of the coefficients of our quadratic equation are large.

An alternative method is to use **Vieta's formulas.** Vieta's formulas state that, for a quadratic equation of the form

$$


ax^2+bx+c=0


$$

with $a \neq 0$ and two solutions $x=x_1$ and $x=x_2,$ the sum of these solutions is

$$


x_1 + x_2 = -\dfrac{b}{a},


$$

and the product of these solutions is

$$


x_1\cdot x_2 = \dfrac{c}{a}.


$$

We'll explain how these formulas are derived at the end of the lesson.

### Applying Vieta's Formulas

Let's find the sum and product of the solutions of our equation

$$


2x^2 - 160x - 6\,882 = 0.


$$

In this case, we have

$$


a=2,\qquad b=-160,\qquad c=-6\,882.


$$

Applying Vieta's formulas, we get the following:

- The sum of the solutions is given by

- The product of the solutions is given by

Finally, let's check our results. First, note that the equation can be factored as

$$


2(x+31)(x-111) = 0.


$$

Therefore, by the zero-product rule, the solutions to this equation are

$$


x_1 = -31, \qquad x_2 = 111.


$$

The sum of the solutions is

$$


x_1 + x_2 = -31 + 111 = 80\quad{\color{green}\checkmark}


$$

and the product of the solutions is

$$


x_1\cdot x_2 = -31 \cdot 111 = -3\,441. \quad{\color{green}\checkmark}


$$

### Example: Determining the Sum of the Roots of a Quadratic Equation

#### Question

Consider the quadratic equation

$$


8x^2 + 5x - 12 = 0.


$$

**** solving the equation, determine the sum of its solutions.

#### Explanation

Suppose the quadratic equation

$$


ax^2 + bx + c = 0


$$

has the solutions $x = x_1$ and $x = x_2,$ where $a\neq 0.$

Then, Vieta's formulas state the following:

- The sum of the solutions is given by

- The product of the solutions is given by

For the given quadratic equation, we have

$$


a = 8, \qquad b = 5, \qquad c = -12.


$$

Therefore, the sum of the solutions is

$$


\begin{aligned}−\frac{𝑏}{𝑎} & =−\frac{5}{8}.\end{aligned}


$$

### Example: Determining the Product of the Roots of a Quadratic Equation

#### Question

Consider the quadratic equation

$$


x^2 - 37x + 247 = 0.


$$

**** solving the equation, determine the product of its solutions.

#### Explanation

Suppose the quadratic equation

$$


ax^2 + bx + c = 0


$$

has the solutions $x = x_1$ and $x = x_2,$ where $a\neq 0.$

Then, Vieta's formulas state the following:

- The sum of the solutions is given by

- The product of the solutions is given by

For the given quadratic equation, we have

$$


a = 1, \qquad b = -37, \qquad c = 247.


$$

Therefore, the product of the solutions is

$$


\begin{aligned}\frac{𝑐}{𝑎} & =\frac{247}{1}=247.\end{aligned}


$$

### Example: Constructing a Quadratic Equation With a Given Sum and Product of Roots

#### Question

The quadratic coefficient of a particular quadratic equation equals $8.$ The sum of the solutions equals $-11,$ and the product of the solutions equals $24.$ Find the equation.

#### Explanation

Suppose the quadratic equation

$$


ax^2 + bx + c = 0


$$

has the solutions $x = x_1$ and $x = x_2,$ where $a\neq 0.$

Then, Vieta's formulas state the following:

- The sum of the solutions is given by

- The product of the solutions is given by

Now, let's use the given information to determine the values of $a, b,$ and $c$ in this case:

- We're told that the quadratic coefficient equals $8.$ Therefore, we have

- We're told that the sum of the roots equals $-11.$ Therefore, we have

- We're told that the product of the roots equals $24.$ Therefore, we have

Therefore, our equation has coefficients

$$


a = 8, \qquad b = 88, \qquad c = 192


$$

and the equation is

$$


8x^2 +88x + 192 = 0.


$$

### Deriving Vieta's Formulas

We'll now derive Vieta's formulas for the sum and product of the solutions of a quadratic equation.

Consider the quadratic equation

$$


ax^2+bx+c=0


$$

with solutions $x_1$ and $x_2.$

According to a mathematical theorem known as the fundamental theorem of algebra, the left-hand side of our quadratic equation can *always* be factored as

$$


ax^2+bx+c = a(x-x_1)(x-x_2).


$$

You'll learn more about the fundamental theorem of algebra in future lessons.

Expanding the parentheses on the right-hand side, we have

$$


\begin{aligned}𝑎(𝑥−𝑥_{1})(𝑥−𝑥_{2}) & =𝑎(𝑥^{2}−𝑥_{1}𝑥−𝑥_{2}𝑥+𝑥_{1}𝑥_{2}) \\ & =𝑎(𝑥^{2}−(𝑥_{1}+𝑥_{2})𝑥+𝑥_{1}𝑥_{2}) \\ & =𝑎𝑥^{2}−𝑎(𝑥_{1}+𝑥_{2})𝑥+𝑎𝑥_{1}𝑥_{2}.\end{aligned}


$$

Since this is identical to the original equation, we have

$$


ax^2+bx+c = ax^2 - a(x_1 + x_2) x + ax_1x_2


$$

which is true for all values of $x.$

Since $a\neq 0,$ dividing both sides by $a,$ we obtain

$$


x^2+{\color{blue}\dfrac{b}{a}}x+{\color{red}\dfrac{c}{a}} = x^2 \:{\color{blue}- \:(x_1+x_2)}x + {\color{red}x_1 x_2}.


$$

Since this equation is true for all values of $x,$ we can extract Vieta's formulas by equating the coefficients of the linear and constant terms on both sides of the equation, as follows:

- Equating the linear coefficients, we have which we can write as

- Equating the constants, we have
