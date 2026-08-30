# Advanced Rational Equations

Source: https://www.mathacademy.com/topics/708?courseId=101
Topic ID: 708

## Prerequisites

- [Rational Equations With Three Terms](./440-rational-equations-with-three-terms.md)
- [The Least Common Multiple of Two Polynomials](../../../traditional/lessons/algebra-ii/2626-the-least-common-multiple-of-two-polynomials.md)

## Lesson

### Introduction

Suppose we want to solve the following rational equation.

Notice that each of the denominators in our equation is either a binomial or product of binomials.

From here, we make the following observations:

- The least common denominator () is the least common multiple () of the denominators, which in this case is given by

- The values and cannot be solutions to our equation. These values make at least one denominator in our original equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

After canceling, we are left with the equation

Solving this equation for we get the following:

So, is a *potential* solution.

We now need to check this value against the prohibited solutions and mentioned earlier. Now, since and we have that is indeed a valid solution.

Therefore, we conclude that the solution to our original equation is

### Example: Solving Rational Equations Using the Lowest Common Denominator

#### Question

Solve the equation $\dfrac{4} {x - 2} - \dfrac{8} {x(x - 2)} = \dfrac {3} {x}.$

#### Explanation

We make the following observations:

- The least common denominator of our equation is given by

- The values $x = 0$ and $x=2$ cannot be solutions to our equation. These values make at least one denominator in our original equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

$$


\begin{aligned}\frac{4}{𝑥−2}−\frac{8}{𝑥(𝑥−2)} & =\frac{3}{𝑥} \\ 𝑥(𝑥−2)⋅(\frac{4}{𝑥−2}−\frac{8}{𝑥(𝑥−2)}) & =𝑥(𝑥−2)⋅\frac{3}{𝑥} \\ \frac{4𝑥(𝑥−2)}{𝑥−2}−\frac{8𝑥(𝑥−2)}{𝑥(𝑥−2)} & =\frac{3𝑥(𝑥−2)}{𝑥} \\ \frac{4𝑥(𝑥−2)}{𝑥−2}−\frac{8𝑥(𝑥−2)}{𝑥(𝑥−2)} & =\frac{3𝑥(𝑥−2)}{𝑥} \\ 4𝑥−8 & =3(𝑥−2)\end{aligned}


$$

Solving this equation for $x,$ we get the following:

$$


\begin{aligned}4𝑥−8 & =3(𝑥−2) \\ 4𝑥−8 & =3𝑥−6 \\ 4𝑥−3𝑥 & =−6+8 \\ 𝑥 & =2\end{aligned}


$$

However, since $x=2$ is not a valid solution, we conclude that our equation has no solutions.

### Solving Rational Equations by Factoring

When a rational equation contains a quadratic denominator, it's often helpful to factor this denominator first. By doing so, we may spot the least common denominator of the equation, leading to a more straightforward solution.

For example, consider the following equation:

$$


\dfrac{1}{x-1}+\dfrac{2}{x-2}=\dfrac{5}{x^2-3x+2}


$$

Notice that the right-hand side of our equation contains a term with a quadratic denominator. This denominator can be factored, giving us the equation

$$


\dfrac{1}{x-1}+\dfrac{2}{x-2}=\dfrac{5}{(x-1)(x-2)}\,.


$$

We now make the following observations:

- The least common denominator is given by

- The values $x=1$ and $x=2$ *cannot* be solutions to our equation. These values make at least one denominator in our original equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify the equation as follows:

$$


\begin{aligned}(𝑥−1)(𝑥−2)⋅(\frac{1}{𝑥−1}+\frac{2}{𝑥−2}) & =(𝑥−1)(𝑥−2)⋅(\frac{5}{(𝑥−1)(𝑥−2)}) \\ \frac{(𝑥−1)(𝑥−2)}{𝑥−1}+\frac{2(𝑥−1)(𝑥−2)}{𝑥−2} & =\frac{5(𝑥−1)(𝑥−2)}{(𝑥−1)(𝑥−2)} \\ \frac{(𝑥−1)⋅(𝑥−2)}{𝑥−1}+\frac{2(𝑥−1)⋅(𝑥−2)}{𝑥−2} & =\frac{5(𝑥−1)(𝑥−2)}{(𝑥−1)(𝑥−2)} \\ (𝑥−2)+2(𝑥−1) & =5\end{aligned}


$$

Solving this equation for $x,$ we get the following:

$$


