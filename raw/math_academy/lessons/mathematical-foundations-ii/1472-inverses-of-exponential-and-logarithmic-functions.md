# Inverses of Exponential and Logarithmic Functions

Source: https://www.mathacademy.com/topics/1472?courseId=111
Topic ID: 1472

## Prerequisites

- [Calculating the Inverse of a Function](./627-calculating-the-inverse-of-a-function.md)
- [Solving Equations Containing the Exponential Function](./870-solving-equations-containing-the-exponential-function.md)
- [Solving Logarithmic Equations Containing the Natural Logarithm](./1551-solving-logarithmic-equations-containing-the-natural-logarithm.md)

## Lesson

### Introduction

Suppose we have the transformed exponential function

$$


f(x)=2^{5x}+1


$$

and we wish to find the inverse function $f^{-1}(x).$ We can do this using the following three steps.

**Step 1:** We start by replacing $f(x)$ with $y\mathbin{:}$

$$


\begin{aligned}𝑦 & =2^{5𝑥}+1\end{aligned}


$$

**Step 2:** Then, we interchange $x$ and $y\mathbin{:}$

$$


\begin{aligned}𝑥 & =2^{5𝑦}+1\end{aligned}


$$

**Step 3:** Finally, we make $y$ the subject of the equation:

$$


\begin{aligned}𝑥 & =2^{5𝑦}+1 \\ 𝑥−1 & =2^{5𝑦} \\ log_{2}⁡(𝑥−1) & =log_{2}⁡(2^{5𝑦}) \\ log_{2}⁡(𝑥−1) & =5𝑦 \\ 5𝑦 & =log_{2}⁡(𝑥−1) \\ 𝑦 & =\frac{1}{5}log_{2}⁡(𝑥−1)\end{aligned}


$$

Therefore, the inverse function is

$$


f^{-1}(x) = \dfrac{1}{5}\log_2{(x-1)}.


$$

### Example: Finding Inverses of Exponential Functions With Up to Two Transformations

#### Question

The function $f(x) = e^{x-k}+2$ has an inverse function given by $f^{-1}(x) = \ln{(x-2)}+4.$ What is the value of $k?$

#### Explanation

To find $f^{-1}(x),$ we start by replacing $f(x)$ with $y\mathbin{:}$

$$


\begin{aligned}𝑦 & =𝑒^{𝑥−𝑘}+2\end{aligned}


$$

Now, interchanging $x$ and $y$ gives

$$


\begin{aligned}𝑥 & =𝑒^{𝑦−𝑘}+2.\end{aligned}


$$

Finally, we make $y$ the subject of the equation, as follows:

$$


\begin{aligned}𝑥 & =𝑒^{𝑦−𝑘}+2 \\ 𝑒^{𝑦−𝑘} & =𝑥−2 \\ ln⁡(𝑒^{𝑦−𝑘}) & =ln⁡(𝑥−2) \\ 𝑦−𝑘 & =ln⁡(𝑥−2) \\ 𝑦 & =ln⁡(𝑥−2)+𝑘\end{aligned}


$$

Therefore, the inverse function is $f^{-1}(x) = \ln{(x-2)} + k.$

Comparing our answer with the given expression, we conclude that $k=4.$

### Example: Finding Inverses of Exponential Functions With More Than Two Transformations

#### Question

Find the inverse of the function $f(x) = \dfrac12 e^{x+8}-2.$

#### Explanation

To find $f^{-1}(x),$ we start by replacing $f(x)$ with $y\mathbin{:}$

$$


\begin{aligned}𝑦 & =\frac{1}{2}𝑒^{𝑥+8}−2\end{aligned}


$$

Now, interchanging $x$ and $y$ gives

$$


\begin{aligned}𝑥 & =\frac{1}{2}𝑒^{𝑦+8}−2.\end{aligned}


$$

Finally, we make $y$ the subject of the equation, as follows:

$$


