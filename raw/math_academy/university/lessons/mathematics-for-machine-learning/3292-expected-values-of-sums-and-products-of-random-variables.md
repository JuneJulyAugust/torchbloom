# Expected Values of Sums and Products of Random Variables

Source: https://www.mathacademy.com/topics/3292?courseId=145
Topic ID: 3292

## Prerequisites

- [Properties of Expectation for Discrete Random Variables](./2836-properties-of-expectation-for-discrete-random-variables.md)
- [Independence of Discrete Random Variables](./3048-independence-of-discrete-random-variables.md)

## Lesson

### Introduction

We can use the following property to simplify expressions involving expected values:

For any random variables $X$ and $Y$ and constants $a$ and $b,$ we have

$$


\textrm E[aX+bY] = a \textrm E[X] + b \textrm E[Y].


$$

In other words, the expected value of a sum of scaled random variables equals the sum of the scaled expected values.

For example,

$$


\textrm E[2X+5Y] = 2 \textrm E[X] + 5 \textrm E[Y].


$$

Note that the property also works with subtraction:

$$


\textrm E[2X-5Y] = 2 \textrm E[X] - 5 \textrm E[Y]


$$

We can extend this idea to any number of random variables. For example, for any random variables $X_1, X_2,\ldots, X_n,$ and real constants $a_1, a_2, \ldots, a_n$, we have

$$


\text{E}[a_1X_1+a_2X_2+\cdots+ a_nX_n]= a_1\textrm E[X_1]+a_2\textrm E[X_2]+\cdots +a_n\text{E}[X_n],


$$

or more concisely,

$$


\text{E}\left[\sum_{i=1}^n a_i X_i\right] =\sum_{i=1}^n a_i \textrm E[X_i].


$$

Note that the random variables $X_1, X_2,\ldots, X_n,$ are *not* required to be independent.

### Example: Finding the Expected Value of a Sum of Random Variables

#### Question

Compute $\textrm E[5X-2Y]$ if $\textrm E[X]=1$ and $\textrm E[Y] = 2.$

#### Explanation

For any random variables $X,Y$ and any constants $a,b,$ we have

$$


\textrm E[aX+bY] = a \textrm E[X] + b \textrm E[Y].


$$

Therefore,

$$


\begin{aligned}E[5𝑋−2𝑌] & =5E[𝑋]−2E[𝑌] \\ & =5(1)−2(2) \\ & =1.\end{aligned}


$$

### Example: Finding the Expected Value of a Sum of Random Variables in Context

#### Question

Andrea has two dice. One of them is fair, and the other is not. The rolls of the unfair die follow the probability mass function $f(y)$ shown in the table below. What is the expected sum of the outcomes of $2$ throws of the fair die and $4$ throws of the unfair one?

#### Explanation

Let $X_i$ be the $i$th score obtained from the fair die, and let $Y_j$ be the $j$th score obtained from the unfair die. Also, let $X$ and $Y$ represent the scores obtained from a typical throw of the fair and unfair die, respectively.

Then, we need to calculate

$$


\textrm E\left[ \sum_{i=1}^2 X_i + \sum_{j=1}^4 Y_j \right].


$$

Using the properties of expected value, we have

$$


\begin{aligned}E[\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}𝑋_{𝑖}+\underset{\underset{𝑗=1}{∑}}{\overset{}{4}}𝑌_{𝑗}] & =\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}E[𝑋_{𝑖}]+\underset{\underset{𝑗=1}{∑}}{\overset{}{4}}E[𝑌_{𝑗}] \\ & =2E[𝑋]+4E[𝑌],\end{aligned}


$$

where the last equality above is true because $\textrm E[X_i] = \textrm E[X]$ and $\textrm E[Y_j] = \textrm E[Y]$ for all $1\leq i \leq 2,\: 1\leq j\leq 4.$

The expected values of $X$ and $Y$ are calculated as follows:

$$


\begin{aligned}E[𝑋] & =1⋅\frac{1}{6}+2⋅\frac{1}{6}+3⋅\frac{1}{6}+4⋅\frac{1}{6}+5⋅\frac{1}{6}+6⋅\frac{1}{6}=\frac{7}{2} \\ E[𝑌] & =1⋅\frac{1}{4}+2⋅\frac{1}{16}+3⋅\frac{1}{4}+4⋅\frac{1}{8}+5⋅\frac{1}{4}+6⋅\frac{1}{16}=\frac{13}{4}\end{aligned}


$$

Hence, we get

$$


\textrm E[2X+4Y]=2\textrm E[X]+4\textrm E[Y]= 2\cdot \dfrac{7}{2}+4\cdot \dfrac{13}{4} =20.


$$

### The Expectation of a Product of Random Variables

The expected value of the product of two *independent* random variables is equal to the product of the expected values. So, if the random variables $X$ and $Y$ are independent, we have

$$


\text{E}[X\cdot Y] = \textrm E[X]\cdot \textrm E[Y].


$$

For example, if we know that $X$ are $Y$ are independent, and that $\textrm E[X]=2$ and $\textrm E[Y]=3$, then

$$


\begin{aligned}E[𝑋⋅𝑌] & =E[𝑋]⋅E[𝑌] \\ & =2⋅3 \\ & =6.\end{aligned}


$$

When working with the expected value of a product of random variables, it's important to check that the variables are independent. The formula above is *not* true if $X$ and $Y$ are not independent.

More generally, if the random variables $X_1, X_2,\ldots, X_n$ are *mutually* independent, then

$$


\textrm E[X_1\cdot X_2 \cdots X_n]=\textrm E[X_1]\cdot \textrm E[X_2]\cdot\ldots\cdot \textrm E[X_n],


$$

or more concisely,

$$


\text{E}\left[ \prod_{i=1}^n X_i\right] = \prod_{i=1}^n \textrm E[X_i],


$$

where $\prod$ is the product operator.

### Example: Finding the Expected Value of a Product of Random Variables

#### Question

The probability distributions of the independent random variables $X$ and $Y$ are given below.

Find $\textrm E[XY].$

#### Explanation

Recall that if $X$ and $Y$ are ** random variables, then

$$


\textrm E[X\cdot Y]=\textrm E[X]\cdot \textrm E[Y].


$$

The expected values of $X$ and $Y$ are calculated as follows:

$$


\begin{aligned}E[𝑋] & =−4⋅\frac{1}{6}−2⋅\frac{1}{3}+2⋅\frac{1}{3}+4⋅\frac{1}{6}=0 \\ E[𝑌] & =1⋅\frac{1}{4}+2⋅\frac{1}{4}+3⋅\frac{1}{2}=\frac{9}{4}\end{aligned}


$$

Since $X$ and $Y$ are independent, we have

$$


\textrm E[X\cdot Y] = \textrm E[X] \cdot \textrm E[Y] = 0 \cdot \dfrac{9}{4} = 0.


$$
