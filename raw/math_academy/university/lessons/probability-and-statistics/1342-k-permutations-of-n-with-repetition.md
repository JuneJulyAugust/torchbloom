# K Permutations of N With Repetition

Source: https://www.mathacademy.com/topics/1342?courseId=73
Topic ID: 1342

## Prerequisites

- [Permutations](../../../high-school/traditional/lessons/geometry/703-permutations.md)

## Lesson

### Introduction

Suppose we have the letters $a,b,c,$ and we want to count the number of two-letter permutations that can be formed, where each of the given letters can be repeated.

- We have $3$ choices for the first letter: $a,b,$ or $c.$

- Likewise, we have $3$ choices for the second letter: $a,b,$ or $c.$

The total number of two-letter permutations that can be formed is given by the product

$$


3 \times 3 = 3^2 = 9.


$$

To verify that we are correct, we can list out the $9$ permutations below:

$$


\begin{aligned}𝑎𝑎 & 𝑎𝑏 & 𝑎𝑐 \\ 𝑏𝑎 & 𝑏𝑏 & 𝑏𝑐 \\ 𝑐𝑎 & 𝑐𝑏 & 𝑐𝑐\end{aligned}


$$

In general, the number of permutations of $k$ items chosen from a set of $n$ with repetition is $n^k.$

To see why, remember that we have $n$ choices for the first item, $n$ choices for the second item, and so on for all $k$ items. So, by the multiplication principle, the total number of permutations is given by the following product:

$$


\underbrace{n \times n \times \cdots \times n}_{\large k \textrm{ times}} = n^k


$$

### Example: Counting How Many Numbers Can be Formed Given Some Digits

#### Question

How many two-digit numbers can be formed with the digits $2,4,6,8?$ Each of the listed digits can be repeated several times.

#### Explanation

The number of permutations of $k$ items chosen from a set of $n$ with repetition is $n^k.$

Here, we want to count how many two-digit numbers can be formed from a set of $4$ digits ($2,4,6,8$) with repetition.

This is equal to the number of permutations of $2$ items chosen from a set of $4$ with repetition, which is

$$


4^2 = 16.


$$

### Example: Counting How Many Numbers Can Be Formed Given Some Digits When One Digit Is Zero

#### Question

How many four-digit numbers can be formed with the digits $0,1,2,3,4,5$ if each of the listed digits can be repeated several times? Take into account that the numbers cannot start with zero.

#### Explanation

Let's consider the first digit separately from the last three digits.

- For the first digit, we have $5$ possibilities ($1,2,3,4,5$ - zero is excluded).

- For each of last three digits, there are $6$ possibilities ($0,1,2,3,4,5$). The number of ways to choose the last three digits is equal to the number of permutations of $3$ items chosen from a set of $6$ with repetition, which is $6^3.$

So, the total number of possible four-digit numbers is

$$


\begin{aligned}5×6^{3} & =5×216 \\ & =1\,080.\end{aligned}


$$

### Example: Counting How Many Permutations Can be Formed Using Numbers, Letters, and Colors

#### Question

A password consists of $3$ digits chosen from $0$ to $9$ followed by two letters of the English alphabet containing $26$ letters. Both digits and letters can be repeated. How many different possible passwords are there?

#### Explanation

Let's consider the digits and the letters separately.

- For each of the three digits, there are $10$ possibilities ($0,1,2, \ldots, 9$). The number of ways to choose three digits is equal to the number of permutations of $3$ items chosen from a set of $10$ with repetition, which is $10^3.$

- For each of the two letters of the alphabet, there are $26$ possibilities ($a,b,c, \ldots, z$). The number of ways to choose two letters is equal to the number of permutations of $2$ items chosen from a set of $26$ with repetition, which is $26^2.$

Therefore, the number of possible passwords is given by

$$


\begin{aligned}10^{3}×26^{2} & =1\,000×676 \\ & =676\,000.\end{aligned}


$$

### Example: Counting How Many Numbers Can be Formed Using Digits Containing a Duplicate

#### Question

How many distinct two-digit numbers can be formed with the digits $1,1, 2, 3?$

#### Explanation

First, we find how many two-digit numbers can be formed using the digits $1,2,3$ with repetition. This is equal to the number of permutations of $2$ items chosen from a set of $3$ with repetition, which is

$$


3^2=9.


$$

Now, we take into account that only the digit $1$ can be repeated. The other digits, $2$ and $3,$ cannot be repeated, because they appear only once in the given list $1,1,2,3.$ Consequently, the numbers $22$ and $33$ should be excluded from consideration.

Excluding these $2$ numbers from consideration, the remaining number of possibilities is

$$


9-2=7.


$$
