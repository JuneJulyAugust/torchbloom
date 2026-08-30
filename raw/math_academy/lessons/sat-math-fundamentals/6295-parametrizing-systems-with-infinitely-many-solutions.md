# Parametrizing Systems With Infinitely Many Solutions

Source: https://www.mathacademy.com/topics/6295?courseId=120
Topic ID: 6295

## Prerequisites

- [Systems of Equations With No Solutions and Infinitely Many Solutions](../algebra-i/493-systems-of-equations-with-no-solutions-and-infinitely-many-solutions.md)

## Lesson

### Introduction

When a system of linear equations has a unique solution, we can describe it as a single point $(x,y).$ This represents the point where the two lines intersect.

Now, suppose a system of linear equations has *infinitely many* solutions. Can we describe the solutions to the system in a similar way?

Indeed, we can. Since there are infinitely many solutions, the set of intersection points $(x,y)$ forms an entire line, not just a single point. So, to find an expression that represents every point of intersection, we can **parametrize** the solution, as follows:

- *Choose one variable freely*: For example, we set $x=t,$ where $t$ represents any real number.

- *Express the other variable in terms of the chosen one*: We find the corresponding $y$-coordinate for each $x$-coordinate by solving one of the equations for $y.$

- *Write the solution as an ordered pair*: Finally, we write the final result in terms of $t.$

As a result, the parametrization of the solutions will be in the form

$$


({\color{blue}{t}},{\color{red}{f(t)}}).


$$

Let's take a look at a concrete example.

### A Concrete Example

To demonstrate, consider the following system that has infinitely many solutions:

$$


\begin{aligned}4𝑥+2𝑦=10 \\ 8𝑥+4𝑦=20\end{aligned}


$$

Let's express the solutions in the form $(t,f(t)).$ First, set $x=t.$ Then, picking the first equation (it doesn't matter which) and solving for $y,$ we have

$$


\begin{aligned}4𝑥+2𝑦 & =10 \\ 2𝑦 & =10−4𝑥 \\ 𝑦 & =\frac{10−4𝑥}{2} \\ 𝑦 & =\frac{10}{2}−\frac{4𝑥}{2} \\ 𝑦 & =5−2𝑥.\end{aligned}


$$

Therefore, for any given $x$-value, the corresponding $y$-value is $y = 5-2x.$ Finally, replacing $x$ with $t,$ we can express the intersection points as

$$


\left({\color{blue}{t}},{\color{red}{5-2t}}\right),


$$

where $\color{blue}t$ is *any* number. This compact expression represents all solutions to the system, since every value of $t$ produces one solution pair.

**Note:** Mathematicians often choose letters such as $t$ and $r$ to represent the freely-varying parameter. However, since $x = t$ in this case, we could have also represented the solution using the variable $x$ instead:

$$


\left({\color{blue}{x}},{\color{red}{5-2x}}\right)


$$

We saw this representation in a previous lesson. It's important to recognize that both representations give the same solution!

### Example: Parametrizing Systems Using the Form (t, y(t))

#### Question

Given that the lines $4x + 5y = 10$ and $8x + 10y = 20$ intersect at an infinite number of points, which points $\big(t, f(t)\big)$ describe the intersection points, where $t$ is a real number?

#### Explanation

We're given that the two lines intersect at an infinite number of points.

We want to find an expression that represents every point of intersection. Notice that we're required to write our solution in the form

$$


\big(t, f(t)\big).


$$

Therefore, we can find our solution as follows:

- First, we set $x=t.$

- Then, we find the corresponding $y$-coordinate for each $x$-coordinate by solving one of the lines for $y.$

- Finally, we write the final result in terms of $t.$

So, we pick the line $4x + 5y = 10,$ solve it for $y,$ and then substitute $x = t,$ as follows:

$$


