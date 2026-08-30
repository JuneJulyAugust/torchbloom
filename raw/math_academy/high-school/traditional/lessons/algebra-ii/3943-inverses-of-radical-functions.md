# Inverses of Radical Functions

Source: https://www.mathacademy.com/topics/3943?courseId=51
Topic ID: 3943

## Prerequisites

- [Solving Radical Equations](../algebra-i/116-solving-radical-equations.md)
- [Solving Rational Equations Using the Flip Method](../algebra-i/266-solving-rational-equations-using-the-flip-method.md)
- [Calculating the Inverse of a Function](./627-calculating-the-inverse-of-a-function.md)
- [The Power of Quotient Rule With Algebraic Expressions](../algebra-i/1428-the-power-of-quotient-rule-with-algebraic-expressions.md)
- [The Domain of a Transformed Radical Function](./1600-the-domain-of-a-transformed-radical-function.md)
- [Domain and Range of Inverse Functions](./3734-domain-and-range-of-inverse-functions.md)
- [The Range of a Transformed Radical Function](./3741-the-range-of-a-transformed-radical-function.md)

## Lesson

### Introduction

In this lesson, we'll use our knowledge of solving radical equations to compute inverses of radical functions.

For example, let's consider the following radical function:

$$



f(x) = 3\sqrt{x} + 2



$$

To compute the inverse of $f(x),$ we follow the usual four steps:

**Step 1:** First, we replace $f(x)$ with $y\mathbin{:}$

$$



y = 3\sqrt{x} + 2



$$

**Step 2:** Then, we swap $x$ and $y\mathbin{:}$

$$



x = 3\sqrt{y} + 2



$$

**Step 3:** Next, we solve for $y\mathbin{:}$

$$



\begin{aligned}𝑥 & =3\sqrt{𝑦}+2 \\ 3\sqrt{𝑦} & =𝑥−2 \\ \sqrt{𝑦} & =\frac{1}{3}(𝑥−2) \\ (\sqrt{𝑦})^{2} & =(\frac{1}{3}(𝑥−2))^{2} \\ 𝑦 & =\frac{1}{9}(𝑥−2)^{2}\end{aligned}



$$

**Step 4:** Finally, we replace $y$ with $f^{-1}(x)\mathbin{:}$

$$



f^{-1}(x) = \dfrac{1}{9}(x - 2)^2



$$

**Note**: The domain and range of $f(x)$ are

$$



x \geq 0, \qquad f(x) \geq 2.



$$

Therefore, the domain and range of $f^{-1}(x)$ are

$$



x \geq 2, \qquad f^{-1}(x) \geq 0.



$$

### Example: Finding the Inverse of a Radical Function

#### Question

Find the inverse of the function $f(x) = 1 - \dfrac{1}{3}\sqrt{x}.$

#### Explanation

To find $f^{-1}(x),$ we start by replacing $f(x)$ with $y{:}$

$$



y = 1 - \dfrac{1}{3}\sqrt{x}



$$

Now, interchanging $x$ and $y$ gives

$$



x = 1 - \dfrac{1}{3}\sqrt{y}.



$$

Then, we make $y$ the subject of the equation as follows:

$$



\begin{aligned}𝑥 & =1−\frac{1}{3}\sqrt{𝑦} \\ \frac{1}{3}\sqrt{𝑦} & =1−𝑥 \\ \sqrt{𝑦} & =3(1−𝑥) \\ (\sqrt{𝑦})^{2} & =(3(1−𝑥))^{2} \\ 𝑦 & =9(1−𝑥)^{2} \\ 𝑦 & =9(𝑥−1)^{2}\end{aligned}



$$

Therefore, the inverse function is

$$



f^{-1}(x) = 9(x - 1)^2.



$$

****: The domain and range of $f(x)$ are

$$



x \geq 0, \qquad f(x) \leq 1.



$$

Therefore, the domain and range of $f^{-1}(x)$ are

$$



x \leq 1, \qquad f^{-1}(x) \geq 0.



$$

### Example: Finding the Inverse of a Reciprocal Radical Function

#### Question

Find the inverse of the function

#### Explanation

To find we start by replacing with

Now, interchanging and gives

Then, we make the subject of the equation, as follows:

Therefore, the inverse function is

****: The domain and range of are

Therefore, the domain and range of are

### Example: Finding the Inverse of a Radical Function Containing a Linear Argument

#### Question

Find the inverse of the function $f(x) = \dfrac{1}{5}\sqrt{4x + 1}.$

#### Explanation

To find $f^{-1}(x),$ we start by replacing $f(x)$ with $y{:}$

$$



y = \dfrac{1}{5}\sqrt{4x + 1}



$$

Now, interchanging $x$ and $y$ gives

$$



x = \dfrac{1}{5}\sqrt{4y + 1}.



$$

Then, we make $y$ the subject of the equation as follows:

$$



\begin{aligned}𝑥 & =\frac{1}{5}\sqrt{4𝑦+1} \\ \sqrt{4𝑦+1} & =5𝑥 \\ (\sqrt{4𝑦+1})^{2} & =(5𝑥)^{2} \\ 4𝑦+1 & =25𝑥^{2} \\ 4𝑦 & =25𝑥^{2}−1 \\ 𝑦 & =\frac{1}{4}(25𝑥^{2}−1)\end{aligned}



$$

Therefore, the inverse function is

$$



f^{-1}(x) = \dfrac{1}{4}\left(25x^2 - 1\right).



$$

****: The domain and range of $f(x)$ are given by

$$



x \geq -\dfrac14, \qquad f(x) \geq 0.



$$

Therefore, the domain and range of $f^{-1}(x)$ are

$$



x \geq 0, \qquad f^{-1}(x) \geq -\dfrac14.



$$

### Example: Determining an Unknown Value Given the Inverse of a Radical Function

#### Question

The function $f(x) = 3\sqrt{x + k} - 2$ has an inverse function given by $f^{-1}(x) = \dfrac{1}{9}(x + 2)^2 + 3.$ What is the value of $k?$

#### Explanation

To find $f^{-1}(x),$ we start by replacing $f(x)$ with $y{:}$

$$



y = 3\sqrt{x+k} - 2



$$

Now, interchanging $x$ and $y$ gives

$$



x = 3\sqrt{y + k} - 2.



$$

Then, we make $y$ the subject of the equation as follows:

$$



\begin{aligned}𝑥 & =3\sqrt{𝑦+𝑘}−2 \\ 3\sqrt{𝑦+𝑘} & =𝑥+2 \\ \sqrt{𝑦+𝑘} & =\frac{1}{3}(𝑥+2) \\ (\sqrt{𝑦+𝑘})^{2} & =(\frac{1}{3}(𝑥+2))^{2} \\ 𝑦+𝑘 & =\frac{1}{9}(𝑥+2)^{2} \\ 𝑦 & =\frac{1}{9}(𝑥+2)^{2}−𝑘\end{aligned}



$$

Therefore, the inverse function is

$$



f^{-1}(x) = \dfrac{1}{9}(x + 2)^2 - k.



$$

Comparing our answer with the given expression, we conclude that

$$



-k = 3 \qquad \Longrightarrow \qquad k = -3.



$$

****: The domain and range of $f(x)$ are given by

$$



x \geq 3, \qquad f(x) \geq -2.



$$

Therefore, the domain and range of $f^{-1}(x)$ are

$$



x \geq -2, \qquad f^{-1}(x) \geq3.



$$
