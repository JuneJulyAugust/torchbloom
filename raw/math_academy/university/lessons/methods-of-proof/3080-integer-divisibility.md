# Integer Divisibility

Source: https://www.mathacademy.com/topics/3080?courseId=76
Topic ID: 3080

## Prerequisites

- [Negating Quantified Statements](./2791-negating-quantified-statements.md)
- [Parity](./3411-parity.md)

## Lesson

### Introduction

Suppose $a$ and $b$ are integers where $a\neq 0.$ We say that $\boldsymbol a$ **divides** $\boldsymbol b$ and write

$$


a\mid b


$$

if there exists an integer $k$ such that

$$


b = ka.


$$

We can write this more formally as follows:

$$


a\mid b \qquad \Leftrightarrow\qquad \exists k \in \mathbb Z, b = ka


$$

For example, $2\mid 8$ because there exists an integer ${\color{blue}{k}} = {\color{blue}{4}}$ such that

$$


8 = {\color{blue}{4}}\cdot 2.


$$

### Example: Stating the Definition of Integer Divisibility

#### Question

Fill in the blanks so that the following reasoning is correct:

The notation $3 \mid 18$ means $3/𝑑𝑖𝑣𝑖𝑑𝑒𝑠//18$ It is equivalent to the statement that there exists $𝑎𝑛//𝑖𝑛𝑡𝑒𝑔𝑒𝑟$ such that $18=3.𝑘///$

#### Explanation

The notation $a \mid b$ means $a$ divides $b.$ So, $3 \mid 18$ means $3$

According to the definition of integer divisibility, the fact that $a$ divides $b$ means that there exists an integer $k$ such that

$$


b=a k.


$$

Therefore, $3 \mid 18$ is equivalent to the statement that there exists $\boxed{\color{blue}\text{an integer}}$ $k$ such that $\boxed{\color{blue}18 = 3k}.$

### Non-Divisibility

We have the following definition of integer divisibility.

$$


a\mid b \qquad \Leftrightarrow\qquad \exists k \in \mathbb Z, b = ka


$$

If $a$ **does not divide** $b,$ we write $a\not\mid b.$ Therefore, by negating the two statements above, we get the following equivalence:

$$


\begin{aligned}¬(𝑎∣𝑏)\, & ⇔\,¬(∃𝑘∈ℤ,𝑏=𝑘𝑎) \\ 𝑎∤𝑏\, & ⇔\,∀𝑘∈ℤ,𝑏≠𝑘𝑎\end{aligned}


$$

Thus, $a\not\mid b$ means that $b \neq ak$ *for all* integers $k.$

For example, $3\not \mid 8$ because there does not exist an integer ${\color{red}{k_2}}$ such that

$$


8 = {\color{red}{k_2}}\cdot 3.


$$

### Example: Stating the Definition of Non-Divisibility

#### Question

Fill in the blanks so that the following reasoning is correct:

The notation $5 \not\mid 16$ means $5𝑑𝑜𝑒𝑠𝑛𝑜𝑡𝑑𝑖𝑣𝑖𝑑𝑒𝑠//16$ It is equivalent to the statement that for $\\[6pt]$ $////𝑓𝑜𝑟𝑎𝑛𝑦$ $𝑎𝑛//𝑖𝑛𝑡𝑒𝑔𝑒𝑟$ we have $16=/=5.𝑘///$

#### Explanation

The notation $a \not\mid b$ means $a$ does not divide $b.$ So, $5 \not\mid 16$ means $5$

According to the definition of integer divisibility, the fact that $a$ does not divide $b$ means that for any integer $k,$ we have that

$$


b \neq a k.


$$

Therefore, $5 \not\mid 16$ is equivalent to the statement that for $\boxed{\color{blue}\text{any}}$ $\boxed{\color{blue}\text{integer}}$ $k,$ we have $\boxed{\color{blue}16 \neq 5k}.$

### Example: Inferring Divisibility in Algebraic Expressions

#### Question

Which of the following statements must be true for any integers $x$ and $y?$

1. $4 \mid (6x+9y)$

2. $5 \mid (6x+9y)$

3. $3 \mid (6x+9y)$

#### Explanation

The notation $a \mid b$ means $a$ divides $b.$

According to the definition of integer divisibility, the fact that $a$ divides $b$ means that there exists an integer $k$ such that

$$


b=a k.


$$

With that in mind, let's examine our statement in turn.

- Statement I is false. For example, if $x=0$ and $y=1,$ we have $6(0)+9(1) = 9,$ which is not divisible by $4.$

- Statement II is false. For example, if $x=1$ and $y=0,$ we have $6(1)+9(0) = 6,$ which is not divisible by $5.$

- Statement III is true. Notice that Since $x$ and $y$ are integers, $2x+3y$ must be an integer, too. So, $3 \mid (6x+9y).$

Therefore, the correct answer is "III only."
