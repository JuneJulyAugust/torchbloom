# Linear vs. Exponential Growth and Decay Models

Source: https://www.mathacademy.com/topics/3676?courseId=120
Topic ID: 3676

## Prerequisites

- [Linear vs. Exponential Growth and Decay](../../../high-school/traditional/lessons/algebra-i/1859-linear-vs-exponential-growth-and-decay.md)
- [Modeling Exponential Growth With Functions](../../../high-school/traditional/lessons/algebra-i/2471-modeling-exponential-growth-with-functions.md)
- [Modeling Exponential Decay With Functions](../../../high-school/traditional/lessons/algebra-i/2472-modeling-exponential-decay-with-functions.md)

## Lesson

### Introduction

In everyday life, some quantities vary linearly while others vary exponentially.

For example, suppose that Dominic collects rainwater in a flask during a storm. He measures the total amount of water in the flask every hour. The flask started with $2\,\textrm{mm}$ of rainwater, and he noticed that the volume of water in the flask increases by $10\,\textrm{mm}$ every hour. If $R(t)$ is a function that gives the amount of rainwater after $t$ hours, is $R(t)$ linear or exponential?

To solve this problem, we write down the amount of water in the flask every hour and try to spot a pattern:

- The initial amount of rainwater in the flask was $2\,\textrm{mm}.$

- After $1$ hour, there will be $2+10$ millimeters of water in the flask.

- After $\color{blue}2$ hours, there will be $2 + \underbrace{10 + 10}_{{10\,\cdot\, \color{blue}{2}}}$ millimeters of water in the flask.

- After $\color{blue}3$ hours, there will be $2 + \underbrace{10 + 10 + 10}_{10\,\cdot\, {\color{blue}{3}}}$ millimeters of water in the flask. $\quad\vdots$

- After $\color{blue}t$ hours, there will be $2+ \underbrace{10 +\cdots + 10}_{10\,\cdot\, {\color{blue}t}}$ millimeters of water in the flask.

Therefore, the amount of rainwater after $t$ hours is given by

$$


R(t) = 2+10t,


$$

which is a linear function.

Therefore, we conclude that $R(t)$ is linear because it increases by $10$ when $t$ increases by $1.$

### Example: Constructing a Model and Determining Whether Its Linear or Exponential

#### Question

Due to high performance, Anna's weekly bonus, which started at $150$, increases by $3\%$ every week. Let $B(t)$ be Anna's bonus after $t$ weeks. Is $B(t)$ an exponential or a linear function?

#### Explanation

Anna's weekly bonus started at $150,$ increasing by $3\%$ each week. Since $3\%$ as a decimal is $0.03,$ an increase of $3\%$ corresponds to multiplication by a factor of

$$


1+0.03 = 1.03.


$$

So, we have the following:

- After $1$ week, Anna's bonus will be $150\cdot (1.03)$ dollars.

- After $\color{blue}2$ weeks, Anna's bonus will be $150\cdot (1.03)^{\color{blue}{2}}$ dollars.

- After $\color{blue}3$ weeks, Anna's bonus will be $150\cdot (1.03)^{\color{blue}{3}}$ dollars. $\quad\vdots$

- After $\color{blue}t$ weeks, Anna's bonus will be $150\cdot(1.03)^{\color{blue}{t}}$ dollars.

Therefore,

$$


B(t) = 150\cdot(1.03)^t,


$$

which is an exponential growth function.

Finally, we conclude that $B(t)$ is exponential because it increases by a factor of $1.03$ when $t$ increases by $1.$

### Example: Identifying Whether a Model Increases or Decreases Either Linearly Or Exponentially

#### Question

A generator is consuming fuel from a storage tank: its fuel volume drops from $8{,}000$ liters to $6{,}000$ liters at a constant rate of $125$ liters per minute. If $F(t)$ denotes the fuel volume (in liters) after $t \geq 0$ minutes, what description best fits the function relating $F(t)$ and $t?$

