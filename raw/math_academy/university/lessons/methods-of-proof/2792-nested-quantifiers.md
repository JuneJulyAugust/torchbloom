# Nested Quantifiers

Source: https://www.mathacademy.com/topics/2792?courseId=76
Topic ID: 2792

## Prerequisites

- [Universal and Existential Quantifiers](./2787-universal-and-existential-quantifiers.md)

## Lesson

### Introduction

We can apply quantifiers to predicates with more than one variable.

For example, the statement

$$


\forall m \in \mathbb{N}, \, \exists n \in \mathbb{Z}, \, n > m


$$

reads as follows:

$\qquad$ *For all $m \in \mathbb{N},$ there exists $n \in \mathbb{Z}$ such that $n > m.$*

This statement is true. Informally, it states that given *any* natural number ${\color{blue}{m}},$ there is an integer ${\color{red}{n}}$ that's larger than ${\color{blue}{m}}.$

- If ${\color{blue}{m}}={\color{blue}{1}}\in \mathbb N$ and we select ${\color{red}{n}}={\color{red}{2}}\in \mathbb Z,$ we have ${\color{red}{2}} > {\color{blue}{1}}$ which is true. $\quad{\color{green}{\checkmark}}$

- If ${\color{blue}{m}}={\color{blue}{2}}\in \mathbb N$ and we select ${\color{red}{n}}={\color{red}{3}}\in \mathbb Z,$ we have ${\color{red}{3}} > {\color{blue}{2}}$ which is true. $\quad{\color{green}{\checkmark}}$

- If ${\color{blue}{m}}={\color{blue}{3}}\in \mathbb N$ and we select ${\color{red}{n}}={\color{red}{4}}\in \mathbb Z,$ we have ${\color{red}{4}} > {\color{blue}{3}}$ which is true. $\quad{\color{green}{\checkmark}}$

And so on. It's easy to see that this statement is true since for any $m\in\mathbb N,$ we can simply select $n = m+1,$ and thus $n > m.$

**Watch out!** The order in which the quantifiers are stated is very important. If we swap the quantifiers in this example, we get

$$


\exists n \in \mathbb{Z}, \, \forall m \in \mathbb{N}, \, n > m


$$

which reads as follows:

$\qquad$ *There exists $n \in \mathbb{Z}$ such that for all $m \in \mathbb{N},$ $n > m.$*

This new statement has an entirely different meaning! Informally, it states that there is an integer $n$ that's larger than *every* natural number, which is false!

However, quantifiers *of the same type* can be swapped. For example,

$$


\exists m \in \mathbb{N}, \, \exists n \in \mathbb{Z}, \, n > m \: \equiv \: \exists n \in \mathbb{Z}, \, \exists m \in \mathbb{N}, \, n > m.


$$

Finally, if we have two or more quantifiers of the same type defined over the same domain, we can write only one quantifier followed by the corresponding variables.

For example, the (false) statement

$$


\forall x \in \mathbb{R}, \, \forall y \in \mathbb{R}, \, x \leq y


$$

can be written more compactly as

$$


\forall \, x,y \in \mathbb{R}, \, x \leq y.


$$

Similarly, the (true) statement

$$


\begin{aligned}∃𝑥∈ℝ,\,∃𝑦∈ℝ,\,𝑥≤𝑦\end{aligned}


$$

can be written as

$$


\exists \, x,y \in \mathbb{R}, \, x \leq y.


$$

We'll learn more about determining the truth value of a statement containing multiple quantifiers later in the lesson.

### Example: Translating Statements Involving Nested Quantifiers

#### Question

Express the following statement in words.

$\qquad$ $\forall \, x \in \mathbb{R}^+,\,\exists \, a \in \mathbb{R},\, a^2 =x.$

#### Explanation

Our quantified statement reads as follows:

$\qquad$ **** $x \in \mathbb{R}^+,$ **** $a \in \mathbb{R}$ **** $a^2=x.$

