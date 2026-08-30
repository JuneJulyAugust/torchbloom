# Probability Mass Functions of Discrete Random Variables

Source: https://www.mathacademy.com/topics/1290?courseId=136
Topic ID: 1290

## Prerequisites

- [Piecewise Functions](../algebra-i/165-piecewise-functions.md)
- [Sigma Notation](../integrated-math-ii-honors/673-sigma-notation.md)
- [The Range of a Function](../algebra-i/754-the-range-of-a-function.md)
- [Mutually Exclusive Events](./1154-mutually-exclusive-events.md)

## Lesson

### Introduction

A **random variable** is a variable whose value is determined by the outcome of a trial or experiment.

For example, suppose we conduct an experiment where we flip a coin twice. The sample space for this experiment, which we'll denote as $\Omega$ (the Greek capital letter "Omega") is given below:

$$


\Omega = \left\{HH, HT, TH, TT\right\}


$$

Now, suppose we define the random variable $X$ as follows:

$\qquad$ $X =$ "*the number of heads we get when a coin is flipped twice*."

Let's work out the possible values of $X.$

- If we get two heads (i.e. the outcome of the experiment is an element of $\{HH\}$), then $X = 2.$

- If we get one head (i.e. the outcome of the experiment is an element of $\{HT,TH\}$), then $X = 1.$

- If we get no heads (i.e. the outcome of the experiment is an element of $\{TT\}$), then $X = 0.$

So, the possible values of $X$ are given by the following set:

$$


S = \{0,1,2\}


$$

Informally, if we flip a coin twice and count the number of heads, we can get either no heads, one head, or two heads. No other values are possible.

The set $S$ is called the **range** or **support** of $X,$ and it includes *every possible value* of the random variable $X.$

### Discrete Random Variables

A **discrete random variable** is a random variable

- that has finitely many possible values, or

- whose possible values can be listed in a sequence: $x_1, x_2, x_3, \ldots$

Note that an interval of real numbers cannot be listed in a sequence.

For example, the result of rolling a $6$-sided dice is a discrete random variable because its possible values can be listed in a sequence: $1,2,3,4,5,6.$

On the other hand, the temperature outside is *not* a discrete random variable because its possible values form an interval of real numbers. The temperature could be anywhere between, say, $50^\circ \, \textrm F$ and $90^\circ \, \textrm F,$ and the interval of real numbers $[50, 90]$ cannot be listed in a sequence.

### Example: Identifying Discrete Random Variables

#### Question

Which of the following are discrete random variables?

1. The number of heads obtained when a coin is flipped $6$ times

2. The number of times a $6$-sided die is rolled until a $6$ appears

3. The number of months in a particular year

#### Explanation

A random variable is a variable whose value is determined by the outcome of a trial or experiment.

A ** random variable is a random variable

- that has finitely many possible values, or

- whose possible values can be listed in a sequence: $x_1, x_2, x_3, \ldots$

Remember that a real interval (e.g. $(a,b)$ or $[a,b]$) cannot be listed in a sequence.

With that in mind, let's consider each of the given statements.

- Statement I describes a discrete random variable. Its value is determined by the result of an experiment, and its possible values can be listed in a sequence: $0,1,2,3,4,5,6.$

- Statement II describes a discrete random variable. Its value is determined by the result of an experiment, and we can count its possible values in a sequence: $1,2,3,\ldots$

- Statement III does ** describe a discrete random variable. The number of months in a particular year is not the outcome of a trial or experiment. (By definition, there are $12$ months in a year.)

Therefore, the correct answer is "I and II only."

### The Probability Mass Function for a Discrete Random Variable

The **probability distribution**, or more precisely, **probability mass function** of a discrete random variable $X$ on a set $S$ is a function $f(x)$ that maps each element $x \in S$ to its probability of occurring:

$$


P(X = x) = f(x)


$$

The above can be read as "the probability that the random variable $X$ takes on the value $x,$ is equal to $f(x).$"

