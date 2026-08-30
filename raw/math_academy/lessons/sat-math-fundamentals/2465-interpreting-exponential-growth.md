# Interpreting Exponential Growth

Source: https://www.mathacademy.com/topics/2465?courseId=120
Topic ID: 2465

## Prerequisites

- [Modeling Exponential Growth With Functions](../algebra-i/2471-modeling-exponential-growth-with-functions.md)

## Lesson

### Introduction

A scientist models the number of bacteria in a Petri dish using the function

$$


y(t) = 1\,500 \cdot 3^t.


$$

Here, $y(t)$ gives the number of bacteria in the dish, and $t$ gives the number of days since the start of an experiment.

Without being given any more information, what can we deduce about the number of bacteria?

The first thing to notice is that the function above is an exponential growth function:

$$


y(t) = a \cdot b^t


$$

Comparing the function that the scientist is using with the general expression above, we can deduce the following:

- $a=1\,500$ represents the initial value. This tells us the number of bacteria at the start of the experiment.

- $b = 3$ is the growth factor. This tells us that the number of bacteria increases by a factor of $3$ every day.

- $t =$ is the time since the start of the observations, in days.

In this lesson, we'll get practice at interpreting the various parts of an exponential growth expression or function. The trick is to compare a given expression with $y(t) = a\cdot b^t.$

### Example: Interpreting an Exponential Growth Expression

#### Question

At the beginning of the year $2000,$ only $300$ people in a particular town had a cell phone. Since then, the number of cellphone subscribers doubled every year. What does the expression $300\cdot 2^5$ mean in this context?

#### Explanation

The given expression is an exponential growth expression of the form $y(t) = a \cdot b^t,$ where we have the following:

- $a=300$ represents the initial number of cellphone subscribers.

- $b = 2$ is the growth factor. This tells us that the number of subscribers doubles every year.

- $t = 5$ is the time, in years.

Since $t=5,$ the expression $300\cdot 2^5$ gives the total number of cell phone subscribers after $5$ years.

### Example: Interpreting the Exponential Part of an Expression

#### Question

A chemical reaction starts with $250$ molecules in a reaction chamber, and this number increases exponentially. If after $5$ hours there are $250\cdot 2^5$ molecules in the chamber, what does the factor $2^5$ mean in this context?

#### Explanation

The given expression $250\cdot 2^5$ is an exponential growth expression of the form $y(t) = ab^t,$ where:

- $a=250$ represents the initial number of molecules,

- $b = 2$ is the growth factor, and

- $t = 5$ is the time since the start of the observations, in hours.

For the factor $2^5,$ the growth rate $(2)$ means that the number of molecules doubles every hour, and the exponent $(5)$ indicates the number of hours.

Therefore, $2^5 = 32$ means that the number of molecules has increased by a factor of $32$ in five hours.

### Example: Interpreting the Output of an Exponential Function

#### Question

The altitude, in meters, of a hot-air balloon is modeled by the function $A(t)=12\cdot 2^t,$ where $t$ represents the number of minutes since the balloon took off from a platform.

1. What does $A(3)$ mean in this context?

2. How high does the balloon climb between the third minute and the sixth minute of its flight?

#### Explanation

To answer question I, the value $A(3)$ represents the value of the function $A(t)$ at $t=3.$ In this context, it represents the altitude of the balloon $3$ minutes after taking off from the platform.

Question II asks for the total height that the balloon climbed between $t=3$ and $t=6$ minutes. To calculate this, we find the balloon's altitude after $6$ minutes, and we subtract its altitude after $3$ minutes. So we need to work out

$$


A(6) - A(3).


$$

First, let's work out $A(6){:}$

$$


A(6) = 12\cdot 2^6 = 768


$$

Next, we work out $A(3){:}$

$$


A(3) = 12\cdot 2^3 = 96


$$

Therefore, the balloon's altitude increased by $768 - 96 = 672$ meters between the third and the sixth minute.

### Example: Interpreting the Growth Rate In an Exponential Expression

#### Question

The value of a piece of jewelry, in dollars, is given by the expression $600 \cdot (1.2)^{t},$ where $t$ is the number of years since the piece was purchased. What is the growth rate of the piece?

#### Explanation

We're asked for the growth rate, and so we use the growth rate formula.

The given expression is an exponential growth expression of the form $y(t) = a \cdot (1+r)^t,$ where:

- $a=600$ represents the initial value of the jewelry, in dollars

- $1+r = 1.2,$ where $r$ is the growth rate

- $t =$ the time since the piece was purchased, in years

Solving for $r,$ we get

$$


1+r = 1.2\quad\Longrightarrow\quad r = 0.2.


$$

Now, $0.2$ (expressed as a percent) is equal to $20\%.$ Therefore, the value of the jewelry grows by $20\%$ per year.
