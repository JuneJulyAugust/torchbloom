# Computing Probabilities Using Combinatorics

Source: https://www.mathacademy.com/topics/132?courseId=128
Topic ID: 132

## Prerequisites

- [Combinations](../geometry/705-combinations.md)
- [The Complement of an Event](../geometry/1120-the-complement-of-an-event.md)

## Lesson

### Introduction

Sometimes, when calculating probabilities, we have to use our knowledge of permutations. We do this when the order of occurrences in the event matters.

For instance, suppose we create a $3$-digit number from the digits $1,$ $2,$ $3,$ and $4,$ without repetition. What is the probability that our number starts with $1?$

Let $A$ represent the event that our number starts with $1.$ We can use the formula

$$


3


$$

First, let's calculate the total number of ways to choose a $3$-digit number using the digits $1,$ $2,$ $3,$ and $4$ without repetition. From $4$ digits, we choose $3$ of them, and since the order of the digits matters, we use permutations:

$$


N = {}_{4}P_3 = \dfrac{4!}{(4-3)!} = 24


$$

Then, we calculate the number of ways to choose a $3$-digit number starting with $1.$ The first digit has to be $1,$ and so to form the rest of the number, we can choose another $2$ digits out of the remaining $3.$ Again, since the order of the digits matters, we use permutations:

$$


n = {}_{3}P_2 = \dfrac{3!}{(3-2)!} = \dfrac{3!}{1!} = 6


$$

Therefore, using the formula, the probability is

$$


P(A) = \dfrac{n}{N} = \dfrac{6}{24} = \dfrac{1}{4} = 25\%.


$$

### Example: Computing Probabilities Using Permutations

#### Question

What is the probability that if a random $4$-digit number is created using the digits $1$ through $9$ (but ** $0$), no digits are repeated?

#### Explanation

Let $A$ represent the event described in the question. Then

$$


\begin{aligned}𝑃(𝐴) & =\frac{𝑛}{𝑁},\end{aligned}


$$

where $N$ is the total number of $4$-digit numbers that can be created from the $9$ digits, and $n$ is the number of those $4$-digit numbers in which no digits are repeated.

First, we compute $N.$ We want to count how many $4$-digit numbers can be formed from a set of $9$ digits with repetition. This is equal to the number of permutations of $4$ items chosen from a set of $9$ with repetition, which is

$$


N = 9^4 = 6\,561.


$$

Now, we compute $n.$ To create a $4$-digit number from the $9$ digits where no digits are repeated, we choose $4$ of the $9$ possible digits. Since the order of the digits matters, we use permutations:

$$


\begin{aligned}𝑛=_{9}𝑃_{4} & =\frac{9!}{5!}=3\,024\end{aligned}


$$

Finally, we have

$$


\begin{aligned}𝑃(𝐴) & =\frac{3\,024}{6\,561}≈0.46=46\%.\end{aligned}


$$

### Computing Probabilities Using Combinations

When the order of occurrences in an event does *not* matter, we use combinations instead of permutations.

For example, suppose that in a game, a player must draw two tiles randomly from a bag. Each tile is labeled with a letter from either $a,$ $b,$ $c,$ or $d,$ and there are five tiles of each letter (so a total of $20$ tiles). What is the probability that both of the player's tiles are labeled with the letter $a?$

Let $A$ represent the event described in the question. Then

$$


P(A) = \dfrac{n}{N},


$$

where $N$ is the total number of ways to pick $2$ tiles out of $20,$ and $n$ is the number of those $2$-tile picks where both tiles have the letter $a.$

Note that since the order of the picks does not matter, we must use combinations.

First, we compute $N.$ The number of ways to draw $2$ tiles from a total of $20$ is

$$


N = {}_{20}C_2 = \dfrac{20!}{2!\cdot 18!} = 190.


$$

Now, we compute $n.$ There are $5$ tiles with the letter $a,$ so the number of ways to choose $2$ of those tiles (out of $5$) is

$$


n = {}_{5}C_2 = \dfrac{5!}{2!\cdot 3!} = 10.


$$

Finally,

$$


P(A) = \dfrac{10}{190} = \dfrac{1}{19}.


$$

### Example: Computing Probabilities Using Combinations

#### Question

