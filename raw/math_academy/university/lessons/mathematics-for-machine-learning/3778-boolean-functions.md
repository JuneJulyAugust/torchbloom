# Boolean Functions

Source: https://www.mathacademy.com/topics/3778?courseId=145
Topic ID: 3778

## Prerequisites

- [The Rules of Sum and Product](../../../high-school/traditional/lessons/geometry/161-the-rules-of-sum-and-product.md)
- [Sets and Functions](./3334-sets-and-functions.md)
- [The Maximum and Minimum of a Set](./4396-the-maximum-and-minimum-of-a-set.md)

## Lesson

### Introduction

A **Boolean function** of $n$ variables is a function whose variables are either $1$'s or $0$'s and whose value is either $0$ or $1;$ that is,

$$


f: \{0,1\}^n \to \{0,1\}.


$$

Since such functions have finite domains, they can be completely described using a **Boolean table** with $|\{0,1\}^n| = 2^n$ rows, one for each possible combination of the variables' values. For example, consider the function

$$


f(x_1,x_2) = \max\{ x_1,x_2 \}.


$$

Defining $f$ over the domain $\{0,1\}^2 = \{0,1\} \times \{0,1\},$ this is a Boolean function of two variables $x_1$ and $x_2,$ and there are $2^2=4$ possible combinations of the variables' values:

- If $x_1=0$ and $x_2=0,$ then

- If $x_1=0$ and $x_2=1,$ then

- If $x_1=1$ and $x_2=0,$ then

- If $x_1=1$ and $x_2=1,$ then

We create a table with a column for each variable and a column for the function's value, where each row represents a combination of the variables' values:

### Example: Representing Boolean Functions Using Tables

#### Question

Let $f$ be the Boolean function of three variables defined as

$$


\ f(x_1,x_2,x_3) = (x_1 + x_2 + x_3) \: \textrm{mod} \: 2.


$$

Complete the following table corresponding to $f.$

**

$$


\begin{aligned}0, & \,\,if x is even, \\ 1, & \,\,if x is odd.\end{aligned}


$$

#### Explanation

A Boolean function of $n$ variables $x_1,x_2,\ldots,x_n$ is a function of the the form $f: \{0,1\}^n \to \{0,1\}$ whose variables are either $1$'s or $0$'s and whose value is either $1$ or $0.$

In our case, we have a Boolean function of three variables $x_1,$ $x_2,$ and $x_3,$ so there are $8$ possible combinations of variables' values. Let's compute the missing ones from the table:

- If $x_1=0, x_2=0, x_3=0,$ then

- If $x_1=0, x_2=1, x_3=0,$ then

- If $x_1=1, x_2=0, x_3=0,$ then

- If $x_1=1, x_2=1, x_3=0,$ then

Therefore, we get the following table:

### Example: Representing Compositions of Boolean Functions Using Tables

#### Question

Let $f$ and $g$ be Boolean functions of three variables defined as

$$


\begin{aligned}𝑓(𝑥_{1},𝑥_{2},𝑥_{3}) & =max{𝑥_{1},𝑥_{2},𝑥_{3}}, \\ 𝑔(𝑥_{1},𝑥_{2},𝑥_{3}) & =(𝑥_{2}⋅𝑥_{3})^{𝑥_{1}+1}.\end{aligned}


$$

Complete the following table corresponding to the function $g(x_1,f(x_1,x_2,x_3),x_3).$

#### Explanation

A Boolean function of $n$ variables $x_1,x_2,x_3\ldots,x_n$ is a function of the the form $f: \{0,1\}^n \to \{0,1\}$ whose variables are either $1$'s or $0$'s and whose value is either $1$ or $0.$

First, we complete the table for $f(x_1,x_2,x_3)$ using the definition of the function:

Next, we complete the table for $g(x_1,f(x_1,x_2,x_3), x_3)$ using the definition of the function with inputs $x_1, x_2:= f(x_1,x_2,x_3),$ and $x_3,$ respectively:

### Number of Boolean Functions of N Variables

For a nonnegative integer $n,$ there are $2^{2^n}$ distinct Boolean functions of $n$ variables.

To see why, first note that a Boolean function $f: \{0,1\}^n \to \{0,1\}$ of $n$ variables can be uniquely represented by a Boolean table with a column for each variable and a column for the output, where each row represents a combination of the variables' values:

