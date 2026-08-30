# Translating Between Explicit and Recursive Formulas for Arithmetic Sequences

Source: https://www.mathacademy.com/topics/2214?courseId=134
Topic ID: 2214

## Prerequisites

- [The Nth Term of an Arithmetic Sequence](../../../traditional/lessons/algebra-i/668-the-nth-term-of-an-arithmetic-sequence.md)
- [Recursive Formulas for Arithmetic Sequences](../../../traditional/lessons/algebra-i/3695-recursive-formulas-for-arithmetic-sequences.md)

## Lesson

### Introduction

The explicit formula for the $n$th term of an arithmetic sequence is

$$


a_n = a_1 + (n-1)d, \quad n \geq 1.


$$

Every arithmetic sequence can also be written using the following recursive formula:

$$


𝑎


$$

For example, suppose that we're given the following explicit formula for an arithmetic sequence:

$$


a_n =2n+6, \quad n\geq 1


$$

To convert to a recursive formula, we just need to work out the first term and common difference. The first two terms are

$$


\begin{aligned}𝑎_{1} & =2(1)+6=8 \\ 𝑎_{2} & =2(2)+6=10,\end{aligned}


$$

and the common difference is

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =10−8 \\ & =2.\end{aligned}


$$

So, the first term is $a_1={\color{blue}8}$ and the common difference is $d={\color{red}2}.$ Therefore, the recursive formula is as follows:

$$


a_{n+1} = a_n + {\color{red}2}, \quad a_1 = {\color{blue}8}, \quad n \geq 1


$$

### Example: Converting an Explicit Formula to a Recursive Formula

#### Question

The formula for the $n$th term of an arithmetic sequence is $a_n = 1-2n$ for $n\geq 1.$ What is the recursive formula for this sequence?

#### Explanation

The recursive formula for an arithmetic sequence is as follows:

$$


a_{n+1} = a_n + d, \qquad a_1 = \_\_\_ \,, \qquad n \geq 1


$$

To complete the formula, we need to work out the first term and common difference. The first two terms are

$$


\begin{aligned}𝑎_{1} & =1−2(1)=−1 \\ 𝑎_{2} & =1−2(2)=−3\end{aligned}


$$

and the common difference is

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =−3−(−1) \\ & =−3+1 \\ & =−2.\end{aligned}


$$

So, the first term is $a_1={\color{blue}-1}$ and the common difference is $d={\color{red}-2}.$ Therefore, the recursive formula is as follows:

$$


a_{n+1}=a_n{\color{red}-2}, \qquad a_1={\color{blue}-1}, \qquad n\geq1


$$

### Example: Converting an Explicit Formula to a Recursive Formula Using Function Notation

#### Question

The formula for the $n$th term of an arithmetic sequence is $f(n) = 3n-11$ for $n\geq 1.$ What is the recursive formula for this sequence?

#### Explanation

The recursive formula for an arithmetic sequence is as follows:

$$


f(n+1) = f(n) + d, \qquad f(1) = \_\_\_ \,, \qquad n \geq 1


$$

To complete the formula, we need to work out the first term and common difference. The first two terms are

$$


\begin{aligned}𝑓(1) & =3(1)−11=−8 \\ 𝑓(2) & =3(2)−11=−5\end{aligned}


$$

and the common difference is

$$


\begin{aligned}𝑑 & =𝑓(2)−𝑓(1) \\ & =−5−(−8) \\ & =3.\end{aligned}


$$

So, the first term is $f(1)={\color{blue}-8}$ and the common difference is $d={\color{red}3}.$ Therefore, the recursive formula is as follows:

$$


f(n+1) = f(n) + {\color{red}3}, \qquad f(1) = {\color{blue}-8}, \qquad n \geq 1


$$

### Translating From the Recursive to the Explicit Formula

It's often more useful to translate from the recursive formula to an explicit one. So how do we find the explicit formula for the arithmetic sequence defined recursively as

$$


a_{n+1} = a_n + {\color{red}1},\, \quad a_1 = {\color{blue}6},\, \quad n\geq 1?


