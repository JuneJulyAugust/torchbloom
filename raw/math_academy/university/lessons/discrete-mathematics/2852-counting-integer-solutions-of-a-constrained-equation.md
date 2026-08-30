# Counting Integer Solutions of a Constrained Equation

Source: https://www.mathacademy.com/topics/2852?courseId=109
Topic ID: 2852

## Prerequisites

- [The Inclusion-Exclusion Principle](./1344-the-inclusion-exclusion-principle.md)

## Lesson

### Introduction

Consider the equation $x + y =10.$ How many solutions does it have in the non-negative integers with

$$



x < 8 \quad \textbf{and} \quad y < 9?



$$

We know that $x$ must be an integer between $0$ and $10,$ and rearranging the equation, we know that

$$



y=10-x.



$$

So, we can list out all the possibilities for $x$ in a line and then write the corresponding value of $y$ below.

$$



\begin{aligned}𝑥 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\ 𝑦 & 10 & 9 & 8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 & 0\end{aligned}



$$

As we can see, there are $6$ solutions (marked in blue) such that $x < 8$ and $y < 9.$

**Note:** Sometimes, we may have to count up many solutions. To do that, it's helpful to remember that the number of integers between $a$ and $b$ inclusive is given by

$$



b-a+1.



$$

In our case, there is one solution for each value of $x$ between $2$ and $7$ inclusive, which means there are

$$



7-2+1=6



$$

solutions in total.

### Example: Counting Positive Integer Solutions Using a Two-Line Format with Dots

#### Question

How many solutions does the equation $x + y =28$ have in the non-negative integers with

$$



x \leq 12 \quad \textbf{or} \quad y > 12?



$$

#### Explanation

We know that $x$ must be an integer between $0$ and $28.$ Rearranging the equation, we get

$$



y=28-x.



$$

We can list out all the possibilities for $x$ in a line and then write the corresponding value of $y$ below.

$$



\begin{aligned}𝑥 & 0 & ⋯ & 12 & 13 & ⋯ & 15 & 16 & ⋯ & 28 \\ 𝑦 & 28 & ⋯ & 16 & 15 & ⋯ & 13 & 12 & ⋯ & 0\end{aligned}



$$

The solutions are marked in blue. There is one solution for each value of $x$ between $0$ and $15$ inclusive, which means there are

$$



15-0+1=16



$$

solutions in total.

### Example: Counting Positive Integer Solutions Using Combinations with Repetition: No Constraint

#### Question

How many solutions does the equation $x + y + z=11$ have in the non-negative integers?

#### Explanation

Let $X$ be the set of solutions of $x + y +z =11$ in the non-negative integers. We can present this equation in the form

$$



\underbrace{1+1+\cdots +1}_{x}+\underbrace{1+1+\cdots +1}_{y}+\underbrace{1+1+\cdots +1}_{z}=11.



$$

