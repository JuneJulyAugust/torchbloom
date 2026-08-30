# Solving Polynomial Equations Using the GCF

Source: https://www.mathacademy.com/topics/480?courseId=120
Topic ID: 480

## Prerequisites

- [Solving Quadratic Equations Using a Difference of Squares](../algebra-i/394-solving-quadratic-equations-using-a-difference-of-squares.md)
- [Determining the Roots of Polynomials](../algebra-ii/469-determining-the-roots-of-polynomials.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)
- [Further Factoring of Polynomials Using GCFs](../algebra-ii/2337-further-factoring-of-polynomials-using-gcfs.md)

## Lesson

### Introduction

A **polynomial equation** is an equation that can be written in the form

$$


P_n(x)=0,


$$

where $P_n(x)$ is a polynomial of degree $n.$ A **cubic equation** is a polynomial equation of degree $n=3.$

To solve a polynomial equation with no constant term, we factor the polynomial part using the greatest common factor. Once we've done that, we can apply the zero product rule to the resulting factors.

For instance, consider the cubic equation $x^3-x=0.$

First, notice that all of the terms of the polynomial have a common factor of $x.$ We can factor out the $x$ as follows:

$$


\begin{aligned}𝑥^{3}−𝑥 & =0 \\ 𝑥(𝑥^{2}−1) & =0\end{aligned}


$$

Now, we factor the expression $x^2-1$ using the difference of squares formula:

$$


\begin{aligned}𝑥(𝑥^{2}−1) & =0 \\ 𝑥(𝑥+1)(𝑥−1) & =0\end{aligned}


$$

Finally, by applying the zero product rule, we conclude that the solutions are ${\color{red}x=0},$ ${\color{blue}x = -1},$ and ${\color{purple}x=1}.$

### Example: Solving a Cubic Equation With No Constant Term

#### Question

Solve the equation $2x^3 - 6x^2 + 4x= 0.$

#### Explanation

First, notice that all of the terms of the polynomial have a common factor of $2x.$ We can factor out the $2x$ as follows:

$$


\begin{aligned}2𝑥^{3}−6𝑥^{2}+4𝑥 & =0 \\ 2𝑥(𝑥^{2}−3𝑥+2) & =0\end{aligned}


$$

Now, we factor the expression $x^2-3x+2$ as follows:

$$


\begin{aligned}2𝑥(𝑥^{2}−3𝑥+2) & =0 \\ 2𝑥(𝑥−1)(𝑥−2) & =0\end{aligned}


$$

Finally, by applying the zero product rule, the solutions are $x = 0,$ $x = 1,$ and $x = 2.$

### Example: Solving a Cubic Equation by Rearranging

#### Question

Solve for $x$ where $x^3 - x^2 - x = 3x^2 + 4x.$

#### Explanation

First, let's rewrite the polynomial equation in the form $P_n(x)=0.$ To do this, we subtract all the terms from the right-hand side so that the right-hand side becomes $0\mathbin{:}$

$$


\begin{aligned}𝑥^{3}−𝑥^{2}−𝑥 & =3𝑥^{2}+4𝑥 \\ 𝑥^{3}−4𝑥^{2}−𝑥 & =4𝑥 \\ 𝑥^{3}−4𝑥^{2}−5𝑥 & =0\end{aligned}


$$

Next, notice that all of the terms of the polynomial have a common factor of $x.$ We can factor out the $x$ as follows:

$$


\begin{aligned}𝑥^{3}−4𝑥^{2}−5𝑥 & =0 \\ 𝑥(𝑥^{2}−4𝑥−5) & =0\end{aligned}


$$

Now, we factor the expression $x^2 - 4x - 5$ as follows:

$$


\begin{aligned}𝑥(𝑥^{2}−4𝑥−5) & =0 \\ 𝑥(𝑥+1)(𝑥−5) & =0\end{aligned}


$$

Finally, by applying the zero product rule, the solutions are $x = 0,$ $x = -1,$ and $x = 5.$

### Example: Solving a Higher-Order Polynomial Equation With No Constant Term

#### Question

If $3x^5 + x^3 = 3x^3 - 5x^4,$ then what are the values of $x?$

#### Explanation

First, let's rewrite the polynomial equation in the form $P_n(x)=0\mathbin{:}$

$$


\begin{aligned}3𝑥^{5}+𝑥^{3} & =3𝑥^{3}−5𝑥^{4} \\ 3𝑥^{5}+5𝑥^{4}+𝑥^{3} & =3𝑥^{3} \\ 3𝑥^{5}+5𝑥^{4}−2𝑥^{3} & =0\end{aligned}


$$

Next, notice that all of the terms of the polynomial have a common factor of $x^3.$ We can factor out the $x^3$ as follows:

$$


\begin{aligned}3𝑥^{5}+5𝑥^{4}−2𝑥^{3} & =0 \\ 𝑥^{3}(3𝑥^{2}+5𝑥−2) & =0\end{aligned}


$$

Now, we factor the expression $3x^2+5x-2$ as follows:

$$


\begin{aligned}𝑥^{3}(3𝑥^{2}+5𝑥−2) & =0 \\ 𝑥^{3}(3𝑥−1)(𝑥+2) & =0\end{aligned}


$$

Finally, by applying the zero product rule, the solutions are $x = 0,$ $x = \dfrac{1}{3},$ and $x = -2.$
