# Relations on Finite Sets

Source: https://www.mathacademy.com/topics/2817?courseId=76
Topic ID: 2817

## Prerequisites

- [Modular Congruence](./2641-modular-congruence.md)

## Lesson

### Introduction

We'll now begin discussing **relations**, one of the most important topics in elementary set theory. Most (if not all) of the mathematical concepts you've learned up to this point can be thought of in terms of relations. The goal is to give these concepts a common framework.

To start with, let's define the set $A$ as

$$


A = \big\{1,2,3,4\big\}.


$$

Now, consider the following standard relationships we can define between elements of $A{:}$

- Suppose we want to define the concept "$a$ is less than $b$" over the elements of $A.$ One way to do this is to write down a set containing *all ordered* pairs $(a,b)$ such that $a < b$ and $a, b\in A.$ This gives the following set:

- Next, suppose we want to define "$a$ divides $b$" over the elements of $A.$ This time, we write down the ordered pairs $(a,b)$ such that $a \mid b.$ Note that $(1,1) \in R_{\,\mid\,}$ since $1 \mid 1.$ The same is true for for $(2,2),(3,3),(4,4).$

- Finally, let's define "$a$ has the same parity as $b$" over $A.$ Remember that two numbers have the same parity if they're both even or both odd: Note that "$2$ has the same parity as $4$" and "$4$ has the same parity as $2$" are considered separately. Since both are true, we include $(2,4)$ *and* $(4,2)$ in our set of ordered pairs.

Although $R_{\,<\,}, R_{\,\mid\,}$ and $R_p$ describe very different relationships between pairs of elements of $A,$ they have one thing in common: they're all *subsets of the Cartesian product* $A\times A.$ This suggests that subsets of the Cartesian product can be used to describe a wide variety of mathematical relationships that exist between pairs of set elements.

This gives us our first definition:

*A **** $R$ on a set $A$ is a subset of the Cartesian product $A\times A = A^2.$*

$$


R\subseteq A^2


$$

We often refer to binary relations simply as **relations**. So, the sets $R_{\,<\,}, R_{\,\mid\,}$ and $R_p$ are all (binary) relations on $A.$

### Example: Listing the Elements of a Standard Relation

#### Question

Let $A=\{1, 2\}$ and consider the relation "is greater than or equal to" $(\geq)$ on $A.$ If this relation is given by the set $R,$ express $R$ as a set of ordered pairs.

#### Explanation

A relation $R$ on a set $A$ is a subset of the Cartesian product $A\times A = A^2.$

$$


R\subseteq A^2


$$

In this case, $R$ is the set of ordered pairs $(x,y) \in A^2$ such that $x\geq y.$

Let's check each element $x \in A$ to see which elements $y \in A$ it could be paired with to satisfy the relation.

- If $x=1,$ then the value $y=1$ satisfies $x\geq y.$ So, $R$ contains the ordered pair $(1,1).$

- If $x=2,$ then the values $y=1$ and $y=2$ satisfy $x\geq y.$ So, $R$ contains the ordered pairs $(2,1)$ and $(2,2).$

Therefore, we can describe our relation as the following set of ordered pairs:

$$


R = \{ (1,1), (2, 1), ( 2, 2) \}


$$

### Example: Identifying Elements of Standard Relations

#### Question

Let $A=\{-2, 0, 2\}$ and consider the relation "are congruent modulo $4$" on $A.$ Write out $R$ as a set of ordered pairs.

#### Explanation

A relation $R$ on a set $A$ is a subset of the Cartesian product $A\times A = A^2.$

$$


R\subseteq A^2


$$

In this case, $R$ is the set of ordered pairs $(x,y) \in A^2$ such that $x \equiv y \: (\textrm{mod}\:4).$

Let's check each element $x \in A$ to see which elements $y \in A$ it could be paired with to satisfy the relation.

- If $x=-2,$ then the values $y=-2$ and $y=2$ satisfy $x \equiv y \: (\textrm{mod}\:4),$ since $4 \mid (-2+2)$ and $4 \mid (-2-2).$ So, $R$ contains the ordered pairs $(-2,-2)$ and $(-2,2).$

- If $x=0,$ then the value $y=0$ satisfies $x \equiv y \: (\textrm{mod}\:4),$ since $4 \mid (0-0).$ So, $R$ contains the ordered pair $(0,0).$

