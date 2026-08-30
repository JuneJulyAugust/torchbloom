# The Multinomial Distribution

Source: https://www.mathacademy.com/topics/5394?courseId=73
Topic ID: 5394

## Prerequisites

- [The Trinomial Distribution](./2989-the-trinomial-distribution.md)

## Lesson

### Introduction

Consider a trial that results in exactly one of some fixed finite number $k$ of mutually exclusive outcomes with probabilities $p_1$, $p_ 2, \ldots, p_k$ such that

$$


p_1+p_2+\ldots+p_k=1


$$

and there are $n$ independent trials.

Let the random variables $X_i$ indicate the number of times outcome $i$ was observed over the $n$ trials. Then, the tuple

$$


X = (X_1, X_2, \ldots, X_k)


$$

follows a **multinomial distribution** with parameters $n$ and $p=(p_1,p_2,\ldots,p_k)$, and we write

$$


X \sim \text{Multinomial}(n, p).


$$

For example, suppose we throw a fair tetrahedral die $10$ times. Let the random variables $X_i$ for $i = 1, 2,3,4$ denote the number of times $i$ is observed. Then, the random tuple

$$


X = (X_1, X_2, X_3, X_4)


$$

follows a multinomial distribution. We have $p_i=\dfrac{1}{4}$ for all $i,$ and

$$


X \sim \text{Multinomial}\left(10, \left(\dfrac 14,\dfrac 14, \dfrac 14, \dfrac 14\right)\right).


$$

The **multinomial probability mass function** of $X=(X_1,\ldots, X_k) \sim \text{Multinomial}(n, p)$ is given by

$$


f(x_1,x_2,\ldots,x_k)=P(X_1=x_1,X_2=x_2,\ldots,X_{k}=x_{k})=\dfrac{n!}{x_1!\,x_2!\,\cdots\, x_k!}p_1^{x_1}p_2^{x_2}\cdot\ldots\cdot p_k^{x_k},


$$

where the $x_i$'s are nonnegative integers that sum to $n.$

Finally, note that the marginal distribution of each $X_i$ is

$$


X_i\sim B(n,p_j).


$$

### Example: Computing a Probability at a Point

#### Question

Given that $X \sim \text{Multinomial}(10, \mathbf{p})$ where $\mathbf{p}=(p_1,0.1,0.2,0.5),$ find $P(X_2=1,X_3=2,X_4=3).$ Round your answer to $3$ decimal places.

#### Explanation

Recall that the multinomial probability mass function of $X\sim \text{Multinomial}(n, \mathbf{p})$ is given by

$$


f(x_1,x_2,\ldots,x_k)=\dfrac{n!}{x_1!\,x_2!\, \cdots \,x_k!} \, p_1^{x_1}p_2^{x_2}\cdots p_k^{x_k},


$$

where $x_i$ are nonnegative integers such that $\displaystyle\sum\limits_{i=1}^k x_i = n$ and $\displaystyle\sum\limits_{i=1}^k p_i = 1.$

As a result, we can solve for $p_1{:}$

$$


\begin{aligned}𝑝_{1}+𝑝_{2}+𝑝_{3}+𝑝_{4} & =1 \\ 𝑝_{1}+0.1+0.2+0.5 & =1 \\ 𝑝_{1} & =0.2\end{aligned}


$$

We can also solve for $x_1{:}$

$$


\begin{aligned}𝑥_{1}+𝑥_{2}+𝑥_{3}+𝑥_{4} & =𝑛 \\ 𝑥_{1}+1+2+3 & =10 \\ 𝑥_{1} & =4\end{aligned}


$$

So, we have

$$


\begin{aligned} & 𝑛=10,\,𝐩=(0.2,0.1,0.2,0.5),\,𝑥_{1}=4,\,𝑥_{2}=1,\,𝑥_{3}=2,\,𝑥_{4}=3.\end{aligned}


$$

Therefore, for our multinomial random variable $X,$ we obtain

$$


\begin{aligned}𝑃(𝑋_{2}=1,𝑋_{3}=2,𝑋_{4}=3) & =𝑃(𝑋_{1}=4,𝑋_{2}=1,𝑋_{3}=2,𝑋_{4}=3) \\ & =𝑓(4,1,2,3) \\ & =\frac{10!}{4!\,1!\,2!\,3!}(0.2)^{4}(0.1)^{1}(0.2)^{2}(0.5)^{3} \\ & ≈0.010\end{aligned}


$$

rounded to $3$ decimal places.

### Example: Computing a Multinomial Probability Over an Interval

#### Question

