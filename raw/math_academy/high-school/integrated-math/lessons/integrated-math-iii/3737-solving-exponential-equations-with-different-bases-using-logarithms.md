# Solving Exponential Equations With Different Bases Using Logarithms

Source: https://www.mathacademy.com/topics/3737?courseId=134
Topic ID: 3737

## Prerequisites

- [The Product Rule for Logarithms](../../../traditional/lessons/algebra-ii/1473-the-product-rule-for-logarithms.md)
- [Solving Exponential Equations With Different Bases](../../../traditional/lessons/algebra-ii/1583-solving-exponential-equations-with-different-bases.md)

## Lesson

### Introduction

The most general way of solving exponential equations with different bases is to use logarithms on both sides of the equation. For example, given the equation

$$


3^{x+1} = 5^{x},


$$

we could apply $\log_3$ on both sides and get

$$


\log_3(3^{x+1}) = \log_3(5^{x}).


$$

Now, we use the fact that $\log_b \left(b^c \right) = c$ to simplify the left-hand side:

$$


\begin{aligned}𝑥+1 & =log_{3}⁡(5^{𝑥})\end{aligned}


$$

Next, we use the power law for logarithms to simplify the right-hand side:

$$


\begin{aligned}𝑥+1 & =𝑥log_{3}⁡(5)\end{aligned}


$$

Finally, we solve for $x,$ as follows:

$$


\begin{aligned}𝑥+1 & =𝑥log_{3}⁡(5) \\ 𝑥−𝑥log_{3}⁡(5) & =−1 \\ 𝑥(1−log_{3}⁡(5)) & =−1 \\ 𝑥 & =−\frac{1}{1−log_{3}⁡(5)} \\ 𝑥 & =\frac{1}{log_{3}⁡(5)−1}\end{aligned}


$$

**Note:** in the first step, we also could have applied $\log_5$ on both sides of our equation, instead of $\log_3.$ Then, the answer would be numerically the same but expressed using $\log_5$ instead of $\log_3.$

### Example: Finding Exact Solutions of Exponential Equations

#### Question

Expressed in terms of $\log_2,$ what value of $x$ satisfies the equation $2^{x+1}=3^x?$

#### Explanation

First, we take $\log_2$ on both sides of the equation:

$$


\begin{aligned}2^{𝑥+1} & =3^{𝑥} \\ log_{2}⁡(2^{𝑥+1}) & =log_{2}⁡(3^{𝑥})\end{aligned}


$$

Now, we use the fact that $\log_b \left(b^c \right) = c$ to simplify the left-hand side. This gives:

$$


x+1 = \log_2 \left(3^{x}\right)


$$

Next, we use the power law of logarithms to simplify the right-hand side:

$$


x+1 = x \log_2 \left(3\right)


$$

Finally, we solve for $x,$ as follows:

$$


\begin{aligned}𝑥+1 & =𝑥log_{2}⁡(3) \\ 𝑥log_{2}⁡(3)−𝑥 & =1 \\ 𝑥(log_{2}⁡(3)−1) & =1 \\ 𝑥 & =\frac{1}{log_{2}⁡(3)−1}\end{aligned}


$$

### Example: Finding Solutions of Exponential Equations Using the Natural Logarithm

#### Question

Expressed in terms of natural logarithms, what value of $x$ satisfies the equation $e^{x+1}=2^x\cdot 5?$

#### Explanation

First, we take the natural logarithm $\left(\ln\right)$ of both sides of the equation:

$$


\begin{aligned}𝑒^{𝑥+1} & =2^{𝑥}⋅5 \\ ln⁡(𝑒^{𝑥+1}) & =ln⁡(2^{𝑥}⋅5)\end{aligned}


$$

Now, we use the fact that $\ln \left(e^a \right) = a$ to simplify the left-hand side. This gives:

$$


x+1 =\ln \left(2^{x}\cdot 5\right)


$$

Next, we use the power and product laws of logarithms to simplify the right-hand side:

$$


\begin{aligned}𝑥+1 & =ln⁡(2^{𝑥})+ln⁡(5) \\ 𝑥+1 & =𝑥ln⁡(2)+ln⁡(5)\end{aligned}


$$

Finally, we solve for $x,$ as follows:

$$


\begin{aligned}𝑥+1 & =𝑥ln⁡(2)+ln⁡(5) \\ 𝑥−𝑥ln⁡(2) & =ln⁡(5)−1 \\ 𝑥(1−ln⁡(2)) & =ln⁡(5)−1 \\ 𝑥 & =\frac{ln⁡(5)−1}{1−ln⁡(2)}\end{aligned}


$$

### Example: Finding Solutions of Exponential Equations Using the Natural Logarithm: Advanced Cases

#### Question

Expressed in terms of natural logarithms, determine the value of $x$ that satisfies the equation $5^{x+2}=9^{x-2}.$

#### Explanation

First, we take the natural logarithm $\left(\ln\right)$ of both sides of the equation:

$$


\begin{aligned}5^{𝑥+2} & =9^{𝑥−2} \\ ln⁡(5^{𝑥+2}) & =ln⁡(9^{𝑥−2})\end{aligned}


$$

Now, we use the power law of logarithms to simplify both sides of the equation. This gives

$$


(x+2)\ln(5) = (x-2)\ln(9).


$$

Finally, we solve for $x$, as follows:

$$


\begin{aligned}(𝑥+2)ln⁡(5) & =(𝑥−2)ln⁡(9) \\ 𝑥ln⁡(5)+2ln⁡(5) & =𝑥ln⁡(9)−2ln⁡(9) \\ 𝑥ln⁡(5)−𝑥ln⁡(9) & =−2ln⁡(9)−2ln⁡(5) \\ 𝑥ln⁡(9)−𝑥ln⁡(5) & =2ln⁡(9)+2ln⁡(5) \\ 𝑥(ln⁡(9)−ln⁡(5)) & =2(ln⁡(5)+ln⁡(9)) \\ 𝑥 & =\frac{2(ln⁡(5)+ln⁡(9))}{ln⁡(9)−ln⁡(5)}\end{aligned}


$$
