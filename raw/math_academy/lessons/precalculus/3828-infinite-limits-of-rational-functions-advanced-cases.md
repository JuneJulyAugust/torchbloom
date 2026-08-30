# Infinite Limits of Rational Functions: Advanced Cases

Source: https://www.mathacademy.com/topics/3828?courseId=43
Topic ID: 3828

## Prerequisites

- [Infinite Limits of Rational Functions](./2189-infinite-limits-of-rational-functions.md)

## Lesson

### Introduction

It's often necessary to simplify a rational function to determine its behavior near a vertical asymptote. In this lesson, we'll discuss the general process.

As an example, let's consider the following rational function:

$$



f(x) = \dfrac{x}{x^2 - 4}



$$

First, we factor the numerator and denominator. This gives

$$



\begin{aligned}𝑓(𝑥) & =\frac{𝑥}{(𝑥+2)(𝑥−2)}.\end{aligned}



$$

At this point, we would usually cancel any common factors in the numerator and denominator. However, in this case, there are no common factors, so we can now determine its unbounded behavior using the usual methods.

We see that $f(x)$ has vertical asymptotes at $x=\pm 2.$ Let's determine its behavior as we approach $x=-2$ *from the left.* For this, we use a table of values:

Notice that all the values of $f(x)$ in our table are *negative*, and they *decrease* as we approach $x = -2.$

Therefore, we conclude that

$$



f(x) \rightarrow {\color{red}{-\infty}} \quad\textrm{as}\quad x \rightarrow -2^-.



$$

**Note**: In our table, we calculated the value of $f(x)$ at four points. After some practice, you'll only need to compute $f(x)$ at one or two points to determine its behavior near an asymptote.

### Example: Calculating a Left-Sided Infinite Limit for a Rational Function with an Expanded Denominator

#### Question

Given that $f(x)= -\dfrac{2x+4}{x^2+x - 2} \to a$ as $x \to 1^{-},$ what is the value of $a?$

#### Explanation

We wish to determine the behavior of $f(x)$ as $x$ approaches $1$ from the **.

Factoring the numerator and denominator and canceling any common factors, we get

$$



\begin{aligned}𝑓(𝑥) & =−\frac{2𝑥+4}{𝑥^{2}+𝑥−2} \\ & =−\frac{2(𝑥+2)}{(𝑥+2)(𝑥−1)} \\ & =−\frac{2(𝑥+2)}{(𝑥+2)(𝑥−1)} \\ & =−\frac{2}{𝑥−1}.\end{aligned}



$$

Now, note the following:

- the function $f(x)$ has a vertical asymptote at $x = 1,$

- therefore, $f(x)$ can approach ** $\color{blue}\infty$ ** $\color{red}-\infty$ as $x$ approaches $1$ from the left.

We can see how $f(x)$ behaves as $x$ approaches $1$ from the left using a table of values.

Notice that all the values of $f(x)$ in our table are **, and they ** as we approach $x=1.$

Therefore, $f(x) \rightarrow {\color{blue}{\infty}}$ as $x\rightarrow 1^-,$ which means that $a={\color{blue}{\infty}}.$

### Example: Calculating a Right-Sided Infinite Limit for a Rational Function with an Expanded Denominator

#### Question

Given that $f(x) = \dfrac{2x+10}{25 - x^2} \to a$ as $x \rightarrow 5^{+},$ what is the value of $a?$

#### Explanation

We wish to determine the behavior of $f(x)$ as $x$ approaches $5$ from the **.

Factoring the numerator and denominator and canceling any common factors (if any), we get

$$



\begin{aligned}𝑓(𝑥) & =\frac{2𝑥+10}{25−𝑥^{2}} \\ & =\frac{2(𝑥+5)}{(5+𝑥)(5−𝑥)} \\ & =\frac{2(𝑥+5)}{(5+𝑥)(5−𝑥)} \\ & =\frac{2}{5−𝑥}.\end{aligned}



$$

Now, note the following:

- the function $f(x)$ has a vertical asymptote at $x = 5,$

- therefore, $f(x)$ can approach ** $\color{blue}\infty$ ** $\color{red}-\infty$ as $x$ approaches $5$ from the right.

We can see how $f(x)$ behaves as $x$ approaches $5$ from the right using a table of values.

Notice that all the values of $f(x)$ in our table are **, and they ** as we approach $x = 5.$

