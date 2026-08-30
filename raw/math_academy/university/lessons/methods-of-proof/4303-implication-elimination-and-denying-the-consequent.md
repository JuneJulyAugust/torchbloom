# Implication Elimination and Denying the Consequent

Source: https://www.mathacademy.com/topics/4303?courseId=76
Topic ID: 4303

## Prerequisites

- [Conditional Statements With Predicates](./4257-conditional-statements-with-predicates.md)

## Lesson

### Introduction

The rules of logic provide a theory that allows us to process logical statements correctly. However, these rules do not concern themselves with the truth values of the statements involved.

Therefore, care must be taken when applying logical principles to real-world situations, as blindly following these rules does not guarantee the truthfulness of the conclusions drawn. In particular, we must also consider the truth values of the statements involved.

To demonstrate, consider the following statements:

- $P:\:$ Isaac Newton was a Martian.

- $Q:\:$ All Martians are from Mars.

- $R:\:$ Therefore, Isaac Newton was from Mars.

Now, while statement $R$ follows *logically* from statements $P$ and $Q,$ we cannot assert that $R$ is true and that Isaac Newton was actually from Mars! The problem, of course, is that the statement $P$ is false.

We say that a statement $\beta$ **follows** from statements $\alpha_1, \alpha_2, \ldots, \alpha_n$ if $\beta$ is true whenever *all* of $\alpha_1, \alpha_2, \ldots, \alpha_n$ are true. This is called a **logical inference**.

In this lesson, we'll study some well-known rules of logical inference.

### Implication Elimination

The first logical inference rule we'll study is called **implication elimination** (or **modus ponens** in Latin). It states the following:

*If $P \Rightarrow Q$ and $P$ are both true, then $Q$ must be also true.*

To understand this rule, we consider the corresponding truth table:

Both $P \Rightarrow Q$ and $P$ have truth value ${\color{blue}\mathrm{T}}$ (true) only in the first row of the table. For this row, $Q$ is also ${\color{red}\mathrm{T}}$ (true). So, according to our definition, we have a logical inference.

An alternative way of writing the rule is

$$


\begin{aligned}𝑃⇒𝑄 \\ 𝑃 \\ ∴𝑄\end{aligned}


$$

where the symbol $\,\raise{1pt}{\therefore}\,$ reads as "therefore". So, the entire thing reads as follows:

*We have $P \Rightarrow Q$ and $P.$ Therefore, $Q.$*

Since the order of the premises does not matter, we have the following variants of the rule:

$$


\begin{aligned}𝑃⇒𝑄 \\ 𝑃 \\ ∴𝑄\end{aligned}


$$

### A Concrete Example

As a concrete example, let's complete the following logical inference:

$$


\begin{aligned}If x is greater than 1, then x is positive \\ x is greater than 1 \\ ∴\,𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴\end{aligned}


$$

The logical inference rule of implication elimination asserts that if $P$ implies $Q$ is true, and $P$ is true, then $Q$ is also true.

Let's denote:

- $P(x):$ $x$ is greater than $1$

- $Q(x):$ $x$ is positive

Then, using the modus ponens inference rule, we obtain the following:

$$


\begin{aligned}𝑃⇒𝑄 \\ 𝑃 \\ ∴𝑄\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}If x is greater than 1, then x is positive \\ x is greater than 1 \\ ∴\,x is positive\end{aligned}


$$

### Example: Identifying Implication Elimination

#### Question

$$


\begin{aligned}(𝐴∧𝐵)⇒¬𝐶 \\ 𝐴∧𝐵 \\ ∴\,𝐴𝐴𝐴𝐴\end{aligned}


$$

What is the missing part of the logical inference rule above?

#### Explanation

The logical inference rule of ** (also known as **) asserts that if $P$ implies $Q$ is true, and $P$ is true, then $Q$ is also true.

In the case above, the modus ponens inference rule can be written as follows:

$$


\begin{aligned}(𝐴∧𝐵)⇒¬𝐶 \\ 𝐴∧𝐵 \\ ∴¬𝐶\end{aligned}


$$

Therefore, the missing part is $\lnot C.$

### Example: Logical Inference Using the Implication Elimination

#### Question

According to the modus ponens inference rule, what is missing from the series of statements below?

$$


