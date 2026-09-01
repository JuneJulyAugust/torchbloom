# Lower Riemann Sums Over General Rectangular Partitions

Source: https://www.mathacademy.com/topics/2615?courseId=54
Topic ID: 2615

## Prerequisites

- [Double Summations](./1983-double-summations.md)
- [Approximating Volumes Using Lower Riemann Sums](./2613-approximating-volumes-using-lower-riemann-sums.md)

## Lesson

### Introduction

We know how to write the lower Riemann sum for a function $f(x,y)$ over a *fixed* rectangular partition. In this lesson, we will learn how to write down an expression for the lower Riemann sum for an *arbitrary* rectangular partition.

As a concrete example, let $R = [0,1] \times [0,1]$ be a region in the $xy$-plane, and define the function $f(x,y)$ as

$$


f(x,y) = x^2+y^2.


$$

Further, let $P$ be an arbitrary partition of $R,$ where

$$


\begin{aligned}𝑃_{1}={𝑥_{0},𝑥_{1},…,𝑥_{𝑚}},\,𝑃_{2}={𝑦_{0},𝑦_{1},…,𝑦_{𝑛}},\,𝑃=𝑃_{1}×𝑃_{2}.\end{aligned}


$$

Our goal is to find an expression for $L(f, P),$ the lower Riemann sum of $f$ with respect to this partition. We proceed identically to the case where $P$ was fixed.

First, we consider an arbitrary subregion $R_{ij}$ of the partition. This subregion lies between $x_{i-1}$ and $x_i$ over the $x$-axis and $y_{j-1}$ and $y_j$ over the $y$-axis, as shown below.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/f2e5b8df6c41c6ee.png)

Since we're computing the *lower* sum, we're interested in the *minimum* value of $f$ in this subregion.

Notice that

- $f(x,y) = x^2+y^2$ increases as $x$ increases on $[0,1],$ and

- $f(x,y) = x^2+y^2$ increases as $y$ increases on $[0,1].$

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/9911fd8a2333f369.png)

Therefore, the *minimum* value of $f$ in the subregion is attained when we have the *smallest* possible $x$ and the *smallest* possible $y.$ This is the value of $f$ at the *bottom left corner* of the subregion.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/eda2c502cde002c3.png)

So, if $m_{ij}$ denotes the minimum value of $f$ in each subregion, we have

$$


m_{ij} = f(x_{i-1}, y_{j-1}) = x_{i-1}^2 + y_{j-1}^2


$$

for all $1\leq i\leq m$ and $1\leq j\leq n.$

Since the area of $R_{ij}$ is $\Delta x_i\Delta y_j,$ the volume of the rectangular solid with base $R_{ij}$ and height $m_{ij}$ is

$$


m_{ij}\Delta x_i\Delta y_j = (x_{i-1}^2 + y_{j-1}^2)\Delta x_i \Delta y_j \, .


$$

Finally, summing up all of our rectangular solids over the entire partition $P$, we find that the lower Riemann sum is given by

$$


L(f,P) = \sum_{i=1}^m\sum_{j=1}^n (x_{i-1}^2 + y_{j-1}^2)\Delta x_i \Delta y_j \, .


$$

### Example: Writing the Lower Riemann Sum for a Strictly Increasing Function

#### Question

Let $R = [0,2]\times [1,3]$ be a region in the $xy$-plane, and let $f(x,y) = x+2y.$ Further, let $P$ be a partition of $R,$ where

$$


\begin{aligned}𝑃_{1}={𝑥_{0},𝑥_{1},…,𝑥_{𝑚}},\,𝑃_{2}={𝑦_{0},𝑦_{1},…,𝑦_{𝑛}},\,𝑃=𝑃_{1}×𝑃_{2}.\end{aligned}


$$

Write down the lower Riemann sum $L(f, P).$

#### Explanation

The lower Riemann sum is given by

$$


\begin{aligned}𝐿(𝑓,𝑃) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑚_{𝑖𝑗}Δ𝑥_{𝑖}Δ𝑦_{𝑗}\end{aligned}


$$

where $m_{ij}$ is the ** value of $f$ in each subregion $R_{ij}.$

We consider an arbitrary subregion $R_{ij}$ of the partition. This subregion lies between $x_{i-1}$ and $x_i$ over the $x$-axis and $y_{i-1}$ and $y_i$ over the $y$-axis, as shown below.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/50f9c6106d41da71.png)

Notice that

- $f(x,y) = x+2y$ increases as $x$ increases, and

- $f(x,y) = x+2y$ increases as $y$ increases.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/ca0d09efd77a162a.png)

As a result, the ** value of $f$ in each subregion is attained when we have the ** possible $x$ and the ** possible $y$. This is the value at the ** of each subregion.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/a8df8e1140e2fa1a.png)

Therefore,

$$


\begin{aligned}𝑚_{𝑖𝑗} & =𝑓(𝑥_{𝑖−1},𝑦_{𝑗−1})=𝑥_{𝑖−1}+2𝑦_{𝑗−1}\end{aligned}


