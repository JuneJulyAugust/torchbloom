# Modeling Coin Problems Using Systems of Linear Equations

Source: https://www.mathacademy.com/topics/963?courseId=132
Topic ID: 963

## Prerequisites

- [Systems of Linear Equations With Decimal Coefficients](../../../traditional/lessons/algebra-i/1081-systems-of-linear-equations-with-decimal-coefficients.md)
- [Further Modeling With Linear Equations in Two Variables](../../../traditional/lessons/algebra-i/3765-further-modeling-with-linear-equations-in-two-variables.md)

## Lesson

### Introduction

Suppose that we have $10$ stamps worth $\color{blue}3$ cents each and $4$ stamps worth $\color{blue}5$ cents each. We can compute the total value of our stamps by multiplying the value of each stamp by its quantity and then adding the totals.

$$



\underbrace{ \hspace{.25cm} \color{blue}3 \text{ cents} \hspace{.25cm} }_{\large\color{blue}\text{value}} \times \overbrace{10}^{\large\text{quantity}} + \underbrace{\hspace{.25cm} \color{blue}5 \text{ cents} \hspace{.25cm} }_{\large\color{blue}\text{value}} \times \overbrace{4}^{\large\text{quantity}} = 50 \text{ cents}



$$

We can use this principle to set up equations for problems involving items with monetary values.

For example, if we have $a$ stamps worth $3$ cents each and $b$ stamps worth $5$ cents each, and the total cost of all the stamps is $80$ cents, then

$$



\underbrace{\color{blue}3}_{\large\color{blue}\text{value}} \times \overbrace{a}^{\large\text{quantity}} + \underbrace{\color{blue}5}_{\large\color{blue}\text{value}} \times \overbrace{b}^{\large\text{quantity}} = 80



$$

Also, if we know that there are $16$ stamps in total, then we have

$$



a+b=16.



$$

Therefore, we can represent this problem as the following system of equations in the unknowns $a$ and $b\mathbin{:}$

$$



\begin{aligned}3𝑎+5𝑏=80 \\ 𝑎+𝑏=16\end{aligned}



$$

This system can be solved using substitution or elimination.

### United States Currency

Before we continue, it's worth highlighting some basic details regarding the monetary system used in the United States of America.

- The monetary currency of the United States is the **United States dollar**, or simply **the dollar.** The symbol of the dollar is $.$

- $1$ is equal to $100$ **cents.**

- Physical money (also known as **fiat**) is issued as **bills** (i.e., paper money) or **coins.**

- Bills come in **denominations** of $1, 2, 5, 10, 20, 50,$ and $100.$

- Coins come in the following denominations: $\quad$ $1$-cent - called a **penny** $\quad$ $5$-cent - called a **nickel** $\quad$ $10$-cent - called a **dime** $\quad$ $25$-cent - called a **quarter** $\quad$ $50$-cent - called a **half-dollar** $1$ coins also exist, though they are rare.

### Example: Solving for a Quantity of Coins

#### Question

A wallet contains pennies ($1$-cent coins) and nickels ($5$-cent coins). There are $16$ coins in total. If the total amount of money in the wallet is $0.56$, how many of each coin are there?

#### Explanation

Let $p$ be the number of pennies and $n$ the number of nickels in the wallet.

- There are $16$ coins in total, so $p+n=16.$

- Each penny is worth $1$ cent, each nickel is worth $5$ cents, and the total value of all the coins is $56$ cents, so $p+5n=56.$

Putting these equations together, we have the following system of equations:

$$



\begin{aligned}𝑝+𝑛=16 \\ 𝑝+5𝑛=56\end{aligned}



$$

We will solve the system using elimination. Multiplying the first equation by $-1$ and adding the result to the second equation, we solve for $n\mathbin{:}$

$$



\begin{aligned}−𝑝−𝑛 & =−16 \\ 𝑝+5𝑛 & =56 \\ 4𝑛 & =40 \\ 𝑛 & =10\end{aligned}



$$

To find $p,$ we substitute $n=10$ into the first equation:

$$



\begin{aligned}𝑝+𝑛 & =16 \\ 𝑝+(10) & =16 \\ 𝑝 & =6\end{aligned}



$$

The solution to the system is $p=6$ and $n=10.$ Therefore, there are $6$ pennies and $10$ nickels in the wallet.

### Example: Solving for a Quantity of Items

#### Question

In a store, a box of cereal is $3$, while a box of pasta is $5.$ Ross spends $27$ on boxes of cereal and pasta. If Ross buys a total of $7$ items, how many boxes of pasta does he buy?

#### Explanation

Let $x$ be the number of cereal boxes, and $y$ be the number of pasta boxes.

- Each box of cereal costs $3,$ each box of pasta costs $5,$ and Ross spent $27,$ so $3x+5y=27.$

- Ross bought a total of $7$ items, so $x+y=7.$

Putting these equations together, we have the following system of equations:

$$



\begin{aligned}3𝑥+5𝑦=27 \\ 𝑥+𝑦=7\end{aligned}



$$

We will solve the system using elimination. Multiplying the second equation by $-3$ and adding the result to the first equation, we solve for $y\mathbin{:}$

$$



\begin{aligned}3𝑥+5𝑦 & =27 \\ −3𝑥−3𝑦 & =−21 \\ 2𝑦 & =6 \\ 𝑦 & =3\end{aligned}



$$

Therefore, Ross bought $3$ boxes of pasta.

### Example: Solving for a Value

#### Question

A store sells a bag containing $3\,\mathrm{kg}$ of apples and $2\,\mathrm{kg}$ of plums for $12.$ If the combined price of $2\,\mathrm{kg}$ of plums and $1\,\mathrm{kg}$ of apples is $8$, how much does a kilogram of plums cost?

#### Explanation

Let $x$ be the price of a kilogram of apples and $y$ the price of a kilogram of plums.

- The combined price of $3\,\mathrm{kg}$ of apples and $2\,\mathrm{kg}$ of plums is $12,$ so $3x + 2y = 12.$

- The combined price of $2\,\mathrm{kg}$ of plums and $1\,\mathrm{kg}$ of apples is $8$, so $x+2y = 8.$

Putting these equations together, we have the following system of equations:

$$



\begin{aligned}3𝑥+2𝑦=12 \\ 𝑥+2𝑦=8\end{aligned}



$$

We will solve the system using substitution. We solve for $x$ in the second equation:

$$



\begin{aligned}2𝑦+𝑥 & =8 \\ 𝑥 & =8−2𝑦\end{aligned}



$$

Then, we can substitute $x=8-2y$ into the first equation and solve for $y\mathbin{:}$

$$



\begin{aligned}3𝑥+2𝑦 & =12 \\ 3(8−2𝑦)+2𝑦 & =12 \\ 24−6𝑦+2𝑦 & =12 \\ 24−4𝑦 & =12 \\ −4𝑦 & =−12 \\ 𝑦 & =3\end{aligned}



$$

Therefore, a kilogram of plums costs $3.$