Therefore, the number of distinct Boolean functions of $n$ variables equals the number of distinct tables, one table for each function. Let's count the number of distinct tables.

- Each combination of our Boolean variables can be uniquely represented by a tuple of length $n{:}$

- Each coordinate of the tuple can only take one of $2$ possible values: $0$ or $1.$ Thus, by the combinatorial rule of product, there are possible combinations in total. As a result, each Boolean table has $2^n$ rows.

- Then, for each row of a table, the function's output can only be one of $2$ possible values: $0$ or $1.$ Therefore, by the combinatorial rule of product, there are distinct tables in total.

Therefore, there are $2^{2^n}$ possible Boolean functions of $n$ variables.

### Example: Finding the Number of Boolean Functions

#### Question

A Boolean table, such as the above, can uniquely represent a Boolean function $f$ of $3$ variables. Fill in the blanks for the reasoning about the number of Boolean functions on $3$ variables below.

Each combination of our Boolean variables can be uniquely represented by a tuple of length $𝑋𝑋$.

Now, each coordinate of the tuple can have one of $𝑋𝑋$ possible values. Thus, by the combinatorial rule of $𝑝𝑟𝑜𝑑𝑢𝑐𝑡$, there are $𝑋𝑋$ possible tuples in total.

As a result, our table has $𝑋𝑋$ rows. Here, each row contains one of $𝑋𝑋$ possible function values. Therefore, by the combinatorial rule of $𝑝𝑟𝑜𝑑𝑢𝑐𝑡$, there are $𝑋𝑋$ possible functions in total.

#### Explanation

We start by connecting the task of finding the number of functions to finding the number of possible tables (one table for each possible function).

Each combination of our Boolean variables can be uniquely represented by a tuple of length $\boxed{\color{blue}3}.$

We first need to determine the number of rows in a table to find the number of possible tables.

Now, each coordinate of the tuple can have one of $\boxed{\color{blue}2}$ possible values. Thus, by the combinatorial rule of $\boxed{\color{blue}\textrm{product}},$ there are $\boxed{\color{blue}2^{3}}$ possible tuples in total.

Notice that the number of tuples was computed as ${2 \cdot 2 \cdot 2}= 2^{3}.$

Finally, we find the number of possible tables.

As a result, our table has $\boxed{\color{blue}2^{3}}$ rows. Here, each row contains one of $\boxed{\color{blue}2}$ possible function values. Therefore, by the combinatorial rule of $\boxed{\color{blue}\textrm{product}},$ there are $\boxed{\color{blue}2^{2^3}}$ possible functions in total.

Notice that the number of tuples was computed as $2^{3}$

### Equivalent Boolean Functions

Two Boolean functions are **equivalent** if the corresponding truth tables for the functions are identical. To demonstrate, let's compare the truth tables for the functions $f(x_1,x_2) = x_1(1-x_2)+x_2$ and $g(x_1,x_2) = \max\{x_1,x_2\}.$

Filling out the truth table corresponding to $f(x_1,x_2),$ we get the following:

Similarly, the table corresponding to $g(x_1,x_2)$ is the following:

Notice that the outputs in each truth table are identical. Therefore, $f(x_1,x_2) = x_1(1-x_2)+x_2$ and $g(x_1,x_2) = \max\{x_1,x_2\}$ are equivalent.

### Example: Identifying Equivalent Boolean Functions

#### Question

Consider the following Boolean function:

$$


f(x_1,x_2) = x_1 \cdot x_2 .


$$

Which of the following boolean functions are equivalent to $f?$

1. $g_1(x_1,x_2) = \max\{x_1,x_2\}$

2. $g_2(x_1,x_2) = \min\{x_1,x_2\}$

3. $g_3(x_1,x_2) = (x_1 + x_2) \: \textrm{mod} \: 2$

**

$$


\begin{aligned}0, & \,\,if x is even, \\ 1, & \,\,if x is odd.\end{aligned}


$$

#### Explanation

Two Boolean functions are ** if the corresponding truth tables for the functions are identical.

First, we fill out the table corresponding to $f(x_1,x_2){:}$

The tables corresponding to $g_1,g_2$ and $g_3$ are the following:

Notice that the resulting column of $g_2$ is the same as that of $f.$ On the other hand, the resulting columns of $g_1$ and $g_3$ are not the same as for $f.$

Therefore, the correct answer is "II only."
