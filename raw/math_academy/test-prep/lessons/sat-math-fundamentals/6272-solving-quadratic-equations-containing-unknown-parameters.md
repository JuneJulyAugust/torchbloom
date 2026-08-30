# Solving Quadratic Equations Containing Unknown Parameters

Source: https://www.mathacademy.com/topics/6272?courseId=120
Topic ID: 6272

## Prerequisites

- [Solving Two-Variable Equations](../../../middle-school/lessons/grade-7/356-solving-two-variable-equations.md)
- [The Zero Product Rule for Solving Quadratic Equations](../../../high-school/traditional/lessons/algebra-i/1424-the-zero-product-rule-for-solving-quadratic-equations.md)
- [Factoring Expressions Containing Hidden Factors](./6172-factoring-expressions-containing-hidden-factors.md)

## Lesson

### Introduction

In this lesson, we will learn how to identify solutions from a factored quadratic equation containing unknown parameters. For this, we'll typically use the zero product property.

Recall that the zero product rule says if we have the equation

$$


A \cdot B = 0,


$$

then either

$$


A = 0 \quad \text{or} \quad B = 0.


$$

We use this rule when equations are written in factored form. It allows us to break a single product equation into simpler linear equations, which we can then solve directly.

Suppose we want to find the solution to the equation

$$


(x-8)(x+n-6) = 0


$$

where $n$ is a constant.

Our equation is already factored with zero on the right-hand side. According to the zero product property, a product equals zero only if one of its factors equals zero. So we set each factor equal to zero.

Setting the first factor to zero, we have

$$


x - 8 = 0 \quad \Rightarrow \quad x = 8.


$$

Setting the second factor to zero and solving for $x,$ we have

$$


\begin{aligned}𝑥+𝑛−6 & =0 \\ 𝑥+𝑛−6−𝑛+6 & =0−𝑛+6 \\ 𝑥 & =0−𝑛+6 \\ 𝑥 & =6−𝑛.\end{aligned}


$$

Therefore, the solutions are $x = 8$ or $x = 6 - n$. Notice that the second solution is written in terms of the parameter $n.$

### Example: Solving a Factored Quadratic Equation With Unknown Parameters

#### Question

Which of the following **** be a solution to the equation

$$


(x-5)(x-k+4) = 0


$$

if $k > 2$ is a constant?

1. $x=5$

2. $x=3$

3. $x=-5$

#### Explanation

We are given the factored equation

$$


(x-5)(x-k+4) = 0.


$$

According to the zero product property, a product equals zero only if one of its factors equals zero. So we set each factor equal to zero. This gives

$$


x - 5 = 0 \quad \Rightarrow\quad x = 5


$$

or

$$


x - k + 4 = 0 \quad \Rightarrow\quad x = k - 4.


$$

Therefore, the potential solutions are $x = 5$ or $x = k - 4.$

With that in mind, let's examine each option.

- Option I: $x = 5$ is indeed a solution.$\:{\color{green}{\checkmark}}$

- Option II: $x = 3$ would require $k - 4 = 3$, which gives $k = 7.$ Since $k > 2$, this is possible, so $3$ can be a solution.$\:{\color{green}{\checkmark}}$

- Option III: $x = -5$ would require $k - 4 = -5$, which gives $k = -1.$ But this contradicts the condition $k > 2.$ So $-5$ is not a solution.$\:{\color{red}{\times}}$

Therefore, the correct answer is "I and II only."

### Factoring Before Applying the Zero Product Rule

If a quadratic equation is *not* given in factored form, we must rewrite it in standard form and then factor it.

For example, suppose we want to find the solutions to

$$


(x - m + 7)(x - 9) - 1(x - 9) = 0


$$

where $m$ is a constant.

First, notice that both terms on the left-hand side contain a factor of ${\color{blue}{(x-9)}}.$

$$


(x - m + 7){\color{blue}{(x-9)}} - {\color{blue}{(x-9)}} = 0.


$$

Therefore, to solve this equation, we first factor out ${\color{blue}{(x-9)}},$ as follows:

$$


\begin{aligned}(𝑥−𝑚+7)(𝑥−9)−(𝑥−9) & =0 \\ (𝑥−𝑚+7)(𝑥−9)\,−\,1⋅(𝑥−9) & =0 \\ (𝑥−9)[(𝑥−𝑚+7)\,−\,1] & =0 \\ (𝑥−9)(𝑥−𝑚+6) & =0\end{aligned}


$$

According to the zero product property, a product equals zero only if one of its factors equals zero. So we set each factor equal to zero. This gives

$$


x - 9 = 0 \quad \Rightarrow\quad x = 9


$$

or

$$


x - m + 6 = 0 \quad \Rightarrow\quad x = m - 6.


$$

Let's see some more examples.

### Example: Factoring and Solving a Quadratic Equation With Unknown Parameters

#### Question

Which of the following **** be a solution to the equation

$$


(x - p + 3)(x - 15) - 6(x - 15) = 0


$$

where $p$ is a constant.

1. $x = 15$

2. $x = p+4$

3. $x = p+3$

4. $x = p+6$

#### Explanation

We are given the equation

$$


(x - p + 3)(x - 15) - 6(x - 15) = 0.


$$

To solve this equation, we first factor out $(x - 15),$ as follows:

$$


(x - 15)\big[(x - p + 3) - 6\big] = 0


$$

$$


(x - 15)(x - p - 3) = 0


$$

According to the zero product property, a product equals zero only if one of its factors equals zero. So we set each factor equal to zero. This gives

$$


x - 15 = 0 \quad \Rightarrow\quad x = 15


$$

or

$$


