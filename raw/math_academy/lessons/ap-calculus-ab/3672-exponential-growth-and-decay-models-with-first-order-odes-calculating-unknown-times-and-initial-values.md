# Exponential Growth and Decay Models With First-Order ODEs: Calculating Unknown Times and Initial Values

Source: https://www.mathacademy.com/topics/3672?courseId=24
Topic ID: 3672

## Prerequisites

- [Exponential Growth and Decay Models With First-Order ODEs](./876-exponential-growth-and-decay-models-with-first-order-odes.md)

## Lesson

### Introduction

If a population is growing, we are often interested to know how long it will take for the population to reach a particular size.

Since the rate of growth of a population is often modeled using a differential equation, we typically follow a three-step process:

- **Step 1:** Find the general solution of the differential equation.

- **Step 2:** Apply an initial condition to find a particular solution.

- **Step 3:** Use the particular solution to set up and solve an equation for the unknown quantity.

Let's apply this process to an example.

### A Worked Example

Suppose that the population $P(t)$ of a particular bacteria grows according to the differential equation

$$


\dfrac{\textrm{d}P}{\textrm{d}t} = \dfrac15 P,


$$

where $t$ is the time, measured in hours. There were initially $1\,000$ bacteria. How long will it take for the population size to increase to $100\,000?$

- **Step 1:** Find the general solution. The given differential equation is an exponential growth equation. The general solution is where $P_0$ is the initial population.

- **Step 2:** Find the particular solution. We are given that the initial population is $1\,000.$ Therefore, we set $P_0 = 1\,000$ to get the particular solution:

- **Step 3:** Solve for the required value. To find how long it takes for the population to reach $100\,000,$ we set $P(t)=100\,000$ and solve for $t{:}$

Therefore, it takes approximately $23$ hours for the bacteria population to grow to $100\,000.$

### Example: Computing an Unknown Time Given an Exponential Growth Model

#### Question

The rate at which the balance in a savings account grows $B(t),$ after $t$ years, can be modeled by the differential equation

$$


\dfrac{\textrm d B}{\textrm d t} = 0.05B.


$$

How many years does it take for the balance to increase by $60\%?$ Round your answer to the nearest year.

#### Explanation

We model the balance growth using the differential equation

$$


\dfrac{\textrm d B}{\textrm d t} = 0.05B.


$$

The solution to this equation is

$$


B(t) = B_0\,e^{0.05t},


$$

where $B_0$ is the initial balance.

Let $t_1$ be the time when the balance has increased by $60\%.$ That is,

$$


B(t_1) = 1.6B_0.


$$

We solve the above equation for $t_1,$ as follows:

$$


\begin{aligned}𝐵(𝑡_{1}) & =𝐵_{0}𝑒^{0.05⋅𝑡_{1}} \\ 1.6𝐵_{0} & =𝐵_{0}𝑒^{0.05𝑡_{1}} \\ 1.6 & =𝑒^{0.05𝑡_{1}} \\ ln⁡(1.6) & =ln⁡(𝑒^{0.05𝑡_{1}}) \\ ln⁡(1.6) & =0.05𝑡_{1} \\ 𝑡_{1} & =\frac{ln⁡(1.6)}{0.05} \\ 𝑡_{1} & ≈9.40\end{aligned}


$$

Rounding to the nearest integer, we conclude that it takes $9$ years for the balance to increase by $60\%.$

### Example: Computing an Unknown Time Given an Exponential Decay Model

#### Question

The rate at which the amount of medicine in a person’s bloodstream decreases $M(t),$ after $t$ hours, can be modeled by the differential equation

$$


\dfrac{\textrm{d}M}{\textrm{d}t} = -0.08M.


$$

How many hours does it take for the amount of medicine to decrease to $30\%$ of the original amount? Round your answer to the nearest hour.

#### Explanation

We model the amount of medicine using the differential equation

$$


\dfrac{\textrm{d}M}{\textrm{d}t} = -0.08M.


$$

The solution to this equation is

$$


M(t) = M_0\,e^{-0.08t},


$$

where $M_0$ is the initial amount of medicine.

Let $t_1$ be the time when the amount of medicine is $30\%$ of the original amount. That is,

$$


M(t_1) = 0.30M_0.


$$

We solve the above equation for $t_1,$ as follows:

$$


\begin{aligned}0.30𝑀_{0} & =𝑀_{0}\,𝑒^{−0.08𝑡_{1}} \\ 0.30 & =𝑒^{−0.08𝑡_{1}} \\ ln⁡(0.30) & =ln⁡(𝑒^{−0.08𝑡_{1}}) \\ ln⁡(0.30) & =−0.08𝑡_{1} \\ 𝑡_{1} & =−\frac{ln⁡(0.30)}{0.08} \\ 𝑡_{1} & ≈15.050\end{aligned}


