# Euler's Totient Function

Source: https://www.mathacademy.com/topics/2654?courseId=109
Topic ID: 2654

## Prerequisites

- [The Euclidean Algorithm](../methods-of-proof/2676-the-euclidean-algorithm.md)

## Lesson

### Introduction

Given a natural number $n,$ **Euler's totient function** $\phi(n)$ returns the number of positive integers that are less than $n$ and are coprime to $n.$ Here, $\phi$ is the Greek letter phi.

To illustrate, let's calculate $\phi(12).$ Since $12$ is a small number, we can first write down all positive integers that are less than $12,$ and then remove any numbers that are not coprime to $12\mathbin{:}$

$$



 1, \: \bcancel{2}, \: \bcancel{3}, \: \bcancel{4}, \: {5}, \: \bcancel{6}, \: {7}, \: \bcancel{8}, \: \bcancel{9}, \: \bcancel{10}, 11



$$

We end up with only $4$ positive integers that are less than $12$ and are coprime to $12.$ These numbers are $1,5,7,$ and $11.$ Therefore,

$$



\phi(12) = 4.



$$

### Example: Evaluating Euler's Totient Function in the Simplest Cases

#### Question

What is the value of $\phi(47),$ where $\phi$ is Euler's totient function?

#### Explanation

Given a natural number $n,$ Euler's totient function $\phi(n)$ returns the total number of positive integers that are less than $n$ and are coprime to $n.$

First, notice that $47$ is a prime number. This means that all positive integers that are less than $47$ are coprime to $47.$ That is to say, the numbers $1,2,3, \ldots, 46$ are all coprime to $47.$

Therefore,

$$



\phi(47) = 47-1 = 46.



$$

In general, $\phi(p) = p-1,$ where $p$ is prime.

### Euler's Totient Function When the Argument is a Power of a Prime

There is a nice rule that allows us to easily calculate Euler's totient function when the argument is a prime number raised to a positive integer power.

*If $p$ is a prime and $k$ is a positive integer, then*

$$



\phi \left(p^k\right)=p^k-p^{k-1}.



$$

For example, suppose that we want to calculate $\phi(2^7).$ First, notice that $2^7$ is the seventh power ($k=7$) of the prime number $p=2.$ Therefore,

$$



\begin{aligned}𝜙(2^{7}) & =𝑝^{𝑘}−𝑝^{𝑘−1} \\ & =2^{7}−2^{7−1} \\ & =128−64 \\ & =64.\end{aligned}



$$

To see why this rule works, recall that $\phi(p^k)$ returns the number of positive integers less than $p^k$ that are coprime to $p^k.$

Now, since $p$ is a prime number, we have that

- the only possible values of $\mathrm{gcd}\left(m, p^k\right)$ are $1,p, p^2, \ldots, p^{k},$ and

- $\mathrm{gcd}\left(m, p^k\right)\neq 1$ only if $m$ is a multiple of $p,$ i.e., $m= p, \: 2p, \: \ldots, \: p^{k-1}p.$

So, since there are $p^{k-1}$ multiples of $p$ that are less than or equal to $p^k,$ there must be $p^k-p^{k-1}$ numbers less than $p^k$ that are coprime to $p^k.$ Therefore, $\phi \left(p^k\right)=p^k-p^{k-1}.$

### Example: Evaluating Euler's Totient Function When the Argument is a Prime Raised to a Power

#### Question

What is the value of $\phi(32),$ where $\phi$ is Euler's totient function?

#### Explanation

Given a natural number $n,$ Euler's totient function $\phi(n)$ returns the total number of positive integers that are less than $n$ and are coprime to $n.$

Moreover, if $n=p^k,$ where $k\geq 1$ is a natural number and $p$ is prime, then

$$



\phi(n) = \phi(p^k) = p^k - p^{k-1}.



$$

Notice that $32 = 2^5$ is the fifth power ($k=5$) of the prime number $p=2.$ Therefore,

$$



\begin{aligned}𝜙(2^{5}) & =𝑝^{𝑘}−𝑝^{𝑘−1} \\ & =2^{5}−2^{5−1} \\ & =32−16 \\ & =16.\end{aligned}



$$

### The Multiplicativity of Euler's Totient Function

It can be shown that Euler's totient function is a **multiplicative function**, meaning that if two positive integers $m$ and $n$ are coprime, then

$$



\phi(mn) = \phi(m)\phi(n).



$$

This property can be used to simplify many calculations.

For example, let's use the property to calculate $\phi(51).$ First, notice that

$$



51 = 3 \cdot 17.



$$

Since $3$ and $17$ are prime numbers, we have

$$



\begin{aligned}𝜙(3) & =3−1=2, \\ 𝜙(17) & =17−1=16.\end{aligned}



$$

Then, using that $\phi$ is multiplicative and $\text{gcd}(3,17)=1,$ we obtain

$$



\begin{aligned}𝜙(51) & =𝜙(3)⋅𝜙(17) \\ & =2⋅16 \\ & =32.\end{aligned}



$$

### Example: Evaluating Euler's Totient Function Using the Multiplicative Property

#### Question

Evaluate $\phi(210),$ where $\phi$ is Euler's totient function.

#### Explanation

Given a natural number $n,$ Euler's totient function $\phi(n)$ returns the total number of positive integers that are less than $n$ and are coprime to $n.$

Recall that Euler's totient function is a multiplicative function, meaning that if two positive integers $m$ and $n$ are coprime, then

$$



\phi(mn) = \phi(m)\phi(n).



$$

First, notice that

$$



