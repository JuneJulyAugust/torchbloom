# Proving Injectivity

Source: https://www.mathacademy.com/topics/3421?courseId=76
Topic ID: 3421

## Prerequisites

- [Injections](./2678-injections.md)
- [Proof by Contrapositive](./2807-proof-by-contrapositive.md)
- [Negating Statements With Nested Quantifiers](./4258-negating-statements-with-nested-quantifiers.md)

## Lesson

### Introduction

Consider the function $f: \mathbb{R} \to \mathbb{R}$ defined by $f(x)=3x+2.$ Let's prove that this function is injective.

First, we recall the definition of an injection:

*A function $f: X\rightarrow Y$ is an injection if every element $x\in X$ is mapped to a distinct element in $Y{:}$*

$$


x_1 \neq x_2 \qquad\Rightarrow\qquad f(x_1) \neq f(x_2)


$$

This statement contains some negations. Thus, it's easier to show that a function is injective using the (equivalent) contrapositive statement:

*This implication is equivalent to its contrapositive:*

$$


f(x_1)=f(x_2) \qquad\Rightarrow\qquad x_1=x_2


$$

Therefore, the injectivity of $f$ means the following:

*In our case, for all $x_1,x_2 \in \mathbb{R},$*

$$


3x_1+2 = 3x_2+2 \qquad\Rightarrow\qquad x_1 = x_2.


$$

So, to prove the injectivity of $f,$ we need to derive $x_1=x_2$ by assuming that $f(x_1)=f(x_2){:}$

We begin our proof as follows:

*Let $x_1,x_2 \in \mathbb{R},$ and suppose that $f(x_1)=f(x_2).$ Then, we have the following:*

$$


\begin{aligned}𝑓(𝑥_{1}) & =𝑓(𝑥_{2}) \\ 3𝑥_{1}+2 & =3𝑥_{2}+2 \\ 3𝑥_{1} & =3𝑥_{2} \\ 𝑥_{1} & =𝑥_{2}\end{aligned}


$$

This proves that $f(x_1) = f(x_2)$ implies $x_1 = x_2.$

Finally, we state the conclusion:

*Hence, $x_1=x_2,$ as was to be shown. Therefore, $f$ is an injection.*

For clarity, let's restate our proposition and its proof.

### Restating the Full Proof

Proposition:

*The function $f: \mathbb{R} \to \mathbb{R},$ defined by $f(x)=3x+2,$ is injective.*

Proof:

*A function $f: X\rightarrow Y$ is an injection if every element $x\in X$ is mapped to a distinct element in $Y{:}$*

$$


x_1 \neq x_2 \qquad\Rightarrow\qquad f(x_1) \neq f(x_2)


$$

*This implication is equivalent to its contrapositive:*

$$


f(x_1)=f(x_2) \qquad\Rightarrow\qquad x_1=x_2


$$

*In our case, for all $x_1,x_2 \in \mathbb{R},$*

$$


3x_1+2 = 3x_2+2 \qquad\Rightarrow\qquad x_1 = x_2.


$$

*Let $x_1,x_2 \in \mathbb{R},$ and suppose that $f(x_1)=f(x_2).$ Then, we have the following:*

$$


\begin{aligned}𝑓(𝑥_{1}) & =𝑓(𝑥_{2}) \\ 3𝑥_{1}+2 & =3𝑥_{2}+2 \\ 3𝑥_{1} & =3𝑥_{2} \\ 𝑥_{1} & =𝑥_{2}\end{aligned}


$$

*Hence, $x_1=x_2,$ as was to be shown. Therefore, $f$ is an injection.*

### Example: Understanding the Definition of Injectivity

#### Question

What does it mean for the function $f: \mathbb{Z} \to \mathbb{N}$ defined by $f(x)=3x^2+1$ to be **** injective?

#### Explanation

A function $f: X\rightarrow Y$ is an injection if every element $x\in X$ is mapped to a distinct element in $Y.$

In other words,

$$


\forall x_1, x_2 \: \big( x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2) \big).


$$

The negation of this statement is

$$


\exists x_1, x_2 \: \lnot \big( x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2) \big).


$$

Now, recall that

$$


\begin{aligned}¬(𝐴⇒𝐵) & ≡¬(¬𝐴∨𝐵) \\ & ≡¬(¬𝐴)∧¬𝐵 \\ & ≡𝐴∧¬𝐵\end{aligned}


$$

So, to determine non-injectivity, we need to show that there exists $x_1,x_2$ such that

$$


x_1 \neq x_2 \qquad\textrm{and}\qquad f(x_1) = f(x_2).


$$

In our case, the non-injectivity of $f$ means that $\boxed{\color{blue}\textrm{there exist}}$ at least two values $x_1$ and $x_2$ such that

$$


\boxed{\color{blue}x_1 \neq x_2} \qquad \boxed{\color{blue}\textrm{and}} \qquad \boxed{\color{blue}3x_1^2+1 = 3x_2^2+1}.


