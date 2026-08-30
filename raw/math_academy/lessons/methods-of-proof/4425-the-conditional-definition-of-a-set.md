# The Conditional Definition of a Set

Source: https://www.mathacademy.com/topics/4425?courseId=76
Topic ID: 4425

## Prerequisites

- [The Constructive Definition of a Set](./46-the-constructive-definition-of-a-set.md)
- [Statements and Predicates](./58-statements-and-predicates.md)
- [General Solutions of Elementary Trigonometric Equations](../integrated-math-iii-honors/1258-general-solutions-of-elementary-trigonometric-equations.md)

## Lesson

### Introduction

Another way of describing a set is to use a so-called **conditional definition**.

Consider the following set:

$$


A = \big\{n \in \mathbb{Z}: |3n-1|=2 \big\}


$$

This notation tells us that the elements of $A$ are the *integers* $(n\in\mathbb Z)$ that satisfy the absolute value equation

$$


|3n-1| = 2.


$$

To list the elements of this set, we start by solving this equation:

$$


\begin{aligned}|3𝑛−1| & =2 \\ 3𝑛−1 & =±2 \\ 3𝑛 & =1±2 \\ 𝑛 & =\frac{1±2}{3}\end{aligned}


$$

So, the solutions to our equation are $n=1$ and $n=-\dfrac13.$

We now inspect each solution to see which of them (if any) are elements of $A{:}$

- The solution $n=1$ is an integer. Hence, this solution *is* a member of $A.$

- The solution $n=-\dfrac13$ is *not* an integer. Hence, this solution is *not* a member of $A.$

Therefore, the set $A$ contains only one element.

Finally, listing all elements of $A,$ we have

$$


A = \{1\}.


$$

### Some Comments

Let's go back to our set, written using a conditional definition:

$$


A = \big\{n \in \mathbb{Z}: |3n-1|=2 \big\}


$$

Note the following:

- Under this definition, $n\in\mathbb Z$ describes the universal set for the type of mathematical object we're considering. In this case, the universal set is the set of integers.

- The condition $|3n-1| = 2$ is a predicate that defines the set's internal logic. Therefore, $A$ is the set of integers that give a true statement when substituted into the equation $|3n-1| = 2.$

- Note that $A$ itself is *not* a predicate but a set; therefore, it does not have a truth value.

- When a set is written using a conditional definition, the symbol "$:$" is read as "such that." So, in words, we can describe the set $A$ as follows: $\qquad$ *$A$ is the set of integers $n$ **** $|3n-1| = 2.$*

- The variable $n$ is a dummy variable. Its purpose is to describe the logic behind the set's definition and can be replaced with any other variable.

- An alternative to the "conditional definition of a set" terminology is to say the set is written using **set-builder notation**.

- Instead of using a "$:$" symbol to separate the universal set from its predicate, it's common to use the "$|$" symbol, as follows:

### Example: Sets Defined Using Linear Equations and Inequalities

#### Question

List the elements of the set $A = \{n \in \mathbb{N}: 5n - 2 \leq 21 \}.$

#### Explanation

The elements of the given set are the natural numbers that satisfy the inequality $5n - 2 \leq 21.$

So, we first need to solve our inequality for $n{:}$

$$


\begin{aligned}5𝑛−2 & ≤21 \\ 5𝑛 & ≤23 \\ 𝑛 & ≤\frac{23}{5}\end{aligned}


$$

The positive integer solutions of the inequality above are $1,2,3,4.$ Therefore, the given set can be written as

$$


A = \{1,2,3,4\}.


$$

### Example: Sets Defined Using Quadratic Equations and Inequalities

#### Question

List the elements of the set $A = \{x \in \mathbb{Z}: x^2 - 9 \lt 0\}.$

#### Explanation

The elements of the given set are the integers that satisfy the inequality $x^2 - 9 < 0.$

So, we first need to solve our inequality for $x{:}$

$$


\begin{aligned}𝑥^{2}−9 & <0 \\ 𝑥^{2} & <9 \\ \sqrt{√𝑥^{2}} & <\sqrt{√9} \\ |𝑥| & <3 \\ −3<𝑥 & <3\end{aligned}


$$

The integer solutions of the inequality above are $0,\pm1,\pm2.$ Therefore, the given set can be written as

$$


A = \{ 0, \pm 1, \pm 2\}.


$$

### Example: Sets Defined Using Absolute Value Equations and Inequalities

#### Question

List the elements of the set $A=\{k \in \mathbb{Z}: |k-1| \leq 4 \}.$

#### Explanation

The elements of the given set are the integers that satisfy the inequality $|k-1| \leq 4.$ So, we first need to solve for $k{:}$

$$


\begin{aligned}|𝑘−1|≤4 \\ −4≤𝑘−1≤4 \\ −3≤𝑘≤5\end{aligned}


$$

The integer solutions of the above inequality are $-3,-2,-1,0,1,2,3,4,5.$

Therefore, the given set can be written as

$$


A = \{0,\pm1,\pm2,\pm3,4,5 \}.


$$

### Example: Sets Defined Using Trigonometric Equations

#### Question

List the elements of the set $A = \left\{x\in \mathbb R \::\: \tan \left(\dfrac{\pi x}{2}\right) = 0 \right\}.$

#### Explanation

Notice that the solutions to the equation

$$


\tan \left(\dfrac{\pi x}{2}\right) = 0


$$

are given by

$$


\begin{aligned}\frac{𝜋𝑥}{2} & =𝑛𝜋 \\ 𝑥 & =2𝑛\end{aligned}


$$

where $n\in\mathbb Z.$

Substituting different values of $n,$ we see that the solutions are

$$


x = 0,\, \pm 2 ,\, \pm 4,\, \pm 6,\, \ldots


$$

Therefore, our set $A$ is equivalent to

$$


A= \{0,\, \pm 2 ,\, \pm 4,\, \pm 6,\, \ldots\}.


$$
