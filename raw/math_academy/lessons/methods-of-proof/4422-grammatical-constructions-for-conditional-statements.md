# Grammatical Constructions for Conditional Statements

Source: https://www.mathacademy.com/topics/4422?courseId=76
Topic ID: 4422

## Prerequisites

- [Converse, Inverse, and Contrapositive](./252-converse-inverse-and-contrapositive.md)
- [Necessary and Sufficient Conditions](./2793-necessary-and-sufficient-conditions.md)

## Lesson

### Introduction

Up to now, we've seen several grammatical constructions for implications and biconditionals. In this lesson, we'll review all those that are commonly used.

The implication $P \Rightarrow Q$ has the following grammatical constructions:

- If $P,$ then $Q$

- $P$ only if $Q$

- $Q$ if $P$

- $P$ implies $Q$

For example,

$\qquad$ **If** $4 \mid n,$ **then** $2 \mid n$

is equivalent to the following:

- $4 \mid n$ **implies** $2 \mid n$

- $4 \mid n$ **only if** $2 \mid n$

- $2 \mid n,$ **if** $4 \mid n$

Using these grammatical constructions correctly within a particular mathematical context can be tricky. It's important to go through each and understand why it's equivalent to $P\Rightarrow Q.$ So, let's do that. We assume that $P\Rightarrow Q$ is *true* in each case.

- If $P,$ then $Q{:}$ If $P$ is true, then $Q$ *must* be true.

- $P$ only if $Q{:}$ The *only* way that $P$ is true is if $Q$ is also true.

- $Q$ if $P{:}$ $Q$ is *guaranteed* to be true if $P$ is true.

- $P$ implies $Q.$ This is the same as "If $P,$ then $Q.$"

### Example: "If-Then", "If", "Only If", and "Implies"

#### Question

Consider the following predicates:

$\qquad$ $P(x):$ $x$ is prime $\qquad$ $Q(x):$ $x$ is not a multiple of $10$

Which of the following expresses the conditional predicate $P(x) \Rightarrow Q(x)?$

1. $x$ is not a multiple of $10$ if $x$ is prime

2. If $x$ is not a multiple of $10,$ then $x$ is prime

3. $x$ is prime implies $x$ is not a multiple of $10$

4. $x$ is not a multiple of $10$ only if $x$ is prime

#### Explanation

Let's recall the following grammatical constructions for the implication $P\Rightarrow Q{:}$

- If $P,$ then $Q$

- $P$ only if $Q$

- $Q$ if $P$

- $P$ implies $Q$

With that in mind, let's examine the given options.

- Option I reads which corresponds to $P(x) \Rightarrow Q(x).$ $\:{\color{green}\checkmark}$

- Option II reads which corresponds to $Q(x) \Rightarrow P(x).$ $\:{\color{red}\times}$

- Option III reads which corresponds to $P(x) \Rightarrow Q(x).$ $\:{\color{darkgreen}\checkmark}$

- Option IV reads which corresponds to $Q(x) \Rightarrow P(x).$ $\:{\color{red}\times}$

Therefore, the correct answer is "I and III only."

### Necessary and Sufficient Conditions

Recall that, in terms of necessary and sufficient conditions, we have

$$


\underbrace{\textrm{Sufficient}\phantom{|}}_{P} \Rightarrow \underbrace{\textrm{Necessary}}_{Q}.


$$

Therefore, we get the following equivalent grammatical constructions:

- $P$ is **sufficient** for $Q$

- For $Q,$ it is **sufficient** that $P$

- $Q$ is **necessary** for $P$

- For $P,$ it is **necessary** that $Q$

Let's go back to the following true implication that we encountered in a previous lesson:

$$


\underbrace{\big( \, a > 0 \, \big)}_{\large\textrm{sufficient}} \: \Rightarrow \: \underbrace{\big( \, a^2 > 0 \, \big)}_{\large\textrm{necessary}}


$$

We can use the following grammatical constructions in terms of sufficient conditions:

- $a > 0$ is a *sufficient condition* for $a^2 > 0$

- $a > 0$ is *sufficient* for $a^2 > 0$

- For $a^2 > 0,$ it is *sufficient* that $a > 0$

These all mean the same thing, namely that $a > 0$ *guarantees* that $a^2 > 0.$

For necessary conditions, we have:

- $a^2 > 0$ is a *necessary condition* for $a > 0$

- $a^2 > 0$ is *necessary* for $a > 0$

- For $a > 0,$ it is *necessary* that $a^2 > 0$

These all mean that if $a > 0$ it follows that $a^2 > 0,$ but $a^2 > 0$ *does not guarantee* that $a > 0.$

### Example: Necessary and Sufficient Conditions

