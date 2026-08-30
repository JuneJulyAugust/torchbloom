# Clairaut Differential Equations

Source: https://www.mathacademy.com/topics/6355?courseId=61
Topic ID: 6355

## Prerequisites

- [Cartesian Equations of Parametric Curves](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1255-cartesian-equations-of-parametric-curves.md)
- [Continuity and Differentiability of Functions](../../../ap-courses/lessons/ap-calculus-ab/1691-continuity-and-differentiability-of-functions.md)
- [Solving First-Order ODEs by Substitution](./3179-solving-first-order-odes-by-substitution.md)

## Lesson

### Introduction

A **Clairaut differential equation** is an ordinary differential equation of the form

$$


y=x y'+g(y')


$$

where $g$ is a continuously differentiable function.

For example, consider the equation

$$


y = xy' + (y')^{2}.


$$

This is a Clairaut differential equation with

$$


g(y') = (y')^{2}.


$$

Clairaut equations have a special structure that allows them to be solved using elementary methods, leading to a family of straight-line solutions and a singular solution.

Later in the lesson, we will learn how to solve these equations. For now, let’s practice identifying them.

### Example: Identifying Clairaut Differential Equations

#### Question

Which of the following equations is a Clairaut differential equation?

1. $y -xy' -\ln(y')=0$

2. $y^4\cos(x) +xyy' = y^2$

3. $y= xy' + 2y'$

#### Explanation

A Clairaut differential equation has the form

$$


y = xy' + g(y'),


$$

where $g$ is a differentiable function of $y'.$

With that in mind, let's examine the given options.

- Equation I is a Clairaut differential equation. Isolating the variable $y,$ we get which is a Clairaut differential equation of the form $y = xy' + g(y')$ with

- Equation II is ** a Clairaut differential equation. Dividing the equation by $y,$ we get This equation cannot be written in the form $y = xy' + g(y').$

- Equation III is a Clairaut differential equation of the form $y = xy' + g(y')$ with

Therefore, the correct answer is "I and III only."

### Solving a Clairaut Differential Equation

Now that we have practiced identifying Clairaut equations, let’s see how to solve them.

The key feature of Clairaut’s equation is its special form, which leads to a family of **straight-line** solutions and one **singular solution**.

Recall that a Clairaut equation has the form

$$


y = x\,y' + g(y'),


$$

where $g$ is a differentiable function.

To simplify the notation, we introduce the substitution:

$$


p = y'


$$

With this substitution, the equation becomes

$$


y = xp + g(p).


$$

Next, we differentiate both sides of the substituted equation with respect to $x$. Remember, $p$ is a function of $x$, so we must use the product rule on the $xp$ term and the chain rule on $g(p)$:

$$


\begin{aligned}𝑦^{′} & =\frac{d}{d𝑥}(𝑥𝑝)+\frac{d}{d𝑥}(𝑔(𝑝)) \\ 𝑝 & =(1⋅𝑝+𝑥⋅\frac{d𝑝}{d𝑥})+𝑔^{′}(𝑝)⋅\frac{d𝑝}{d𝑥}\end{aligned}


$$

Using $p' = \dfrac{\textrm{d}p}{\textrm{d}x}$, the expression simplifies to

$$


p = p + x p' + g'(p)\,p'.


$$

Now, if we simply subtract $p$ from both sides and factor out the common term $p'$, we arrive at the pivotal equation for finding our solutions:

$$


0 = p'(x + g'(p))


$$

Since this expression is a product that equals zero, the equation can be satisfied in two different ways. Each way provides us with one type of solution.

- **Case I: The General Solution.** The first possibility is that the derivative of $p$ is zero. If $p' = 0$, then $p$ must be a constant. Let's denote this constant as $c$: Substituting $p = c$ back into the original Clairaut equation ($y = xp + g(p)$), we directly obtain the **general solution** This gives a family of straight-line solutions. Each value of $c$ produces a different line, where $c$ is the slope and $g(c)$ gives the $y$-intercept.

- **Case II: The Singular Solution.** If instead $x + g'(p) = 0$, then we obtain a singular solution. Let's first solve for $x$ in terms of $p$: Then, let's substitute this $x$ back into the original Clairaut equation: This gives us the **singular solution** defined parametrically by the equations:

Now, let’s take a look at a concrete example of how to find the general solution to a Clairaut equation.

### Finding the General Solution

Let's find the general solution of the Clairaut differential equation

$$


y = xy' + (y')^2.


$$

To solve this, we start by setting $p = y'.$

Substituting this into the equation gives

$$


y = x p + p^2.


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}𝑦^{′} & =(𝑥𝑝+𝑝^{2})^{′} \\ 𝑝 & =𝑝+𝑥𝑝^{′}+2𝑝𝑝^{′} \\ 0 & =𝑝^{′}(𝑥+2𝑝)\end{aligned}


$$

The product on the right-hand side equals zero, so at least one factor must be zero.

The **general solution** is obtained by setting the first factor to zero, i.e., $p' = 0.$ (The other factor, $x+2p=0,$ leads to a *singular solution*, which we are not finding here.)

Since $p' = 0,$ $p$ is constant, say

$$


p = c.


$$

Substituting $p = c$ into $y = x p + p^2$ we get the general solution

$$


y = cx + c^2.


$$

This represents a family of straight lines, one line for each constant value of $c.$

### Example: Finding the General Solution

#### Question

Find the general solution of the Clairaut differential equation:

$$


y = xy' + e^{-y'}


$$

#### Explanation

To solve the Clairaut differential equation

