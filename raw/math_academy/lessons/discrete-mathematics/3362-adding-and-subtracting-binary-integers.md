# Adding and Subtracting Binary Integers

Source: https://www.mathacademy.com/topics/3362?courseId=109
Topic ID: 3362

## Prerequisites

- [Binary Integers](./3363-binary-integers.md)
- [Subtracting Numbers Up to Seven Digits](../grade-4/3909-subtracting-numbers-up-to-seven-digits.md)

## Lesson

### Introduction

Binary integers addition is much like whole number addition, except we operate in base $2.$

To demonstrate, let's add $(1\,010)_2 + (1\,101)_2.$

First, we note the following basic addition rules in base $2{:}$

$$



\begin{aligned}0+0 & =0 \\ 0+1 & =1 \\ 1+0 & =1 \\ 1+1 & =10\end{aligned}



$$

The last rule states that one plus one equals two, and $10$ is simply the binary representation of two.

Now, we line up the numbers:

$$



\begin{aligned} & & & 1 & 0 & 1 & 0 \\ & \,\,\,\,+\,\,\,\, & & 1 & 1 & 0 & 1 \\ & & & & & & \end{aligned}



$$

Next, we proceed by adding the numbers from right to left.

Adding the first three columns, we obtain the following:

$$



\begin{aligned} & & & & & & \\ & & & 1 & 0 & 1 & 0 \\ & + & & 1 & 1 & 0 & 1 \\ & & & & 1 & 1 & 1\end{aligned}



$$

Finally, we need to add $\boxed{1}$ and $\boxed{1}$ in the $4$th position:

$$



\begin{aligned} & & & & & & \\ & & & 1 & 0 & 1 & 0 \\ & + & & 1 & 1 & 0 & 1 \\ & & & & 1 & 1 & 1\end{aligned}



$$

We know that $(1)_2+(1)_2=({\color{blue}1}0)_2.$ So, we write down $0$ in the $4$th position and carry ${\color{blue}1}$ to the next ($5$th) position:

$$



\begin{aligned} & & \begin{aligned} \\ 1\end{aligned} & & & & \\ & & & 1 & 0 & 1 & 0 \\ & + & & 1 & 1 & 0 & 1 \\ & & 1 & 0 & 1 & 1 & 1\end{aligned}



$$

Therefore, $(1\,010)_2 + (1\,101)_2 =(10\,111)_2.$

**Note**: The equivalent sum in base $10$ is $10+13 = 23.$

### Example: Adding Binary Integers

#### Question

Compute $(1\,110)_2 + (100\,010)_2.$

#### Explanation

First, recall the basic addition rules in base $2{:}$

$$



\begin{aligned}0+0 & =0 \\ 0+1 & =1 \\ 1+0 & =1 \\ 1+1 & =10\end{aligned}



$$

Now, we line up the numbers:

$$



\begin{aligned} & & & & & 1 & 1 & 1 & 0 \\ & + & & 1 & 0 & 0 & 0 & 1 & 0 \\ & & & & & & & & \end{aligned}



$$

Next, we proceed by adding as usual. The only difference is that we are operating in base $2{:}$

$$



\begin{aligned} & & & & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 1\end{aligned} & & \\ & & & & & 1 & 1 & 1 & 0 \\ & + & & 1 & 0 & 0 & 0 & 1 & 0 \\ & & & 1 & 1 & 0 & 0 & 0 & 0\end{aligned}



$$

Therefore, $(1\,110)_2 + (100\,010)_2 =(110\,000)_2.$

### Subtracting Binary Integers

Binary integer subtraction is also similar to decimal subtraction.

First, recall the basic addition rules in base $2{:}$

$$



\begin{aligned}0+0 & =0 \\ 0+1 & =1 \\ 1+0 & =1 \\ 1+1 & =10\end{aligned}



$$

Let's use this to calculate $(10\,100)_2 - (1\,101)_2.$

First, we line up the numbers:

$$



\begin{aligned} & 1 & 0 & 1 & 0 & 0 \\ \,\,\,\,−\,\,\,\, & & 1 & 1 & 0 & 1 \\ & & & & & \end{aligned}



$$

Next, we proceed by subtracting as usual, from right to left.

In the $1$st column (from left), we need to subtract $\boxed{1}$ from $\boxed{0}{:}$

$$



\begin{aligned} & & & & & \\ & 1 & 0 & 1 & 0 & 0 \\ − & & 1 & 1 & 0 & 1 \\ & & & & & \end{aligned}



