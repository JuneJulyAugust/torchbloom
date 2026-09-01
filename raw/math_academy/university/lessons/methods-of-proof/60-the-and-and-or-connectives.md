# The "And" and "Or" Connectives

Source: https://www.mathacademy.com/topics/60?courseId=76
Topic ID: 60

## Prerequisites

- [Statements and Predicates](./58-statements-and-predicates.md)

## Lesson

### Introduction

A **compound statement** is a sentence that consists of two or more statements separated by logical connectors, such as the word "and" or the word "or."

For example, the following sentence is a compound statement:

$P: 2$ is an integer **and** $2$ is positive

The first statement is "$2$ is an integer," and the second is "$2$ is positive." These two statements are separated by the logical connector "and."

The following sentence is also a compound statement:

$7$ is odd **or** $7$ is even

In this case, the first statement is "$7$ is odd," and the second statement is "$7$ is even." These two statements are separated by the logical connector "or."

We can express the logical connectives "and" and "or" using symbols:

- The word "and" is represented by the symbol "$\land$". Notice that it resembles "A" for "And."

- The word "or" is represented by the symbol "$\lor$".

Let's translate the following sentence into symbolic form:

$2$ is an integer **and** $2$ is positive

To start, we introduce the letters $A$ and $B$ to denote each individual statement:

- $A:$ $2$ is an integer

- $B:$ $2$ is positive

Then, our sentence becomes

$$


\underbrace{2 \vphantom{p}\text{ is an integer} }_A \quad \underbrace{\vphantom{p}\text{and}}_{\land} \quad \underbrace{2 \vphantom{p}\text{ is positive} }_B,


$$

that is, $A \land B.$

Finally, note the following terminology:

- The statement "$P$ and $Q$" is called the **conjunction** of the statements $P$ and $Q.$

- The statement "$P$ or $Q$" is called the **disjunction** of the statements $P$ and $Q.$

### Example: Expressing Compound Statements in Symbolic Form

#### Question

Consider the following statement:

$14$ is divisible by $4$ **** $\sqrt{3}$ is a rational number.

Write this statement in symbolic form using the following notations:

- $14$

- $\sqrt{3}$

#### Explanation

The word "or" is represented by the symbol "$\lor$".

So, the sentence reads

$$


\underbrace{14 \vphantom{p}\text{ is divisible by }\vphantom{p} 4 }_S \quad \underbrace{\vphantom{p}\textbf{or}}_{\lor} \quad \underbrace{\sqrt{3} \vphantom{p}\text{ is a rational number} }_T,


$$

that is, $S \lor T.$

### Example: Expressing Nested Compound Statements in Symbolic Form

#### Question

$7$ is odd **** a multiple of $3$, **** $3$ is less than $7$.

Express the compound statement above in symbolic form given the following notations:

- $7$

- $7$

- $3$

#### Explanation

The word "and" is represented by the symbol "$\land$", while the word "or" is represented by the symbol "$\lor$".

Note that this sentence consists of two parts:

- **** $7$ is odd or a multiple of $3.$ This corresponds to that is, $P \lor Q.$

- **** $3$ is less than $7$. This corresponds to $R.$

So, we can express the sentence as

$$


\underbrace{7 \vphantom{p}\text{ is odd} \textbf{ or } \vphantom{p} \vphantom{p}\text{ a multiple of } 3}_{P \, \lor \,Q}, \quad \underbrace{\vphantom{p}\textbf{and}}_{\land} \quad \underbrace{3 \vphantom{p}\text{ is less than } 7 }_R


$$

that is, $(P \lor Q) \land R.$

### Truth Values of Statements Containing the "And" Connective

Let's now consider the truth values of the logical connector "and". We have the following key idea:

*The statement $A \land B$ is true if $A$ is true **** $B$ is true. Otherwise, it is false.*

Let's determine the truth values of the following compound statement:

$2$ is positive **and** $2$ is even.

Writing this in symbols, we have the following:

$$


