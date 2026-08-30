# Dividing Polynomials Using Long Division

Source: https://www.mathacademy.com/topics/427?courseId=111
Topic ID: 427

## Prerequisites

- [Dividing Polynomials by Linear Binomials Using Long Division](./2013-dividing-polynomials-by-linear-binomials-using-long-division.md)

## Lesson

### Introduction

The long division method allows us to divide a polynomial by another nonlinear polynomial.

For example, suppose we want to find the quotient and remainder of the following division problem:

$$


\dfrac{-4x^3+4x^2+x+4}{4x^2-1}


$$

Here, the divisor is the quadratic polynomial $4x^2-1$.

Again, we follow a step-by-step process.

**Step 1**

We start by writing the dividend and the divisor as follows:

$$


\begin{aligned} & 4𝑥^{2}−1\,\,\,−\,4𝑥^{3}+4𝑥^{2}+0𝑥+4\,\,\end{aligned}


$$

**Step 2**

We divide the leading term of the dividend $({\color{red}{-4x^3}})$ by the leading term of the divisor $({\color{blue}{4x^2}}).$ This gives $\left(\dfrac{\color{red}{-4x^3}}{{\color{blue}{4x^2}}}\right)={\color{#8b008b}{-x}}.$ We add this result to the quotient line:

$$


\begin{aligned} & 4𝑥^{2}−1\,\,\,\,\,−𝑥 \\ & 4𝑥^{2}−1\,\,\,−\,4𝑥^{3}+4𝑥^{2}+0𝑥+4\,\,\end{aligned}


$$

Next, we multiply the $\color{#8b008b}-x$ we just found by the full divisor ${\color{blue}{4x^2}}-1.$ This gives ${\color{#8b008b}-x}({\color{blue}{4x^2}}-1)=-4x^3+x.$ We place this underneath the dividend, being sure to match the terms. Notice that we include a zero coefficient for the $x^2$ term.

$$


\begin{aligned} & 4𝑥^{2}−1\,\,\,\,\,−𝑥 \\ & 4𝑥^{2}−1\,\,\,−\,4𝑥^{3}+4𝑥^{2}+0𝑥+4\,\, \\ & 4𝑥^{2}−1\,\,\,\,\,\underset{}{−\,4𝑥^{3}+0𝑥^{2}+0𝑥}\end{aligned}


$$

Now, we subtract $-4x^3+0x^2+x$ from $-4x^3+4x^2+x+4$ and get $4x^2+0x+4\mathbin{:}$

$$


\begin{aligned} & 4𝑥^{2}−1\,\,\,\,\,−𝑥 \\ & 4𝑥^{2}−1\,\,\,−\,4𝑥^{3}+4𝑥^{2}+0𝑥+4\,\, \\ & 4𝑥^{2}−1\,\,\,\,\,\underset{}{−\,4𝑥^{3}+0𝑥^{2}+0𝑥} \\ & 4𝑥^{2}−1\,\,\,\,\,\,\,\,−4𝑥^{3}+4𝑥^{2}+0𝑥+4\end{aligned}


$$

**Step 3**

We now repeat the process. The new dividend is ${\color{red}{4x^2}}+0x+4.$

We divide the leading term of the dividend $({\color{red}{4x^2}})$ by the leading term of the divisor $({\color{blue}{4x^2}}).$ This gives $\left(\dfrac{{\color{red}{4x^2}}}{{\color{blue}{4x^2}}}\right)={\color{#8b008b}{1}}.$ We add this result to the quotient:

$$


\begin{aligned} & 4𝑥^{2}−1\,\,\,\,\,−𝑥+1 \\ & 4𝑥^{2}−1\,\,\,−\,4𝑥^{3}+4𝑥^{2}+0𝑥+4\,\, \\ & 4𝑥^{2}−1\,\,\,\,\,\underset{}{−\,4𝑥^{3}+0𝑥^{2}+0𝑥} \\ & 4𝑥^{2}−1\,\,\,\,\,\,\,\,−4𝑥^{3}+4𝑥^{2}+0𝑥+4\end{aligned}


$$

Next, we multiply the ${\color{#8b008b}{1}}$ we just found by the full divisor ${\color{blue}{4x^2}}-1.$ This gives ${\color{#8b008b}{1}}({\color{blue}{4x^2}}-1)=4x^2-1.$ We place this result underneath the dividend:

$$


\begin{aligned} & 4𝑥^{2}−1\,\,\,\,\,−𝑥+1 \\ & 4𝑥^{2}−1\,\,\,−\,4𝑥^{3}+4𝑥^{2}+0𝑥+4\,\, \\ & 4𝑥^{2}−1\,\,\,\,\,\underset{}{−\,4𝑥^{3}+0𝑥^{2}+0𝑥} \\ & 4𝑥^{2}−1\,\,\,\,\,\,\,\,−4𝑥^{3}+4𝑥^{2}+0𝑥+4 \\ & 4𝑥^{2}−1\,\,\,\,\,\,\,\,−4𝑥^{3}+\underset{}{4𝑥^{2}+0𝑥−1}\end{aligned}


$$

Finally, we subtract $4x^2+0x-1$ from $4x^2+0x+4$ to get ${\color{red}{5}}\mathbin{:}$

$$


\begin{aligned} & 4𝑥^{2}−1\,\,\,\,\,−𝑥+1 \\ & 4𝑥^{2}−1\,\,\,−\,4𝑥^{3}+4𝑥^{2}+0𝑥+4\,\, \\ & 4𝑥^{2}−1\,\,\,\,\,\underset{}{−\,4𝑥^{3}+0𝑥^{2}+0𝑥} \\ & 4𝑥^{2}−1\,\,\,\,\,\,\,\,−4𝑥^{3}+4𝑥^{2}+0𝑥+4 \\ & 4𝑥^{2}−1\,\,\,\,\,\,\,\,−4𝑥^{3}+\underset{}{4𝑥^{2}+0𝑥−1} \\ & 4𝑥^{2}−1\,\,\,\,\,\,\,\,−4𝑥^{3}+4𝑥^{2}+0𝑥+\,5\end{aligned}


$$

We're left with the constant $\color{red}5$, which has a smaller degree than the divisor. So, the division is complete.

Therefore, we conclude that

- the quotient of the polynomial division is ${\color{blue}{-x+1}},$ and

- the remainder is ${\color{red}{5}}.$

Our complete result can be summarized as follows:

$$


\frac{-4x^3+4x^2+x+4}{4x^2-1}={\color{blue}{-x+1}} + \dfrac{\color{red}5}{4x^2-1}


$$

### Example: Dividing a Cubic Polynomial by a Quadratic Polynomial

#### Question

Determine the quotient and remainder of $6x^3-x^2+3x+1$ divided by $3x^2+x+2.$

#### Explanation

Using the method of polynomial division, we obtain the following:

$$


\begin{aligned} & 3𝑥^{2}+𝑥+2\,\,\,\,\,2𝑥−1 \\ & 3𝑥^{2}+𝑥+2\,\,\,6𝑥^{3}−0𝑥^{2}+3𝑥+1\,\, \\ & 3𝑥^{2}+𝑥+2\,\,\,\,\,\underset{}{6𝑥^{3}+2𝑥^{2}+4𝑥} \\ & 3𝑥^{2}+𝑥+2\,\,\,\,\,6𝑥^{3}−3𝑥^{2}−0𝑥+1 \\ & 3𝑥^{2}+𝑥+2\,\,\,\,\,\,6𝑥^{3}\underset{}{−\,3𝑥^{2}−0𝑥−2} \\ & 3𝑥^{2}+𝑥+2\,\,\,\,\,\,6𝑥^{3}−3𝑥^{2}−𝑥+\,\,\,3\end{aligned}


$$

Therefore,

- the quotient is ${\color{blue}2x-1},$ and

- the remainder is ${\color{red}3}.$

### Example: Dividing a Quartic Polynomial by a Quadratic or Cubic Polynomial

#### Question

Find the quotient and remainder of the following division problem:

$$


\dfrac {5x^4- 2x^3 - 18x^2 + 11x - 13} {5x^2-2x+2}


$$

#### Explanation

Using the method of polynomial division, we obtain the following:

$$


\begin{aligned} & 5𝑥^{2}−2𝑥+2\,\,\,\,\,𝑥^{2}−4 \\ & 5𝑥^{2}−2𝑥+2\,\,\,5𝑥^{4}−2𝑥^{3}−18𝑥^{2}+11𝑥−13\,\, \\ & 5𝑥^{2}−2𝑥+2\,\,\,\,\,\underset{}{5𝑥^{4}−2𝑥^{3}+02𝑥^{2}} \\ & 5𝑥^{2}−2𝑥+2\,\,\,\,\,5𝑥^{4}−2𝑥^{3}−20𝑥^{2}+11𝑥−13 \\ & 5𝑥^{2}−2𝑥+2\,\,\,\,\,\,5𝑥^{4}−2𝑥^{3}\underset{}{−\,20𝑥^{2}+08𝑥−08} \\ & 5𝑥^{2}−2𝑥+2\,\,\,\,\,\,\,5𝑥^{4}−2𝑥^{3}−20𝑥^{2}+03𝑥−05\end{aligned}


$$

As a result,

- the quotient is $x^2-4,$ and

- the remainder is $3x-5.$

Therefore,

$$


\dfrac{5x^4-2x^3-18x^2+11x-13}{5x^2-2x+2}=x^2-4 + \dfrac{3x-5}{5x^2-2x+2}.


$$

### Example: Dividing Polynomials When the Dividend Contains Zero Coefficients

#### Question

Find the quotient and remainder of the following division problem:

$$


\dfrac{2x^4 - 7x^2 - x + 8}{x^2 - 1}


$$

#### Explanation

Notice that the dividend is missing the $x^3$ term. So, we first rewrite it by including the missing term with a coefficient of zero, as follows:

$$


2x^4-7x^2-x+8 = 2x^4+{\color{red}0}x^3-7x^2-x+8


$$

Now, using the method of polynomial division, we obtain the following:

$$


\begin{aligned} & 𝑥^{2}−1\,\,\,\,\,2𝑥^{2}−5 \\ & 𝑥^{2}−1\,\,\,2𝑥^{4}+0𝑥^{3}−7𝑥^{2}−0𝑥+8\,\, \\ & 𝑥^{2}−1\,\,\,\,\,\underset{}{2𝑥^{4}+0𝑥^{3}−2𝑥^{2}} \\ & 𝑥^{2}−1\,\,\,\,\,2𝑥^{4}+0𝑥^{3}−5𝑥^{2}−0𝑥+8 \\ & 𝑥^{2}−1\,\,\,\,\,\,2𝑥^{4}+0𝑥^{3}\underset{}{−\,5𝑥^{2}+0𝑥+5} \\ & 𝑥^{2}−1\,\,\,\,\,\,\,2𝑥^{4}+0𝑥^{3}−5𝑥^{2}−0𝑥+3\end{aligned}


$$

As a result,

- the quotient is ${2x^2 - 5},$ and

- the remainder is ${-x+3}.$

Therefore,

$$


\dfrac{2x^4 - 7x^2 - x +8}{x^2 - 1} = 2x^2-5 + \dfrac{-x+3}{x^2-1}.


$$

We can rewrite this result as follows:

$$


\dfrac{2x^4 - 7x^2 - x +8}{x^2 - 1} = 2x^2-5 - \dfrac{x-3}{x^2-1}


$$
