# Solving Systems of Linear Equations by Identifying Structure

Source: https://www.mathacademy.com/topics/6156?courseId=120
Topic ID: 6156

## Prerequisites

- [Factoring Linear Expressions](../../../middle-school/lessons/grade-7/87-factoring-linear-expressions.md)
- [Solving Systems of Equations by Substitution](../../../middle-school/lessons/grade-7/487-solving-systems-of-equations-by-substitution.md)
- [Solving Systems of Linear Equations Using Elimination: Two Transformations](../../../high-school/traditional/lessons/algebra-i/4236-solving-systems-of-linear-equations-using-elimination-two-transformations.md)
- [Manipulating Expressions and Equations](./6142-manipulating-expressions-and-equations.md)

## Lesson

### Introduction

In this lesson, we'll explore some techniques for solving systems of equations efficiently.

To motivate our discussion, let's consider the system of equations below.

$$


\begin{aligned}7𝑥+10𝑦=80 \\ 10𝑥+7𝑦=73\end{aligned}


$$

Suppose we want to determine the quantity $x+y.$ What's the easiest way to do this?

When solving systems of linear equations, two primary techniques are available: the substitution method and the elimination method.

- To solve this using *substitution*, we might start by expressing the first equation in terms of the variable $y.$ By doing this, we get Notice we've introduced a fraction, which makes the remaining steps more awkward.

- To solve this using *elimination*, on the other hand, we might choose to multiply the first equation by $7$ (the coefficient of $y$ in the second equation), the second equation by $10$ (the coefficient of $y$ in the first equation), before subtracting them to eliminate $y{:}$ The issue now is that we've created a system containing very large numbers.

It turns out that we can exploit the system's symmetry to solve it more efficiently. We'll talk about this next.

### Exploiting the Symmetry of a Linear System

Let's consider our system of equations once again.

$$


\begin{aligned}7𝑥+10𝑦=80 \\ 10𝑥+7𝑦=73\end{aligned}


$$

Recall that we wish to calculate the value of $x+y.$

Notice that the coefficient of $x$ in the first equation $(7)$ equals the coefficient of $y$ in the second equation, and vice versa.

$$


\begin{aligned}7𝑥+10𝑦=80 \\ 10𝑥+7𝑦=73\end{aligned}


$$

Because of this symmetry, if we *add* the two equations, both variables will appear with the *same coefficient*:

$$


\begin{aligned}7𝑥+10𝑦 & =80 \\ 10𝑥+7𝑦 & =73 \\ (7𝑥+10𝑥)+(10𝑦+7𝑦) & =80+73 \\ 17𝑥+17𝑦 & =153\end{aligned}


$$

Now, we can solve the resulting equation for $x + y{:}$

$$


\begin{aligned}17𝑥+17𝑦 & =153 \\ 17(𝑥+𝑦) & =153 \\ 𝑥+𝑦 & =\frac{153}{17} \\ 𝑥+𝑦 & =9\end{aligned}


$$

And we're done!

### Symmetric Systems Containing Opposite Signs

Now, consider the case where the coefficients are arranged with *opposite signs*:

$$


\begin{aligned}𝑎𝑥−𝑏𝑦=𝑚 \\ 𝑏𝑥−𝑎𝑦=𝑛\end{aligned}


$$

In this case, adding the equations produces equal coefficients of $x$ and $y,$ but with *opposite signs*, allowing us to solve quickly for $x-y.$

Let's see a concrete example of the case with opposite signs.

### Example: Solving Systems of Equations Using Symmetry

#### Question

$$


\begin{aligned}6𝑥−13𝑦=80 \\ 13𝑥−6𝑦=72\end{aligned}


$$

If the solution to the system above is $(x, y),$ what is the value of $x - y?$

#### Explanation

Notice that the coefficient of $x$ in the first equation and the coefficient of $y$ in the second equation differ by a factor of $-1$, and vice versa.

$$


\begin{aligned}6𝑥\,−\,13𝑦=80 \\ 13𝑥\,−\,6𝑦=72\end{aligned}


$$

Therefore, if we add the equations, the variables will have the same coefficient.

First, we add the two equations and group like terms:

$$


\begin{aligned}6𝑥−13𝑦 & =80 \\ 13𝑥−6𝑦 & =72 \\ (6𝑥+13𝑥)+(−13𝑦−6𝑦) & =(80+72) \\ 19𝑥−19𝑦 & =152\end{aligned}


$$

Next, we solve the resulting equation for $x - y{:}$

$$


\begin{aligned}19𝑥−19𝑦 & =152 \\ 19(𝑥−𝑦) & =152 \\ 𝑥−𝑦 & =\frac{152}{19} \\ & =8\end{aligned}


$$

Hence, the value of $x-y$ is $8.$

### Quick-Substitution

Now, consider the system of equations below.

$$


\begin{aligned}\frac{5}{6}𝑦=−18 \\ 𝑥+\frac{5}{6}𝑦=7\end{aligned}


$$

How can we quickly find the value of $x?$

