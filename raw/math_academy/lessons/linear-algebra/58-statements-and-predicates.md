# Statements and Predicates

Source: https://www.mathacademy.com/topics/58?courseId=55
Topic ID: 58

## Prerequisites

- [Special Sets](./47-special-sets.md)
- [Prime and Composite Numbers](../grade-4/840-prime-and-composite-numbers.md)
- [Classifying Quadrilaterals](../grade-7/1459-classifying-quadrilaterals.md)
- [The Union of Sets](../geometry/2826-the-union-of-sets.md)
- [The Intersection of Sets](../geometry/2827-the-intersection-of-sets.md)

## Lesson

### Introduction

A **mathematical statement** is a sentence or mathematical expression that is either **true** or **false**.

For example:

- The sentence, "The sum of $1$ and $2$ is $3$" is a mathematical statement because it is *true.*

- Likewise, "$2+2=5$" is a mathematical statement because it is *false.*

The following examples are *not* mathematical statements:

- "Find the sum of $1$ and $2$" is *not* a mathematical statement because it is neither true nor false. It is an instruction.

- "What is the sum of $1$ and $2?$" is *not* a mathematical statement because it is neither true nor false. It is a question.

- Similarly, "$6+9$" is *not* a mathematical statement because it is neither true nor false.

We often use upper-case letters such as $P, Q,$ and $R$ to represent statements. For example:

- $P:$ The sum of two even integers is odd.

- $Q: 3 \in \mathbb Z$

- $R: \{2,4,6\ldots\}\cup \{1,3,5,\ldots\} = \mathbb N$

In this case, the statements $Q$ and $R$ are true, whereas statement $P$ is false.

### Example: Determining the Truth Value of a Statement

#### Question

Which of the following statements are true?

- $P:$ $4$ is a positive number.

- $Q:$ $2^3$ is a natural number.

- $R:$ $-4 \geq 2$

#### Explanation

A mathematical statement is a sentence or mathematical expression that is either true or false.

With that in mind, let's evaluate the truth value of each statement:

- Statement $P$ is ** Indeed, $4$ is a positive number.

- Statement $Q$ is ** Indeed, $2^3=8$ is a natural number.

- Statement $R$ is ** because $-4 \ngeq 2$.

Therefore, the correct answer is "$P$ and $Q$ only."

### Example: Identifying Mathematical Statements

#### Question

Which of the following are mathematical statements?

- $P$: Compute the product of the first four prime numbers.

- $Q$: Four is a prime number.

- $R$: Is four a prime number?

#### Explanation

A mathematical statement is a sentence or mathematical expression that is either true or false.

With that in mind, let's examine the given options:

- $P$ is ** a statement because it is neither true nor false. Rather, it is an instruction.

- $Q$ is a statement. This statement is ** because $4$ is not a prime number (it is divisible by $2$).

- $R$ is ** a statement because it is neither true nor false. Rather, it is a question, and the possible answers are "yes" or "no."

Therefore, the correct answer is "$Q$ only."

### Divisibility Notation

Before we continue, we need a brief discussion on the concept of **integer divisibility.**

Suppose $a$ and $b$ are integers. We write $a \mid b$ to mean that $\boldsymbol a$ **divides** $\boldsymbol b.$ Informally, this means the quotient of $\dfrac b a$ is an *integer*, and there is *no remainder*.

For example, consider the following statement:

$$


5 \,|\, 20


$$

This statement reads, "$5$ divides $20$". Moreover, this is a *true* statement because $20\div 5 = 4$ is an integer.

Now consider the following statement:

$$


6\, |\, 20


$$

This statement is *false* because $20\div 6 = 3 {\color{blue}{\dfrac13}},$ which is *not* an integer. The correct statement is

$$


6 \! \not | \: 20.


$$

This statement reads, "$6$ does not divide $20$".

For now, this is all we need to understand the notation $a\mid b.$ More formal discussions on integer divisibility will be given in future lessons.

### Example: Identifying Statements Expressed Using Symbols

#### Question

Which of the following are mathematical statements?

- $P: \{5,6,7\}\cap \{6,8,10\} = \{6\}$

- $Q: \sqrt{3} +2$

- $R: 4\mid 2$

****: The notation

$$


a\mid b


$$

means "$a$ divides $b.$" This is equivalent to the statement that $b$ is divisible by $a.$

#### Explanation

A mathematical statement is a sentence or mathematical expression that is either true or false.

With that in mind, let's examine the given options:

- $P$ is a statement. This statement is ** because the intersection of the given sets is indeed the set $\{6\}.$

- $Q$ is ** a statement because it is neither true nor false.

- $R$ is a statement. This statement is ** because $4$ does not divide $2$ (i.e., $2$ is not divisible by $4$).

Therefore, the correct answer is "$P$ and $R$ only."

### Predicates

A **predicate** (or **open sentence**) of one variable is a sentence that contains a variable defined on some *universal set* and has the property that when we substitute a concrete value of the variable into the predicate, the result becomes a mathematical statement that is either *true* or *false*.

For example, consider the following predicate:

$x > 1$

This is a predicate because substituting concrete values for $x$ gives a mathematical statement.

For instance:

- Substituting $x=2$ gives the *true* statement "$2 > 1$"

- Substituting $x=5$ gives the *true* statement "$5 > 1$"

- Substituting $x=0$ gives the *false* statement "$0 > 1$"

We denote predicates using capital letters and the corresponding variable in parentheses. In this example, we can write our predicate more formally as follows:

$P(x):$ $x > 1$

Any predicate must be defined with its **universal set,** which is the set from which we are allowed to pull the concrete values of the variable. So, we could state our predicate more formally as

$P(x):$ $x > 1,$ $\quad$ where $x \in \mathbb{R}.$

The universal set can often be identified from the context and doesn't need to be explicitly stated. For example, if we have the predicate

$n$ is divisible by 5,

we can assume that $n$ is defined on the set of all integers, i.e., $n \in \mathbb{Z}.$

In math, *any equation or inequality is a predicate*. However, a sentence containing a variable is not necessarily a predicate. For example, the sentence

$\qquad$ "What is the sign of $y?$"

is *not* a predicate because substituting a concrete value for $y$ does not give a mathematical statement. Instead, it gives a question.

Similarly,

$z^2-5$

is *not* a predicate either. It's just an expression.

### Example: Identifying Predicates

#### Question

Which of the following are mathematical predicates of one variable?

1. Subtract $x$ from $10.$

2. $y^2 -2 \leq 3$

3. $1+z$ is a perfect square.

#### Explanation

A ** of one variable is a sentence that contains the variable defined on some ** and has the property that when we substitute any concrete value of the variable into the predicate, the result becomes a statement that is either true or false.

With that in mind, let's examine our options.

- Option I is ** a predicate. Substituting a concrete value for $x$ into the sentence, we do not get a statement that is either true or false. Rather, it gives an instruction.

- Option II is a predicate. Substituting a concrete value for $y$ into the sentence, we get a statement that is either true or false.

- Option III is a predicate. Substituting a concrete value for $z$ into the sentence, we get a statement that is either true or false.

Therefore, the correct answer is "II and III only."
