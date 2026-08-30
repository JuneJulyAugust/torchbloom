# Factorials in Variable Expressions

Source: https://www.mathacademy.com/topics/3710?courseId=128
Topic ID: 3710

## Prerequisites

- [Multiplying Binomials](../../../traditional/lessons/algebra-i/371-multiplying-binomials.md)
- [Simplifying Rational Expressions by Factoring](../../../traditional/lessons/algebra-i/423-simplifying-rational-expressions-by-factoring.md)
- [Factorials](../../../traditional/lessons/geometry/774-factorials.md)

## Lesson

### Introduction

Factorials can be applied to variables, too. To manipulate a factorial expression involving a variable, we just need to remember that the variable represents a number, and the previous number can be obtained by subtracting $1$ from the variable.

So, in the same way that we have

$$


\begin{aligned}5! & =5⋅\overset{4⋅3⋅2⋅1}{4!} \\ & =5⋅4!\end{aligned}


$$

we also have

$$


\begin{aligned}𝑛! & =𝑛⋅\overset{(𝑛−1)⋅(𝑛−2)⋅\,⋯\,⋅2⋅1}{(𝑛−1)!} \\ & =𝑛⋅(𝑛−1)!\end{aligned}


$$

where $n$ denotes some positive integer.

Likewise, in the same way that we have

$$


5! = 5 \cdot 4 \cdot 3!


$$

we also have

$$


x! = x \cdot (x-1) \cdot (x-2)!


$$

### Example: Writing a Factorial in an Equivalent Form

#### Question

Which of the following is equivalent to $(k+1)!$ for any $k \geq 2?$

1. $(k+1) \cdot k \cdot (k-1)$

2. $(k+1) \cdot k \cdot (k-1)!$

3. $(k+1) \cdot k$

#### Explanation

Using the definition of factorial, we have

$$


(k+1)! = (k+1) \cdot k \cdot (k-1) \cdot (k-2) \cdot \: \cdots \: \cdot 2 \cdot 1.


$$

Now, applying the factorial definition to all but the first two factors, we get

$$


\begin{aligned}(𝑘+1)! & =(𝑘+1)⋅𝑘⋅\overset{(𝑘−1)⋅(𝑘−2)⋅\,⋯\,⋅2⋅1}{(𝑘−1)!} \\ & =(𝑘+1)⋅𝑘⋅(𝑘−1)!\end{aligned}


$$

Therefore, the correct answer is "II only."

### Example: Simplifying a Variable Expression Containing a Quotient of Factorials

#### Question

Given that $n \geq 2$ is an integer, simplify $\dfrac {n!} {(n - 2)!}.$

#### Explanation

First, notice the following:

$$


n! = n \cdot (n-1) \cdot (n-2)!


$$

Then, we cancel the $(n-2)!$ that occurs in both the numerator and the denominator:

$$


\begin{aligned} \dfrac {n!} {(n - 2)!} &= \dfrac {n \cdot (n - 1) \cdot (n - 2)!} {(n - 2)!}\\[5pt] &= \dfrac {n \cdot (n - 1) \cdot (n - 2)!} {(n - 2)!}\\[5pt] &= n(n -1) \\[5pt] &= n^2 - n \end{aligned}


$$

### Example: Simplifying a Variable Expression Containing a Quotient With Many Factorials

#### Question

Given that $k \geq 1$ is an integer, simplify $\dfrac {k^2(k - 1)!} {k!}.$

#### Explanation

First, we notice that

$$


k! = k \cdot (k-1)!


$$

So, we can simplify the numerator as follows:

$$


k^2 (k-1)! = k \cdot \underbrace{k \cdot (k-1)!}_{k!} = k \cdot k!


$$

Then, we cancel the $k!$ that occurs in both the numerator and the denominator:

$$


\begin{aligned} \dfrac {k^2(k - 1)!} {k!} &= \dfrac {k \cdot k!} {k!}\\[5pt] &= \dfrac {k \cdot k!} {k!} \\[5pt] &= \dfrac {k} {1} \\[5pt] &= k \end{aligned}


$$
