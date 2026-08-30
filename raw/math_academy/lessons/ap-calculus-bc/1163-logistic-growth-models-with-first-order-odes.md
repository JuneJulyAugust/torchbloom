# Logistic Growth Models With First-Order ODEs

Source: https://www.mathacademy.com/topics/1163?courseId=21
Topic ID: 1163

## Prerequisites

- [Exponential Growth and Decay Models With First-Order ODEs](../ap-calculus-ab/876-exponential-growth-and-decay-models-with-first-order-odes.md)

## Lesson

### Introduction

A differential equation of the form

$$


\dfrac{\mathrm dy}{\mathrm dt} = ky(a-y),


$$

where $y=y(t)$ is called a **logistic growth equation.**

Note the following:

- $a$ is a positive constant called the **carrying capacity**.

- $k$ is a positive constant of proportionality.

A typical solution curve $y = y(t)$ to this equation is shown below:

![Instructional graphic](../../lesson-assets/ap-calculus-bc/topic-1163/84ae5fbbb7fef532.png)

We will learn more about the structure of the solution curves in future lessons. But for now, it's helpful to realize that for all $t,$ we have

$$


0 < y(t) < a.


$$

An example of a logistic growth equation is

$$


\dfrac{\mathrm dy}{\mathrm dt} = 10y(50-y).


$$

Here, $k = 10$ and the carrying capacity is $a=50.$

### Example: Identifying a Logistic Growth Differential Equation

#### Question

Which of the following differential equations is a logistic growth equation?

1. $\dfrac{\mathrm{d} y}{\mathrm{d} t} = 56y-7y^2$

2. $\dfrac{\mathrm{d} y}{\mathrm{d} t} = 56-7y^2$

3. $\dfrac{\mathrm{d} y}{\mathrm{d} t} = 56y^2-7$

#### Explanation

A logistic growth equation has the form

$$


\dfrac{\mathrm{d} y}{\mathrm{d} t} = ky(a-y),


$$

where $k > 0$ is a constant of proportionality, and $a > y$ is the carrying capacity.

From the given options, the only logistic growth equation is

$$


\dfrac{\mathrm{d} y}{\mathrm{d} t} = 56y-7y^2.


$$

To see this, let's factor the right-hand side of the equation. This gives

$$


\dfrac{\mathrm{d} y}{\mathrm{d} t} = 7y(8-y).


$$

From here, we see that the constant of proportionality $k=7,$ and the carrying capacity is $a=8.$

### Modeling Situations Using a Logistic Growth Equation

Suppose we want to create a model of the deer population in a forest. Let's denote the number of deer in the forest at time $t$ as $P(t).$

Imagine that we have two factors that influence the size of the deer population:

- Unconstrained, the rate at which the deer population increases is proportional to the size of the deer population (i.e., exponential growth).

- However, as the deer population increases, food resources become more scarce. The forest cannot sustain an arbitrarily large number of deer. Therefore, we must specify the maximum number of deer that the forest can sustain. This maximum number is the forest's carrying capacity, denoted $a,$ as before.

Therefore, we say that the rate of change of the deer population $P(t)$ is **jointly proportional** to *both* the deer population $P$ itself *and* the remaining room for growth, which is $a-P.$ This gives us the logistic growth equation

$$


\dfrac{\textrm d P}{\textrm d t} = kP(a-P).


$$

### Example: Constructing a Logistic Growth Equation

#### Question

The growth rate of the hamster population $P(t)$ in a park is jointly proportional to the hamster population at time $t,$ measured in years, and the difference between the park's carrying capacity and the hamster population. If the constant of proportionality is $0.005$ and the maximum possible hamster population is $120,$ which differential equation could be used to model $P(t)?$

#### Explanation

Since the hamster population's growth rate is ** proportional to the hamster population at time $t$ and the difference between the carrying capacity and the hamster population, the hamster population follows a logistic growth model.

A logistic growth equation has the form

$$


\dfrac{\mathrm{d} P}{\mathrm{d} t} = kP(a-P),


$$

where $k > 0$ is a constant of proportionality, and $a > P$ is the carrying capacity.

In this case, the constant of proportionality is $k=0.005,$ and the carrying capacity is $a=120.$ Therefore, the hamster population is given by the equation

$$


\dfrac{\mathrm{d} P}{\mathrm{d} t} = 0.005P(120-P).


$$
