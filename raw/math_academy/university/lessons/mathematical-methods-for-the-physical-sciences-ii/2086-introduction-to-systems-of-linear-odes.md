# Introduction to Systems of Linear ODEs

Source: https://www.mathacademy.com/topics/2086?courseId=155
Topic ID: 2086

## Prerequisites

- [Introduction to First-Order Linear ODEs](../differential-equations/906-introduction-to-first-order-linear-odes.md)
- [Verifying Solutions of Differential Equations](../../../ap-courses/lessons/ap-calculus-ab/1181-verifying-solutions-of-differential-equations.md)
- [Representing 2x2 Systems of Equations Using a Matrix Product](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1729-representing-2x2-systems-of-equations-using-a-matrix-product.md)
- [Differentiating Vector-Valued Functions](../../../ap-courses/lessons/ap-calculus-bc/4139-differentiating-vector-valued-functions.md)

## Lesson

### Introduction

A **first-order linear system of differential equations** with two dependent variables is a system of equations that takes the following *standard form*:

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=𝑎(𝑡)𝑥_{1}(𝑡)+𝑏(𝑡)𝑥_{2}(𝑡)+𝑓(𝑡) \\ 𝑥_{′2}^{}(𝑡)=𝑐(𝑡)𝑥_{1}(𝑡)+𝑑(𝑡)𝑥_{2}(𝑡)+𝑔(𝑡)\end{aligned}


$$

where

- $a(t),$ $b(t),$ $c(t),$ $d(t),$ $f(t),$ and $g(t)$ are *known* functions, and

- $x_1(t)$ and $x_2(t)$ are *unknown* functions (dependent variables).

For example,

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=ln⁡(𝑡)𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=−2𝑡𝑥_{1}(𝑡)+𝑥_{2}(𝑡)+5𝑡^{2}+1\end{aligned}


$$

is a first-order linear system of ODEs since it can be written in the standard form

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=0⋅𝑥_{1}(𝑡)+ln⁡(𝑡)⋅𝑥_{2}(𝑡)+0 \\ 𝑥_{′2}^{}(𝑡)=−2𝑡⋅𝑥_{1}(𝑡)+1⋅𝑥_{2}(𝑡)+(5𝑡^{2}+1)\end{aligned}


$$

where

$$


\begin{aligned}𝑎(𝑡)=0, & & 𝑏(𝑡)=ln⁡(𝑡), & & 𝑓(𝑡)=0, \\ 𝑐(𝑡)=−2𝑡, & & 𝑑(𝑡)=1, & & 𝑔(𝑡)=5𝑡^{2}+1.\end{aligned}


$$

On the other hand,

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=ln⁡(𝑥_{1}(𝑡))+𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=𝑡𝑥_{1}(𝑡)−𝑡^{2}𝑥_{2}(𝑡)+sin⁡(𝑡)\end{aligned}


$$

is not a first-order linear system of ODEs since it contains the term $\ln(x_1(t)).$

Similar definitions apply to systems with three or more variables.

### Example: Identifying a Linear System of Differential Equations

#### Question

Which of the following systems of differential equations are linear?

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=\frac{1}{2}𝑥_{21}^{}(𝑡)+5𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=\sqrt{√5}𝑥_{1}(𝑡)+3sin⁡(𝑥_{2}(𝑡))\end{aligned}


$$

#### Explanation

A first-order linear system of differential equations with two dependent variables is a system of equations that takes the following standard form:

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=𝑎(𝑡)𝑥_{1}(𝑡)+𝑏(𝑡)𝑥_{2}(𝑡)+𝑓(𝑡) \\ 𝑥_{′2}^{}(𝑡)=𝑐(𝑡)𝑥_{1}(𝑡)+𝑑(𝑡)𝑥_{2}(𝑡)+𝑔(𝑡)\end{aligned}


$$

where

- $a(t),$ $b(t),$ $c(t),$ $d(t),$ $f(t),$ and $g(t)$ are known functions, and

- $x_1(t)$ and $x_2(t)$ are unknown functions (dependent variables).