Therefore, $f(x) \rightarrow {\color{red}{-\infty}}$ as $x \rightarrow 5^+,$ which means that $a = {\color{red}{-\infty}}.$

### The Connection Between Infinite Limits and One-Sided Limits

Let's determine the behavior of the following function near its asymptotes:

$$



f(x) = \dfrac{1}{x^2 - 2x + 1}



$$

First, we factor the function and cancel the common factors (if any):

$$



\begin{aligned}𝑓(𝑥) & =\frac{1}{𝑥^{2}−2𝑥+1} \\ & =\frac{1}{(𝑥−1)^{2}}\end{aligned}



$$

The function $f(x)$ has a vertical asymptote at $x=1.$ We will now consider the behavior of this function as $x$ approaches $1$ from the left *and* from the right.

First, we create a table of values:

We now analyze our results:

- The values of $f(x)$ in our table are *positive* for $x < 1,$ and they *increase* as we approach $x=1$ from the *left*. Therefore,

- The values of $f(x)$ in our table are *positive* for $x > 1,$ and they *increase* as we approach $x=1$ from the *right.* Therefore,

Now, since $f(x)$ approaches ${\color{blue}{\infty}}$ from the left *and* from the right, we say that *"$f(x)$ approaches ${\color{blue}{\infty}}$ as $x$ approaches $1$*", and we write

$$



f(x) \to {\color{blue}{\infty}} \quad \textrm{as}\quad \quad x \to 1.



$$

This statement indicates that the behavior of $f(x)$ near the asymptote *does not depend* on the direction in which we approach the asymptote.

### Example: Identifying True Statements Regarding Infinite Limits of Factored Rational Functions

#### Question

Given that $f(x) =\dfrac{2x+1}{(x-1)(x-3)},$ which of the following statements are true?

1. $f(x)\to \infty$ as $x\to 3^-$

2. $f(x)\to \infty$ as $x\to 3^+$

3. $f(x)\to \infty$ as $x\to 3$

#### Explanation

We wish to determine the behavior of $f(x)$ as $x$ approaches $3.$

Note the following:

- the function $f(x)$ has a vertical asymptote at $x=3,$

- therefore, $f(x)$ can approach ** $\color{blue}\infty$ ** $\color{red}-\infty$ as $x$ approaches $3$ from the **,

- similarly, $f(x)$ can approach ** $\color{blue}\infty$ ** $\color{red}-\infty$ as $x$ approaches $3$ from the **.

We can see how $f(x)$ behaves as $x$ approaches $3$ using a table of values.

Let's now analyze each of the statements in turn:

- Statement I is false. The values of $f(x)$ in our table are ** for $x < 3,$ and they ** as we approach $x=3$ from the **. Therefore,

- Statement II is true. The values of $f(x)$ in our table are ** for $x >3,$ and they ** as we approach $x= 3$ from the **.

- Statement III is false. Since statement II is true yet statement I is false, we conclude that

Therefore, the correct answer is "II only."

### Example: Identifying True Statements Regarding Infinite Limits of Rational Functions

#### Question

Given that $f(x) = \dfrac{2x+1}{2x^2-3x-2},$ which of the following statements are true?

1. $f(x)\to \infty$ as $x\to 2^-$

2. $f(x)\to \infty$ as $x\to 2^+$

3. $f(x)\to \infty$ as $x\to 2$

#### Explanation

We wish to determine the behavior of $f(x)$ as $x$ approaches $2.$

First, let's factor the function and cancel the common factors (if any):

Note the following:

- The function $f(x)$ has a vertical asymptote at $x=2.$

- Therefore, $f(x)$ can approach ** $\color{blue}\infty$ ** $\color{red}-\infty$ as $x$ approaches $2$ from the **.

- Similarly, $f(x)$ can approach ** $\color{blue}\infty$ ** $\color{red}-\infty$ as $x$ approaches $2$ from the **.

We can see how $f(x)$ behaves as $x$ approaches $2$ using a table of values.

Let's now analyze each of the statements in turn:

- Statement I is false. The values of $f(x)$ in our table are ** for $x < 2,$ and they ** as we approach $x=2$ from the **. Therefore,

- Statement II is true. The values of $f(x)$ in our table are ** for $x >2,$ and they ** as we approach $x=2$ from the **

- Statement III is false. Since statement II is true yet statement I is false, we conclude that

Therefore, the correct answer is "II only."
