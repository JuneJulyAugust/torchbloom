# Double Summations

Source: https://www.mathacademy.com/topics/1983?courseId=54
Topic ID: 1983

## Prerequisites

- [Properties of Finite Series](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/3958-properties-of-finite-series.md)

## Lesson

### Introduction

Recall that we use **sigma notation** to write sums concisely. For example,

$$


\displaystyle \sum_{i=1}^n a_i


$$

refers to the sum of all terms in the sequence $a_i,$ where the **index** $i$ ranges from $1$ to $n\mathbin{:}$

$$


\sum_{i=1}^n a_i = a_1+a_2+\cdots+a_n


$$

Sigma notation can also represent sums whose terms depend on two indices. That is, **double sums** of the form

$$


\displaystyle \sum_{i=1}^m \sum_{j=1}^n a_{ij}


$$

where $i$ ranges from $1$ to $m,$ and $j$ ranges from $1$ to $n\mathbin.$ Thus, a double summation is just a "sum of a sum."

In calculating double summations, we follow two steps:

- First, we evaluate the inner sum by fixing the index of the outer sum ($i$) and incrementing only the inner index ($j$).

- Next, we evaluate the outer sum by incrementing the outer sum index.

To illustrate how it works, suppose we are given the following double sum:

$$


\sum_{i=1}^2 \sum_{j=1}^4 (i+j)


$$

To compute this double sum, we can proceed as follows:

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}\underset{\underset{𝑗=1}{∑}}{\overset{}{4}}(𝑖+𝑗) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}[(\underset{\underset{𝑗=1}{∑}}{\overset{}{4}}(𝑖+𝑗))] \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}[(𝑖+1)+(𝑖+2)+(𝑖+3)+(𝑖+4)] \\ & =\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}(4𝑖+10) \\ & =4(1)+10+4(2)+10 \\ & =4+10+8+10 \\ & =32\end{aligned}


$$

Later, we will provide some formulas that will help us simplify many double summations calculations.

### Example: Computing a Double Summation

#### Question

Evaluate $\displaystyle \sum_{j=1}^3\sum_{i=1}^2 (i+j).$

#### Explanation

First, we write out the inner summation by summing over the index $i\mathbin{:}$

$$


\begin{aligned}\underset{\underset{𝑗=1}{∑}}{\overset{}{3}}\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}(𝑖+𝑗) & =\underset{\underset{𝑗=1}{∑}}{\overset{}{3}}[\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}(𝑖+𝑗)] \\ & =\underset{\underset{𝑗=1}{∑}}{\overset{}{3}}[(1+𝑗)+(2+𝑗)] \\ & =\underset{\underset{𝑗=1}{∑}}{\overset{}{3}}(3+2𝑗)\end{aligned}


$$

Then, we calculate the sum above by summing over the index $j\mathbin{:}$

$$


\begin{aligned}\underset{\underset{𝑗=1}{∑}}{\overset{}{3}}(3+2𝑗) & =(3+2⋅1)+(3+2⋅2)+(3+2⋅3) \\ & =5+7+9 \\ & =21\end{aligned}


$$

### The Sum and Constant Multiple Rules

Double summations satisfy the following properties:

**The Constant Multiple Rule**

We can factor out a constant multiple from a double summation:

$$


\displaystyle\sum_{i=1}^m\sum_{j=1}^n k a_{ij} = k\sum_{i=1}^m\sum_{j=1}^n a_{ij}


$$

**The Sum Rule**

We can distribute a double summation over a sum of terms.

$$


\displaystyle\sum_{i=1}^m\sum_{j=1}^n (a_{ij} + b_{ij}) = \sum_{i=1}^m\sum_{j=1}^n a_{ij} + \sum_{i=1}^m\sum_{j=1}^n b_{ij}


$$

**The Double Sum of Units**

Recall that for single summations, we have

$$


\sum_{j=1}^{n} 1 = \underbrace{1+1+\cdots+1}_{n\text{ times}} = n.


$$

Analogously for double summations, we have that

$$


\sum_{i=1}^m\sum_{j=1}^n 1 = mn.


$$

### Example: Applying the Sum and Constant Multiple Rules

#### Question

Find the value of the double sum

$$


\sum_{i=1}^{5} \sum_{j=1}^{8} (1+2a_{ij}-b_{ij})


$$

given that

$$


\sum_{i=1}^{5} \sum_{j=1}^{8} a_{ij} = 8, \qquad\sum_{i=1}^{5} \sum_{j=1}^{8} b_{ij} = 15.


