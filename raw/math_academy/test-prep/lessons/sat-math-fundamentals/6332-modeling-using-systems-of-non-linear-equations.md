# Modeling Using Systems of Non-Linear Equations

Source: https://www.mathacademy.com/topics/6332?courseId=120
Topic ID: 6332

## Prerequisites

- [Modeling Using Systems of Linear Equations](../../../high-school/traditional/lessons/algebra-i/890-modeling-using-systems-of-linear-equations.md)
- [Areas of Triangles](../../../middle-school/lessons/grade-7/1397-areas-of-triangles.md)
- [Finding Intersections of Lines and Quadratic Functions](../../../high-school/traditional/lessons/algebra-i/6341-finding-intersections-of-lines-and-quadratic-functions.md)

## Lesson

### Introduction

We can use systems of nonlinear equations to model and solve various algebra problems using a three-step process.

1. First, we name each quantity mentioned in the problem statement with a variable.

2. Then, we write one or more equations relating the variables.

3. Finally, we use our knowledge of systems of non-linear equations to solve these equations and answer the question.

For example, suppose the difference between two positive numbers is $29,$ and the larger number is $9$ more than the square of the smaller number. Let's find the values of these numbers by modeling this situation using a nonlinear system.

Let $x$ and $y$ be the two positive numbers, where $y$ is the larger number.

- Their difference is $29,$ so $y-x=29.$

- The larger is $9$ more than the square of the smaller, so $y=x^2+9.$

Putting these equations together, we have the following system of equations:

$$


\begin{aligned}𝑦−𝑥=29 \\ 𝑦=𝑥^{2}+9\end{aligned}


$$

We will solve the system using the substitution method. The second equation $y=x^2+9$ is already solved for $y,$ so we can substitute it into the first equation and solve for $x{:}$

$$


\begin{aligned}𝑦−𝑥 & =29 \\ (𝑥^{2}+9)−𝑥 & =29 \\ 𝑥^{2}−𝑥+9 & =29 \\ 𝑥^{2}−𝑥−20 & =0 \\ (𝑥−5)(𝑥+4) & =0.\end{aligned}


$$

Since the numbers are positive, we discard the negative solution. Hence, the only solution is $x=5.$

Finally, we can substitute $x=5$ back into the equation $y=x^2+9$ to solve for $y{:}$

$$


\begin{aligned}𝑦 & =𝑥^{2}+9 \\ & =5^{2}+9 \\ & =34\end{aligned}


$$

Therefore, the two numbers are $x=5$ and $y=34.$

### Example: Solving Number Problems Using Nonlinear Systems of Equations

#### Question

Two positive numbers add up to $21.$ The square of one of the numbers is $9$ less than three times the other. What are the two numbers?

#### Explanation

Let $x$ and $y$ be the two positive numbers.

- Their sum is $21,$ so $x+y=21.$

- The square of one is $9$ less than three times the other, so $x^2=3y-9.$

Putting these equations together, we have the following system of equations:

$$


\begin{aligned}𝑥+𝑦=21 \\ 𝑥^{2}=3𝑦−9\end{aligned}


$$

We will solve the system using substitution. We solve for $y$ in the first equation:

$$


\begin{aligned}𝑥+𝑦 & =21 \\ 𝑦 & =21−𝑥\end{aligned}


$$

Then, we can substitute $y=21-x$ into the second equation and solve for $x{:}$

$$


\begin{aligned}𝑥^{2} & =3(21−𝑥)−9 \\ 𝑥^{2} & =63−3𝑥−9 \\ 𝑥^{2} & =54−3𝑥 \\ 𝑥^{2}+3𝑥−54 & =0 \\ (𝑥+9)(𝑥−6) & =0.\end{aligned}


$$

Since the numbers are positive, we discard the negative solution. Hence, the only solution is $x=6.$

Finally, we can substitute $x=6$ back into the equation $y=21-x$ to solve for $y{:}$

$$


\begin{aligned}𝑦 & =21−𝑥 \\ & =21−6 \\ & =15\end{aligned}


$$

Therefore, the two numbers are $x=6$ and $y=15.$

### Example: Solving Area Problems Using Nonlinear Systems of Equations

#### Question

A rectangular field has an area of $230\,\textrm{m}^2.$ Twelve times its length is $36\,\textrm{m}$ more than twenty-four times its width. What is the width of the field?

#### Explanation

Let $w$ be the width and let $l$ be the length of the field.

- Twelve times its length is $36\,\textrm{m}$ more than twenty-four times its width, so $12l=24w+36.$

- The area is $230\,\textrm{m}^2,$ so $lw=230.$

Putting these equations together, we have the following system of equations:

$$


\begin{aligned}12𝑙=24𝑤+36 \\ 𝑙𝑤=230\end{aligned}


$$

We will solve the system using substitution. We solve for $l$ in the first equation:

$$


\begin{aligned}12𝑙 & =24𝑤+36 \\ \frac{12𝑙}{12} & =\frac{24𝑤+36}{12} \\ 𝑙 & =2𝑤+3\end{aligned}


$$

Then, we can substitute $l=2w+3$ into the second equation and solve for $w{:}$

$$


\begin{aligned}𝑙𝑤 & =230 \\ 𝑤(2𝑤+3) & =230 \\ 2𝑤^{2}+3𝑤−230 & =0\end{aligned}


$$

Applying the quadratic formula, we get

$$


\begin{aligned}𝑤 & =\frac{−3±\sqrt{√3^{2}−4(2)(−230)}}{2⋅2} \\ & =\frac{−3±\sqrt{√9+1,840}}{4} \\ & =\frac{−3±\sqrt{√1,849}}{4} \\ & =\frac{−3±43}{4}.\end{aligned}


$$

Since the width cannot be negative, we consider only the positive root:

$$


w=\dfrac{-3+43}{4}=\dfrac{40}{4}=10


$$

Therefore, the width of the field is $10\,\textrm{m}.$
