# Modeling Financial Problems Using Geometric Series

Source: https://www.mathacademy.com/topics/3681?courseId=43
Topic ID: 3681

## Prerequisites

- [Continuously Compounded Interest](../algebra-ii/237-continuously-compounded-interest.md)
- [The Sum of a Finite Geometric Series](./1016-the-sum-of-a-finite-geometric-series.md)

## Lesson

### Introduction

An investor plans to retire in $30$ years, and they wish to build up enough savings to live on throughout their retirement. So they decide to place $5\,000$ into an investment account that generates a return of $8\%,$ compounded annually.

The value $S_n$ of this investment after $n$ years is given by the exponential growth expression

$$



S_n = 5\,000\cdot (1.08)^n.



$$

Therefore, the value of this investment in $30$ years is

$$



S_{30} = 5\,000\cdot (1.08)^{30} \approx 50\,313.



$$

While $50\,313$ might seem like a lot of money, it is unlikely to be enough to cover the investor's retirement.

In reality, it's unlikely that an investor will make a single deposit into an investment account and leave it there for $30$ years. Instead, they are more likely to make multiple deposits throughout their life.

In this lesson, we learn how geometric series can be used to calculate the value of an investment portfolio when an investor makes multiple deposits.

### Calculating the Value of an Investment With Annual Compounding

Now let's suppose that the investor pays $5\,000$ *per year* into an investment account that generates a return of $8\%,$ compounded annually. Let $S_n$ be the value of the investment at the end of the $n$th year. Our goal is to calculate $S_{30},$ the value of the portfolio when the investor retires in $30$ years.

Let's work out $S_n$ for $n=1,2,3,\ldots,$ and see if we can spot a pattern.

- At the end of year $1,$ the investment will be worth

- To calculate the value of the investment at the end of year $2,$ we first need to add $5\,000$ to the balance at the end of year $1.$ This gives the expression Then, we increase the amount by $8 \%.$ Therefore, at the end of the year $2,$ the investment will be worth Substituting our expression for $S_1$ and expanding the parentheses, we get

- Similarly, at the end of the year $3,$ the investment will be worth

You can probably spot the pattern now. We can deduce that the expression for $S_{30}$ is equal to

$$



5\,000⋅(1.08)^{2}+



$$

To evaluate this sum, we first factor it as follows:

$$



S_{30} = 5\,000\cdot (1.08) \cdot \left[ (1.08)^{29} +(1.08)^{28} + \cdots + (1.08) + 1 \right]



$$

Notice that the expression inside the square brackets is a geometric series with $a_1 = 1,$ $r = 1.08,$ and $N = 30.$ Thus, after $30$ years, the investment will be worth

$$



\begin{aligned}𝑆_{30} & =5\,000⋅(1.08)⋅(\frac{𝑎_{1}(1−𝑟^{𝑁})}{1−𝑟}) \\ & =5\,400⋅(\frac{1⋅(1−1.08^{30})}{1−1.08}) \\ & =5\,400⋅(\frac{1−1.08^{30}}{1−1.08}) \\ & ≈611\,729\end{aligned}



$$

rounded to the nearest dollar.

This example illustrates how compound interest can be used to fund retirements. The investor deposited a total of $5\,000\cdot 30 = 150\,000$ over $30$ years, yet this was worth $611\,729$ by the time they retired!

### Example: Calculating the Value of an Investment With Annual Compounding

#### Question

Monica pays into an investment account at the beginning of every year. She earns an annual interest of paid at the end of the year. To the nearest dollar, how much money will be in her investment account by the end of the th year?

#### Explanation

Let be the value of Monica's investment at the end of the th year.

- At the end of the year Monica's investment will be worth

- To calculate the value of the investment at the end of year we need to add to the balance at the end of year and then increase the entire amount by Therefore, at the end of the year Monica's investment will be worth

- Similarly, at the end of the year Monica's investment will be worth

- Continuing this process, we may deduce that by the end of the year Monica's investment will be worth

Notice that the expression inside the square brackets is a geometric series with and Thus, after years, Monica's investment will be worth rounded to the nearest dollar.

### Example: Calculating the Value of an Investment With Monthly Compounding

#### Question

Charlie pays $1\,000$ into an investment account at the beginning of every year. He earns an annual interest of $4.8 \%,$ compounded monthly, paid at the end of each month. To the nearest dollar, how much money will be in his investment account by the end of the $6$th year?

#### Explanation

Let $S_n$ be the value of Charlie's investment at the end of the $n$th year.

- The interest rate is $4.8 \%,$ compounded monthly. Therefore, at the end of year $1,$ Charlie's investment will be worth

- To calculate the value of the investment at the end of year $2,$ we need to add $1\,000$ to the balance at the end of year $1,$ and then increase the entire amount by $4.8 \%,$ compounded monthly. Therefore, at the end of year $2,$ Charlie's investment will be worth

- $\quad \vdots$

- Continuing this process, we may deduce that by the end of year $6,$ Charlie's investment will be worth

Notice that the expression inside the curly braces is a geometric series with $a_1 = 1,$ $r = (1.004)^{12}$ and $N = 6.$ Thus, after $6$ years, Charlie's investment will be worth

$$



\begin{aligned}𝑆_{6} & =1\,000⋅(1.004)^{12}⋅(\frac{𝑎_{1}(1−𝑟^{𝑁})}{1−𝑟}) \\ & =1\,000⋅(1.004)^{12}⋅\frac{1⋅(1−[(1.004)^{12}]^{6})}{1−(1.004)^{12}} \\ & =1\,000⋅(1.004)^{12}⋅(\frac{1−[(1.004)^{12}]^{6}}{1−(1.004)^{12}}) \\ & ≈7\,119\end{aligned}



$$

rounded to the nearest dollar.

### Example: Calculating the Value of an Investment With Continuous Compounding

#### Question

Harold pays $2\,500$ into an investment account at the beginning of every year. He earns an annual interest of $4\%,$ compounded continuously. To the nearest dollar, how much money will be in his investment account by the end of the $10$th year?

#### Explanation

Let $S_n$ be the value of Harold's investment at the end of the $n$th year.

- The interest rate is $4\%$ per year, compounded continuously. Therefore, at the end of year $1,$ Harold's investment will be worth

- To calculate the value of the investment at the end of year $2,$ we need to add $2\,500$ to the balance at the end of year $1,$ and then increase the entire amount by $4\%,$ compounded continuously. Therefore, at the end of year $2,$ Harold's investment will be worth

- $\quad \vdots$

- Continuing this process, we may deduce that by the end of year $10,$ Harold's investment will be worth

Notice that the expression inside the curly braces is a geometric series with $a_1=1$, $r=e^{0.04}$, and $N=10.$ Thus, after $10$ years, Harold's investment will be worth

$$



\begin{aligned}𝑆_{10} & =2\,500⋅𝑒^{0.04}⋅(\frac{𝑎_{1}(1−𝑟^{𝑁})}{1−𝑟}) \\ & =2\,500⋅𝑒^{0.04}⋅\frac{1⋅(1−[𝑒^{0.04}]^{10})}{1−𝑒^{0.04}} \\ & =2\,500⋅𝑒^{0.04}⋅(\frac{1−[𝑒^{0.04}]^{10}}{1−𝑒^{0.04}}) \\ & ≈31\,358\end{aligned}



$$

rounded to the nearest dollar.
