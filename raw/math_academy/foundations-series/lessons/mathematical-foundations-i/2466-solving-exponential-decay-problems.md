# Solving Exponential Decay Problems

Source: https://www.mathacademy.com/topics/2466?courseId=113
Topic ID: 2466

## Prerequisites

- [Interpreting Exponential Decay](./1629-interpreting-exponential-decay.md)

## Lesson

### Introduction

We can use our knowledge of exponential equations to extract helpful information from a process that undergoes exponential decay.

Suppose, for example, that the vegetation coverage of a town is decreasing exponentially due to rapid urbanization, and that the vegetation coverage $C(t)$ (measured in acres) of the town varies according to the function

$$


C(t) = 48 \left(\dfrac 1 2\right)^t,


$$

where $t$ is the number of years since urbanization began. Can we find how long it will take for the vegetation coverage to reduce to only $3$ acres?

To find the time taken for the vegetation cover to fall to $3$ acres, we need to solve the equation $C(t) = 3$. Setting up the equation, we have

$$


48 \left(\dfrac 1 2\right)^t = 3.


$$

To solve this equation, we first isolate the exponential term by dividing both sides by $48\mathbin{:}$

$$


\begin{aligned}\frac{48(\frac{1}{2})^{𝑡}}{2} & =\frac{3}{48} \\ \frac{48(\frac{1}{2})^{𝑡}}{2} & =\frac{3}{48} \\ (\frac{1}{2})^{𝑡} & =\frac{3}{48} \\ (\frac{1}{2})^{𝑡} & =\frac{1}{16}\end{aligned}


$$

Now, we notice that $16 = 2^4,$ and so we can rewrite the right-hand side as follows:

$$


\begin{aligned}(\frac{1}{2})^{𝑡} & =\frac{1}{16} \\ (\frac{1}{2})^{𝑡} & =\frac{1}{2^{4}} \\ (\frac{1}{2})^{𝑡} & =(\frac{1}{2})^{4}\end{aligned}


$$

Since both sides of the equation now have the same base, we can equate the exponents. This gives

$$


{\color{blue}{t}} = {\color{blue}{4}}.


$$

Therefore, it will take $4$ years for the vegetation cover to reduce to $3$ acres.

### Example: Creating an Exponential Decay Model Using a Decay Factor

#### Question

The number of participants of a webinar reduces by $\dfrac 1 8$ every hour. If the webinar started with $900$ participants, find an equation that determines how long it will take for the number of participants to reduce to $140.$

#### Explanation

Since the number of participants reduces by $\dfrac{1}{8}$ every hour, this means that every hour, $\dfrac{7}{8}$ of the previous hour's participants remain. So the decay factor is $\dfrac 7 8.$

The formula for exponential decay (in terms of a decay factor $b$) is

$$


y = ab^t.


$$

In this case, we have the following:

- $a=900$ is the initial number of participants.

- $b = \dfrac 7 8$ is the decay factor.

- $t=$ the time, in hours, since the webinar started.

Therefore, the correct expression for $y(t)$ is

$$


y(t)= 900\cdot \left(\dfrac 7 8\right)^{t}.


$$

Since we want to know how long it takes for the number of participants to decrease to $140$, we need to solve $y(t)=140.$ This gives

$$


900\cdot \left(\dfrac{7}{8}\right)^t = 140.


$$

### Example: Creating an Exponential Decay Model Using a Decay Rate

#### Question

A car was purchased for $13\,000.$ It's known that the value of this particular model depreciates at a rate of $20\%$ per year. Find an equation that determines the number of years it takes for the car's value to reduce to $8\, 320.$

#### Explanation

The value of the car $y(t)$ decreases exponentially with a decay rate of $20\%.$

The formula for exponential decay (in terms of a decay rate $r$) is

$$


y(t) = a(1-r)^t.


$$

In this case, we have the following:

- $a=13\,000$ is the purchase price, in dollars.

- $r = 0.2$ is the decay rate ($20\%$ expressed as a decimal).

- $t=$ the time, in years, since the vehicle was purchased.

Therefore, the correct expression for $y(t)$ is

$$


y(t)= 13\, 000 \cdot (1-0.2)^t = 13\, 000 \cdot (0.8)^t.


$$

Since we want to know how long it takes for the car's value to decrease to $8\,320$, we need to solve the equation $y(t) =8\,320.$ This gives

$$


13\, 000 \cdot (0.8)^t = 8\,320.


$$

### Example: Solving for an Unknown Initial Value

#### Question

Due to server migration, the occupied disk space $S(t)$ (measured in $\text{GB}$) of a web server reduces exponentially according to the function

$$


S(t)= S_0\left(0.8\right)^{t},


$$

where $t$ is the time, in hours, since the migration began, and $S_0$ is the amount of disk space that the server occupied initially. If the server occupied $55 \text{GB}$ of storage twelve hours after the migration began, what was the initial amount of disk space that the server used?

#### Explanation

We know that $S(12) = 55,$ so we substitute this into the formula for $S(t).$ This gives

$$


55 =S_0\left(0.8\right)^{12}.


$$

We now solve for $S_0,$ as follows:

$$


\begin{aligned}\frac{55}{(0.8)^{12}} & =\frac{𝑆_{0}(0.8)^{12}}{(0.8)^{12}} \\ \frac{55}{(0.8)^{12}} & =\frac{𝑆_{0}(0.8)^{12}}{(0.8)^{12}} \\ \frac{55}{(0.8)^{12}} & =𝑆_{0} \\ 𝑆_{0} & =\frac{55}{(0.8)^{12}}\end{aligned}


$$

Evaluating this expression on a calculator, we get

$$


S_0\approx 800.


$$

Therefore, we conclude that the initial disk usage of the server was around $800\,\text{GB}.$
