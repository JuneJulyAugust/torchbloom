# Solving Exponential Growth Problems

Source: https://www.mathacademy.com/topics/2464?courseId=120
Topic ID: 2464

## Prerequisites

- [Interpreting Exponential Growth](../../../high-school/traditional/lessons/algebra-i/2465-interpreting-exponential-growth.md)

## Lesson

### Introduction

We can use our knowledge of solving exponential equations to obtain information about a system that follows an exponential growth model.

For example, suppose that the revenue $R(t),$ in millions of dollars, of a rapidly growing startup company is given by the function

$$


R(t) = 2\cdot 3^t,


$$

where $t$ is the number of years since the company was incorporated. How long will it take for the company's revenue to reach $18$ million?

To find the solution to this problem, we need to solve the equation $R(t) = 18.$ This gives us the equation

$$


2\cdot 3^t = 18.


$$

To solve this equation, we first divide both sides by $2{:}$

$$


\begin{aligned}2⋅3^{𝑡} & =18 \\ \frac{2⋅3^{𝑡}}{2} & =\frac{18}{2} \\ \frac{2⋅3^{𝑡}}{2} & =9 \\ 3^{𝑡} & =9\end{aligned}


$$

Now, we notice that $9$ is a power of $3,$ because $9=3^2.$ So we get

$$


3^{\color{blue}t} = 3^{\color{blue}2}.


$$

The bases of both exponents are equal, so the powers must also be equal. Therefore, our solution is

$$


t = {\color{blue}2}.


$$

We conclude that it will take the company $\color{blue}2$ years to reach a revenue of $18$ million.

### Example: Solving for an Unknown Time

#### Question

The number of hedgehogs $N(t)$ in a particular nature reserve after $t$ years is modeled by the function

$$


N(t) = 30 \cdot 2^t.


$$

How many years will it take for the population of hedgehogs to increase to $7\,680?$

#### Explanation

To find the time it takes for the number of hedgehogs to reach $7\,680,$ we need to solve the equation $N(t)=7\,680$ for $t,$ as follows:

$$


\begin{aligned}𝑁(𝑡) & =7\,680 \\ 30⋅2^{𝑡} & =7\,680 \\ 2^{𝑡} & =\frac{7\,680}{30} \\ 2^{𝑡} & =256 \\ 2^{𝑡} & =2^{8}\end{aligned}


$$

Therefore, it will take $t=8$ years for the population of hedgehogs to increase to $7\,680.$

### Example: Creating a Model and Solving for an Unknown Time

#### Question

Bob invests $250$ into some high-growth stocks, and the value of his investment doubles every year. How long will it take for Bob's investment to increase to $16\,000?$

#### Explanation

We know that Bob's investment doubles every year. So the value of Bob's investment, which we'll call $y(t),$ grows exponentially with a growth factor of $2.$

The formula for exponential growth (in terms of a growth factor $b$) is

$$


y(t) = ab^t.


$$

From the given information, we have the following:

- $a=250$ is the initial investment (in dollars).

- $b=2$ is the growth factor.

- $t$ is the time, in years, since the investment was first made.

Therefore, the expression for $y(t)$ is

$$


y(t) = 250\cdot 2^t.


$$

Now, to find the time taken for the investment to reach $16\,000,$ we need to solve the equation $y(t) = 16\,000$ for $t,$ as follows:

$$


\begin{aligned}𝑦(𝑡) & =16\,000 \\ 250⋅2^{𝑡} & =16\,000 \\ 2^{𝑡} & =\frac{16\,000}{250} \\ 2^{𝑡} & =64 \\ 2^{𝑡} & =2^{6} \\ 𝑡 & =6\end{aligned}


$$

Therefore, it will take $6$ years for Bob's investment to grow to $16\,000.$

### Example: Creating and Solving a Model Given Some Percentage Growth

#### Question

Mary is conducting a scientific experiment with bacteria. She notices that the number of bacteria in a Petri dish grows by $15\%$ each day. If there were initially $100$ bacteria in the dish, what equation does Mary need to solve to predict how long it will take for the number of bacteria to increase to $535?$

#### Explanation

The number of bacteria $y(t)$ grows exponentially with a growth rate of $15\%.$

The formula for exponential growth (in terms of a growth rate $r$) is

$$


y = a(1+r)^t.


$$

From the given information, we have the following:

- $a=100$ is the initial number of bacteria.

- $r = 0.15$ is the growth rate.

- $t$ is the time, in days, since the experiment is started.

So, the expression for $y(t)$ is

$$


y(t) = 100\cdot(1+0.15)^t = 100\cdot (1.15)^t.


$$

Therefore, to find the time it will take for the number of bacteria to reach $535,$ we would need to solve the equation $y(t)= 535,$ which gives

$$


\begin{aligned}100⋅(1.15)^{𝑡} & =535.\end{aligned}


$$

### Unknown Initial Values

We often need to know the system's state at $t=0$ when using an exponential growth model.

For example, suppose that the number of users $N(t)$ of a new phone app can be modeled by the function

$$


N(t) = N_0(1.2)^t,


$$

where $t$ represents the time, in weeks, since the app launched, and $N_0$ is a constant. If there are $5\,000$ users $5$ weeks after launch, can we determine how many users the app had when it launched?

Here, $N_0$ represents the initial number of users, and this is what we're trying to find.

From the given information, we know that $N(5) = 5\,000,$ So let's plug this into our function:

$$


5\,000 = N_0(1.2)^5


$$

To solve this equation, we can divide both sides by $(1.2)^5{:}$

$$


\begin{aligned}\frac{5\,000}{(1.2)^{5}} & =\frac{𝑁_{0}(1.2)^{5}}{(1.2)^{5}} \\ \frac{5\,000}{(1.2)^{5}} & =\frac{𝑁_{0}(1.2)^{5}}{(1.2)^{5}} \\ \frac{5\,000}{(1.2)^{5}} & =𝑁_{0}\end{aligned}


$$

Let's flip the equation around to make it easier to work with.

$$


N_0 = \dfrac{5\,000}{(1.2)^5}


$$

We can now work out $N_0$ using a calculator. We find that

$$


N_0\approx 2\,009.


$$

We have rounded to the nearest integer since $N_0$ refers to a number of people.

Therefore, when it launched, the app had $2\,009$ users.

### Example: Solving for an Unknown Initial Value

#### Question

Some scientists are monitoring the growth of the wolf population in a particular nature reserve. The population of wolves $W(t)$ after $t$ decades of observations is given by

$$


W(t) = W_{0} \cdot 4^{t},


$$

where $W_{0}$ represents the wolves' population at the beginning of the study. If there were $3\,200$ wolves after $3$ decades, how many wolves were there at the beginning of the study?

#### Explanation

There are $3\,200$ wolves $3$ decades after the scientists started studying the wolf population, so $W(3) = 3\,200.$

To find the initial number of wolves $W_0,$ we substitute $t=3$ and $W(3) = 3\,200$ into the given equation and solve for $W_0,$ as follows:

$$


\begin{aligned}𝑊(3) & =𝑊_{0}⋅4^{3} \\ 3\,200 & =𝑊_{0}⋅64 \\ 𝑊_{0} & =\frac{3\,200}{64} \\ 𝑊_{0} & =50\end{aligned}


$$

Therefore, there were $50$ wolves at the beginning of the study.
