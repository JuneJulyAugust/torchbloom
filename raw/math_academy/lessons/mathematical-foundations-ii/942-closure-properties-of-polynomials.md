# Closure Properties of Polynomials

Source: https://www.mathacademy.com/topics/942?courseId=111
Topic ID: 942

## Prerequisites

- [Sets](./45-sets.md)
- [Splitting Rational Expressions Into Separate Terms](../algebra-ii/355-splitting-rational-expressions-into-separate-terms.md)
- [Multiplying Polynomials](../algebra-i/361-multiplying-polynomials.md)
- [The Quotient Rule for Exponents With Algebraic Expressions](../algebra-i/374-the-quotient-rule-for-exponents-with-algebraic-expressions.md)
- [Simplifying Rational Expressions Using Polynomial Factorization](./1676-simplifying-rational-expressions-using-polynomial-factorization.md)
- [Further Factoring of Polynomials Using GCFs](./2337-further-factoring-of-polynomials-using-gcfs.md)

## Lesson

### Introduction

When we add, subtract, or multiply two integers, the answer is always an integer.

To illustrate, let's consider the following two integers:

$$


a = 3, \qquad b=2


$$

- When we *add* the two integers, we get an integer:

- When we *subtract* the two integers, we get an integer:

- When we *multiply* the two integers, we get an integer:

- However, dividing the two integers does *not* give an integer:

We say the integers are **closed** under addition, subtraction, and multiplication but **not closed** under division.

**Watch Out!** Although integers are not closed under division, the ratio of two integers is *sometimes* an integer. For example, if $a=4$ and $b=2,$ then

$$


\dfrac{a}{b} = \dfrac{4}{2} = 2,


$$

which is an integer.

### Closure Properties of Polynomials

Polynomials are also closed under addition, subtraction, and multiplication but not closed under division.

To illustrate, let's consider the following two polynomials:

$$


P(x) = x+1, \qquad Q(x) = x^2


$$

- When we *add* the two polynomials, we get a polynomial:

- When we *subtract* the two polynomials, we get a polynomial:

- When we *multiply* the two polynomials, we get a polynomial:

- However, *dividing* the two polynomials does *not* give a polynomial:

**Watch Out!** Although polynomials are not closed under division, the ratio of two polynomials is *sometimes* a polynomial. For example, if $P=x^2$ and $Q=x,$ then

$$


\dfrac{P}{Q} = \dfrac{x^2}{x} = x,


$$

which is a polynomial.

### Example: Identifying Closure Properties of Polynomials

#### Question

Which of the following expressions are polynomials?

1. $(5x^2-10x^3) \div (5x)$

2. $(1-x^3) \div (x^3)$

3. $(2x^5) \cdot (-x^3-7)$

#### Explanation

Recall that polynomials have the following closure properties:

- Polynomials are closed under addition, subtraction, and multiplication. This means that the sum, difference, and product of two polynomials is ** a polynomial.

- Polynomials are ** closed under division. This means that the quotient of two polynomials is ** always a polynomial.

With that in mind, let's examine our expressions in turn.

- Expression I is a polynomial. Even though polynomials are ** closed under division, the quotient of these two polynomials results in a polynomial:

- Expression II is ** a polynomial. Carrying out the division, we get which is ** a polynomial.

- Expression III is a polynomial. It's a product of two polynomials, and polynomials are closed under multiplication.

Therefore, the correct answer is "I and III only."

### The Degree of a Product of Two Polynomials

Consider the following polynomials:

$$


P(x) = 2x^{\color{blue}4} - 3x + 1, \qquad Q(x) = -6x^{\color{red}3} + 5x^2 + x


$$

Notice that these polynomials have degrees $4$ and $3,$ respectively. We write this as

$$


\textrm{deg}(P) = {\color{blue}4}, \qquad \textrm{deg}(Q) = {\color{red}3}.


$$

Furthermore,

- the leading term in $P(x)$ is $2x^{\color{blue}4},$ and

- the leading term in $Q(x)$ is $-6x^{\color{red}3}$

As a result, the leading term in the product $P \cdot Q$ equals the product of the leading terms of $P$ and $Q\mathbin{:}$

$$


2x^{\color{blue}4} \cdot (-6x^{\color{red}3}) = -12x^{{\color{blue}4}+{\color{red}3}} = -12x^{\color{purple}7}


$$

Therefore, the degree of $P \cdot Q$ must be ${\color{purple}{7}}.$

We have the following general rule:

