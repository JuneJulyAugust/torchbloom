# Modeling With Compound Interest

Source: https://www.mathacademy.com/topics/1481?courseId=51
Topic ID: 1481

## Prerequisites

- [Solving Exponential Equations Using Logarithms](./1482-solving-exponential-equations-using-logarithms.md)
- [Solving Exponential Growth Problems](../algebra-i/2464-solving-exponential-growth-problems.md)

## Lesson

### Introduction

When money is deposited into a bank account, the bank pays an **annual interest.** This interest can be **compounded**, or split, throughout the year.

The interest is worked out for the first period and added to the total. Then, the interest is calculated for the next period, added to the total, and so on.

To calculate how much money, $P,$ we will have in an account after $t$ years, we can use the **compound interest equation**:

$$



\begin{aligned} P &= P_0\left(1 + \dfrac r n \right)^{nt}, \\\end{aligned}



$$

where $P_0$ is the initial deposit, $r$ is the annual interest rate, and $n$ is the number of times payments are compounded per year.

For example, suppose you deposit $P_0=1,000$ into a bank account, and a bank employee suggests three options:

- An account paying $r=12\%$ annual interest compounded yearly.

- An account paying $r=12\%$ annual interest compounded quarterly.

- An account paying $r=12\%$ annual interest compounded monthly.

Which should you choose to have the most money after $t=1$ year?

- If payments are **compounded annually**, there is only $n=1$ payment in the year. In this case, at the end of the first year, we will have

- When payments are **compounded quarterly**, we receive a payment for each quarter of the year. There are $n=4$ quarters in the year, so at the end of the first year, we will get

- On the other hand, when payments are **compounded monthly**, we receive a payment each month of the year. There are $n=12$ months in the year, so at the end of the first year, we will have

The accounts are not the same after all! The most profitable account is the one with the annual interest compounded monthly.

### Example: Calculating an Amount of Money After Compound Interest Is Applied

#### Question

Rebecca invested $10,000$ into an account paying a $3\%$ annual interest, compounded monthly. How much money will be in her account after $10$ years? Round your answer to the nearest dollar.

#### Explanation

The compound interest equation states that

$$



\begin{aligned} P &= P_0\left(1 + \dfrac r n \right)^{nt}. \end{aligned}



$$

There are $12$ months in one year, so $n=12.$ We also have an initial amount of $P_0=10,000,$ an annual interest of $r=0.03,$ and a length of $t=10$ years. Substituting these values into the formula, we obtain

$$



\begin{aligned} P &= P_0\left(1 + \dfrac {r} {n} \right)^{(n)(t)} \\[5pt] &= 10,000\left(1 + \dfrac {0.03} {12} \right)^{(12)(10)} \\[5pt] &= 10,000(1 + 0.0025)^{120} \\[5pt] &= 10,000(1.0025)^{120} \\[5pt] &= 10,000(1.349\,353...) \\[5pt] &= 13,493.53...\\[5pt] &\approx 13,494. \end{aligned}



$$

Consequently, after $10$ years Rebecca will have $13,494$ in the account.

### Example: Calculating an Initial Deposit

#### Question

How much money would you need to deposit today at a $2\%$ annual interest rate, compounded yearly, to have $10,000$ in the account after $10$ years? Round your answer to the nearest dollar.

#### Explanation

The compound interest equation states that

$$



\begin{aligned} P &= P_0\left(1 + \dfrac r n \right)^{nt}. \end{aligned}



$$

Since the payments are compounded yearly, we have $n=1.$ We also have an annual rate of $r=0.02,$ and a final amount of $P=10,000$ after $t=10$ years. To find the initial deposit, $P_0,$ we substitute these values into the formula and solve for $P_0\mathbin{:}$

$$



\begin{aligned} P &= P_0\left(1 + \dfrac {r} {n}\right)^{nt} \\[5pt] 10,000 &=P_0\left(1 + \dfrac {0.02} {1}\right)^{(1)(10)} \\[5pt] 10,000 &= P_0(1.02)^{10} \\[5pt] 10,000 &= P_0(1.218,994...) \\[5pt] P_0 &= \dfrac {10,000} {1.218,994...} \\[5pt] P_0 &= 8,203.48... \\[5pt] P_0 &\approx 8,203 \end{aligned}



$$

Consequently, you would need to deposit $8,203.$

### Example: Calculating the Number of Years to Yield a Particular Amount

#### Question

If you deposit into an account with a annual interest rate, compounded quarterly, how many years will it take until there is at least in the account?

#### Explanation

The compound interest equation states that

The annual interest is compounded quarterly, and there are quarters in one year, so We also have an initial amount of and annual rate of

To find the number of years it will take until we substitute these values into the formula and solve for

Remember payments are compounded quarterly, so we must choose either or years.

- After years, there is still less than in the account, because

- After years, there will be more than in the account, since

Therefore, it will take years (years and quarters) until there is at least in the account.
