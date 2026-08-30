# The Cyclic Property of the Imaginary Unit

Source: https://www.mathacademy.com/topics/32?courseId=134
Topic ID: 32

## Prerequisites

- [Imaginary Numbers](../../../traditional/lessons/algebra-ii/14-imaginary-numbers.md)
- [The Power Rule for Exponents](../../../../middle-school/lessons/grade-8/1224-the-power-rule-for-exponents.md)

## Lesson

### Introduction

Let's compute the first few powers of $\text{i},$ where $\text{i} = \sqrt{-1}\mathbin{:}$

$$


\begin{aligned}i^{0} & =1 \\ i^{1} & =i \\ i^{2} & =−1 \\ i^{3} & =i^{2}⋅i=(−1)⋅i=−i \\ i^{4} & =i^{2}⋅i^{2}=(−1)⋅(−1)=1\end{aligned}


$$

We can use these results to evaluate expressions containing powers of $\text{i}.$ Let's take a look at some examples.

### Example: Raising i to a Small Positive Integer Power

#### Question

What is the value of $4\text{i}^3?$

#### Explanation

Let's recall the first few powers of $\text{i},$ where $\text{i} = \sqrt{-1}\mathbin{:}$

$$


\begin{aligned}i^{0} & =1 \\ i^{1} & =i \\ i^{2} & =−1 \\ i^{3} & =i^{2}⋅i=(−1)⋅i=−i \\ i^{4} & =i^{2}⋅i^{2}=(−1)⋅(−1)=1\end{aligned}


$$

Therefore,

$$


\begin{aligned}4i^{3} & =4⋅(−i)=−4i.\end{aligned}


$$

### The Cyclic Nature of Powers of i

Let's remind ourselves of the first few powers of $\text{i}\mathbin{:}$

$$


\begin{aligned}i^{1} & =i \\ i^{2} & =−1 \\ i^{3} & =−i \\ i^{4} & =1\end{aligned}


$$

At the fourth power, we return to the value of $1,$ which can also be written as $\text{i}^0 = 1.$ This means that if we continue to increase the powers, we would cycle through the same four values once again, as shown below.

![Instructional graphic](../../../../lesson-assets/integrated-math-iii/topic-32/f8a63747bb175fce.png)

So, for $\text{i}^5$ through $\text{i}^8,$ the exact same pattern repeats. Remembering that $\text{i}^4 = 1,$ we have

$$


\begin{aligned} \text{i}^5&=\text{i}^4 \cdot \text{i} &= \text{i}\\[5pt] \text{i}^6&=\text{i}^4 \cdot \text{i}^2 &=-1\\[5pt] \text{i}^7&=\text{i}^4 \cdot \text{i}^3 &= -\text{i} \\[5pt] \text{i}^8&=\text{i}^4 \cdot \text{i}^4 &= 1 . \end{aligned}


$$

Similarly, for $\text{i}^9$ through to $\text{i}^{12},$ the pattern repeats again:

$$


\begin{aligned} \text{i}^9&=(\text{i}^4)^2 \cdot \text{i} &= \text{i}\\[5pt] \text{i}^{10}&=(\text{i}^4)^2 \cdot \text{i}^2 &=-1\\[5pt] \text{i}^{11}&=(\text{i}^4)^2 \cdot \text{i}^3 &= -\text{i} \\[5pt] \text{i}^{12}&=(\text{i}^4)^2 \cdot \text{i}^4 &= 1 \end{aligned}


$$

Therefore, to simplify a higher integer power of $\text{i},$ we *divide the power by $4$ and raise $\text{i}$ to the remainder*.

Let's see this idea in action.

### Example: Raising i to a Positive Integer Power Using the Cyclic Property

#### Question

Simplify $\text{i}^{15}.$

#### Explanation

To find the value of $\text{i}$ to some positive integer power $n$, we divide $n$ by $4$ and raise $\text{i}$ to the remainder.

In our case, we have $n=15.$ Dividing the power by $4,$ we get

$$


15\div 4 = 3\,\text{R} \color{blue}{3}.


$$

So the remainder is $\color{blue}3.$ Therefore,

$$


\text{i}^{15} = \text{i}^{\color{blue}{3}} = -\text{i}.


$$

### Example: Evaluating an Expression Involving Powers of i Using the Laws of Exponents

#### Question

If $a = \text{i}^9$ and $b = \text{i}^{7},$ then $ab =$

#### Explanation

Using the addition law for exponents, we have

$$


ab =\text{i}^9\cdot\text{i}^7 = \text{i}^{9+7} = \text{i}^{16}.


$$

To find the value of $\text{i}$ raised to some positive integer power $n,$ we divide $n$ by $4$ and raise $\text{i}$ to the remainder.

In our case, we have $n=16.$ Dividing the power by $4,$ we get

$$


16\div 4 = 4\,\text{R} \color{blue}{0}.


$$

So the remainder is $\color{blue}0.$ Therefore,

$$


\text{i}^{16} = \text{i}^{\color{blue}{0}} =1.


$$

### Example: Raising i to a Negative Power

#### Question

Find the value of $\text{i}^{-2}.$

#### Explanation

First, using the laws of exponents, we can write

$$


\text{i}^{-2}=\dfrac{1}{\text{i}^2}.


$$

We now recall that $\text{i}^2 = -1.$ Therefore,

$$


\dfrac{1}{\text{i}^2} = \dfrac{1}{(-1)} = -1.


$$