Notice that the expression $\dfrac{5}{6}y$ occurs in both equations.

$$


\begin{aligned}\frac{5}{6}𝑦=−18 \\ 𝑥+\frac{5}{6}𝑦=7\end{aligned}


$$

This means we don't need to solve for the variable $y$ in the first equation to find $x.$ This saves us a lot of time.

From the first equation, we have

$$


{\color{blue}\dfrac{5}{6}y} = {\color{red}{-18}}.


$$

Next, we substitute this value into the second equation:

$$


\begin{aligned}𝑥+\frac{5}{6}𝑦 & =7 \\ 𝑥+(−18) & =7 \\ 𝑥−18 & =7\end{aligned}


$$

Finally, we solve for $x{:}$

$$


\begin{aligned}𝑥−18 & =7 \\ 𝑥−18+18 & =7+18 \\ 𝑥 & =25\end{aligned}


$$

Therefore, the value of $x$ is $25.$

Notice that this problem used the substitution method. But since a repeated expression appeared in both equations, taking advantage of this made the solution much easier.

Let's see another example.

### Example: Solving Systems of Equations Using Quick-Substitution

#### Question

$$


\begin{aligned}𝑥+𝑦=10 \\ 4(𝑥+𝑦)+2𝑦=52\end{aligned}


$$

If $(x, y)$ is the solution to the given system of equations, what is the value of $y?$

#### Explanation

Notice that the expression $(x+y)$ occurs in both equations.

From the first equation, we have that

$$


x+y = 10.


$$

Next, we substitute this value into the second equation to solve for $y{:}$

$$


\begin{aligned}4(𝑥+𝑦)+2𝑦 & =52 \\ 4(10)+2𝑦 & =52 \\ 40+2𝑦 & =52 \\ 2𝑦 & =52−40 \\ 2𝑦 & =12 \\ 𝑦 & =\frac{12}{2} \\ 𝑦 & =6\end{aligned}


$$

Therefore, the value of $y$ is $6.$

### Introducing New Variables

Sometimes, we may want to introduce new variables into our system to expedite the solution process.

To demonstrate, let's solve the system of equations below.

$$


\begin{aligned}4(5𝑥)+3(6𝑦)=29 \\ −4(5𝑥)+3(6𝑦)=13\end{aligned}


$$

Notice that the expressions $5x$ and $6y$ each appear multiple times. To simplify the system, we introduce two *new variables* $w$ and $z,$ as follows:

$$


w=5x \qquad\text{and}\qquad z=6y


$$

Then, our system of equations can be written as follows:

$$


\begin{aligned}4𝑤+3𝑧=29 \\ −4𝑤+3𝑧=13\end{aligned}


$$

We will solve the new system using the elimination method.

Notice that when we add the two equations, the $4w$ terms will cancel:

$$


\begin{aligned}4𝑤+3𝑧 & =29 \\ −4𝑤+3𝑧 & =13 \\ (3𝑧+3𝑧) & =(29+13) \\ 6𝑧 & =42 \\ 𝑧 & =7\end{aligned}


$$

Now, we plug in $z=7$ into the first equation to find $w{:}$

$$


\begin{aligned}4𝑤+3𝑧 & =29 \\ 4𝑤+3(7) & =29 \\ 4𝑤+21 & =29 \\ 4𝑤 & =8 \\ 𝑤 & =2\end{aligned}


$$

Finally, we can solve for the original variables $x$ and $y{:}$

$$


\begin{aligned}\begin{aligned}𝑤=2 \\ 𝑧=7\end{aligned}\,⟹\,\begin{aligned}5𝑥=2 \\ 6𝑦=7\end{aligned}\,⟹\,\begin{aligned}𝑥=\frac{2}{5} \\ 𝑦=\frac{7}{6}\end{aligned}\end{aligned}


$$

This method is similar to substitution, but instead of reusing an expression directly, we create new variables to represent complex pieces.

Let's see another, slightly more complicated example.

### Example: Solving Systems of Equations by Introducing New Variables

#### Question

$$


\begin{aligned}4(𝑥−2)+3(2𝑦+1)=39 \\ −4(𝑥−2)+3(2𝑦+1)=21\end{aligned}


$$

The equations above form a system, and the solution is $(x, y).$ What is the value of $3(2y + 1)?$

#### Explanation

First, we let $w=x-2$ and $z=2y+1,$ so that the system may be written as follows:

$$


\begin{aligned}4𝑤+3𝑧=39 \\ −4𝑤+3𝑧=21\end{aligned}


$$

We will solve the system using elimination.

Notice that when we add the two equations, the $4w$ terms will cancel:

$$


\begin{aligned}4𝑤+3𝑧 & =39 \\ −4𝑤+3𝑧 & =21 \\ (3𝑧+3𝑧) & =(39+21) \\ 6𝑧 & =60 \\ 𝑧 & =10\end{aligned}


$$

Since $z=2y+1,$ we have

$$


\begin{aligned}3(2𝑦+1) & =3𝑧 \\ & =3(10) \\ & =30.\end{aligned}


$$
