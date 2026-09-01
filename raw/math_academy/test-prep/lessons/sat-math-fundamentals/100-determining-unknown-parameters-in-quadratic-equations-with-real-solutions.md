# Determining Unknown Parameters in Quadratic Equations With Real Solutions

Source: https://www.mathacademy.com/topics/100?courseId=120
Topic ID: 100

## Prerequisites

- [Solving Elementary Quadratic Inequalities](../../../high-school/traditional/lessons/precalculus/1495-solving-elementary-quadratic-inequalities.md)
- [Determining Unknown Parameters in Quadratic Equations With One Real Solution](../../../high-school/traditional/lessons/algebra-i/6266-determining-unknown-parameters-in-quadratic-equations-with-one-real-solution.md)

## Lesson

### Introduction

Recall that for a quadratic equation

$$


ax^2 + bx + c = 0,


$$

with $a\neq 0,$ the discriminant is defined as

$$


\mathcal{D} = b^2 - 4ac.


$$

The discriminant tells us about the nature of the equation's solutions:

- If $\mathcal{D} > 0,$ we have *two distinct real solutions*.

- If $\mathcal{D} = 0,$ we have *one repeated real solution* (sometimes called a “double root”).

- If $\mathcal{D} < 0,$ we have *no real solutions.*

Combining the first two conditions, we can say that a quadratic equation *has real solutions* if the discriminant is *non-negative*:

$$


\mathcal{D} \geq 0


$$

If a quadratic equation contains an unknown parameter and we know the equation has real solutions, we can use the condition $\mathcal D \geq 0$ to place conditions on the unknown parameter.

To demonstrate, let's consider the equation

$$


x^2 - 2x + k = 0,


$$

where $k$ is a real parameter. We want to determine *all* the values of $k$ for which the equation has real solutions.

To compute the discriminant, we first note that the coefficients are

$$


a = 1, \qquad b = -2, \qquad c = k.


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−2)^{2}−4(1)(𝑘) \\ & =4−4𝑘.\end{aligned}


$$

To have real solutions, we need $\mathcal{D} \geq 0.$ This gives the inequality

$$


4 - 4k \geq 0.


$$

Solving this inequality for the variable $k,$ we get the following:

$$


\begin{aligned}4−4𝑘 & ≥0 \\ 4 & ≥4𝑘 \\ 4𝑘 & ≤4 \\ 𝑘 & ≤\frac{4}{4}=1\end{aligned}


$$

Therefore, our solution is

$$


k\leq 1


$$

We can also express this solution using interval notation:

$$


k \in (-\infty, 1 ]


$$

Any value of $k$ in this interval will give a quadratic equation with real solutions.

Sometimes, these kinds of problems involve solving a simple quadratic inequality. Let's see an example.

### Example: Determining Ranges of Parameter Values in Quadratic Equations With Real Solutions

#### Question

For which values of $k$ does the equation $3z^2 - 6kz + 12 = 0$ have real solutions?

#### Explanation

A quadratic equation has real solutions if it has two distinct real solutions ($\mathcal{D}>0$) or one distinct real solution ($\mathcal{D}=0$). Putting these conditions together, we must have $\mathcal{D} \geq 0.$

To compute the discriminant, first note the following coefficients: $a=3,$ $b=-6k,$ and $c=12.$ So, we require

$$


\begin{aligned}D & ≥0 \\ 𝑏^{2}−4𝑎𝑐 & ≥0 \\ (−6𝑘)^{2}−4(3)(12) & ≥0 \\ 36𝑘^{2}−144 & ≥0 \\ 36𝑘^{2} & ≥144 \\ 𝑘^{2} & ≥4 \\ \sqrt{𝑘^{2}} & ≥\sqrt{4} \\ |𝑘| & ≥2.\end{aligned}


$$

If $|k| \geq 2,$ then $k \leq -2$ or $k \geq 2.$ Using interval notation, then, our solution is

$$


k \in (-\infty,-2] \cup [2, \infty).


$$

### Example: Determining Extreme Parameter Values in Quadratic Equations With Real Solutions

#### Question

Given that $x(5x - k) = -10,$ where $k$ is a **** constant, has real solutions, what is the least possible value of $k?$

#### Explanation

A quadratic equation has real solutions if the discriminant is non-negative: $\mathcal{D} \geq 0.$

First, rewrite the equation in standard quadratic form:

$$


\begin{aligned}𝑥(5𝑥−𝑘) & =−10 \\ 5𝑥^{2}−𝑘𝑥 & =−10 \\ 5𝑥^{2}−𝑘𝑥+10 & =0\end{aligned}


$$

The coefficients of our quadratic equation are the following:

$$


a = 5, \qquad b = -k, \qquad c = 10


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−𝑘)^{2}−4(5)(10) \\ & =𝑘^{2}−200.\end{aligned}


$$

To have real solutions, we need $\mathcal{D} \geq 0{:}$

$$


\begin{aligned}𝑘^{2}−200 & ≥0 \\ 𝑘^{2} & ≥200 \\ 𝑘 & ≥\sqrt{200}\end{aligned}


$$

Since $k$ must be positive, we conclude that the least possible value is $10\sqrt{2}.$

### Determining Unknown Coefficients in Quadratic Equations With Distinct Real Solutions

For a quadratic equation $ax^2+bx+c=0,$ the discriminant $\mathcal{D} = b^2 - 4ac$ tells us about the equation's solutions:

- If $\mathcal{D} > 0,$ there are *two distinct real solutions.*

- If $\mathcal{D} = 0,$ there is *one distinct real solution.*

- If $\mathcal{D} < 0,$ there are *no real solutions.*

If we are given a quadratic equation with an unknown parameter, then we can use the criterion $D > 0$ to determine the values of the unknown parameter such that the quadratic equation has two *distinct* real solutions.

For example, suppose we have the quadratic equation

$$


x^2+kx+9=0.


$$

Let's find all the values of $k$ such that this equation has two distinct real solutions.

A quadratic equation has two distinct real solutions if its discriminant is positive: $\mathcal{D}>0.$ To compute the discriminant, we first note that the coefficients of the equation are

$$


a=1,\quad b=k,\quad c=9.


$$

So, we require

$$


\begin{aligned}D & >0 \\ 𝑏^{2}−4𝑎𝑐 & >0 \\ (𝑘)^{2}−4(1)(9) & >0 \\ 𝑘^{2}−36 & >0.\end{aligned}


$$

Solving this inequality for the variable $k,$ we get the following:

$$


\begin{aligned}𝑘^{2} & >36 \\ \sqrt{𝑘^{2}} & >\sqrt{36} \\ |𝑘| & >6\end{aligned}


$$

Therefore, the solutions are

$$


k > 6\quad\text{or}\quad k < -6.


$$

Using interval notation, we can write our solution as

$$


k \in (-\infty,-6) \cup (6,\infty).


$$

Any value of $k$ inside this interval will give a quadratic equation with *distinct* real solutions.

### Interpreting Extreme Values

Let's consider our quadratic equation once more:

$$


x^2+kx+9=0


$$

Earlier, we saw that this equation has *distinct* real solutions for all values of $k$ in the interval

$$


k \in (-\infty,-6) \cup (6,\infty).


$$

Note the following:

- The values $k=-6$ and $k=6$ are *not* included in the solution! While these values give real solutions, they are *not* distinct! For example, if we substitute $k=6$ into the equation, we get and this can be factored as Thus, $k=6$ corresponds to the "double solutions" case, where the solutions are real but *not distinct*! The same is true for $k=-6.$

- Suppose we wanted the *smallest positive integer* value of $k$ such that the equation has distinct solutions. All the positive values of $k$ lie in the interval $(6,\infty),$ and the smallest positive integer in this interval is $k=7.$

- Similarly, suppose we wanted the *largest negative integer* value of $k$ such that the equation has distinct solutions. All the negative values of $k$ lie in the interval $(-\infty,-6),$ and the largest negative integer in this interval is $k=-7.$

Let's see some more examples.

### Example: Determining Ranges of Parameter Values in Quadratic Equations With Distinct Real Solutions

#### Question

Given that $3kx^2+12x+k=0,$ where $k$ is a non-zero real number, find the values of $k$ for which the equation has two distinct real solutions.

#### Explanation

A quadratic equation has two distinct real solutions if its discriminant is positive: $\mathcal{D}>0.$

To compute the discriminant, note the following coefficients: $a=3k,$ $b=12,$ and $c=k.$

So, we require

$$


\begin{aligned}D & >0 \\ 𝑏^{2}−4𝑎𝑐 & >0 \\ (12)^{2}−4(3𝑘)(𝑘) & >0 \\ 144−12𝑘^{2} & >0 \\ 144 & >12𝑘^{2} \\ 12𝑘^{2} & <144 \\ 𝑘^{2} & <12 \\ \sqrt{𝑘^{2}} & <\sqrt{12} \\ |𝑘| & <2\sqrt{3}.\end{aligned}


$$

If $|k| < 2\sqrt{3},$ then $-2\sqrt{3} < k < 2\sqrt{3}.$ Using interval notation, then, our solution is $(-2\sqrt{3},2\sqrt{3}).$

Finally, taking into account that $k\neq 0,$ we have $k\in(-2\sqrt{3}, 0) \cup (0,2\sqrt{3}).$

### Example: Determining Extreme Parameter Values in Quadratic Equations With Distinct Real Solutions

#### Question

Given that $x(kx + 10) = -5,$ where $k$ is a **** constant, has two distinct real solutions, what is the greatest possible value of $k?$

#### Explanation

A quadratic equation has two distinct real solutions if the discriminant is positive: $\mathcal{D} > 0.$

First, we rewrite the equation in standard quadratic form:

$$


\begin{aligned}𝑥(𝑘𝑥+10) & =−5 \\ 𝑘𝑥^{2}+10𝑥 & =−5 \\ 𝑘𝑥^{2}+10𝑥+5 & =0\end{aligned}


$$

The coefficients of our quadratic equation are the following:

$$


a = k, \qquad b = 10, \qquad c = 5


$$

So, computing the discriminant, we get

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(10)^{2}−4(𝑘)(5) \\ & =100−20𝑘.\end{aligned}


$$

To have distinct real solutions, we need $\mathcal{D} > 0{:}$

$$


\begin{aligned}100−20𝑘 & >0 \\ 100 & >20𝑘 \\ 20𝑘 & <100 \\ 𝑘 & <\frac{100}{20} \\ 𝑘 & <5\end{aligned}


$$

Since $k$ must be positive and an integer, we conclude that the greatest possible value is $k=4.$