Given $X \sim\text{Multinomial}(7, \mathbf{p})$ where $\mathbf{p}=(0.1,0.2,0.2,0.5),$ compute $P(X_1=1, 1 < X_2 \leq 3, X_3=2).$ Round your answer to $3$ decimal places.

#### Explanation

Recall that the multinomial probability mass function of $X\sim \text{Multinomial}(n, \mathbf{p})$ is given by

$$


f(x_1,x_2,\ldots,x_k)=\dfrac{n!}{x_1!\,x_2!\, \cdots \,x_k!} \, p_1^{x_1}p_2^{x_2}\cdots p_k^{x_k},


$$

where $x_i$ are nonnegative integers such that $\displaystyle\sum\limits_{i=1}^k x_i = n$ and $\displaystyle\sum\limits_{i=1}^k p_i = 1.$

In our case, we have

$$


\begin{aligned} & 𝑛=7,\,𝐩=(0.1,0.2,0.2,0.5)\end{aligned}


$$

and

$$


\begin{aligned}𝑥_{4} & =𝑛−𝑥_{1}−𝑥_{2}−𝑥_{3} \\ & =7−𝑥_{1}−𝑥_{2}−𝑥_{3}.\end{aligned}


$$

Therefore, for our multinomial random variable $X,$ we obtain

$$


\begin{aligned}𝑃(𝑋_{1}=1,1<𝑋_{2}≤3,𝑋_{3}=2) & =𝑃(𝑋_{1}=1,𝑋_{2}∈{2,3},𝑋_{3}=2) \\ & =𝑃(𝑋_{1}=1,𝑋_{2}=2,𝑋_{3}=2) \\ & =\,+𝑃(𝑋_{1}=1,𝑋_{2}=3,𝑋_{3}=2) \\ & =𝑃(𝑋_{1}=1,𝑋_{2}=2,𝑋_{3}=2,𝑋_{4}=2) \\ & =\,+𝑃(𝑋_{1}=1,𝑋_{2}=3,𝑋_{3}=2,𝑋_{4}=1) \\ & =\frac{7!}{1!\,2!\,2!\,2!}(0.1)^{1}(0.2)^{2}(0.2)^{2}(0.5)^{2} \\ & =\,+\frac{7!}{1!\,3!\,2!\,1!}(0.1)^{1}(0.2)^{3}(0.2)^{2}(0.5)^{1} \\ & ≈0.032\end{aligned}


$$

rounded to $3$ decimal places.

### Example: Computing a Multinomial Probability in Context

#### Question

In an ice cream parlor, the probability that a customer buys chocolate, strawberry, vanilla, or another flavor of ice cream is $0.3,$ $0.2,$ $0.1,$ and $0.4$, respectively. If $7$ customers enter the ice cream parlor, find the probability that $2$ will buy chocolate, $1$ will buy strawberry, and $2$ will buy vanilla ice cream. Round your answer to $3$ decimal places.

#### Explanation

Let $X_1,$ $X_2, X_3,$ and $X_4$ be the number of customers that buy chocolate, strawberry, vanilla, or another flavor of ice cream, respectively. Then, the corresponding probabilities are

$$


p_1=0.3, \qquad p_2=0.2, \qquad p_3=0.1, \qquad p_4=0.4.


$$

This situation can be modeled using a multinomial distribution.

Recall that the multinomial probability mass function of $X\sim \text{Multinomial}(n, \mathbf{p})$ is given by

$$


f(x_1,x_2,\ldots,x_k)=\dfrac{n!}{x_1!\,x_2!\, \cdots \,x_k!} \, p_1^{x_1}p_2^{x_2}\cdots p_k^{x_k},


$$

where $x_i$ are nonnegative integers such that $\displaystyle\sum\limits_{i=1}^k x_i = n$ and $\displaystyle\sum\limits_{i=1}^k p_i = 1.$

In our case, we have

$$


\begin{aligned} & 𝑛=7,\,𝐩=(0.3,0.2,0.1,0.4)\,𝑥_{1}=2,\,𝑥_{2}=1,\,𝑥_{3}=2\end{aligned}


$$

and

$$


\begin{aligned}𝑥_{4} & =𝑛−𝑥_{1}−𝑥_{2}−𝑥_{3} \\ & =7−2−1−2 \\ & =2.\end{aligned}


$$

Therefore, for our multinomial distribution $X,$ we obtain

$$


\begin{aligned}𝑃(𝑋_{1}=2,𝑋_{2}=1,𝑋_{3}=2,𝑋_{4}=2) & =\frac{7!}{2!\,1!\,2!\,2!}(0.3)^{2}(0.2)^{1}(0.1)^{2}(0.4)^{2} \\ & ≈0.018.\end{aligned}


$$