#### Explanation

The initial fuel volume in the tank is $8{,}000$ liters.

- After $1$ minute, there will be $8{,}000 - 125$ liters in the tank.

- After $\color{blue}2$ minutes, there will be $8{,}000 \underbrace{\:-\: 125 - 125}_{{-\,125\,\cdot\, \color{blue}{2}}}$ liters in the tank.

- After $\color{blue}3$ minutes, there will be $8{,}000 \underbrace{\:-\: 125 - 125 - 125}_{{-\,125\,\cdot\, \color{blue}{3}}}$ liters in the tank. $\qquad\vdots$

- After $\color{blue}t$ minutes, there will be $8{,}000 \underbrace{\:-\: 125 - \cdots - 125}_{{-\,125\,\cdot\, \color{blue}{t}}}$ liters in the tank.

Therefore,

$$


F(t)=8{,}000 - 125t,


$$

which is a linear function.

Finally, since the slope $(-125)$ is negative, $F$ decreases as $t$ increases. Therefore, $F$ is a decreasing linear function.

### Example: Identifying True Statements About a Linear or Exponential Model

#### Question

The population of a small town is $15 \, 000$ initially, and it increases by $1.5\%$ per year. Which of the following statements are true?

1. The town's population is $15 \, 000\cdot(1.015)^3$ after $3$ years.

2. The relationship between the time and the town's population is linear.

3. The relationship between the time and the town's population is exponential.

#### Explanation

The town's population increases by $1.5\%$ per year; that is, by a factor of $(1+0.015)=1.015$ every year.

Let $t$ denote the number of years and $P(t)$ the population of the town. We can construct a table for the relationship between $t$ and $P(t),$ as follows:

To determine if the relationship is linear or exponential, we need to determine how $P(t)$ changes as $t$ increases at each step:

- For a linear relationship, there should be a common ** between successive values of $P(t).$

- For an exponential relationship, there should be a common ** between successive values of $P(t).$

With that in mind, let's check each statement.

- Statement I is true. From our table, we see that $P(3) = 15\,000\cdot(1.015)^3$.

- Statement II is false. Let's check for a linear pattern by finding the difference between successive values of $P(t){:}$ This list of differences does not show a definite common difference.

- Statement III is true. Let's check for a common ratio by dividing successive values of $P(t){:}$ This list of quotients shows a definite common ratio of $1.015.$

Therefore, the function that best models the relationship is an exponential function with a common ratio of $1.015.$

Therefore, the correct answer is "I and III only."

### Example: Identifying Models That Change Either Linearly or Exponentially

#### Question

Which of the following quantities change linearly and which vary exponentially?

1. The total number of visitors to a web page that attracts $10$ new visitors every day.

2. The number of squirrels living in a natural reserve if the population increases by $2\%$ every year.

3. The amount of pizza dough left in a restaurant kitchen if $2\,\textrm{kg}$ of dough is consumed every hour.

#### Explanation

Let's look at each situation in turn.

- Quantity I changes linearly. Let $V(t)$ be the number of visitors to the web page after $t$ days. Since $V$ increases by a fixed amount of $10$ every day, we have that where $V_0$ is the initial number of visitors. Therefore, $V(t)$ increases linearly with a common difference of $10.$

- Quantity II changes exponentially. Let $S(t)$ be the number of squirrels after $t$ years. Since $S(t)$ increases by $2\%$ every year, we have that where $S_0$ is the initial number of squirrels. Therefore, $S(t)$ grows exponentially with a growth rate of $1.02.$

- Quantity III changes linearly. Let $P(t)$ be the amount of dough left in the kitchen after $t$ hours (in kilograms). Since $P$ decreases by a fixed amount of $2\,\textrm{kg}$ every hour, we have that where $P_0$ is the initial amount of pizza dough. Therefore, $P(t)$ decreases linearly with a common difference of $-2.$

So, I and III change linearly, while II changes exponentially.
