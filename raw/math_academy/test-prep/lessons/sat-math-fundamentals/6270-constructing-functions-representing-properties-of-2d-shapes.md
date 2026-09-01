# Constructing Functions Representing Properties of 2D Shapes

Source: https://www.mathacademy.com/topics/6270?courseId=120
Topic ID: 6270

## Prerequisites

- [The Circumference of a Circle](../../../high-school/traditional/lessons/geometry/460-the-circumference-of-a-circle.md)
- [Areas of Circles](../../../high-school/traditional/lessons/geometry/1745-areas-of-circles.md)
- [The Area of an Equilateral Triangle](../../../high-school/traditional/lessons/geometry/2886-the-area-of-an-equilateral-triangle.md)

## Lesson

### Introduction

In this lesson, we'll learn how to represent geometric properties of 2D shapes using algebraic functions. This allows us to translate real-world measurements into mathematical (algebraic) models that we can analyze.

We'll begin by learning to interpret algebraic expressions representing geometric properties.

For example, suppose we are given that the area $A,$ in square centimeters, of a rectangular solar panel can be represented by the expression

$$


A = w(w + 14)


$$

where $w$ is the width, in centimeters, of the panel. What expression represents the length, in centimeters, of the panel in this expression?

The area of a rectangle is given by

$$


A = \text{width} \cdot \text{length}.


$$

Here, we have

$$


A = w \cdot (w + 14),


$$

where $w$ is the width.

$$


\begin{aligned}𝐴\,= & width & ⋅ & length \\ & ↕ & & ↕ \\ 𝐴\,= & 𝑤 & ⋅ & (𝑤+14)\end{aligned}


$$

Therefore, comparing the two expressions, we conclude that the length must be

$$


w + 14.


$$

### Example: Interpreting Expressions Representing Area or Perimeter

#### Question

$$


P = 2l + 2(l+7)


$$

The perimeter $P,$ in yards, of a rectangle can be represented by the expression shown above, where $l$ is the length, in yards, of the rectangle. What expression represents the width, in yards, of the rectangle?

#### Explanation

The perimeter of a rectangle is given by

$$


P = 2\cdot\text{length} + 2\cdot \text{width}.


$$

Here, we have

$$


P = 2\cdot l + 2\cdot (l+7)


$$

where $l$ is the length.

Therefore, comparing the two expressions, we conclude that the width must be

$$


l+7.


$$

### Example: Constructing Functions Representing Areas of Triangles and Rectangles

#### Question

A triangle has a height of $x$ inches. The length of the triangle's base is $5$ inches more than the height. What function $A$ gives the area of the triangle, in square inches, in terms of the height of the triangle?

#### Explanation

From the description, our triangle has the following measurements:

- The height is $h = x$ inches.

- The base is $b = x+5$ inches ($5$ inches more than the height).

Therefore, the area of the triangle is given by

$$


\begin{aligned}𝐴(𝑥) & =\frac{1}{2}𝑏ℎ \\ & =\frac{1}{2}⋅(𝑥+5)⋅𝑥 \\ & =\frac{1}{2}𝑥(𝑥+5).\end{aligned}


$$

### Correctly Interpreting Problem Statements

Sometimes the phrasing used in geometric descriptions can be confusing or misleading. In such cases, it's important to read the descriptions *very carefully*, write down the appropriate equations, and *rearrange them using algebra if necessary!*

Let's consider the following description:

A triangle has a height of $x$ meters, which is $2$ meters more than its base. Construct a function $A(x)$ that gives the area of the triangle, in square meters, in terms of the height of the triangle.

This question is asking us to construct a function representing the area $A$ of a triangle, which requires us to make use of the formula

$$


A = \dfrac12 bh


$$

where $b$ is the base of the triangle, and $h$ is its height. Since we need to find the area $A$ as a function of $x,$ we need to express $b$ and $h$ in terms of $x.$

From the description, our triangle has the following measurements:

- The height is $h = x$ meters.

- And here is the tricky part! Let's denote the base by $b.$ We are told that the height is $2$ meters *more* than its base, which gives Solving this equation for $b,$ we get In other words, the base of the triangle is $2$ meters *less* than its height. And, since $h = x,$ we have

Therefore, the area of the triangle is given by

$$


