# Necessary and Sufficient Conditions

Source: https://www.mathacademy.com/topics/2793?courseId=76
Topic ID: 2793

## Prerequisites

- [Integrating Trigonometric Functions](../../../ap-courses/lessons/ap-calculus-ab/285-integrating-trigonometric-functions.md)
- [Integrating Exponential Functions](../../../ap-courses/lessons/ap-calculus-ab/312-integrating-exponential-functions.md)
- [Continuity and Differentiability of Functions](../../../ap-courses/lessons/ap-calculus-ab/1691-continuity-and-differentiability-of-functions.md)
- [Properties of Integer Divisibility](./4433-properties-of-integer-divisibility.md)

## Lesson

### Introduction

Consider the truth table for $S \Rightarrow N$ below. Note that the implication is true $({\color{blue}\text{T}})$ in the $1$st, $3$rd, and $4$th rows.

Of the three rows where the implication is true, $S$ is true $({\color{red}\text{T}})$ only in the $1$st row, and $N$ is also true $({\color{red}\text{T}})$ in this row.

So, if the implication is true, $S$ being true *guarantees* that $N$ must also be true. Therefore, $S$ is called a **sufficient condition** for $N.$

On the other hand, if $S$ is true, it is *necessary* that $N$ is also true. Therefore, $N$ is called a **necessary condition** for $S.$ However, $N$ being true *does not guarantee* that $S$ is true, as we can see from the $3$rd row in the truth table.

These ideas can be summarized as follows:

$$


\textbf{S}\text{ufficient} \: \Rightarrow \: \textbf{N}\text{ecessary}.


$$

Let's look at some examples:

- Consider the following true implication: We can label each part of the statement as follows: Therefore: $a > 0$ is a *sufficient* condition for $a^2 > 0.$ In other words, $a > 0$ *guarantees* that $a^2 > 0.$ $a^2 > 0$ is a *necessary* condition for $a > 0.$ In other words, if $a > 0,$ it is necessary that $a^2 > 0.$ However, $a^2 > 0$ *does not guarantee* that $a > 0.$

- Suppose your teacher promises that *if* you score at least $90$ on the exam, *then* you will receive an $A.$ We can express this promise as the following implication: Let's assume the teacher is telling the truth, so the implication is true. We can label each part of our implication as follows: Therefore: Scoring at least $90$ on the exam is a *sufficient* condition for getting an $A.$ In other words, scoring at least $90$ *guarantees* that you'll get an $A.$ Getting an $A$ is a *necessary* condition for scoring at least $90.$ In other words, if you score at least $90,$ it necessarily follows that you'll receive $A.$ However, getting an $A$ *does not guarantee* that you scored at least $90$ on the exam. For example, the teacher may have decided to award an $A$ despite a score smaller than 90 if the exam was particularly tough that year.

### Example: Identifying Necessary or Sufficient Conditions From Implications

#### Question

$\qquad$ $(A=\overline{B}) \Rightarrow (A\cap B = \emptyset)$

Which of the following statements are true regarding the true implication above?

1. $A=\overline{B}$ is a **** condition for $A\cap B = \emptyset$

2. $A=\overline{B}$ is a **** condition for $A\cap B = \emptyset$

3. $A\cap B = \emptyset$ is a **** condition for $A=\overline{B}$

4. $A\cap B = \emptyset$ is a **** condition for $A=\overline{B}$

#### Explanation

Given that the implication $S \Rightarrow N$ is true, we have the following:

- $S$ being true ** that $N$ must also be true. Therefore, $S$ is a ** for $N.$

- For $S$ to be true, it is ** that $N$ is true. Therefore, $N$ is a ** for $S.$ However, note that $N$ being true does ** guarantee that $S$ is true.

These ideas can be summarized as follows:

$$


\textbf{S}\text{ufficient} \: \Rightarrow \: \textbf{N}\text{ecessary}.


$$

In our case,

$$


\underbrace{\big( \, A=\overline{B} \, \big)}_{\large\text{sufficient}} \: \Rightarrow \: \underbrace{\big( \, A\cap B = \emptyset \, \big)}_{\large\text{necessary}}


$$

is a true statement. Therefore:

- Statement II is true. $A=\overline{B}$ is a **** condition for $A\cap B = \emptyset.$

- Statement III is true. $A\cap B = \emptyset$ is a **** condition for $A=\overline{B}.$

Therefore, the correct answer is "II and III only."

### Example: Identifying Necessary Conditions

#### Question

Consider the following statement:

$\qquad$ $x$ is divisible by $8$

Which of the following conditions are necessary for this statement to be true?

1. $x$ is divisible by $2$

2. $x$ is divisible by $4$

3. $x$ is divisible by $6$

#### Explanation

