# Constructing Linear Functions

Source: https://www.mathacademy.com/topics/6219?courseId=127
Topic ID: 6219

## Prerequisites

- [The Domain of a Function](../../../traditional/lessons/algebra-i/802-the-domain-of-a-function.md)
- [Modeling With Linear Functions](../../../traditional/lessons/algebra-i/2220-modeling-with-linear-functions.md)

## Lesson

### Introduction

We often use linear functions in real-world situations to describe relationships between quantities.

For example, suppose a writer is tracking their progress while typing a draft. They observe that

- after $2$ minutes, they have typed $300$ words, and

- after $5$ minutes, they have typed $750$ words.

We can build a linear function to model this situation.

Let $x$ represent the number of minutes, and $g(x)$ represent the number of words typed after $x$ minutes. Then, the linear function modeling this situation is

$$


g(x) = mx + b,


$$

for some slope $m$ and value $b,$ which we need to find.

From the two observations, we know two points on the line:

$$


\begin{aligned}(𝑥_{1},𝑦_{1}) & =(2,300) \\ (𝑥_{2},𝑦_{2}) & =(5,750)\end{aligned}


$$

Using the given two points, we find the slope $m$ using the slope formula:

$$


\begin{aligned}𝑚 & =\frac{𝑦_{2}−𝑦_{1}}{𝑥_{2}−𝑥_{1}} \\ & =\frac{750−300}{5−2} \\ & =\frac{450}{3} \\ & =150\end{aligned}


$$

This means that the writer is typing at a rate of $150$ words per minute. So, the linear function is

$$


\begin{aligned}𝑔(𝑥) & =𝑚𝑥+𝑏 \\ & =150𝑥+𝑏.\end{aligned}


$$

To find the value of $b,$ we substitute one of the points, say $(2, 300),$ into this equation:

$$


\begin{aligned}300 & =150×2+𝑏 \\ 300 & =300+𝑏 \\ 𝑏 & =0\end{aligned}


$$

This means the starting number of words is $0$ - the writer began typing from scratch. Therefore, the linear equation that defines $g(x)$ is

$$


g(x) = 150x.


$$

### Example: Constructing Linear Functions Using Slope-Intercept Form

#### Question

A linear function $g(x)$ gives the remaining mobile data, in gigabytes, on a monthly plan after $x$ days of continuous usage. There are $48$ GB remaining after $2$ days, and $30$ GB remaining after $5$ days. Which equation defines $g(x)?$

#### Explanation

The linear function modeling this situation is

$$


g(x) = mx + b.


$$

We know two points on the line:

$$


\begin{aligned}(𝑥_{1},𝑦_{1}) & =(2,48) \\ (𝑥_{2},𝑦_{2}) & =(5,30)\end{aligned}


$$

Using the given two points, we find the slope $m{:}$

$$


\begin{aligned}𝑚 & =\frac{𝑦_{2}−𝑦_{1}}{𝑥_{2}−𝑥_{1}} \\ & =\frac{30−48}{5−2} \\ & =\frac{−18}{3} \\ & =−6\end{aligned}


$$

So, the linear function is

$$


\begin{aligned}𝑔(𝑥) & =𝑚𝑥+𝑏 \\ & =−6𝑥+𝑏.\end{aligned}


$$

To find the value of $b,$ we substitute one of the points, say $(2, 48),$ into this equation:

$$


\begin{aligned}48 & =−6×2+𝑏 \\ 48 & =−12+𝑏 \\ 𝑏 & =60\end{aligned}


$$

Therefore, the linear equation that defines $g(x)$ is

$$


g(x) = -6x + 60.


$$

### Example: Constructing Functions From Tabular Data

#### Question

Some values of the linear function $r$ are shown in the table above. Which of the following defines $r(x)?$

#### Explanation

Since $r$ is a linear function, we know it must be of the form

$$


r(x) = mx + b


$$

where

- $m$ is the slope, and

- $b$ is the $y$-intercept.

First, we find the slope using two points. For $x = 6$ and $x = 9,$ we have

$$


\begin{aligned}𝑚 & =\frac{𝑟(𝑥_{2})−𝑟(𝑥_{1})}{𝑥_{2}−𝑥_{1}} \\ & =\frac{31−22}{9−6} \\ & =\frac{9}{3} \\ & =3.\end{aligned}


$$

So, the linear function is

$$


\begin{aligned}𝑟(𝑥) & =𝑚𝑥+𝑏 \\ & =3𝑥+𝑏.\end{aligned}


$$

Next, we find the $y$-intercept using one point. For $x = 6,$ we have

$$


\begin{aligned}𝑟(6) & =3(6)+𝑏 \\ 22 & =18+𝑏 \\ 𝑏 & =4.\end{aligned}


$$

Therefore, the linear equation that defines $r(x)$ is

$$


r(x) = 3x + 4.


$$

### Linear Functions With Alternative Domains

Sometimes, when modeling real-life situations with linear functions, the independent variable does not start at zero.

For example, suppose a puzzle enthusiast is working on a large jigsaw puzzle. Their progress follows this pattern:

- On the first day, they place $50$ pieces.

- They add $30$ more pieces on each of the following days.

With this, we can construct a linear function $P$ for the total number of puzzle pieces placed after $d$ days, where $d \geq 1.$

First, let's break down the pattern to understand it:

- On day $d=1,$ they place $P=50$ pieces.

- On day $d=2,$ they place $P=50+30=80$ pieces in total.

- On day $d=3,$ they place $P=50+30+30=110$ pieces in total.

- $\cdots$

And so on.

Notice that the amount added each day after the first is always $30.$ So the total number of pieces placed includes

- the initial $50$ pieces placed on the first day, and

- $30$ pieces for each additional day *beyond the first*. Since the first $50$ pieces are placed on day $1,$ the number of *additional* pieces placed by day $d$ equals

Therefore, the total number of pieces $P$ placed after $d$ days, where $d \geq 1,$ is

$$


\begin{aligned}𝑃(𝑑) & =50+30(𝑑−1) \\ & =50+30𝑑−30 \\ & =30𝑑+20.\end{aligned}


$$

Let's see another example.

### Example: Constructing Functions With Alternative Domains

#### Question

A theme park charges $65$ per person for the first $30$ people in a group and $50$ for each additional person. Which function $C$ gives the total cost, in dollars, for a group of $g$ people, where $g \geq 30?$

#### Explanation

The total cost consists of two parts.

- For the first $30$ people, the park charges

$$


65 \times 30 = 1,950\,\,\text{dollars}.


$$

- For the additional persons beyond $30,$ the park charges

$$


50(g - 30)\,\,\text{dollars}.


$$

Therefore, the total cost $C,$ in dollars, for a group of $g$ people, where $g\geq 30,$ is

$$


\begin{aligned}𝐶(𝑔) & =1,950+50(𝑔−30) \\ & =1,950+50𝑔−1,500 \\ & =50𝑔+450.\end{aligned}


$$
