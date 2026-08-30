# Evaluating Logarithms

Source: https://www.mathacademy.com/topics/378?courseId=111
Topic ID: 378

## Prerequisites

- [Converting From Logarithmic to Exponential Form](./457-converting-from-logarithmic-to-exponential-form.md)

## Lesson

### Introduction

We can evaluate some logarithm expressions by using the fact that the logarithm reverses the action of the exponent.

The idea is that the log of a power of the base equals the power itself:

$$


\log_b(b^x) = x


$$

For example, in the case of $\log_2 \left(2^{-1/2}\right),$ we have $b=2$ and $x=-\dfrac 1 2.$ Therefore,

$$


\log_2\left(2^{-1/2}\right) = -\dfrac{1}{2}.


$$

### Example: Evaluating Logarithms Using the Definition

#### Question

Evaluate $\log_{2} \left(2^{5} \right).$

#### Explanation

The logarithm reverses the action of the exponent. The idea is that the log of a power of the base equals the power itself:

$$


\log_b(b^x) = x


$$

In our case, we have $b=2$ and $x=5.$ Therefore,

$$


\log_{2}\left( 2^{5}\right) = 5.


$$

### Evaluating Logarithms Using Exponents

When the argument of the logarithm isn't written as an exponential, we can often still evaluate the logarithm. All we need to do is rewrite the argument so that it is in the form $b^x,$ where $b$ is the base of the logarithm.

For instance, to evaluate $\log_2\left(8\right),$ we rewrite $8$ as a power of $2$ (the base of the logarithm) as follows:

$$


8 = 2^{3}


$$

Therefore, we have

$$


\log_{2}{8} = \log_{2}\left(2^{3}\right) .


$$

Now we can proceed as before. The log of a power of the base equals the power itself:

$$


\log_b(b^x) = x


$$

In our case, we have $b = 2$ and $x = 3.$ Therefore,

$$


\log_{2}\left(2^{3}\right) = 3.


$$

### Example: Evaluating Logarithms Using Exponents

#### Question

Find the value of $\log_{3}{9}.$

#### Explanation

First, we rewrite $9$ as a power of $3$ (the base of the logarithm) as follows:

$$


9 = 3^2


$$

Therefore, we have

$$


\log_{3}{9} = \log_{3}(3^2).


$$

Now we can proceed as usual. The log of a power of the base equals the power itself:

$$


\log_b(b^x) = x


$$

In our case, we have $b = 3$ and $x = 2.$ Therefore,

$$


\log_{3}(3^2) = 2.


$$

### Example: Evaluating the Logarithm of a Fraction or Root

#### Question

Evaluate $\log_{2} \left(\dfrac 1 {8} \right).$

#### Explanation

First, we rewrite $\dfrac{1}{8}$ as a power of $2$ (the base of the logarithm) as follows:

$$


\dfrac{1}{8} = \dfrac{1}{2^3} = 2^{-3}


$$

Therefore, we have

$$


\log_{2} \left(\dfrac 1 {8} \right)= \log_{2} (2^{-3}).


$$

Now we can proceed as usual. The log of a power of the base equals the power itself:

$$


\log_b(b^x) = x


$$

In our case, we have $b=2$ and $x=-3.$ Therefore,

$$


\log_{2}( 2^{-3} )= -3.


$$

### Special Values of Logarithms

Recall that two special cases of exponentials are

$$


n^0 =1 \qquad \text{and} \qquad n^1 =n.


$$

What do these look like in logarithm form? We can use the definition of a logarithm to find out:

$a = {n}^{x}$ is equivalent to $\log_{n}{a} = {x}.$

Using the above, we have that $n^0 =1$ is equivalent to

$$


\log_n 1 = 0.


$$

Also, we have that $n^1 =n$ is equivalent to

$$


\log_n n = 1.


$$

These are two special values for logarithms that are true for any base $n>0, n \neq 1.$

**Watch out!** We should always assume that the base $n$ of the logarithm does not equal $1.$ Recall that $\log_n{a} = x$ is equivalent to $a = n^x.$ If $n=1$ that transforms to

$$


a = 1^x.


$$

Now, we have the following two possibilities:

- if $a \neq 1,$ we get that $a \neq 1^x$ for any real $x,$ and

- if $a = 1,$ we obtain that $1 = 1^x$ for all real $x.$

In both cases, the notation $\log_1{a}$ does not make much sense.

### Example: Evaluating Special Values of Logarithms

#### Question

Find the value of $\log_{8}{8}.$

#### Explanation

We have the general rule that

$$


\log_n n = 1.


$$

In our case, $n=8.$ Therefore,

$$


\log_{8}{8} =1.


$$
