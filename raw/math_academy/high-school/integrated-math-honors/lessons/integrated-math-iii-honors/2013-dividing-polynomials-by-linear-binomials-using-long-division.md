# Dividing Polynomials by Linear Binomials Using Long Division

Source: https://www.mathacademy.com/topics/2013?courseId=101
Topic ID: 2013

## Prerequisites

- [Multiplying Polynomials](../../../traditional/lessons/algebra-i/361-multiplying-polynomials.md)
- [Multiplying Rational Expressions](../../../traditional/lessons/algebra-ii/435-multiplying-rational-expressions.md)

## Lesson

### Introduction

Suppose we want to divide one polynomial by another. For example,

$$


\dfrac{2x^2+8x-5}{x+5}.


$$

First, let's introduce some terminology:

- the **dividend** is the polynomial that we want to divide ($2x^2+8x-5$)

- the **divisor** is the polynomial by which we want to divide the dividend ($x+5$)

- the result of the division is the **quotient**

- the **remainder** is what is left after the division

To carry out this division, we will use the method of **long division of polynomials**.

**Note:** Up to now, you may have used synthetic division for this kind of task. However, you should still learn the long division method. As we'll soon see, long division allows us to divide any two polynomials, whereas synthetic division only works if the divisor is a linear binomial.

### A Worked Example

Our task is to find the quotient and remainder of the following division problem:

$$


\dfrac{2x^2+8x-5}{x+5}


$$

Before we start, we need to check that the polynomials are written in standard form. In this case, the terms in both the numerator and denominator are in descending order of their degree, so we're ready to begin.

To carry out the division, we follow the following step-by-step process.

**Step 1**

We start by writing the dividend and the divisor as follows:

$$


\begin{aligned} & 𝑥+2\,\,\,\,\, \\ & 𝑥+5\,\,\,2𝑥^{2}+18𝑥−15\,\,\end{aligned}


$$

**Step 2**