- If $x=2,$ then the values $y=-2$ and $y=2$ satisfy $x \equiv y \: (\textrm{mod}\:4),$ since $4 \mid (2+2)$ and $4 \mid (2-2).$ So, $R$ contains the ordered pairs $(2,-2)$ and $(2,2).$

Therefore, we can describe our relation as the following set of ordered pairs:

$$


R = \big\{ (-2,-2), (-2,2), (0,0), (2,-2), (2,2)\big\}


$$

### The x R y Notation

Suppose we have a binary relation $R$ on $A,$ so $R\subseteq A^2.$ Then, the following notation is often convenient:

- When $(x,y) \in R,$ we write $x \: R \: y.$ In words, we say "$x$ is related to $y$ by $R.$"

- When $(x,y) \notin R,$ we write $ x R y.$ In words, we say "$x$ is *not* related to $y$ by $R.$"

For example, consider the following relation:

$$


R = \big\{ (x,y) \in \mathbb{Z}^2 \: : \: x \mid y \big\}


$$

The following statements are equivalent:

$$


(2,10) \in R \qquad\Leftrightarrow\qquad 2 \: R \: 10


$$

We also have

$$


(3,10) \notin R \qquad\Leftrightarrow\qquad 3 \: {\!R\!} \: 10


$$

The relation $x \mid y$ is a so-called **standard relation.** With standard relations, we can replace the letter $R$ with the usual symbol describing the relation to retrieve our usual notation:

$$


(2,10) \in R \qquad\Leftrightarrow\qquad 2 \: {\color{red}{R}} \: 10 \qquad\Leftrightarrow\qquad 2 \:{\color{red}{\mid}}\: 10


$$

For an ordered pair that's not an element of our relation, we negate the usual symbol.

$$


(3,10) \not\in R \qquad\Leftrightarrow\qquad 3 \: {\color{red}{\!R\!}} \: 10 \qquad\Leftrightarrow\qquad 3 \:{\color{red}{\not\mid}}\: 10


$$

The same idea applies to other standard relations. For example, consider the set $A,$ given by

$$


A=\big\{2,4,6,8,10\big\}.


$$

Suppose we define the relations "is less than" $(\lt)$, "is congruent modulo $2$ to" $(\equiv),$ and "is equal to" $(=)$ over $A.$ Then, we have the following equivalences.

$$


\begin{aligned}(2,10)∈𝑅_{<} & \,⇔\,2\,𝑅_{<}\,10\, & & ⇔\,2<10 \\ (2,4)∈𝑅_{≡} & \,⇔\,2\,𝑅_{≡}\,4\, & & ⇔\,2≡4 \\ (6,6)∈𝑅_{=} & \,⇔\,6\,𝑅_{=}\,6\, & & ⇔\,6=6\end{aligned}


$$

Similarly, for elements not in the standard relation, we have:

$$


\begin{aligned}(10,2)∉𝑅_{<} & \,⇔\,10\,\,𝑅_{<}\,\,2\, & & ⇔\,10≮2 \\ (1,4)∉𝑅_{≡} & \,⇔\,1\,\,𝑅_{≡}\,\,4\, & & ⇔\,1≢4 \\ (2,4)∉𝑅_{=} & \,⇔\,2\,\,𝑅_{=}\,\,4\, & & ⇔\,2≠4\end{aligned}


$$

So, not only can relations be thought of as a general way to describe relationships between mathematical objects, but the $a\,R\, b$ notation is something you've been using all along!

### Example: Using the x R y Notation

#### Question

Consider the following set:

$$


A = \big\{0, 1\big\}


$$

Given the relation $R$ on $A$ defined by

$$


x\:R\: y \quad \Leftrightarrow \quad x\neq y,


$$

which of the following statements are true?

1. $0\: R\: 0$

2. $0 \: R\: 1$

3. $1 \: \!R\!\: 1$

#### Explanation

A relation $R$ on a set $A$ is a subset of the Cartesian product $A\times A = A^2.$

$$


R\subseteq A^2


$$

We also have the following notations:

- $x \: R \: y$ if and only if $(x,y) \in R$

- $x \: \!R\! \: y$ if and only if $(x,y) \notin R$

In this case, we have $x \: R \: y$ if and only if $x\neq y.$ For this relation, note that

- the symbols $R$ and $\neq$ are interchangeable, and

- the symbols $\!R\!$ and $=$ are also interchangeable.

With that in mind, let's examine our statements in turn:

- Statement I is false. Replacing $R$ with the symbol $\neq$, we have $0 \neq 0,$ which is false.

- Statement II is true. Replacing $R$ with the symbol $\neq,$ we have $0 \neq 1,$ which is true.

- Statement III is true. Replacing $\!R\!$ with the symbol $=,$ we have $1 = 1,$ which is true.

Therefore, the correct answer is "II and III only."

### Non-Standard Relations

The relations we've considered so far (e.g., "is greater than" or "divides") are all standard relations that are encountered regularly when studying mathematics.

However, defining a relation as a subset of a Cartesian product allows us to think of relations more broadly.

To explain, let's consider the following set:

$$


A = \big\{1,2,3,4\big\}.


$$

We saw how to define "$a$ is less than $b,$" "$a$ divides $b$," and "$a$ has the same parity as $b$" over $A.$ But relations do not necessarily need to have any "standard" meaning attributed to them. For example, the following set is also a valid relation on $A{:}$

$$


R= \big\{(1,2), (1,4), (3,2), (4,3)\big\}


$$

You might be hard-pressed to find an intuitive meaning behind this relation, but it's a relation on $A$ nonetheless! We'll refer to these kinds of relations as **non-standard relations.**

We can also define non-standard relations using set-builder notation. For example, consider the following relation over $B = \{2,4,5\}.$

$$


R = \big\{ (x,y) \in B^2 \: : \: x \mid y^2 \big\}


$$

In this case, $R$ is the set of ordered pairs $(x,y) \in B^2$ such that $x$ divides $y^2{:}$

Let's check each element $x \in B$ to see which elements $y \in B$ it could be paired with to satisfy the conditions of our relation.

- If $x={\color{red}{2}},$ then the values $y={\color{blue}{2}}$ and $y={\color{blue}{4}}$ satisfy $x\mid y^2,$ since So, $R$ contains the ordered pairs $({\color{red}{2}},{\color{blue}{2}})$ and $({\color{red}{2}},{\color{blue}{4}}).$

- If $x={\color{red}{4}},$ then the values $y={\color{blue}{2}}$ and $y={\color{blue}{4}}$ satisfy $x\mid y^2,$ since So, $R$ contains the ordered pairs $({\color{red}{4}},{\color{blue}{2}})$ and $({\color{red}{4}},{\color{blue}{4}}).$

- If $x={\color{red}{5}},$ then the value $y={\color{blue}{5}}$ satisfies $x\mid y^2,$ since So, $R$ contains the ordered pair $({\color{red}{5}},{\color{blue}{5}}).$

Therefore,

$$


R = \big\{ ({\color{red}{2}},{\color{blue}{2}}), ({\color{red}{2}},{\color{blue}{4}}), ({\color{red}{4}},{\color{blue}{2}}), ({\color{red}{4}},{\color{blue}{4}}), ({\color{red}{5}},{\color{blue}{5}}) \big\}.


$$

**Watch Out!** When applying the $x\,R\,y$ notation to non-standard relations, care must be used when replacing $R$ with the symbol involved in the description of the relation. For example,

$$


({\color{red}{4}},{\color{blue}{2}}) \in R \quad \Leftrightarrow\quad {\color{red}{4}}\mid {\color{blue}{2}}^2


$$

however

$$


({\color{red}{4}},{\color{blue}{2}}) \in R \quad \not\Leftrightarrow\quad {\color{red}{4}}\mid {\color{blue}{2}}.


$$

### Example: Listing the Elements of a Non-Standard Relation

#### Question

Let $S = \{3, 5 \}.$ Which set is equivalent to the following relation on $S?$

$$


R = \big\{ (x,y) \in S^2 \: : \: y \not \mid 3x \big\}


$$

#### Explanation

A relation $R$ on a set $A$ is a subset of the Cartesian product $A\times A = A^2.$

$$


R\subseteq A\times A


$$

In this case, $R$ is the set of ordered pairs $(x,y) \in S^2$ such that $y \not \mid 3x.$

Let's check each element $x \in S$ to see which elements $y \in S$ it could be paired with to satisfy the conditions of our relation.

- If $x=3,$ then the value $y=5$ satisfies $y \not\mid 3x.$ So, $R$ contains the ordered pair $(3,5).$

- If $x=5,$ then there is no value of $y \in B$ that satisfies $y \not\mid 3x.$

Therefore, we can describe our relation as the following set of ordered pairs:

$$


R = \big\{ (3,5) \big\}


$$