This can be re-phrased as follows:

$\qquad$ For every positive real number $x$ there is a real number $a$ such that $a^2=x.$

### The Scope of a Quantifier

Consider the following quantified expression

$$


\exists y \in \mathbb{N} \big( \, x > 0 \Rightarrow \forall x \in \mathbb{R}, y < 10 \, \big)


$$

This expression has two quantifiers. The **scope** of each quantifier is the range in the expression where the quantifier is applied. We can use parentheses to avoid ambiguity in complex expressions.

In this example, the scope of the quantifier $\boxed{\exists y}$ is the following:

$$


∃𝑦


$$

and the scope of $\boxed{\forall x}$ is the following:

$$


∀𝑥


$$

### Free and Bound Occurrences of Variables

The occurrence of a variable is called **bound** if it is placed right next to a quantifier or lies within the scope of a quantifier that uses the same variable. Otherwise, the occurrence is called **free**.

For example, let's examine the occurrences of variables in the following statement:

$$


\exists y \in \mathbb{N} \big( \, x > 0 \Rightarrow \forall x \in \mathbb{R}, y < 10 \, \big).


$$

- The following occurrence of $y$ is *bound* since it is placed right next to the quantifier $\boxed{\exists}{:}$

- The following occurrence of $x$ is *free* since it isn't placed right next to a quantifier and it doesn't lie within the scope of a quantifier that uses $x{:}$

- The following occurrence of $x$ is *bound* since it is placed right next to the quantifier $\boxed{\forall}{:}$

- The following occurrence of $y$ is *bound* since it lies within the scope of the quantifier $\exists y$ that uses $y{:}$

So, in our expression, we have:

- two occurrences of $y,$ both of which are bound, and

- two occurrences of $x,$ where one is free, and another is bound.

$$


\exists \boxed{y} \in \mathbb{N} \big( \, \boxed{x} > 0 \Rightarrow \big( \, \forall \boxed{x} \in \mathbb{R}, \boxed{y} < 10 \, \big) \, \big)


$$

Distinguishing between free and bound occurrences is important since we are allowed to substitute values into free occurrences of variables. In particular, since the first occurrence of $\boxed{x}$ is free, we can substitute concrete values for this variable (but not for the other occurrence of $\boxed{x}$).

Therefore, the above expression can be viewed as a predicate of one variable ($\boxed{x}$) since all occurrences of $y$ are bound.

### Example: Identifying Free and Bound Occurrences of Variables

#### Question

$$


\big( \, \forall \underset{\substack{\phantom{.} \\[4pt] \uparrow \\[6pt] \large\text{I}}}{x} \in \mathbb{R}, \, {x} > 1 \, \big) \Rightarrow \big( \, \exists {y} \in [0, 2\pi), \, \! \underset{\substack{\phantom{.} \\[4pt] \uparrow \\[6pt] \large\text{II}}}{x} \! \cos\!\!{\underset{\substack{\phantom{.} \\[2pt] \uparrow \\[6pt] \large\text{III}}}{y}} \!=1 \, \big)


$$

Which occurrences of the variables in the expression above are free?

#### Explanation

Let's examine our expression and mark the occurrences of the variables as bound $(\boxed{\small\text{b}})$ or free $(\boxed{\small\text{f}}).$

- Occurrence I of the variable $x$ is ** since it is placed right next to the quantifier $\boxed{\forall}{:}$

- Occurrence II of the variable $x$ is ** since it isn't placed right next to a quantifier and it doesn't lie within the scope of a quantifier that uses $x.$

- Occurrence III of the variable $y$ is ** since it lies within the scope of the quantifier $\exists y$ that uses $y{:}$

The occurrences of variables in the expression are as follows:

$$


