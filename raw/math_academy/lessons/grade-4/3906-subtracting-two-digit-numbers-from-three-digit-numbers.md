# Subtracting Two-Digit Numbers From Three-Digit Numbers

Source: https://www.mathacademy.com/topics/3906?courseId=75
Topic ID: 3906

## Prerequisites

- [Subtracting Two-Digit Numbers](./3876-subtracting-two-digit-numbers.md)

## Lesson

### Introduction

Let's take a look at the following subtraction problem:

$$
253 - 27
$$

In this case, we're subtracting a two-digit number from a three-digit number. To do this, we use the standard algorithm.

The first step is to write the numbers in the usual way, where ones are aligned over ones, tens over tens, and hundreds over hundreds:

$$
\begin{aligned} & \,\,\,\,2\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,3\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,7\,\,\,\, \\ & \,\,\,\,\,\,\, & \,\,\,\,\,\, & \,\,\,\,\,\,\,\end{aligned}
$$

Next, we proceed by subtracting the numbers in each place value (from right to left):

**Step 1.** We cannot compute $3 - 7.$ So, we have to "borrow" $1$ from the *tens* place. This leaves us with $5-1=\color{red}4$ tens and $\color{red}13$ ones:

$$
\begin{aligned} & \,\,\,\,\,\,\, & \,\,\,4\,\,\, & \,\,\,\,13\,\,\,\, \\ & \,\,\,\,2\,\,\, & \,\,\,\,\,5\,\,\, & \,\,\,\,3\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\, & \,\,\,2\,\,\, & \,\,\,7\,\,\,\, \\ & \,\,\,\,\,\,\, & \,\,\,\,\,\, & \,\,\,\,\,\,\,\end{aligned}
$$

**Step 2.** Then, we subtract ones from ones and tens from tens:

$$
\begin{aligned} & \,\,\,\,\,\,\, & \,\,\,4\,\,\, & \,\,\,\,13\,\,\,\, \\ & \,\,\,\,2\,\,\, & \,\,\,\,\,5\,\,\, & \,\,\,\,3\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\, & \,\,\,2\,\,\, & \,\,\,7\,\,\,\, \\ & \,\,\,\,\,\,\, & \,\,\,2\,\,\, & \,\,\,6\,\,\,\,\end{aligned}
$$

**Step 3.** Notice that $27$ has no hundreds digit. Therefore, we place a $\color{red}0$ in its hundreds place:

$$
\begin{aligned} & \,\,\,\,\,\,\, & \,\,\,4\,\,\, & \,\,\,\,13\,\,\,\, \\ & \,\,\,\,2\,\,\, & \,\,\,\,\,5\,\,\, & \,\,\,\,3\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,0\,\,\, & \,\,\,2\,\,\, & \,\,\,7\,\,\,\, \\ & \,\,\,\,\,\,\, & \,\,\,2\,\,\, & \,\,\,6\,\,\,\,\end{aligned}
$$

Then, subtracting the hundreds, we get the following:

$$
\begin{aligned} & \,\,\,\,\,\,\, & \,\,\,4\,\,\, & \,\,\,\,13\,\,\,\, \\ & \,\,\,\,2\,\,\, & \,\,\,\,\,5\,\,\, & \,\,\,\,3\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,0\,\,\, & \,\,\,2\,\,\, & \,\,\,7\,\,\,\, \\ & \,\,\,\,2\,\,\, & \,\,\,2\,\,\, & \,\,\,6\,\,\,\,\end{aligned}
$$

Therefore, we conclude that

$$
253 - 27 = 226.
$$

### Example: Subtracting Two-Digit Numbers From Three-Digit Numbers

#### Question

What is $498 - 75?$

#### Explanation

First, we line up our numbers (** over **, ** over **, and ** over **):

$$
\begin{aligned} & \,\,\,\,4\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,8\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,5\,\,\,\, \\ & & \,\,\,\,\,\,\,\, & \,\,\,\,\,\,\,\,\end{aligned}
$$

Next, we proceed by subtracting the numbers in each place value (from right to left):

**** Subtracting the ones, ${\color{blue}8} - {\color{blue}5} = {\color{blue}3}{:}$

$$
\begin{aligned} & \,\,\,\,4\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,8\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,5\,\,\,\, \\ & & \,\,\,\,\,\,\,\, & \,\,\,\,3\,\,\,\,\end{aligned}
$$

**** Subtracting the tens, ${\color{blue}9} - {\color{blue}7} = {\color{blue}2}{:}$

$$
\begin{aligned} & \,\,\,\,4\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,8\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,5\,\,\,\, \\ & & \,\,\,\,2\,\,\,\, & \,\,\,\,3\,\,\,\,\end{aligned}
$$

**** Subtracting the hundreds, ${\color{blue}4} - {\color{blue}0} = {\color{blue}4}{:}$

$$
\begin{aligned} & \,\,\,\,4\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,8\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,5\,\,\,\, \\ & \,\,\,\,4\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,3\,\,\,\,\end{aligned}
$$

Therefore, $498 - 75 = 423.$

### Example: Subtracting Two-Digit Numbers From Three-Digit Numbers: Borrowing Once

#### Question

What is $335 - 61?$

#### Explanation

First, we line up our numbers:

$$
\begin{aligned} & \,\,\,\,3\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,5\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,1\,\,\,\, \\ & \,\,\,\,\,\,\,\, & \,\,\,\,\,\,\, & \,\,\,\,\,\,\,\,\end{aligned}
$$

Next, we proceed by subtracting the numbers in each place value (from right to left):

**** Subtracting the ones, ${\color{blue}5} - {\color{blue}1} = {\color{blue}4}{:}$