\begin{aligned}𝐴(𝑥) & =\frac{1}{2}𝑏ℎ \\ & =\frac{1}{2}⋅(𝑥−2)⋅𝑥 \\ & =\frac{1}{2}𝑥(𝑥−2).\end{aligned}


$$

**Watch out!** In problems like these, a common mistake would be to write the area as $\dfrac{1}{2}x(x \, {\color{red}+} \, 2).$

Let's take a look at a slightly tricker example.

### Example: Constructing Functions Representing Area: Harder Cases

#### Question

A rectangle has a length of $x$ centimeters, which is $7$ centimeters less than three times its width. Construct a function $A(x)$ that gives the area of the rectangle, in square centimeters, in terms of the length of the rectangle.

#### Explanation

From the description, our rectangle has the following measurements:

- The length is $l = x$ centimeters.

- Let's denote the width by $w.$ We are told that the length is $7$ centimeters less than three times its width: Solving for $w,$ we get

Therefore, the area of the rectangle is given by

$$


\begin{aligned}𝐴(𝑥) & =𝑤𝑙 \\ & =\frac{1}{3}(𝑥+7)⋅𝑥 \\ & =\frac{1}{3}𝑥(𝑥+7).\end{aligned}


$$

### Expressing Properties of One Shape in Terms of Another

Now, suppose that circle $X$ has a radius of $x$ yards. Circle $Y$ has a circumference that is $40\pi$ yards greater than the circumference of circle $X.$ What is the function $A(x)$ that represents the area of circle $Y,$ in square yards?

To answer this question, we need to define some variables. So, we let

- $x$ be the radius of circle $X,$ and

- $y$ be the radius of circle $Y.$

Then,

- the circumference of circle $X$ is $2\pi x,$ and

- the circumference of circle $Y$ is $2\pi y.$

We are told that the circumference of circle $Y$ is $40\pi$ yards greater than the circumference of circle $X.$ In symbols, this means that

$$


2\pi y = 2\pi x + 40\pi.


$$

Since we want to find an expression for the area of circle $Y,$ we solve this equation for $y.$ We start by dividing the equation by $2\pi{:}$

$$


\begin{aligned}2𝜋𝑦 & =2𝜋𝑥+40𝜋 \\ \frac{2𝜋𝑦}{2𝜋} & =\frac{2𝜋𝑥+40𝜋}{2𝜋} \\ \frac{2𝜋𝑦}{2𝜋} & =\frac{2𝜋𝑥}{2𝜋}+\frac{20⋅2𝜋}{2𝜋} \\ 𝑦 & =𝑥+20\end{aligned}


$$

Therefore, the function $A(x)$ that represents the area of circle $Y$ is given by

$$


\begin{aligned}𝐴(𝑥) & =𝜋𝑦^{2} \\ & =𝜋(𝑥+20)^{2}.\end{aligned}


$$

Let's see another example.

### Example: Constructing Area Functions Given Two Related Objects

#### Question

Equilateral triangle $S$ has a side length of $x$ centimeters. Equilateral triangle $T$ has a perimeter that is $15$ centimeters less than the perimeter of triangle $S.$ What is the function $A$ that represents the area of triangle $T,$ in square centimeters, where $x > 5?$

#### Explanation

Let

- $x$ be the side length of equilateral triangle $S,$ and

- $y$ be the side length of equilateral triangle $T.$

Then,

- the perimeter of triangle $S$ is $3x,$ and

- the perimeter of triangle $T$ is $3y.$

We are told that the perimeter of triangle $T$ is $15$ centimeters less than the perimeter of triangle $S.$ In symbols, this means that

$$


3y = 3x - 15.


$$

Since we want to find an expression for the area of triangle $T,$ we solve this equation for $y{:}$

$$


\begin{aligned}3𝑦 & =3𝑥−15 \\ \frac{3𝑦}{3} & =\frac{3𝑥−15}{3} \\ 𝑦 & =𝑥−5\end{aligned}


$$

Therefore, the function $A$ that represents the area of triangle $T$ is given by

$$


\begin{aligned}𝐴(𝑥) & =\frac{\sqrt{3}}{4}𝑦^{2} \\ & =\frac{\sqrt{3}}{4}(𝑥−5)^{2}.\end{aligned}


$$