$$

To do that, we need to borrow from the $3$rd column because this is the next nonzero digit in the first number. So, we have the following:

- Borrow ${\color{blue}1}$ from the $3$rd column, where we have $1-{\color{blue}1}={\color{blue}0},$ and get ${\color{blue}10}$ in the $2$nd column:

$$



\begin{aligned} & & & \begin{aligned} \\ 0\end{aligned} & \begin{aligned} \\ 10\end{aligned} & \\ & 1 & 0 & 1 & 0 & 0 \\ − & & 1 & 1 & 0 & 1 \\ & & & & & \end{aligned}



$$

- Borrow $1$ from the $2$nd column, where we have $10-1={\color{blue}1},$ and get ${\color{blue}10}$ in the $1$st column:

$$



\begin{aligned} & & & \begin{aligned} \\ 0\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 10\end{aligned} \\ & 1 & 0 & 1 & 0 & 0 \\ − & & 1 & 1 & 0 & 1 \\ & & & & & \end{aligned}



$$

So, we can now subtract in the $1$st and $2$nd columns:

$$



\begin{aligned} & & & \begin{aligned} \\ 0\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 10\end{aligned} \\ & 1 & 0 & 1 & 0 & 0 \\ − & & 1 & 1 & 0 & 1 \\ & & & & 1 & 1\end{aligned}



$$

Now, we need to subtract $\boxed{1}$ from $\boxed{0}$ in the $3$rd column:

$$



\begin{aligned} & & & \begin{aligned} \\ 0\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 10\end{aligned} \\ & 1 & 0 & 1 & 0 & 0 \\ − & & 1 & 1 & 0 & 1 \\ & & & & 1 & 1\end{aligned}



$$

To do that, we need to borrow from the $5$rd column because this is the next nonzero digit in the first number. So, we have the following:

- Borrow ${\color{blue}1}$ from the $5$th column, where we have $1-{\color{blue}1}={\color{blue}0},$ and get ${\color{blue}10}$ in the $4$th column:

$$



\begin{aligned} & \begin{aligned} \\ 0\end{aligned} & \begin{aligned} \\ 10\end{aligned} & \begin{aligned} \\ 0\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 10\end{aligned} \\ & 1 & 0 & 1 & 0 & 0 \\ − & & 1 & 1 & 0 & 1 \\ & & & & 1 & 1\end{aligned}



$$

- Borrow ${\color{blue}1}$ from the $4$th column, where we have $10-{\color{blue}1}={\color{blue}1},$ and get ${\color{blue}10}$ in the $3$rd column:

$$



\begin{aligned} & \begin{aligned} \\ 0\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 10\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 10\end{aligned} \\ & 1 & 0 & 1 & 0 & 0 \\ − & & 1 & 1 & 0 & 1 \\ & & & & 1 & 1\end{aligned}



$$

Finally, we can subtract in the $3$rd, $4$th, and $5$th columns:

$$



\begin{aligned} & \begin{aligned} \\ 0\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 10\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 10\end{aligned} \\ & 1 & 0 & 1 & 0 & 0 \\ − & & 1 & 1 & 0 & 1 \\ & 0 & 0 & 1 & 1 & 1\end{aligned}



$$

Therefore, $(10\,100)_2 - (1\,101)_2 =(111)_2.$

### Example: Subtracting Binary Integers

#### Question

Compute $(100\,011)_2 - (1\,100)_2.$

#### Explanation

First, recall the basic addition rules in base $2{:}$

$$



\begin{aligned}0+0 & =0 \\ 0+1 & =1 \\ 1+0 & =1 \\ 1+1 & =10\end{aligned}



$$

Now, we line up the numbers:

$$



\begin{aligned} & & 1 & 0 & 0 & 0 & 1 & 1 \\ & − & & & 1 & 1 & 0 & 0 \\ & & & & & & & \end{aligned}



$$

Next, we proceed by subtracting as usual. The only difference is that we are operating in base $2{:}$

$$



\begin{aligned} & & \begin{aligned} \\ 0\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 1\end{aligned} & \begin{aligned} \\ 10\end{aligned} & \begin{aligned}\end{aligned} & \begin{aligned}\end{aligned} \\ & & 1 & 0 & 0 & 0 & 1 & 1 \\ & − & & & 1 & 1 & 0 & 0 \\ & & & 1 & 0 & 1 & 1 & 1\end{aligned}



$$

Therefore, $(100\,011)_2 - (1\,100)_2 =(10\,111)_2.$
