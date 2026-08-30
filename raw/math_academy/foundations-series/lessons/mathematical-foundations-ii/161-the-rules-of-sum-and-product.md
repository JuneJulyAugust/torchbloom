# The Rules of Sum and Product

Source: https://www.mathacademy.com/topics/161?courseId=111
Topic ID: 161

## Prerequisites

- [Evaluating Whole Number Expressions Containing Exponents](../../../elementary-school/lessons/grade-5/2475-evaluating-whole-number-expressions-containing-exponents.md)

## Lesson

### Introduction

Suppose we have to choose a course to take. We can choose either a language course or a musical instrument course.

- The $\color{red}3$ language courses are French, German, and Cantonese.

- The $\color{blue}2$ musical instrument courses are Piano and Violin.

To find the total number of choices we have, we can use the **rule of sum**:

If we have to pick an element from *either* a set $\color{red}A$ with $\color{red}m$ elements *or* from a set $\color{blue}B$ with $\color{blue}n$ elements, the number of possible choices is ${\color{red}m}+{\color{blue}n}.$

Therefore, the total number of choices is ${\color{red}3}+ {\color{blue}2} = 5.$

We can also extend the rule of sum to any number of sets.

### Example: Applying the Rule of Sum

#### Question

Noah has $2$ red ties, $4$ black ties, and $3$ blue ties. How many choices of tie does Noah have?

#### Explanation

In order to find the total number of choices Noah has, we can use the ****:

$$


2+4+3 = 9


$$

Therefore, Noah has $9$ choices of tie.

### The Rule of Product

Now suppose that we can choose a language *and* a musical instrument course when deciding which courses to take.

- The $\color{red}3$ language courses are French, German, and Cantonese.

- The $\color{blue}2$ musical instrument courses are Piano and Violin.

To find the total number of combinations, we can use the **rule of product**:

If we have to pick an element from a set $\color{red}A$ with $\color{red}m$ elements *and* an element from a set $\color{blue}B$ with $\color{blue}n$ elements, the number of possible choices is ${\color{red}m}\times {\color{blue}n}.$

Therefore, there are ${\color{red}3} \times {\color{blue}2} = 6$ possible choices.

To check this, we can create a table:

In the table above, each pair represents a single combination of courses. For example, $(F,P)$ means we take the French and Piano courses. Counting up the number of pairs, we confirm that there are $6$ choices in total.

We can also extend the rule of product to any number of sets.

### Example: Applying the Rule of Product

#### Question

Paul rolls a six-sided die and flips $2$ quarter coins. How many different possible outcomes are there?

#### Explanation

For the die, there is a total of $6$ outcomes: $1,2,3,4,5,6.$

For each quarter, there are just $2$ outcomes: "Heads" and "Tails".

Using the rule of product, we have

$$


\begin{aligned}Total Possible Outcomes & =Number of outcomes for the die \\ & ×Number of outcomes for the first coin \\ & ×Number of outcomes for the second coin \\ & =6×2×2 \\ & =6×2^{2} \\ & =24.\end{aligned}


$$

So, there are $24$ possible outcomes.

### The Rule of Sum and Rule of Product Applied to Combination Locks

When bike lock manufacturers design combination locks, they rely on there being a large number of possible combinations. It would take a thief way too long to try every combination, provided that there are enough combinations.

For example, let's consider the following ordered combination lock.

For this lock, each "Letter" can be any capital from A-E, and each "Digit" can be any integer between $0$-$9.$ How many possible ordered combinations are there?

To solve this problem, we use the rule of product.

First, we note that:

- for each letter, there is a total of $5$ possibilities: "A", "B", "C", "D", "E", and

- for each digit, there are $10$ possibilities: $0,$ $1,$ $2,$ $3,$ $4,$ $5,$ $6,$ $7,$ $8,$ $9.$

Using the rule of product, we have

$$


\begin{aligned}Number of combinations & =Number of options in the first slot \\ & ×Number of options in the second slot \\ & ×Number of options in the third slot \\ & ×Number of options in the fourth slot \\ & =5×5×10×10 \\ & =5^{2}×10^{2} \\ & =25×100 \\ & =2\,500.\end{aligned}


$$

So, there are $2\,500$ possible ordered combinations.

### Example: Applying the Rules of Sum and Product With Letter and Digits

#### Question

A bike lock has an ordered combination of $4$ possible characters as shown below:

Here,

- each "Letter" can be any capital from A-E, and

- each "Digit" can be any integer between $0$-$9.$

How many possible ordered combinations are there?

#### Explanation

For each letter, there is a total of $5$ possibilities: A, B, C, D, E.

For each digit, there are $10$ possibilities: $0,$ $1,$ $2,$ $3,$ $4,$ $5,$ $6,$ $7,$ $8,$ $9.$

Using the ****, there are $10 + 5 = 15$ choices for each position.

Now, using the ****, we have

$$


\begin{aligned}Number of combinations & =Number of options in the first slot \\ & ×Number of options in the second slot \\ & ×Number of options in the third slot \\ & ×Number of options in the fourth slot \\ & =15×15×15×15 \\ & =15^{4} \\ & =50\,625.\end{aligned}


$$

So, there are $50\,625$ possible ordered combinations.