With this in mind, let's inspect each system:

- System I is not a first-order linear system of ODEs since it contains the terms $x_1^2(t)$ and $\sin(x_2(t)).$

- System II is a first-order linear system of ODEs since it can be written in the standard form, where

Therefore, only the second system is linear.

### Matrix Differential Equations

We can write any first-order linear system of differential equations in the form of a **matrix differential equation**

$$


\mathbf{x}'(t)=A(t)\mathbf{x}(t)+\mathbf{f}(t).


$$

For example, the system

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=2𝑥_{1}(𝑡)−2𝑥_{2}(𝑡)+4 \\ 𝑥_{′2}^{}(𝑡)=−𝑥_{1}(𝑡)+3𝑥_{2}(𝑡)−𝑡^{2}\end{aligned}


$$

can be written as

$$


[\begin{aligned}𝑥_{′1}^{}(𝑡) \\ 𝑥_{′2}^{}(𝑡)\end{aligned}]


$$

If the coefficients next to the variables are constants (as in the example above), we say that the system has a constant matrix. Then, we can just use the notation $A$ instead of $A(t).$

### Example: Writing a Linear System of Differential Equations in Matrix Form

#### Question

If the following system of differential equations is written in the form $\mathbf{x}'(t)=A\mathbf{x}(t),$ then what is the matrix $A?$

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)+3𝑥_{1}(𝑡)−4𝑥_{2}(𝑡)=0 \\ 𝑥_{′2}^{}(𝑡)−\sqrt{√2}𝑥_{1}(𝑡)+2𝑥_{2}(𝑡)=0\end{aligned}


$$

#### Explanation

A first-order linear system of differential equations with two dependent variables is a system of equations that takes the following standard form:

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=𝑎(𝑡)𝑥_{1}(𝑡)+𝑏(𝑡)𝑥_{2}(𝑡)+𝑓(𝑡) \\ 𝑥_{′2}^{}(𝑡)=𝑐(𝑡)𝑥_{1}(𝑡)+𝑑(𝑡)𝑥_{2}(𝑡)+𝑔(𝑡)\end{aligned}


$$

where

- $a(t),$ $b(t),$ $c(t),$ $d(t),$ $f(t),$ and $g(t)$ are known functions, and

- $x_1(t)$ and $x_2(t)$ are unknown functions (dependent variables). Such a system can always be written in the form

where

$$


[\begin{aligned}𝑥_{1}(𝑡) \\ 𝑥_{2}(𝑡)\end{aligned}]


$$

We have the following system.

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)+3𝑥_{1}(𝑡)−4𝑥_{2}(𝑡)=0 \\ 𝑥_{′2}^{}(𝑡)−\sqrt{√2}𝑥_{1}(𝑡)+2𝑥_{2}(𝑡)=0\end{aligned}


$$

Writing our system in standard form, we get the following:

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=−3𝑥_{1}(𝑡)+4𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=\sqrt{√2}𝑥_{1}(𝑡)−2𝑥_{2}(𝑡).\end{aligned}


$$

So, we can rewrite our system in matrix form as follows:

$$


[\begin{aligned}−3 & 4 \\ \sqrt{√2} & −2\end{aligned}]


$$

Therefore, we have

$$


[\begin{aligned}−3 & 4 \\ \sqrt{√2} & −2\end{aligned}]


$$

### Homogeneous and Inhomogeneous Systems

Recall that a first-order linear system of differential equations with two dependent variables is a system of the form

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=𝑎(𝑡)𝑥_{1}(𝑡)+𝑏(𝑡)𝑥_{2}(𝑡)+𝑓(𝑡) \\ 𝑥_{′2}^{}(𝑡)=𝑐(𝑡)𝑥_{1}(𝑡)+𝑑(𝑡)𝑥_{2}(𝑡)+𝑔(𝑡)\end{aligned}


$$

If $f \equiv 0$ and $g \equiv 0$ (i.e., both $f$ and $g$ are zero functions), then the system is called **homogeneous**. Otherwise, if at least one of $f$ or $g$ is nonzero, the system is **inhomogeneous**.

