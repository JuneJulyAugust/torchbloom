# Constructing Revenue, Cost, and Profit Functions

Source: https://www.mathacademy.com/topics/3667?courseId=133
Topic ID: 3667

## Prerequisites

- [Modeling With Linear Equations](../../../traditional/lessons/algebra-i/426-modeling-with-linear-equations.md)
- [Revenue, Cost, and Profit Functions](../../../traditional/lessons/algebra-i/701-revenue-cost-and-profit-functions.md)

## Lesson

### Introduction

An important function that company managers and economists often track is the **price function** of a good, usually denoted $p(x).$ The price function gives the **price per unit** of selling $x$ units of a product.

When purchasing items in large quantities, there is often a discount which causes the price per unit to decrease as the number of units increases. This is one motivation behind introducing a price function.

For example, suppose that a textile factory manufactures pants. If the price per unit (in dollars) is given by

$$


p(x) = 500-x^2,


$$

then the price for $10$ units is

$$


p(10) = 500-(10)^2 = 400.


$$

It's important to remember that this is the price *per unit*. The total amount that the company would charge for selling $10$ units is

$$


10\cdot p(10) = 10\cdot 400 = 4\,000.


$$

This example shows that the price function is closely connected to the revenue function $R(x).$ Typically, if a company sells $x$ units at a price $p(x),$ then the total revenue is given by

$$


\begin{aligned}𝑅(𝑥) & =(number of units)⋅(price per unit) \\ & =𝑥⋅𝑝(𝑥).\end{aligned}


$$

So, in the case of the above example, the revenue function $R(x)$ is given by

$$


\begin{aligned}𝑅(𝑥) & =𝑥⋅𝑝(𝑥) \\ & =𝑥⋅(500−𝑥^{2}) \\ & =500𝑥−𝑥^{3}.\end{aligned}


$$

While the price of a good sometimes varies with $x,$ other times it may be constant. In cases when the unit price is constant, you'll see the price per unit quoted as a single figure (usually in dollars).

### Example: Constructing Revenue Functions

#### Question

A company produces jeans. The revenue function, in dollars, of this company is given by $R(x) =5x(10-0.02x),$ where $x$ represents the number of units produced and sold per month. Calculate the price function $p(x).$

#### Explanation

Given a price function $p(x),$ the revenue function is given by

$$


\begin{aligned}𝑅(𝑥) & =(number of units)⋅(price per unit) \\ & =𝑥⋅𝑝(𝑥).\end{aligned}


$$

Therefore, the price function is

$$


p(x) = \dfrac{R(x)}{x}.


$$

In our case, we have

$$


\begin{aligned}𝑝(𝑥) & =\frac{5𝑥(10−0.02𝑥)}{𝑥} \\ & =\frac{5𝑥(10−0.02𝑥)}{𝑥} \\ & =5(10−0.02𝑥) \\ & =50−0.1𝑥\end{aligned}


$$

### Cost Functions

We can construct a cost function $C(x)$ for a business using the following equation:

$$


C(x) = (\text{fixed cost}) + (\textrm{number of units})\cdot (\textrm{cost per unit})


$$

Let's break this equation down a bit:

- The **fixed cost** is the part of the cost function that does not change. Irrespective of how many units are produced, fixed costs are always the same. Fixed costs typically incorporate rent, utilities, communications, employee wages, taxes, etc.

- The term $(\textrm{number of units})\cdot (\textrm{cost per unit})$ represents the **variable cost.** This part of the cost function changes depending on how many units are produced.

For example, suppose that a company produces $x$ units of sweaters per month. Each unit costs $49$ to make, and the company's fixed costs are $4\,500$ per month.

We can calculate the cost function $C(x)$ for this company as follows:

$$


\begin{aligned}𝐶(𝑥) & =(fixed cost)+(number of units)⋅(cost per unit) \\ & =4\,500+𝑥⋅49 \\ & =4\,500+49𝑥.\end{aligned}


$$

To calculate the cost of producing $50$ units, we substitute $x=50$ into $C(x).$ This gives

$$