$$

for all $1\leq i\leq m$ and $1\leq j\leq n.$

Finally, the lower Riemann sum is

$$


\begin{aligned}𝐿(𝑓,𝑃) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖−1}+2𝑦_{𝑗−1})Δ𝑥_{𝑖}Δ𝑦_{𝑗}\,.\end{aligned}


$$

### Example: Writing the Lower Riemann Sum for a Strictly Decreasing Function

#### Question

Let $R = [0,1] \times [2,3]$ be a region in the $xy$-plane, and let $f(x,y) = 10-x^2-y^2.$ Further, let $P$ be a partition of $R,$ where

$$


\begin{aligned}𝑃_{1}={𝑥_{0},𝑥_{1},…,𝑥_{𝑚}},\,𝑃_{2}={𝑦_{0},𝑦_{1},…,𝑦_{𝑛}},\,𝑃=𝑃_{1}×𝑃_{2}.\end{aligned}


$$

Write down the lower Riemann sum $L(f, P).$

#### Explanation

The lower Riemann sum is given by

$$


\begin{aligned}𝐿(𝑓,𝑃) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑚_{𝑖𝑗}Δ𝑥_{𝑖}Δ𝑦_{𝑗}\end{aligned}


$$

where $m_{ij}$ is the ** value of $f$ in each subregion $R_{ij}.$

We consider an arbitrary subregion $R_{ij}$ of the partition. This subregion lies between $x_{i-1}$ and $x_i$ over the $x$-axis and $y_{i-1}$ and $y_i$ over the $y$-axis, as shown below.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/c290ce4baa09f5fc.png)

Notice that

- $f(x,y) =10-x^2-y^2$ decreases as $x$ increases on $[0,1]$, and

- $f(x,y) = 10-x^2-y^2$ decreases as $y$ increases on $[2,3].$

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/f20d2a35effe4352.png)

As a result, the ** value of $f$ in each subregion is attained when we have the ** possible $x$ and the ** possible $y.$ This is the value at the ** of each subregion.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/4527722faad0f641.png)

Therefore,

$$


\begin{aligned}𝑚_{𝑖𝑗} & =𝑓(𝑥_{𝑖},𝑦_{𝑗})=10−𝑥_{2𝑖}−𝑦_{2𝑗}.\end{aligned}


$$

for all $1\leq i\leq m$ and $1\leq j\leq n.$

Finally, the lower Riemann sum is

$$


\begin{aligned}𝐿(𝑓,𝑃) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}(10−𝑥_{2𝑖}−𝑦_{2𝑗})Δ𝑥_{𝑖}Δ𝑦_{𝑗}.\end{aligned}


$$

### Example: Writing the Lower Riemann Sum for a Function That's Neither Strictly Increasing Nor Decreasing

#### Question

Let $R = [2,3] \times [1,2]$ be a region in the $xy$-plane, and let $f(x,y) = x - y + 3.$ Further, let $P$ be a partition of $R,$ where

$$


\begin{aligned}𝑃_{1}={𝑥_{0},𝑥_{1},…,𝑥_{𝑚}},\,𝑃_{2}={𝑦_{0},𝑦_{1},…,𝑦_{𝑛}},\,𝑃=𝑃_{1}×𝑃_{2}.\end{aligned}


$$

Write down the lower Riemann sum $L(f, P).$

#### Explanation

The lower Riemann sum is given by

$$


\begin{aligned}𝐿(𝑓,𝑃) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑚_{𝑖𝑗}Δ𝑥_{𝑖}Δ𝑦_{𝑗}\end{aligned}


$$

where $m_{ij}$ is the ** value of $f$ in each subregion $R_{ij}.$

We consider an arbitrary subregion $R_{ij}$ of the partition. This subregion lies between $x_{i-1}$ and $x_i$ over the $x$-axis and $y_{i-1}$ and $y_i$ over the $y$-axis, as shown below.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/bdfb77cbc1a02308.png)

Notice that

- $f(x,y) = x - y + 3$ increases as $x$ increases, and

- $f(x,y) = x - y + 3$ decreases as $y$ increases.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/910ad2009aadcb60.png)

As a result, the ** value of $f$ in each subregion is attained when we have the ** possible $x$ and the ** possible $y.$ This is the value at the ** of each subregion.

![Instructional graphic](../../../lesson-assets/multivariable-calculus/topic-2615/8963a63436246d73.png)

Therefore,

$$


\begin{aligned}𝑚_{𝑖𝑗} & =𝑓(𝑥_{𝑖−1},𝑦_{𝑗})=𝑥_{𝑖−1}−𝑦_{𝑗}+3\end{aligned}


$$

for all $1 \leq i \leq m$ and $1 \leq j \leq n.$

Finally, the lower Riemann sum is

$$


\begin{aligned}𝐿_{(}𝑓,𝑃) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}(𝑥_{𝑖−1}−𝑦_{𝑗}+3)Δ𝑥_{𝑖}Δ𝑦_{𝑗}.\end{aligned}


$$
