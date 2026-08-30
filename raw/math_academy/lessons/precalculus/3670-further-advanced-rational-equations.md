# Further Advanced Rational Equations

Source: https://www.mathacademy.com/topics/3670?courseId=43
Topic ID: 3670

## Prerequisites

- [Solving Quadratic Equations with No Constant Term](../algebra-i/393-solving-quadratic-equations-with-no-constant-term.md)
- [Advanced Rational Equations](./708-advanced-rational-equations.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)

## Lesson

### Introduction

The general method of solving rational equations is always the same:

1. Factor the denominators in the equation.

2. Compute the least common denominator and note any prohibited solutions.

3. Multiply the equation by the least common denominator and solve the resulting equation.

4. Compare all of the solutions found in the third step against the prohibited solutions and reject any invalid solutions.

When solving rational equations, we sometimes find that, after some manipulations, they reduce to quadratic equations. Let's see an example.

### Example: Solving Rational Equations With Two Rational Terms

#### Question

Solve the equation $\dfrac{1}{x - 9} + 2 = \dfrac{5}{x - 3}.$

#### Explanation

To solve this equation, we first make the following observations:

- The least common denominator of our equation is given by

- The values $x=3$ and $x=9$ cannot be solutions to our equation. These values make at least one denominator in our equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

$$


\begin{aligned}\frac{1}{𝑥−9}+2 & =\frac{5}{𝑥−3} \\ (𝑥−9)(𝑥−3)⋅(\frac{1}{𝑥−9}+2) & =(𝑥−9)(𝑥−3)⋅\frac{5}{𝑥−3} \\ \frac{(𝑥−9)(𝑥−3)}{𝑥−9}+2(𝑥−9)(𝑥−3) & =\frac{5(𝑥−9)(𝑥−3)}{𝑥−3} \\ \frac{(𝑥−9)(𝑥−3)}{𝑥−9}+2(𝑥−9)(𝑥−3) & =\frac{5(𝑥−9)(𝑥−3)}{𝑥−3}\end{aligned}


$$

After canceling, we're left with the equation

$$


x - 3 + 2(x - 9)(x - 3) = 5(x - 9).


$$

This is a quadratic equation. Solving this equation for $x,$ we get the following:

$$


\begin{aligned}𝑥−3+2(𝑥−9)(𝑥−3) & =5(𝑥−9) \\ 𝑥−3+2(𝑥−12𝑥+27) & =5𝑥−45 \\ 𝑥−3+2𝑥^{2}−24𝑥+54 & =5𝑥−45 \\ 2𝑥^{2}−28𝑥+96 & =0 \\ 𝑥^{2}−14𝑥+48 & =0 \\ (𝑥−6)(𝑥−8) & =0\end{aligned}


$$

This gives two ** solutions, $x=6$ and $x=8.$ We now need to compare these solutions against the prohibited solutions mentioned previously.

- Since $6\neq 3$ and $6\neq 9,$ we conclude that $x=6$ is a valid solution $\:{\color{green}{\checkmark}}$

- Since $8\neq 3$ and $8\neq 9,$ we conclude that $x=8$ is a valid solution $\:{\color{green}{\checkmark}}$

Therefore, the solutions to our original equation are $x=6$ and $x=8.$

### Example: Solving Rational Equations With Three Rational Terms

#### Question

Find the sum of the solutions to the equation $\dfrac{3}{t+1} + \dfrac{5}{t-3} = \dfrac{12}{t-1}.$

#### Explanation

We make the following observations:

- The least common denominator of our equation is given by

- The values $t = \pm1,$ and $t=3$ cannot be solutions to our equation. These values make at least one denominator in our equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

$$


\begin{aligned}\frac{3}{𝑡+1}+\frac{5}{𝑡−3} & =\frac{12}{𝑡−1} \\ (𝑡+1)(𝑡−1)(𝑡−3)⋅(\frac{3}{𝑡+1}+\frac{5}{𝑡−3}) & =(𝑡+1)(𝑡−1)(𝑡−3)⋅(\frac{12}{𝑡−1}) \\ \frac{3(𝑡+1)(𝑡−1)(𝑡−3)}{𝑡+1}+\frac{5(𝑡+1)(𝑡−1)(𝑡−3)}{𝑡−3} & =\frac{12(𝑡+1)(𝑡−1)(𝑡−3)}{𝑡−1} \\ \frac{3(𝑡+1)(𝑡−1)(𝑡−3)}{𝑡+1}+\frac{5(𝑡+1)(𝑡−1)(𝑡−3)}{𝑡−3} & =\frac{12(𝑡+1)(𝑡−1)(𝑡−3)}{𝑡−1} \\ 3(𝑡−1)(𝑡−3)+5(𝑡+1)(𝑡−1) & =12(𝑡+1)(𝑡−3)\end{aligned}


$$

Solving this equation for $t,$ we get the following:

$$


\begin{aligned}3(𝑡−1)(𝑡−3)+5(𝑡+1)(𝑡−1) & =12(𝑡+1)(𝑡−3) \\ 3(𝑡^{2}−4𝑡+3)+5(𝑡^{2}−1) & =12(𝑡^{2}−2𝑡−3) \\ 3𝑡^{2}−12𝑡+9+5𝑡^{2}−5 & =12𝑡^{2}−24𝑡−36 \\ 8𝑡^{2}−12𝑡+4 & =12𝑡^{2}−24𝑡−36 \\ 8𝑡^{2}−12𝑡+4−12𝑡^{2}+24𝑡+36 & =0 \\ −4𝑡^{2}+12𝑡+40 & =0 \\ 𝑡^{2}−3𝑡−10 & =0 \\ (𝑡+2)(𝑡−5) & =0\end{aligned}


$$

This gives two potential solutions, $t = -2$ and $t = 5\mathbin{:}$

- Since $-2 \neq \pm 1$ and $-2 \neq 3,$ $t = -2$ is a valid solution $\:{\color{green}{\checkmark}}$

- Since $5 \neq \pm 1$ and $5 \neq 3,$ $t = 5$ is a valid solution $\:{\color{green}{\checkmark}}$

Finally, the sum of the solutions is $(-2) + 5 = 3.$