$$

The explicit formula is

$$


a_n = a_1 + (n-1)d, \quad n \geq 1,


$$

so we just need to determine the first term $a_1$ and the common difference $d.$

We are given that the first term is $a_1={\color{blue}6},$ and we can use the recursive rule to compute the second term, as follows:

$$


\begin{aligned}𝑎_{2} & =𝑎_{1}+1 \\ & =6+1 \\ & =7\end{aligned}


$$

Using the first and second terms, we can compute the common difference:

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =7−6 \\ & =1\end{aligned}


$$

Now, we substitute $a_1 = {\color{blue}6}$ and $d={\color{red}1}$ into the formula for the $n$th term:

$$


\begin{aligned} a_n&= a_{1}+(n-1)d \\[3pt] &= {\color{blue}6} + (n - 1)({\color{red}1}) \\[3pt] & =6 + n-1\\[3pt] &=n+5 \end{aligned}


$$

Therefore, the formula for the $n$th term is

$$


a_n=n+5, \quad n \geq 1.


$$

### Example: Converting a Recursive Formula to an Explicit Formula

#### Question

What is the explicit formula for the $n$th term of the arithmetic sequence

$$


a_{n+1} = a_n + 3,\, \qquad a_1 = -1,\, \qquad n\geq 1?


$$

#### Explanation

The explicit formula for the $n$th term of an arithmetic sequence is

$$


a_n = a_1 + (n-1)d, \quad n \geq 1,


$$

so we need to determine the first term $a_1$ and the common difference $d.$

We are given that the first term is $a_1 = {\color{blue}-1},$ and we can use the recursive rule to compute the second term, as follows:

$$


\begin{aligned}𝑎_{2} & =𝑎_{1}+3 \\ & =−1+3 \\ & =2\end{aligned}


$$

Using the first and second terms, we can compute the common difference:

$$


\begin{aligned}𝑑 & =𝑎_{2}−𝑎_{1} \\ & =2−(−1) \\ & =3\end{aligned}


$$

Now we substitute $a_1 = {\color{blue}-1}$ and $d={\color{red}3}$ into the formula for the $n$th term:

$$


\begin{aligned} a_n &= a_1+(n-1)d \\\[5pt] &= {\color{blue}-1} + (n - 1)({\color{red}3}) \\\[5pt] & =-1 + 3n - 3 \\\[5pt] &=3n - 4 \end{aligned}


$$

Therefore, the formula for the $n$th term is

$$


a_n=3n - 4, \qquad n \geq 1.


$$

### Example: Converting a Recursive Formula to an Explicit Formula Using Function Notation

#### Question

What is the explicit formula for the $n$th term of the sequence

$$


f(n+1) = f(n) - 5,\, \qquad f(1) = 3,\, \qquad n\geq 1?


$$

#### Explanation

The explicit formula for the $n$th term of an arithmetic sequence (in function notation) is

$$


f(n) = f(1) + (n-1)d, \quad n \geq 1,


$$

so we need to determine the first term $f(1)$ and the common difference $d.$

We are given that the first term is $f(1)={\color{blue}3},$ and we can use the recursive rule to compute the second term, as follows:

$$


\begin{aligned}𝑓(2) & =𝑓(1)−5 \\ & =3−5 \\ & =−2\end{aligned}


$$

Using the first and second terms, we can compute the common difference:

$$


\begin{aligned}𝑑 & =𝑓(2)−𝑓(1) \\ & =−2−3 \\ & =−5\end{aligned}


$$

Now we substitute $f(1) = {\color{blue}3}$ and $d={\color{red}-5}$ into the formula for the $n$th term:

$$


\begin{aligned} f(n)&= f(1)+(n-1)d \\\[5pt] &= {\color{blue}3} + (n - 1)({\color{red}-5}) \\\[5pt] & =3 - 5n + 5 \\\[5pt] &=8 - 5n \end{aligned}


$$

Therefore, the formula for the $n$th term is

$$


f(n)=8 - 5n, \qquad n \geq 1.


$$
