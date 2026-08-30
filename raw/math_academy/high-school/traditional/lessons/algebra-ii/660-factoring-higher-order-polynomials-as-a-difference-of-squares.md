# Factoring Higher-Order Polynomials as a Difference of Squares

Source: https://www.mathacademy.com/topics/660?courseId=51
Topic ID: 660

## Prerequisites

- [Factoring Differences of Squares](../algebra-i/370-factoring-differences-of-squares.md)

## Lesson

### Introduction

We know how to factor a difference of squares, like $x^2-4,$ but how do we factor an expression like $x^4-16?$

It turns out, we can use the exact same method!

First, let's rewrite the quartics as perfect squares:

$$



\begin{aligned}𝑥^{4}−16 & =(𝑥^{2})^{2}−(4)^{2}\end{aligned}



$$

Now, our expression resembles a difference of squares, which can be factored as follows:

$$



a^2 - b^2 = (a+b)(a-b)



$$

Using $a=x^2$ and $b=4$ in the above formula, we can factor our expression as follows:

$$



x^4 - 16 = (x^2 + 4) (x^2 -4)



$$

We can check that it is correct by doing the multiplication:

$$



\begin{aligned}(𝑥^{2}+4)(𝑥^{2}−4) & =𝑥^{4}−4𝑥^{2}+4𝑥^{2}−4^{2} \\ & =𝑥^{4}−4^{2} \\ & =𝑥^{4}−16\,✓\end{aligned}



$$

Note that we can factor the expression further since it contains another difference of squares, $x^2-4=(x)^2-(2)^2.$ Factoring this difference of squares as well, we get the following final result:

$$



\begin{aligned}𝑥^{4}−16 & =(𝑥^{2}+4)(𝑥^{2}−4) \\ & =(𝑥^{2}+4)(𝑥+2)(𝑥−2)\end{aligned}



$$

### Example: Factoring a Polynomial as a Difference of Squares

#### Question

Factor the expression $y^4 - 81.$

#### Explanation

The difference of squares formula is given by

$$



a^2 - b^2 = (a+b)(a-b).



$$

Notice that our expression can be written as a difference of squares:

$$



y^4 - 81 = \left(y^2\right)^2 - 9^2



$$

Now, we factor our expression using the difference of squares formula:

$$



\left(y^2\right)^2 - 9^2 = (y^2 + 9)(y^2 - 9)



$$

Finally, we notice that the expression in the second set of parentheses is also a difference of squares. Therefore, the expression can be factored further, as follows:

$$



\begin{aligned}(𝑦^{2}+9)(𝑦^{2}−9) & =(𝑦^{2}+9)(𝑦^{2}−3^{2}) \\ & =(𝑦^{2}+9)(𝑦+3)(𝑦−3)\end{aligned}



$$

### Example: Factoring a Polynomial With Leading Coefficients as a Difference of Squares

#### Question

Factor the expression $2m^4-32.$

#### Explanation

The difference of squares formula is given by

$$



a^2 - b^2 = (a+b)(a-b).



$$

Notice that all of the terms have a common factor of $2.$ To simplify the computation, we can factor out the $2,$ as follows:

$$



2m^4 - 32 = 2(m^4 - 16)



$$

The expression in parentheses can be written as a difference of squares:

$$



2(m^4 - 16) = 2\left(\left(m^2\right)^2 -4^2\right)



$$

Now, we factor our expression using the difference of squares formula:

$$



2\left(\left(m^2\right)^2 -4^2\right) = 2(m^2+4)(m^2-4)



$$

Finally, we notice that the expression $m^2-4$ in the second set of parentheses is also a difference of squares. Therefore, the expression can be factored further, as follows:

$$



\begin{aligned}2(𝑚^{2}+4)(𝑚^{2}−4) & =2(𝑚^{2}+4)(𝑚^{2}−2^{2}) \\ & =2(𝑚^{2}+4)(𝑚+2)(𝑚−2)\end{aligned}



$$

### Example: Factoring a Polynomial With Multiple Variables as a Difference of Squares

#### Question

Factor the expression $16x^4 - y^4.$

#### Explanation

The difference of squares formula is given by

$$



a^2 - b^2 = (a+b)(a-b)



$$

Notice that our expression can be written as a difference of squares:

$$



16x^4 - y^4 = \left(4x^2\right)^2 -\left(y^2\right)^2



$$

Now, we factor our expression using the difference of squares formula:

$$



\left(4x^2\right)^2 - \left(y^2\right)^2 = (4x^2+y^2)(4x^2 - y^2)



$$

Finally, we notice that the expression $4x^2-y^2$ in the second set of parentheses is also a difference of squares. Therefore, the expression can be factored further, as follows:

$$



\begin{aligned}(4𝑥^{2}+𝑦^{2})(4𝑥^{2}−𝑦^{2}) & =(4𝑥^{2}+𝑦^{2})((2𝑥)^{2}−𝑦^{2}) \\ & =(4𝑥^{2}+𝑦^{2})(2𝑥+𝑦)(2𝑥−𝑦)\end{aligned}



$$
