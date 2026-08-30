# Properties of Integer Divisibility

Source: https://www.mathacademy.com/topics/4433?courseId=76
Topic ID: 4433

## Prerequisites

- [The Extended Euclidean Algorithm](./2677-the-extended-euclidean-algorithm.md)
- [Disproving Implications](./4927-disproving-implications.md)

## Lesson

### Introduction

Recall that if $a$ and $b$ are integers where $a \neq 0,$ the notation

$$


a \mid b


$$

means that $a$ divides $b.$ This means there exists an integer $k$ such that

$$


b = a \cdot k.


$$

On the other hand, $a \not\mid b$ denotes the fact that $a$ does not divide $b.$

This simple definition can be used to prove some basic properties of integer divisibility.

### Transitivity of Divisibility

The first property we'll study is called the **transitivity of divisibility.** It states the following:

**Theorem**

*For integers $a,$ $b,$ and $c$ with $a, b\neq 0,$ we have*

$\qquad$ $a \mid b \quad$ *and* $\quad b \mid c$ $\qquad\Longrightarrow\qquad$ $a \mid c.$

We can prove this statement using the definition of divisibility.

**Proof**

*Given that $a \mid b,$ there exists an integer $k_1$ such that*

$$


b=ak_1.


$$

*Similarly, given that $b \mid c,$ there exists an integer $k_2$ such that*

$$


c=bk_2.


$$

*Substituting the expression for $b$ into our equation for $c,$ we get*

$$


\begin{aligned}𝑐 & =𝑏𝑘_{2} \\ & =(𝑎𝑘_{1})𝑘_{2} \\ & =𝑎(𝑘_{1}𝑘_{2}).\end{aligned}


$$

*Since $k_1$ and $k_2$ are integers, their product $k=k_1k_2$ is also an integer. Therefore,*

$$


c = ak


$$

*which, by the definition of divisibility, means that $a \mid c.$*

### Example: Identifying True Statements Regarding the Transitivity of Divisibility

#### Question

Which of the following statements are true?

1. If $5 \mid m$ then $25 \mid m$

2. If $25 \mid m$ then $10 \mid m$

3. If $25 \mid m$ then $5 \mid m$

#### Explanation

For any integers $a,$ $b,$ and $c,$ we have transitivity of divisibility:

$a \mid b \quad$ and $\quad b \mid c$ $\qquad\Longrightarrow\qquad$ $a \mid c$

With that in mind, let's examine each of the statements.

- Statement I is false. As a counterexample, let ${\color{blue}{m}}={\color{blue}{5}}.$ Then, $5\mid {\color{blue}{5}}$ but $25\not \mid {\color{blue}{5}}.$

- Statement II is false. As a counterexample, let ${\color{blue}{m}}={\color{blue}{25}}.$ Then, $25\mid {\color{blue}{25}}$ but $10\not \mid {\color{blue}{25}}.$

- Statement III is true. First, note that $5 \mid 25.$ Therefore, we have $5\mid 25$ and $25\mid m,$ which implies that $5 \mid m.$

Therefore, the correct answer is "III only."

### The Divisibility of a Product

Let's now state our next property, known as the **divisibility of a product:**

**Theorem**

*For any integers $a,$ $b,$ and $c,$*

$\qquad$ $c \mid ab \quad$ *and* $\quad \text{gcd}(a,c)=1$ $\qquad\Longrightarrow\qquad$ $c \mid b$

This statement assumes that $\text{gcd}(a,c)=1$ (i.e., that $a$ and $c$ are coprime). This suggests we may want to use *Bézout’s identity* to prove this statement since it relates two integers to their greatest common divisor.

Recall that Bézout’s identity states that for any two integers $a$ and $b,$ there exist integers $u$ and $v$ such that

$$


au+bv= \text{gcd}(a,b)


$$

where $\text{gcd}(a,b)$ is the greatest common divisor of $a$ and $b.$

With that in mind, let's prove this statement.

**Proof**

*Given that $\text{gcd}(a,c)=1,$ by Bézout’s identity there exist integers $u$ and $v$ such that*

$$


au + cv = 1.


$$

*On the other hand, since $c\: | \: ab,$ there exists an integer $k$ such that*

$$


ab=ck.


$$

*Multiplying both sides of the first equation by $b$ and substituting $ab=ck,$ we get the following:*

$$


\begin{aligned}𝑎𝑢+𝑐𝑣 & =1 \\ (𝑎𝑢+𝑐𝑣)𝑏 & =𝑏 \\ (𝑎𝑏)𝑢+𝑐𝑣𝑏 & =𝑏 \\ (𝑐𝑘)𝑢+𝑐𝑣𝑏 & =𝑏 \\ 𝑐(𝑘𝑢+𝑣𝑏) & =𝑏\end{aligned}


$$

