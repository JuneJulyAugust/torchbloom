# Solving Systems of Nonlinear Equations by Identifying Structure

Source: https://www.mathacademy.com/topics/6155?courseId=120
Topic ID: 6155

## Prerequisites

- [Solving Systems of Nonlinear Equations Using Graphs](../algebra-i/101-solving-systems-of-nonlinear-equations-using-graphs.md)
- [Factoring Differences of Squares](../algebra-i/370-factoring-differences-of-squares.md)
- [Solving Systems of Linear Equations by Identifying Structure](./6156-solving-systems-of-linear-equations-by-identifying-structure.md)

## Lesson

### Introduction

In this topic, we’ll learn how to solve systems of *nonlinear* equations by exploiting their structure. This means spotting repeated expressions or factors that allow us to simplify the system.

To demonstrate, consider the nonlinear system of equations below.

$$


\begin{aligned}4𝑥−12=\sqrt{√14} \\ (4𝑥−12)^{2}=𝑦\end{aligned}


$$

How can we quickly determine the value of $y?$

When solving nonlinear systems, it is often helpful to check whether both equations share a *common expression*. If they do, we can isolate that expression in one equation and substitute it into the other, greatly simplifying our work.

Here, notice that both equations involve the expression $4x - 12.$

$$


\begin{aligned}4𝑥−12=\sqrt{√14} \\ (4𝑥−12)^{2}=𝑦\end{aligned}


$$

From the first equation, we have

$$


4x - 12 = \sqrt{14}.


$$

This tells us precisely what $4x-12$ equals, and so we can replace it with this value wherever it appears.

Thus, substituting $\sqrt{14}$ in place of $4x-12$ in the second equation, we have

$$


\begin{aligned}(4𝑥−12)^{2} & =𝑦 \\ (\sqrt{√14})^{2} & =𝑦 \\ 14 & =𝑦\end{aligned}


$$

Therefore, $y = 14.$

The key steps of this approach are the following:

1. Identify a common expression.

2. Solve for the common expression in one equation.

3. Substitute its value into the other equation.

Let’s see some more examples.

### Example: Solving Nonlinear Systems by Substituting Expressions With One Variable

#### Question

$$


\begin{aligned}5𝑥−\frac{7}{11}=\sqrt{√3} \\ 𝑦=−2(\frac{7}{11}−5𝑥)^{2}\end{aligned}


$$

The solution to the given system of equations is the ordered pair $(x,y).$ What is the value of $y?$

#### Explanation

From the first equation, we have

$$


5x-\dfrac{7}{11}=\sqrt{3}.


$$

Notice that if we multiply this equation by $-1,$ we get

$$


\dfrac{7}{11} - 5x = -\sqrt{3},


$$

and the expression on the left-hand side features in the second equation.

So next, we substitute $-\sqrt{3}$ for $\left(\dfrac{7}{11}-5x\right)$ in the second equation:

$$


\begin{aligned}𝑦 & =−2(\frac{7}{11}−5𝑥)^{2} \\ & =−2(−\sqrt{√3})^{2} \\ & =−2⋅3 \\ 𝑦 & =−6\end{aligned}


$$

Therefore, the value of $y$ is $-6.$

### Solving Systems of Equations by Factoring

Sometimes, we can simplify nonlinear systems of equations by factoring the equations first. This can reveal a repeated structure that we can exploit to solve the system efficiently.

For example, consider the following system:

$$


\begin{aligned}𝑥^{2}−𝑦^{2}=15 \\ 𝑥+𝑦=5\end{aligned}


$$

Notice that we can factor the expression on the left-hand side of the first equation as a difference of squares:

$$


x^2-y^2=(x+y)(x-y)


$$

Thus, we can rewrite our system as follows:

$$


\begin{aligned}(𝑥+𝑦)(𝑥−𝑦)=15 \\ 𝑥+𝑦=5\end{aligned}


$$

Notice that the expression ${\color{blue}{x+y}}$ is common to both equations. Moreover, we know from the second equation that this equals ${\color{red}{5}}.$

So, substituting ${\color{blue}{x+y}}={\color{red}{5}}$ into the first equation gives

$$


