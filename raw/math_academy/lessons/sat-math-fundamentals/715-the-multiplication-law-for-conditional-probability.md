# The Multiplication Law for Conditional Probability

Source: https://www.mathacademy.com/topics/715?courseId=120
Topic ID: 715

## Prerequisites

- [Fractions of Fractions](../grade-7/323-fractions-of-fractions.md)
- [Conditional Probabilities From Venn Diagrams](../geometry/324-conditional-probabilities-from-venn-diagrams.md)

## Lesson

### Introduction

Suppose and are two events in a random experiment. The conditional probability is the probability that the event occurs *given that has already occurred*.

We've already seen how to compute conditional probabilities using Venn diagrams. But is there a formula that we can use?

By definition, we say that is given by the formula

For instance, let's suppose we have different shaped and colored candies in a bag, and we take one out at random. Let's assume that the probability of picking a green circle candy is while the probability of picking a green candy is Then, what is the probability that the candy we have picked is a circle, given that it is green?

Let's call the event "the candy is a circle" and the event "the candy is green." Then we need to find

- The probability of picking a green circle candy is so

- The probability of picking a green candy is therefore,

So, using the definition of a conditional probability, we get

### Example: Computing a Conditional Probability Given a Joint Probability

#### Question

Suppose that $A$ and $B$ are two events such that $P(B) = \dfrac23$ and $P(A\cap B) = \dfrac13.$ What is $P(A|B)?$

#### Explanation

We use the definition of the conditional probability $P(A|B){:}$

$$


P(A|B) = \dfrac{P(A\cap B)}{P(B)}


$$

Substituting the given values, we get

$$


\begin{aligned}P(A|B)&=\dfrac{P(A\cap B)}{P(B)}\\\[5pt] &=\dfrac{\left(\dfrac{1}{3}\right)}{\left(\dfrac{2}{3}\right)}\\\[5pt] &=\dfrac{1}{2}. \end{aligned}


$$

### Example: Computing a Conditional Probability: Word Problems

#### Question

A number is selected randomly from the set of integers between $1$ to $10$ inclusive. If the selected number is odd, then what is the probability that the number is less than $4?$

#### Explanation

Let us call $O$ the event "the number is odd" and $L$ the event " the number is less than $4$".

The required probability is $P(L | O)$, which is given by

$$


P(L | O)= \dfrac{P(O\cap L)}{P(O)}.


$$

Let's find $P(O)$ and $P(O\cap L).$

- There are $5$ odd numbers among the $10$ integers from $1$ to $10,$ so we have

- There are only two numbers, $1$ and $3$, that are both odd and less than $4.$ So, we have

Therefore, substituting the above into our formula for $P(L | O)$, we get

$$


P(L | O) = \dfrac{\left(\dfrac{1}{5}\right)}{\left(\dfrac12\right)} = \dfrac{2}{5}.


$$

### The Multiplication Law for Conditional Probability

Given two events $A$ and $B$ in a random experiment, the definition of the conditional probability $P(A|B)$ is

$$


P(A|B) = \dfrac{P(A\cap B)}{P(B)}.


$$

By multiplying both sides of the formula by $P(B),$ we get the **multiplication law for probability**, which states that

$$


P(A\cap B) = P(B) \cdot P(A|B).


$$

Also, since $P(A\cap B) = P(B\cap A),$ we can also write the multiplication law in the following form:

$$


P(A\cap B) = P(A) \cdot P(B|A)


$$

### Example: Computing a Probability Using the Multiplication Law for Conditional Probability

#### Question

Suppose that $A$ and $B$ are two events such that $P(A|B)=0.3,$ $P(A)=0.5,$ and $P(B)=0.6.$ Find $P(B|A).$

#### Explanation

Using the multiplication law for probability, we have that

$$


\begin{aligned}𝑃(𝐴∩𝐵) & =𝑃(𝐵)⋅𝑃(𝐴|𝐵) \\ & =0.6⋅0.3 \\ & =0.18.\end{aligned}


$$

Now, substituting $P(A\cap B) = 0.18$ and $P(A)=0.5$ into the definition of $P(B|A),$ we get

$$


\begin{aligned}𝑃(𝐵|𝐴) & =\frac{𝑃(𝐵∩𝐴)}{𝑃(𝐴)} \\ & =\frac{𝑃(𝐴∩𝐵)}{𝑃(𝐴)} \\ & =\frac{0.18}{0.5} \\ & =0.36.\end{aligned}


$$

Notice that we used the fact that $P(A\cap B) = P(B\cap A).$

### Example: Computing a Probability Using the Multiplication Law for Conditional Probability: Word Problems

#### Question

A box contains $3$ red, $1$ blue, and $2$ green marbles. Two marbles are randomly drawn one by one without replacement. What is the probability that both marbles are red?

#### Explanation

Let us call $R_1$ the event "the first marble is red" and $R_2$ the event "the second marble is red."

The required probability is $P(R_1\cap R_2),$ which is given by

$$


P(R_1\cap R_2) = P(R_1) \cdot P(R_2|R_1).


$$

Let's find $P(R_1)$ and $P(R_2|R_1).$

- There are $3$ red marbles among the $3+1+2=6$ marbles, so we have

- If a red marble is drawn, there are $2$ red marbles left in the box among the remaining $5$ marbles. So, we have

Substituting the above data into the multiplication law for conditional probability, we get

$$


P(R_1\cap R_2)=\dfrac{1}{2}\cdot\dfrac{2}{5}=\dfrac{1}{5}.


$$