\begin{aligned}𝐶(50) & =4\,500+49(50) \\ & =4\,500+2\,450 \\ & =6\,950.\end{aligned}


$$

Therefore, it costs the company $6\,950$ to produce $50$ units.

### Example: Constructing Cost Functions

#### Question

A company produces $x$ units of baseball caps per month. Each unit costs $1.50$ to make, and the company’s fixed costs are $3\,700$ per month. Calculate the total cost of producing $400$ units of the product.

#### Explanation

The cost function $C(x)$ can be calculated as follows:

$$


C(x) = (\text{fixed cost}) + (\textrm{number of units})\cdot (\textrm{cost per unit})


$$

In this case, we're told that the fixed costs are $3\,700$ per month, and each unit costs $1.50$ to make. Therefore, the cost function is

$$


\begin{aligned}𝐶(𝑥) & =3\,700+𝑥⋅1.5 \\ & =3\,700+1.5𝑥.\end{aligned}


$$

To calculate the cost of producing $400$ units, we substitute $x=400$ into $C(x).$ This gives

$$


\begin{aligned}𝐶(400) & =3\,700+1.5(400) \\ & =3\,700+600 \\ & =4\,300.\end{aligned}


$$

Therefore, it costs the company $4\,300$ to produce $400$ units.

### Profit Functions

A company manufactures canned mixed nuts. The price function for this company is given by

$$


p(x) = 60-0.01x,


$$

where $x$ represents the number of units produced and sold per month. Additionally, each unit costs $25$ to make, and the company's fixed costs are $8\,800$ per month.

Let's calculate the profit function $P(x)$ for this company.

Recall that profit function $P(x)$ is equal to the revenue function $R(x)$ minus the cost function $C(x)\mathbin{:}$

$$


P(x)=R(x)-C(x)


$$

So, to calculate the profit function, we first need to construct $R(x)$ and $C(x).$

- We're given the price function $p(x),$ so the revenue function is

- We're also given that the fixed costs are $8\,800$ per month and that each unit costs $25$ to make. Therefore, the cost function is

Finally, we can now calculate the profit function:

$$


\begin{aligned}𝑃(𝑥) & =𝑅(𝑥)−𝐶(𝑥) \\ & =(60𝑥−0.01𝑥^{2})−(8\,800+25𝑥) \\ & =60𝑥−0.01𝑥^{2}−8\,800−25𝑥 \\ & =−0.01𝑥^{2}+35𝑥−8\,800\end{aligned}


$$

### Example: Constructing Profit Functions

#### Question

To produce a certain brand of t-shirts, a manufacturing company bases the price of each unit on the price function $p(x) = 50-0.1x$, where $x$ represents the number of units produced and sold per month. Each unit costs $20$ to make, and the company’s fixed costs are $2\,000$ per month. Calculate the profit function $P(x).$

#### Explanation

We know that the profit function is given by

$$


P(x)=R(x)-C(x)


$$

where $x$ is the number of units, $C(x)$ is the cost function and $R(x)$ is the revenue function.

We're given the price function $p(x),$ so the revenue function is

$$


\begin{aligned}𝑅(𝑥) & =(number of units)⋅(price per unit) \\ & =𝑥⋅𝑝(𝑥) \\ & =𝑥(50−0.1𝑥) \\ & =50𝑥−0.1𝑥^{2}.\end{aligned}


$$

We're also told that the fixed costs are $2\,000$ per month, and each unit costs $20$ to make. Therefore, the cost function is

$$


\begin{aligned}𝐶(𝑥) & =(fixed cost)+(number of units)⋅(cost per unit) \\ & =2\,000+𝑥⋅20 \\ & =2\,000+20𝑥.\end{aligned}


$$

Finally, we can now calculate the profit function:

$$


\begin{aligned}𝑃(𝑥) & =𝑅(𝑥)−𝐶(𝑥) \\ & =(50𝑥−0.1𝑥^{2})−(2\,000+20𝑥) \\ & =50𝑥−0.1𝑥^{2}−2\,000−20𝑥 \\ & =−0.1𝑥^{2}+30𝑥−2\,000\end{aligned}


$$
