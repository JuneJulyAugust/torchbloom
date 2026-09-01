# Cardinality of Finite Sets

Source: https://www.mathacademy.com/topics/48?courseId=145
Topic ID: 48

## Prerequisites

- [Determining Indexes of Terms in Arithmetic Sequences](../../../high-school/traditional/lessons/algebra-i/672-determining-indexes-of-terms-in-arithmetic-sequences.md)
- [Determining Indexes of Terms in Geometric Sequences](../../../high-school/traditional/lessons/algebra-i/685-determining-indexes-of-terms-in-geometric-sequences.md)
- [Solving Exponential Equations Using Logarithms](../../../high-school/traditional/lessons/algebra-ii/1482-solving-exponential-equations-using-logarithms.md)
- [Describing Sets Using Set-Builder Notation](./4393-describing-sets-using-set-builder-notation.md)

## Lesson

### Introduction

Recall that a set is **finite** if it contains a finite number of elements, while a set is **infinite** if it contains infinitely many elements.

The **cardinality** of a *finite* set $S,$ denoted $|S|,$ is the number of elements in $S.$

For example:

- The set $A,$ given by $A = \{a,b,c \}$ contains $3$ elements: So, its cardinality is $|A|=3$

- The set $B,$ given by $B = \{2, 4, \{6, 8\}, \emptyset\}$ contains $4$ elements: So, its cardinality is $|B| = 4.$

- The set $C,$ given by $C = \{5, 6, 6, 7, 8, 8, 8, 9 \}$ contains $5$ *unique* elements: So, its cardinality $|C| = 5.$

The cardinality of a set is sometimes called its **cardinal number.** So, the cardinal numbers of $A,B,$ and $C$ are $3,4,$ and $5,$ respectively.

Note that the empty set

$$


\emptyset = \{\}


$$

has cardinality $\left|\emptyset\right| = 0$ since it contains no elements. The empty set is the *only* set with cardinality zero.

Finally, you might be wondering about the cardinality of infinite sets. For example, what is the cardinality of the set of natural numbers?

$$


|\mathbb N| = |\{1,2,3,\ldots\}| = \,?


$$

When a set is infinite, we do *not* usually write $|\mathbb N| = \infty.$ The reason is that although $\mathbb N$ is infinite, so is $\mathbb R,$ and there is a sense in which $|\mathbb R|$ is "larger than" $|\mathbb N|.$ Thus, we need an entirely new system for labeling cardinalities of infinite sets. These ideas will be discussed at length in future lessons.

We'll consider finite sets only for the remainder of this lesson.

### Example: Finding the Cardinality of a Finite Set

#### Question

If $A = \{1, 1, 2,1, 3,3\}$, then what is $\left|A\right|?$

#### Explanation

The cardinality of a finite set $A$ is the number of elements in $A.$

Let's start by listing all the elements of $A{:}$

$$


1,\qquad 2, \qquad 3


$$

Note that only ** elements are counted. In other words, duplicate elements are ** counted separately.

Since $A$ has $3$ elements, its cardinality is $|A| = 3.$

### Example: Finding the Cardinality of a Set With Set Elements

#### Question

What is the cardinal number of $X = \{a, \emptyset, \{\emptyset\}, \{\{\emptyset\}\}, b \}?$

#### Explanation

The cardinality of a finite set $X$ is the number of elements in $X.$

Let's start by listing all the elements of $X{:}$

$$


a, \qquad \emptyset, \qquad \{\emptyset\}, \qquad \{\{\emptyset\}\}, \qquad b


$$

Note the following:

- Only ** elements are counted. In other words, duplicate elements are ** counted separately.

- $\emptyset, \{\emptyset\}$ and $\{\{\emptyset\}\}$ each count as single, distinct elements of $X.$

Since $X$ has $5$ elements, the cardinality is $|X| = 5.$

### Example: Sets Defined Using Arithmetic Sequences

#### Question

If $A = \{10, 19, 28,\ldots,865\},$ then what is $|A|?$

#### Explanation

The cardinality of a finite set $A$ is the number of elements in $A.$

Notice that the elements of our set

$$


10, \quad 19, \quad 28,\quad \ldots


$$

form an arithmetic sequence with a common difference $d=9{:}$

$$


\begin{aligned}𝑑 & =9 \\ & =19−10 \\ & =28−19 \\ & =⋯\end{aligned}


$$

The $n$th term of our arithmetic sequence, denoted $a_n,$ is given by

$$


\begin{aligned}𝑎_{𝑛} & =10+(𝑛−1)⋅9 \\ & =10+9𝑛−9 \\ & =9𝑛+1.\end{aligned}


$$

Therefore, we can express $A$ in set-builder notation as follows:

$$


\begin{aligned}𝐴 & ={9𝑛+1:𝑛∈ℕ,\,1≤𝑛≤𝑁}\end{aligned}


$$

where $N\in \mathbb N$ is to be determined.

To find $N,$ we solve the following equation:

$$


\begin{aligned}9𝑁+1 & =865 \\ 9𝑁 & =864 \\ 𝑁 & =\frac{864}{9} \\ 𝑁 & =96\end{aligned}


$$

Therefore, our set $A$ can be expressed as

$$


A = \left\{9n+1: n\in \mathbb N,\: 1\leq n \leq 96 \right\}.


$$

Finally, since $A$ has $96$ elements, we must have $|A| = 96.$

### Example: Sets Defined Using Geometric Sequences

#### Question

If $A = \{3, 21, 147,1\,029,\ldots,5\,931\,980\,229\},$ then what is $|A|?$

#### Explanation

The cardinality of a finite set $A$ is the number of elements in $A.$

Notice that the elements of our set

$$


3, \quad 21, \quad 147, \quad 1\,029,\quad \ldots


$$

form a geometric sequence with a common ratio $r=7{:}$

$$


\begin{aligned}𝑟 & =7 \\ & =\frac{21}{3} \\ & =\frac{147}{21} \\ & =⋯\end{aligned}


$$

The $n$th term of our geometric sequence, denoted $a_n,$ is given by

$$


a_n = a_1 r^{n-1} = 3(7^{n-1}) = \dfrac37(7)^n.


$$

Therefore, we can express $A$ in set-builder notation as follows:

$$


A = \left\{\dfrac37(7)^n : n\in \mathbb N,\: 1\leq n \leq N \right\}


$$

where $N\in \mathbb N$ is to be determined.

To find $N,$ we solve the following equation:

$$


\begin{aligned}\frac{3}{7}(7)^{𝑁} & =5\,931\,980\,229 \\ 7^{𝑁} & =13\,841\,287\,201 \\ 𝑁 & =log_{7}⁡(13\,841\,287\,201) \\ 𝑁 & =\frac{log_{10}⁡(13\,841\,287\,201)}{log_{10}⁡(7)} \\ 𝑁 & =12\end{aligned}


$$

Therefore, our set $A$ can be expressed as

$$


A = \left\{\dfrac37(7)^n : n\in \mathbb N,\: 1\leq n \leq 12\right\}.


$$

Finally, since $A$ has $12$ elements, we must have $|A| = 12.$
