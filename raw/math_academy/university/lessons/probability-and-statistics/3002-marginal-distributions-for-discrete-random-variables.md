# Marginal Distributions for Discrete Random Variables

Source: https://www.mathacademy.com/topics/3002?courseId=73
Topic ID: 3002

## Prerequisites

- [The Law of Total Probability](./773-the-law-of-total-probability.md)
- [Joint Distributions for Discrete Random Variables](./3001-joint-distributions-for-discrete-random-variables.md)

## Lesson

### Introduction

The joint PMF $f(x,y)$ of two discrete random variables $X$ and $Y$ tells us all possible events $(X, Y)$ and the probabilities associated with each event. However, suppose we wish to determine the probability mass function for $X$ only. How can this be deduced from the joint PMF?

Let's build some intuition by considering an example.

Consider the joint probability mass function $f(x,y)$ for the discrete random variables $X$ and $Y,$ shown below.

The support of $X$ is $S_X = \{{\color{blue}{1}},{\color{red}{2}}\}.$ Let's now deduce the probabilities associated with each value of $X$ in $S_X\mathbin{:}$

- According to the law of total probability, we can deduce $P(X=1)$ by summing the values in the first row of the table, as follows: Notice that we summed over all possible values of $Y$ associated with $X=1.$

- Similarly, by summing the values in the second row in the table, we have Notice that we summed over all possible values of $Y$ associated with $X=2.$

Therefore, the probability mass function for $X$ is as follows:

Notice that we have used the notation $f_X(x).$ Since $f_X(x)$ was deduced from the joint probability mass function $f(x,y),$ we call $f_X(x)$ the **marginal mass function** for $X.$

### Deducing the Marginal Mass Function for Y

Let's go back to the last example for the random variables $X$ and $Y.$

We saw that the marginal mass function $f_X$ for $X$ is found by summing the rows in the table. So let's add the sum of each row to our table:

Notice how we wrote the values of the *marginal* mass function in the right *margin* of the table.

From here, we can immediately deduce that

$$


P(X=1) = f_X(1) = 0.2, \qquad P(X=2) = f_X(2) = 0.8.


$$

Similarly, we can compute the marginal mass function of $Y,$ denoted $f_Y(y),$ by summing the columns. Adding these totals to our table, we get the following:

Again, notice how we wrote the values of the *marginal* mass function in the bottom *margin* of the table.

From here, we can immediately deduce that

$$


P(Y={\color{blue}{1}}) = f_Y({\color{blue}{1}}) = 0.75, \qquad P(Y={\color{red}{2}}) = f_Y({\color{red}{2}}) = 0.25.


$$

Finally, the marginal mass function $f_Y(y)$ of $Y$ is as follows:

### A Formal Definition of the Marginal Mass Function

Now that we've built some intuition, let's define the marginal mass functions formally.

Let $f(x,y)$ be the joint PMF of the discrete random variables $X$ and $Y$ with supports $S_X$ and $S_Y$, respectively.

- The **marginal mass function** of $X,$ denoted $f_X(x),$ is defined as

- The **marginal mass function** of $Y,$ denoted $f_Y(y),$ is defined as

We can relate these definitions to our previous intuition:

- The first definition states that, to compute $P(X=x)$ for some particular value $x,$ we sum all possible values of $Y$ in the row corresponding to $X=x.$

- The second definition states that, to compute $P(Y=y)$ for some particular value $y,$ we sum all possible values of $X$ in the column corresponding to $Y=y.$

Finally, note that marginal mass functions are sometimes called **marginal probability mass functions**, **marginal PMFs**, or (less formally) **marginal distributions**.

### Example: Finding a Marginal Probability

#### Question

Given the joint probability distribution $f(x,y)$ below for the discrete random variables $X$ and $Y,$ find $P(X = 0).$

#### Explanation

If the random variables $X$ and $Y$ have joint distribution with joint probability mass function $f(x,y),$ then we have

$$


\begin{aligned}𝑃(𝑋=𝑥) & =𝑓_{𝑋}(𝑥)=\underset{𝑦}{∑}𝑓(𝑥,𝑦) \\ 𝑃(𝑌=𝑦) & =𝑓_{𝑌}(𝑦)=\underset{𝑥}{∑}𝑓(𝑥,𝑦)\end{aligned}


$$

where $f_X(x)$ and $f_Y(y)$ are the marginal mass functions for $X$ and $Y,$ respectively.

In this case, the marginal distribution for $X$ corresponds to the row totals, and the marginal distribution for $Y$ corresponds to the column totals. Let's add these row and column totals to our table:

Finally, using the table, we have

$$


\begin{aligned}𝑃(𝑋=0) & =𝑓_{𝑋}(0) \\ & =𝑓(0,0)+𝑓(0,1) \\ & =\frac{1}{6}+\frac{5}{12} \\ & =\frac{7}{12}.\end{aligned}


$$

### Example: Finding a Marginal Probability Distribution

#### Question

Given the joint probability mass function $f(x,y)$ above for the discrete random variables $X$ and $Y,$ find the marginal mass function for $X.$

#### Explanation

If the random variables $X$ and $Y$ have joint distribution with joint probability mass function $f(x,y),$ then we have

$$


\begin{aligned}𝑃(𝑋=𝑥) & =𝑓_{𝑋}(𝑥)=\underset{𝑦}{∑}𝑓(𝑥,𝑦) \\ 𝑃(𝑌=𝑦) & =𝑓_{𝑌}(𝑦)=\underset{𝑥}{∑}𝑓(𝑥,𝑦)\end{aligned}


$$

where $f_X(x)$ and $f_Y(y)$ are the marginal mass functions for $X$ and $Y,$ respectively.

In this case, the marginal distribution for $X$ corresponds to the row totals, and the marginal distribution for $Y$ corresponds to the column totals. Let's add these row and column totals to our table:

Finally, the marginal mass function for $X$ is given by the following table:

### Example: Finding a Cumulative Probability Given a Joint Distribution

#### Question

Given the joint probability mass function $f(x,y)$ above for the discrete random variables $X$ and $Y,$ calculate $P(X \geq 2).$

#### Explanation

If the random variables $X$ and $Y$ have joint distribution with joint probability mass function $f(x,y),$ then we have

$$


\begin{aligned}𝑃(𝑋=𝑥) & =𝑓_{𝑋}(𝑥)=\underset{𝑦}{∑}𝑓(𝑥,𝑦) \\ 𝑃(𝑌=𝑦) & =𝑓_{𝑌}(𝑦)=\underset{𝑥}{∑}𝑓(𝑥,𝑦)\end{aligned}


$$

where $f_X(x)$ and $f_Y(y)$ are the marginal mass functions for $X$ and $Y,$ respectively.

In this case, the marginal distribution for $X$ corresponds to the row totals, and the marginal distribution for $Y$ corresponds to the column totals. Let's add these row and column totals to our table:

The marginal mass function for $X$ is given in the following table:

Finally, using the table of values of the marginal mass function for $X,$ we have

$$


\begin{aligned}𝑃(𝑋≥2) & =𝑃(𝑋∈{2,3}) \\ & =𝑃(𝑋=2)+𝑃(𝑋=3) \\ & =0.5+0.25 \\ & =0.75.\end{aligned}


$$