$$

### Example: Proving a Function is Injective

#### Question

Prove that the function $f: \mathbb{C} \to \mathbb{R} \times \mathbb{R}$ defined by $f(z)=\left(\dfrac12(z+\overline{z}), \dfrac{\mathrm{i}}2(\overline{z}-z)\right)$ is injective.

#### Explanation

First, we recall the definition of an injection:

A function $f: X\rightarrow Y$ is an injection if every element $x\in X$ is mapped to a distinct element in $Y{:}$

$$


x_1 \neq x_2 \qquad\Rightarrow\qquad f(x_1) \neq f(x_2)


$$

In this case, it would be easier to prove the contrapositive statement.

This implication is equivalent to its contrapositive:

$$


f(x_1)=f(x_2) \qquad\Rightarrow\qquad x_1=x_2


$$

Now, we simply need to derive $z_1=z_2$ by assuming that $f(z_1)=f(z_2){:}$

So, let $z_1,z_2 \in \mathbb{C},$ and suppose that $f(z_1)=f(z_2).$ Then, we have

$$


\begin{aligned}𝑓(𝑧_{1}) & =𝑓(𝑧_{2}) \\ (\frac{1}{2}(𝑧_{1}+\overset{𝑧_{1}}{}),\frac{i}{2}(\overset{𝑧_{1}}{}−𝑧_{1})) & =(\frac{1}{2}(𝑧_{2}+\overset{𝑧_{2}}{}),\frac{i}{2}(\overset{𝑧_{2}}{}−𝑧_{2})).\end{aligned}


$$

Since two pairs are equal if and only if their respective components are equal, we obtain:

$$


\begin{aligned}\begin{aligned}\frac{1}{2}(𝑧_{1}+\overset{𝑧_{1}}{})=\frac{1}{2}(𝑧_{2}+\overset{𝑧_{2}}{}) \\ \frac{i}{2}(\overset{𝑧_{1}}{}−𝑧_{1})=\frac{i}{2}(\overset{𝑧_{2}}{}−𝑧_{2})\end{aligned}\, & ⇒\,\begin{aligned}𝑧_{1}+\overset{𝑧_{1}}{}=𝑧_{2}+\overset{𝑧_{2}}{} \\ \overset{𝑧_{1}}{}−𝑧_{1}=\overset{𝑧_{2}}{}−𝑧_{2}\end{aligned}\end{aligned}


$$

To solve this system, recall the following properties of the complex conjugate:

$$


z_1+\overline{z_1} = 2\cdot \textrm{Re}(z_1), \qquad z_1-\overline{z_1} = 2\textrm{i}\cdot \textrm{Im}(z_1)


$$

Therefore, our system reduces to

$$


\begin{aligned}\begin{aligned}2⋅Re(𝑧_{1})=2⋅Re(𝑧_{2}) \\ −2i⋅Im(𝑧_{1})=−2i⋅Im(𝑧_{2})\end{aligned}\, & ⇒\,\begin{aligned}Re(𝑧_{1})=Re(𝑧_{2}) \\ Im(𝑧_{1})=Im(𝑧_{2})\end{aligned}\, & ⇒\,𝑧_{1}=𝑧_{2}\end{aligned}


$$

Finally, we state the conclusion:

Hence, $z_1=z_2,$ as was to be shown. Therefore, $f$ is an injection.

### Example: Proving a Function is Not Injective

#### Question

Prove that the function $f: \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z} \times \mathbb{Z}$ defined by $f(u,v)=(2u-v,v-2u)$ is **** injective.

#### Explanation

First, we recall the definition of an injection:

A function $f: X\rightarrow Y$ is an injection if every element $x$ in $X$ is mapped to a distinct element in $Y.$

In other words,

$$


\forall x_1, x_2 \: \big( x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2) \big).


$$

The negation of this statement is

$$


\exists x_1, x_2 \: \lnot \big( x_1 \neq x_2 \Rightarrow f(x_1) \neq f(x_2) \big).


$$

Now, recall that

$$


\begin{aligned}¬(𝐴⇒𝐵) & ≡¬(¬𝐴∨𝐵) \\ & ≡¬(¬𝐴)∧¬𝐵 \\ & ≡𝐴∧¬𝐵\end{aligned}


$$

So, we get the following:

To disprove a universal statement, it's sufficient to find a counterexample.

In other words, we need to show that there exists $x_1,x_2$ such that

$$


x_1 \neq x_2 \qquad\textrm{and}\qquad f(x_1) = f(x_2).


$$

So, we simply need to find two pairs that give the same value of the function.

Notice that

$$


f(1,1) = (1,-1)


$$

and

$$


f(2,3) = (1,-1).


$$

Finally, we state the conclusion:

Hence, $(1,1) \neq (2,3)$ and $f(1,1) = f(2,3).$ Therefore, $f$ isn't an injection.
