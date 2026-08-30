# Finding Lowest Common Multiples Using Prime Factorization

Source: https://www.mathacademy.com/topics/755?courseId=113
Topic ID: 755

## Prerequisites

- [The Fundamental Theorem of Arithmetic](./4250-the-fundamental-theorem-of-arithmetic.md)

## Lesson

### Introduction

The **lowest common multiple** (or $\textrm{LCM}$) of two integers is the smallest multiple that's common to both numbers.

To find the lowest common multiple of two small numbers, we can list all multiples of the two numbers and identify the smallest multiple that they have in common.

For example, let's find the lowest common multiple of $4$ and $6.$ We start by listing all multiples of $4$ and $6\mathbin{:}$

$$


\begin{aligned}4 & \,→\,04,\,08,\,12,\,16,\,20,\,24,\,… \\ 6 & \,→\,06,\,12,\,18,\,24,\,30,\,36,\,…\end{aligned}


$$

The smallest multiple in both lists is $12$ So $12$ is our answer, and we can write

$$


\textrm{LCM}(4,6)= 12.


$$

**Note:** The lowest common multiple is also sometimes called the *least* common multiple.

### Finding the Lowest Common Multiple of Two Larger Numbers

Now suppose that we want to find the lowest common multiple of two larger numbers. It would take a while to make long lists of multiples. Luckily, there is a faster method.

Let's demonstrate by finding $\textrm{LCM}(10,12).$ We start by writing the prime factorization of $10$ and $12$, writing any repeating factors as powers:

$$


\begin{aligned}10 & =2⋅5=2^{1}⋅5^{1} \\ 12 & =2⋅2⋅3=2^{2}⋅3^{1}\end{aligned}


$$

Then, we write down each unique prime factor that appears in either of our decompositions. In our case, the unique prime factors are

$$


{\color{red}2}, \qquad {\color{red}3}, \qquad {\color{red}5}.


$$

Now, for each number in our list, we look at *both* prime factorizations and we take the *largest* power shown for each prime factor:

- The factors corresponding to ${\color{red}2}$ are ${\color{red}2}^{\color{blue}1}$ and ${\color{red}2}^{\color{blue}2}.$ Of these, the larger power is ${\color{red}2}^{\color{blue}2}.$

- There is only one factor corresponding to ${\color{red}3}.$ It is ${\color{red}3}^{\color{blue}1}.$

- There is only one factor corresponding to ${\color{red}5}.$ It is ${\color{red}5}^{\color{blue}1}.$

Finally, we multiply the largest powers of each factor together, and we get

$$


\begin{aligned}LCM(10,12) & =2^{2}⋅3^{1}⋅5^{1} \\ & =4⋅3⋅5 \\ & =60.\end{aligned}


$$

### Example: Finding the Lowest Common Multiple of Two Integers

#### Question

Calculate $\textrm{LCM}(120, 90).$

#### Explanation

To find the lowest common multiple of two numbers, we first find the prime factorization of both numbers.

- We start by finding the prime factorization of $120\mathbin{:}$ Therefore, $120 = 2^3 \cdot 3 \cdot 5.$

- Next, we find the prime factorization of $90\mathbin{:}$ Therefore, $90 = 2 \cdot 3^2 \cdot 5.$

So, we have the following prime factorizations:

$$


\begin{aligned}120 & =2^{3}⋅3⋅5 \\ 90 & =2⋅3^{2}⋅5\end{aligned}


$$

Now, we write down every prime factor that is shown above, and we raise each prime factor to the highest power given in either factorization:

- the highest power of $2$ is $3$

- the highest power of $3$ is $2$

- the highest power of $5$ is $1$

Therefore, the lowest common multiple of $120$ and $90$ is

$$


\textrm{LCM}(120, 90) = 2^3 \cdot 3^2 \cdot 5 = 360.


$$

### Example: Finding the Lowest Common Multiple of Three Integers

#### Question

Calculate $\textrm{LCM}(30, 33, 20).$

#### Explanation

To find the lowest common multiple of three numbers, we first find their prime factorizations.

- We start by finding the prime factorization of $30\mathbin{:}$ Therefore, $30 = 2 \cdot 3 \cdot 5.$

- Next, we find the prime factorization of $33.$ We easily deduce that $33 = 3 \cdot 11.$

- Then, we find the prime factorization of $20{:}$ Therefore, $20=2^2 \cdot 5.$

So, we have the following prime factorizations:

$$


\begin{aligned}30 & =2⋅3⋅5 \\ 33 & =3⋅11 \\ 20 & =2^{2}⋅5\end{aligned}


$$

Now, we write down every prime factor that is shown above, and we raise each prime factor to the highest power given in any of the factorizations:

- the highest power of $2$ is $2$

- the highest power of $3$ is $1$

- the highest power of $5$ is $1$

- the highest power of $11$ is $1$

Therefore, the lowest common multiple of $30$, $33,$ and $20$ is

$$


\textrm{LCM}(30, 33, 20) = 2^2 \cdot 3 \cdot 5 \cdot 11 = 660.


$$

### Example: Finding the Lowest Common Denominator of Two Fractions

#### Question

Find the lowest common denominator of $\dfrac{4}{45}$ and $\dfrac{7}{48}.$

#### Explanation

The lowest common denominator of two fractions is the least common multiple of the denominators.

So, to find the lowest common denominator of two fractions, we first find the prime factorization of both denominators.

- We start by finding the prime factorization of $45\mathbin{:}$ Therefore, $45= 3^2 \cdot 5.$

- Next, we find the prime factorization of $48{:}$ Therefore, $48 = 2^4 \cdot 3.$

So, we have the following prime factorizations:

$$


\begin{aligned}45 & =3^{2}⋅5 \\ 48 & =2^{4}⋅3\end{aligned}


$$

Now, we write down every prime factor that is shown above, and we raise each prime factor to the highest power given in either factorization:

- the highest power of $2$ is $4$

- the highest power of $3$ is $2$

- the highest power of $5$ is $1$

Therefore, the lowest common denominator is $2^4\cdot 3^2 \cdot 5 = 720.$