Given that the implication $S \Rightarrow N$ is true, we have the following:

- $S$ being true ** that $N$ must also be true. Therefore, $S$ is a ** for $N.$

- For $S$ to be true, it is ** that $N$ is true. Therefore, $N$ is a ** for $S.$ However, note that $N$ being true does ** guarantee that $S$ is true.

These ideas can be summarized as follows:

$$


\textbf{S}\text{ufficient} \: \Rightarrow \: \textbf{N}\text{ecessary}.


$$

In our case, we need to find the conditions that are ** from the given one:

$$


𝑥


$$

With that in mind, let's inspect each of the given conditions.

- Condition I is a necessary condition: Since $2$ is a factor of $8,$ any number $x$ that is divisible by $8$ is also divisible by $2.$

- Condition II is a necessary condition: Since $4$ is a factor of $8,$ any number $x$ that is divisible by $8$ is also divisible by $4.$

- Condition III is ** a necessary condition: For example, the number $x=16$ is divisible by $8,$ but it is ** divisible by $6.$

Therefore, the correct answer is "I and II only."

### Example: Identifying Sufficient Conditions

#### Question

Consider the following statement:

$\qquad$ $n$ is divisible by $2$

Which of the following conditions are sufficient for the above to be true?

1. $n$ is divisible by $4$

2. $n$ is divisible by $6$

3. $n$ is divisible by $9$

#### Explanation

Given that the implication $S \Rightarrow N$ is true, we have the following:

- $S$ being true ** that $N$ must also be true. Therefore, $S$ is a ** for $N.$

- For $S$ to be true, it is ** that $N$ is true. Therefore, $N$ is a ** for $S.$ However, note that $N$ being true does ** guarantee that $S$ is true.

These ideas can be summarized as follows:

$$


\textbf{S}\text{ufficient} \: \Rightarrow \: \textbf{N}\text{ecessary}.


$$

In our case, we need to find the conditions that are ** for the given one:

$$


𝑛


$$

With that in mind, let's inspect each of the given conditions.

- Condition I is a sufficient condition: Since $2$ is a factor of $4$, any number $n$ that is divisible by $4$ is also a divisible by $2.$

- Condition II is a sufficient condition: Since $2$ is a factor of $6$, any number $n$ that is divisible by $6$ is also a divisible by $2.$

- Condition III is ** a sufficient condition: For example, $n=9$ is divisible by $9,$ but $9$ is not divisible by $2.$

Therefore, the correct answer is "I and II only."

### Necessary and Sufficient Conditions

Suppose that an equivalence $P \Leftrightarrow Q$ is true. Then, we have the following terminology:

- $P$ is a **necessary and sufficient condition** for $Q$

- $Q$ is a **necessary and sufficient condition** for $P$

For example, consider the following two predicates:

- $35 \mid n$

- $5 \mid n$ and $7 \mid n$

These are both necessary and sufficient conditions for each other.

Indeed, recall that a number is divisible by $35$ *if and only if* it's divisible by both $5$ and $7.$ In other words, we have

$$


5∣𝑛


$$

and

$$


5∣𝑛


$$

Therefore, we can write

$$


5∣𝑛


$$

In words:

- $\big(35 \mid n \big)$ *is necessary and sufficient for* $5∣𝑛$

- $5∣𝑛$ *is necessary and sufficient for* $\big(35 \mid n \big).$

### Example: Identifying Necessary and Sufficient Conditions

#### Question

Consider the following statement:

$\qquad$ $x^2 - x = 0$

Which of the following conditions are necessary and sufficient for the above statement to be true?

1. $x = 0$ or $x=1$

2. $x = 1$

3. $x$ is an integer.

#### Explanation

Given that the equivalence $P \Leftrightarrow Q$ is true, we have that $P$ is a ** for $Q.$

In our case, we need to find the conditions that are ** for the given one. In other words,

$$


\big( x^2 - x = 0 \big) \: \Rightarrow \: \text{Condition}


$$

and

$$


\big( x^2 - x = 0 \big) \: \Leftarrow \: \text{Condition}.


$$

Note that the solution to the given equation is

$$


\begin{aligned}𝑥^{2}−𝑥 & =0 \\ 𝑥(𝑥−1) & =0 \\ 𝑥 & =0,1\end{aligned}


$$

With that in mind, let's inspect each of the given conditions.

- Condition I is both necessary and sufficient: The statement $x^2 - x=0$ is true ** $x=0$ or $x=1.$ and Therefore, we can write

- Condition II is ** a necessary condition: For example, for the number $x=0,$ the statement $x^2 - x=0$ is true but $x\neq 1.$

- Condition III is ** a sufficient condition: For example, the number $x=2$ is an integer but it is not a solution to $x^2 - x=0.$

Therefore, the correct answer is "I only."
