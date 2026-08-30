# Modeling With First-Order ODEs

Source: https://www.mathacademy.com/topics/2023?courseId=106
Topic ID: 2023

## Prerequisites

- [Rates of Change in Applied Contexts](../../../ap-courses/lessons/ap-calculus-ab/620-rates-of-change-in-applied-contexts.md)
- [Modeling with Direct Variation](../../../high-school/traditional/lessons/algebra-i/2274-modeling-with-direct-variation.md)
- [Introduction to Differential Equations](./3215-introduction-to-differential-equations.md)
- [Modeling With Inverse Variation](../../../high-school/traditional/lessons/algebra-i/3664-modeling-with-inverse-variation.md)

## Lesson

### Introduction

Differential equations provide a powerful way of modeling physical situations. Most of the fundamental laws of physics can be expressed as differential equations.

In this lesson, we'll learn how to take a real-world situation and model it using a differential equation.

Suppose that a thick layer of ice covers a lake in Norway. Due to cold winter weather, the thickness of the ice increases by per week. Let's model this situation using a differential equation.

If the thickness of the ice is then the rate of change of the ice thickness is

where is the time in weeks.

Since the thickness of the ice *increases* by every week, the rate of change of the ice thickness is given by

And we're done! We can now solve this equation for the function and use this to predict the ice thickness after weeks.

In this example, the ice thickness *increased* with time, and therefore the rate of change is positive. Next, we'll see an example where the rate of change is negative.

### Example: Translating Problems With Constant Rates of Change Into Differential Equations

#### Question

A helium balloon loses $20$ grams of helium every second. What differential equation describes the rate of change of the mass $M$ of the balloon?

#### Explanation

If the mass of the balloon is $M$ grams, then the rate of change of the mass is $\dfrac{\textrm{d}M}{\textrm{d}t},$ where $t$ is the time in seconds.

Since $20$ grams are lost every second, the rate of change of the balloon's mass is given by the differential equation

$$


\dfrac{\textrm{d}M}{\textrm{d}t}=-20.


$$

Notice that the right-hand side is ** because the balloon is ** mass.

### Modeling Situations With Proportional Rates of Change

So far, we've considered situations where the derivative is constant. Another common situation is when the derivative is proportional to one of the variables.

Consider the following situation:

*The **** $M(t)$ (in milligrams) of a particular drug in a patient's bloodstream **** at a **** that is **** to the **** of the drug in the patient's bloodstream*.

We want to find a differential equation that models the mass of the drug in the patient's bloodstream. We note the following:

- The statement describes the *rate* at which the *mass* varies. Therefore, this is a statement about the quantity

- We're told that $\dfrac{\textrm d M}{\textrm d t}$ is *proportional* to the *mass* of the drug. In other words, Recall that $\propto$ means "is proportional to."

- Finally, we want to replace the proportionality symbol with an equality symbol. Let $k$ be a positive constant. Since the mass of the drug *decreases* with time, our derivative should be *negative*. Therefore, we can rewrite our proportionality statement as

And we're done!

In this example, the dependent variable $M$ is featured on the right-hand side. Next, we'll see an example where the independent variable $t$ features on the right-hand side.

### Example: Translating Problems With Proportional Rates of Change Into Differential Equations

#### Question

The volume of water $V(t)$ in a leaking tank decreases at a rate that is proportional to the time $t$ (in minutes) since the leak started. What differential equation describes the rate of change of the volume of water at time $t?$

#### Explanation

Let's highlight the important words in the given statement:

**

We note the following:

- The question describes the ** at which the ** of water varies. Therefore, this is a statement about the quantity

- We're told that $\dfrac{\textrm d V}{\textrm d t}$ is ** the ** since the water begins to leak. In other words, Recall that $\propto$ means "is proportional to."

- Finally, we want to replace the proportionality symbol with an equality symbol. Let $k$ be a positive constant. Since the volume of water ** with time, our derivative should be **. Therefore, we can rewrite our proportionality statement as

### Example: Further Translating Problems With Proportional Rates of Change Into Differential Equations

#### Question

The area $A$ of a forest decreases with time due to deforestation. The rate of change of the forest area is proportional to the square of the area. What differential equation describes the rate of change of the area at time $t?$

#### Explanation

Let's highlight the important words in the given statement:

**

We note the following:

- The question describes the ** at which the ** varies. Therefore, this is a statement about the quantity

- We're told that $\dfrac{\textrm d A}{\textrm d t}$ is ** the ** In other words, Recall that $\propto$ means "is proportional to."

- Finally, we want to replace the proportionality symbol with an equality symbol. Let $k$ be a positive constant. Since the area ** with time, our derivative should be **. Therefore, we can rewrite our proportionality statement as

### Modeling Situations With Inversely Proportional Rates of Change

The last situation we will consider is when the derivative is inversely proportional to one of the variables.

Consider the following situation:

*The **** $P(t)$ (in dollars) for selling a particular product **** at a **** that is **** to the **** sold*.

We want to find a differential equation that models the profit. We note the following:

- The question describes the *rate* at which the *profit* varies. Therefore, this is a statement about the quantity

- We're told that $\dfrac{\textrm d P}{\textrm d t}$ is *inversely proportional* to the *number of units* sold. In other words, Recall that $\propto$ means "is proportional to."

- Finally, we want to replace the proportionality symbol with an equality symbol. Let $k$ be a positive constant. Since the profit *increases* with time, our derivative should be *positive*. Therefore, we can rewrite our proportionality statement as

### Example: Translating Problems With Inversely Proportional Rates of Change Into Differential Equations

#### Question

The volume of water $V$ in a bucket decreases at a rate that's inversely proportional to the square of the volume of water. What differential equation describes the rate of change of the volume of water $V?$

#### Explanation

Let's highlight the important words in the given statement:

**

We note the following:

- The question describes the ** at which the ** varies. Therefore, this is a statement about the quantity

- We're told that $\dfrac{\textrm d V}{\textrm d t}$ is ** the ** In other words, Recall that $\propto$ means "is proportional to."

- Finally, we want to replace the proportionality symbol with an equality symbol. Let $k$ be a positive constant. Since the volume of water ** with time, our derivative should be **. Therefore, we can rewrite our proportionality statement as
