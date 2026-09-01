# The Trinomial Distribution

Source: https://www.mathacademy.com/topics/2989?courseId=73
Topic ID: 2989

## Prerequisites

- [Permutations With Repetition](./1341-permutations-with-repetition.md)
- [Modeling With the Binomial Distribution](./1395-modeling-with-the-binomial-distribution.md)
- [Independence of Discrete Random Variables](./3048-independence-of-discrete-random-variables.md)

## Lesson

### Introduction

Suppose there are $3$ red, $2$ green, and $5$ blue balls in a box. Let's consider a sequence of $5$ independent draws of one ball from the box *with replacement* (i.e., we put the ball back in the box after drawing it). So, on each draw, we have

$$


P(\text{red}) = \dfrac{3}{10}, \qquad P(\text{green}) = \dfrac{2}{10}, \qquad P(\text{blue}) = \dfrac{5}{10}.


$$

Suppose we draw $5$ balls and get the following sequence:

$$


\text{red},\qquad \text{green}, \qquad \text{green}, \qquad \text{blue}, \qquad \text{blue}.


$$

The probability of getting precisely this sequence of balls is

$$


\left(\dfrac{3}{10}\right)^{1}\cdot \left(\dfrac{2}{10}\right)^{2}\cdot \left(\dfrac{5}{10}\right)^{2}.


$$

Now, suppose we were interested in finding the probability of getting one red, two green, and two blue balls *in any order*. In other words, we wish to calculate the joint probability

$$


P(X_1 = 1, X_2 = 2, X_3 = 2)


$$

where $X_1,$ $X_2,$ and $X_3$ are the numbers of red, green, and blue balls drawn from the box, respectively. To find this probability, we must multiply the probability we found earlier by the number of possible permutations of $1$ red, $2$ green, and $2$ blue balls.

The exact number of possible permutations is given by the trinomial coefficient

$$


(\begin{aligned}5 \\ 1,2,2\end{aligned})


$$

Therefore, the probability of getting $1$ red, $2$ green, and $2$ blue balls *in any order* is

$$


P(X_1 = 1, X_2 = 2, X_3 = 2) = \dfrac{5!}{1!\ 2!\ 2!} \cdot \left(\dfrac{3}{10}\right)^{1}\cdot \left(\dfrac{2}{10}\right)^{2}\cdot \left(\dfrac{5}{10}\right)^{2}.


$$

The tuple $X = (X_1, X_2, X_3)$ is an example of a **trinomial random variable**.

### The Trinomial Distribution

Consider a random experiment with three mutually exclusive and exhaustive events $A_1, A_2,$ and $A_3$ with $p_i = P(A_i)$ for $i=1,2,3.$ Thus,

$$


p_1 + p_2 + p_3 = 1.


$$

We repeat the experiment $n$ times independently. Let the random variables $X_1, X_2$, and $X_3$ be the number of times that events $A_1$, $A_2,$ and $A_3$ occur, respectively. Then, we say that the random vector

$$


X = (X_1, X_2, X_3)


$$

follows a **trinomial distribution** with parameters $n$ and $p=(p_1,p_2,p_3),$ and we write

$$


X \sim \text{Trinomial}(n, (p_1,p_2,p_3)).


$$

The **trinomial probability mass function** of $X\sim \text{Trinomial}(n, (p_1,p_2,p_3))$ is given by

$$


f(x_1,x_2,x_3)=P(X_1=x_1,X_2=x_2,X_3=x_3)=\dfrac{n!}{x_1!\,x_2!\,x_3!}p_1^{x_1}p_2^{x_2}p_3^{x_3},


$$

where $x_i$ are nonnegative integers, $x_1+x_2+x_3=n,$ and $p_1+p_2+p_3=1$.

Let's break this down:

- The product $p_1^{x_1}p_2^{x_2}p_3^{x_3}$ gives the probability of getting a specific arrangement.

- However, there are many ways to get $X_1 = x_1, X_2 = x_2$ and $X_3 = x_3.$ The exact number of possible permutations is given by the trinomial coefficient

The marginal distributions of $X_1$, $X_2$, and $X_3$ are

$$


X_1 \sim B(n, p_1),\qquad X_2 \sim B(n,p_2), \qquad X_3 \sim B(n,p_3),


$$

with $p_1+p_2+p_3=1.$ This follows from the fact that $X_1$ is the number of "successes" in $n$ independent trials with $p_1$ being the probability of "successes" in each trial (similarly, for $X_2$ and $X_3$).

**Note:** The random variables $X_1, X_2,$ and $X_3$ are *dependent* because if we multiply their marginal probability mass functions together, we don't get the trinomial probability mass function.

### Example: Computing a Trinomial Probability

#### Question

Given that $X \sim \text{Trinomial}(8, \mathbf{p})$ where $\mathbf{p}=(p_1,0.2,0.4),$ find $P(X_1=4, X_3=2).$

#### Explanation

Recall that the trinomial probability mass function of $X=(X_1,X_2,X_3)$ is given by

$$


f(x_1,x_2,x_3)=P(X_1=x_1,X_2=x_2,X_3=x_3)=\dfrac{n!}{x_1!\,x_2!\,x_3!} \, p_1^{x_1}p_2^{x_2}p_3^{x_3},


$$

where $x_i$ are nonnegative integers such that $x_1+x_2+x_3=n,$ and $p_1+p_2+p_3=1.$