We divide the leading term of the dividend $({\color{red}2x^2})$ by the leading term of the divisor $({\color{blue}x}).$ This gives $\left(\dfrac{{\color{red}2x^2}}{{\color{blue}x}}\right)={\color{#8b008b}2x}.$ We write this result in the quotient line:

$$


\begin{aligned} & 𝑥+5\,\,\,\,\,2𝑥 \\ & 𝑥+5\,\,\,2𝑥^{2}+18𝑥−15\,\,\end{aligned}


$$

Next, we multiply the ${\color{#8b008b}{2x}}$ we just found by the full divisor ${{\color{blue}{x}}+5}.$ This gives ${\color{#8b008b}{2x}}{({\color{blue}{x}}+5)}={2x^2+10x}.$ We place this result underneath the dividend:

$$


\begin{aligned} & 𝑥+5\,\,\,\,\,2𝑥 \\ & 𝑥+5\,\,\,2𝑥^{2}+18𝑥−15\,\, \\ & 𝑥+2\,\,\,\,\,\underset{}{2𝑥^{2}+10𝑥−18}\end{aligned}


$$

Now, we subtract ${2x^2+10x}$ from ${2x^2+8x - 5}$ and get ${{-2x-5}}{:}$

$$


\begin{aligned} & 𝑥+5\,\,\,\,\,2𝑥 \\ & 𝑥+5\,\,\,2𝑥^{2}+18𝑥−15\,\, \\ & 𝑥+2\,\,\,\,\,\underset{}{2𝑥^{2}+10𝑥−18} \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}1−2𝑥−5\end{aligned}


$$

**Step 3**

We now repeat the process. The dividend is now ${{\color{red}{-2x}}-5}.$

We divide the leading term of the dividend $({\color{red}-2x})$ by the leading term of the divisor $({\color{blue}x}).$ This gives $\left(\dfrac{{\color{red}-2x}}{{\color{blue}x}}\right)={\color{#8b008b}{-2}}.$ We write this result in the quotient line:

$$


\begin{aligned} & 𝑥+5\,\,\,\,\,2𝑥\,\,−12 \\ & 𝑥+5\,\,\,2𝑥^{2}+18𝑥−15\,\, \\ & 𝑥+2\,\,\,\,\,\underset{}{2𝑥^{2}+10𝑥−18} \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}1−2𝑥−5 \\ & \end{aligned}


$$

Next, we multiply the ${\color{#8b008b}{-2}}$ term we just found by the full divisor ${{\color{blue}{x}}+5}.$ This gives ${\color{#8b008b}{-2}}({{\color{blue}{x}}+5})={-2x-10}.$ We place this result underneath the dividend:

$$


\begin{aligned} & 𝑥+5\,\,\,\,\,2𝑥\,\,−12 \\ & 𝑥+5\,\,\,2𝑥^{2}+18𝑥−15\,\, \\ & 𝑥+2\,\,\,\,\,\underset{}{2𝑥^{2}+10𝑥−18} \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}−12𝑥−15 \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}\underset{}{−12𝑥−10}\end{aligned}


$$

Finally, we subtract ${{-2x-10}}$ from ${{-2x-5}}$ to get ${\color{red}{5}}{:}$

$$


\begin{aligned} & 𝑥+5\,\,\,\,\,2𝑥\,\,−12 \\ & 𝑥+5\,\,\,2𝑥^{2}+18𝑥−15\,\, \\ & 𝑥+2\,\,\,\,\,\underset{}{2𝑥^{2}+10𝑥−18} \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}−12𝑥−15 \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}\underset{}{−12𝑥−10} \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}−12𝑥−15\end{aligned}


$$

We're left with the constant ${\color{red}{5}}.$ Therefore, we conclude that

- the quotient of the polynomial division is $\color{blue}{2x-2},$ and

- the remainder is ${\color{red}{5}}.$

### Example: Dividing a Polynomial by a Linear Binomial

#### Question

From top to bottom, what are the missing expressions in the following polynomial division problem?

$$


\begin{aligned} & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\phantom{2x+20} \\ & 𝑥−4\,\,\,2𝑥^{2}+12𝑥+25\,\, \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\underset{}{2𝑥^{2}−\,\,8𝑥} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,4𝑥^{2}−\phantom{20x+25} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,4𝑥^{2}−\underset{}{20𝑥−80} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,4𝑥^{2}+26𝑥\,\,\,\,105 \\ & \end{aligned}


$$

#### Explanation

Using the method of polynomial division, we obtain the following:

$$


\begin{aligned} & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,2𝑥+20 \\ & 𝑥−4\,\,\,2𝑥^{2}+12𝑥+25\,\, \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\underset{}{2𝑥^{2}−\,\,8𝑥} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,4𝑥^{2}−20𝑥+25 \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,4𝑥^{2}−\underset{}{20𝑥−80} \\ & \,\,\,\,\,\,\,\,\,\,\,\,\,\,\,\,4𝑥^{2}+26𝑥\,\,\,\,105 \\ & \end{aligned}


$$

Therefore, the missing expressions are $2x+20$ and $20x+25.$

### Writing the Result of a Polynomial Division

When we divide a dividend by a divisor, we get a quotient and a remainder.

In general, we can write the result of any division as follows:

$$


\frac{\text{dividend}}{\text{divisor}}={\color{blue}\text{quotient}} +\dfrac{{\color{red}\text{remainder}}}{\text{divisor}}


$$

### Example: Writing the Result of Dividing a Polynomial by a Linear Binomial

#### Question

Consider the following polynomial division:

$$


\begin{aligned} & 𝑥+2\,\,\,\,\,2𝑥−2 \\ & 𝑥+5\,\,\,2𝑥^{2}+18𝑥−15\,\, \\ & 𝑥+2\,\,\,\,\,\underset{}{2𝑥^{2}+10𝑥−15} \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}−12𝑥−15 \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}\underset{}{−12𝑥−10} \\ & 𝑥+2\,\,\,\,\,\,\,\,\,3𝑥^{2}−2𝑥−15\end{aligned}


$$

From the above, what is $\dfrac{2x^2+8x-5}{x+5}?$

#### Explanation

$$


\begin{aligned} & 𝑥+2\,\,\,\,\,2𝑥−2 \\ & 𝑥+5\,\,\,2𝑥^{2}+18𝑥−15\,\, \\ & 𝑥+2\,\,\,\,\,\underset{}{2𝑥^{2}+10𝑥−15} \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}−12𝑥−15 \\ & 𝑥+2\,\,\,\,\,\,\,3𝑥^{2}\underset{}{−12𝑥−10} \\ & 𝑥+2\,\,\,\,\,\,\,\,\,3𝑥^{2}−2𝑥−15\end{aligned}


$$

From the given polynomial division, we deduce that dividing the polynomial $2x^2+8x -5$ by the linear binomial ${\color{purple}x+5}$ gives

- the quotient ${\color{blue}2x-2},$ and

- the remainder ${\color{red}5}.$

Therefore, we obtain

$$


\dfrac{2x^2+8x-5}{x+5} = {\color{blue}2x-2}+\dfrac{\color{red}5}{\color{purple}x+5}.


$$

### Dealing With Missing Terms in the Dividend

When using polynomial division, we must write both the dividend and divisor in descending powers of $x.$

If there are missing powers of $x,$ then we need to introduce these terms using zero coefficients.

For example, consider the following division problem:

$$


