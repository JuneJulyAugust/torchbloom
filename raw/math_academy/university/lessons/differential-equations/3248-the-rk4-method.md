# The RK4 Method

Source: https://www.mathacademy.com/topics/3248?courseId=61
Topic ID: 3248

## Prerequisites

- [Euler's Method: Calculating Multiple Steps](./3668-euler-s-method-calculating-multiple-steps.md)

## Lesson

### Introduction

For a first-order initial value problem, Euler's method approximates the increment in $y$ over a step by using a single slope - the slope at the current point.

This is simple and works well when the slope stays nearly constant across a step, but can become inaccurate when the slope changes noticeably between successive $x$-values.

The Runge–Kutta Method improves this idea by sampling the slope at several points within the same step and combining them into a weighted average. For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the increment in $y$ using the **Runge-Kutta** (**RK4**) **Method** with step size $\Delta x$ is

$$


\Delta y = \dfrac16\left(y' + 2y'_1 + 2y'_2 + y'_3\right) \cdot \Delta x,


$$

where

- $y' = f(x,y)$ is the slope at the initial point $(x,y),$

- $y'_1 = f(x_1,y_1)$ is the estimated slope at $(x_1,y_1) = \left(x + \dfrac12 \Delta x,\: y + \dfrac12 y' \cdot \Delta x\right)\!,$

- $y'_2 = f(x_2,y_2)$ is the estimated slope at $(x_2,y_2) = \left(x + \dfrac12 \Delta x,\: y + \dfrac12 y'_1 \cdot \Delta x\right)\!,$

- $y'_3 = f(x_3, y_3)$ is the estimated slope at $(x_3,y_3) = (x + \Delta x,\: y + y'_2 \cdot \Delta x).$

Instead of assuming the initial slope represents the entire interval, we take additional “in-between” slope estimates at the midpoint of the step and near its end. This provides a much better estimate of the overall increment in $y$ during the step, while still using only evaluations of $f(x,y).$

We'll see an example of how to implement the RK4 method soon, but first, let's make sure we know at which points the slope is evaluated in the next example.

Important note: Many texts denote the four intermediate values by $k_1, k_2, k_3, k_4,$ sometimes scaling each by $\Delta x,$ but the underlying idea is the same.

### Example: Identifying the Runge-Kutta Method

#### Question

Suppose we wish to solve the initial value problem

$$


y' = f(x,y), \qquad y(a) =c,


$$

and we take a step of size $\Delta x$ using the Runge-Kutta (RK4) method. Fill in the blanks to complete the weighted-average formula for the increment and the stage definitions, starting at the point $(x,y).$

$$


\begin{aligned}Δ𝑦 & =\frac{1}{6}(𝑦^{′}+2𝑦_{′1}^{}+2𝑦_{′2}^{}+𝑦_{′3}^{})⋅Δ𝑥 \\ 𝑦^{′} & =𝑓(𝑥,𝑦) \\ 𝑦_{′1}^{} & =𝑓(𝑥_{1},𝑦_{1})\, where \,(𝑥_{1},𝑦_{1})=(\phantom{(q_0,1,L)},\,𝑦+\frac{1}{2}𝑦^{′}⋅Δ𝑥) \\ 𝑦_{′2}^{} & =𝑓(𝑥_{2},𝑦_{2})\, where \,(𝑥_{2},𝑦_{2})=(𝑥+\frac{1}{2}Δ𝑥,\,\phantom{(q_0,1,L)}) \\ 𝑦_{′3}^{} & =𝑓(𝑥_{3},𝑦_{3})\, where \,(𝑥_{3},𝑦_{3})=(\phantom{(q_0,1,L)},\,𝑦+𝑦_{′2}^{}⋅Δ𝑥)\end{aligned}


$$

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the increment in $y$ using the Runge-Kutta (RK4) method with step size $\Delta x$ is computed as the weighted average of four sample slopes:

$$


\Delta y = \dfrac16 \left(y' + 2y'_1 + 2y'_2 + y'_3\right) \cdot \Delta x,


$$

where

- $y' = f(x,y)$ is the estimated slope at the point $(x,y),$

- $y'_1 = f(x_1, y_1)$ is the estimated slope at $𝑥+\frac{1}{2}Δ𝑥$

- $y'_2 = f(x_2, y_2)$ is the estimated slope at $𝑦+\frac{1}{2}𝑦_{′1}^{}⋅Δ𝑥$

- $y'_3 = f(x_3, y_3)$ is the estimated slope at $𝑥+Δ𝑥$

### A Worked Example

Consider the following initial value problem:

$$


y' = 3x - 2y + 5, \qquad y(0) = 1


$$

Our goal is to approximate $y(1)$ using the Runge-Kutta (RK4) method.

Since we know $y(0)$ and wish to estimate $y(1),$ we will use a step size of

$$


\Delta x = 1 - 0 = 1.


$$

Let's use a table to keep track of all important values, including the intermediate slopes. We start by adding the initial condition data $y(0)=1.$

Now let's find the required values.

- First, we compute the value of $y'$ according to the given rule: So, we add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $1$ $3$

