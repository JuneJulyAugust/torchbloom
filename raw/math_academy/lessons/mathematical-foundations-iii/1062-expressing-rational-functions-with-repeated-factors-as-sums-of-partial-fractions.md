# Expressing Rational Functions with Repeated Factors as Sums of Partial Fractions

Source: https://www.mathacademy.com/topics/1062?courseId=136
Topic ID: 1062

## Prerequisites

- [Solving Systems of Equations by Substitution](../grade-7/487-solving-systems-of-equations-by-substitution.md)
- [Expressing Rational Functions as Sums of Partial Fractions](./1060-expressing-rational-functions-as-sums-of-partial-fractions.md)

## Lesson

### Introduction

When a rational expression has a repeated factor in the denominator, the repeated factor generates additional terms in the partial fractions expansion.

For example, consider the rational expression $\dfrac{4x-1}{(x+2)^2(x-1)}.$ For this rational expression, the **repeated factor** $(x+2)^2$ generates *two* partial fractions, and the partial fraction expansion takes the following form:

$$


\begin{aligned}\frac{4𝑥−1}{(𝑥+2)^{2}(𝑥−1)} & =\frac{𝐴}{(𝑥+2)}+\frac{𝐵}{(𝑥+2)^{2}}+\frac{𝐶}{(𝑥−1)}\end{aligned}


$$

We can find the values of $A,$ $B,$ and $C$ using the same process as usual. To start, we multiply both sides by $(x+2)^2(x-1)$ and get

$$


4x-1= A(x+2)(x-1) +B(x-1) + C(x+2)^2.


$$

Plugging in $x=1$ gets rid of the $A$ and $B$ terms and allows us to solve for $C\mathbin{:}$

$$


\begin{aligned}4(1)−1=𝐶⋅(3)^{2}\,⟹\,𝐶=\frac{1}{3}\end{aligned}


$$

On the other hand, plugging in $x=-2$ gets rid of the $A$ and $C$ terms and allows us to solve for $B\mathbin{:}$

$$


\begin{aligned}4(−2)−1=𝐵(−2−1)\,⟹\,𝐵=3\end{aligned}


$$

We still need to solve for $A.$ To do this, we can substitute our results for $B$ and $C$ and also plug in any value of $x$ that we haven't already used. To keep things simple, let's plug in $x=0.$ Doing this, we get

$$


\begin{aligned}4(0)−1 & =𝐴⋅(0+2)(0−1)+3(0−1)+\frac{1}{3}⋅(0+2)^{2} \\ −1 & =−2𝐴−3+\frac{4}{3} \\ −1 & =−2𝐴−\frac{5}{3} \\ \frac{2}{3} & =−2𝐴 \\ 𝐴 & =−\frac{1}{3}.\end{aligned}


$$

Knowing that $A=-\dfrac{1}{3},$ $B=3,$ and $C = \dfrac{1}{3},$ we have

$$


\begin{aligned}\frac{4𝑥−1}{(𝑥+2)^{2}(𝑥−1)} & =\frac{(−\frac{1}{3})}{3}+\frac{3}{(𝑥+2)^{2}}+\frac{(\frac{1}{3})}{3} \\ & =−\frac{1}{3(𝑥+2)}+\frac{3}{(𝑥+2)^{2}}+\frac{1}{3(𝑥−1)}.\end{aligned}


$$

### Example: Calculating a Missing Coefficient

#### Question

Given that

$$


\dfrac{7x+6}{(x+2)^2} = \dfrac{A}{x+2} -\dfrac{8}{(x+2)^2},


$$

what is the value of $A?$

#### Explanation

Multiplying both sides of the given equality by $(x+2)^2$ gives

$$


\begin{aligned}7𝑥+6 & =𝐴(𝑥+2)−8.\end{aligned}


$$

Now, we can substitute some value for $x$ and solve for $A.$