\begin{aligned}\underset{𝐴}{\underset{}{2𝑝 is positive}}\,\underset{∧}{\underset{}{𝑝𝐚𝐧𝐝}}\,\underset{𝐵}{\underset{}{2𝑝 is even}}\end{aligned}


$$

or, simply

$$


A\land B.


$$

Since $A$ is true and $B$ is true, this compound statement is true:

$$


\begin{aligned}𝐴∧𝐵≡true∧true≡true\end{aligned}


$$

In this context, the symbol "$\equiv$" means "is logically equivalent to."

Let's now consider a similar compound statement but with the $2$ replaced with a $3$ in the second statement.

$$


\begin{aligned}\underset{𝐴}{\underset{}{2𝑝 is positive}}\,\underset{∧}{\underset{}{𝑝𝐚𝐧𝐝}}\,\underset{𝐶}{\underset{}{3𝑝 is even}}\end{aligned}


$$

We can write this symbolically as follows:

$$


A\land C


$$

Since $A$ is true and $C$ is false, this compound statement is false:

$$


\begin{aligned}𝐴∧𝐶≡true∧false≡false\end{aligned}


$$

### Truth Values of Statements Containing the "Or" Connective

Let's now consider the truth values of the logical connector "or". We have the following key idea:

*The statement $A \lor B$ is true if $A$ is true, or $B$ is true, or both $A$ and $B$ are true. Otherwise, it is false.*

Let's consider some examples:

- First, consider the following statement: Since $A$ is true and $B$ is true, this compound statement is true:

- Next, consider the following statement: Since $A$ is true, this compound statement is true:

- Now, consider the following: Since $B$ is true, this compound statement is true:

- Finally, consider the following: Since $D$ and $C$ are both false, this compound statement is false:

### Example: Finding Truth Values of Compound Statements

#### Question

Consider the following compound statement:

$$


\underbrace{5 \vphantom{p}\text{ is prime} }_A \quad \underbrace{\vphantom{p}\textbf{or}}_{\lor} \quad \underbrace{\dfrac13 \in \mathbb{Z}}_B


$$

Find the truth values of the statements $A$ and $B,$ and the compound statement $A\lor B.$

#### Explanation

First, let's recall the following facts about the "and" $(\land)$ and "or" $(\lor)$ logical connectives:

- The statement $A \land B$ is true if ** $A$ and $B$ are true.

- The statement $A \lor B$ is true if either $A$ is true, or $B$ is true, or ** $A$ and $B$ are true.

In our case, $A$ is true, and $B$ is false. Therefore, the result is true:

$$


\begin{aligned}\underset{𝐴}{\underset{}{5𝑝 is prime}}\,\underset{∨}{\underset{}{𝑝𝐨𝐫}}\,\underset{𝐵}{\underset{}{\frac{1}{3}∈ℤ}} & \,\,≡\,true∨false≡true\end{aligned}


$$

### Example: Finding Truth Values of Complex Statements

#### Question

Consider the following compound statement:

$$


\underbrace{\mathbb{Z}\cup \mathbb{R}=\mathbb{Z} }_P \quad \underbrace{\vphantom{|}\textbf{and}}_{\land} \quad \underbrace{\overbrace{7 \,|\, 21}^Q \quad \overbrace{\vphantom{|}\textbf{or}}^{\lor} \quad \overbrace{7 \,|\, 29}^R }_{Q \, \lor \, R}


$$

Find the truth values of the statements $P,$ $Q$ and $R,$ and the compound statements $Q\lor R$ and $P\land (Q\lor R).$

#### Explanation

First, let's recall the following facts about the "and" $(\land)$ and "or" $(\lor)$ logical connectives:

- The statement $A \land B$ is true if ** $A$ and $B$ are true.

- The statement $A \lor B$ is true if either $A$ is true, or $B$ is true, or ** $A$ and $B$ are true.

In our case, $P$ is false, $Q$ is true, and $R$ is false. Therefore, $Q \lor R$ is true, but the result is false:

$$


\begin{aligned}𝑃∧(𝑄∨𝑅) & ≡false∧\overset{(true∨false)}{true} \\ & ≡false∧true \\ & ≡false\end{aligned}


$$