\begin{aligned}(𝑥+𝑦)(𝑥−𝑦) & =15 \\ (5)(𝑥−𝑦) & =15 \\ 𝑥−𝑦 & =\frac{15}{5} \\ 𝑥−𝑦 & =3.\end{aligned}


$$

So, we now have the simpler, linear system:

$$


\begin{aligned}𝑥+𝑦=5 \\ 𝑥−𝑦=3\end{aligned}


$$

Here, adding the two equations gives the following:

$$


\begin{aligned}(𝑥+𝑦)+(𝑥−𝑦) & =5+3 \\ 2𝑥 & =8 \\ 𝑥 & =4\end{aligned}


$$

Finally, substituting $x=4$ into $x+y=5,$ we get

$$


(4)+y=5 \qquad \Longrightarrow \qquad y=1.


$$

Therefore, the solution is $(x,y)=(4,1).$

We see from this example that even for nonlinear systems, identifying algebraic structures such as a difference of squares can transform the problem into a simpler linear system that's easier to solve.

### Example: Solving Nonlinear Systems by Substituting Expressions With Two Variables

#### Question

$$


\begin{aligned}2𝑥−2𝑦=−6 \\ (𝑦−𝑥)(𝑥+𝑦)=15\end{aligned}


$$

The ordered pair $(x, y)$ is the solution to the above system of equations. What is the value of $x+y?$

#### Explanation

First, we write both equations of the given system in factored form:

$$


\begin{aligned}−2(𝑦−𝑥)=−6 \\ (𝑦−𝑥)(𝑥+𝑦)=15\end{aligned}


$$

Notice that $(y-x)$ is a common factor in both equations.

Now, we solve the first equation for $(y-x){:}$

$$


\begin{aligned}−2(𝑦−𝑥) & =−6 \\ 𝑦−𝑥 & =\frac{−6}{−2} \\ 𝑦−𝑥 & =3\end{aligned}


$$

Next, we substitute the result in the second equation:

$$


\begin{aligned}(𝑦−𝑥)(𝑥+𝑦) & =15 \\ (3)⋅(𝑥+𝑦) & =15 \\ 𝑥+𝑦 & =\frac{15}{3} \\ 𝑥+𝑦 & =5\end{aligned}


$$

Therefore, the value of $x+y$ is $5.$

### Example: Solving Nonlinear Systems by Recognizing Differences of Squares

#### Question

$$


\begin{aligned}4𝑥+8𝑦=32 \\ 4𝑦^{2}−𝑥^{2}=−32\end{aligned}


$$

The ordered pair $(x, y)$ is the solution to the above system of equations. What is the value of $y?$

#### Explanation

First, notice that $4y^2-x^2 = (2y)^2-x^2$ is a difference of squares, so we apply the difference of squares formula:

$$


(2y)^2-x^2=(2y+x)(2y-x)


$$

Thus, we write both equations of the given system in factored form:

$$


\begin{aligned}4(2𝑦+𝑥)=32 \\ (2𝑦+𝑥)(2𝑦−𝑥)=−32\end{aligned}


$$

Notice that $(2y+x)$ is a common factor in both equations.

Now, we solve the first equation for $(2y+x){:}$

$$


\begin{aligned}4(2𝑦+𝑥) & =32 \\ 2𝑦+𝑥 & =\frac{32}{4} \\ 2𝑦+𝑥 & =8\end{aligned}


$$

Next, we substitute the result in the second equation:

$$


\begin{aligned}(2𝑦+𝑥)(2𝑦−𝑥) & =−32 \\ 8⋅(2𝑦−𝑥) & =−32 \\ 2𝑦−𝑥 & =−4\end{aligned}


$$

Then, we get the following system with linear equations:

$$


\begin{aligned}2𝑦+𝑥=8 \\ 2𝑦−𝑥=−4\end{aligned}


$$

From the second equation, $x = 2y+4,$ which we substitute into the first equation:

$$


\begin{aligned}2𝑦+(2𝑦+4) & =8 \\ 4𝑦+4 & =8 \\ 4𝑦 & =4 \\ 𝑦 & =1\end{aligned}


$$

Therefore, the value of $y$ is $1.$
