# Disjunctive Syllogism and Transitivity of Implication

Source: https://www.mathacademy.com/topics/4305?courseId=76
Topic ID: 4305

## Prerequisites

- [Implication Elimination and Denying the Consequent](./4303-implication-elimination-and-denying-the-consequent.md)

## Lesson

### Introduction

Recall that a statement $\beta$ *follows* from statements $\alpha_1, \alpha_2, \ldots, \alpha_n$ if $\beta$ is true whenever *all* of $\alpha_1, \alpha_2, \ldots, \alpha_n$ are true. This is called a *logical inference*.

Let's consider another logical inference rule known as **disjunctive syllogism** (**disjunction elimination** or simply **elimination**). We can state this rule as follows:

$$


\begin{aligned}𝑃∨𝑄 \\ ¬𝑃 \\ ∴\,𝑄\end{aligned}


$$

This rule reads as follows:

*We have $P \lor Q$ and $\lnot P.$ Therefore, $Q.$*

To check that the rule is valid, we can use a truth table:

Both $P \lor Q$ and $\lnot P$ have the truth value ${\color{blue}\mathrm{T}}$ (true) only in the third row of the table. For this row, $Q$ is also ${\color{red}\mathrm{T}}$ (true). So, according to the definition, we have a logical inference.

Since disjunction is commutative and the order of the premises does not matter, we have the following variants of the rule:

$$


\begin{aligned}𝑃∨𝑄 \\ ¬𝑃 \\ ∴\,𝑄\end{aligned}


$$

### A Concrete Example

Let's complete the following logical inference:

$$


\begin{aligned}x is positive or x is less than -1 \\ x is not positive \\ ∴\,𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴\end{aligned}


$$

The logical inference rule of disjunctive syllogism asserts that if $P$ or $Q$ is true, yet $P$ is false, then $Q$ must be true.

Let's denote:

- $P(x):$ $x$ is positive

- $Q(x):$ $x$ is less than $-1$

Then, using the disjunctive syllogism rule, we obtain the following:

$$


\begin{aligned}𝑃∨𝑄 \\ ¬𝑃 \\ ∴\,𝑄\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}x is positive or x is less than -1 \\ x is not positive \\ ∴\,x is less than -1\end{aligned}


$$

### Example: Identifying Disjunction Elimination

#### Question

$$


\begin{aligned}¬𝐾 \\ 𝐾∨𝑀 \\ ∴\,𝐴\end{aligned}


$$

What is the missing part of the logical inference rule above?

#### Explanation

The logical inference rule of ** asserts that if $P$ or $Q$ is true, yet $P$ is false, then $Q$ must be true.

In the case above, the disjunctive syllogism inference rule can be written as follows:

$$


\begin{aligned}¬𝐾 \\ 𝐾∨𝑀 \\ ∴𝑀\end{aligned}


$$

Therefore, the missing part is $M.$

### Example: Logical Inference Using Disjunction Elimination

#### Question

According to the disjunctive syllogism inference rule, what is missing from the series of statements below?

$$


\begin{aligned}x is divisible by 3 or x is prime \\ x is not prime \\ 𝑥𝑖𝑠𝑑𝑖𝑣𝑖𝑠𝑖𝑏𝑙𝑒𝑏𝑦3.\end{aligned}


$$

#### Explanation

The logical inference rule of ** asserts that if $P$ or $Q$ is true, yet $P$ is false, then $Q$ must be true.

Let's denote:

- $D(x):$ $x$ is divisible by $3$

- $P(x):$ $x$ is prime

Then, using our disjunctive syllogism inference rule, we obtain the following:

$$


\begin{aligned}𝐷∨𝑃 \\ ¬𝑃 \\ ∴𝐷\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}x divisible by 3 or x is prime \\ x is not prime \\ ∴\,x is divisible by 3\end{aligned}


$$

### Transitivity of Implication

Another important rule of logical inference is called **transitivity of implication** (**chain argument** or **hypothetical syllogism**):

