# Fitting Quadratic Functions to Data Using Vertex Form

Source: https://www.mathacademy.com/topics/6296?courseId=120
Topic ID: 6296

## Prerequisites

- [The Average of the Roots Formula](../algebra-i/1451-the-average-of-the-roots-formula.md)
- [Writing the Equation of a Parabola in Vertex Form](../algebra-i/3546-writing-the-equation-of-a-parabola-in-vertex-form.md)

## Lesson

### Introduction

We can model quadratic functions using vertex form if we know the coordinates of the vertex and one additional point on the graph. This approach gives us a straightforward procedure for fitting a quadratic curve to a data set.

Recall that the vertex form of a quadratic function $y = f(x)$ is given by

$$


f(x) = a(x-h)^2 + k,


$$

where $(h,k)$ are the coordinates the vertex, and $a$ is a constant.

For example, suppose the graph of a quadratic function $f$ has the vertex at $(3,-3).$ Then, we can immediately express it in vertex form as

$$


f(x) = a(x-3)^2 - 3.


$$

Notice that we don't know the value of the constant $a.$ However, we can find this using some additional information about the curve.

Suppose we know that the graph passes through the point $(1,-1).$ To find the value of $a,$ we substitute this into the equation and solve:

$$


\begin{aligned}𝑓(𝑥) & =𝑎(𝑥−3)^{2}−3 \\ 𝑓(1) & =𝑎(1−3)^{2}−3 \\ −1 & =𝑎(−2)^{2}−3 \\ −1 & =4𝑎−3 \\ 2 & =4𝑎 \\ \frac{2}{4} & =\frac{4𝑎}{4} \\ \frac{1}{2} & =𝑎 \\ 𝑎 & =\frac{1}{2}\end{aligned}


$$

Therefore, the function is

$$


f(x) = \dfrac12(x-3)^2-3.


$$

### Example: Fitting Data to a Quadratic Function

#### Question

The graph of a quadratic function $f(x)$ has the vertex at $(1,-3).$ Find the expression of the function in terms of $x$ if its graph also passes through the point $(4,-12).$

#### Explanation

The quadratic function in vertex form is given by

$$


f(x) = a(x - h)^2 + k


$$

where $(h, k)$ is the vertex of the parabola.

First, the graph of our function has the vertex at $(1, -3),$ so

$$


h = 1 \qquad\text{and}\qquad k = -3,


$$

and the function becomes

$$


f(x) = a(x-1)^2 - 3.


$$

Next, we know that the graph passes through $(4,-12).$ We substitute this into the equation and solve for the parameter $a{:}$

$$


\begin{aligned}𝑓(4) & =𝑎(4−1)^{2}−3 \\ −12 & =𝑎(3)^{2}−3 \\ −12 & =9𝑎−3 \\ −9 & =9𝑎 \\ \frac{−9}{9} & =\frac{9𝑎}{9} \\ −1 & =𝑎 \\ 𝑎 & =−1\end{aligned}


$$

Therefore, the function is

$$


f(x) = \boxed{-(x-1)^2-3}.


$$

### Example: Fitting Table Data to a Quadratic Function

#### Question

The graph of a quadratic function $y = f(x)$ passes through the points given by their $(x,y)$-coordinates in the table above. Find the expression of the function in terms of $x.$

#### Explanation

A quadratic function in vertex form is given by

$$


f(x) = a(x - h)^2 + k


$$

where $(h, k)$ is the vertex of the parabola.

Notice that the function is symmetric about $x=0$ and $x=4,$ since

$$


f(0) = f(4) = 19.


$$

Therefore, the midpoint of these two points must correspond to the vertex of the parabola $y=f(x).$ The $x$-coordinate of the midpoint is

$$


h = \dfrac{0+4}{2} = 2.


$$

Therefore, the vertex of the parabola is $(2,3),$ and the function becomes

$$


\begin{aligned}𝑓(𝑥) & =𝑎(𝑥−2)^{2}+3.\end{aligned}


$$

Next, we know that the graph passes through $(4,19).$ We substitute this into the equation and solve for the parameter $a{:}$

$$


\begin{aligned}19 & =𝑎(4−2)^{2}+3 \\ 19 & =4𝑎+3 \\ 16 & =4𝑎 \\ \frac{16}{4} & =\frac{4𝑎}{4} \\ 4 & =𝑎 \\ 𝑎 & =4\end{aligned}


$$

Therefore, the function is

$$


\begin{aligned}𝑓(𝑥) & =4(𝑥−2)^{2}+3 \\ & =4(𝑥^{2}−4𝑥+4)+3 \\ & =4𝑥^{2}−16𝑥+19.\end{aligned}


$$

### Example: Modeling Using Quadratic Functions

#### Question

The quadratic function $H$ models the height, in feet, of an arrow above the ground $t$ seconds after it was released. The function estimates that the arrow reached a maximum height of $64$ feet $2$ seconds after release and then returned to the ground $4$ seconds after release. Based on the function, what was the arrow’s estimated height, to the nearest foot, $3$ seconds after release?

#### Explanation

We model the arrow’s height with a quadratic function $H(t),$ where $t$ is the number of seconds since release and $H(t)$ gives the height in feet. Since the arrow reaches a maximum height, the function takes the vertex form

$$


H(t) = a(t - h)^2 + k


$$

where $(h, k)$ is the vertex of the parabola.

First, the arrow reached the maximum height of $64$ feet at $t=2.$ This means the vertex of the quadratic function is at $(2, 64),$ so

$$


h = 2 \qquad\text{and}\qquad k = 64.


$$

So, our function is

$$


H(t) = a(t-2)^2 + 64.


$$

Next, the arrow returned to the ground ($0$ feet) at $t=4,$ which means $H(4) = 0.$ So we set up the equation and solve for $a{:}$

$$


\begin{aligned}𝐻(𝑡) & =𝑎(𝑡−2)^{2}+64 \\ 𝐻(4) & =𝑎(4−2)^{2}+64 \\ 0 & =𝑎(2)^{2}+64 \\ 0 & =4𝑎+64 \\ −4𝑎 & =64 \\ 𝑎 & =−\frac{64}{4} \\ & =−16\end{aligned}


$$

So the height function is

$$


H(t) = -16(t - 2)^2 + 64.


$$

Therefore, the arrow’s height at $t=3$ is

$$


\begin{aligned}𝐻(3) & =−16(3−2)^{2}+64 \\ & =−16(1)^{2}+64 \\ & =−16+64 \\ & =48 feet.\end{aligned}


$$