#### Question

Complete the following table:

#### Explanation

Given that the implication $S \Rightarrow N$ is true, we have the following:

- $S$ is a ** for $N.$

- $N$ is a ** for $S.$

These ideas can be summarized as follows:

$$


\textbf{S}\textrm{ufficient} \: \Rightarrow \: \textbf{N}\textrm{ecessary}.


$$

We have the following grammatical constructions for $S\Rightarrow N{:}$

- $S$ is sufficient for $N$

- For $N,$ it is sufficient that $S$

- $N$ is necessary for $S$

- For $S,$ it is necessary that $N$

Let's now compare these against the entries in our table:

- "$B$ is sufficient for $A$" means $B\Rightarrow A.$

- "For $A,$ it is sufficient that $B$" means $B\Rightarrow A.$

- "$B$ is necessary for $A$" means $A\Rightarrow B.$

- "For $A,$ it is necessary that $B$" means $A\Rightarrow B.$

The completed table is shown below.

### Whenever and Provided That

Implication $P \Rightarrow Q$ also can be written using "whenever" and "provided" as follows:

- **Whenever** $P,$ then $Q$

- $Q$ **whenever** $P$

- $Q,$ **provided** that $P$

Let's again go through each one and convince ourselves that they're all equivalent to $P\Rightarrow Q.$ Again, we assume that $P\Rightarrow Q$ is *true* in each case.

- **Whenever** $P,$ then $Q{:}$ Whenever $P$ is true, $Q$ is guaranteed to be true.

- $Q$ **whenever** $P{:}$ $Q$ is guaranteed to be true whenever $P$ is true.

- $Q,$ **provided** that $P{:}$ $Q$ is guaranteed to be true provided that $P$ is true.

Let's see some examples.

### Example: "Whenever", and "Provided That"

#### Question

Consider the following predicates:

$\qquad$ $P(x):$ $x\in\mathbb {Z}^{-}$ $\qquad$ $Q(x):$ $x$ is negative

Which of the following expresses the conditional predicate $P(x) \Rightarrow Q(x)?$

1. Whenever $x$ is negative, then $x\in\mathbb {Z}^{-}$

2. $x$ is negative whenever $x\in\mathbb {Z}^{-}$

3. $x$ is negative, provided that $x\in\mathbb {Z}^{-}$

#### Explanation

Given that the implication $P \Rightarrow Q$ is true, we have the following:

- Whenever $P,$ then $Q$

- $Q$ whenever $P$

- $Q,$ provided that $P$

With that in mind, let's examine the given options.

- Option I reads which corresponds to $Q(x) \Rightarrow P(x).$ $\:{\color{red}\times}$

- Option II reads which corresponds to $P(x) \Rightarrow Q(x).$ $\:{\color{green}\checkmark}$

- Option III reads which corresponds to $P(x) \Rightarrow Q(x).$ $\:{\color{green}\checkmark}$

Therefore, the correct answer is "II and III only."

### Biconditionals

The grammatical constructions for biconditionals $P\Leftrightarrow Q$ are slightly more straightforward than for conditionals.

We've already seen the following constructions:

- $P$ **if and only if** $Q$

- $P$ is **necessary and sufficient** for $Q$

- $P$ is **equivalent** to $Q$

The following constructions are also commonly used:

- $P$ **iff** $Q$

- If $P$ then $Q,$ **and conversely**

Here, "iff" is simply shorthand for "if and only if."

The construction "If $P$ then $Q,$ and conversely" is interesting. Recall that the converse of $P\Rightarrow Q$ is $Q\Rightarrow P.$ If $P\Rightarrow Q$ and $Q\Rightarrow P$ are both true, we have that $P$ implies $Q$ and $Q$ implies $P,$ i.e., $P\Leftrightarrow Q.$

### Example: Biconditionals

#### Question

Express $P \Leftrightarrow Q$ as a sentence given the following:

- $P:$ $A \cup B = A.$

- $Q:$ $B \subseteq A.$

#### Explanation

Let's recall the following grammatical constructions for the biconditional $P\Leftrightarrow Q{:}$

- $P$ if and only if $Q$

- $P$ iff $Q$

- $P$ is necessary and sufficient for $Q$

- $P$ is equivalent to $Q$

- If $P$ then $Q,$ and conversely

Therefore, some correct grammatical constructions of $P \Leftrightarrow Q$ are the following:

- $A \cup B = A$ **** $B \subseteq A.$

- $A \cup B = A$ **** $B \subseteq A.$

- $A \cup B = A$ **** $B \subseteq A.$

- $A \cup B = A$ **** $B \subseteq A.$

- **** $A \cup B = A,$ **** $B \subseteq A,$ ****.