x - p - 3 = 0 \quad \Rightarrow\quad x = p + 3.


$$

With that in mind, let's examine each option.

- Option I: $x = 15$ is indeed a solution.$\:{\color{green}{\checkmark}}$

- Option II: $x = p+4$ is **** a solution.$\:{\color{red}{\times}}$

- Option III: $x = p+3$ is indeed a solution.$\:{\color{green}{\checkmark}}$

- Option IV: $x = p+6$ is **** a solution.$\:{\color{red}{\times}}$

Therefore, the correct answer is "I and III only."

### Example: Rearranging a Quadratic Equation With Unknown Parameters Before Solving

#### Question

Which of the following **** be a solution to the equation

$$


(x - y + 9)(x - 16) = 11(x - 16)


$$

where $y$ is a constant?

1. $x = 16$

2. $x = y-3$

3. $x = y+2$

4. $x = y+7$

#### Explanation

We are given the equation

$$


(x - y + 9)(x - 16) = 11(x - 16).


$$

To solve this equation, we first bring everything over to one side by subtracting $11(x-16)$ from both sides, as follows:

$$


(x - y + 9)(x - 16) - 11(x - 16) = 0


$$

Now, we factor out $(x - 16){:}$

$$


\begin{aligned}(𝑥−16)[(𝑥−𝑦+9)−11] & =0 \\ (𝑥−16)(𝑥−𝑦−2) & =0\end{aligned}


$$

According to the zero product property, a product equals zero only if one of its factors equals zero. So we set each factor equal to zero. This gives

$$


\begin{aligned}𝑥−16=0\,⇒\,𝑥=16\end{aligned}


$$

or

$$


\begin{aligned}𝑥−𝑦−2=0\,⇒\,𝑥=𝑦+2.\end{aligned}


$$

With that in mind, let's examine each option.

- Option I: $x = 16$ is indeed a solution.$\:{\color{green}{\checkmark}}$

- Option II: $x = y-3$ is **** a solution.$\:{\color{red}{\times}}$

- Option III: $x = y+2$ is indeed a solution.$\:{\color{green}{\checkmark}}$

- Option IV: $x = y+7$ is **** a solution.$\:{\color{red}{\times}}$

Therefore, the correct answer is "I and III only."

### Cases With Hidden Factors

Sometimes, an equation must be rewritten to reveal its factors before it can be solved using the zero product rule.

For example, suppose we are given the following equation:

$$


(x - t + 9)(x - 12) + 6(12 - x) = 0


$$

At first glance, this equation looks complicated. However, notice that the factors ${\color{blue}{(x - 12)}}$ and ${\color{red}{(12 - x)}}$ in the first and second terms respectively are additive inverses of each other (i.e., they give zero when added).

$$


(x - t + 9){\color{blue}{(x - 12)}} + 6{\color{red}{(12 - x)}} = 0


$$

Thus, to factor the equation, we first rewrite the second term by factoring out $-1{:}$

$$


6{\color{red}{(12 - x)}} = -6{\color{blue}{(x - 12)}}.


$$

So, the equation becomes

$$


(x - t + 9){\color{blue}{(x - 12)}} - 6{\color{blue}{(x - 12)}} = 0.


$$

Notice that the factors are now the same, and the sign in front of the second term has changed.

Now, we factor out $(x - 12),$ as follows:

$$


\begin{aligned}(𝑥−12)[(𝑥−𝑡+9)−6] & =0 \\ (𝑥−12)(𝑥−𝑡+3) & =0\end{aligned}


$$

According to the zero product property, a product equals zero only if one of its factors equals zero. So we set each factor equal to zero. This gives

$$


\begin{aligned}𝑥−12=0\,⇒\,𝑥=12\end{aligned}


$$

or

$$


\begin{aligned}𝑥−𝑡+3=0\,⇒\,𝑥=𝑡−3.\end{aligned}


$$

### Example: Dealing With Hidden Factors in Quadratic Equations With Unknown Parameters

#### Question

Which of the following **** be a solution to the equation

$$


(x - y + 8)(x - 11) + 5(11 - x) = 0


$$

where $y$ is a constant?

1. $x = 11$

2. $x = y+1$

3. $x = y-1$

4. $x = y-3$

#### Explanation

We are given the equation

$$


(x - y + 8)(x - 11) + 5(11 - x) = 0.


$$

Notice that the last term can be rewritten by factoring out $-1{:}$

$$


5(11 - x) = -5(x - 11).


$$

So, the equation becomes

$$


(x - y + 8)(x - 11) - 5(x - 11) = 0.


$$

Now, we factor out $(x - 11),$ as follows:

$$


\begin{aligned}(𝑥−11)[(𝑥−𝑦+8)−5] & =0 \\ (𝑥−11)(𝑥−𝑦+3) & =0\end{aligned}


$$

According to the zero product property, a product equals zero only if one of its factors equals zero. So we set each factor equal to zero. This gives

$$


\begin{aligned}𝑥−11=0\,⇒\,𝑥=11\end{aligned}


$$

or

$$


\begin{aligned}𝑥−𝑦+3=0\,⇒\,𝑥=𝑦−3.\end{aligned}


$$

With that in mind, let's examine each option.

- Option I: $x = 11$ is indeed a solution.$\:{\color{green}{\checkmark}}$

- Option II: $x = y+1$ is **** a solution.$\:{\color{red}{\times}}$

- Option III: $x = y-1$ is **** a solution.$\:{\color{red}{\times}}$

- Option IV: $x = y-3$ is indeed a solution.$\:{\color{green}{\checkmark}}$

Therefore, the correct answer is "I and IV only."
