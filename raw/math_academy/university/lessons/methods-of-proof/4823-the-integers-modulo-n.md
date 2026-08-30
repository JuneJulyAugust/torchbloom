# The Integers Modulo N

Source: https://www.mathacademy.com/topics/4823?courseId=76
Topic ID: 4823

## Prerequisites

- [Residue Classes](./2655-residue-classes.md)
- [The Multiplication Properties of Modular Arithmetic](./2674-the-multiplication-properties-of-modular-arithmetic.md)

## Lesson

### Introduction

Let $n$ be a positive integer. The set $\mathbb{Z}_n$ of residue (or equivalence) classes modulo $n$ is called **the integers modulo** $\boldsymbol n{:}$

$$


\mathbb{Z}_n = \big\{ [\, 0 \,]_n\,, [\, 1 \,]_n\,, [\, 2 \,]_n\,, \quad \ldots, \quad [\, n-1 \,]_n \big\}.


$$

It's normal to drop the $n$ subscript from the residue classes when the modulus is clear. So, we can also write

$$


\mathbb{Z}_n = \big\{ [\, 0 \,], [\, 1 \,], [\, 2 \,], \quad \ldots, \quad [\, n-1 \,] \big\}.


$$

The set of integers modulo $n$ is special because we can perform arithmetic with its elements.

- The addition of "integers" (classes) in $\mathbb Z_n$ is defined as For example, in $\mathbb Z_4,$ we have Recall that we can pick any element of a residue class as its representative. Since $[\, 5 \,] = [\, 1 \,]$ because $5\equiv 1\, (\textrm{mod} \: 4),$ we can write our answer as

- The subtraction of integers in $\mathbb Z_n$ is defined as For example, in $\mathbb Z_4,$ we have Since $[\, -1 \,] = [\, 3 \,]$ we can write our answer as

In other words, we add (or subtract) integers modulo $n$ as usual and compute the residue modulo $n$ at the end.

The complete addition table modulo $4$ is shown below.

Notice that we can drop the square brackets from the classes if it's clear that we're dealing with residue classes and not ordinary integers.

### Example: Adding and Subtracting Integers Modulo N

#### Question

Perform the following operations in $\mathbb Z_{11}.$ Use the smallest nonnegative representative for the resulting classes.

$$


\begin{aligned}[\,9\,]+[\,5\,] & =[\,?\,] \\ [\,6\,]−[\,10\,] & =[\,?\,]\end{aligned}


$$

#### Explanation

Addition and subtraction of integers in $\mathbb Z_n$ is defined as

$$


\big[ \, a \, \big] \pm \big[ \, b \, \big] = \big[ \, a \pm b \, \big].


$$

Also, recall that we can pick any element of an equivalence class as its representative.

In this case, all operations are carried out modulo $11.$

With that in mind, we obtain the following:

$$


\begin{aligned}[\,9\,]+[\,5\,] & =[\,9+5\,] \\ & =[\,14\,] \\ & =[\,11+3\,] \\ & =[\,3\,] \\ [\,6\,]−[\,10\,] & =[\,6−10\,] \\ & =[\,−4\,] \\ & =[\,0−4\,] \\ & =[\,11−4\,] \\ & =[\,7\,]\end{aligned}


$$

### Multiplication Modulo N

The multiplication of integers in $\mathbb Z_n$ is defined as

$$


\big[ \, a \, \big] \cdot \big[ \, b \, \big] = \big[ \, a \cdot b \, \big].


$$

For example, in $\mathbb Z_4,$ we have

$$


[\, 2 \,] \cdot [\, 3 \,] = [\, 2 \cdot 3 \,] = [\, 6 \,].


$$

Since $[\, 6 \,] = [\, 2 \,]$ because $6 \: \textrm{mod} \: 4 \equiv 2,$ we can express our result as

$$


[\, 2 \,] \cdot [\, 3 \,] = [\, 2 \,].


$$

In other words, we multiply integers modulo $n$ as usual, but at the end, we compute the residue modulo $n$ of the result.

The complete multiplication table modulo $4$ is shown below.

**Watch out!** Multiplication modulo $n$ shares similar properties with multiplication of integers or real numbers. However, some properties might look a bit odd at first glance. For example, notice that in $\mathbb{Z}_4,$ we have

$$


[\, 2 \,] \cdot [\, 2 \,] = [\, 0 \,]


$$

meaning that the product of two nonzero integers modulo $4$ can give zero!

### Example: Multiplying Integers Modulo N

#### Question