*The degree of the product of two polynomials equals the sum of the degrees of these polynomials:*

$$


\textrm{deg}(P \cdot Q) = \textrm{deg}(P) + \textrm{deg}(Q)


$$

### Example: Identifying the Degree of a Product of Polynomials

#### Question

If $P(x)$ and $Q(x)$ are polynomials of degree $2$ and $8$, respectively, what is the degree of $P \cdot Q?$

#### Explanation

Since $P$ is a polynomial of degree $2,$ the leading term contains an $x^2.$

Since $Q$ is a polynomial of degree $8,$ the leading term contains an $x^8.$

In $P \cdot Q,$ the $x^2$ term in $P$ multiplies with the $x^8$ term in $Q$ to form a term containing $x^2 \cdot x^8 = x^{2+8} = x^{10}.$

Therefore, the degree of $P \cdot Q$ must be $10.$

### Degrees of Sums and Differences of Polynomials: Case 1

Let's now consider the degree of the sum and difference of two polynomials $P$ and $Q.$

First, let's suppose that $P(x)$ and $Q(x)$ have *different* degrees. In this case, the degree of the sum or difference equals the largest of the two degrees. We write

$$


\textrm{deg}(P \pm Q) = \max \big\{ \textrm{deg}(P), \textrm{deg}(Q) \big\},


$$

where the $\textrm{max}$ function simply returns the largest element of the set.

For example, suppose that $\textrm{deg}(P) = 5$ and $\textrm{deg}(Q) = 2.$ Then,

$$


\textrm{deg}(P + Q) = \max \big\{ 5, 2 \big\} = 5.


$$

To see why this is true, note that the leading term of $P$ contains an $x^5,$ and the leading term of $Q$ has an $x^2.$ When we add the two polynomials, no term of $Q$ could cancel out the leading term of $P.$ So the sum of the polynomials must have degree $5.$

### Degrees of Sums and Differences of Polynomials: Case 2

Now suppose that $P(x)$ and $Q(x)$ have the *same* degree. That is

$$


\textrm{deg}(P) = \textrm{deg}(Q) = n.


$$

In this case, the degree of the sum or difference can be *any integer* from $0$ to $n.$

$$


0 \leq \textrm{deg}(P \pm Q) \leq n


$$

Let's consider some examples:

- Let $P$ and $Q$ be polynomials of degree $15.$ Then, the *largest possible degree* of $P+Q$ is $15$ since the resulting polynomial can't contain terms of order higher than $15.$

- On the other hand, the *smallest possible degree* of $P+Q$ is $0.$ For instance, suppose $P=x^{15}$ and $Q=1-x^{15}.$ Then $P +Q = 1,$ which is a polynomial of degree $0.$

### Example: Identifying Constraints on the Degree of a Polynomial

#### Question

If $P(x)$ and $Q(x)$ are polynomials of degree $3$ and $2$, respectively, what is the degree of $P - Q?$

#### Explanation

Since $P$ is a polynomial of degree $3,$ the leading term contains an $x^3.$

Since $Q$ is a polynomial of degree $2,$ the leading term contains an $x^2.$

In $P-Q,$ the highest-exponent term still contains an $x^3.$ There is no $x^3$ term in $Q$ that could possibly cancel out the $x^3$ term in $P.$

Therefore, the degree of $P-Q$ must be $3.$

### Example: Identifying True Statements About Operations on Polynomials

#### Question

Given that $P(x)$ and $Q(x)$ are polynomials of degree $5$, which of the following statements are true?

1. $P \cdot Q$ is always a polynomial of degree $10$,

2. $P + Q$ is always a polynomial of degree $5$,

3. $\dfrac{P}{Q}$ is sometimes a polynomial.

#### Explanation

Let's look at each statement in turn.

- Statement I is true. The highest-degree terms in $P$ and $Q$ must both contain $x^5.$ Therefore, the highest-degree term in $P \cdot Q$ must contain $x^5 \cdot x^5 = x^{5+5} = x^{10},$ meaning that $P \cdot Q$ has degree $10.$

- Statement II is false. For example, suppose that $P=x^5$ and $Q=-x^5.$ Then $P+Q = x^5+(-x^5)=0,$ which is not a polynomial of degree $5.$

- Statement III is true. For example, suppose that $P=x^5$ and $Q=x^5.$ Then $\dfrac{P}{Q} = \dfrac{x^5}{x^5} = 1,$ which is a polynomial of degree $0.$

In conclusion, only statements I and III are true.
