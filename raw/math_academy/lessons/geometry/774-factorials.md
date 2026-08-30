# Factorials

Source: https://www.mathacademy.com/topics/774?courseId=126
Topic ID: 774

## Prerequisites

- [Simplifying Rational Expressions](../grade-7/68-simplifying-rational-expressions.md)

## Lesson

### Introduction

The **factorial** of a natural number is the product of the number and all of the natural numbers below it. The factorial of a number is denoted by placing an exclamation point after the number.

For example, the factorial of $4$ is written as $4!$ (with an exclamation point after the $4$), and is computed as

$$


4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24.


$$

So, we say that "four factorial is twenty-four".

The factorials of the natural numbers $1$ through $5$ are as follows:

$$


\begin{aligned} 1! &= 1 \\\[5pt] 2! &= 2 \cdot 1 = 2 \\\[5pt] 3! &= 3 \cdot 2 \cdot 1 = 6 \\\[5pt] 4! &= 4 \cdot 3 \cdot 2 \cdot 1 = 24 \\\[5pt] 5! &= 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120 \end{aligned}


$$

Note that the factorial of $0$ is defined to be equal to $1\mathbin{:}$

$$


0! = 1


$$

### Example: Evaluating Factorials

#### Question

$5!\,2!=$

#### Explanation

The given expression is a product of two factorials.

- Computing $5!$ using the definition, we get

- Computing $2!$ using the definition, we get

Finally, we can evaluate the given expression:

$$


\begin{aligned}5!\,2! & =5!⋅2! \\ & =120⋅2 \\ & =240\end{aligned}


$$

### Example: Evaluating the Factorial of Zero

#### Question

Calculate $\dfrac{5!}{0!}.$

#### Explanation

The given expression is a quotient of two factorials.

- Computing $5!$ using the definition, we get

- By definition, the factorial of zero equals one:

Finally, we can evaluate the given expression:

$$


\begin{aligned}\frac{5!}{0!} & =\frac{120}{1}=120\end{aligned}


$$

### Simplifying Rational Expressions that Contain Factorials

One way to simplify a rational expression containing factorials is to calculate the numerator and denominator separately, and then divide the results.

For example, computing $\dfrac{10!}{8!}$ using this method, we get

$$


\begin{aligned} \dfrac {10!}{8!} &= \dfrac {10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} {8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1} = \dfrac {3\,628\,800} {40\,320} = 90. \end{aligned}


$$

However, the method above involves lots of computations. Thankfully, there's an easier way!

Before we multiply, we can cancel out any numbers that appear in both the numerator and denominator, thereby reducing the amount of computation that's needed. Using this method, we get the same result with far fewer computations:

$$


 \begin{aligned} \dfrac {10!}{8!} &= \dfrac {10 \cdot 9 \cdot 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 } { 8 \cdot 7 \cdot 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 } = \dfrac{10 \cdot 9}{1} = 90 \end{aligned}


$$

Even quicker, we could just realize that $10! = 10 \cdot 9 \cdot 8!$ and then cancel the $8!$ that appears in both the numerator and the denominator:

$$


 \dfrac {10!}{8!} = \dfrac {10 \cdot 9 \cdot 8!} {8!} = \dfrac {10 \cdot 9} {1} = 90


$$

### Example: Evaluating a Quotient of Factorials

#### Question

Evaluate $\dfrac {5!} {2!}.$

#### Explanation

First, notice that $5! = 5 \cdot 4 \cdot 3 \cdot 2! \,.$ Then, we can cancel the $2!$ that occurs in both the numerator and the denominator:

$$


 \begin{aligned} \dfrac {5!} {2!} &= \dfrac {5 \cdot 4 \cdot 3 \cdot 2!} {2!} \\\[5pt] &= \dfrac {5 \cdot 4 \cdot 3 \cdot 2!} {2!} \\\[5pt] &= \dfrac {5 \cdot 4 \cdot 3} {1} \\\[5pt] &= 60 \end{aligned}


$$