The problem of finding the number of solutions is analogous to finding the number of ways to distribute $11$ identical balls (the $1$'s) into $3$ boxes ($x,$ $y,$ and $z$). So, the number of solutions is

$$



\begin{aligned}|𝑋| & =(\frac{11+3−1}{11}) \\ & =(\frac{13}{11}) \\ & =\frac{13!}{11!2!} \\ & =78.\end{aligned}



$$

### Example: Counting Positive Integer Solutions Using Combinations with Repetition: Constraint

#### Question

How many solutions does the equation $x + y + z=20$ have in the non-negative integers with $x \geq 9?$

#### Explanation

First, we create an equivalent equation without a constraint. To do that, we substitute $x=9+x',$ where $x'$ is a non-negative integer. Then the equation becomes

$$



\begin{aligned}𝑥+𝑦+𝑧 & =20 \\ (9+𝑥^{′})+𝑦+𝑧 & =20 \\ 𝑥^{′}+𝑦+𝑧 & =11.\end{aligned}



$$

Now, we can carry on as usual. Let $X$ be the set of solutions of $x' + y +z =11$ in the non-negative integers. We can present this equation in the form

$$



\underbrace{1+1+\cdots +1}_{x'}+\underbrace{1+1+\cdots +1}_{y}+\underbrace{1+1+\cdots +1}_{z}=11.



$$

The problem of finding the number of solutions is analogous to finding the number of ways to distribute $11$ identical balls (the $1$'s) into $3$ boxes ($x',$ $y,$ and $z$). So, the number of solutions is

$$



\begin{aligned}|𝑋| & =(\frac{11+3−1}{11}) \\ & =(\frac{13}{11}) \\ & =\frac{13!}{11!2!} \\ & =78.\end{aligned}



$$

### Example: Counting Positive Integer Solutions Using the Inclusion-Exclusion Principle

#### Question

How many solutions does the equation $x + y + z = 16$ have in the non-negative integers with $x > 9$ **** $y \geq 7?$

#### Explanation

Let $A$ be the set of solutions in the non-negative integers with $x > 9$ and let $B$ be the set of solutions in the non-negative integers with $y \geq 7.$ Then the number of solutions where $x > 9$ or $y \geq 7$ corresponds to $|A \cup B|,$ and we can compute this using the inclusion-exclusion principle:

$$



|A\cup B| = |A| + |B| - |A\cap B|



$$

- To compute $|A|,$ we need to count the number of solutions in the non-negative integers such that $x > 9,$ or equivalently, $x \geq 10.$ To do this, we can replace $x=10+x',$ where $x'$ is a non-negative integer, which gives So, the number of solutions in $A$ is equal to the number of non-negative integer solutions of the equation above, which is given by

- To compute $|B|,$ we apply the same procedure. We replace $y=7+y'$ to get the equation and the number of solutions of this equation is given by

- To compute $|A\cap B|,$ we need to find the number of solutions in the non-negative integers such that both $x > 9$ and $y \geq 7.$ So, we replace both $x=10+x'$ and $y=7+y'$ and get which permits no non-negative integer solutions. This tells us that $|A \cap B| = 0.$

Finally, according to the inclusion-exclusion principle, we have

$$



\begin{aligned}|𝐴∪𝐵| & =|𝐴|+|𝐵|−|𝐴∩𝐵| \\ & =28+55−0 \\ & =83.\end{aligned}



$$

Therefore, there are $83$ solutions in the non-negative integers with $x > 9$ or $y \geq 7.$

### Example: Counting Positive Integer Solutions Using the Inclusion-Exclusion Principle and Subtraction

#### Question

How many solutions does the equation $x + y + z = 17$ have in the non-negative integers with $x \leq 10$ **** $y \leq 12?$

#### Explanation

Let $X$ be the set of solutions of $x + y + z = 17$ in the non-negative integers (without restriction). The number of solutions is given by

$$



\begin{aligned}|𝑋| & =(\frac{17+3−1}{17})=\frac{19!}{17!2!}=171.\end{aligned}



$$

However, we only want to count the solutions in the non-negative integers with $x \leq 10$ and $y \leq 12.$ So, we need to subtract the number of solutions where $x > 10$ or $y > 12.$

Let $A$ be the set of solutions in the non-negative integers with $x > 10$ and let $B$ be the set of solutions in the non-negative integers with $y > 12.$ Then the number of solutions where $x > 10$ or $y > 12$ corresponds to $|A \cup B|,$ and we can compute this using the inclusion-exclusion principle:

$$



|A\cup B| = |A| + |B| - |A\cap B|



$$

- To compute $|A|,$ we need to count the number of solutions in the non-negative integers such that $x > 10,$ or equivalently, $x \geq 11.$ To do this, we can replace $x=11+x',$ where $x'$ is a non-negative integer, which gives So, the number of solutions in $A$ is equal to the number of non-negative integer solutions of the equation above, which is given by

- To compute $|B|,$ we apply the same procedure. We replace $y=13+y'$ to get the equation and the number of solutions of this equation is given by

- To compute $|A\cap B|,$ we need to find the number of solutions in the non-negative integers such that both $x > 10$ and $y > 12.$ So, we replace both $x=11+x'$ and $y=13+y'$ and get which permits no non-negative integer solutions. This tells us that $|A \cap B| = 0.$

Finally, according to the inclusion-exclusion principle, we have

$$



\begin{aligned}|𝐴∪𝐵| & =|𝐴|+|𝐵|−|𝐴∩𝐵| \\ & =28+15−0 \\ & =43,\end{aligned}



$$

and the number of solutions in the non-negative integers with $x \leq 10$ and $y \leq 12$ is given by

$$



|X|-|A\cup B|=171 - 43 =128.



$$
