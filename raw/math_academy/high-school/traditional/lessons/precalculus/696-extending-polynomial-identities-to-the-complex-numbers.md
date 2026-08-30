# Extending Polynomial Identities to the Complex Numbers

Source: https://www.mathacademy.com/topics/696?courseId=43
Topic ID: 696

## Prerequisites

- [Multiplying Complex Numbers](../algebra-ii/33-multiplying-complex-numbers.md)
- [Factoring Higher-Order Polynomials as a Difference of Squares](../algebra-ii/660-factoring-higher-order-polynomials-as-a-difference-of-squares.md)
- [Factoring Biquadratic Expressions](../algebra-ii/2336-factoring-biquadratic-expressions.md)
- [Further Factoring of Polynomials Using GCFs](../algebra-ii/2337-further-factoring-of-polynomials-using-gcfs.md)

## Lesson

### Introduction

We know that a difference of squares can be factored using the difference of squares formula

$$



a^2 - b^2 = (a+b)(a-b).



$$

But how do we factor a *sum* of squares?

As an example, let's consider the quadratic expression $x^2 + 4.$ Notice that we can write it as the sum of squares

$$



x^2 + 2^2.



$$

As it turns out, a sum of squares cannot be factored using real numbers. However, a sum of squares can be factored using complex numbers and the difference of squares formula.

We start by writing $x^2+4$ as a difference:

$$



x^2 + 4 = x^2 - \left(-4\right)



$$

Then, we rewrite the second term as the square of an imaginary number, as follows:

$$



\begin{aligned}𝑥^{2}−(−4) & =𝑥^{2}−(−2^{2}) \\ & =𝑥^{2}−((−1)⋅2^{2}) \\ & =𝑥^{2}−(i^{2}⋅2^{2}) \\ & =𝑥^{2}−(i⋅2)^{2} \\ & =𝑥^{2}−(2i)^{2}\end{aligned}



$$

Finally, we factor the expression as a difference of squares:

$$



\begin{aligned}𝑥^{2}−(2i)^{2}=(𝑥+2i)(𝑥−2i)\end{aligned}



$$

And, we're done! Notice that we can easily check that this is correct by multiplying out the parentheses:

$$



\begin{aligned}(𝑥+2i)(𝑥−2i) & =𝑥^{2}−2i𝑥+2i𝑥−4i^{2} \\ & =𝑥^{2}−4i^{2} \\ & =𝑥^{2}−4(−1) \\ & =𝑥^{2}+4\,✓\end{aligned}



$$

### Example: Factoring a Sum of Squares

#### Question

Factor $m^2 + 16n^2.$

#### Explanation

To factor a sum of squares, we first write it as a difference. Then, we rewrite the second term using $\text{i}^2 = -1.$ Finally, we factor as a difference of squares.

$$



\begin{aligned}𝑚^{2}+16𝑛^{2} & =𝑚^{2}−(−16𝑛^{2}) \\ & =𝑚^{2}−(16\,i^{2}𝑛^{2}) \\ & =𝑚^{2}−(4^{2}i^{2}𝑛^{2}) \\ & =𝑚^{2}−(4i𝑛)^{2} \\ & =(𝑚+4i𝑛)(𝑚−4i𝑛).\end{aligned}



$$

### Example: Factoring a Sum of Higher-Degree Squares

#### Question

Factor $25x^4 + 4 y^8.$

#### Explanation

Notice that the given expression is a sum of squares, since

$$



25x^4 + 4 y^8 = \left( 5x^2\right)^2 + \left(2 y^4\right)^2.



$$

To factor a sum of squares, we first write it as a difference. Then, we rewrite the second term using $\text{i}^2 = -1.$ Finally, we factor as a difference of squares.

$$



\begin{aligned}25𝑥^{4}+4𝑦^{8} & =25𝑥^{4}−(−4𝑦^{8}) \\ & =25𝑥^{4}−(4i^{2}𝑦^{8}) \\ & =(5𝑥^{2})^{2}−(2i𝑦^{4})^{2} \\ & =(5𝑥^{2}+2i𝑦^{4})(5𝑥^{2}−2i𝑦^{4}).\end{aligned}



$$

### Example: Factoring an Expression Containing a Sum of Squares

#### Question

Factor $-z^3-25z.$

#### Explanation

First, let's factor $-z$ from the expression. We have

$$



-z^3-25z =-z(z^2+25).



$$

Let's now focus on factoring the expression $\left(z^2+25\right).$

To factor a sum of squares, we first write it as a difference. Then, we rewrite the second term using $\text{i}^2 = -1.$ Finally, we factor as a difference of squares.

$$



\begin{aligned}𝑧^{2}+25 & =𝑧^{2}−(−25) \\ & =𝑧^{2}−(25i^{2}) \\ & =𝑧^{2}−(5i)^{2} \\ & =(𝑧+5i)(𝑧−5i).\end{aligned}



$$

Finally, substituting this back into our main expression, we get

$$



-z(z^2+25)=-z(z+5\textrm i)(z-5\textrm i).



$$

### Example: Factoring a Perfect Square Quartic Trinomial

#### Question

Factor $x^4+18x^2+81.$

#### Explanation

First, let's factor the expression as a perfect square trinomial in $x^2.$ We have

$$



\begin{aligned}𝑥^{4}+18𝑥^{2}+81 & =(𝑥^{2})^{2}+2⋅9⋅\,(𝑥^{2})+(9)^{2} \\ & =(𝑥^{2}+9)^{2}.\end{aligned}



$$

Now, we need to factor the sum of squares in the parentheses. To do this, we first write it as a difference. Then, we rewrite the second term using $\text{i}^2 = -1.$ Finally, we factor as a difference of squares.

$$



\begin{aligned}𝑥^{2}+9 & =𝑥^{2}−(−9) \\ & =𝑥^{2}−(9i^{2}) \\ & =𝑥^{2}−(3i)^{2} \\ & =(𝑥+3i)(𝑥−3i)\end{aligned}



$$

Finally, substituting this back into our main expression, we get

$$



\begin{aligned}𝑥^{4}+18𝑥^{2}+81 & =(𝑥^{2}+9)^{2} \\ & =((𝑥+3i)(𝑥−3i))^{2} \\ & =(𝑥+3i)^{2}(𝑥−3i)^{2}.\end{aligned}



$$