$$


\begin{aligned}𝑃⇒𝑄 \\ 𝑄⇒𝑅 \\ ∴\,𝑃⇒𝑅\end{aligned}


$$

This rule is read as follows:

*We have $P \Rightarrow Q$ and $Q \Rightarrow R.$ Therefore, $P \Rightarrow R.$*

We can use a truth table to check this rule is valid:

Both $P \Rightarrow Q$ and $Q \Rightarrow R$ have the truth value ${\color{blue}\mathrm{T}}$ (true) in the first, fifth, seventh, and eighth rows of the table only. For these rows, $P \Rightarrow R$ also has the truth value ${\color{red}\mathrm{T}}$ (true). So, according to the definition, we have a logical inference.

Since the order of the premises does not matter, we have the following variants of the rule:

$$


\begin{aligned}𝑃⇒𝑄 \\ 𝑄⇒𝑅 \\ ∴\,𝑃⇒𝑅\end{aligned}


$$

### A Concrete Example

Let's complete the following logical inference:

$$


\begin{aligned}If x is positive, then 2x is positive \\ If 2x is positive, then 2x+1 is positive \\ ∴\,𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴\end{aligned}


$$

The logical inference rule of *transitivity of implication* asserts that if $P$ implies $Q$ is true, and $Q$ implies $R$ is true, then $P$ implies $R$ must be true.

Let's denote:

- $P(x):$ $x$ is positive

- $Q(x):$ $2x$ is positive

- $R(x):$ $2x+1$ is positive

Then, using the transitivity of implication rule, we obtain the following:

$$


\begin{aligned}𝑃⇒𝑄 \\ 𝑄⇒𝑅 \\ ∴\,𝑃⇒𝑅\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}If x is positive, then 2x is positive \\ If 2x is positive, then 2x+1 is positive \\ ∴\,If x is positive, then 2x+1 is positive\end{aligned}


$$

### Example: Identifying Transitivity of Implication

#### Question

$$


\begin{aligned}𝐿⇒𝑀 \\ 𝐾⇒𝐿 \\ ∴\,𝐴𝐴𝐴\end{aligned}


$$

What is the missing part of the logical inference rule above?

#### Explanation

The logical inference rule of ** (also known as **) asserts that if $P$ implies $Q$ is true, and $Q$ implies $R$ is true, then $P$ implies $R$ must be true.

In this case, the hypothetical syllogism rule can be written as follows:

$$


\begin{aligned}𝐿⇒𝑀 \\ 𝐾⇒𝐿 \\ ∴𝐾⇒𝑀\end{aligned}


$$

Therefore, the missing part is $K \Rightarrow M.$

### Example: Logical Inference Using Transitivity of Implication

#### Question

According to the rule of transitivity of implication, what is missing from the series of statements below?

$$


\begin{aligned}If x is even, then 2 \mid x \\ If 2\mid x, then 2 \mid (x+8) \\ 𝐼𝑓𝑥𝑖𝑠𝑒𝑣𝑒𝑛,𝑡ℎ𝑒𝑛2∣(𝑥+8)\end{aligned}


$$

#### Explanation

The logical inference rule of ** (also known as **) asserts that if $P$ implies $Q$ is true, and $Q$ implies $R$ is true, then $P$ implies $R$ must be true.

Let's denote:

- $P(x):$ $x$ is even

- $Q(x):$ $2 \mid x$

- $R(x):$ $2 \mid (x+8)$

Then, using the transitivity of implication rule, we obtain the following:

$$


\begin{aligned}𝑃⇒𝑄 \\ 𝑄⇒𝑅 \\ ∴𝑃⇒𝑅\end{aligned}


$$

Therefore, we have:

$$


\begin{aligned}If x is even, then 2 \mid x \\ If 2\mid x, then 2 \mid (x+8) \\ ∴\,If x is even, then 2\mid (x+8)\end{aligned}


$$