For example, if $X$ is the result of rolling a $6$-sided die, then we have

$$


\begin{aligned}\frac{1}{6},\, & 𝑥=1,2,3,4,5,6 \\ 0,\, & otherwise.\end{aligned}


$$

This function tells us that

- the probability of the die landing on any integer between $1$ and $6$ inclusive is $\dfrac{1}{6},$ and

- the probability of the die landing on any other number is zero.

We can also represent this probability mass function using a table, as follows:

### Conditions for a Function To Be a Valid Probability Mass Function

In general, for a function $f(x)$ to be a valid probability mass function for a random variable $X$ on a set $S,$ it must satisfy the following conditions:

- $0 \leq f(x) \leq 1$ for all $x$ in $S$

- $\displaystyle \sum\limits_{x \in S} f(x) = 1$

There is some nice intuition to the conditions above.

- The condition $0 \leq f(x) \leq 1$ for all $x$ in $S$ states that any possible outcome for $X$ must have a probability between $0$ and $1.$

- The condition $\displaystyle \sum\limits_{x \in S} f(x) = 1$ states that the sum of all the probabilities over all possible values of $X$ must add up to $1.$

### Example: Identifying Probability Mass Functions

#### Question

Which of the following functions are valid probability mass functions?

$$


\begin{aligned}𝑓(𝑥)=\begin{aligned}\frac{2}{5}, & 𝑥=0 \\ −\frac{1}{5}, & 𝑥=1 \\ \frac{4}{5}, & 𝑥=2\end{aligned}\,𝑔(𝑥)=\begin{aligned}\frac{2}{5}, & 𝑥=0 \\ \frac{3}{10}, & 𝑥=1\end{aligned}\,ℎ(𝑥)=\begin{aligned}\frac{3}{10}, & 𝑥=0 \\ \frac{1}{2}, & 𝑥=1 \\ \frac{1}{5}, & 𝑥=2\end{aligned}\,\end{aligned}


$$

#### Explanation

For a function $f(x)$ to be a valid probability mass function on a set $S,$ it must satisfy the following conditions:

- $0 \leq f(x) \leq 1$ for all $x$ in $S$

- $\displaystyle \sum\limits_{x \in S} f(x) = 1$

Let's check the above conditions for each of the given functions.

- The function $f$ is ** a valid probability distribution because the value $f(1)=-\dfrac15$ does not satisfy the first condition (it is not between $0$ and $1$).

- The function $g$ is ** a valid probability distribution because it does not satisfy the second condition. The values of $h$ do not sum to $1{:}$

- The function $h$ is a valid probability distribution. Indeed, we have and

Therefore, the correct answer is "$h$ only."

### Example: Computing the Probability That a Discrete Random Variable Lies Within a Set of Values

#### Question

Compute $P\left(X\in \{2,4,6\}\right)$ given that the random variable $X$ has the probability mass function $f(x)$ shown in the table above.

#### Explanation

Using the values in the table, we have

$$


\begin{aligned}𝑃(𝑋∈{2,4,6}) & =𝑃(𝑋=2)+𝑃(𝑋=4)+𝑃(𝑋=6) \\ & =𝑓(2)+𝑓(4)+𝑓(6) \\ & =0.1+0.1+0.2 \\ & =0.4.\end{aligned}


$$

### Example: Computing the Probability That a Discrete Random Variable Lies Within an Interval

#### Question

Compute $P\left(X \leq 3 \right)$ given that the random variable $X$ has the probability mass function shown in the table above.

#### Explanation

Using the values in the table, we have

$$


\begin{aligned}𝑃(𝑋≤3) & =𝑃(𝑥∈{1,2,3}) \\ & =𝑃(𝑋=1)+𝑃(𝑋=2)+𝑃(𝑋=3) \\ & =\frac{1}{5}+\frac{3}{10}+\frac{1}{10} \\ & =\frac{3}{5}.\end{aligned}


$$