In matrix form, the system

$$


\mathbf{x}'(t)=A(t)\mathbf{x}(t)+\mathbf{f}(t)


$$

is homogeneous when $\mathbf{f} \equiv \mathbf{0},$ and inhomogeneous when $\mathbf{f} \not\equiv \mathbf{0}.$

For example:

- The system below is homogeneous because $\mathbf{f}(t) = \mathbf{0}$:

- The system below is inhomogeneous because of the term $5t^2$:

### Example: Identifying Homogeneous and Inhomogeneous Systems

#### Question

Which of the following systems are homogeneous?

1. $\begin{aligned}𝑥_{′1}^{}(𝑡)=−2𝑥_{1}(𝑡)+3𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=6𝑥_{1}(𝑡)+𝑥_{2}(𝑡)\end{aligned}$

2. $\begin{aligned}𝑥_{′1}^{}(𝑡)=𝑥_{1}(𝑡)+𝑡^{3} \\ 𝑥_{′2}^{}(𝑡)=−𝑥_{2}(𝑡)+1\end{aligned}$

3. $\begin{aligned}𝑥_{′1}^{}(𝑡)=5𝑥_{1}(𝑡)−𝑥_{2}(𝑡) \\ 𝑥_{′2}^{}(𝑡)=−2𝑥_{1}(𝑡)+4𝑥_{2}(𝑡)\end{aligned}$

#### Explanation

Recall that a first-order linear system of differential equations with two dependent variables is a system of the form

$$


\begin{aligned}𝑥_{′1}^{}(𝑡)=𝑎(𝑡)𝑥_{1}(𝑡)+𝑏(𝑡)𝑥_{2}(𝑡)+𝑓(𝑡) \\ 𝑥_{′2}^{}(𝑡)=𝑐(𝑡)𝑥_{1}(𝑡)+𝑑(𝑡)𝑥_{2}(𝑡)+𝑔(𝑡).\end{aligned}


$$

If $f \equiv 0$ and $g \equiv 0$ (i.e., both $f$ and $g$ are zero functions), then the system is **. Otherwise, if at least one of $f$ or $g$ is not identically zero, the system is **.

With this in mind, let's inspect each system:

- System I is homogeneous since it can be written in the standard form with $f \equiv 0$ and $g \equiv 0{:}$

- System II is inhomogeneous since it can be written in the standard form with $f \not\equiv 0$ and $g \not\equiv 0{:}$

- System III is homogeneous since it can be written in the standard form with $f \equiv 0$ and $g \equiv 0{:}$

Therefore, only the first and third systems are homogeneous.

### Solutions for Systems of ODEs

A **solution of the system** is a vector $\mathbf{x}(t)$ that satisfies the equation

$$


\mathbf{x}'(t)=A\mathbf{x}(t)+\mathbf{f}(t).


$$

For example, one solution to our linear system

$$


[\begin{aligned}2 & −2 \\ −1 & 3\end{aligned}]


$$

is the vector $[\begin{aligned}2𝑒^{𝑡} \\ 𝑒^{𝑡}\end{aligned}]$ We can check this by substituting the vector into the equation:

$$


\begin{aligned}𝐱^{′}(𝑡) & =[\begin{aligned}2 & −2 \\ −1 & 3\end{aligned}]𝐱(𝑡) \\ [\begin{aligned}(2𝑒^{𝑡})^{′} \\ (𝑒^{𝑡})^{′}\end{aligned}] & =[\begin{aligned}2 & −2 \\ −1 & 3\end{aligned}][\begin{aligned}2𝑒^{𝑡} \\ 𝑒^{𝑡}\end{aligned}] \\ [\begin{aligned}2𝑒^{𝑡} \\ 𝑒^{𝑡}\end{aligned}] & =[\begin{aligned}2⋅(2𝑒^{𝑡})+(−2)⋅(𝑒^{𝑡}) \\ (−1)⋅(2𝑒^{𝑡})+3⋅(𝑒^{𝑡})\end{aligned}] \\ [\begin{aligned}2𝑒^{𝑡} \\ 𝑒^{𝑡}\end{aligned}] & =[\begin{aligned}4𝑒^{𝑡}−2𝑒^{𝑡} \\ −2𝑒^{𝑡}+3𝑒^{𝑡}\end{aligned}] \\ [\begin{aligned}2𝑒^{𝑡} \\ 𝑒^{𝑡}\end{aligned}] & =[\begin{aligned}2𝑒^{𝑡} \\ 𝑒^{𝑡}\end{aligned}]\,✓\end{aligned}


