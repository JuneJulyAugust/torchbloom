# Divisibility of Integers by 2, 5, 10, 4, and 8

Source: https://www.mathacademy.com/topics/2805?courseId=39
Topic ID: 2805

## Prerequisites

- [Three-Digit by One-Digit Division](../grade-5/536-three-digit-by-one-digit-division.md)
- [Creating and Interpreting Whole Number Expressions](../grade-5/2396-creating-and-interpreting-whole-number-expressions.md)

## Lesson

### Introduction

Dividing very large numbers can take some effort. Thankfully, there are some rules that allow us to determine whether one number is divisible by another *without* having to carry out the division!

A number is divisible by $2$ if the *last digit* is an even number. In other words, if the last digit is ${\color{blue}{0}},{\color{blue}{2}},{\color{blue}{4}},{\color{blue}{6}},$ or ${\color{blue}{8}},$ then the number is divisible by $2.$

For example, the following numbers are divisible by $2$ because their last digit is even.

$$


51{\color{blue}{0}}, \qquad 785{\color{blue}{2}}, \qquad 232,65{\color{blue}{4}}, \qquad 197,478,24{\color{blue}{6}}, \qquad 578,197,478,24{\color{blue}{8}}


$$

On the other hand, the following numbers are *not* divisible by $2$ because their last digit is *not* even.

$$


35{\color{red}{1}}, \qquad 547{\color{red}{3}}, \qquad 58,68{\color{red}{5}}, \qquad 239,63{\color{red}{7}}, \qquad 100,000,000,00{\color{red}{9}}


$$

We also have some easy divisibility rules for $5$ and $10.$ Again, they depend only on the last digit:

- A number is divisible by $5$ if the *last digit* is $5$ or $0.$

- A number is divisible by $10$ if the *last digit* is $0.$

Let's see some examples.

### Example: Determining Whether a Number is Divisible by 2, 5, or 10

#### Question

Which of the following numbers is $135\,215\,780$ divisible by?

1. $2$

2. $5$

3. $10$

#### Explanation

Recall the following divisibility tests for $2,$ $5,$ and $10{:}$

- A number is divisible by $2$ if the last digit is an even number (i.e. $0,$ $2,$ $4,$ $6,$ or $8$).

- A number is divisible by $5$ if the last digit is $5$ or $0.$

- A number is divisible by $10$ if the last digit is $0.$

The last digit of the number $135\,215\,780$ is $0.$ So, $135\,215\,780$ is divisible by $2,$ $5,$ and $10.$

Therefore, the correct answer is "I, II, and III."

### Divisibility by 4

A number is divisible by $4$ if the *last two digits* are divisible by $4$.

Let's determine whether the following number is divisible by $4{:}$

$$


124, 424, 6{\color{blue}{24}}


$$

The number formed by the last two digits is ${\color{blue}{24}},$ and ${\color{blue}{24}}$ is divisible by $4.$ Therefore, $124, 424, 624$ is divisible by $4.$

Now, consider the following number:

$$


251, 8{\color{red}{18}}


$$

The number formed by the last two digits is ${\color{red}{18}},$ and ${\color{red}{18}}$ is *not* divisible by $4.$ Therefore, $251, 818$ is *not* divisible by $4.$

We sometimes need to use long division to determine whether the last two digits are divisible by $4.$

For example, the number

$$


1,7{\color{blue}{84}}


$$

is divisible by $4$ because ${\color{blue}{84}}$ is divisible by $4.$ We can check this using long division.

Finally, note that if a number is divisible by $4,$ then it is divisible by $2.$ Consequently, any number whose last digit is odd is *not* divisible by $4.$

### Example: Determining Whether a Number is Divisible by 4

#### Question

Which digits, when inserted into the blank, make the number $153\,384\,2\square4$ divisible by $4?$

1. $1$

2. $2$

3. $4$

#### Explanation

A number is divisible by $4$ if the last two digits form a number that is divisible by $4.$

The last two digits of the number $153\,384\,2\square4$ are $\square4.$

- If $1$ is substituted into the blank, then the last two digits are $14,$ which is ** divisible by $4.$

- If $2$ is substituted into the blank, then the last two digits are $24,$ which is indeed divisible by $4.$

- If $4$ is substituted into the blank, then the last two digits are $44,$ which is indeed divisible by $4.$

Therefore, the correct answer is "II and III only."

### Divisibility by 8

A number is divisible by $8$ if the last three digits form a number that is divisible by $8.$

For example, consider the number $845\,128\,016.$ The last three digits form the number $016 = 16,$ which is divisible by $8.$ Therefore, the number $845\,128\,016$ is divisible by $8.$

Okay, that was easy. But what about the number $745\,254\,786\,768?$ Is this divisible by $8?$

The last three digits form the number $768.$ Dividing $768$ by $8$ requires a bit more work. However, there is an easy rule to check whether a $3$-digit number is divisible by $8.$ That is, we add four times the hundreds digit to twice the tens digit and the ones digit, and then check if the result is divisible by $8.$ In our case, we have

$$


4(7) + 2(6) + 8 = 28+12+8 = 48,


$$

which is divisible by $8.$ Therefore, $745\,254\,786\,768$ is divisible by $8.$

Finally, note that if a number is not divisible by $2$ *and* $4,$ then it cannot be divisible by $8.$ Sometimes, it's easiest to check those first.

### Example: Determining Whether a Number is Divisible by 8

#### Question

Which of the following numbers are divisible by $8?$

1. $2\,134\,564$

2. $687\,335\,123$

3. $31\,125\,784$

#### Explanation

A number is divisible by $8$ if the last three digits form a number that is divisible by $8.$

Note that if a number is not divisible by $2$ and $4,$ then it cannot be divisible by $8.$

With that in mind, let's go through each of our numbers:

- The last three digits of $2\,134\,564$ are $564.$ Since $564$ is not divisible by $8,$ we conclude that $2\,134\,564$ is not divisible by $8$ either.

- The number $687\,335\,123$ is ** divisible by $8$ since it is not divisible by $2.$

- The last three digits of $31\,125\,784$ are $784.$ Since $784$ is divisible by $8,$ we conclude that $31\,125\,784$ is divisible by $8.$

Therefore, the correct answer is "III only."
