# Modular Residues

Source: https://www.mathacademy.com/topics/2786?courseId=76
Topic ID: 2786

## Prerequisites

- [The Addition Property of Modular Arithmetic](./2673-the-addition-property-of-modular-arithmetic.md)

## Lesson

### Introduction

The **residue** of an integer $a$ modulo $n$ is the *unique* integer $0 \leq r < n$ such that

$$


a \equiv r \quad (\textrm{mod}\,n).


$$

This integer $r$ is sometimes called the **least residue** of $a$ modulo $n.$

For example, consider the following statements:

$$


\begin{aligned}25 & ≡1\, & (mod\,6) \\ 25 & ≡7\, & (mod\,6) \\ 25 & ≡13\, & (mod\,6) \\ 25 & ≡19\, & (mod\,6) \\ & \,\,\,⋮ & \end{aligned}


$$

All of these statements are true. However, we say that "the residue of $25$ modulo $6$ is ${\color{blue}{1}}$", because $0\leq {\color{blue}{1}} < 6.$ We write this as

$$


25 \textrm{ mod } 6 = 1.


$$

Notice that there are no parentheses around the $\textrm{mod}$. When there are no parentheses, it means that we're treating $\textrm{mod}$ as though it were a type of function. This function takes our integer $25$ as its input and returns the remainder that we get when $25$ is divided by $6.$

Similarly,

$$


\begin{aligned}7 mod 6 & =1 \\ 13 mod 6 & =1 \\ 19 mod 6 & =1 \\ & \,\,\,⋮\end{aligned}


$$

We'll present two methods of computing residues. Make sure that you understand *both* methods.

### Example: Modular Residues of Positive Integers

#### Question

What is $26 \textrm{mod} 3?$

#### Explanation

The residue of $26$ modulo $3$ is the integer $0 \leq r < 3$ such that

$$


26 \equiv r \quad (\textrm{mod}\,3).


$$

****

To find the residue $r,$ we need to write $26$ as an integer multiple of $3,$ plus the residue $r.$

We note that $26 \equiv 2 \, (\textrm{mod}\,3)$ because

$$


26 = 8\cdot 3 + {\color{blue}{2}} .


$$

Therefore, the residue of $26$ modulo $3$ is ${\color{blue}{2}}.$

****

We can use the subtraction property. Remember that any integer multiple of $3$ is congruent to $0$ modulo $3.$

$$


\begin{aligned}26 & ≡26−0 & & (mod\,3) \\ & ≡26−8⋅3 & & (mod\,3) \\ & ≡26−24 & & (mod\,3) \\ & ≡2 & & (mod\,3)\end{aligned}


$$

Therefore, the residue of $26$ modulo $3$ is ${\color{blue}{2}}.$

### Example: Modular Residues of Negative Integers

#### Question

What is $-13 \textrm{mod} 4?$

#### Explanation

The residue of $-13$ modulo $4$ is the integer $0 \leq r < 4$ such that

$$


-13 \equiv r \quad (\textrm{mod}\,4).


$$

****

To find the residue $r,$ we need to write $-13$ as an integer multiple of $4,$ plus the residue $r.$

We note that $-13 \equiv 3 \, (\textrm{mod}\,4)$ because

$$


-13 = (-4)\cdot 4 + {\color{blue}{3}} .


$$

Therefore, the residue of $-13$ modulo $4$ is ${\color{blue}{3}}.$

****

We can use the addition property. Remember that any integer multiple of $4$ is congruent to $0$ modulo $4.$

$$


\begin{aligned}−13 & ≡−13+0 & & (mod\,4) \\ & ≡−13+4⋅4 & & (mod\,4) \\ & ≡−13+16 & & (mod\,4) \\ & ≡3 & & (mod\,4)\end{aligned}


$$

Therefore, the residue of $-13$ modulo $4$ is ${\color{blue}{3}}.$

### Residues Modulo Powers of Ten

Some interesting problems in number theory require finding the last few digits of a large integer. We can use properties of congruences to help us solve these types of problems.

Consider a positive number $a,$ where the digit $d_1$ is in the ones place, $d_2$ is in the tens place, $d_3$ is in the hundreds place, and so on.

$$


a = \ldots d_3 d_2 d_1


$$

Then, $a$ can be written in expanded form as follows:

$$


\begin{aligned}𝑎 & =⋯+100𝑑_{3}+10𝑑_{2}+𝑑_{1} \\ & =10(⋯+10𝑑_{3}+𝑑_{2})+𝑑_{1}\end{aligned}


$$

Now, we compute the residue of $a$ modulo $10{:}$

$$


\begin{aligned}𝑎 & ≡10(⋯+10𝑑_{3}+𝑑_{2})+𝑑_{1} & & (mod\,10) \\ & ≡0⋅(⋯+10𝑑_{3}+𝑑_{2})+𝑑_{1} & & (mod\,10) \\ & ≡0+𝑑_{1} & & (mod\,10) \\ & ≡𝑑_{1} & & (mod\,10)\end{aligned}


$$

Therefore, the expression $a \: \textrm{mod}\: 10$ returns the last digit of $a$.

For example,

$$


25\,409\,19{\color{blue}3} \: \textrm{mod} \: 10 = {\color{blue}3}.


$$

Using similar reasoning,

- the expression $a \: \textrm{mod}\: 100$ returns the last two digits of $a,$ e.g.,

- the expression $a \: \textrm{mod}\: 1\,000$ returns the last three digits of $a,$ e.g.,

and so on.

### Example: Determining the Last Few Digits of a Number

#### Question

Let $a$ be a positive integer. Construct an expression that gives the last digit of $24a+15.$

#### Explanation

Let $b=24a+15.$ Note that $b$ is positive. Now, let $d_3,$ $d_2,$ and $d_1$ be the last three digits of the number $b{:}$

$$


b = \ldots d_3 d_2 d_1


$$

Then, $b$ can be written in expanded form as follows:

$$


\begin{aligned}𝑏 & =⋯+100𝑑_{3}+10𝑑_{2}+𝑑_{1} \\ & =10(⋯+10𝑑_{3}+𝑑_{2})+𝑑_{1}\end{aligned}


$$

Now, we compute the residue of $b$ modulo $10{:}$

$$


\begin{aligned}𝑏 & ≡10(⋯+10𝑑_{3}+𝑑_{2})+𝑑_{1} & & (mod\,10) \\ & ≡0⋅(⋯+10𝑑_{3}+𝑑_{2})+𝑑_{1} & & (mod\,10) \\ & ≡0+𝑑_{1} & & (mod\,10) \\ & ≡𝑑_{1} & & (mod\,10)\end{aligned}


$$

Notice that $d_1$ is the last digit of $b.$

Finally, since $b = 24a+15,$ and

$$


24\equiv 4, \qquad 15\equiv 5 \qquad (\textrm{mod}\,10)


$$

we have the following:

$$


\begin{aligned}𝑏 & ≡𝑑_{1} & & (mod\,10) \\ 24𝑎+15 & ≡𝑑_{1} & & (mod\,10) \\ 4𝑎+5 & ≡𝑑_{1} & & (mod\,10)\end{aligned}


$$

Therefore, the expression that gives the last digit of $24a+15$ is the following:

$$


(4a+5) \: \textrm{mod}\: 10


$$
