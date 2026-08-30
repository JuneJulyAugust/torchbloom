# Interpreting Exponential Decay

Source: https://www.mathacademy.com/topics/1629?courseId=44
Topic ID: 1629

## Prerequisites

- [Modeling Exponential Decay With Functions](./2472-modeling-exponential-decay-with-functions.md)

## Lesson

### Introduction

In this lesson, we will learn how to interpret various aspects of an exponential decay expression or function.

For example, suppose that, due to overfishing, a fish population decays exponentially. The population $y(t)$ is given by

$$


y(t) = 5\,000 \left(\dfrac 1 2\right)^t,


$$

where $t$ is the time, in months, since the overfishing began. What can we deduce about the population of fish from this model?

The first thing to notice is that the function above is an exponential decay function of the form

$$


y(t) = a \cdot b^t.


$$

So, we can deduce the following:

- $a=5\,000$ represents the initial value. So this tells us that there were $5\,000$ fish when the overfishing began.

- $b = \dfrac 1 2$ is the decay factor. Since $0 < b < 1,$ this tells us that we're dealing with exponential decay, *not* exponential growth (for exponential growth we need $b > 1$).

- $t$ is the time, in months, since the overfishing began.

### Example: Interpreting Exponential Expressions

#### Question

A house was purchased for $90\,000.$ Shortly after purchasing the property, the owners discovered widening cracks in the foundation. As a result, the value of the property is reduced by one-half every year. What does the expression $\,90\,000\left(\dfrac{1}{2}\right)^6$ mean in this context?

#### Explanation

The given expression is an exponential decay expression of the form $y(t) = a \cdot b^t,$ where we have the following:

- $a=90\,000$ represents the purchase price of the property.

- $b = \dfrac 1 2$ is the decay factor.

- $t = 6$ the time, in years, since the property was bought.

Since $t=6,$ the expression $\,90\,000\left(\dfrac{1}{2}\right)^6$ gives the value of the property after $6$ years.

### Example: Interpreting the Output of an Exponential Decay Function

#### Question

The value of a certain stock, in dollars, decays according to the formula

$$


V(t)= 4\, 500\cdot (0.85)^t,


$$

where $t$ is the time, in years, since the stock was bought.

1. What does $V(3)$ mean in this context?

2. Calculate $V(2) - V(3),$ and determine its meaning in this context.

#### Explanation

- The value $V(3)$ represents the value of the function $V(t)$ at $t=3.$ In this context, it represents the value of the stock $3$ years after the initial investment.

- By similar reasoning to the above, $V(2)$ represents the stock's value $2$ years after the initial investment. Therefore, the expression represents the total reduction in the value of the stock between $t=2$ and $t=3$ years since the initial investment. Now, let's compute its value. We get rounded to the nearest integer. Therefore, the value of the stock dropped by $488$ between years $2$ and $3.$

### Example: Interpreting a Decay Rate

#### Question

The market value $V(t)$ of a car, in dollars, $t$ years since it was first purchased depreciates according to the following rule:

$$


V(t) = 25\, 000\cdot (0.95)^t


$$

What does the base of the exponential expression $(0.95)$ mean in this context?

#### Explanation

We're asked for the decay rate, so we use the decay rate formula.

The given expression is an exponential decay expression of the form $y(t) = a \cdot (1-r)^t,$ where

- $a=25\,000$ represents the initial value of the car (in dollars).

- $1-r = 0.95,$ where $r$ is the decay rate.

- $t$ is the time since the car was first purchased, in years.

Solving for the decay rate $r,$ we get

$$


1-r = 0.95\quad\Longrightarrow\quad r = 0.05.


$$

Now, $0.05$ (expressed as a percent) is equal to $5\%.$ Therefore, the value of the car depreciates by $5\%$ each year.