As a result, we can solve for $p_1{:}$

$$


\begin{aligned}𝑝_{1}+𝑝_{2}+𝑝_{3} & =1 \\ 𝑝_{1}+0.2+0.4 & =1 \\ 𝑝_{1} & =0.4\end{aligned}


$$

We can also solve for $x_2{:}$

$$


\begin{aligned}𝑥_{1}+𝑥_{2}+𝑥_{3} & =8 \\ 2+𝑥_{2}+4 & =8 \\ 𝑥_{2} & =2\end{aligned}


$$

So, we have

$$


\begin{aligned} & 𝑛=8, \\ & 𝐩=(0.4,0.2,0.4) \\ & 𝑥_{1}=4,\,𝑥_{2}=2,\,𝑥_{3}=2.\end{aligned}


$$

Therefore, for our trinomial random variable $X,$ we obtain

$$


\begin{aligned}𝑃(𝑋_{1}=4,𝑋_{3}=2) & =𝑃(𝑋_{1}=4,𝑋_{2}=2,𝑋_{3}=2) \\ & =\frac{8!}{4!\,2!\,2!}\,(0.4)^{4}(0.2)^{2}(0.4)^{2} \\ & ≈0.0688,\end{aligned}


$$

rounded to $4$ decimal places.

### Example: Computing a Trinomial Probability Over an Interval

#### Question

Given $X \sim\text{Trinomial}(5, \mathbf{p})$ where $\mathbf{p}=(0.4,0.5,0.1),$ compute $P(1 \leq X_1 < 3, X_2=1).$

#### Explanation

Recall that the trinomial probability mass function of $X=(X_1,X_2,X_3)$ is given by

$$


f(x_1,x_2,x_3)=P(X_1=x_1,X_2=x_2,X_3=x_3)=\dfrac{n!}{x_1!\,x_2!\,x_3!} \, p_1^{x_1}p_2^{x_2}p_3^{x_3},


$$

where $x_i$ are nonnegative integers such that $x_1+x_2+x_3=n,$ and $p_1+p_2+p_3=1.$

In our case, we have

$$


\begin{aligned} & 𝑛=5,\,𝐩=(0.4,0.5,0.1)\end{aligned}


$$

and

$$


\begin{aligned}𝑥_{3} & =𝑛−𝑥_{1}−𝑥_{2} \\ & =5−𝑥_{1}−𝑥_{2}.\end{aligned}


$$

Therefore, for our trinomial random variable $X,$ we obtain

$$


\begin{aligned}𝑃(1≤𝑋_{1}<3,𝑋_{2}=1) & =𝑃(𝑋_{1}∈{1,2},𝑋_{2}=1) \\ & =𝑃(𝑋_{1}=1,𝑋_{2}=1) \\ & +𝑃(𝑋_{1}=2,𝑋_{2}=1) \\ & =𝑃(𝑋_{1}=1,𝑋_{2}=1,𝑋_{3}=3) \\ & +𝑃(𝑋_{1}=2,𝑋_{2}=1,𝑋_{3}=2) \\ & =\frac{5!}{1!\,1!\,3!}(0.4)^{1}(0.5)^{1}(0.1)^{3}+\frac{5!}{2!\,1!\,2!}(0.4)^{2}(0.5)^{1}(0.1)^{2} \\ & =0.004+0.024 \\ & =0.028.\end{aligned}


$$

### Example: Computing a Trinomial Probability in Context

#### Question

At a ticket counter, the probability that a person buys no tickets, one ticket, or two or more tickets is $0.4,$ $0.4,$ and $0.2,$ respectively. If $6$ people visit the counter, find the probability that exactly $2$ people buy no tickets and exactly $3$ buy one ticket.

#### Explanation

Let $X_1,$ $X_2,$ and $X_3$ be the number of people who buy zero, one, or at least two tickets, respectively. Then, the corresponding probabilities are

$$


p_1=0.4, \qquad p_2=0.4, \qquad p_3=0.2.


$$

This situation can be modeled using a trinomial distribution.

Recall that the trinomial probability mass function of $X=(X_1,X_2,X_3)$ is given by

$$


f(x_1,x_2,x_3)=P(X_1=x_1,X_2=x_2,X_3=x_3)=\dfrac{n!}{x_1!\,x_2!\,x_3!} \, p_1^{x_1}p_2^{x_2}p_3^{x_3},


$$

where $x_i$ are nonnegative integers such that $x_1+x_2+x_3=n,$ and $p_1+p_2+p_3=1.$

In our case, we have

$$


\begin{aligned} & 𝑛=6,\,𝐩=(0.4,0.4,0.2),\,𝑥_{1}=2,\,𝑥_{2}=3\end{aligned}


$$

and

$$


\begin{aligned}𝑥_{3} & =𝑛−𝑥_{1}−𝑥_{2} \\ & =6−2−3 \\ & =1.\end{aligned}


$$

Therefore, for our trinomial random variable $X,$ we obtain

$$


\begin{aligned}𝑃(𝑋_{1}=2,𝑋_{2}=3,𝑋_{3}=1) & =\frac{6!}{2!\,3!\,1!}(0.4)^{2}(0.4)^{3}(0.2)^{1} \\ & ≈0.123\end{aligned}


$$

rounded to $2$ decimal places.