*As $k,u,v,$ and $b$ are integers, then $ku+ vb = m$ is an integer too. Hence,*

$$


cm = b


$$

*which implies that*

$$


c\: | \: b.


$$

### Example: Identifying True Statements Regarding the Divisibility of a Product

#### Question

Which of the following statements are true?

1. If $3^3 \: | \: 3^2b$ then $3^3 \: | \: b$

2. If $20 \: | \: 30b$ then $20 \: | \: b$

3. If $2^5 \: | \: 3^4b$ then $2^5 \: | \: b$

#### Explanation

For any integers $a,$ $b,$ and $c,$

$c \:|\: ab \quad$ and $\quad \text{gcd}(a,c)=1$ $\qquad\Longrightarrow\qquad$ $\quad c \:|\: b.$

With that in mind, let's examine each of the statements.

- Statement I is false. As a counterexample, let ${\color{blue}{b}}={\color{blue}{3}}.$ Then, $3^3\mid 3^2\cdot {\color{blue}{3}}$ but $3^3\not\mid {\color{blue}{3}}.$

- Statement II is false. As a counterexample, let ${\color{blue}{b}}={\color{blue}{2}}.$ Then, $20\mid 30\cdot {\color{blue}{2}}$ but $20\not\mid {\color{blue}{2}}.$

- Statement III is true. First, note that $\text{gcd}(2^5, 3^4)=1.$ Therefore, we have $2^5 \: | \: 3^4b$ and $\text{gcd}(2^5, 3^4)=1,$ which implies $2^5\: | \: b.$

Therefore, the correct answer is "III only."

### Divisibility by a Product

Let's now state our final property, known as the **divisibility of an integer by a product:**

**Theorem**

*For any integers $a,$ $b,$ and $c,$*

$\qquad$ *$a \:|\: c,$ $\quad b \:|\: c, \quad$ and $\quad \text{gcd}(a,b)=1$ $\qquad\Longrightarrow\qquad$ $ab \:|\: c.$*

The proof is given below.

**Proof**

*Given that $\text{gcd}(a,b)=1,$ there exist integers $u$ and $v$ such that*

$$


au + bv = 1.


$$

*On the other hand, since $a\: | \: c$ and $b\: | \: c,$ there exist integers $k$ and $l$ such that*

$$


c=ak, \qquad\text{and}\qquad c=bl.


$$

*Multiplying both sides of the first equation by $c$ and substituting $c=ak$ and $c=bl,$ we get the following:*

$$


\begin{aligned}𝑎𝑢+𝑏𝑣 & =1 \\ (𝑎𝑢+𝑏𝑣)𝑐 & =𝑐 \\ 𝑎𝑢𝑐+𝑏𝑣𝑐 & =𝑐 \\ 𝑎𝑢(𝑏𝑙)+𝑏𝑣(𝑎𝑘) & =𝑐 \\ 𝑎𝑏(𝑢𝑙+𝑣𝑘) & =𝑐\end{aligned}


$$

*As $k,l,u,$ and $v$ are integers, then $ul + vk = m$ is an integer too. Hence,*

$$


ab\cdot m = c


$$

*which implies that*

$$


ab\: | \: c.


$$

### Example: Identifying True Statements Regarding Divisibility by a Product

#### Question

Which of the following statements are true?

1. If $3 \: | \: a$ and $21 \: | \: a$ then $63 \: | \: a$

2. If $3 \: | \: b$ and $22 \: | \: b$ then $66 \: | \: b$

3. If $2^3 \: | \: c$ and $3^2 \: | \: c$ then $72 \: | \: c$

#### Explanation

Recall that for any integers $a,$ $b,$ and $c,$

$a \:|\: c,$ $\quad b \:|\: c, \quad$ and $\quad \text{gcd}(a,b)=1$ $\qquad\Longrightarrow\qquad$ $ab \:|\: c.$

With that in mind, let's examine each of the statements.

- Statement I is false. As a counterexample, let ${\color{blue}{a}}={\color{blue}{21}}.$ Then, $(3\mid {\color{blue}{21}})$ and $(21\mid {\color{blue}{21}}),$ but $(63\not\mid {\color{blue}{21}}).$

- Statement II is true. First, note that $\text{gcd}(3, 22)=1$ and $3\cdot 22 = 66.$ Therefore, we have $(3 \: | \: b), (22 \: | \: b),$ and $\text{gcd}(3, 22)=1,$ which implies $(66\: | \: b).$

- Statement III is true. First, note that $\text{gcd}(2^3, 3^2)=1$ and $2^3\cdot 3^2 = 72.$ Therefore, we have $(2^3 \: | \: c), (3^2 \: | \: c),$ and $\text{gcd}(2^3, 3^2)=1,$ which implies $(72 \: | \: c).$

Therefore, the correct answer is "II and III only."
