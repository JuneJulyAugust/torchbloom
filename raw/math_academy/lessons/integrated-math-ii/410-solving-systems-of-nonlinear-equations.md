# Solving Systems of Nonlinear Equations

Source: https://www.mathacademy.com/topics/410?courseId=133
Topic ID: 410

## Prerequisites

- [Solving Quadratic Equations with No Constant Term](../algebra-i/393-solving-quadratic-equations-with-no-constant-term.md)
- [The Discriminant of a Quadratic Equation](../algebra-i/425-the-discriminant-of-a-quadratic-equation.md)
- [Solving Systems of Equations by Substitution](../grade-7/487-solving-systems-of-equations-by-substitution.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)

## Lesson

### Introduction

In previous lessons, we learned how to solve a system of two equations using the substitution method. In this lesson, we'll learn how to solve systems where at least one equation is quadratic.

Consider the system of equations given below.

$$


\begin{aligned}𝑦=𝑥^{2}−5𝑥+6 \\ 𝑦=2\end{aligned}


$$

We call this a **system of nonlinear equations** because at least one equation is nonlinear. In fact, the first equation is quadratic in the variable $x,$ making the entire system nonlinear.

The good news is that we can solve a system of nonlinear equations using the substitution method!

Notice that, for this particular system, both equations are solved explicitly for the variable $y.$ Therefore, we can set the right-hand side of both equations equal to each other and solve for $x,$ as follows:

$$


\begin{aligned}𝑥^{2}−5𝑥+6 & =2 \\ 𝑥^{2}−5𝑥+6−2 & =2−2 \\ 𝑥^{2}−5𝑥+4 & =0 \\ (𝑥−1)(𝑥−4) & =0 \\ 𝑥 & =1,\,4\end{aligned}


$$

Now, from the second equation, we have

$$


y=2.


$$

Therefore, the solutions to this system are

$$


(x_1,y_1) = (1,2) \qquad\text{and}\qquad (x_2,y_2) = (4,2).


$$

### The Number of Solutions of a Linear-Quadratic System

Let's consider our system of equations once more:

$$


\begin{aligned}𝑦=𝑥^{2}−5𝑥+6 \\ 𝑦=2\end{aligned}


$$

Notice that this system contains two variables $x$ and $y,$ and consists of one linear and one quadratic equation.

We'll now summarize the steps we took to find the solution:

- **Step 1**: First, we used the method of substitution to eliminate the variable $y,$ giving the following quadratic equation in the variable $x{:}$

- **Step 2**: Next, we found that the solutions to this equation were

- **Step 3**: Finally, we found the value of $y$ corresponding to each $x$-value by substituting back into one of the original equations. In this case, we found that $y = 2$ for both values of $x,$ giving the solutions

This particular system had two unique solutions in total. The number of solutions to a system consisting of one linear and one quadratic equation depends upon the *discriminant* of the quadratic equation found in step 1.

Recall that:

- If $\mathcal{D}>0,$ then the system of equations has $2$ distinct real solutions.

- If $\mathcal{D}=0,$ then the system of equations has $1$ real solution.

- If $\mathcal{D}<0,$ then the system of equations has no real solutions.

These results can also be viewed geometrically, an idea that we'll explore in future lessons.

Let's take a look at an example where there are no real solutions to a nonlinear system.

### Example: Solving Systems of Equations When One Value Is Given

#### Question

$$


\begin{aligned}𝑥=6 \\ 𝑥=−3𝑦^{2}+2𝑦+4\end{aligned}


$$

Solve the system of equations shown above.

#### Explanation

First, we set the equations equal and solve for $y{:}$

$$


\begin{aligned}−3𝑦^{2}+2𝑦+4 & =6 \\ −3𝑦^{2}+2𝑦−2 & =0 \\ 3𝑦^{2}−2𝑦+2 & =0\end{aligned}


$$

In the obtained quadratic equation, we have

$$


a = 3, \qquad b = -2, \qquad c = 2.


$$

So, the discriminant of the quadratic is

$$


\begin{aligned}D & =𝑏^{2}−4𝑎𝑐 \\ & =(−2)^{2}−4(3)(2) \\ & =4−24 \\ & =−20 \\ & <0\end{aligned}


