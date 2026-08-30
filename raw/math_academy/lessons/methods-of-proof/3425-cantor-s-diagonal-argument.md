# Cantor's Diagonal Argument

Source: https://www.mathacademy.com/topics/3425?courseId=76
Topic ID: 3425

## Prerequisites

- [Proof by Contradiction](./3414-proof-by-contradiction.md)
- [Cardinality of the Natural Numbers, Integers, and Rationals](./4394-cardinality-of-the-natural-numbers-integers-and-rationals.md)
- [Continuous Infinite Sets With Equal Cardinality](./4860-continuous-infinite-sets-with-equal-cardinality.md)

## Lesson

### Introduction

Previously, we saw that the cardinality of the natural numbers $\mathbb N$ is defined as

$$


|\mathbb N| = \aleph_0.


$$

Moreover, any *countably infinite* set also has cardinality $\aleph_0.$ In particular,

$$


|\mathbb Z| = |\mathbb Q| = \aleph_0.


$$

This is true because bijections exist between $\mathbb N$ and $\mathbb Z,$ and $\mathbb N$ and $\mathbb Q.$ We've already seen how these bijections are constructed.

However, not all infinite sets have cardinality $\aleph_0.$ In particular, we have the following important result:

*The open interval $(0,1)$ of real numbers is uncountable.*

In other words, a bijection *does not exist* between $\mathbb N$ and $(0,1).$ We can prove this using **Cantor's diagonal argument,** which we'll discuss later in the lesson.

The fact that there is no bijection between $\mathbb N$ and $(0,1)$ tells us that although both sets are infinite, the set $(0,1)$ is, in some sense, "bigger" than $\mathbb N.$ We'll make these ideas more precise shortly.

The cardinality of $(0,1)$ is defined to be $\mathfrak{c},$ which stands for **continuum**:

$$


\big| (0,1) \big| = \mathfrak{c}


$$

Since we're able to construct bijections between other infinite sets and $(0,1),$ we can prove that many sets also have cardinality $\mathfrak{c}.$

For example:

- Since $f: (0,1) \to \mathbb R$ defined by $f(x) = \cot(\pi x)$ is a bijection from $(0,1)$ onto $\mathbb{R},$ we have

- Since $f: (0,1) \to \mathbb (a,b)$ defined by $f(x) = a + (b-a)x$ is a bijection from $(0,1)$ onto $(a,b),$ we have for any $a < b$ and $a,b \in \mathbb{R}.$

To summarize,

$$


\big| (0,1) \big| = \big| (a,b) \big| = | \mathbb{R} | = \mathfrak{c}.


$$

You may wish to make use of these results throughout this lesson.

### Example: Identifying Sets of Cardinality Continuum

#### Question

Consider the following sets.

$$


A = \{ x \in \mathbb{R} \mid |x| < 2 \}, \qquad B= (-3, \infty)


$$

Which of the following statements are true?

1. $|A| = \mathfrak{c}$

2. $|B| = \mathfrak{c}$

3. $|A| = |B|$

#### Explanation

Let's examine our statements in turn.

- Statement I is true. Solving the restricting inequality for $x,$ we get the following: As a result, $A = (-2, 2).$ Notice that the function $x \to 4x-2$ is a bijection that maps $(0,1)$ onto $(-2,2).$ So,

- Statement II is true. The function $x \to e^x-3$ is a bijection that maps $(-\infty, \infty)=\mathbb{R}$ onto $(-3, \infty).$ So,

- Statement III is true. Indeed, we have

Therefore, the correct answer is "I, II, and III."

### Cantor's Diagonal Argument

Let's now prove the theorem stated earlier:

*The open interval $(0,1)$ of real numbers is uncountable.*

We'll prove this by showing that a contradiction arises by assuming $(0,1)$ is countably infinite.

So, suppose there exists a bijection $f: \mathbb{N} \to (0,1)$ such that *all* the elements of $(0,1)$ can be listed in a sequence, as shown below.

Note that $a_{ij}$ denotes the digit in the $j$th decimal place for the $i$th number in our list.

Now, let's show that there is a number in $(0,1)$ that does not belong to this list. To do that, we consider the digits after the decimal point that lie on the "diagonal" of our list (denoted $\boxed{\color{blue}a_{ii}}$ for $i=1,2,3,\ldots).$

We define a new number $b = 0. b_1 b_2 \ldots b_n \ldots$ whose digits are selected from $\{1, 2 \}$ such that