Multiply the following integers in $\mathbb Z_{10}.$ Use the smallest nonnegative representative for the resulting class.

$$


\begin{aligned}[\,2\,]⋅[\,4\,] & =[\,?\,] \\ [\,4\,]⋅[\,9\,] & =[\,?\,]\end{aligned}


$$

#### Explanation

Multiplication of integers in $\mathbb Z_n$ is defined as

$$


\big[ \, a \, \big] \cdot \big[ \, b \, \big] = \big[ \, a \cdot b \, \big].


$$

Also, recall that we can pick any element of an equivalence class as its representative.

In this case, all operations are carried out modulo $10.$

With that in mind, we obtain the following:

$$


\begin{aligned}[\,2\,]⋅[\,4\,] & =[\,2⋅4\,] \\ & =[\,8\,] \\ [\,4\,]⋅[\,9\,] & =[\,4⋅9\,] \\ & =[\,36\,] \\ & =[\,3⋅10+6\,] \\ & =[\,3⋅0+6\,] \\ & =[\,6\,]\end{aligned}


$$

### Example: Filling Addition and Multiplication Tables

#### Question

Complete the following multiplication table for $\mathbb Z_6.$ Use the smallest nonnegative representative for each resulting class.

#### Explanation

Multiplication of integers in $\mathbb Z_n$ is defined as

$$


\big[ \, a \, \big] \cdot \big[ \, b \, \big] = \big[ \, a \cdot b \, \big].


$$

Also, recall that we can pick any element of an equivalence class as its representative.

With that in mind, we obtain the following:

$$


\begin{aligned}[\,3\,]⋅[\,3\,] & =[\,9\,]=[\,6+3\,]=[\,3\,] \\ [\,3\,]⋅[\,4\,] & =[\,12\,]=[\,2⋅6\,]=[\,0\,] \\ [\,3\,]⋅[\,5\,] & =[\,15\,]=[\,2⋅6+3\,]=[\,3\,] \\ [\,4\,]⋅[\,3\,] & =[\,12\,]=[\,2⋅6\,]=[\,0\,] \\ [\,4\,]⋅[\,4\,] & =[\,16\,]=[\,2⋅6+4\,]=[\,4\,] \\ [\,4\,]⋅[\,5\,] & =[\,20\,]=[\,3⋅6+2\,]=[\,2\,] \\ [\,5\,]⋅[\,3\,] & =[\,15\,]=[\,2⋅6+3\,]=[\,3\,] \\ [\,5\,]⋅[\,4\,] & =[\,20\,]=[\,3⋅6+2\,]=[\,2\,] \\ [\,5\,]⋅[\,5\,] & =[\,25\,]=[\,4⋅6+1\,]=[\,1\,]\end{aligned}


$$

The completed multiplication table is shown below.

### Example: Arithmetic Modulo N

#### Question

Compute the result of the following operations on elements of $\mathbb Z_{9}.$ Use the smallest nonnegative representative for the resulting class.

$$


\big( \big[ \, 6\, \big] - \big[ \, 20\, \big] \big)\cdot \big( \big[ \, 6\, \big] + \big[ \, 15\, \big] \big) = \big[ \, \boxed{\color{blue}?} \, \big]


$$

#### Explanation

Addition, subtraction, and multiplication of integers in $\mathbb Z_n$ is defined as

$$


\begin{aligned}[\,𝑎\,]±[\,𝑏\,] & =[\,𝑎±𝑏\,] \\ [\,𝑎\,]⋅[\,𝑏\,] & =[\,𝑎⋅𝑏\,]\end{aligned}


$$

Also, recall that we can pick any element of an equivalence class as its representative.

In this case, all operations are carried out modulo $9.$

With that in mind, we obtain the following:

$$


\begin{aligned}([\,6\,]−[\,20\,])⋅([\,6\,]+[\,15\,]) & =[\,6−20\,]⋅[\,6+15\,] \\ & =[\,−14\,]⋅[\,21\,] \\ & =[\,0−14\,]⋅[\,21\,] \\ & =[\,2⋅9−14\,]⋅[\,21\,] \\ & =[\,4\,]⋅[\,21\,] \\ & =[\,4\,]⋅[\,2⋅9+3\,] \\ & =[\,4\,]⋅[\,0+3\,] \\ & =[\,4\,]⋅[\,3\,] \\ & =[\,4⋅3\,] \\ & =[\,12\,] \\ & =[\,9+3\,] \\ & =[\,0+3\,] \\ & =[\,3\,]\end{aligned}


$$
