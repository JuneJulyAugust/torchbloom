# Truth-Preserving Boolean Functions

Source: https://www.mathacademy.com/topics/3783?courseId=109
Topic ID: 3783

## Prerequisites

- [Boolean Functions And Logical Operations](./3779-boolean-functions-and-logical-operations.md)

## Lesson

### Introduction

A Boolean function is **truth-preserving** if it returns $1$ when all its variables are assigned a value of $1.$ Similarly, a Boolean function is **falsity-preserving** if it returns $0$ when all its variables are assigned a value of $0.$

Consider the Boolean function given by its table below.

Looking at the $4$th row of the table, we have $f(1,1) =0.$ Since $f\big(1, 1\big) \neq 1,$ the function is *not* truth-preserving.

On the other hand, by the $1$st row of the table, we have $f(0,0) =0.$ So, the function is falsity-preserving.

### Example: Classifying Boolean Functions Given Tables

#### Question

Consider the Boolean function given by its table above. Determine whether the function is truth preserving or falsity-preserving.

#### Explanation

A Boolean function (logical operation) is truth-preserving if it returns $1$ (true) when all its variables are assigned a value of $1$ (true).

With that in mind, let's consider the $8$th row of the table.

Since $f(1,1,1) =1,$ the function is truth-preserving.

A Boolean function (logical operation) is falsity-preserving if it returns $0$ (false) when all its variables are assigned a value of $0$ (false).

With that in mind, let's consider the $1$st row of the table.

Since $f(0,0,0)=0,$ the function is falsity-preserving.

### Example: Identifying Truth-Preserving Boolean Functions

#### Question

Which of the following Boolean functions are truth-preserving?

1. $f(x_1) \equiv \min\{x_1^2, \overline{x_1}\}$

2. $g(x_1,x_2) \equiv x_1 \cdot x_2$

3. $h(x_1,x_2,x_3) \equiv (x_1 \Rightarrow \overline{x_2}) \land x_3$

#### Explanation

A Boolean function (logical operation) is truth-preserving if it returns $1$ (true) when all its variables are assigned a value of $1$ (true).

With that in mind, let's examine our functions.

- Function I is ** truth-preserving since substituting $x_1=1$ does not give a value of $1{:}$

- Function II is truth-preserving since substituting $x_1=x_2=1$ gives a value of $1{:}$

- Function III is ** truth-preserving. Indeed, substituting $x_1=x_2=x_3=1$ does not give a value of $1{:}$

Therefore, the correct answer is "II only."

### Example: Identifying Falsity-Preserving Boolean Functions

#### Question

Which of the following Boolean functions are falsity-preserving?

1. $f(x_1) \equiv \max\{x_1,\overline{x_1}\}$

2. $g(x_1,x_2) \equiv \overline{x_1 \Rightarrow x_2}$

3. $h(x_1,x_2,x_3) \equiv \min\{x_1,x_2\} \lor x_3$

#### Explanation

A Boolean function (logical operation) is falsity-preserving if it returns $0$ (false) when all its variables are assigned a value of $0$ (false).

With that in mind, let's examine our functions.

- Function I is ** falsity-preserving since substituting $x_1=0$ does not give a value of $0{:}$

- Function II is falsity-preserving since substituting $x_1=x_2=0$ gives a value of $0{:}$

- Function III is falsity-preserving. Indeed, substituting $x_1=x_2=x_3=0$ gives a value of $0{:}$

Therefore, the correct answer is "II and III only."

### Properties of Truth-Preserving and Falsity-Preserving Boolean Functions

Truth-preserving functions are closed under composition; this is, the composition of truth-preserving functions is a truth-preserving function.

To see why, let $g$ and $h_1, \ldots, h_n$ be truth-preserving functions on the Boolean variables $(x_1,\ldots,x_n).$ By definition, we have

$$



g(1,1,\ldots,1) = 1 \qquad\text{and}\qquad h_i(1,1,\ldots,1) = 1 \:\:\:\text{for}\:\: i \in \{1,2,\ldots,n\}.



$$

Define $f$ to be the composition $f \equiv g(h_1, \ldots, h_n).$ Then, assigning the variables a value of $1,$ we get

$$



\begin{aligned}𝑓(1,1,…,1) & ≡𝑔(ℎ_{1}(1,1,…,1),…,ℎ_{𝑛}(1,1,…,1)) \\ & ≡𝑔(1,1,…,1) \\ & ≡1.\end{aligned}



$$

Therefore, $f \equiv g(h_1, \ldots, h_n)$ is a truth-preserving function.

Similarly, falsity-preserving functions are closed under composition, a result that can be justified using a method analogous to the one outlined above for truth-preserving functions.