\begin{aligned}\mathcal{P} is a square \\ If \mathcal{P} is a square, then \mathcal{P} is a rectangle \\ ∴\,𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴\end{aligned}


$$

#### Explanation

The logical inference rule of ** (also known as **) asserts that if $P$ implies $Q$ is true, and $P$ is true, then $Q$ is also true.

Let's denote:

- $P:$ $\mathcal{P}$ is a square

- $Q:$ $\mathcal{P}$ is a rectangle

Then, using the modus ponens inference rule, we obtain the following:

$$


\begin{aligned}𝑃 \\ 𝑃⇒𝑄 \\ ∴𝑄\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}\mathcal{P} is a square \\ If \mathcal{P} is a square, then \mathcal{P} is a rectangle \\ ∴\,\mathcal{P} is a rectangle\end{aligned}


$$

### Denying the Consequent

Let's now consider another logical inference rule called **denying the consequent** (or **modus tollens** in Latin):

$$


\begin{aligned}𝑃⇒𝑄 \\ ¬𝑄 \\ ∴¬𝑃\end{aligned}


$$

It reads as follows:

*We have $P \Rightarrow Q$ and $\lnot Q.$ Therefore, $\lnot P.$*

We can use a truth table to check that the rule is valid.

Both $P \Rightarrow Q$ and $\lnot Q$ have the truth value ${\color{blue}\mathrm{T}}$ (true) only in the fourth row of the table. For this row, $\lnot P$ also has truth value ${\color{red}\mathrm{T}}$ (true). So, according to the definition, we have a logical inference.

Since the order of the premises does not matter, we have the following variants of the rule:

$$


\begin{aligned}𝑃⇒𝑄 \\ ¬𝑄 \\ ∴¬𝑃\end{aligned}


$$

### A Concrete Example

As a concrete example, let's complete the following logical inference:

$$


\begin{aligned}If x is greater than 1, then x is positive \\ x is not positive \\ ∴\,𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴\end{aligned}


$$

The logical inference rule of *denying the consequent* asserts that if $P$ implies $Q$ is true, and $Q$ is false, then $P$ is also false.

Let's denote:

- $P(x):$ $x$ is greater than $1$

- $Q(x):$ $x$ is positive

Then, using the modus tollens inference rule, we obtain the following:

$$


\begin{aligned}𝑃⇒𝑄 \\ ¬𝑄 \\ ∴¬𝑃\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}If x is greater than 1, then x is positive \\ x is not positive \\ ∴\,x is not greater than 1\end{aligned}


$$

### Example: Identifying Modus Tollens

#### Question

$$


\begin{aligned}(¬𝑅∧𝑆)⇒𝑇 \\ ¬𝑇 \\ ∴\,𝐴𝐴𝐴\end{aligned}


$$

What is the missing part of the logical inference rule above?

#### Explanation

The logical inference rule of ** (also known as **) asserts that if $P$ implies $Q$ is true, and $Q$ is false, then $P$ is also false.

In the case above, the modus tollens inference rule can be written as follows:

$$


\begin{aligned}(¬𝑅∧𝑆)⇒𝑇 \\ ¬𝑇 \\ ∴¬(¬𝑅∧𝑆)\end{aligned}


$$

Therefore, the missing part is $\lnot (\lnot R \land S).$

### Example: Logical Inference Using Modus Tollens

#### Question

According to the modus tollens inference rule, what is missing from the series of statements below?

$$


\begin{aligned}\mathcal{P} is not a parallelogram \\ If \mathcal{P} is a rhombus, then \mathcal{P} is a parallelogram \\ ∴\,𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴\end{aligned}


$$

#### Explanation

The logical inference rule of ** (also known as **) asserts that if $P$ implies $Q$ is true, and $Q$ is false, then $P$ is also false.

Let's denote:

- $P:$ $\mathcal{P}$ is a rhombus

- $Q:$ $\mathcal{P}$ is a parallelogram

Then, using the modus tollens inference rule, we obtain the following:

$$


\begin{aligned}¬𝑄 \\ 𝑃⇒𝑄 \\ ∴¬𝑃\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}\mathcal{P} is not a parallelogram \\ If \mathcal{P} is a rhombus, then \mathcal{P} is a parallelogram \\ ∴\,\mathcal{P} is not a rhombus\end{aligned}


$$
