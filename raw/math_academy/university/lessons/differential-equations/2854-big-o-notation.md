# Big-O Notation

Source: https://www.mathacademy.com/topics/2854?courseId=61
Topic ID: 2854

## Prerequisites

- [L'Hopital's Rule](../../../ap-courses/lessons/ap-calculus-ab/463-l-hopital-s-rule.md)
- [The Pythagorean Theorem and the Triangle Inequality](../linear-algebra/2153-the-pythagorean-theorem-and-the-triangle-inequality.md)

## Lesson

### Introduction

When studying limiting behavior, it is often useful to compare the size of one function to another near a given point. **Big-O** notation provides a concise way to express such boundedness.

For example, saying that a function is $\mathcal O(1)$ near a point means that it remains *bounded* within some neighborhood of that point - it does not "blow up" as we approach the limit.

Formally, we say that $f(x)$ **is of order** $g(x)$ as $x\to a,$ and we write

$$


f(x)=\mathcal O(g(x)) \qquad \text{as} \qquad x\to a


$$

if there exist positive constants $K$ and $\delta$ such that

$$


|f(x)| \le K|g(x)| \qquad \text{for all } 0<|x-a|<\delta.


$$

To illustrate this, consider the polynomial

$$


f(x) = -7x^3 + 3x + 4.


$$

We will prove that $f=\mathcal O(1)$ as $x\to 0.$

In this case, we must show that

$$


|f| \leq K\cdot 1 \qquad \text{for} \qquad 0 < |x| < \delta,


$$

i.e.,

$$


{|f| \leq K} \qquad \text{for} \qquad {0 < |x| < \delta}.


$$

By the triangle inequality, we have

$$


\begin{aligned}|𝑓(𝑥)| & =|−7𝑥^{3}+3𝑥+4| \\ & ≤|7𝑥^{3}|+|3𝑥|+|4| \\ & =7|𝑥|^{3}+3|𝑥|+4.\end{aligned}


$$

Now, let $|x| < 1.$ Then, we have

$$


\begin{aligned}|𝑓(𝑥)| & ≤7|𝑥|^{3}+3|𝑥|+4 \\ & <7|1|^{3}+3|1|+4 \\ & =14.\end{aligned}


$$

Therefore, $|f(x)| \leq 14$ whenever $|x| < 1.$ Thus, taking ${K=14}$ and ${\delta =1}$ satisfies the definition, and we conclude

$$


f(x) = \mathcal O(1) \qquad \text{as} \qquad x\to 0.


$$

### Example: Proving the Order of a Polynomial

#### Question

For the polynomial $f(x) = -3x^4 + x^2 + 4x,$ show that $f = \mathcal O(x)$ as $x\to 0.$

#### Explanation

We say $f(x)$ is of order $g(x)$ as $x\to a,$ and we write

$$


f(x) = \mathcal O(g(x)) \quad \text{as}\quad x\to a


$$

if there exist ${\text{positive}}$ constants $K$ and $\delta$ such that

$$


{|f(x)| \leq K|g(x)|} \quad\text{for all}\quad 0 < |x-a| < \delta.


$$

So, in our case, we need to show that

$$


{|f(x)| \leq K|x|} \quad \text{for} \quad {0 < |x| < \delta}.


$$

By the triangle inequality, we have

$$


\begin{aligned}|𝑓(𝑥)| & =|−3𝑥^{4}+𝑥^{2}+4𝑥| \\ & ≤|3𝑥^{4}|+|𝑥^{2}|+|4𝑥| \\ & =3|𝑥|^{4}+|𝑥|^{2}+4|𝑥|.\end{aligned}


$$

If $|x| < 1,$ then we have ${|x|^2 \lt |x|}.$ Also, since $|x|<1,$ we have $|x|^4 < |x|.$ Therefore,

$$


3|x|^4 \le 3|x| \quad\text{and}\quad |x|^2 \le |x|.


$$

Hence

$$


\begin{aligned}|𝑓(𝑥)| & ≤3|𝑥|^{4}+|𝑥|^{2}+4|𝑥| \\ & ≤3|𝑥|+|𝑥|+4|𝑥| \\ & =8|𝑥|.\end{aligned}


$$

Therefore, $|f(x)| \leq 8|x|$ whenever $|x| < 1.$ Thus, taking ${K=8}$ and ${\delta = 1}$ satisfies the definition, and we conclude that $f = \mathcal O(x)$ as $x\to 0.$

### Infinite Limit

We say $f(x)$ *is of order* $g(x)$ as $x\to \infty,$ and we write

$$


f(x) = \mathcal O(g(x)) \qquad \text{as} \qquad x\to \infty


$$

if there exist positive constants $K$ and $M$ such that

$$


|f(x)| \leq K|g(x)|\qquad\text{for all }\qquad x > M.


$$

We often abbreviate this to simply

