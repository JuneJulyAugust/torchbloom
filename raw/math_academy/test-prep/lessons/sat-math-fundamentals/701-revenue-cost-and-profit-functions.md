# Revenue, Cost, and Profit Functions

Source: https://www.mathacademy.com/topics/701?courseId=120
Topic ID: 701

## Prerequisites

- [Simplifying Rational Expressions](../../../high-school/traditional/lessons/algebra-i/68-simplifying-rational-expressions.md)
- [The Arithmetic of Functions](../../../high-school/traditional/lessons/algebra-i/140-the-arithmetic-of-functions.md)
- [The Quadratic Formula](../../../high-school/traditional/lessons/algebra-i/422-the-quadratic-formula.md)

## Lesson

### Introduction

Business managers need to model and track different financial metrics to ensure that their businesses remain healthy and sustainable.

Let's assume that a particular company produces a single product, and it creates and sells $x$ **units** of the product over a fixed interval of time (usually monthly or annually).

- The **revenue** of the business is the amount of money the company generates after selling $x$ units of its product. We model the revenue using a **revenue function** $R(x).$

- The **cost** is the amount of money the company spends to produce $x$ units of its product. We model the cost using a **cost function** $C(x).$

- The **profit** is the difference between revenue and cost. It represents the amount of money the business earns for producing and selling $x$ units of its product. The profit is modeled using the **profit function** $P(x),$ given by

For example, suppose a company manufactures bottled water and that the revenue and cost functions, in dollars, of this company are given by

$$


R(x)= 130x-x^2, \qquad C(x) = 750 + 5x.


$$

We calculate the profit function as follows:

$$


\begin{aligned}𝑃(𝑥) & =𝑅(𝑥)−𝐶(𝑥) \\ & =(130𝑥−𝑥^{2})−(750+5𝑥) \\ & =−𝑥^{2}+125𝑥−750\end{aligned}


$$

If we want to find the total profit earned for producing and selling $100$ units, we substitute $x=100$ into $P(x),$ as follows:

$$


\begin{aligned}𝑃(100) & =−(100)^{2}+125(100)−750 \\ & =−10\,000+12\,500−750 \\ & =1\,750\end{aligned}


$$

Therefore, the company makes a profit of $1\,750$ for selling $100$ units.

Companies produce products in large quantities. Therefore, it's usually convenient to let $x$ be the number of *units* produced. A unit refers to an industrial product unit, not necessarily an individual product. So in the example above, $x$ might represent the number of boxes or containers of water bottles. It does not necessarily represent the number of individual bottles.

### Example: Calculating Revenue, Cost, and Profit Functions

#### Question

A company produces TV commercials. The revenue and profit functions, in thousands of dollars, of this company are given by

$$


R(x)=65x-x^2, \qquad P(x)=-x^2+45x-50,


$$

where $x$ represents the number of commercials produced by the company per year. Find the cost function $C(x).$

#### Explanation

The profit is equal to the revenue minus the cost:

$$


P(x)=R(x)-C(x)


$$

Hence, the cost function is given by

$$


C(x) = R(x) - P(x).


$$

Therefore,

$$


\begin{aligned}𝐶(𝑥) & =𝑅(𝑥)−𝑃(𝑥) \\ & =(65𝑥−𝑥^{2})−(−𝑥^{2}+45𝑥−50) \\ & =65𝑥−𝑥^{2}+𝑥^{2}−45𝑥+50 \\ & =50+20𝑥.\end{aligned}


$$

### Example: Calculating the Number of Units Required to Generate a Given Profit

#### Question

A company manufactures teddy bears. The revenue and cost functions, in thousands of dollars, of this company are given by

$$


C(x) = 6\,700 + 26x, \qquad R(x) = 130x - 0.4x^2,


$$

where $x$ represents the number of units produced per month. Find the number of units the company should produce per month to make a profit of $20\,000.$

#### Explanation

The profit is equal to the revenue minus the cost:

$$


\begin{aligned}𝑃(𝑥) & =𝑅(𝑥)−𝐶(𝑥) \\ & =(130𝑥−0.4𝑥^{2})−(6\,700+26𝑥) \\ & =−0.4𝑥^{2}+104𝑥−6\,700\end{aligned}


$$

Now, since we want a profit of $20\,000,$ and $P(x)$ is measured in thousands of dollars, we set $P(x)$ equal to $20\,000\div 1\,000 = 20\mathbin{:}$

$$


\begin{aligned}𝑃(𝑥) & =20 \\ −0.4𝑥^{2}+104𝑥−6\,700 & =20\end{aligned}


$$

We can tidy up the equation so that it becomes a quadratic equation in standard form with a leading coefficient of $1\mathbin{:}$

$$


\begin{aligned}−0.4𝑥^{2}+104𝑥−6\,700 & =20 \\ 0.4𝑥^{2}−104𝑥+6\,720 & =0 \\ \frac{0.4𝑥^{2}−104𝑥+6\,720}{0.4} & =\frac{0}{0.4} \\ 𝑥^{2}−260𝑥+16\,800 & =0\end{aligned}


$$

Now, to solve for $x,$ we apply the quadratic formula:

$$


\begin{aligned}𝑥 & =\frac{−(−260)±\sqrt{√(−260)^{2}−4(1)(16\,800)}}{2} \\ & \\ & =\frac{260±\sqrt{√400}}{2} \\ & \\ & =\frac{260±20}{2} \\ & \end{aligned}


$$

The solutions are $x=120$ and $x=140.$ Therefore, the company will make a profit of $20\,000$ if it produces $120$ or $140$ units.
