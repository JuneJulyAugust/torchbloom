# Permutations With Repetition

Source: https://www.mathacademy.com/topics/1341?courseId=109
Topic ID: 1341

## Prerequisites

- [Combinations](../../../high-school/traditional/lessons/geometry/705-combinations.md)

## Lesson

### Introduction

Suppose we wish to find the number of *distinct* permutations of the following letters:

$$



a, \qquad a, \qquad b, \qquad b, \qquad c



$$

There are two $a$'s, two $b$'s, and one $c,$ and a total of $5$ letters.

First, recall that there are $5!$ ways of arranging a sequence of $5$ objects. However, some arrangements will be the same since we have repeated letters. For example, we get the same final arrangement by swapping the first and the second positions in the sequence above.

If we were to list all arrangements of the above sequence by shuffling only the repeated letters among themselves (using suffixes to track the repeated letters), we get the following:

$$



\begin{aligned}𝑎_{1},\,𝑎_{2},\,𝑏_{1},\,𝑏_{2},\,𝑐 \\ 𝑎_{2},\,𝑎_{1},\,𝑏_{1},\,𝑏_{2},\,𝑐 \\ 𝑎_{1},\,𝑎_{2},\,𝑏_{2},\,𝑏_{1},\,𝑐 \\ 𝑎_{2},\,𝑎_{1},\,𝑏_{2},\,𝑏_{1},\,𝑐\end{aligned}



$$

Rearranging the $a$'s among themselves in any way will not change the final result, nor will rearranging the $b$'s and $c$'s.

Notice that we have $4$ ways of rearranging the letters among themselves:

- Since we have two $a$'s, there are $2!$ ways of arranging them.

- Since we have two $b$'s, there are $2!$ ways of arranging them.

- Since we have one $c$, there is only $1!=1$ way of arranging it.

In total, there are $2! \cdot 2! \cdot 1! = 4$ ways of arranging letters of our sequence if we can shuffle only the same letters among themselves.

So, to find the number of *distinct* permutations of our sequence, we need to divide the total number of arrangements $(5!)$ by the number of arrangements that do not change anything ($2! \cdot 2! \cdot 1!$):

$$



\dfrac{5!}{2! \cdot 2! \cdot 1!} = 30



$$

Therefore, there are $30$ distinct ways of arranging this sequence of letters.

### The General Formula

The number of permutations of $N$ symbols with $m_1, m_2,...,m_k$ repeated symbols is given by the **multinomial coefficient formula**:

$$



\begin{aligned}(\begin{matrix}𝑁 \\ 𝑚_{1},𝑚_{2},…,𝑚_{𝑘}\end{matrix})=\frac{𝑁!}{𝑚_{1}! 𝑚_{2}! … 𝑚_{𝑘}!},\end{aligned}



$$

where $m_1 + m_2 + \ldots + m_k = N.$

Let's see some more examples.

### Example: Computing the Number of Permutations With One Repeated Item

#### Question

How many distinct permutations can be formed using all letters of the word "FREE"?

#### Explanation

The number of permutations of $N$ symbols with $m_1, m_2,...,m_k$ repeated symbols is given by the multinomial formula:

$$



\begin{aligned}(\begin{matrix}𝑁 \\ 𝑚_{1},𝑚_{2},…,𝑚_{𝑘}\end{matrix})=\frac{𝑁!}{𝑚_{1}! 𝑚_{2}! … 𝑚_{𝑘}!},\end{aligned}



$$

where $m_1 + m_2 + \ldots + m_k = N.$

Here, the word "FREE" has $4$ letters in total, so $N=4.$

- The letter "F" appears once, so $m_1=1.$

- The letter "R" appears once, so $m_2=1.$

- The letter "E" appears twice, so $m_3=2.$

Therefore, the number of permutations is given by

$$



\begin{aligned}(\begin{matrix}4 \\ 1,1,2\end{matrix}) & =\frac{4!}{1! 1! 2!} \\ & =\frac{4×3×2×1}{2} \\ & =12.\end{aligned}



$$

### Example: Computing the Number of Permutations With Two Repeated Items

#### Question

How many distinct $7$-digit numbers can be formed using the numbers $2, 2, 2, 3, 4, 5, 5?$

#### Explanation

Each $7$-digit number is a permutation of the given numbers.

The number of permutations of $N$ symbols with $m_1, m_2,...,m_k$ repeated symbols is given by the multinomial formula:

$$



\begin{aligned}(\begin{matrix}𝑁 \\ 𝑚_{1},𝑚_{2},…,𝑚_{𝑘}\end{matrix})=\frac{𝑁!}{𝑚_{1}! 𝑚_{2}! … 𝑚_{𝑘}!},\end{aligned}



$$

where $m_1 + m_2 + \ldots + m_k = N.$

Here, we have $7$ numbers in total, so $N=7.$

- The number $2$ appears $3$ times, so $m_1=3.$

- The number $3$ appears once, so $m_2=1.$

- The number $4$ appears once, so $m_3=1.$

- The number $5$ appears twice, so $m_4=2.$

Therefore, the number of permutations is given by

$$



\begin{aligned}(\begin{matrix}7 \\ 3,1,1,2\end{matrix}) & =\frac{7!}{3! 1! 1! 2!} \\ & =\frac{7×6×5×4×3!}{3!×2} \\ & =420.\end{aligned}



$$

### Example: Computing the Number of Permutations With Three or More Repeated Items

#### Question

A hat store has $4$ baseball caps, $2$ sun hats, and $6$ berets in stock. In how many sequences can it sell all the hats?

#### Explanation

Each sequence in which the hats are sold is a permutation of the hats.

The number of permutations of $N$ symbols with $m_1, m_2,...,m_k$ repeated symbols is given by the multinomial formula:

$$



\begin{aligned}(\begin{matrix}𝑁 \\ 𝑚_{1},𝑚_{2},…,𝑚_{𝑘}\end{matrix})=\frac{𝑁!}{𝑚_{1}! 𝑚_{2}! … 𝑚_{𝑘}!},\end{aligned}



$$

where $m_1 + m_2 + \ldots + m_k = N.$

Here, we have $12$ hats in total, so $N=12.$

- There are $4$ baseball caps, so $m_1=4.$

- There are $2$ sun hats, so $m_2=2.$

- There are $6$ berets, so $m_3=6.$

Therefore, the number of permutations is given by

$$



\begin{aligned}(\begin{matrix}12 \\ 4,2,6\end{matrix}) & =\frac{12!}{4! 2! 6!} \\ & =\frac{12×11×10×9×8×7×6!}{4!×2!×6!} \\ & =\frac{12×11×10×9×8×7×6!}{4×3×2×2×6!} \\ & =\frac{6×2×11×10×9×8×7}{4×3×2×2} \\ & =13\,860.\end{aligned}



$$

### The Relationship Between the Multinomial and Binomial Formulas

The binomial formula is a special case of the multinomial formula. According to the binomial formula, the number of ways that we can choose $r$ objects from a set of $N$ objects is

$$



\binom{N}{r} = \dfrac{N!}{r! (N-r)!}.



$$

If we let $m_1 = r$ and $m_2 = N-r,$ then we have

$$



\binom{N}{r} = \dfrac{N!}{r! (N-r)!} = \dfrac{N!}{m_1! \, m_2!} = \binom{N}{m_1, m_2}.



$$
