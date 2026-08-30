# The Recursive Formula for a Geometric Sequence

Source: https://www.mathacademy.com/topics/1818?courseId=111
Topic ID: 1818

## Prerequisites

- [Introduction to Geometric Sequences](./679-introduction-to-geometric-sequences.md)
- [Recursive Sequences](./1226-recursive-sequences.md)

## Lesson

### Introduction

The **recursive formula for a geometric sequence** with common ratio $r$ takes the form

$$


a_{n+1} = r \cdot a_{n}


$$

The above formula states that to get to the next term in the sequence, we multiply the previous term by $r.$

To illustrate, consider the geometric sequence below:

$$


1, \: 3, \: 9, \: 27, \: \dots


$$

The first term is $a_1=1,$ and we can calculate the common ratio $r$ as

$$


r = \dfrac{a_2}{a_1} = \dfrac 3 1 = 3.


$$

Therefore, the recursive formula is

$$


a_{n+1} = 3 \cdot a_{n} , \qquad a_1 = 1, \qquad n\geq 1.


$$

When writing out our final answer for the recursive formula, we should also state the first term and the range for $n.$

To check that the recursive formula is correct, we can use it to generate the next few terms of the series:

$$


\begin{aligned}𝑎_{2} & =3⋅𝑎_{1}=3⋅1=30\,✓ \\ 𝑎_{3} & =3⋅𝑎_{2}=3⋅3=90\,✓ \\ 𝑎_{4} & =3⋅𝑎_{3}=3⋅9=27\,✓\end{aligned}


$$

### Example: Constructing a Recursive Formula for a Geometric Sequence

#### Question

What is the recursive formula for the following geometric sequence?

$$


1, \: 4, \: 16, \: \ldots


$$

#### Explanation

The recursive formula for a geometric sequence with common ratio $r$ takes the form

$$


a_{n+1} = r \cdot a_{n}.


$$

In this case, the first term is $a_1={\color{blue}1},$ and we can calculate the common ratio $r$ as

$$


r = \dfrac{a_2}{a_1} = \dfrac 4 1 = {\color{red}4}.


$$

Therefore, the recursive formula is

$$


a_{n+1} = {\color{red}4} \cdot a_{n} , \qquad a_1 = {\color{blue}1}, \qquad n\geq 1.


$$

### Example: Calculating a Term of a Geometric Sequence Given Its Recursive Formula

#### Question

What is the $4$th term of the geometric sequence given below?

$$


a_{n+1} = -3 a_n,\qquad a_1 = 2,\qquad n \geq 1


$$

#### Explanation

We use the recursive formula to compute the terms of the sequence up to the $4$th term:

$$


\begin{aligned}𝑎_{1} & =2 \\ 𝑎_{2} & =−3𝑎_{1}=−3(2)=−6 \\ 𝑎_{3} & =−3𝑎_{2}=−3(−6)=18 \\ 𝑎_{4} & =−3𝑎_{3}=−3(18)=−54\end{aligned}


$$

Therefore, $a_4 = -54.$

### Example: Calculating a Term of a Geometric Sequence Given a Recursive Formula in Function Notation

#### Question

What is the $5$th term of the geometric sequence given below?

$$


f(n+1) = -5f(n),\quad f(1) = -1,\quad n\geq 1


$$

#### Explanation

We use the recursive formula to compute the terms of the sequence up to the $4$th term:

$$


\begin{aligned}𝑓(1) & =−1 \\ 𝑓(2) & =−5𝑓(1)=−5(−1)=5 \\ 𝑓(3) & =−5𝑓(2)=−5(5)=−25 \\ 𝑓(4) & =−5𝑓(3)=−5(−25)=125 \\ 𝑓(5) & =−5𝑓(4)=−5(125)=−625\end{aligned}


$$

Therefore, $f(5)=-625.$

### Example: Identifying Geometric Sequences

#### Question

Which of the three sequences below are geometric sequences?

1. $10, \: 20, \: 30, \: 40, \: \dots$

2. $a_{n+1} = \dfrac{1}{6}a_n,\quad a_1 = 36,\quad n\geq 1$

3. $f(n+1) = 2f(n)-1,\quad f(1) =2,\quad n\geq 1$

#### Explanation

A sequence is geometric if there is a common ratio between its terms. Let's check each sequence in turn.

- Sequence I is not geometric because not every pair of consecutive terms has the same ratio. To see this, we only need to go up to the third term:

- Sequence II is a geometric sequence. The recursive rule $a_{n+1} = \dfrac{1}{6}a_n$ tells us that each term is $\dfrac{1}{6}$ times the previous term, so the common ratio is $r=\dfrac{1}{6}.$

- Sequence III is not a geometric sequence. To see this, we can calculate the first $3$ terms of the sequence and then compute the ratios of consecutive terms. The first two pairs of consecutive terms have different ratios:

In conclusion, only sequence II is a geometric sequence.
