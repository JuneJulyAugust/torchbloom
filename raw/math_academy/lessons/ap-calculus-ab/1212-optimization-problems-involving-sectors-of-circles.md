# Optimization Problems Involving Sectors of Circles

Source: https://www.mathacademy.com/topics/1212?courseId=24
Topic ID: 1212

## Prerequisites

- [Solving Optimization Problems Using Derivatives](./1211-solving-optimization-problems-using-derivatives.md)
- [Calculating Areas of Sectors Using Radians](../geometry/1606-calculating-areas-of-sectors-using-radians.md)

## Lesson

### Introduction

We can use differentiation to solve problems involving sectors of circles, such as finding the maximum area of the sector of a circle given a fixed perimeter. Let's remind ourselves of the general strategy for optimization problems.

1. Draw a diagram of the situation, introducing variables where necessary.

2. Write down the equation of the quantity that you're trying to maximize or minimize. This is called the **objective function**, and it might include more than one variable.

3. Write down the constraint equation.

4. Use the constraint equation to write the objective function in terms of a single variable only.

5. Differentiate the objective function, set it equal to zero, and solve for the stationary points.

6. Test each stationary point using the second derivative test. Or you can use the first derivative test if it's easier.

### Example: Maximizing the Area of a Circular Sector With a Fixed Perimeter

#### Question

Suppose that we have a string of length $20$ inches and that we shape it to make a circular sector, as shown in the diagram below. Among all of the circular sectors that can be made with that string, what's the radius of the one that gives the largest area?

![Instructional graphic](../../lesson-assets/ap-calculus-ab/topic-1212/351ef202eb5ebd95.png)

#### Explanation

First, let $r$ stand for the circular sector's radius and let $\theta$ be the angle (in radians) subtended by it. We want to maximize the area

$$


A = \dfrac{1}{2}r^2\theta.


$$

We know that the perimeter of our sector is fixed at $20$ inches in length, so we also have the constraint condition

$$


20=2r + r\theta,


$$

where we recall that $s=r\theta$ gives the arc-length $s$ of a circular sector of radius $r$ and central angle $\theta,$ where $\theta$ is in radians.

Now, by making $\theta$ the subject of the constraint equation, we find that

$$


\theta = \dfrac{20-2r}{r} = \dfrac{20}{r} -2.


$$

Plugging the above into our expression for $A,$ we obtain

$$


\begin{aligned} A(r) &= \dfrac{1}{2}r^2\left(\dfrac{20}{r} -2\right)\\[3pt] &= 10r -r^2.\end{aligned}


$$

We want to maximize $A,$ so we need to differentiate $A$ and set the derivative equal to zero. The derivative is

$$


A'(r) = 10 -2r.


$$

Setting $A'(r) = 0$ and solving for $r$ gives

$$


\begin{aligned}𝐴^{′}(𝑟) & =0 \\ 10−2𝑟 & =0 \\ 𝑟 & =5.\end{aligned}


$$

Finally, we confirm that $r=5$ is a maximum using the second derivative test. The second derivative is

$$


A''(r) = -2 \quad \Longrightarrow \quad A''(5) = -2 < 0.


$$

Since $A''(5)$ is negative, we conclude that $r=5$ is indeed a maximum of $A(r).$

Therefore, the circular sector of the greatest area will have a radius of $5\,\textrm{in},$ and the maximum area is given by

$$


A(5) = 10(5) - 5^2 = 25\,\textrm{in}^2.


$$

### Example: Minimizing the Perimeter of a Circular Sector With a Fixed Area

#### Question

Consider all circular sectors $MON$ with area $A=8$ square units. What is the angle $\theta$ of the circular sector that has the smallest possible perimeter?

![Instructional graphic](../../lesson-assets/ap-calculus-ab/topic-1212/0c741eabe02091bf.png)

#### Explanation

We let $r$ be the radius of the circular sector and let $\theta$ be the angle (in radians) subtended by it. Then, we want to minimize the perimeter

$$


P= 2r + r\theta.


$$

We know that the area is fixed at $8$ square units, so we also have the constraint condition

$$


8 = \frac{1}{2}r^2\theta.


$$

Now, by making $\theta$ the subject of the constraint equation, we find that

$$


\begin{aligned} 8 &= \frac{1}{2}r^2\theta\\[3pt] \theta &= \dfrac{16}{r^2}. \end{aligned}


$$

Plugging this value into our expression for $P,$ we obtain

$$


\begin{aligned}𝑃 & =2𝑟+𝑟𝜃 \\ & =2𝑟+𝑟⋅\frac{16}{𝑟^{2}} \\ & =2𝑟+\frac{16}{𝑟}.\end{aligned}


$$

We want to minimize $P,$ so we need to differentiate $P$ and set the derivative equal to zero. The derivative is

$$


P'(r) = 2 - \dfrac{16}{r^2}.


$$

Setting the derivative equal to zero and solving for $r$ gives

$$


\begin{aligned}2−\frac{16}{𝑟^{2}} & =0 \\ 2𝑟^{2} & =16 \\ 𝑟^{2} & =8 \\ 𝑟 & =2\sqrt{√2}.\end{aligned}


$$

Finally, we confirm that $r=2\sqrt{2}$ is a minimum using the second derivative test.

Since the second derivative $P''(r) = \dfrac{32}{r^3} > 0$, the stationary point $r=2\sqrt{2}$ is a minimum.

Finally, when $r=2\sqrt{2}$, we have

$$


\begin{aligned}𝜃 & =\frac{16}{𝑟^{2}} \\ & =\frac{16}{(2\sqrt{√2})^{2}} \\ & =2.\end{aligned}


$$

Finally, we conclude that the angle $\theta = 2$ radians minimizes the perimeter of the circular sector $MON.$