210 = 5\cdot 6 \cdot 7.



$$

- Since $5$ and $7$ are distinct prime numbers, we have

- To compute $\phi(6),$ let's write down all positive integers that are less than $6$ and cancel out the numbers that are not coprime to $6\mathbin{:}$ So, $\phi(6) = 2.$

Finally, since $\phi$ is multiplicative and $\text{gcd}(5,6,7)=1,$ we obtain

$$



\begin{aligned}𝜙(210) & =𝜙(5)⋅𝜙(6)⋅𝜙(7) \\ & =4⋅2⋅6 \\ & =48.\end{aligned}



$$

### The General Formula for Euler's Totient Function

**Euler's product formula** for computing states that if where are distinct prime numbers and are positive integer exponents, then

To illustrate how this formula works, let's use it to evaluate

First, note that

So, using the formula, we get

### Example: Evaluating Euler's Totient Function Using the Fundamental Theorem of Arithmetic

#### Question

Evaluate $\phi(405),$ where $\phi$ is Euler's totient function.

#### Explanation

Given a natural number $n,$ Euler's totient function $\phi(n)$ returns the total number of positive integers that are less than $n$ and are coprime to $n.$

Recall that if

$$



n=p_1^{k_1} \cdot p_2^{k_2} \cdot \cdots \cdot p_s^{k_s},



$$

where $p_1,p_2, \ldots, p_s$ are distinct prime numbers, then

$$



\phi(n) = n\left(1-\dfrac{1}{p_1}\right)\left(1-\dfrac{1}{p_2}\right)\cdots\left(1-\dfrac{1}{p_s}\right).



$$

Now, notice that

$$



\begin{aligned}405 & =81⋅5 \\ & =3^{4}⋅5.\end{aligned}



$$

Therefore, we get

$$



\begin{aligned}𝜙(3^{4}⋅5) & =𝑛(1−\frac{1}{𝑝_{1}})(1−\frac{1}{𝑝_{2}}) \\ & =(3^{4}⋅5)⋅(1−\frac{1}{3})(1−\frac{1}{5}) \\ & =3^{4}⋅5⋅\frac{2}{3}⋅\frac{4}{5} \\ & =3^{3}⋅2⋅4 \\ & =27⋅8 \\ & =216.\end{aligned}



$$

### Proof of the General Formula

We've been using Euler's product formula, which states that if

$$



n=p_1^{k_1} \cdot p_2^{k_2} \cdot \cdots \cdot p_s^{k_s},



$$

where $p_1,p_2, \ldots, p_s$ are distinct prime numbers, then

$$



\phi(n) = n\left(1-\dfrac{1}{p_1}\right)\left(1-\dfrac{1}{p_2}\right)\cdots\left(1-\dfrac{1}{p_s}\right).



$$

Let's now prove Euler's product formula in the general case.

Let $n=p_1^{k_1} \cdot p_2^{k_2} \cdot \cdots \cdot p_s^{k_s},$ where $p_1,p_2, \ldots, p_s$ are distinct primes. Then, since

$$



\mathrm{gcd}\left(p_1^{k_1}, p^{k_2}, \ldots, p_s^{k_s}\right) =1



$$

and since $\phi$ is a multiplicative function, we have

$$



\begin{aligned}𝜙(𝑛) & =𝜙(𝑝_{𝑘_{1}1}^{}𝑝_{𝑘_{2}2}^{}⋯𝑝_{𝑘_{𝑠}𝑠}^{}) \\ & =𝜙(𝑝_{𝑘_{1}1}^{})⋅𝜙(𝑝_{𝑘_{2}2}^{})⋯𝜙(𝑝_{𝑘_{𝑠}𝑠}^{}) \\ & =(𝑝_{𝑘_{1}1}^{}−𝑝_{𝑘_{1}−11}^{})⋅(𝑝_{𝑘_{2}2}^{}−𝑝_{𝑘_{2}−12}^{})⋅(𝑝_{𝑘_{𝑠}𝑠}^{}−𝑝_{𝑘_{𝑠}−1𝑠}^{}).\end{aligned}



$$

Now, observe that

$$



p^k-p^{k-1}= p^{k}(1-p^{-1}) = p^k\left(1-\dfrac{1}{p}\right).



$$

So, we have

$$



\begin{aligned}𝜙(𝑛) & =(𝑝_{𝑘_{1}1}^{}−𝑝_{𝑘_{1}−11}^{})(𝑝_{𝑘_{2}2}^{}−𝑝_{𝑘_{2}−12}^{})⋅(𝑝_{𝑘_{𝑠}𝑠}^{}−𝑝_{𝑘_{𝑠}−1𝑠}^{}) \\ & =𝑝_{𝑘_{1}1}^{}(1−\frac{1}{𝑝_{1}})⋅𝑝_{𝑘_{2}2}^{}(1−\frac{1}{𝑝_{2}})⋯𝑝_{𝑘_{𝑠}𝑠}^{}(1−\frac{1}{𝑝_{𝑠}}) \\ & =𝑝_{𝑘_{1}1}^{}𝑝_{𝑘_{2}2}^{}⋯𝑝_{𝑘_{𝑠}𝑠}^{}(1−\frac{1}{𝑝_{1}})(1−\frac{1}{𝑝_{2}})⋯(1−\frac{1}{𝑝_{𝑠}}) \\ & =𝑛(1−\frac{1}{𝑝_{1}})(1−\frac{1}{𝑝_{2}})⋯(1−\frac{1}{𝑝_{𝑠}}).\end{aligned}



$$