\begin{aligned}𝑥 & =\frac{1}{2}𝑒^{𝑦+8}−2 \\ \frac{1}{2}𝑒^{𝑦+8} & =𝑥+2 \\ 𝑒^{𝑦+8} & =2𝑥+4 \\ ln⁡(𝑒^{𝑦+8}) & =ln⁡(2𝑥+4) \\ 𝑦+8 & =ln⁡(2𝑥+4) \\ 𝑦 & =ln⁡(2𝑥+4)−8\end{aligned}


$$

Therefore, the inverse function is $f^{-1}(x) = \ln{(2x+4)} - 8.$

### Finding the Inverse of a Transformed Logarithmic Function

Now suppose we wish to find the inverse of the logarithmic function

$$


f(x)=3\log_{2}(x-1)+1.


$$

We can find $f^{-1}(x)$ using the same three steps as before.

**Step 1:** We start by replacing $f(x)$ with $y{:}$

$$


y = 3\log_{2}(x-1)+1


$$

**Step 2:** Then, we interchange $x$ and $y\mathbin{:}$

$$


x = 3\log_{2}(y-1)+1


$$

**Step 3:** Finally, we make $y$ the subject of the equation:

$$


\begin{aligned}3log_{2}⁡(𝑦−1)+1 & =𝑥 \\ 3log_{2}⁡(𝑦−1) & =𝑥−1 \\ log_{2}⁡(𝑦−1) & =\frac{𝑥−1}{3} \\ 2^{log_{2}⁡(𝑦−1)} & =2^{(𝑥−1)/3} \\ 𝑦−1 & =2^{(𝑥−1)/3} \\ 𝑦 & =2^{(𝑥−1)/3}+1\end{aligned}


$$

Therefore, the inverse function is

$$


f^{-1}(x) = {2}^{(x-1)/3}+1.


$$

### Example: Finding Inverses of Logarithmic Functions With Up to Two Transformations

#### Question

What is the inverse of $f(x) =\ln(x+3)+6?$

#### Explanation

To find $f^{-1}(x),$ we start by replacing $f(x)$ with $y\mathbin{:}$

$$


y = \ln(x+3)+6


$$

Then, we swap $x$ and $y{:}$

$$


\begin{aligned}𝑥 & =ln⁡(𝑦+3)+6\end{aligned}


$$

Finally, we make $y$ the subject of the equation, as follows:

$$


\begin{aligned}𝑥 & =ln⁡(𝑦+3)+6 \\ ln⁡(𝑦+3) & =𝑥−6 \\ 𝑒^{ln⁡(𝑦+3)} & =𝑒^{𝑥−6} \\ 𝑦+3 & =𝑒^{𝑥−6} \\ 𝑦 & =𝑒^{𝑥−6}−3\end{aligned}


$$

Therefore, the inverse function is $f^{-1}(x) = e^{x-6}-3.$

### Example: Finding Inverses of Logarithmic Functions With More Than Two Transformations

#### Question

What is the inverse of $f(x) = 2\log_4(3x)-1?$

#### Explanation

To find $f^{-1}(x),$ we start by replacing $f(x)$ with $y\mathbin{:}$

$$


\begin{aligned}𝑦 & =2log_{4}⁡(3𝑥)−1\end{aligned}


$$

Then, we swap $x$ and $y{:}$

$$


\begin{aligned}𝑥 & =2log_{4}⁡(3𝑦)−1\end{aligned}


$$

Finally, we make $y$ the subject of the equation, as follows:

$$


\begin{aligned}𝑥 & =2log_{4}⁡(3𝑦)−1 \\ 2log_{4}⁡(3𝑦) & =𝑥+1 \\ log_{4}⁡(3𝑦) & =\frac{𝑥+1}{2} \\ 4^{log_{4}⁡(3𝑦)} & =4^{(𝑥+1)/2} \\ 3𝑦 & =4^{(𝑥+1)/2} \\ 𝑦 & =\frac{1}{3}4^{(𝑥+1)/2}\end{aligned}


$$

Therefore, the inverse function is $f^{-1}(x) =\dfrac13 4^{(x+1)/2}.$
