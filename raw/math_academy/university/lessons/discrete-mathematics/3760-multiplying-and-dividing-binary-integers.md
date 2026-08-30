# Multiplying and Dividing Binary Integers

Source: https://www.mathacademy.com/topics/3760?courseId=109
Topic ID: 3760

## Prerequisites

- [Four-Digit by Two-Digit Division](../../../elementary-school/lessons/grade-5/2331-four-digit-by-two-digit-division.md)
- [Adding and Subtracting Binary Integers](./3362-adding-and-subtracting-binary-integers.md)

## Lesson

### Introduction

Let's consider a few powers of $2$ and their corresponding binary notations:

$$



\begin{aligned}2^{0} & =(1)_{2} \\ 2^{1} & =(10)_{2} \\ 2^{2} & =(100)_{2} \\ 2^{3} & =(1000)_{2} \\ & \,\,\,⋮ \\ 2^{𝑛} & =(1\underset{n times}{\underset{}{00…0}})_{2}\end{aligned}



$$

Notice that in base $2,$ the powers of $2$ look similar to powers of $10$ in base $10.$ It turns out that they also play a similar role in multiplication and division.

- To multiply a binary integer by a power of $2,$ we append the corresponding number of zeros to the right of the number. For example,

- To divide a binary integer by a power of $2,$ we erase the corresponding number of zeros on the right of the number. For example,

$$



 (111{\color{blue}00})_2 \div (1{\color{blue}00})_2 = (111)_2 .



$$

### Example: Multiplying and Dividing Binary Integers by Powers of Two

#### Question

$(10\,001\,010)_2 \div (10)_2 =$

#### Explanation

To divide a binary integer by a power of $2,$ we erase the corresponding number of zeros:

$$



(10\,001\,01{\color{blue}0})_2 \div (1{\color{blue}0})_2 = (1\,000\,101)_2



$$

### Multiplying Binary Integers

Binary integer multiplication is much like decimal multiplication, except that we operate in base $2.$

For example, let's compute the following product:

$$



(1\,100)_2 \cdot (101)_2



$$

First, we note the following basic addition and multiplication rules in base $2{:}$

$$



\begin{aligned} & 0+0=0 & & \,0⋅0=0 \\ & 0+1=1 & & \,0⋅1=0 \\ & 1+0=1 & & \,1⋅0=0 \\ & 1+1=10 & & \,1⋅1=1\end{aligned}



$$

To compute our product, we start by lining up the numbers:

$$



\begin{aligned} & \begin{matrix} & & & & 1 & 1 & 0 & 0 \\ & × & & & & 1 & 0 & 1 \\ & & & & & & & \end{matrix}\end{aligned}



$$

Next, we proceed by multiplying with the standard algorithm, as usual.

First, we multiply $1\,100$ by the rightmost digit of $101{:}$

$$



\begin{aligned} & \begin{matrix} & & & & 1 & 1 & 0 & 0 \\ & × & & & & 1 & 0 & 1 \\ & & & & 1 & 1 & 0 & 0\end{matrix}\end{aligned}



$$

Then, we multiply $1\,100$ by the second digit of $101.$ We add a zero in the rightmost position and then do the rest of the multiplication.

$$



\begin{aligned} & \begin{matrix} & & & & 1 & 1 & 0 & 0 \\ & × & & & & 1 & 0 & 1 \\ & & & & 1 & 1 & 0 & 0 \\ & & & 0 & 0 & 0 & 0 & 0\end{matrix}\end{aligned}



$$

Next, we multiply $1\,100$ by the third digit of $101.$ We add two zeros to the rightmost positions and then carry out the rest of the multiplication:

$$



\begin{aligned} & \begin{matrix} & & & & 1 & 1 & 0 & 0 \\ & × & & & & 1 & 0 & 1 \\ & & & & 1 & 1 & 0 & 0 \\ & & & 0 & 0 & 0 & 0 & 0 \\ & & 1 & 1 & 0 & 0 & 0 & 0\end{matrix}\end{aligned}



$$

Finally, we sum the three numbers as follows:

$$



\begin{aligned} & \begin{matrix} & & & & 1 & 1 & 0 & 0 \\ & × & & & & 1 & 0 & 1 \\ & & & & 1 & 1 & 0 & 0 \\ & & & 0 & 0 & 0 & 0 & 0 \\ & + & 1 & 1 & 0 & 0 & 0 & 0 \\ & & 1 & 1 & 1 & 1 & 0 & 0\end{matrix}\end{aligned}



$$

Therefore, $(1\,100)_2 \cdot (101)_2 = (111\,100)_2.$

### Example: Multiplying Binary Integers

#### Question

Compute

#### Explanation

First, recall the basic addition and multiplication rules in base

Now, we line up the numbers:

Next, we proceed by multiplying with the standard algorithm, as usual. The only difference is that we are operating in base

Therefore,

### Dividing Binary Integers

Let's now learn how to divide integers in base $2.$

Consider the following division problem:

$$



(1111)_2 \div (11)_2



$$

First, we recall the basic addition and multiplication rules in base $2{:}$

$$



\begin{aligned} & 0+0=0 & & \,0⋅0=0 \\ & 0+1=1 & & \,0⋅1=0 \\ & 1+0=1 & & \,1⋅0=0 \\ & 1+1=10 & & \,1⋅1=1\end{aligned}



$$

We proceed using the standard algorithm for long division:

- Notice that $(11)_2$ goes ${\color{blue}1}$ time into $(11)_2.$ So, we write ${\color{blue}1}$ in the quotient and $(11)_2-(11)_2=({\color{red}0})_2{:}$

- Bring down ${\color{purple}1}.$ Notice that $(11)_2$ goes ${\color{blue}0}$ times into $(1)_2.$ So, we write ${\color{blue}0}$ in the quotient:

- Bring down ${\color{purple}1}.$ Notice that $(11)_2$ goes ${\color{blue}1}$ times into $(11)_2.$ So, we write ${\color{blue}1}$ in the quotient and $(11)_2 - (11)_2 = ({\color{red}0})_2{:}$

Therefore, $(1\,111)_2 \div (11)_2 = (101)_2.$

### Example: Dividing Binary Integers

#### Question

Compute $(110\,010) \div (1\,010).$

#### Explanation

First, recall the basic addition and multiplication rules in base $2{:}$

$$



\begin{aligned} & 0+0=0 & & \,0⋅0=0 \\ & 0+1=1 & & \,0⋅1=0 \\ & 1+0=1 & & \,1⋅0=0 \\ & 1+1=10 & & \,1⋅1=1\end{aligned}



$$

We write our task in an equivalent form by dropping an equal amount of zeros from the right of the dividend and divisor:

$$



(110\,01{\color{blue}0})_2 \div (1\,01{\color{blue}0})_2 = (11\,001)_2 \div (101)_2



$$

We proceed by long division with the standard algorithm, as usual. The only difference is that we are operating in base $2{:}$

- Notice that $(101)_2$ goes $1$ time into $(110)_2.$ So, we write $1$ in the quotient and $(110)_2-(101)_2=(1)_2{:}$

- Bring down $0.$ Notice that $(101)_2$ goes $0$ times into $(10)_2.$ So, we write $0$ in the quotient:

- Bring down $1.$ Notice that $(101)_2$ goes $1$ time into $(101)_2.$ So, we write $1$ in the quotient and $(101)_2 - (101)_2 = (0)_2{:}$

Therefore, $(110\,010)_2 \div (1\,010)_2 = (101)_2.$
