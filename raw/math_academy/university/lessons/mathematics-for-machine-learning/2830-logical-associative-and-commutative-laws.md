# Logical Associative and Commutative Laws

Source: https://www.mathacademy.com/topics/2830?courseId=145
Topic ID: 2830

## Prerequisites

- [Logical Equivalence](./2821-logical-equivalence.md)

## Lesson

### Introduction

The **associative law for conjunctions** states that when we have multiple conjunctions in a row, the placement of parentheses does not matter:

$$


(A \land B) \land C \equiv A \land (B \land C)


$$

We can prove this equivalence using a truth table.

In natural language, the associative law for conjunctions amounts to moving a comma between "and" statements. For example, the associative law states that the sentence

$$


\underbrace{\vphantom{p}\text{The cat is quiet}}_{(A} \quad \underbrace{\text{and}\vphantom{p}}_{\land} \quad \underbrace{\vphantom{p}\text{the dog is loud}}_{B)} \quad , \quad \underbrace{\vphantom{p}\text{and}}_{\land} \quad \underbrace{\vphantom{p}\text{the turtle is slow}}_{C}


$$

is logically equivalent to the sentence

$$


\underbrace{\vphantom{p}\text{The cat is quiet}}_{A} \quad , \quad \underbrace{\vphantom{p}\text{and}}_{\land} \quad \underbrace{\vphantom{p}\text{the dog is loud}}_{(B} \quad \underbrace{\text{and}\vphantom{p}}_{\land} \quad \underbrace{\text{the turtle is slow}}_{C)}.


$$

### The Associative Law for Disjunctions

The **associative law for disjunctions** is similar:

$$


(A \lor B) \lor C \equiv A \lor (B \lor C)


$$

We can prove this equivalence using a truth table.

In natural language, the associative law for disjunctions amounts to moving a comma between "or" statements. For example, the associative law states that the sentence

$$


\underbrace{\vphantom{p}\text{The cat is quiet}}_{(A} \quad \underbrace{\text{or}\vphantom{p}}_{\lor} \quad \underbrace{\vphantom{p}\text{the dog is loud}}_{B)} \quad , \quad \underbrace{\vphantom{p}\text{or}}_{\lor} \quad \underbrace{\vphantom{p}\text{the turtle is slow}}_{C}


$$

is logically equivalent to the sentence

$$


\underbrace{\vphantom{p}\text{The cat is quiet}}_{A} \quad , \quad \underbrace{\vphantom{p}\text{or}}_{\lor} \quad \underbrace{\vphantom{p}\text{the dog is loud}}_{(B} \quad \underbrace{\text{or}\vphantom{p}}_{\lor} \quad \underbrace{\text{the turtle is slow}}_{C)}.


$$

### Example: Simplifying Sentences Using the Associative Law

#### Question

Simplify the sentence "The car is fancy and big, and the car is big."

#### Explanation

First, let's rewrite the phrase "the car is fancy and big" as the equivalent phrase "the car is fancy and the car is big." The sentence now reads

"The car is fancy and the car is big, and the car is big."

Then, using the associative law, we can move the comma:

"The car is fancy, and the car is big and the car is big."

Now, we can simplify the phrase "the car is big and the car is big" to just "the car is big." The sentence now reads

"The car is fancy, and the car is big."

Finally, we can write the sentence more concisely as

"The car is fancy and big."

### Example: Simplifying Symbolic Statements Using the Associative Law

#### Question

Simplify $(P \land Q) \land (Q \lor Q).$

#### Explanation

Using the associative and idempotent laws, we get

$$


\begin{aligned}(𝑃∧𝑄)∧(𝑄∨𝑄) & ≡(𝑃∧𝑄)∧𝑄 \\ & ≡𝑃∧(𝑄∧𝑄) \\ & ≡𝑃∧𝑄.\end{aligned}


$$

### The Commutative Law for Conjunctions

The **commutative law for conjunctions** states that we can switch the order of a conjunction:

$$


A \land B \equiv B \land A


$$

We can prove this result using a truth table.

In natural language, the commutative law for conjunctions amounts to swapping two phrases surrounding the word "and." For example, the commutative law states that the sentence

$$


\underbrace{\vphantom{p}\text{The cat is quiet}}_{(A} \quad \underbrace{\text{and}\vphantom{p}}_{\land} \quad \underbrace{\vphantom{p}\text{the dog is loud}}_{B)}


$$

is logically equivalent to the sentence

$$


\underbrace{\vphantom{p}\text{The dog is loud}}_{(B} \quad \underbrace{\text{and}\vphantom{p}}_{\land} \quad \underbrace{\vphantom{p}\text{the cat is quiet}}_{A)}.


$$

### The Commutative Law for Disjunctions

The **commutative law for disjunctions** is similar:

$$


A \lor B \equiv B \lor A


$$

We can prove this result using a truth table.

Likewise, in natural language, the commutative law for disjunctions amounts to swapping two phrases surrounding the word "or." For example, the commutative law states that the sentence

$$


\underbrace{\vphantom{p}\text{The cat is quiet}}_{(A} \quad \underbrace{\text{or}\vphantom{p}}_{\lor} \quad \underbrace{\vphantom{p}\text{the dog is loud}}_{B)}


$$

is logically equivalent to the sentence

$$


\underbrace{\vphantom{p}\text{The dog is loud}}_{(B} \quad \underbrace{\text{or}\vphantom{p}}_{\lor} \quad \underbrace{\vphantom{p}\text{the cat is quiet}}_{A)}.


$$

### Example: Simplifying Sentences Using the Commutative Law

#### Question

Simplify the following sentence: "The table is brown and it is high, and it is brown."

#### Explanation

Using the commutative law, we can replace the phrase "the table is brown and it is high" with the phrase "the table is high and it is brown." The sentence now reads

"The table is high and it is brown, and it is brown."

Then, using the associative law, we can move the comma:

"The table is high, and it is brown and it is brown."

Now, we can simplify the phrase "it is brown and it is brown" to just "it is brown." The sentence now reads

"The table is high and it is brown."

Finally, we can write the sentence more concisely:

"The table is high and brown."

### Example: Simplifying Symbolic Statements Using the Commutative Law

#### Question

Simplify $(A \land B) \land (B \land A).$

#### Explanation

Using the associative, commutative, and idempotent laws, we get

$$


\begin{aligned}(𝐴∧𝐵)∧(𝐵∧𝐴) & ≡𝐴∧(𝐵∧𝐵)∧𝐴 \\ & ≡𝐴∧𝐵∧𝐴 \\ & ≡(𝐴∧𝐴)∧𝐵 \\ & ≡𝐴∧𝐵.\end{aligned}


$$