\big( \, {\forall} \!\! \underset{\substack{\phantom{.} \\[4pt] \uparrow \\[6pt] \large\phantom{.}\boxed{\text{b}}}}{x} \!\! \in \mathbb{R}, \, \!\! \underset{\substack{\phantom{.} \\[4pt] \uparrow \\[6pt] \large\phantom{.}\boxed{\text{b}}}}{x} \!\! > 1 \, \big) \Rightarrow \big( \, {\exists} \!\! \underset{\substack{\phantom{.} \\[4pt] \uparrow \\[6pt] \large\phantom{.}\boxed{\text{b}}}}{y} \!\! \in [0, 2\pi), \, \!\! \underset{\substack{\phantom{.} \\[4pt] \uparrow \\[6pt] \large\phantom{.}\boxed{\text{f}}}}{x} \!\! \cos \!\!\!\underset{\substack{\phantom{.} \\[4pt] \uparrow \\[6pt] \large\phantom{.}\boxed{\text{b}}}}{y}\! =1\, \big)


$$

Therefore, the free occurrence is "II only."

### The Truth Value of a Statement Involving Nested Quantifiers

Consider the statement

$$


\forall\, m \in \mathbb{N}, \, \forall\, n \in \mathbb{N}, \, m > n


$$

that reads as follows:

$\qquad$ For all natural $m$ and $n,$ we have $m > n.$

Is the statement true or false? To figure this out, we proceed as described below.

First, let's write down the inner predicate and determine its truth set:

$$


P(m): \quad \forall\, n \in \mathbb{N}, \, m > n.


$$

Notice that this is a predicate in the variable $m$ since $m$ is a free variable in the $P(m)$ statement.

The predicate $P(m)$ is false for all values $m \in \mathbb {N}.$ For example,

$$


P(1) : \quad \forall\, n \in \mathbb{N}, \, 1 > n


$$

is false since we can take $n=1.$ Similarly,

$$


P(2): \quad \forall\, n \in \mathbb{N}, \, 2 > n


$$

is false, since we can take $n=2.$ In general, it's sufficient to take $n=m$ for any value of $m.$ As a result, the truth set of $P(m)$ is $T_P=\emptyset.$

Now, notice that we can write our original statement as follows:

$$


\forall\, m \in \mathbb{N}, \, \forall\, n \in \mathbb{N}, \, m > n \: \equiv \: \forall m \in \mathbb{N}, \, P(m).


$$

This statement is true whenever the *inner* predicate $P(m)$ is true over the universal set $\mathbb N.$ However, this is not the case, as we discovered above.

Therefore, the statement $\forall\, m \in \mathbb{N}, \, \forall\, n \in \mathbb{N}, \, m > n$ is false.

### Example: Finding the Truth Value of a Statement Involving Nested Quantifiers

#### Question

Which of the following statements are true?

1. $\exists \, y \in \mathbb{R}, \, 2+y=0.$

2. The truth set of the predicate $\big(\, \exists y \in \mathbb{R}, \, x+y = 0 \, \big)$ is $\mathbb{R}.$

3. $\forall\, x \in \mathbb{R}, \, \exists y \in \mathbb{R}, \, x+y=0.$

#### Explanation

First, notice that the statement

$$


\forall\, x \in \mathbb{R}, \, \exists y \in \mathbb{R}, \, x+y=0


$$

from option III reads as follows:

$\qquad$ For every real $x$ there exists real $y$ such that $x+y=0.$

With that in mind, let's examine our statements in turn.

- Statement I is true since $2+y=0$ for some real number $y$ (e.g., for $y=-2$).

- Statement II is true. The predicate is true for any real $x.$ For example, is true since we can take $y=-1.$ Similarly, is true since we can take $y=-2.$ And so on. In general, it's sufficient to take $y=-x.$

- Statement III is true. The sentence can be written as which is true whenever the inner predicate $P(x)$ is true over the universal set $\mathbb R.$ And, according to statement II, this is the case.

Therefore, the correct answer is "I, II, and III."
