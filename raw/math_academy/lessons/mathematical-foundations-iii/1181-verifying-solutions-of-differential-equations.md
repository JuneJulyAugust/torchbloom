# Verifying Solutions of Differential Equations

Source: https://www.mathacademy.com/topics/1181?courseId=136
Topic ID: 1181

## Prerequisites

- [The Chain Rule With Trigonometric Functions](../ap-calculus-ab/305-the-chain-rule-with-trigonometric-functions.md)
- [The Chain Rule With Exponential Functions](../ap-calculus-ab/1007-the-chain-rule-with-exponential-functions.md)
- [Introduction to Differential Equations](./3215-introduction-to-differential-equations.md)

## Lesson

### Introduction

Suppose we have the differential equation

$$


\dfrac{\textrm d y}{\textrm d x} = 2y.


$$

How can we verify whether a given function is a **solution** of this equation? For example, is $y=e^{2x}$ a solution?

To check whether a given function $y$ satisfies a differential equation, we calculate the derivative and plug the result into the equation.

For $y=e^{2x},$ the derivative is

$$


\dfrac{\textrm d y}{\textrm d x} = 2e^{2x}.


$$

We now substitute the above and our expression for $y,$ into the original equation and see if we get a true statement:

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =2𝑦 \\ \underset{𝑦^{′}}{\underset{}{2𝑒^{2𝑥}}} & =2⋅\underset{𝑦}{\underset{}{𝑒^{2𝑥}}} \\ 2𝑒^{2𝑥} & =2𝑒^{2𝑥}\,✓\end{aligned}


$$

We get a true statement! Therefore, $y=e^{2x}$ is a solution to the original equation.

**Note:** There are often infinitely many solutions to a given differential equation! We will learn how to solve differential equations like the one shown above in future lessons.

### Example: Identifying a Solution to a First-Order Differential Equation

#### Question

Consider the following differential equation.

$$


y' = -\dfrac{y}{x}, \qquad x \neq 0


$$

Let $f(x) = \dfrac{1}{x}.$ Which of the following statements are true?

1. $f'(x) = -\dfrac{1}{x^2}$

2. Substituting $y = f(x)$ and $y' = f'(x)$ into the differential equation gives a true statement

3. The function $y=f(x)$ is a solution of the differential equation

#### Explanation

For a function $f(x)$ to be a solution to a differential equation, it must satisfy the equation for all values of $x$ in the equation's domain.

With that in mind, let's check each statement in turn.

- Statement I is true. Differentiating $f(x) = \dfrac{1}{x},$ we get

- Statement II is true. Substituting $y = \dfrac{1}{x}$ and $y' = -\dfrac{1}{x^2}$ into the original equation, we get a true statement:

- Statement III is true. Since statement II is true, the function $y = \dfrac{1}{x}$ is a solution to our differential equation.

Therefore, the correct answer is "I, II, and III."

### Example: Identifying Solutions to First-Order Differential Equations

#### Question

Consider the differential equation

$$


\dfrac{\textrm{d}y}{\textrm{d}x} = y.


$$

Which of the following is a solution to this equation?

1. $y = e^x + 1$

2. $y = -e^x$

3. $y = 2e^x$

#### Explanation

For a function $f(x)$ to be a solution to a differential equation, it must satisfy the equation for all values of $x$ in the equation's domain.

We check each proposed solution by differentiating and substituting it into the original equation.

- Differentiating $y = e^x + 1,$ we get $\dfrac{\textrm{d}y}{\textrm{d}x} = e^x.$ Substituting into the original equation, we get This statement is **. Therefore, the function $y = e^x+1$ is ** a solution to our differential equation.

- Differentiating $y = -e^x,$ we get $\dfrac{\textrm{d}y}{\textrm{d}x} = -e^x.$ Substituting into the original equation, we get This statement is **. Therefore, the function $y = -e^x$ ** a solution to our differential equation.

- Differentiating $y = 2e^x,$ we get $\dfrac{\textrm{d}y}{\textrm{d}x} = 2e^x.$ Substituting into the original equation, we get This statement is **. Therefore, the function $y = 2e^x$ ** a solution to our differential equation.

Therefore, the correct answer is "II and III only."

### Example: Identifying Solutions to Initial Value Problems

#### Question

Consider the following initial value problem

$$


\dfrac{\textrm{d}y}{\textrm{d}x} = \dfrac{3y}{x}, \qquad y(-1) = -2.


$$

You're given that $y = Ax^3$ is the solution to this initial value problem. What is the value of the constant $A?$

#### Explanation

We're given that $y = Ax^3$ is the solution to the initial value problem. Therefore, it must satisfy the differential equation ** the initial condition $y(-1) = -2.$

Substituting the initial condition $y({\color{red}{-1}}) = {\color{blue}{-2}}$ into our solution and solving for $A,$ we get

$$


\begin{aligned}𝑦 & =𝐴𝑥^{3} \\ −2 & =𝐴(−1)^{3} \\ −2 & =𝐴(−1) \\ 𝐴 & =2.\end{aligned}


$$

Therefore, the solution to the initial value problem is

$$


y = 2x^3 .


$$