A club has only $4$ female and $6$ male members. Two members are to be chosen at random to represent the club at an event. What is the probability that those chosen will both be women?

#### Explanation

Let $A$ denote the event described in the question. Then

$$


\begin{aligned}𝑃(𝐴) & =\frac{𝑛}{𝑁},\end{aligned}


$$

where $N$ is the total number of ways to select $2$ persons out of $10,$ and $n$ is the number of ways to select exactly $2$ women.

Note that since the order of the selections does not matter, we use combinations.

First, we compute $N.$ The number of ways to select $2$ persons out of a total of $10$ is

$$


\begin{aligned}𝑁=_{10}𝐶_{2} & =\frac{10!}{2!⋅8!}=45.\end{aligned}


$$

Now, we compute $n.$ A total of $4$ club members are women, so the number of ways to choose $2$ women (out of $4$) is

$$


\begin{aligned}𝑛=_{4}𝐶_{2}=\frac{4!}{2!⋅2!}=6.\end{aligned}


$$

Finally, we obtain

$$


\begin{aligned}𝑃(𝐴) & =\frac{𝑛}{𝑁}=\frac{6}{45}=\frac{2}{15}\end{aligned}


$$

### Example: Further Computing Probabilities Using Combinations

#### Question

In a game, a player must draw five tiles randomly from a bag. Each tile is labeled with a letter $a,$ $b,$ or $c,$ and there are four tiles of each letter (so a total of $12$ tiles). What is the probability that the player gets $2$ tiles with the letter $b$ and $3$ tiles with the letter $c?$ Round your answer to the nearest percent.

#### Explanation

Let $A$ represent the event described in the question. Then

$$


P(A) = \dfrac{n}{N},


$$

where $N$ is the total number of ways to pick $5$ tiles out of $12,$ and $n$ is the number of those $5$-tile picks where $2$ tiles have the letter $b$ and $3$ tiles have the letter $c.$

Note that since the order of the picks does not matter, we must use combinations.

First, we compute $N.$ The number of ways to draw $5$ tiles from a total of $12$ is

$$


N = {}_{12}C_5 = \dfrac{12!}{5!\cdot 7!} = 792.


$$

Now, we compute $n.$ The computation of $n$ can be divided into two steps:

- the number of ways to choose $2$ (out of $4$) tiles with the letter $b$ is

- the number of ways to choose $3$ (out of $4$) tiles with the letter $c$ is

Multiplying the results from the above steps, we get

$$


n = {}_4 C_2 \cdot {}_4 C_3 = 6 \cdot 4 = 24.


$$

Finally,

$$


P(A) = \dfrac{24}{792} \approx 0.03=3\%.


$$

### Example: Computing Probabilities Using the Complement

#### Question

What is the probability that among $4$ randomly chosen people whose birthdays are all in the last full week of September, at least two will have birthdays on the same day? Round your answer to $3$ decimal places.

#### Explanation

Let $A$ denote the event that at least two of the people have birthdays on the same day. In this case, it would be easier to find $P(A'),$ where the complement $A'$ represents the event when all of the people have their birthdays on different days.

The probability of the complement can be computed as

$$


P(A') = \dfrac{n}{N},


$$

where $N$ is the total number of ways to assign a day of the week to each person, and $n$ is the number of ways to assign a ** day of the week to each person.

To assign a unique day to each of the $4$ people, we must choose $4$ days out of $7,$ where the order matters. The number of ways to do this is

$$


n = {}_{7}P_4 = \dfrac{7!}{3!} = 840.


$$

On the other hand, if the same day can be assigned to different people, we have $7$ ways to assign a day for the first person, $7$ for the second, $7$ for the third, and $7$ for the fourth person. Multiplying these choices together, we get

$$


N = 7 \cdot 7 \cdot 7 \cdot 7 = 2401.


$$

Finally, the probability of the complement is

$$


P(A') = \dfrac{n}{N} = \dfrac{840}{2\, 401} \approx 0.350


$$

rounded to $3$ decimal places.

Therefore, we have

$$


\begin{aligned}𝑃(𝐴) & =1−𝑃(𝐴^{′}) \\ & ≈1−0.350 \\ & =0.650\end{aligned}


$$

rounded to $3$ decimal places.
