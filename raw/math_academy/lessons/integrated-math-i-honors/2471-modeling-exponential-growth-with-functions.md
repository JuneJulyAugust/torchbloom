# Modeling Exponential Growth With Functions

Source: https://www.mathacademy.com/topics/2471?courseId=127
Topic ID: 2471

## Prerequisites

- [Exponential Functions](../algebra-i/1153-exponential-functions.md)
- [Creating Exponential Growth Expressions](../algebra-i/1499-creating-exponential-growth-expressions.md)
- [Degrees of Accuracy](../algebra-i/2234-degrees-of-accuracy.md)

## Lesson

### Introduction

Suppose that there are $120$ deer in a wildlife reserve. If the deer population doubles every year, can we find a function that gives the number of deer after $t$ years?

First, let's write down what we know:

- $a = 120$ is the **initial number** of deer

- $b =2$ is the **growth factor** (equal to $2$ because the number of deer doubles every year)

- $t=$ the time (in years)

We let $y(t)$ be the number of deer in the reserve after $t$ years. The formula for $y(t)$ is given by

$$


y(t) = ab^t.


$$

Substituting our values for $a$ and $b,$ we get

$$


y(t) = 120\cdot 2^t.


$$

We can use this formula to find the number of deer in the reserve for any value of $t \geq 0.$ For example, to find the number of deer after $3$ years, we substitute $t=3$ into the function:

$$


\begin{aligned}𝑦(3) & =120⋅2^{3} \\ & =120⋅8 \\ & =960\end{aligned}


$$

So there will be $960$ deer after $3$ years.

Finally, notice that substituting $t=0$ into the formula gives the initial number of deer:

$$


\begin{aligned}𝑦(0) & =120⋅2^{0} \\ & =120⋅1 \\ & =120\end{aligned}


$$

### Example: Modeling Exponential Growth Using a Growth Factor

#### Question

A computer has $10$ files infected with a computer virus. If the number of infected files quadruples every hour, find a function that gives the number of infected files after $t$ hours. How many infected files will there be after $6$ hours?

#### Explanation

The number of infected files, $y(t),$ grows exponentially with a growth factor of $4.$

Let's write down what we know:

- $a = 10$ is the initial number of infected files

- $b = 4$ is the growth factor (the number of infected files quadruples)

- $t=$ the time (in hours)

The formula for exponential growth (in terms of a growth factor $b$) is

$$


y = ab^t.


$$

Therefore, the correct expression for $y(t)$ is

$$


y(t)= 10 \cdot 4^{t}.


$$

To find the number of files infected after $6$ hours, we substitute $t=6$ into the above:

$$


y(6) = 10 \cdot 4^{6} = 40\,960


$$

Therefore, the computer will have $40\,960$ infected files after $6$ hours.

### Modeling Exponential Growth Using a Growth Rate

When dealing with exponential growth, it's more common to be given a **growth rate** instead of a growth factor. A growth rate is usually expressed as a percent.

For example, suppose that an investor invests $500$ dollars in the shares of some high-growth companies. It's expected that the investment will grow by $35\%$ each year. Can we write a function that describes the value of the investment after $t$ years?

Let's write down what we know:

- $a=500$ is the **initial value** of the investment

- $r = 0.35$ is the **growth rate** (this is simply $35\%$ expressed as a decimal)

- $t$ is the time (in years)

Let $y(t)$ be the value of the investment after $t$ years. The formula for $y(t)$ is given by

$$


y = a(1+r)^t.


$$

Substituting in our values for $a$ and $r,$ we get

$$


y(t) = 500(1+0.35)^t.


$$

Simplifying the above, we arrive at

$$


y(t) = 500(1.35)^t.


$$

When creating exponential growth functions, the key takeaway is this:

- If you're given a **growth rate** $r$ (usually expressed as a percent), then use the formula $y = a(1+r)^t.$

- If you're given a **growth factor** $b,$ then use the formula $y = ab^t.$

### Example: Modeling Exponential Growth Using a Growth Rate

#### Question

In the week of opening, the grocery store sold $20$ kilograms of apples. After that, the weekly sales increased by $25 \%$ every week.

Find a function that models the total weight of apples sold in week $t$ after opening, and use this function to find the total amount of apples sold in the $4$th week.

#### Explanation

The number of kilograms of apples sold $y(t)$ grows exponentially with a growth rate of $25 \%.$

Let's write down what we know:

- $a = 20$ is the total weight of the apples (in kilograms) sold initially

- $r = 0.25$ is the growth rate ($25 \%$ expressed as a decimal)

- $t=$ the time (in weeks) after opening

The formula for exponential growth (in terms of a growth rate $r$) is

$$


y = a(1+r)^t.


$$

Therefore, the correct expression for $y(t)$ is

$$


y = 20 \cdot (1 + 0.25)^{t}.


$$

Simplifying the above, we get

$$


y(t) = 20 \cdot (1.25)^{t}.


$$

To find the total weight of apples sold in week $4,$ we evaluate the above for $t=4\mathbin{:}$

$$


y(4) = 20 \cdot (1.25)^{4} \approx 49


$$

Therefore, approximately $49$ kilograms of apples were sold in week $4.$

### Example: Modeling Exponential Growth Using Percentage Increases Greater Than 100%

#### Question

A podcast was released with $80$ initial listeners. An exponential model estimates that at the end of each week after release, the number of listeners increased by $190\%$ of the number of listeners at the end of the previous week.

According to this model, how many listeners are there estimated to be after $2$ weeks?

#### Explanation

The number of listeners $L(t)$ grows exponentially with a growth rate of $190\%.$

Let's write down what we know:

- $a = 80$ is the total number of listeners initially

- $r = 1.9$ is the growth rate ($190\%$ expressed as a decimal)

- $t=$ the time (in weeks) after release

The formula for exponential growth is

$$


L = a(1+r)^t.


$$

Therefore, the correct expression for $L(t)$ is

$$


L = 80 \cdot (1 + 1.9)^{t}.


$$

Simplifying the above, we get

$$


L(t) = 80 \cdot (2.9)^{t}.


$$

To find the total number of listeners after $2$ weeks, we evaluate the above for $t=2{:}$

$$


L(2) = 80 \cdot (2.9)^{2} \approx 673


$$

Therefore, the estimated number of listeners after $2$ weeks is $673.$