$$
\begin{aligned} & \,\,\,\,3\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,5\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,1\,\,\,\, \\ & \,\,\,\,\,\,\,\, & \,\,\,\,\,\,\, & \,\,\,\,4\,\,\,\,\end{aligned}
$$

**** We cannot compute $3 - 6.$ So, we borrow $1$ from the ** place:

$$
\begin{aligned} & \,\,\,2\,\,\, & \,\,\,13\,\,\, & \,\,\,\,\,\,\, \\ & \,\,\,\,\,3\,\,\, & \,\,\,\,3\,\,\, & \,\,\,5\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\, & \,\,\,6\,\,\, & \,\,\,1\,\,\,\, \\ & \,\,\,\,\,\,\, & \,\,\,\,\,\, & \,\,\,4\,\,\,\,\end{aligned}
$$

**** Then, we subtract tens and hundreds:

$$
\begin{aligned} & \,\,\,2\,\,\, & \,\,\,13\,\,\, & \,\,\,\,\,\,\, \\ & \,\,\,\,\,3\,\,\, & \,\,\,\,3\,\,\, & \,\,\,5\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,0\,\,\, & \,\,\,6\,\,\, & \,\,\,1\,\,\,\, \\ & \,\,\,\,2\,\,\, & \,\,\,7\,\,\, & \,\,\,4\,\,\,\,\end{aligned}
$$

Therefore, $335 - 61 = 274.$

### Example: Subtracting Two-Digit Numbers From Three-Digit Numbers: Borrowing Twice

#### Question

What is $312 - 88?$

#### Explanation

First, we line up our numbers:

$$
\begin{aligned} & \,\,\,\,3\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,2\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,8\,\,\,\, \\ & \,\,\,\,\,\,\, & \,\,\,\,\,\, & \,\,\,\,\,\,\,\end{aligned}
$$

Next, we proceed by subtracting the numbers in each place value (from right to left):

**** We cannot compute $2 - 8.$ So, we borrow $1$ from the ** place. Then, subtracting the ones, ${\color{blue}12} - {\color{blue}8} = {\color{blue}4}{:}$

$$
\begin{aligned} & \,\,\,\,\,\,\, & \,\,\,\,0\,\,\, & \,\,\,\,12\,\,\,\, \\ & \,\,\,\,3\,\,\, & \,\,\,\,\,1\,\,\, & \,\,\,\,\,2\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\, & \,\,\,8\,\,\, & \,\,\,8\,\,\,\, \\ & \,\,\,\,\,\,\, & \,\,\,\,\,\, & \,\,\,4\,\,\,\,\end{aligned}
$$

**** We cannot compute $0 - 8.$ So, we borrow $1$ from the ** place. Then, we subtract tens and hundreds:

$$
\begin{aligned} & \,\,\,\,2\,\,\, & \,\,\,\,10\,\,\, & \,\,\,\,12\,\,\,\, \\ & \,\,\,\,\,\,3\,\,\,\, & \,\,\,\,\,1\,\,\, & \,\,\,\,2\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,0\,\,\, & \,\,\,8\,\,\, & \,\,\,8\,\,\,\, \\ & \,\,\,\,2\,\,\, & \,\,\,2\,\,\, & \,\,\,4\,\,\,\,\end{aligned}
$$

Therefore, $312 - 88 = 224.$

### Example: Borrowing From Zero

#### Question

What is $208 - 49?$

#### Explanation

First, we line up our numbers:

$$
\begin{aligned} & \,\,\,\,2\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,8\,\,\,\, & \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,9\,\,\,\, & \\ & & & & \end{aligned}
$$

Next, we proceed by subtracting the numbers in each place value (from right to left):

**** We cannot compute $8 - 9,$ and there are $0$ tens to borrow from. So, we borrow $1$ from the ** place first:

$$
\begin{aligned} & \,\,\,1\,\,\, & \,\,\,10\,\,\, & \,\,\,\,\,\,\, \\ & \,\,\,\,\,2\,\,\, & \,\,\,\,0\,\,\, & \,\,\,8\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\, & \,\,\,4\,\,\, & \,\,\,9\,\,\,\, \\ & \,\,\,\,\,\,\, & \,\,\,\,\,\, & \,\,\,\,\,\,\,\end{aligned}
$$

Then, we borrow $1$ from the ** place:

$$
\begin{aligned} & \,\,\,\,\,\,\, & \,\,\,9\,\,\, & \,\,\,18\,\,\,\, \\ & \,\,\,1\,\,\, & \,\,\,10\,\,\, & \,\,\,8\,\,\,\, \\ & \,\,\,\,\,2\,\,\, & \,\,\,\,0\,\,\, & \,\,\,8\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,\,\,\, & \,\,\,4\,\,\, & \,\,9\,\,\,\, \\ & \,\,\,\,\,\,\, & \,\,\,\,\,\, & \,\,\,\,\,\,\,\end{aligned}
$$

**** Then we subtract ones, tens, and hundreds:

$$
\begin{aligned} & \,\,\,\,\,\,\, & \,\,\,9\,\,\, & \,\,\,18\,\,\,\, \\ & \,\,\,1\,\,\, & \,\,\,10\,\,\, & \,\,\,8\,\,\,\, \\ & \,\,\,\,\,2\,\,\, & \,\,\,\,0\,\,\, & \,\,\,8\,\,\,\, \\ \,\,\,\,−\,\,\,\, & \,\,\,\,0\,\,\, & \,\,\,4\,\,\, & \,\,9\,\,\,\, \\ & \,\,\,\,1\,\,\, & \,\,\,5\,\,\, & \,\,9\,\,\,\,\end{aligned}
$$

Therefore, $208 - 49 = 159.$
