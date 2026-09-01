# Factoring Sums and Differences of Cubes

Source: https://www.mathacademy.com/topics/441?courseId=134
Topic ID: 441

## Prerequisites

- [Factoring Differences of Squares](../../../traditional/lessons/algebra-i/370-factoring-differences-of-squares.md)
- [The Cube Root of a Perfect Cube With Algebraic Expressions](../../../traditional/lessons/algebra-i/381-the-cube-root-of-a-perfect-cube-with-algebraic-expressions.md)

## Lesson

### Introduction

A polynomial of the form $a^3 + b^3$ is called a **sum of cubes**, while a polynomial of the form $a^3 – b^3$ is called a **difference of cubes**.

Both of these polynomials follow a similar factor pattern:

$$


\begin{aligned}𝑎^{3}+𝑏^{3} & =(𝑎+𝑏)(𝑎^{2}−𝑎𝑏+𝑏^{2}) \\ 𝑎^{3}−𝑏^{3} & =(𝑎−𝑏)(𝑎^{2}+𝑎𝑏+𝑏^{2})\end{aligned}


$$

One trick to memorizing the signs in these patterns is to use the mnemonic **SOAP**, which stands for **S**ame, **O**pposite, **A**lways **P**ositive.

- The sign of the linear factor is the **S**ame as that of the original polynomial,

- the first sign of the quadratic factor is the **O**pposite sign, and

- the last sign of the quadratic factor is **A**lways **P**ositive.

### Example: Factoring a Difference of Cubes

#### Question

Factor $x^3 - 8.$

#### Explanation

The difference of cubes formula is given by

$$


a^3-b^3=(a-b)(a^2+ab+b^2).


$$

Notice that we can write the given expression as a difference of cubes:

$$


x^3 - 8 = x^3 - 2^3


$$

Now, we factor the given expression using the difference of cubes formula:

$$


\begin{aligned} x^3 - 8 & = x^3 - 2^3\\[3pt] & = (x - 2)\left(x^2 + 2\cdot x + 2^2\right)\\[3pt] & = (x - 2)\left(x^2 + 2x + 4\right) \end{aligned}


$$

### Example: Factoring a Sum of Cubes

#### Question

Factor $8n^3 + m^6.$

#### Explanation

The sum of cubes formula is given by

$$


a^3+b^3=(a+b)(a^2-ab+b^2).


$$

Notice that we can write our expression as a sum of cubes, as follows:

$$


8n^3 + m^6 = (2n)^3 + (m^2)^3


$$

Now, we factor our expression using the sum of cubes formula:

$$


\begin{aligned}8𝑛^{3}+𝑚^{6} & =(2𝑛)^{3}+(𝑚^{2})^{3} \\ & =(2𝑛+𝑚^{2})((2𝑛)^{2}−2𝑛⋅𝑚^{2}+(𝑚^{2})^{2}) \\ & =(2𝑛+𝑚^{2})(4𝑛^{2}−2𝑚^{2}𝑛+𝑚^{4})\end{aligned}


$$

### Example: Factoring Sums and Differences of Cubes with Fractional Terms

#### Question

Factor $1 - \dfrac 1 {t^9}.$

#### Explanation

The difference of cubes formula is given by

$$


a^3-b^3=(a-b)(a^2+ab+b^2).


$$

Notice that our expression can be written as a difference of cubes, as follows:

$$


1 - \dfrac{1}{t^9} = 1^3 - \left( \dfrac{1}{t^3}\right)^3


$$

Now, we factor our expression using the difference of cubes formula:

$$


\begin{aligned}1−\frac{1}{𝑡^{9}} & =1^{3}−(\frac{1}{𝑡^{3}})^{3} \\ & =(1−\frac{1}{𝑡^{3}})(1^{2}+1⋅\frac{1}{𝑡^{3}}+(\frac{1}{𝑡^{3}})^{2}) \\ & =(1−\frac{1}{𝑡^{3}})(1+\frac{1}{𝑡^{3}}+\frac{1}{(𝑡^{3})^{2}}) \\ & =(1−\frac{1}{𝑡^{3}})(1+\frac{1}{𝑡^{3}}+\frac{1}{𝑡^{6}})\end{aligned}


$$

### Verifying the Sum of Cubes Formula

To verify the identity

$$


a^3 + b^3 = (a + b)(a^2 - ab + b^2)


$$

we begin by expanding the right-hand side:

$$


(a + b)(a^2 - ab + b^2) = a(a^2 - ab + b^2) + b(a^2 - ab + b^2)


$$

Now, we apply the distributive law to each term:

- For the first term, we have

- For the second term, we have

Adding both expressions gives

$$


\begin{aligned}(𝑎+𝑏)(𝑎^{2}−𝑎𝑏+𝑏^{2}) & =𝑎^{3}−𝑎^{2}𝑏+𝑎𝑏^{2}+𝑎^{2}𝑏−𝑎𝑏^{2}+𝑏^{3} \\ & =𝑎^{3}−𝑎^{2}𝑏+𝑎𝑏^{2}+𝑎^{2}𝑏−𝑎𝑏^{2}+𝑏^{3} \\ & =𝑎^{3}+𝑎𝑏^{2}−𝑎𝑏^{2}+𝑏^{3} \\ & =𝑎^{3}+𝑎𝑏^{2}−𝑎𝑏^{2}+𝑏^{3} \\ & =𝑎^{3}+𝑏^{3}\end{aligned}


$$

as required.

We can verify the formula for the difference in cubes, i.e.

$$


a^3 - b^3 = (a - b)(a^2 + ab + b^2)


$$

in a similar way.