We ** choose $x=-2,$ since this would eliminate $A$ from the equation. But we can choose any other value of $x.$ So let’s choose a simple value, say, $x=0.$

Plugging $x=0$ into the equation, we get

$$


\begin{aligned}7𝑥+6 & =𝐴(𝑥+2)−8 \\ 7(0)+6 & =𝐴(0+2)−8 \\ 6 & =2𝐴−8 \\ 14 & =2𝐴 \\ 𝐴 & =7.\end{aligned}


$$

### Example: Calculating a Two-Term Partial Fraction Decomposition

#### Question

Given that

$$


\dfrac{7-4x}{(x+5)^2} = \dfrac{A}{x+5} +\dfrac{B}{(x+5)^2},


$$

find the values of $A$ and $B.$

#### Explanation

Multiplying both sides of the given equality by $(x+5)^2$ gives

$$


\begin{aligned}7−4𝑥 & =𝐴(𝑥+5)+𝐵.\end{aligned}


$$

We want to solve for $A$ and $B,$ and both of these constants appear in the equation simultaneously. However, we can eliminate $A$ if we substitute $x=-5.$

Plugging $x=-5$ into the equation, we get

$$


\begin{aligned}7−4𝑥 & =𝐴(𝑥+5)+𝐵 \\ 7−4(−5) & =𝐴(−5+5)+𝐵 \\ 27 & =𝐴(0)+𝐵 \\ 27 & =0+𝐵 \\ 27 & =𝐵.\end{aligned}


$$

Now, we need to solve for $A.$ To do this, let’s start by substituting our value $B=27$ into the equation:

$$


\begin{aligned}7−4𝑥 & =𝐴(𝑥+5)+27\end{aligned}


$$

We can substitute some value for $x$ and solve for $A.$

We ** choose $x=-5,$ since this would eliminate $A$ from the equation. But we can choose any other value of $x.$ So let’s choose a simple value, say, $x=0.$

Plugging $x=0$ into the equation, we get

$$


\begin{aligned}7−4𝑥 & =𝐴(𝑥+5)+27 \\ 7−4(0) & =𝐴(0+5)+27 \\ 7 & =5𝐴+27 \\ −20 & =5𝐴 \\ 𝐴 & =−4.\end{aligned}


$$

Therefore, $A=-4$ and $B=27.$

### Example: Calculating a Three-Term Partial Fraction Decomposition

#### Question

Given that

$$


\dfrac{3x^2-5x+8}{(x-3)^2(x+1)} = \dfrac{A}{(x-3)} +\dfrac{B}{(x-3)^2} + \dfrac{C}{(x+1)},


$$

where $A$, $B$, and $C$ are real constants, calculate $A\cdot B\cdot C.$

#### Explanation

First, we multiply the expression through by $(x-3)^2(x+1)$ to give

$$


3x^2-5x+8= A(x-3)(x+1)+B(x+1)+C(x-3)^2.


$$

Plugging in $x=3$ eliminates the $A$ and $C$ terms and allows us to solve for $B.$ We get

$$


\begin{aligned}3(3)^{2}−5(3)+8=𝐵⋅4\,⟹\,𝐵=5.\end{aligned}


$$

On the other hand, plugging in $x=-1$ eliminates the $A$ and $B$ terms and allows us to solve for $C.$ We get

$$


\begin{aligned}3(−1)^{2}−5(−1)+8=𝐶⋅(−4)^{2}\,⟹\,𝐶=1.\end{aligned}


$$

Unfortunately, there is no value of $x$ that we can substitute to eliminate both $B$ and $C.$ However, using our results for $B$ and $C$ gives

$$


3x^2-5x+8= A(x-3)(x+1)+5(x+1)+1(x-3)^2,


$$

and we can plug in any value of $x$ to solve for $A.$ Let's choose the simplest number to plug in, $x=0.$ We get

$$