- The first intermediate point is So, the first intermediate slope is We can add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $1$ $3$ $\dfrac32$

- The second intermediate point is So, the second intermediate slope is We add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $1$ $3$ $\dfrac32$ $3$

- The third intermediate point is So, the third intermediate slope is We can add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $1$ $3$ $\dfrac32$ $3$ $0$

Finally, we compute $\Delta y$ using the Runge-Kutta Method:

$$


\begin{aligned}Δ𝑦 & =\frac{1}{6}(𝑦^{′}+2𝑦_{′1}^{}+2𝑦_{′2}^{}+𝑦_{′3}^{})⋅Δ𝑥 \\ & =\frac{1}{6}(3+2⋅\frac{3}{2}+2⋅3+0)⋅1 \\ & =\frac{1}{6}⋅12 \\ & =2.\end{aligned}


$$

Therefore, the completed first row is as given below.

To get the values of $x$ and $y$ in the *next* row, we add $\Delta x$ to $x$ and $\Delta y$ to $y,$ as follows:

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥 \\ & =0+1 \\ & =1 \\ 𝑦_{new} & =𝑦+Δ𝑦 \\ & =1+2 \\ & =3\end{aligned}


$$

Adding these rows to our table gives the following:

Looking at the two leftmost columns, we conclude that $y(1) \approx 3.$

### Example: Calculating a Y-Increment Given All Intermediate Values

#### Question

Consider the following initial value problem:

$$


y' = xy + x, \qquad y(0) = 1


$$

We wish to approximate the solution using the Runge-Kutta (RK4) Method. Complete the first row of the table below, given that the step size is $\Delta x = 1.$

Use the table above to approximate the value of $y(1).$

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c


$$

the increment in $y$ using the Runge-Kutta (RK4) method with step size $\Delta x$ is computed as the weighted average of four sample slopes:

$$


\Delta y = \dfrac16(y' + 2y'_1 + 2y'_2 + y'_3) \cdot \Delta x,


$$

where

- $y' = f(x,y)$ is the estimated slope at the initial point $(x,y),$

- $y'_1 = f(x_1, y_1)$ is the estimated slope at $(x_1, y_1) = \left(x + \dfrac12\Delta x,\: y + \dfrac12y' \cdot \Delta x \right),$

- $y'_2 = f(x_2, y_2)$ is the estimated slope at $(x_2, y_2) = \left(x + \dfrac12\Delta x,\: y + \dfrac12y'_1 \cdot \Delta x \right),$

- $y'_3 = f(x_3, y_3)$ is the estimated slope at $(x_3, y_3) = (x + \Delta x,\: y + y'_2 \cdot \Delta x).$

All four sample slopes are already computed. So, we just need to find the increment on $y.$

We compute $\Delta y$ using the Runge-Kutta method:

$$


\begin{aligned}Δ𝑦 & =\frac{1}{6}(𝑦^{′}+2𝑦_{′1}^{}+2𝑦_{′2}^{}+𝑦_{′3}^{})⋅Δ𝑥 \\ & =\frac{1}{6}(0+2⋅1+2⋅\frac{5}{4}+\frac{13}{4})⋅1 \\ & =\frac{1}{6}(2+\frac{10}{4}+\frac{13}{4}) \\ & =\frac{1}{6}⋅\frac{31}{4} \\ & =\frac{31}{24}.\end{aligned}


$$

Therefore, the completed first row is as given below.

To get the values of $x$ and $y$ in the ** row, we add $\Delta x$ to $x$ and $\Delta y$ to $y,$ as follows:

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥 \\ & =0+1 \\ & =1 \\ 𝑦_{new} & =𝑦+Δ𝑦 \\ & =1+\frac{31}{24} \\ & =\frac{55}{24}\end{aligned}


$$

Adding these rows to our table gives the following:

Finally, we have

$$


\begin{aligned}𝑦(1)≈\frac{55}{24}.\end{aligned}


$$

### Example: Calculating a Y-Increment Given Some Intermediate Values

#### Question

Consider the following initial value problem:

$$


y' = x - y, \qquad y(0) = 1


$$

We wish to approximate the solution using the Runge-Kutta (RK4) method. Complete the first row of the table below, given that the step size is $\Delta x = 1.$

Use the table above to approximate the value of $y(1).$

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c


$$

the increment in $y$ using the Runge-Kutta (RK4) method with step size $\Delta x$ is computed as the weighted average of four sample slopes:

$$


\Delta y = \dfrac16(y' + 2y'_1 + 2y'_2 + y'_3) \cdot \Delta x,


$$

where

- $y' = f(x,y)$ is the estimated slope at the initial point $(x,y),$

- $y'_1 = f(x_1, y_1)$ is the estimated slope at $(x_1, y_1) = \left(x + \dfrac12\Delta x,\: y + \dfrac12y' \cdot \Delta x \right),$

- $y'_2 = f(x_2, y_2)$ is the estimated slope at $(x_2, y_2) = \left(x + \dfrac12\Delta x,\: y + \dfrac12y'_1 \cdot \Delta x \right),$

- $y'_3 = f(x_3, y_3)$ is the estimated slope at $(x_3, y_3) = (x + \Delta x,\: y + y'_2 \cdot \Delta x).$

