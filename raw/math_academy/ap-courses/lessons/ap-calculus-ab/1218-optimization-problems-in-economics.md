# Optimization Problems in Economics

Source: https://www.mathacademy.com/topics/1218?courseId=24
Topic ID: 1218

## Prerequisites

- [The Second Derivative Test](./339-the-second-derivative-test.md)
- [The Candidates Test](./364-the-candidates-test.md)
- [Constructing Revenue, Cost, and Profit Functions](../../../high-school/traditional/lessons/algebra-i/3667-constructing-revenue-cost-and-profit-functions.md)

## Lesson

### Introduction

There are several quantities that businesses need to keep track of to ensure that the business remains healthy:

- Revenue: This is the total amount of money (in dollars) that a company gains after selling $x$ units of product.

- Cost: This is the total amount of money (in dollars) that a company spends to create $x$ units of product.

- Profit. The difference between revenue and cost. It represents the amount of *additional* money that the business has earned after paying its costs.

Businesses often strive to maximize revenue and profit. They also often seek to minimize cost. We can solve these problems using the second derivative or the candidates test. Let's find out how.

### Example: Optimizing a Profit, Revenue, or Cost Function

#### Question

The director of a newspaper estimates that the company's profit, in hundreds of dollars, is given by

$$


P(x) = -x^2 + 44x + 5,


$$

where $x$ is the number of newspapers, in thousands, produced daily. Given that the company has the capacity to produce $30\,000$ newspapers every day, how many newspapers per day should the company produce to maximize profit?

#### Explanation

First, we note that the permitted domain is

$$


0 \leq x \leq 30,


$$

since $x = 30$ corresponds to $30 \cdot 1\,000 = 30\,000$ copies of the newspaper.

We need to find the critical points of $P(x)$ for $0 < x < 30.$ Taking the derivative, we get

$$


P'(x) = -2x + 44,


$$

and solving $P'(x)=0$ gives the following critical point:

$$


\begin{aligned}𝑃^{′}(𝑥) & =0 \\ −2𝑥+44 & =0 \\ 2𝑥 & =44 \\ 𝑥 & =22\end{aligned}


$$

Notice that $x=22$ lies in the interval $0 \leq x \leq 30.$ All that's left now is to confirm that $x=22$ does indeed give a maximum value of $P(x).$ To do this, we compute the second derivative:

$$


P''(x) = -2 < 0.


$$

Since the second derivative is negative, the point $x=22$ is indeed a local maximum of $P(x).$ And since $P(x)$ is quadratic, we conclude that $x=22$ is a global maximum of $P(x).$

Therefore, the company should produce $22 \cdot 1\,000 = 22\,000$ copies of the newspaper per day to maximize its profit.

### A Review of Price and Cost Functions

Recall that the price function $p(x)$ gives the *price per unit* at which a company sells $x$ units of a good.

The revenue function $R(x)$ associated with a price function $p(x)$ is given by

$$


\begin{aligned}𝑅(𝑥) & =(number of units)⋅(price per unit) \\ & =𝑥⋅𝑝(𝑥).\end{aligned}


$$

Also, recall that the cost function $C(x)$ associated with producing $x$ units of a good can be calculated as follows:

$$


\begin{aligned}𝐶(𝑥) & =(fixed cost)+(number of units)⋅(cost per unit) \\ & =(fixed cost)+𝑥⋅(cost per unit)\end{aligned}


$$

The quantity $x\cdot (\textrm{cost per unit})$ is sometimes called the **variable cost** since it is the part of the cost function $C(x)$ that is dependent on the number of units $x$ produced by the company.

Finally, if we know the revenue function $R(x)$ and the cost function $C(x),$ then the profit function $P(x)$ is given by

$$


P(x) = R(x) - C(x).


$$

### Example: Maximizing a Revenue Function Given a Price Function

#### Question

A textile center sells $x$ hundreds of meters of fabric at a price $p(x),$ in dollars, given by

$$


p(x) = x^2 - 15x + 48 + \dfrac{78}{x}.


$$

If the textile center sells between $100$ and $900$ meters of fabric daily, how many meters of fabric must the textile center sell to maximize its revenue?

#### Explanation

To solve this problem, we apply the candidates test.

First, note that for selling $x$ hundreds of meters in total, the total revenue $R(x)$ is given by

$$


\begin{aligned}𝑅(𝑥) & =𝑥⋅𝑝(𝑥) \\ & =𝑥(𝑥^{2}−15𝑥+48+\frac{78}{𝑥}) \\ & =𝑥^{3}−15𝑥^{2}+48𝑥+78.\end{aligned}


$$

Now, we note that the permitted domain is $1 \leq x \leq 9,$ since $x = 1$ corresponds to $1 \cdot 100 = 100$ and $x = 9$ corresponds to $9 \cdot 100 = 900.$ Therefore, $x=1$ and $x=9$ are both candidates for the global maxima of $R(x).$

We need to find the critical points of $R(x)$ for $1 < x < 9.$ Taking the derivative, we get

$$


R'(x) = 3x^2 - 30x + 48,


$$

and solving $R'(x)=0$ gives the following critical points:

$$


\begin{aligned}𝑅^{′}(𝑥) & =0 \\ 3𝑥^{2}−30𝑥+48 & =0 \\ 𝑥^{2}−10𝑥+16 & =0 \\ (𝑥−2)(𝑥−8) & =0\end{aligned}