$$


y = xy' + e^{-y'},


$$

we start by setting $p = y'.$

Substituting this into the equation gives

$$


y = x p + e^{-p}.


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}𝑦^{′} & =(𝑥𝑝+𝑒^{−𝑝})^{′} \\ 𝑝 & =𝑝+𝑥𝑝^{′}−𝑒^{−𝑝}𝑝^{′} \\ 0 & =𝑝^{′}(𝑥−𝑒^{−𝑝})\end{aligned}


$$

The product on the right-hand side equals zero, which means at least one of the factors must be zero.

The general solution of the Clairaut differential equation is obtained if $p' = 0.$ Then, $p$ is constant, say

$$


p = c.


$$

Substituting $p = c$ into $y = x p + e^{-p},$ we get the general solution

$$


y = cx + e^{-c}


$$

This represents a family of straight lines, one line for each constant value of $c.$

### The Singular Solution

Now, let's find the singular solution of the Clairaut differential equation

$$


y = xy' + (y')^2.


$$

**Step 1**: Differentiate the equation to find the conditions for the solution.

To begin, we introduce a parameter by setting $p = y'.$ Substituting this into the equation gives

$$


y = x p + p^2.


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{d}{d𝑥}(𝑥𝑝+𝑝^{2}) \\ 𝑦^{′} & =(1⋅𝑝+𝑥⋅\frac{d𝑝}{d𝑥})+2𝑝⋅\frac{d𝑝}{d𝑥} \\ 𝑝 & =𝑝+𝑥𝑝^{′}+2𝑝𝑝^{′} \\ 0 & =𝑥𝑝^{′}+2𝑝𝑝^{′} \\ 0 & =𝑝^{′}(𝑥+2𝑝)\end{aligned}


$$

This equation tells us that either $p' = 0$ or $x + 2p = 0.$

- The condition $p' = 0$ leads to the *general solution* of the Clairaut equation. We've already seen how to deal with this case.

- The condition $x + 2p = 0$ leads to the *singular solution*, which is the envelope of the general solution's family of curves.

On the next slide, we will use the second condition to find the singular solution.

### Finding the Singular Solution

Recall the original equation in terms of the parameter $p{:}$

$$


y = xp + p^2


$$

And we have the condition for the singular solution:

$$


x = -2p


$$

We now proceed as follows:

**Step 2**: Find the singular solution in parametric form.

Let's substitute this expression for $x$ into the equation for $y{:}$

$$


\begin{aligned}𝑦 & =(−2𝑝)𝑝+𝑝^{2} \\ & =−2𝑝^{2}+𝑝^{2} \\ & =−𝑝^{2}\end{aligned}


$$

This gives us the singular solution in parametric form, using $p$ as the parameter:

$$


\begin{aligned}𝑥=−2𝑝 \\ 𝑦=−𝑝^{2}.\end{aligned}


$$

**Step 3**: Convert the parametric solution to an explicit function $y(x).$

To eliminate the parameter $p,$ we solve the first equation for $p{:}$

$$


p = -\dfrac{x}{2}


$$

Now, we substitute this expression for $p$ into the second equation:

$$


\begin{aligned}𝑦 & =−𝑝^{2} \\ & =−(−\frac{𝑥}{2})^{2} \\ & =−\frac{𝑥^{2}}{4}\end{aligned}


$$

Therefore, the explicit form of the singular solution is

$$


y = -\dfrac{x^2}{4}.


$$

### Example: Finding the Singular Solution

#### Question

Find the singular solution to the following Clairaut differential equation:

$$


y = xy' + (y')^2+1.


$$

#### Explanation

A Clairaut differential equation has the form

$$


y = xy' + g(y'),


$$

where $g$ is a differentiable function of $y'.$

To solve the Clairaut differential equation

$$


y = xy' + (y')^2 +1,


$$

we start by setting $p = y'.$

Substituting this into the equation gives

$$


y = xp + p^2+1.


$$

Next, we differentiate both sides with respect to $x{:}$

$$


\begin{aligned}𝑦^{′} & =(𝑥𝑝+𝑝^{2}+1)^{′} \\ 𝑝 & =𝑝+𝑥𝑝^{′}+2𝑝𝑝^{′} \\ 0 & =𝑝^{′}(𝑥+2𝑝)\end{aligned}


$$

The product on the right-hand side equals zero, so at least one factor must be zero.

The singular solution of the Clairaut differential equation is obtained if $x + 2p = 0.$ Then,

$$


x = -2p.


$$

Now, let's substitute this into $y = xp + p^2+1{:}$

$$


\begin{aligned}𝑦 & =𝑥𝑝+𝑝^{2}+1 \\ & =(−2𝑝)𝑝+𝑝^{2}+1 \\ & =−2𝑝^{2}+𝑝^{2}+1 \\ & =−𝑝^{2}+1\end{aligned}


$$

Thus the singular solution is given parametrically by

$$


\begin{aligned}𝑥=−2𝑝 \\ 𝑦=−𝑝^{2}+1\end{aligned}


$$

To eliminate $p,$ we first solve the first equation for $p{:}$

$$


p = -\dfrac{x}{2}


$$

Next, let's substitute this expression for $p$ into the second equation:

$$


\begin{aligned}𝑦 & =−𝑝^{2}+1 \\ & =−(−\frac{𝑥}{2})^{2}+1 \\ & =1−\frac{𝑥^{2}}{4}\end{aligned}


$$

Therefore, the explicit form of the singular solution is

$$


y = 1- \dfrac{x^2}{4}.


$$