$$


f(x) = \mathcal O(g(x)).


$$

In other words, when there is no $x\to a$ statement, we assume $a$ is infinite.

### The Limit Test

Suppose we wish to test whether the following statement is true:

$$


f(x) = \mathcal O(g(x)) \qquad \text{as}\qquad x\to a


$$

To do this, we can examine the following limit:

$$


\lim\limits_{x\to a} \dfrac{f(x)}{g(x)}


$$

We have the following:

- If the limit is *finite*, the statement is true.

- If the limit is *infinite*, the statement is false.

- If the limit does not exist, the test is *inconclusive*.

Note that the *same* limit test works for $x\to a$ and $x\to\infty$ order statements!

Let's see some examples.

### Example: Applying the Limit Test

#### Question

Suppose $f(x) = e^x + x\ln x.$ Which of the following statements are true?

1. $f= \mathcal O(x)$ as $x\to\infty$

2. $f= \mathcal O(\ln x)$ as $x\to\infty$

3. $f= \mathcal O(xe^{x})$ as $x\to\infty$

#### Explanation

Suppose we wish to test whether the following statement is true:

$$


f(x) = \mathcal O(g(x)) \quad \text{as}\quad x\to a


$$

where $a$ is either finite or $+\infty.$ To do this, we can examine the following limit:

$$


\lim\limits_{x\to a} \dfrac{f(x)}{g(x)}.


$$

We have the following:

- If the limit is **, the statement is true.

- If the limit is **, the statement is false.

- If the limit does not exist, the test is inconclusive.

Here, we must consider the function

$$


f(x) = e^x + x\ln x.


$$

Now, let's consider each statement in turn.

- Statement I is false. Let $g(x) = x.$ Then, we have Since direct evaluation leads to the indeterminate form $\dfrac{\infty}{\infty},$ we can evaluate the limit using L'Hopital's rule: Hence, $f \neq \mathcal O(x)$ as $x\to\infty.$

- Statement II is false. Let $g(x) =\ln x.$ Then, using L'Hopital's rule where needed, we have Hence, $f \neq \mathcal O(x)$ as $x\to\infty.$

- Statement III is true. Let $g(x) = xe^{x}.$ Then, using L'Hopital's rule where needed, we have Hence, $f = \mathcal O(xe^x)$ as $x\to\infty.$

Therefore, the correct answer is "III only."

### Properties of Big-O

We also have the following facts:

- *The sum and product properties*. If $f = \mathcal O(h)$ and $g = \mathcal O(k)$ as $x\to a,$ then

- *The constant multiple property*. If $f = \mathcal O(cg)$ as $x\to a,$ then

- *The reflexive property*.

- *The transitive property*. If $f = \mathcal O(g)$ and $g = \mathcal O(h)$ as $x\to a,$ then

- *The absorption property*. If $f = \mathcal O(g+h)$ and $g = \mathcal O(h)$ as $x\to a,$ then

Let's see how they can be used in practice.

### Example: Applying Properties of Big-O

#### Question

Consider the following statement.

If $f(x) = e^{x}+ \sec x,$ then $f = \mathcal O(1)$ as $x\to 0.$

A sketch of a proof of this statement is given below

$\text{L1}{:}\; e^{x} = \mathcal O(1)$ as $x\to 0$

$\text{L2}{:}\; \sec x = \mathcal O(1)$ as $x\to 0$

$\text{L3}{:}\; f = \mathcal O(2)$ as $x\to 0$

$\text{L4}{:}\; f = \mathcal O(1)$ as $x\to 0$

Fill in the blanks in the reasoning below that justify each step.

$\quad$ Line $\text{L3}$ follows from lines $𝑋𝑋𝑋𝑋𝑋𝑋𝑋𝑋𝑋𝑋$ and the $𝑋𝑋𝑋𝑋𝑋𝑋𝑋$ property.

$\quad$ Line $\text{L4}$ follows from line $𝑋𝑋𝑋𝑋𝑋$ and the $𝑋𝑋𝑋𝑋𝑋𝑋𝑋$.

#### Explanation

Suppose $f(x), g(x), h(x)$ and $k(x)$ are functions and $c$ is a nonzero constant. Then, we have the following properties of Big-O notation.

- The sum and product properties. If then

- The constant multiple property. If then

- The reflexive property.

- The transitive property. If then

- The absorption property. If then

With that in mind, let us justify each selected step.

- We first consider line $\text{L3}.$ From line $\text{L1}$ we have and from line $\text{L2}$ we have Thus, by lines $\boxed{\text{L1 and L3}}$ and $\boxed{\text{the sum property}},$ we obtain

- Finally, we consider line $\text{L4}.$ From line $\boxed{\text{L4}}$ we have Since $2$ is just a constant multiple of $1,$ it follows by $\boxed{\text{the constant multiple property}}$ that