The first three sample slopes, evaluated at the initial point and first intermediate points, are already computed. Now let's find the others.

- The third intermediate point is So, the third intermediate slope is We can add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $1$ $-1$ $0$ $-\dfrac12$ $\dfrac12$

Finally, we compute $\Delta y$ using the Runge-Kutta Method:

$$


\begin{aligned}Δ𝑦 & =\frac{1}{6}(𝑦^{′}+2𝑦_{′1}^{}+2𝑦_{′2}^{}+𝑦_{′3}^{})⋅Δ𝑥 \\ & =\frac{1}{6}(−1+2⋅0+2⋅(−\frac{1}{2})+\frac{1}{2})⋅1 \\ & =\frac{1}{6}(−\frac{3}{2}) \\ & =−\frac{1}{4}.\end{aligned}


$$

Therefore, the completed first row is as given below.

To get the values of $x$ and $y$ in the ** row, we add $\Delta x$ to $x$ and $\Delta y$ to $y,$ as follows:

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥 \\ & =0+1 \\ & =1 \\ 𝑦_{new} & =𝑦+Δ𝑦 \\ & =1+(−\frac{1}{4}) \\ & =\frac{3}{4}.\end{aligned}


$$

Adding these rows to our table gives the following:

Finally, we have

$$


\begin{aligned}𝑦(1)≈\frac{3}{4}.\end{aligned}


$$

### Example: Approximating the Solution to an Initial Value Problem Using RK4

#### Question

Consider the following initial value problem:

$$


y' = 2x(2y+1), \qquad y(0) = 0


$$

Use the Runge-Kutta (RK4) method with one step to approximate $y\!\left(\dfrac12\right).$

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the increment in $y$ using the Runge-Kutta Method with step size $\Delta x$ is computed as the weighted average of four sample slopes:

$$


\Delta y = \dfrac16\left(y' + 2y'_1 + 2y'_2 + y'_3\right) \cdot \Delta x,


$$

where

- $y' = f(x,y)$ is the slope at the initial point $(x,y),$

- $y'_1 = f(x_1,y_1)$ is the slope at $(x_1,y_1) = \left(x + \dfrac12 \Delta x,\: y + \dfrac12 y' \cdot \Delta x\right),$

- $y'_2 = f(x_2,y_2)$ is the slope at $(x_2,y_2) = \left(x + \dfrac12 \Delta x,\: y + \dfrac12 y'_1 \cdot \Delta x\right),$

- $y'_3 = f(x_3, y_3)$ is the slope at $(x_3,y_3) = (x + \Delta x,\: y + y'_2 \cdot \Delta x).$

Since we want to find the value of $y$ at $x=\dfrac12,$ starting from $x=0,$ we will use a step size of

$$


\Delta x = \dfrac12 - 0 = \dfrac12.


$$

First, we create a table and add the initial condition data.

Now let's find the required values.

- First, we compute the value of $y'$ according to the given rule: So, we add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $0$ $0$

- The first intermediate point is So, the first intermediate slope is We can add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $0$ $0$ $\dfrac12$

- The second intermediate point is So, the second intermediate slope is We add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $0$ $0$ $\dfrac12$ $\dfrac58$

- The third intermediate point is So, the third intermediate slope is We can add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $0$ $0$ $\dfrac12$ $\dfrac58$ $\dfrac{13}8$

- Finally, we compute $\Delta y$ using the Runge-Kutta Method: We add this to our table. $\,x\,$ $\,y\,$ $\,y'\,$ $\,y'_1\,$ $\,y'_2\,$ $\,y'_3\,$ $\Delta y$ $0$ $0$ $0$ $\dfrac12$ $\dfrac58$ $\dfrac{13}8$ $\dfrac{31}{96}$

To get the values of $x$ and $y$ in the ** row, we add $\Delta x$ to $x$ and $\Delta y$ to $y,$ as follows:

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥 \\ & =0+\frac{1}{2} \\ & =\frac{1}{2} \\ 𝑦_{new} & =𝑦+Δ𝑦 \\ & =0+\frac{31}{96} \\ & =\frac{31}{96}.\end{aligned}


$$

Adding these rows to our table gives the following:

Therefore, we conclude that $y\!\left(\dfrac12\right) \approx \dfrac{31}{96}.$

### A Graphical Explanation of the RK4 Method

Let's go back to our previous initial value problem:

$$


y' = 3x-2y+5, \qquad y(0)=1


$$

Carrying out the Runge-Kutta method resulted in the following table.

We can view each step of our approximation in the coordinate plane as follows:

- The first intermediate point $(x_1, y_1) = \left(\dfrac12, \dfrac52\right)$ is found using the slope of the initial point $y'=3.$

- The second intermediate point $(x_2, y_2) = \left(\dfrac12, \dfrac74\right)$ is found using the slope of the previous intermediate point $y'_1=\dfrac32.$

- The third intermediate point $(x_3, y_3) = (1,4)$ is found using the slope of the previous intermediate point $y'_2=3.$

- Finally, we compute the increment in $y$ by taking a weighted average of the four sample slopes.