\begin{aligned}(𝑥−2)+2(𝑥−1) & =5 \\ 𝑥−2+2𝑥−2 & =5 \\ 3𝑥−4 & =5 \\ 3𝑥 & =9 \\ 𝑥 & =3\end{aligned}


$$

Since $3\neq 1$ and $3\neq 2,$ we conclude that $x=3$ is a valid solution.

Therefore, the solution to our original equation is $x=3.$

### Example: Solving Rational Equations by Factoring a Quadratic Trinomial

#### Question

Solve the equation $\dfrac{3}{k-3} -\dfrac {2}{k-2} = \dfrac{2}{k^2-5k+6}.$

#### Explanation

First, we factor the quadratic denominator, giving us the equation

$$


\dfrac{3}{k-3} -\dfrac {2}{k-2} = \dfrac{2}{(k-2)(k-3)}.


$$

We now make the following observations:

- The least common denominator of our equation is given by

- The values $k=2$ and $k=3$ cannot be solutions to our equation. These values make at least one denominator in our original equation equal to zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

$$


\begin{aligned}\frac{3}{𝑘−3}−\frac{2}{𝑘−2} & =\frac{2}{(𝑘−2)(𝑘−3)} \\ (𝑘−2)(𝑘−3)⋅(\frac{3}{𝑘−3}−\frac{2}{𝑘−2}) & =(𝑘−2)(𝑘−3)⋅\frac{2}{(𝑘−2)(𝑘−3)} \\ \frac{3(𝑘−2)(𝑘−3)}{𝑘−3}−\frac{2(𝑘−2)(𝑘−3)}{𝑘−2} & =\frac{2(𝑘−2)(𝑘−3)}{(𝑘−2)(𝑘−3)} \\ \frac{3(𝑘−2)⋅(𝑘−3)}{𝑘−3}−\frac{2⋅(𝑘−2)⋅(𝑘−3)}{𝑘−2} & =\frac{2⋅(𝑘−2)(𝑘−3)}{(𝑘−2)(𝑘−3)} \\ 3(𝑘−2)−2(𝑘−3) & =2\end{aligned}


$$

Solving this equation for $k,$ we get the following:

$$


\begin{aligned}3(𝑘−2)−2(𝑘−3) & =2 \\ 3𝑘−6−2𝑘+6 & =2 \\ 𝑘 & =2\end{aligned}


$$

However, since $k=2$ is not a valid solution, our equation has no solutions.

### Example: Solving Rationals Equations by Factoring a Quadratic Denominator With No Constant Term

#### Question

Solve the equation $\dfrac{3}{u+1} - \dfrac{1}{3u} =\dfrac{5}{u^2 +u}.$

#### Explanation

First, we factor the quadratic denominator, giving us the equation

$$


\dfrac{3}{u+1} - \dfrac{1}{3u} =\dfrac{5}{u(u+1)}.


$$

We now make the following observations:

- The least common denominator of our equation is given by

- The values $u=-1$ and $u=0$ cannot be solutions to our equation. These values make at least one denominator in our original equation equal zero, and division by zero is undefined.

Now, multiplying both sides of the equation by the least common denominator, we can simplify it as follows:

$$


\begin{aligned}\frac{3}{𝑢+1}−\frac{1}{3𝑢} & =\frac{5}{𝑢(𝑢+1)} \\ 3𝑢(𝑢+1)⋅(\frac{3}{𝑢+1}−\frac{1}{3𝑢}) & =3𝑢(𝑢+1)⋅\frac{5}{𝑢(𝑢+1)} \\ \frac{9𝑢(𝑢+1)}{𝑢+1}−\frac{3𝑢(𝑢+1)}{3𝑢} & =\frac{15𝑢(𝑢+1)}{𝑢(𝑢+1)} \\ \frac{9𝑢⋅(𝑢+1)}{𝑢+1}−\frac{3𝑢⋅(𝑢+1)}{3𝑢} & =\frac{15⋅𝑢(𝑢+1)}{𝑢(𝑢+1)} \\ 9𝑢−(𝑢+1) & =15\end{aligned}


$$

Solving this equation for $u,$ we get the following:

$$


\begin{aligned}9𝑢−(𝑢+1) & =15 \\ 9𝑢−𝑢−1 & =15 \\ 8𝑢 & =16 \\ 𝑢 & =2\end{aligned}


$$

Since $2\neq -1$ and $2\neq 0,$ we conclude that $u=2$ is a valid solution.

Therefore, the solution to our original equation is $u=2.$