$$

### Example: Identifying Solutions to a Matrix Differential Equation

#### Question

Consider the matrix differential equation $[\begin{aligned}5 & 0 \\ 0 & −3\end{aligned}]$ Which of the following vectors are solutions to this equation?

$$


[\begin{aligned}3𝑒^{5𝑡} \\ 5𝑒^{−3𝑡}\end{aligned}]


$$

#### Explanation

Here, we need to substitute each vector into the given matrix differential equation and check if it results in a true statement.

For $\mathbf{x}_1(t),$ we have

$$


\begin{aligned}[\begin{aligned}(3𝑒^{5𝑡})^{′} \\ (5𝑒^{−3𝑡})^{′}\end{aligned}] & =[\begin{aligned}5 & 0 \\ 0 & −3\end{aligned}][\begin{aligned}3𝑒^{5𝑡} \\ 5𝑒^{−3𝑡}\end{aligned}] \\ [\begin{aligned}15𝑒^{5𝑡} \\ −15𝑒^{−3𝑡}\end{aligned}] & =[\begin{aligned}5 & 0 \\ 0 & −3\end{aligned}][\begin{aligned}3𝑒^{5𝑡} \\ 5𝑒^{−3𝑡}\end{aligned}] \\ [\begin{aligned}15𝑒^{5𝑡} \\ −15𝑒^{−3𝑡}\end{aligned}] & =[\begin{aligned}15𝑒^{5𝑡} \\ −15𝑒^{−3𝑡}\end{aligned}].\,✓\end{aligned}


$$

Now, for $\mathbf{x}_2(t),$ we get

$$


\begin{aligned}[\begin{aligned}(𝑡+5)^{′} \\ (𝑡^{2}−3)^{′}\end{aligned}] & =[\begin{aligned}5 & 0 \\ 0 & −3\end{aligned}][\begin{aligned}𝑡+5 \\ 𝑡^{2}−3\end{aligned}] \\ [\begin{aligned}1 \\ 2𝑡\end{aligned}] & =[\begin{aligned}5 & 0 \\ 0 & −3\end{aligned}][\begin{aligned}𝑡+5 \\ 𝑡^{2}−3\end{aligned}] \\ [\begin{aligned}1 \\ 2𝑡\end{aligned}] & ≠[\begin{aligned}5𝑡+25 \\ −3𝑡^{2}+9\end{aligned}].\,×\end{aligned}


$$

Finally, for $\mathbf{x}_3(t),$ we obtain

$$


\begin{aligned}[\begin{aligned}(5𝑒^{𝑡})^{′} \\ (−3𝑒^{𝑡})^{′}\end{aligned}] & =[\begin{aligned}5 & 0 \\ 0 & −3\end{aligned}][\begin{aligned}5𝑒^{𝑡} \\ −3𝑒^{𝑡}\end{aligned}] \\ [\begin{aligned}5𝑒^{𝑡} \\ −3𝑒^{𝑡}\end{aligned}] & =[\begin{aligned}5 & 0 \\ 0 & −3\end{aligned}][\begin{aligned}5𝑒^{𝑡} \\ −3𝑒^{𝑡}\end{aligned}] \\ [\begin{aligned}5𝑒^{𝑡} \\ −3𝑒^{𝑡}\end{aligned}] & =[\begin{aligned}25𝑒^{𝑡} \\ 9𝑒^{𝑡}\end{aligned}].\,×\end{aligned}


$$

Therefore, we conclude that the correct answer is "$\mathbf{x}_1(t)$ only."
