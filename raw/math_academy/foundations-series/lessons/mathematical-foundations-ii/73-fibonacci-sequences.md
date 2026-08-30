# Fibonacci Sequences

Source: https://www.mathacademy.com/topics/73?courseId=111
Topic ID: 73

## Prerequisites

- [Recursive Sequences](./1226-recursive-sequences.md)

## Lesson

### Introduction

Consider the recursive sequence given by the formula

$$


a_{n+2}=a_{n+1}+a_n , \quad a_1 = {\color{blue}{1}}, \quad a_2 = {\color{red}{3}},\quad n \geq 1.


$$

As we know, to calculate the next term in a recursive sequence, we need to use the previous terms. However, unlike what we've seen before, this time, we need to use *two* previous terms to calculate the next term.

We already know $a_1$ and $a_2,$ so let's calculate $a_3.$ We do this by substituting $n=1$ into the recursive formula:

$$


\begin{aligned}𝑎_{1+2} & =𝑎_{1+1}+𝑎_{1} \\ 𝑎_{3} & =𝑎_{2}+𝑎_{1} \\ 𝑎_{3} & =3+1 \\ 𝑎_{3} & =4\end{aligned}


$$

Now that we know $a_3,$ we can calculate $a_4$ in the same way, by substituting $n=2$ into the formula:

$$


\begin{aligned}𝑎_{2+2} & =𝑎_{2+1}+𝑎_{2} \\ 𝑎_{4} & =𝑎_{3}+𝑎_{2} \\ 𝑎_{4} & =4+3 \\ 𝑎_{4} & =7\end{aligned}


$$

We can keep going by substituting $n=3, 4, 5,$ and so on. The resulting terms of the sequence are as follows:

$$


1, 3, 4, 7, 11, 18, 29, \ldots


$$

**Note:** The recursive rule $a_{n+2}=a_{n+1}+a_n$ gives us the **Fibonacci sequence** if we take $a_1=a_2=1.$

Recursive sequences that follow the rule $a_{n+2}=a_{n+1}+a_n$ but have different values for $a_1$ and $a_2$ are called *variants* of the Fibonacci sequence. So the sequence that we computed above is a variant of the Fibonacci sequence with $a_1=1$ and $a_2=3.$

### Example: Computing the Terms of a Fibonacci Sequence Given in Sequence Notation

#### Question

What is the fifth term in the Fibonacci sequence of numbers, defined by

$$


a_{n+2}=a_{n+1} + a_n, \quad a_1 = a_2 = 1, \quad n \geq 1?


$$

#### Explanation

The fifth term of the sequence corresponds to $a_5.$

To compute $a_5,$ we first need to compute $a_3.$ So, we substitute $n=1$ into the recursive formula, as follows:

$$


\begin{aligned}𝑎_{𝑛+2} & =𝑎_{𝑛+1}+𝑎_{𝑛} \\ 𝑎_{1+2} & =𝑎_{1+1}+𝑎_{1} \\ 𝑎_{3} & =𝑎_{2}+𝑎_{1} \\ 𝑎_{3} & =1+1 \\ 𝑎_{3} & =2\end{aligned}


$$

Next, to compute $a_4,$ we substitute $n=2$ into the recursive formula:

$$


\begin{aligned}𝑎_{2+2} & =𝑎_{2+1}+𝑎_{2} \\ 𝑎_{4} & =𝑎_{3}+𝑎_{2} \\ 𝑎_{4} & =2+1 \\ 𝑎_{4} & =3\end{aligned}


$$

We continue this process to compute $a_5,$ as follows:

$$


\begin{aligned}𝑎_{5} & =𝑎_{4}+𝑎_{3}=3+2=5\end{aligned}


$$

Therefore, the fifth term of the sequence is $a_5 = 5.$

### Example: Computing the Terms of a Fibonacci Sequence Given in Function Notation

#### Question

What is the fourth term of the sequence

$$


f(n+2)=f(n+1)+f(n) \,, \quad f(1)=-1\,, \quad f(2) = 3, \quad n \geq 1 ?


$$

#### Explanation

The fourth term is represented by $f(4).$

To compute $f(4),$ we first need to compute $f(3).$ So, we substitute $n=1$ into the recursive formula, as follows:

$$


\begin{aligned} f(n+2) & =f(n+1)+f(1) \\f(1+2) & =f(1+1)+f(1) \\f(3) & = f(2)+f(1) \\f(3) & = 3+(-1)\\f(3)&= 2 \end{aligned}


$$

Next, to compute $f(4),$ we substitute $n=2$ into the recursive formula:

$$


\begin{aligned} f(2+2) & =f(2+1)+f(2) \\f(4) & = f(3)+f(2) \\f(4) & = 2+3\\f(4)&= 5 \end{aligned}


$$

Therefore, the fourth term of the sequence is $f(4)=5.$