$$

Since the discriminant is less than zero, we conclude that the system has no real solutions.

### Example: Solving Linear-Quadratic Systems of Equations

#### Question

$$


\begin{aligned}𝑦=𝑥−4 \\ 𝑦=𝑥^{2}−5𝑥+5\end{aligned}


$$

Find the solution $(x, y)$ of the system above.

#### Explanation

First, we set the equations equal and solve for $x{:}$

$$


\begin{aligned}𝑥^{2}−5𝑥+5 & =𝑥−4 \\ 𝑥^{2}−6𝑥+9 & =0 \\ (𝑥−3)^{2} & =0 \\ 𝑥−3 & =0 \\ 𝑥 & =3\end{aligned}


$$

Now, we substitute this into the first equation:

$$


\begin{aligned}𝑦 & =𝑥−4 \\ & =3−4 \\ & =−1\end{aligned}


$$

Therefore, the solution is $\big(3, -1 \big).$

### Systems Containing Two Quadratic Equations

Consider the system of equations shown below.

$$


\begin{aligned}𝑥=4𝑦^{2} \\ 𝑥=𝑦^{2}+12𝑦+36\end{aligned}


$$

Notice that, in this case, *both* equations are quadratic in the variable $y.$ However, we can still solve this equation using substitution!

From the second equation, we have

$$


x = y^2 + 12y + 36.


$$

We can substitute this into the first equation and solve the resulting quadratic in the variable $y,$ as follows:

$$


\begin{aligned}𝑥 & =4𝑦^{2} \\ 𝑦^{2}+12𝑦+36 & =4𝑦^{2} \\ −3𝑦^{2}+12𝑦+36 & =0\end{aligned}


$$

Dividing both sides of the equation by $-3,$ we get

$$


\begin{aligned}𝑦^{2}−4𝑦−12 & =0\end{aligned}


$$

and this factors as

$$


\begin{aligned}(𝑦−6)(𝑦+2) & =0.\end{aligned}


$$

So, the solutions for $y$ are $y_1 = -2$ and $y_2 = 6.$

Now, we substitute each value of $y$ into the first equation to find the corresponding values of $x{:}$

- For $y_1=-2,$ we get

- For $y_2=6,$ we get

Therefore, the solutions to this system of equations are

$$


(x_1,y_1) = (16,-2) \qquad\text{and}\qquad (x_2,y_2) = (144,6).


$$

Sometimes, we need to solve one of the equations explicitly for one of the variables before we can perform the substitution. Let's see an example.

### Example: Solving Systems With Two Quadratic Equations

#### Question

$$


\begin{aligned}6𝑥−4𝑦^{2}=2𝑥 \\ 𝑥=2𝑦^{2}−5𝑦\end{aligned}


$$

If $(x,y)$ is a solution of the system above such that $y \ne 0$, what is the value of $\dfrac{x}{y}?$

#### Explanation

First, we simplify the first equation:

$$


\begin{aligned}6𝑥−4𝑦^{2} & =2𝑥 \\ 4𝑥−4𝑦^{2} & =0 \\ 4𝑥 & =4𝑦^{2} \\ 𝑥 & =𝑦^{2}\end{aligned}


$$

Next, from the second equation, we have

$$


x = 2y^2 - 5y.


$$

We substitute this into the first equation:

$$


\begin{aligned}𝑥 & =𝑦^{2} \\ 2𝑦^{2}−5𝑦 & =𝑦^{2} \\ 𝑦^{2}−5𝑦 & =0 \\ 𝑦(𝑦−5) & =0 \\ 𝑦 & =0,\,5\end{aligned}


$$

Now, we substitute $y$ into $x=y^2$.

- For $y_1=0,$ we get

- For $y_2=5,$ we get

Therefore, the solutions are

$$


(x_1,y_1) = (0,0) \qquad\text{and}\qquad (x_2,y_2) = (25,5).


$$

Finally, since we require the solution such that $y \ne 0,$ we have that

$$


\begin{aligned}\frac{𝑥}{𝑦} & =\frac{𝑥_{2}}{𝑦_{2}} \\ & =\frac{25}{5} \\ & =5.\end{aligned}


$$