$$

Rounding to the nearest integer, we conclude that it takes $15$ hours for the amount of medicine to decrease to $30\%$ of the original amount.

### Example: Computing an Unknown Time Given an Exponential Growth or Decay Model With an Unknown Rate

#### Question

During an experiment, the weight $W(t)$ of an object varies according to the differential equation $W'(t) = -r W(t),$ where $t$ is the time, measured in hours, and $r > 0.$ It is known that the object's weight reduces by three-quarters after the first two hours. How long does it take for the object's weight to reduce to one-sixth of its original weight? Round your answer to one decimal place.

#### Explanation

The general solution to the given differential equation is

$$


W(t) = W_0 e^{-rt},


$$

where $W_0$ is the weight when $t=0.$

Let $t_1$ be the time when the weight equals $\dfrac{1}{6}W_0.$ Then, we have

$$


\begin{aligned}𝑊(𝑡_{1}) & =\frac{1}{6}𝑊_{0}\,⇒\,𝑊_{0}𝑒^{−𝑟𝑡_{1}}=\frac{1}{6}𝑊_{0}.\end{aligned}


$$

We solve this equation for $t_1,$ as follows:

$$


\begin{aligned}𝑊_{0}𝑒^{−𝑟𝑡_{1}} & =\frac{1}{6}𝑊_{0} \\ 𝑊_{0}𝑒^{−𝑟𝑡_{1}} & =\frac{1}{6}𝑊_{0} \\ 𝑒^{−𝑟𝑡_{1}} & =\frac{1}{6} \\ ln⁡(𝑒^{−𝑟𝑡_{1}}) & =ln⁡(\frac{1}{6}) \\ −𝑟𝑡_{1} & =−ln⁡6 \\ 𝑡_{1} & =\frac{ln⁡6}{𝑟}\,\,(∗)\end{aligned}


$$

We now need to calculate $r.$ We're told that the weight reduces by three-quarters after the first two hours. Therefore, one-quarter of the weight remains, and we have

$$


W(2) = \dfrac{1}{4}W_0\quad \Rightarrow\quad W_0e^{-2r} = \dfrac{1}{4}W_0


$$

We solve this equation for $r,$ as follows:

$$


\begin{aligned}𝑊_{0}𝑒^{−2𝑟} & =\frac{1}{4}𝑊_{0} \\ 𝑊_{0}𝑒^{−2𝑟} & =\frac{1}{4}𝑊_{0} \\ 𝑒^{−2𝑟} & =\frac{1}{4} \\ ln⁡(𝑒^{−2𝑟}) & =ln⁡(\frac{1}{4}) \\ −2𝑟 & =−ln⁡4 \\ 𝑟 & =\frac{1}{2}ln⁡4 \\ 𝑟 & =ln⁡4^{1/2} \\ 𝑟 & =ln⁡2\end{aligned}


$$

Finally, substituting this into $(*)$ and evaluating, we get

$$


\begin{aligned}𝑡_{1} & =\frac{ln⁡6}{𝑟} \\ & =\frac{ln⁡6}{ln⁡2} \\ & ≈2.6\end{aligned}


$$

rounded to one decimal place.

Therefore, we conclude that it takes approximately $2.6$ hours for the weight to reduce to one-sixth of its original weight.

### Example: Calculating an Unknown Initial Value

#### Question

A marathon runner is participating in a race. The remaining distance $D(t)$ they have left to run $t$ hours since starting the race can be modeled by the differential equation $D'(t)= -0.8D(t).$ Two hours into the race, they have $6\,\text{km}$ remaining. Calculate the distance remaining after four hours.

#### Explanation

The general solution to the given differential equation is

$$


D(t) = D_0\,e^{-0.8t},


$$

where $D_0$ is the remaining distance when $t=0.$

We are given that the remaining distance was $6\,\text{km}$ after $2$ hours. So, substituting $t=2$ and $D(2)=6$ into our general solution and solving for $D_0,$ we get

$$


\begin{aligned}𝐷(2) & =𝐷_{0}\,𝑒^{−0.8⋅2} \\ 6 & =𝐷_{0}\,𝑒^{−1.6} \\ 𝐷_{0} & =\frac{6}{𝑒^{−1.6}} \\ & ≈29.718,\end{aligned}


$$

rounded to $3$ decimal places.

Hence, our particular solution is

$$


D(t) = 29.718\,e^{-0.8t}.


$$

We want to find the distance remaining after $4$ hours. So, substituting $t=4$ into our particular solution, we get

$$


\begin{aligned}𝐷(4) & =29.718\,𝑒^{−0.8⋅4} \\ & =29.718\,𝑒^{−3.2} \\ & ≈1.2,\end{aligned}


$$

rounded to one decimal place.

Therefore, the remaining distance after $4$ hours is $1.2\,\text{km}.$