\dfrac{x^2+5}{x+1}


$$

Notice that the dividend has no $x$ term. To use polynomial division, we need to fill in the missing term using a coefficient of zero. This gives

$$


\dfrac{x^2+{\color{blue} 0x}+5}{x+1}.


$$

The polynomial in the dividend now contains every term in the correct order with nothing missing.

### Example: Dividing a Polynomial With Some Zero Coefficients by a Linear Binomial

#### Question

From top to bottom, what are the missing expressions in the following polynomial division problem?

$$


\begin{aligned} & 𝑥+1\,\,\,\,\phantom{x^2 - x + 1} \\ & 𝑥+1\,\,\,𝑥^{3}+0𝑥^{2}+0𝑥+64\,\, \\ & 𝑥+1\,\,\,\,\,\underset{}{𝑥^{3}+0𝑥^{2}} \\ & 𝑥+1\,\,\,\,\,\,𝑥^{3}−\,0𝑥^{2}+0𝑥+64 \\ & 𝑥+1\,\,\,\,\,\,𝑥^{3}\underset{}{−\,0𝑥^{2}−0𝑥} \\ & 𝑥+1\,\,\,\,\,\,\,\,𝑥^{3}−𝑥^{2}−\,\phantom{x + 64} \\ & 𝑥+1\,\,\,\,\,\,\,\,\,𝑥^{3}−𝑥^{2}−\,\underset{}{𝑥+11} \\ & 𝑥+1\,\,\,\,\,\,\,\,\,𝑥^{3}−𝑥^{2}+𝑥−\,63\end{aligned}


$$

#### Explanation

Notice that the dividend is missing the $x^2$-term and the $x$-term. So, we write it using zero coefficients, as follows:

$$


x^3+{\color{red}0}x^2 + {\color{red}0}x + 64


$$

Using the method of polynomial division, we obtain the following:

$$


\begin{aligned} & 𝑥+1\,\,\,\,\,𝑥^{2}−𝑥+1 \\ & 𝑥+1\,\,\,𝑥^{3}+0𝑥^{2}+0𝑥+64\,\, \\ & 𝑥+1\,\,\,\,\,\underset{}{𝑥^{3}+0𝑥^{2}} \\ & 𝑥+1\,\,\,\,\,\,𝑥^{3}−\,0𝑥^{2}+0𝑥+64 \\ & 𝑥+1\,\,\,\,\,\,𝑥^{3}\underset{}{−\,0𝑥^{2}−0𝑥} \\ & 𝑥+1\,\,\,\,\,\,\,\,\,𝑥^{3}−𝑥^{2}−\,𝑥+64 \\ & 𝑥+1\,\,\,\,\,\,\,\,\,𝑥^{3}−𝑥^{2}−\,\underset{}{𝑥+11} \\ & 𝑥+1\,\,\,\,\,\,\,\,\,𝑥^{3}−𝑥^{2}+𝑥−\,63\end{aligned}


$$

Therefore, the missing expressions are

$\qquad$ $x^2 - x + 1\quad$ and $\quad x + 64.$

### Checking a Polynomial Division Result

To check that a polynomial division result is correct, we can multiply both sides of the equation by the divisor and ensure that both sides are equal.

For example, let's check that the following polynomial division result is correct.

$$


\frac{2x^2+8x - 5}{x+5}=2x-2 +\dfrac{5}{x+5}


$$

First, we multiply the above by $(x+5)$ and simplify:

$$


\begin{aligned}(𝑥+5)×(\frac{2𝑥^{2}+8𝑥−5}{𝑥+5}) & =(𝑥+5)×(2𝑥−2+\frac{5}{𝑥+5}) \\ \frac{(2𝑥^{2}+8𝑥−5)(𝑥+5)}{𝑥+5} & =(2𝑥−2)(𝑥+5)+\frac{5(𝑥+5)}{𝑥+5} \\ \frac{(2𝑥^{2}+8𝑥−5)(𝑥+5)}{𝑥+5} & =(2𝑥−2)(𝑥+5)+\frac{5(𝑥+5)}{𝑥+5} \\ 2𝑥^{2}+8𝑥−5 & =(2𝑥−2)(𝑥+5)+5\end{aligned}


$$

Now, we expand the parentheses on the right-hand side:

$$


\begin{aligned}2𝑥^{2}+8𝑥−5 & =(2𝑥−2)(𝑥+5)+5 \\ 2𝑥^{2}+8𝑥−5 & =2𝑥^{2}+10𝑥−2𝑥−10+5 \\ 2𝑥^{2}+8𝑥−5 & =2𝑥^{2}+8𝑥−5\,✓\end{aligned}


$$

This is a true statement. Therefore, the result is indeed correct.
