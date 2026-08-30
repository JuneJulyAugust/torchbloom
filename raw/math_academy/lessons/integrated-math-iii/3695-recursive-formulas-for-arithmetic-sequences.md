# Recursive Formulas for Arithmetic Sequences

Source: https://www.mathacademy.com/topics/3695?courseId=134
Topic ID: 3695

## Prerequisites

- [Arithmetic Sequences](../algebra-i/667-arithmetic-sequences.md)
- [Recursive Sequences](../algebra-i/1226-recursive-sequences.md)

## Lesson

### Introduction

Suppose we have the following arithmetic sequence with first term $a_1 = {\color{red}4}$ and common difference $d={\color{blue}{3}}\mathbin{:}$

$$


{\color{red}{4}},7,10,13,16,\ldots


$$

Each term is ${\color{blue}{3}}$ more than the previous, starting with ${\color{red}{4}}.$ Therefore, we can express this sequence recursively:

$$


a_{n+1} = a_n + {\color{blue}{3}}, \quad a_1 = {\color{red}{4}}, \quad n\geq 1


$$

We can also express the sequence using function notation:

$$


f(n+1) = f(n) + {\color{blue}{3}}, \quad f(1) = {\color{red}{4}}, \quad n\geq 1


$$

### Example: Computing the Terms of an Arithmetic Sequence

#### Question

Calculate the fourth term of the sequence

$$


f(n+1) = f(n) -6, \quad f(1) = 1, \quad n\geq 1.


$$

#### Explanation

Starting with the first term $f(1)=1,$ we compute the next terms using the recursive rule until we reach the fourth term $f(4).$

$$


\begin{aligned}𝑓(1) & =1 \\ 𝑓(2) & =𝑓(1)−6=1−6=−5 \\ 𝑓(3) & =𝑓(2)−6=−5−6=−11 \\ 𝑓(4) & =𝑓(3)−6=−11−6=−17\end{aligned}


$$

Therefore, the fourth term is $f(4)=-17.$

### Example: Finding a Recursive Formula

#### Question

What is the recursive formula for the following arithmetic sequence?

$$


4,\: 9,\: 14,\: \ldots


$$

#### Explanation

The recursive formula for an arithmetic sequence with common difference $d$ is

$$


a_{n+1} =a_n+d.


$$

In our case, the common difference is

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =9−4 \\ & =5.\end{aligned}


$$

Consequently, the recursive formula for this sequence is

$$


a_{n+1}= a_n + 5, \quad a_1=4, \quad n\geq 1\,.


$$