$$


\begin{aligned}2, & if\,𝑎_{𝑖𝑖}=1 \\ 1, & if\,𝑎_{𝑖𝑖}≠1.\end{aligned}


$$

Now, notice that

- $b$ can't be the $1$st number on the list since $b_1 \neq a_{11},$

- $b$ can't be the $2$nd number on the list since $b_2 \neq a_{22},$

- $b$ can't be the $3$rd number on the list since $b_3 \neq a_{33},$

- $\cdots$

and so on. As a result, $b$ is *not* on the list, which is a contradiction! Hence, the assumption that there exists a bijection $f: \mathbb{N} \to (0,1)$ is false!

Therefore, we conclude that no bijection maps $\mathbb N$ onto $(0,1),$ and so $(0,1)$ is uncountable.

### Example: Applying Cantor's Diagonal Argument to Finite Lists

#### Question

Consider the set of four finite lists with elements from $A = \{\bigstar, \blacksquare, \clubsuit \},$ where we know only one element in each list, as shown below (here, $\ast$ can be any element from $A$).

$$


\begin{aligned}List 1: & ♣, & ∗, & ∗, & ∗ \\ List 2: & ∗, & ◼, & ∗, & ∗ \\ List 3: & ∗, & ∗, & ♣, & ∗ \\ List 4: & ∗, & ∗, & ∗, & ★\end{aligned}


$$

Construct a list that is guaranteed to be different from each of the given lists.

#### Explanation

Since we are given only one element per list and $\ast$ can be any symbol from $A,$ we will proceed as follows:

- The $1$st element in the $1$st list is $\clubsuit.$ If we want our new list to differ from this, we should ** choose $\clubsuit$ as its $1$st element. Let's take, for example, $\bigstar{:}$

- The $2$nd element in the $2$nd list is $\blacksquare.$ If we want our new list to differ from this, we should ** choose $\blacksquare$ as its $2$nd element. Let's take, for example, $\clubsuit{:}$

- The $3$rd element in the $3$rd list is $\clubsuit.$ If we want our new list to differ from this, we should ** choose $\clubsuit$ as its $3$rd element. Let's take, for example, $\blacksquare{:}$

- The $4$th element in the $4$th list is $\bigstar.$ If we want our new list to differ from this, we should ** choose $\bigstar$ as its $4$th element. Let's take, for example, $\clubsuit{:}$

As a result, we obtain the list

$$


\begin{aligned}★, & ♣, & ◼, & ♣\end{aligned}


$$

which is guaranteed to be different from each of the given lists above.

### Example: Proving Uncountability Using Cantor's Diagonal Argument

#### Question

Consider the infinite list of real decimal numbers from the interval $(1,2),$ as shown below.

$$


\begin{aligned}Number 1: & 1.𝑎_{11}𝑎_{12}…𝑎_{1𝑛}… \\ Number 2: & 1.𝑎_{21}𝑎_{22}…𝑎_{2𝑛}… \\ ⋮ & \,⋮ \\ Number n: & 1.𝑎_{𝑛1}𝑎_{𝑛2}…𝑎_{𝑛𝑛}… \\ ⋮ & \,⋮\end{aligned}


$$

Construct a new number from $(1,2)$ that is guaranteed to be different from each of the given numbers on the list.

#### Explanation

According to Cantor's diagonal argument, we consider the digits after the decimal point in the given numbers that lie on the "diagonal", as shown below.

$$


\begin{aligned}Number 1: & 1.𝑎_{11}𝑎_{12}…𝑎_{1𝑛}… \\ Number 2: & 1.𝑎_{21}𝑎_{22}…𝑎_{2𝑛}… \\ & \,⋮ \\ Number n: & 1.𝑎_{𝑛1}𝑎_{𝑛2}…𝑎_{𝑛𝑛}… \\ & \,⋮\end{aligned}


$$

We can define the new number $1. b_1 b_2\ldots b_n\ldots$ with digits after the decimal point from $\{4,5 \}$ such that

$$


\begin{aligned}4, & if\,𝑎_{𝑖𝑖}=5 \\ 5, & if\,𝑎_{𝑖𝑖}≠5.\end{aligned}


$$

This rule guarantees that the $i$th digit after the decimal point $b_i$ of the new number is not equal to the $i$th digit $a_{ii}$ of the $i$th number from the list.

Therefore, the obtained number differs from any other number on the list.
