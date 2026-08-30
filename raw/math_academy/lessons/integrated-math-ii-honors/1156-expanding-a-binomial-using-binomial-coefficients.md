# Expanding a Binomial Using Binomial Coefficients

Source: https://www.mathacademy.com/topics/1156?courseId=128
Topic ID: 1156

## Prerequisites

- [Pascal's Triangle and the Binomial Coefficients](./3404-pascal-s-triangle-and-the-binomial-coefficients.md)

## Lesson

### Introduction

The **binomial theorem** states that for any real numbers $a$ and $b$ and any positive integer $n,$

$$


{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \cdots + {n \choose n}{a^0}{b^n},


$$

where we recall that

$$


{n \choose k} = \dfrac{n!}{k!\, (n-k)! }.


$$

Let's use the binomial theorem to find the first few terms in the expansion of

$$


(2+x)^6.


$$

In this case, we have $a = 2,$ $b= x,$ and $n=6.$ Therefore, the first three terms of our expansion are given by

$$


{\left( {2 + x} \right)^{6}} = {6\choose0} {\left( 2 \right)^{6}}{\left( x \right)^0} + {6\choose1} {\left( 2 \right)^{6 - 1}}{\left( x \right)^1} + {6\choose2} {\left( 2 \right)^{6 - 2}}{\left( x \right)^2} + \cdots.


$$

Using a calculator, we find that

$$


{6\choose0} = {\color{blue}{1}}, \qquad {6\choose1} = {\color{blue}{6}}, \qquad {6\choose2} = {\color{blue}{15}}.


$$

Therefore, our expansion can be simplified as follows:

$$


\begin{aligned}(2+𝑥)^{6} & =(\frac{6}{0})(2)^{6}(𝑥)^{0}+(\frac{6}{1})(2)^{6−1}(𝑥)^{1}+(\frac{6}{2})(2)^{6−2}(𝑥)^{2}+⋯ \\ & =(1)(2^{6})(1)+(6)(2^{5})(𝑥)+(15)(2^{4})(𝑥^{2})+⋯ \\ & =(1)(64)(1)+(6)(32)(𝑥)+(15)(16)(𝑥^{2})+⋯ \\ & =64+192\,𝑥+240\,𝑥^{2}+⋯\end{aligned}


$$

### Example: Finding the First Few Terms of a Binomial Expansion

#### Question

Expand ${(3x + y)}^3$ using the binomial theorem.

#### Explanation

The binomial theorem states that for any positive integer $n,$ we have

$$


{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \cdots + {n \choose n}{a^0}{b^n}.


$$

In the case of ${(3x +y)}^3,$ we have $a=3x,$ $b=y,$ and $n=3.$

Therefore, we can expand ${(3x + y)}^3$ as follows:

$$


\begin{aligned}(3𝑥+𝑦)^{3} & =(\frac{3}{0})(3𝑥)^{3}(𝑦)^{0}+(\frac{3}{1})(3𝑥)^{3−1}(𝑦)^{1}+(\frac{3}{2})(3𝑥)^{3−2}(𝑦)^{2}+(\frac{3}{3})(3𝑥)^{3−3}(𝑦)^{3} \\ & =(\frac{3}{0})(3𝑥)^{3}(1)+(\frac{3}{1})(3𝑥)^{2}(𝑦)^{1}+(\frac{3}{2})(3𝑥)^{1}(𝑦)^{2}+(\frac{3}{3})(3𝑥)^{0}(𝑦)^{3} \\ & =1⋅(3𝑥)^{3}+3⋅(3𝑥)^{2}(𝑦)+3⋅(3𝑥)(𝑦)^{2}+1⋅1⋅(𝑦^{3}) \\ & =27𝑥^{3}+27𝑥^{2}𝑦+9𝑥𝑦^{2}+𝑦^{3}\end{aligned}


$$

### Example: Finding the First Few Terms of an Expansion With Negative Coefficients

#### Question

Find the first three terms of the binomial expansion of ${(x - 3y)}^ 5.$

#### Explanation

The binomial theorem states that for any positive integer $n,$ we have

$$


{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \cdots + {n \choose n}{a^0}{b^n}.


$$

In the case of ${(x - 3y)}^ 5,$ we have $a=x,$ $b=-3y,$ and $n=5.$

Therefore, the first three terms of ${(x - 3y)}^ 5$ are as follows:

$$


\begin{aligned}(𝑥−3𝑦)^{5} & =(\frac{5}{0})(𝑥)^{5}(−3𝑦)^{0}+(\frac{5}{1})(𝑥)^{5−1}(−3𝑦)^{1}+(\frac{5}{2})(𝑥)^{5−2}(−3𝑦)^{2}+⋯ \\ & =1(𝑥)^{5}+5(𝑥)^{4}(−3𝑦)+10(𝑥)^{3}(9𝑦^{2})+⋯ \\ & =𝑥^{5}−15𝑥^{4}𝑦+90𝑥^{3}𝑦^{2}+⋯\end{aligned}


$$

### Example: Finding the Coefficient of a Particular Term

#### Question

Find the coefficient of $x^{4}$ in the expansion of ${\left({3 + x} \right)^{7}}.$

#### Explanation

The binomial theorem states that for any positive integer $n,$ we have

$$


{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \cdots + {n \choose n}{a^0}{b^n}.


$$

In the case of ${\left({3 +x} \right)^{7}},$ we have $a=3,$ $b=x,$ and $n=7.$ Therefore,

$$


\begin{aligned}(3+𝑥)^{7}=(\frac{7}{0})3^{7}𝑥^{0}+(\frac{7}{1})3^{7−1}𝑥^{1}+(\frac{7}{2})3^{7−2}𝑥^{2}+⋯+(\frac{7}{7})3^{7−7}𝑥^{7}.\end{aligned}


$$

From here, we see that the $x^4$ term must be

$$


{7 \choose 4}{3^{7 - 4}}{x^4}.


$$

Evaluating the coefficient, we get

$$


\begin{aligned}(\frac{7}{4})3^{7−4} & =35⋅3^{3} \\ & =35⋅27 \\ & =945.\end{aligned}


$$

Therefore, the coefficient of $x^{4}$ is $945.$