\begin{aligned}8 & =𝐴(0−3)(0+1)+5(0+1)+𝐶(0−3)^{2} \\ 8 & =−3𝐴+5+9 \\ −6 & =−3𝐴 \\ 𝐴 & =2.\end{aligned}


$$

Therefore,

$$


A\cdot B\cdot C=2\cdot 5\cdot 1=10,


$$

and the partial fraction decomposition is

$$


\dfrac{3x^2-5x+8}{(x-3)^2(x+1)} = \dfrac{2}{(x-3)} +\dfrac{5}{(x-3)^2} + \dfrac{1}{(x+1)}.


$$

### Cubic and Higher Order Repeated Factors

If we have an algebraic fraction with higher-order repeated factors, such as

$$


\dfrac{1-2x}{(x+1)(x+2)^3},


$$

we can express this as a sum of partial fractions in a similar way to before:

$$


\dfrac{1-2x}{(x+1)(x+2)^3}= \dfrac{A}{x+1}+\dfrac{B}{x+2} +\dfrac{C}{(x+2)^2} + \dfrac{D}{(x+2)^3}.


$$

So the factor $(x+2)^3$ gives three partial fractions. We can find $A,$ $B,$ $C,$ and $D$ using the same method as before.

### Example: Finding a Partial Fraction Decomposition With Higher Order Factors

#### Question

Given that

$$


\dfrac{1-2x}{(x+1)(x+2)^3}= \dfrac{A}{x+1}+\dfrac{B}{x+2} +\dfrac{C}{(x+2)^2} + \dfrac{D}{(x+2)^3},


$$

where $A$, $B$, $C$ and $D$ are real constants, determine the value of $AB + CD.$

#### Explanation

Multiplying both sides of the given equality by $(x+1)(x+2)^3$ gives

$$


1 - 2x = A(x+2)^3 + B(x+1)(x+2)^2 + C(x+1)(x+2) + D(x+1).


$$

Letting $x = -2$ gives

$$


\begin{aligned}1−2(−2) & =𝐴(−2+2)^{3}+𝐵(−2+1)(−2+2)^{2}+𝐶(−2+1)(−2+2)+𝐷(−2+1) \\ 1+4 & =−𝐷 \\ 𝐷 & =−5.\end{aligned}


$$

Letting $x = -1$ gives

$$


\begin{aligned}1−2(−1) & =𝐴(−1+2)^{3}+𝐵(−1+1)(−1+2)^{2}+𝐶(−1+1)(−1+2)+𝐷(−1+1) \\ 1+2 & =𝐴 \\ 𝐴 & =3.\end{aligned}


$$

Letting $x = 0$ and using our values for $A$ and $D$ gives

$$


\begin{aligned}1−2(0) & =3(0+2)^{3}+𝐵(0+1)(0+2)^{2}+𝐶(0+1)(0+2)+(−5)(0+1) \\ 1−0 & =24+4𝐵+2𝐶−5 \\ 2𝐶 & =−4𝐵−18 \\ 𝐶 & =−2𝐵−9.\,\,(1)\end{aligned}


$$

Now, letting $x = 1$ and using our values for $A$ and $D$ gives

$$


\begin{aligned}1−2(1) & =𝐴(1+2)^{3}+𝐵(1+1)(1+2)^{2}+𝐶(1+1)(1+2)+𝐷(1+1) \\ 1−2 & =81+18𝐵+6𝐶−10 \\ 6𝐶 & =−18𝐵−72 \\ 𝐶 & =−3𝐵−12.\,\,(2)\end{aligned}


$$

From $(1)$ and $(2)$ we have

$$


\begin{aligned}−2𝐵−9 & =−3𝐵−12 \\ 𝐵 & =−3.\end{aligned}


$$

Now we substitute the value of $B$ into $(1)$ to get the value of $C{:}$

$$


C = -2(-3) - 9 = -3


$$

Finally,

$$


AB + CD = 3(-3) + (-3)(-5) = 6.


$$