$$

#### Explanation

The sum and constant multiple rules for double summations state that

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}(𝑎_{𝑖𝑗}+𝑏_{𝑖𝑗}) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑎_{𝑖𝑗}+\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑏_{𝑖𝑗}, \\ \underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑘𝑎_{𝑖𝑗} & =𝑘\underset{\underset{𝑖=1}{∑}}{\overset{}{𝑚}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛}}𝑎_{𝑖𝑗}.\end{aligned}


$$

Applying the sum rule to the given double summation, we have

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}(1+2𝑎_{𝑖𝑗}−𝑏_{𝑖𝑗}) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}1+\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}2𝑎_{𝑖𝑗}−\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}𝑏_{𝑖𝑗} \\ & =(\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}1)+2\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}𝑎_{𝑖𝑗}−\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}𝑏_{𝑖𝑗} \\ & =(\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}1)+2(8)−15 \\ & =(\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}1)+1.\end{aligned}


$$

Now, using the fact that

$$


\sum_{i=1}^m\sum_{j=1}^n 1 = mn,


$$

we have

$$


\begin{aligned}(\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}\underset{\underset{𝑗=1}{∑}}{\overset{}{8}}1)+1 & =5⋅8+1 \\ & =40+1 \\ & =41.\end{aligned}


$$

So, we conclude that

$$


\sum_{i=1}^{5} \sum_{j=1}^{8} (1+2a_{ij}-b_{ij}) = 41.


$$

### The Product and Swap Rules

In addition, we have the following useful rules:

**The Product Rule**

We can distribute a double summation over a product of *single-index* terms with *different* indices.

$$


\displaystyle\sum_{i=1}^m\sum_{j=1}^n a_{i}b_j = \sum_{i=1}^m a_i \sum_{j=1}^n b_{j}


$$

**The Swap Rule**

We can swap the order of summations in a double summation.

$$


\displaystyle\sum_{i=1}^m\sum_{j=1}^n a_{ij}= \sum_{j=1}^n\sum_{i=1}^m a_{ij}


$$

### Example: Applying the Product Rule and Swap Rules

#### Question

Find the value of the double sum

$$


\displaystyle \sum_{i=1}^{15} \sum_{j=1}^{18} (a_{i} - 2)( b_{j}+1)


$$

given that

$$


\displaystyle \sum_{i=1}^{15}a_i = 40, \qquad \displaystyle \sum_{j=1}^{18}b_j =-8 .


$$

#### Explanation

The product rule for double summations states that

$$


\displaystyle\sum_{i=1}^m\sum_{j=1}^n a_{i}b_j = \sum_{i=1}^m a_i \sum_{j=1}^n b_{j}.


$$

So, using the product rule for double summations, we get

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{15}}\underset{\underset{𝑗=1}{∑}}{\overset{}{18}}(𝑎_{𝑖}−2)(𝑏_{𝑗}+1) & =\underset{\underset{𝑖=1}{∑}}{\overset{}{15}}(𝑎_{𝑖}−2)\underset{\underset{𝑗=1}{∑}}{\overset{}{18}}(𝑏_{𝑗}+1).\end{aligned}


$$

Now, using the rules for single summations, we obtain

$$


\begin{aligned}\underset{\underset{𝑖=1}{∑}}{\overset{}{15}}(𝑎_{𝑖}−2)\underset{\underset{𝑗=1}{∑}}{\overset{}{18}}(𝑏_{𝑗}+1) & =(\underset{\underset{𝑖=1}{∑}}{\overset{}{15}}𝑎_{𝑖}−\underset{\underset{𝑖=1}{∑}}{\overset{}{15}}2)⋅(\underset{\underset{𝑗=1}{∑}}{\overset{}{18}}𝑏_{𝑗}+\underset{\underset{𝑗=1}{∑}}{\overset{}{18}}1) \\ & =(\underset{\underset{𝑖=1}{∑}}{\overset{}{15}}𝑎_{𝑖}−2\underset{\underset{𝑖=1}{∑}}{\overset{}{15}}1)⋅(\underset{\underset{𝑗=1}{∑}}{\overset{}{18}}𝑏_{𝑗}+\underset{\underset{𝑗=1}{∑}}{\overset{}{18}}1) \\ & =(40−2⋅15)⋅(−8+18) \\ & =(10)⋅(10) \\ & =100.\end{aligned}


$$