$$

So, the critical points are $x=2$ and $x=8.$

Our candidates are $x=1,2, 8$ and $9.$ Computing $R(x)$ at each of these values, we get the following:

$$


\begin{aligned}𝑅(1) & =(1)^{3}−15(1)^{2}+48(1)+78=112 \\ 𝑅(2) & =(2)^{3}−15(2)^{2}+48(2)+78=122\,✓ \\ 𝑅(8) & =(8)^{3}−15(8)^{2}+48(8)+78=14 \\ 𝑅(9) & =(9)^{3}−15(9)^{2}+48(9)+78=24\end{aligned}


$$

Therefore, to maximize its revenue, the textile center should sell $2 \cdot 100 = 200$ meters of fabric.

### Example: Maximizing a Profit Function Given a Revenue and Cost Function

#### Question

A company spends $C(x) = x^2 + 80x$ dollars to produce $x$ units of a certain product. The company sells the product for $ 180$ per unit. What is the maximum monthly profit that the factory can make given that it can produce at most $60$ units of product per month?

#### Explanation

First, note that for selling $x$ units of the product per month, the company has a monthly revenue (income) of $R(x)=180\cdot x=180 x$ dollars. Therefore, the profit function is given by

$$


\begin{aligned}𝑃(𝑥) & =𝑅(𝑥)−𝐶(𝑥) \\ & =180𝑥−(𝑥^{2}+80𝑥) \\ & =100𝑥−𝑥^{2}.\end{aligned}


$$

From the question statement, we know that the permitted domain is $0\leq x \leq 60.$

We need to find the critical points of $P(x)$ for $0 < x < 60.$ Taking the derivative, we get

$$


P'(x)=100-2x,


$$

and solving $P'(x)=0$ gives the following critical point:

$$


\begin{aligned}𝑃^{′}(𝑥) & =0 \\ 100−2𝑥 & =0 \\ 𝑥 & =50\end{aligned}


$$

Notice that $x=50$ lies in the interval $0 < x < 60.$ All that's left now is to confirm that $x=50$ does indeed give a maximum value of $P(x).$ To do this, we compute the second derivative:

$$


P''(x) = -2 < 0


$$

Since the second derivative is negative, the point $x=50$ is indeed a local maximum of $P(x).$ And since $P(x)$ is quadratic, we conclude that $x=50$ is a global maximum of $P(x).$

Therefore, the maximum monthly profit is

$$


\begin{aligned}𝑃(50) & =100(50)−(50)^{2}=2\,500.\end{aligned}


$$

### Example: Maximizing a Profit Function by Constructing a Revenue and Cost Function

#### Question

A hotel has $21$ rooms. The manager has observed that when the room rate is $12$ per night, all rooms are occupied and, for every $1$ increase in the rate, a single room is vacated. If the maintenance of each rented room is $3$ per night, what rate per room should the manager set to obtain the maximum profit, and what is the maximum profit?

#### Explanation

First, note that if there are $x$ ** rooms, the hotel has $(21-x)$ occupied rooms, and the rate per room is $(12+x)$ dollars. So, the total revenue (in dollars) is given by

$$


\begin{aligned}𝑅(𝑥) & =\underset{occupied rooms}{\underset{}{(21−𝑥)}}×\,\,\,\underset{rate per room}{\underset{}{(12+𝑥)}} \\ & =252+21𝑥−12𝑥−𝑥^{2} \\ & =252+9𝑥−𝑥^{2}.\end{aligned}


$$

On the other hand, for having $(21-x)$ rooms rented out, the hotel has a cost (in dollars) of

$$


\begin{aligned}𝐶(𝑥) & =3(21−𝑥) \\ & =63−3𝑥.\end{aligned}


$$

Therefore, the profit function is given by

$$


\begin{aligned}𝑃(𝑥) & =𝑅(𝑥)−𝐶(𝑥) \\ 𝑃(𝑥) & =(252+9𝑥−𝑥^{2})−(63−3𝑥) \\ & =189+12𝑥−𝑥^{2}.\end{aligned}


$$

Since there are $21$ rooms, the permitted domain is $0 \leq x\leq 21.$

We need to find the critical points of $P(x)$ for $0 \lt x\lt 21.$ Taking the derivative, we get

$$


P'(x) = 12 - 2x \,.


$$

and solving $P'(x)=0$ gives the following critical point:

$$


\begin{aligned}𝑃^{′}(𝑥) & =0 \\ 12−2𝑥 & =0 \\ 2𝑥 & =12 \\ 𝑥 & =6\,.\end{aligned}


$$

Notice that $x=6$ lies in the interval $0 < x < 21.$ All that's left now is to confirm that $x=6$ does indeed give a maximum value of $P(x).$ To do this, we compute the second derivative:

$$


P''(x) = -2 < 0


$$

Since the second derivative is negative, the point $x=6$ is indeed a local maximum of $P(x).$ And since $P(x)$ is quadratic, we conclude that $x=6$ is a global maximum of $P(x).$

Therefore, we conclude that the hotel will have a maximum profit when there are $x=6$ vacant rooms.

We know that the rate per room is $(12+x)$ dollars. If there are $6$ vacant rooms, then the rate per room is

$$


\begin{aligned}12+6 & =18.\end{aligned}


$$

Therefore, the manager should charge a room rate of $18$ per night.