\begin{aligned}4𝑥+5𝑦 & =10 \\ 5𝑦 & =−4𝑥+10 \\ 𝑦 & =\frac{1}{5}(−4𝑥+10) \\ 𝑦 & =−\frac{4}{5}𝑥+2 \\ 𝑦 & =−\frac{4}{5}𝑡+2\end{aligned}


$$

Therefore, the intersection points are $\left(t,-\dfrac{4}{5}t+2 \right),$ where $t$ is any number.

### Parametrizing the Solution in Terms of Y

Recall our previous example, where we considered the solutions of the following system:

$$


\begin{aligned}4𝑥+2𝑦=10 \\ 8𝑥+4𝑦=20\end{aligned}


$$

By freely choosing to replace $x$ with $t,$ we expressed the solutions in the form $(t,f(t))$ as $(t,5-2t).$

But we are not limited to parametrizing in terms of $x.$ We could just as well choose $y$ freely. If we were to do so, it would lead to a parametrization of the form

$$


({\color{red}{g(t)}},{\color{blue}{t}}).


$$

Indeed, we can express the solutions in this form as follows:

- *Choose one variable freely*: We set $y=t.$

- *Express the other variable in terms of the chosen one*: Then, we find the corresponding $x$-coordinate for each $y$-coordinate by solving one of the equations for $x.$

- *Write the solution as an ordered pair*: Finally, we write the final result in terms of $t.$

Let's do this for the system above. First, set $y=t.$ Then, picking the first equation (again, it doesn't matter which) and solving for $x,$ we have

$$


\begin{aligned}4𝑥+2𝑦 & =10 \\ 4𝑥 & =10−2𝑦 \\ 𝑥 & =\frac{10−2𝑦}{4} \\ 𝑥 & =\frac{10}{4}−\frac{2𝑦}{4} \\ 𝑥 & =\frac{5}{2}−\frac{𝑦}{2}\end{aligned}


$$

Therefore, for any given $y$-value, the corresponding $x$-value is $x = \dfrac{5}{2}-\dfrac{y}{2}.$ Finally, replacing $y$ with $t,$ we can express the intersection points as

$$


\left({\color{red}{\dfrac{5}{2}-\dfrac{t}{2}}},{\color{blue}{t}}\right),


$$

where $\color{blue}t$ is *any* number.

Again, since $y = t$ in this case, we can also represent the solution in the following, equivalent form:

$$


\left({\color{red}{\dfrac{5}{2}-\dfrac{y}{2}}},{\color{blue}{y}}\right)


$$

### Example: Parametrizing Systems Using the Forms (x(y), y) or (x(t), t)

#### Question

Given that the lines $6x - 12y = 18$ and $x - 2y = 3$ intersect at an infinite number of points, express the intersection points in the form $\left(g(y),y\right).$

#### Explanation

We're given that the two lines intersect at an infinite number of points.

We want to find an expression that represents every point of intersection. Notice that we're required to write our solution in the form

$$


\big(f(y), y\big).


$$

Any value of $y$ is a solution, and we can find the corresponding $x$-coordinate for each $y$-coordinate by solving one of the lines for $x,$ as follows:

$$


\begin{aligned}𝑥−2𝑦 & =3 \\ 𝑥 & =2𝑦+3\end{aligned}


$$

Therefore, the intersection points are $\left(2y+3,y\right),$ where $y$ is any number.

### Finding More General Parametrizations

Recall again our previous example, where we considered the solutions of the following system:

$$


\begin{aligned}4𝑥+2𝑦=10 \\ 8𝑥+4𝑦=20\end{aligned}


$$

We first expressed the solutions in the form $(t,f(t))$ (by setting $x$ equal to $t$), and later in the form $(g(t),t)$ (by setting $y$ equal to $t$).

But parametrizations are flexible. Instead of setting a variable equal directly to the parameter $t,$ we can set it equal to a **parametric expression** in $t.$

For instance, we might let $x=2t.$ This still produces all solutions, just written in a slightly different form:

$$


