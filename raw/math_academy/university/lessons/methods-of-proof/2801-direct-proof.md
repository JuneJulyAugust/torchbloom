# Direct Proof

Source: https://www.mathacademy.com/topics/2801?courseId=76
Topic ID: 2801

## Prerequisites

- [Expanding Binomials Using Pascal's Triangle](../../../high-school/traditional/lessons/algebra-i/1157-expanding-binomials-using-pascal-s-triangle.md)
- [Grammatical Constructions for Conditional Statements](./4422-grammatical-constructions-for-conditional-statements.md)

## Lesson

### Introduction

We now begin our journey into mathematical proof writing. Let's start by introducing some important terminology:

*An **** is a mathematical statement that is assumed to be true without requiring proof.*

Axioms are the central underpinnings of **axiomatic systems.** All provable results within a system can be derived from a set of axioms using logical reasoning.

For example, most of the geometry you've studied up to this point refers to geometry within flat, two-dimensional space, otherwise known as **Euclidean Geometry**.

There are five axioms from which the *entire system* of Euclidean Geometry is based:

- **Axiom 1:** *Given two distinct points, there is a line segment that joins them.*

- **Axiom 2:** *Any line segment can be extended into a straight line.*

- **Axiom 3:** *Given two distinct points, we can construct a circle where one point lies on the circle and whose center is at the other point.*

- **Axiom 4:** *All right angles are congruent.*

- **Axiom 5:** *Given a line and a point that does not lie on the line, there exists exactly one line through the point that's parallel to the line.*

Everything you know about Euclidean geometry can be proved starting from just these five axioms!

A **mathematical proof** is a rigorous argument that a statement is true based on a set of axioms and previously established results.

Mathematical proofs follow a logical sequence of steps, starting from these foundational principles and building upon them using algebraic techniques and logic to arrive at a conclusion. Any mathematical proof aims to provide a watertight, convincing argument that a statement holds true.

### Direct Proof

**Direct proof** is a technique for proving that an implication $P\Rightarrow Q$ is true. We start with a true statement $P,$ and then use definitions, algebraic techniques, and logic to demonstrate that $Q$ must also be true.

The outline of a typical direct proof is the following:

**Statement.** *If $P,$ then $Q.$*

*Proof.*

**Assumption:** *Suppose $P$ is true.*

*Explanation of what $P$ means using axioms, definitions, or other results.*

*Algebraic techniques, logic, and further definitions or axioms are used to demonstrate, through a series of inferences, that $P$ implies $Q.$*

**Conclusion:** *Therefore, $Q$ is true.*

In this lesson, we'll learn how to prove parity statements using direct proof.

### Parity Statements

Consider the following statement:

$$


𝑛


$$

Notice that this is an (implicit) universal statement of the form

$$


P \Rightarrow Q \quad \equiv \quad \forall n \in \mathbb{Z}, \, P(n) \Rightarrow Q(n).


$$

Let's outline a proof schema (or template) for constructing a proof of this result:

- **Step 1**: We assume $P$ is true. In other words, we let $n$ be an even integer.

- **Step 2:** Next, we use the *definition* of evenness to write $n=2a$ for some integer $a.$

- **Step 3:** Then, we substitute $n=2a$ into the expression for $3n+2$ and use algebraic techniques to show that the expression can be written as $2b,$ where $b$ is an integer.

- **Step 4:** Since $3n+2 = 2b$ is a multiple of $2,$ we conclude that it's even (i.e., that $Q$ is true).

Note the following:

- For now, we're simply constructing a "bird's-eye view" of how direct proof works. We haven't yet proved anything! We'll get to the details of the proof shortly.

- The example concerns a statement of the form However, we can use the same proof template to prove parity statements of the following forms: The only difference is that we'll also need to use the definition of an odd integer. Let's see an example of this.

### Example: Completing a Proof Schema

#### Question

Suppose we wish to construct a direct proof of the following statement:

$5n+4$ ** $n$ **

A proof schema is outlined below. Fill in the missing entries.

Let $n$ be an $\boxed{\phantom{\textrm{odd}}}$ integer. Then, $n=\boxed{\phantom{2a+1}}$ for some integer $a.$

Substituting $\boxed{\phantom{n=2a+1}}$ into the expression $5n+4$, we can show that $5n+4=\boxed{\phantom{2b+1}},$ where $b$ is $\boxed{\phantom{\textrm{an integer}}}.$

Therefore, since $5n+4$ $\boxed{\phantom{\textrm{is one more than}}}$ a multiple of $2,$ we conclude that $5n+4$ is $\boxed{\phantom{\textrm{odd}}}.$

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to show the following:

$$


n \text{ is odd} \quad\Rightarrow\quad 5n+4 \text{ is odd}


$$

We start by using the fact that $n$ is odd.

**

The idea is to substitute $n=2a+1$ into our expression $5n+4$ and show it is ** by writing it as ** a multiple of $2.$

**

Once we've shown this, the proof is complete, and we can state our conclusion.

**

### Constructing a Proof

Recall that we wish to prove the following result:

*If $n$ is even, then $3n+2$ is even.*

Let's go through the proof step-by-step. We start by stating that an arbitrary integer, call it $n,$ is even:

**Step 1:** *Let $n$ be an even integer.*

Now, we use the definition of evenness:

**Step 2:** *Then, $n=2a$ for some integer $a.$*

The idea is to substitute $n=2a$ into the expression $3n+2$ and show it is even by writing it as a multiple of $2.$

**Step 3:** *Substituting $n=2a$ into the expression, we get*

$$


\begin{aligned}3𝑛+2 & =3(2𝑎)+2 \\ & =6𝑎+2 \\ & =2\underset{𝑏}{\underset{}{(3𝑎+1)}}.\end{aligned}


$$

Now, if we define another integer $b=3a+1$ (highlighted above), we have that $3n+2 = 2b,$ which shows that $3n+2$ is indeed a multiple of $2.$ So, we proceed as follows:

*Let $b = 3a+1.$ Since $a$ is an integer, we have that $b$ is an integer. As a result, we have*

$$


\begin{aligned}3𝑛+2 & =2\overset{\overset{(3𝑎+1)}{}}{𝑏} \\ & =2𝑏\end{aligned}


$$

*which is a multiple of $2.$*

Finally, we write our conclusion:

**Step 4:** *Therefore, $3n+2$ is even.*

### Stating the Full Proof

When writing a formal mathematical proof, we usually include only the essential details and exclude any additional commentary.

So, when communicating the full proof that $n$ is even implies $3n+2$ is even, we could write our proof as follows:

*Let $n$ be an even integer.* *Then, $n=2a$ for some integer $a.$*

*Substituting $n=2a$ into the expression, we get*

$$


\begin{aligned}3𝑛+2 & =3(2𝑎)+2 \\ & =2(3𝑎+1).\end{aligned}


$$

*Let $b = 3a+1.$ Since $a$ is an integer, we have that $b$ is an integer. As a result, we have*

$$


\begin{aligned}3𝑛+2 & =2(3𝑎+1) \\ & =2𝑏\end{aligned}


$$

*which is a multiple of $2.$*

*Therefore, $3n+2$ is even.*

Notice that we skipped a few steps in the algebra in step 3. This is quite normal. Formal proofs usually only include the steps essential to understanding the core argument. Although, this depends on the author and the intended reader. If the intended readers are new to mathematical proofs, keeping more detail is probably a good idea.

### Some "Axioms"

Before we look at another example, let's state some results that we'll use in our work without proof:

- The sum of two integers is always an integer.

- The difference between two integers is always an integer.

- The product of two integers is always an integer.

- Any integer is either even or odd (but never both).

- The associative, commutative, and distributive laws hold for all integers.

These results aren't quite axioms because they can be proved from other, more fundamental axioms. Nonetheless, for our purposes, we can think of them as axioms: we won't prove them. Instead, we'll just assume that they're true. In math, we can use statements that were proved earlier in new proofs without re-proving them each time.

### Example: Proving a Linear Expression Is Even

#### Question

Prove that if $n$ is odd, then $7n-1$ is even.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to prove the following:

$$


𝑛


$$

We start by using the fact that $n$ is odd.

If $n$ is odd, then $n=2a+1$ for some integer $a.$

The idea is to substitute $n=2a+1$ into the expression $7n-1$ and show it is even by writing it as a multiple of $2.$

Therefore,

$$


\begin{aligned}7𝑛−1 & =7(2𝑎+1)−1 \\ & =14𝑎+7−1 \\ & =14𝑎+6 \\ & =2\underset{𝑏}{\underset{}{(7𝑎+3)}}.\end{aligned}


$$

Now, if we define another integer $b=7a+3$ (highlighted above), we have that $7n-1 = 2b,$ which shows that $7n-1$ is indeed a multiple of $2.$

Let $b = 7a+3.$ Since $a$ is an integer, we have that $b$ is an integer.

Therefore, we have

$$


\begin{aligned}7𝑛−1 & =2\underset{𝑏}{\underset{}{(7𝑎+3)}} \\ & =2𝑏\end{aligned}


$$

which is a multiple of $2.$

Finally, we write our conclusion.

Therefore, $7n-1$ is even.

### Example: Proving a Linear Expression Is Odd

#### Question

Prove that $15n+7$ is odd whenever $n$ is even.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to show the following:

$$


𝑛


$$

We start by using the fact that $n$ is even.

Let $n$ be an even integer. Then, $n=2a$ for some integer $a.$

The idea is to substitute $n=2a$ into our expression $15n+7$ and show it is odd by writing it as a multiple of $2,$ plus $1.$

Therefore,

$$


\begin{aligned}15𝑛+7 & =15(2𝑎)+7 \\ & =30𝑎+7 \\ & =(30𝑎+6)+1 \\ & =2\underset{𝑏}{\underset{}{(15𝑎+3)}}+1.\end{aligned}


$$

Now, if we define another integer $b = 15a+3$ (highlighted above), we have that $15n+7 = 2b+1,$ which shows that $15n+7$ is indeed one more than a multiple of $2.$

Let $b = 15a+3.$ Since $a$ is an integer, we have that $b$ is an integer.

Therefore, we have

$$


\begin{aligned}15𝑛+7 & =2\underset{𝑏}{\underset{}{(15𝑎+3)}}+1 \\ & =2𝑏+1\end{aligned}


$$

which is one larger than a multiple of $2.$

Finally, we write our conclusion.

Therefore, $15n+7$ is odd.

### Example: Proving the Parity of a Nonlinear Expression

#### Question

Prove that $n^2 - 2$ is odd if $n$ is odd.

#### Explanation

Recall the following:

- If an integer $n$ is even, then there exists an integer $p$ such that $n=2p.$

- If an integer $n$ is odd, then there exists an integer $q$ such that $n=2q+1.$

In this case, we need to prove the following:

$$


𝑛


$$

We start by using the fact that $n$ is odd.

Since $n$ is odd, it can be expressed as $n=2a+1$ for some integer $a.$

The idea is to substitute $n=2a+1$ into our expression $n^2 - 2$ and show it is odd by writing it as a multiple of $2,$ plus $1.$

Now, writing $n^2 - 2$ in terms of $a,$ we obtain the following:

$$


\begin{aligned}𝑛^{2}−2 & =(2𝑎+1)^{2}−2 \\ & =(4𝑎^{2}+4𝑎+1)−2 \\ & =(4𝑎^{2}+4𝑎−2)+1 \\ & =2\underset{𝑏}{\underset{}{(2𝑎^{2}+2𝑎−1)}}+1.\end{aligned}


$$

Now, if we define another integer $b=2a^2 + 2a - 1$ (highlighted above), we have that $n^2 - 2 = 2b+1,$ which shows that $n^2 - 2$ is indeed one more than a multiple of $2.$

Let $b=2a^2 + 2a - 1.$ Since $a$ is an integer, we have that $b$ is an integer.

Therefore, we have

$$


\begin{aligned}𝑛^{2}−2 & =2\underset{𝑏}{\underset{}{(2𝑎^{2}+2𝑎−1)}}+1 \\ & =2𝑏+1\end{aligned}


$$

which is one more than a multiple of $2.$

Finally, we write our conclusion.

Therefore, $n^2 - 2$ is odd.

### Commonly Used Terminology

Different mathematical results have different names. Let's go through those that are commonly used.

- A **theorem** is a major result for which a mathematical proof exists (e.g., the Pythagorean Theorem).

- A **proposition** is a result that is less important than a theorem for which a mathematical proof exists.

- A **lemma** is a small, intermediate result or proposition often used as a stepping stone in proving a larger theorem.

- A **corollary** is a smaller result that follows from a theorem. This is often an important special case of a theorem.

- A **conjecture** is a result that some people believe to be true, but no valid proof currently exists.

One example of a famous conjecture is the **twin prime conjecture.** A twin prime pair is an ordered pair $(p,p+2)$ such that $p$ and $p+2$ are both prime. The first few twin primes are:

$$


(3, 5), \quad (5,7), \quad (11,13), \quad (17,19), \quad ...


$$

It's conjectured that there are infinitely many twin primes. Many mathematicians believe this to be true, but no proof of the twin prime conjecture currently exists.
