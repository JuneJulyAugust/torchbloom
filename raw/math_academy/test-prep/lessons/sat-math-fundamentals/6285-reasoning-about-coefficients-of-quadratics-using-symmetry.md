# Reasoning About Coefficients of Quadratics Using Symmetry

Source: https://www.mathacademy.com/topics/6285?courseId=120
Topic ID: 6285

## Prerequisites

- [The Vertex Form of a Parabola](../../../high-school/traditional/lessons/algebra-i/814-the-vertex-form-of-a-parabola.md)
- [The Average of the Roots Formula](../../../high-school/traditional/lessons/algebra-i/1451-the-average-of-the-roots-formula.md)
- [Equating Polynomial Coefficients](../../../high-school/traditional/lessons/algebra-i/6092-equating-polynomial-coefficients.md)

## Lesson

### Introduction

In this lesson, we’ll see how the symmetry of a parabola lets us quickly determine how the properties of a parabola are affected by its parameters.

For example, consider a parabola

$$


g(x) = ax^{2} + bx + c,


$$

where $a,$ $b$ and $c$ are unknown constants. Let's find the coordinates of the parabola's vertex, given that

$$


g(-2) = g(6).


$$

First, recall that the parabola is symmetric about the vertical line passing through the vertex. Because $g(-2) = g(6)$, the vertex is midway between $x_1 = -2$ and $x_2 = 6.$

So, the $x$-coordinate of the vertex is

$$


\begin{aligned}ℎ & =\frac{𝑥_{1}+𝑥_{2}}{2} \\ & =\frac{6+(−2)}{2} \\ & =2.\end{aligned}


$$

Now, since at the vertex, $g(h) = k,$ we have

$$


\begin{aligned}𝑔(2) & =𝑘 \\ 𝑔(2) & =𝑎(2)^{2}+𝑏(2)+𝑐 \\ 𝑘 & =4𝑎+2𝑏+𝑐.\end{aligned}


$$

Therefore, the coordinates of the vertex are

$$


(h,k)=\big(2, 4a + 2b +c\big).


$$

So far, symmetry has helped us find the vertex. Next, we will use the same condition to see how the coefficients are related.

### Using Symmetry to Relate the Coefficients

So far, we have used symmetry to find the coordinates of the vertex. We can also substitute and into

Since this gives a relationship between the coefficients.

So, the condition tells us that and are not independent; they must satisfy

Now substitute into the expression for:

Therefore, the coordinates of the vertex can also be written as

So, although we began with three unknown constants, the condition shows that the coefficients must satisfy the relation

### Example: Describing the Vertex of a Parabola in Terms of Its Parameters

#### Question

Consider parabola $g(x) = ax^{2} + bx + 9,$ where $a$ and $b$ are constants. What are the coordinates of the parabola's vertex $(h, k),$ if $g(-11) = g(-1)?$

#### Explanation

First, recall that the parabola is symmetric about the vertical line passing through the vertex. Because $g(-11) = g(-1)$, the vertex is midway between $x_1 = -11$ and $x_2 = -1.$

So, the $x$-coordinate of the vertex is

$$


\begin{aligned}ℎ & =\frac{𝑥_{1}+𝑥_{2}}{2} \\ & =\frac{−11−1}{2} \\ & =−6.\end{aligned}


$$

Now, since at the vertex, $g(h) = k,$ we have

$$


\begin{aligned}𝑔(−6) & =𝑎(−6)^{2}+𝑏(−6)+9 \\ 𝑘 & =36𝑎−6𝑏+9.\end{aligned}


$$

We can go a step further and use the given information $g(-11)=g(-1)$ as follows:

$$


\begin{aligned}𝑔(−11) & =𝑔(−1) \\ 𝑎(−11)^{2}+𝑏(−11)+9 & =𝑎(−1)^{2}+𝑏(−1)+9 \\ 121𝑎−11𝑏+9 & =𝑎−𝑏+9 \\ 120𝑎−10𝑏 & =0 \\ 12𝑎−𝑏 & =0 \\ 𝑏 & =12𝑎\end{aligned}


$$

So, the condition $g(-11)=g(-1)$ tells us that $a$ and $b$ are not independent; they must satisfy $b=12a.$

Now substitute $b=12a$ into the expression for $k$:

$$


\begin{aligned}𝑘 & =36𝑎−6𝑏+9 \\ & =36𝑎−6(12𝑎)+9 \\ & =36𝑎−72𝑎+9 \\ & =9−36𝑎\end{aligned}


$$

Therefore, the coordinates of the vertex are

$$


(h,k)=\big(-6, 9-36a\big).


$$

### The x-Coordinate of the Vertex of a Quadratic Function

We have seen that the vertex of a parabola can be written as $(h,k).$ Now, let’s find a formula for the $x$-coordinate of the vertex when a quadratic is written in standard form.

Consider a quadratic function

$$


g(x)=ax^2+bx+c,


$$

where $a\neq 0.$

We can also write the same quadratic in vertex form as

$$


g(x)=a(x-h)^2+k,


$$

where $(h,k)$ is the vertex.

