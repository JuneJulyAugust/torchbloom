# Modeling Exponential Decay With Functions

Source: https://www.mathacademy.com/topics/2472?courseId=113
Topic ID: 2472

## Prerequisites

- [Creating Exponential Decay Expressions](./142-creating-exponential-decay-expressions.md)
- [Exponential Functions](./1153-exponential-functions.md)
- [Degrees of Accuracy](./2234-degrees-of-accuracy.md)

## Lesson

### Introduction

To model an exponential decay situation, it is often useful to start by setting up a function which represents the exponential decay. Then, we can evaluate that function as needed.

For example, suppose that a car's value depreciates by one-fifth every year. If the car was purchased for $25\,000,$ then what function gives the car's value after $t$ years?

First, note that if the car's value reduces by $\dfrac 1 5$ every year, then $\dfrac 4 5$ of its value remains every year.

Let's write down what we know:

- $a = 25\,000$ is the **initial value** of the car (in dollars).

- $b = \dfrac 4 5$ is the **decay factor**.

- $t=$ the time, in years.

Let $y(t)$ be the car's value after $t$ years. The formula for $y(t)$ is given by

$$


y(t) = ab^t.


$$

Substituting our values for $a$ and $b,$ we get

$$


y(t) = 25\,000\left(\dfrac 4 5\right)^t.


$$

To find the value of the car after $5$ years, we substitute $t=5$ into the above:

$$


\begin{aligned}𝑦(5)=25\,000⋅(\frac{4}{5})^{5}=8\,192\end{aligned}


$$

Therefore, the car will be worth $ 8\,192$ in $5$ years.

### Example: Modeling Exponential Decay Using a Decay Factor

#### Question

A mountain has a glacier with a depth of $75\,\text{m}.$ The depth of the glacier reduces by $\dfrac{1}{4}$ every year. Construct a function that represents the depth $d(t)$ of the glacier after $t$ years.

#### Explanation

The depth of the glacier is $75\,\text{m},$ and this reduces by $\dfrac{1}{4}$ every year. Therefore, the depth decays exponentially with a decay factor of $\dfrac 3 4.$

The formula for exponential decay (in terms of a decay factor $b$) is

$$


d(t) = ab^t.


$$

In our case, we have the following:

- $a=75 \text{m}$ is the initial depth of the glacier.

- $b = \dfrac 3 4$ is the decay factor.

- $t =$ the time, in years.

Therefore, the correct expression for the depth $d(t)$ is

$$


d(t)= 75 \cdot \left(\dfrac 3 4\right)^{t}.


$$

### Modeling Exponential Decay Using a Decay Rate

It's common to use a **decay rate** (rather than a decay factor) when describing exponential decay. A decay rate is typically expressed using a percent.

For example, suppose that after treatment with a particular antibiotic, the number of infected cells in a specimen decreased by $30\%$ per hour. If there were approximately $5$ million infected cells at the beginning of the treatment, how many infected cells remained after $3$ hours?

Let $y(t)$ be the number of infected cells after $t$ hours. The formula for exponential decay (in terms of a decay rate $r$) is

$$


y = a(1-r)^t.


$$

Notice that this is very similar to the formula for exponential growth. The difference here is that we have a minus $(-)$ instead of a plus $(+)$ in the parentheses.

In our case, we have:

- $a=5$ is the initial number of infected cells (in millions).

- $r = 0.30$ is the decay rate ($30\%$ expressed as a decimal).

- $t=$ the time, in hours.

Therefore, the correct expression for $y(t)$ is

$$


y = 5(1-0.3)^{t}.


$$

Simplifying the above gives

$$


y(t) =5(0.7)^{t}.


$$

Evaluating the function for $t=3$ hours, we get

$$


y(3) = 5(0.7)^{3} = 1.715.


$$

Therefore, after $3$ hours, there were $1.715$ million infected cells.

When writing down a formula for exponential decay, the key takeaway is this:

- If we're given a **decay rate** (usually expressed as a percent), then we use the formula $y(t) = a(1-r)^t.$

- If we're given a **decay factor**, then we use the formula $y(t) = ab^t.$

### Example: Modeling Exponential Decay Using a Decay Rate

#### Question

The number of members $m$ of a club after $t$ years is given by the formula

$$


m(t) = 766 \cdot (\textrm{\underline{\hspace{3em}}})^{t}.


$$

If there were $766$ members initially, and the number of members decreases by $22\%$ each year, what is the missing value in the expression for $m(t)?$

#### Explanation

The formula for exponential decay (in terms of a decay rate $r$) is

$$


m(t) = a(1-r)^t.


$$

In our case, we have the following:

- $a=766$ is the initial number of members.

- $r = 0.22$ is the decay rate ($22\%$ expressed as a decimal).

- $t=$ the time, in years.

Therefore, the correct expression for $m$ is

$$


m(t)= 766\cdot (1 - 0.22)^{t} = 766\cdot (0.78)^{t}.


$$

So, the missing number is $0.78.$