({\color{blue}2t},{\color{red}h(t)})


$$

Parametrization works exactly the same. That is, we can find the solutions as follows:

- *Choose one variable freely*: We set $x=2t.$

- *Express the other variable in terms of the chosen one*: Then, we find the corresponding $y$-coordinate for each $x$-coordinate by solving one of the equations for $y.$

- *Write the solution as an ordered pair*: Finally, we write the final result in terms of $t.$

Let's do this for the system above. First, set $x=2t.$ Then, picking the first equation (again, it doesn't matter which), solving for $y,$ and substituting $x=2t,$ we have

$$


\begin{aligned}4𝑥+2𝑦 & =10 \\ 2𝑦 & =10−4𝑥 \\ 𝑦 & =\frac{10−4𝑥}{2} \\ 𝑦 & =5−2𝑥 \\ 𝑦 & =5−2(2𝑡) \\ 𝑦 & =5−4𝑡\end{aligned}


$$

Therefore, the intersection points are

$$


\left({\color{blue}2t}, {\color{red}5-4t} \right),


$$

where $t$ is any number.

### Example: Parametrizing Systems Using the Form (x(t), y(t))

#### Question

Given that the lines $4x + 2y = 10$ and $2x + y = 5.$ intersect at an infinite number of points, describe these points in terms of the real parameter $t$ such that $y=-3t.$

#### Explanation

We're given that the two lines intersect at an infinite number of points.

We want to find an expression that represents every point of intersection. Notice that we're required to write our solution in the form

$$


\big(f(t), -3t\big).


$$

Therefore, we can find our solution as follows:

- First, we set $y=-3t.$

- Then, we find the corresponding $x$-coordinate for each $y$-coordinate by solving one of the lines for $x.$

- Finally, we write the final result in terms of $t.$

So, we pick the line $2x + y = 5,$ solve it for $x,$ and then substitute $y = -3t,$ as follows:

$$


\begin{aligned}2𝑥+𝑦 & =5 \\ 2𝑥 & =5−𝑦 \\ 𝑥 & =\frac{5−𝑦}{2} \\ 𝑥 & =\frac{5−(−3𝑡)}{2} \\ 𝑥 & =\frac{5+3𝑡}{2}\end{aligned}


$$

Therefore, the intersection points are $\left(\boxed{\dfrac{5+3t}{2}}, -3t\right),$ where $t$ is any number.

### Example: Determining Valid Parametrizations

#### Question

$$


\begin{aligned}3𝑥+𝑦=6 \\ 9𝑥+3𝑦=18\end{aligned}


$$

Consider the system of equations above. Given that this system has infinitely many solutions $(x,y),$ which of the following are valid parametrizations of the solutions?

1. $(t, -3t+6)$

2. $(3t-6,t)$

3. $(2t, -6t+6)$

#### Explanation

Since there are infinitely many solutions to the system, both equations have the same set of solutions $(x,y).$ Therefore, we only need to consider the solution set of one of the equations.

Let's consider each answer choice in turn.

- First, we must construct a parametrization of the form $(t, f(t)).$ So, we set $x = t$ and solve the equation $3x+y = 6$ for $y,$ as follows: Hence, $(t,-3t+6)$ is a valid parametrization. $\color{green}{\checkmark}$

- Next, we must construct a parametrization of the form $(g(t), t).$ So, we set $y = t$ and solve the equation $3x+y = 6$ for $x,$ as follows: This gives $\left(-\dfrac13t + 2, t\right),$ which is ** the same as $(3t-6,t).$ Hence, $(3t-6,t)$ is **** a valid parametrization. $\color{red}{\times}$

- Finally, we must construct a parametrization of the form $(2t, h(t)).$ So, we set $x = 2t$ and solve the equation $3x+y = 6$ for $y,$ as follows: Hence, $(2t,-6t+6)$ is a valid parametrization. $\color{green}{\checkmark}$

Therefore, the correct answer is "I and III only."