Now, expand the vertex form:

$$


\begin{aligned}𝑔(𝑥) & =𝑎(𝑥−ℎ)^{2}+𝑘 \\ & =𝑎(𝑥^{2}−2ℎ𝑥+ℎ^{2})+𝑘 \\ & =𝑎𝑥^{2}−2𝑎ℎ𝑥+𝑎ℎ^{2}+𝑘.\end{aligned}


$$

Comparing coefficients with

$$


g(x)=ax^2+bx+c,


$$

we see that

$$


ax^2+\underbrace{(-2ah)}_{b}x+\underbrace{(ah^2+k)}_{c}.


$$

So,

$$


-2ah=b,


$$

and therefore

$$


h=-\frac{b}{2a}.


$$

Therefore, for a quadratic function written in standard form as

$$


g(x)=ax^2+bx+c,


$$

the $x$-coordinate of the vertex is

$$


h=-\frac{b}{2a}.


$$

In the next example, we will use this formula together with symmetry to determine information about the coefficients of a quadratic function.

### Example: Identifying Possible Ranges for Parabola Coefficients

#### Question

Consider quadratic function where and are constants. The graph of in the -plane has a vertex at the point where and are constants. If and which of the following **** be true?

#### Explanation

First, recall that the parabola is symmetric about the vertical line passing through the vertex. Because the vertex is midway between and

So, the -coordinate of the vertex is

Now, for a quadratic function the -coordinate of the vertex is given by

Since we have Therefore,

Since at the vertex, we have

Substituting we get

Given that the parabola has vertex below the -axis, we have

Now, we check each statement:

- Statement I is false because does not always have to be negative. Since we could have, for example, which is positive.

- Statement II is true because so

- Statement III is false because does not always have to be positive. Since we could have, for example, which is negative.

Therefore, the correct answer is "II only."

### Example: Using Vertex Form to Determine a Sum of Parabola Coefficients

#### Question

$$


y = ax^2 + bx + c,


$$

In the $xy$-plane, a parabola has the vertex $(0, 3).$ If the equation of the parabola can be written in the standard form above, where $a, b,$ and $c$ are constants, find the sum $a + b + c$ in terms of the parameter $a.$

#### Explanation

We know the vertex is at $(h, k) = (0, 3).$ So, we can write the parabola in vertex form:

$$


\begin{aligned}𝑦 & =𝑎(𝑥−ℎ)^{2}+𝑘 \\ 𝑦 & =𝑎(𝑥−0)^{2}+3\end{aligned}


$$

Next, we simplify:

$$


\begin{aligned}𝑦 & =𝑎(𝑥−0)^{2}+3 \\ & =𝑎(𝑥^{2})+3 \\ & =𝑎𝑥^{2}+3\end{aligned}


$$

Comparing it with the given standard quadratic form, $y = ax^2 + bx + c,$ we get the following:

$$


\begin{aligned}𝑎 & =𝑎 \\ 𝑏 & =0 \\ 𝑐 & =3\end{aligned}


$$

Therefore, adding them up, we get

$$


\begin{aligned}𝑎+𝑏+𝑐 & =𝑎+0+3 \\ & =𝑎+3.\end{aligned}


$$

### Example: Identifying True Statements Regarding Parabola Coefficients

#### Question

In the $xy$-plane, a parabola has vertex $(4, -8)$ and intersects the $x$-axis at two points. If the equation of the parabola is written in the form

$$


y = ax^2 + bx + c,


$$

where $a, b,$ and $c$ are constants, which of the following could be the value of $a + b + c?$

1. $-8$

2. $-1$

3. $10$

#### Explanation

We know the vertex is at $(h, k) = (4, -8).$ So, we can write the parabola in vertex form:

$$


\begin{aligned}𝑦 & =𝑎(𝑥−ℎ)^{2}+𝑘 \\ 𝑦 & =𝑎(𝑥−4)^{2}−8\end{aligned}


$$

Next, we expand:

$$


\begin{aligned}𝑦 & =𝑎(𝑥−4)^{2}−8 \\ & =𝑎(𝑥^{2}−8𝑥+16)−8 \\ & =𝑎𝑥^{2}−8𝑎𝑥+16𝑎−8\end{aligned}


$$

Comparing it with the given standard quadratic form, $y = ax^2 + bx + c,$ we get the following:

$$


\begin{aligned}𝑎 & =𝑎 \\ 𝑏 & =−8𝑎 \\ 𝑐 & =16𝑎−8\end{aligned}


$$

Thus, adding them up, we get

$$


\begin{aligned}𝑎+𝑏+𝑐 & =𝑎+(−8𝑎)+(16𝑎−8) \\ & =9𝑎−8\end{aligned}


$$

Since the parabola intersects the $x$-axis at two points and has its vertex at $(4, -8)$ below the $x$-axis, it must open upward, meaning $a > 0.$

Now, let's go through all the options and check which ones give $a > 0{:}$

- Option I, $-8{:}$

- Option II, $-1{:}$

- Option III, $10{:}$

Therefore, the correct answer is "II and III only".
