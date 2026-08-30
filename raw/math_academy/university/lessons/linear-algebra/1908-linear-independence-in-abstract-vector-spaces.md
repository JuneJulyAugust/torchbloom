# Linear Independence in Abstract Vector Spaces

Source: https://www.mathacademy.com/topics/1908?courseId=55
Topic ID: 1908

## Prerequisites

- [Linear Dependence and Independence](./1861-linear-dependence-and-independence.md)
- [Defining Abstract Vector Spaces](./3835-defining-abstract-vector-spaces.md)

## Lesson

### Introduction

The set of vectors $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \}$ in an abstract vector space $V$ is **linearly dependent** if there exist real scalars $x_1,x_2,\ldots,x_n$ not all zero such that

$$


x_1\mathbf{v}_1+x_2\mathbf{v}_2+\ldots+x_n\mathbf{v}_n=\mathbf{0}.


$$

Otherwise, if $x_1 = x_2 = \cdots = x_n = 0$ is the only solution, the set is **linearly independent**.

Let's consider some examples.

- First, let's consider the vector space $\mathbb{R}[t]$ of all polynomials in variable $t,$ along with the set To determine whether $S$ is linearly dependent in $\mathbb{R}[t],$ we must solve the equation Substituting the given expressions for $p_1(t),p_2(t)$ and $p_3(t)$ into the above equation, we obtain The final equation is true for every $t$ if and only if Since $x_1 = x_2 = x_3 = 0$ is the only solution, $S$ is linearly independent in $\mathbb R[t].$

- Let's consider the vector space $\mathbb R[t]$ once more, along with the set To determine whether $T$ is linearly dependent in $\mathbb{R}[t],$ we must solve the equation The final equation is true for every $t$ if and only if This system has the nonzero solution $(x_1,x_2)=(2,1).$ As a result, we get Therefore, the set $\big\{q_1(t), q_2(t) \big\}$ is linearly dependent in $\mathbb R[t].$

### Example: Finding the Coefficients That Show Linear Dependence Among Polynomial Vectors

#### Question

Consider the set $\big\{p_1(t), p_2(t),p_3(t) \big\}$ of polynomials from $\mathbb{R}[t],$ where

$$


p_1(t)=1+t, \qquad p_2(t)=-2t-4, \qquad p_3(t)=-2t-3.


$$

If the set is linearly dependent, find the value of $\dfrac{x_2}{x_1}$ from a non-zero solution of $x_1 \cdot p_1(t)+x_2 \cdot p_2(t) + x_3 \cdot p_3(t)=0.$

#### Explanation

If the set is linearly dependent, then there exist $x_1,x_2,x_3$ not all zero such that

$$


x_1p_1(t)+x_2p_2(t)+x_3p_3(t)=0.


$$

Otherwise, if $x_1 = x_2 = x_3 = 0,$ the set is linearly independent.

Substituting the given expressions for $p_1(t),p_2(t),$ and $p_3(t)$ into the above equation, we obtain

$$


\begin{aligned}𝑥_{1}(1+𝑡)+𝑥_{2}(−2𝑡−4)+𝑥_{3}(−2𝑡−3) & =0 \\ (𝑥_{1}−4𝑥_{2}−3𝑥_{3})+(𝑥_{1}−2𝑥_{2}−2𝑥_{3})𝑡 & =0.\end{aligned}


$$

The final equation is true for every $t$ if and only if

$$


\begin{aligned}𝑥_{1}−4𝑥_{2}−3𝑥_{3}=0 \\ 𝑥_{1}−2𝑥_{2}−2𝑥_{3}=0.\end{aligned}


$$

Now, we consider the corresponding augmented matrix and reduce it to row echelon form using Gaussian elimination:

$$


\begin{aligned}𝑀 & =[\begin{aligned}1 & −4 & −3 & 0 \\ 1 & −2 & −2 & 0\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+(−1)𝑅_{1} \\ & ∼[\begin{aligned}1 & −4 & −3 & 0 \\ 0 & 2 & 1 & 0\end{aligned}]. & & \end{aligned}


$$

The pivot columns are the $1$st and $2$nd. Hence, $x_3$ is a free variable. The system is now

$$


\begin{aligned}𝑥_{1}−4𝑥_{2}−3𝑥_{3}=0 \\ 2𝑥_{2}+𝑥_{3}=0.\end{aligned}


$$

From the second equation, we get $x_2=-\dfrac 12x_3.$ Substituting this into the first equation, we get

$$


x_1-4\left(-\dfrac 12x_3\right)-3x_3=0 \qquad\Longrightarrow \qquad x_1=x_3.


$$

Therefore, the general solution is

$$


\begin{aligned}𝑥_{1} \\ 𝑥_{2} \\ 𝑥_{3}\end{aligned}


$$

Finally, for any $x_3 \neq 0,$ we obtain

$$


\dfrac{x_2}{x_1}=\dfrac{\left( -\dfrac 12x_3\right)}{x_3}=-\dfrac 12.


$$

### Example: Finding the Coefficients That Show Linear Dependence Among Matrix Vectors

#### Question

Consider the set of matrices $\big\{A, B \big\},$ where

$$


[\begin{aligned}1 & 0 \\ −2 & 4\end{aligned}]


$$

If the set is linearly dependent, find the value of $\dfrac{x_1}{x_2}$ from a non-zero solution of $x_1A+x_2B=O,$ where $O$ is the $2 \times 2$ zero-matrix.

#### Explanation

If the set is linearly dependent, then there exist $x_1,x_2$ not both zero such that

$$


x_1A+x_2B=O.


$$

Otherwise, if $x_1 = x_2 = 0,$ the set is linearly independent.

Substituting the matrices $A$ and $B$ into the above equation, we obtain

$$


\begin{aligned}𝑥_{1}[\begin{aligned}1 & 0 \\ −2 & 4\end{aligned}]+𝑥_{2}[\begin{aligned}3 & 5 \\ 2 & −6\end{aligned}] & =[\begin{aligned}0 & 0 \\ 0 & 0\end{aligned}] \\ [\begin{aligned}𝑥_{1} & 0 \\ −2𝑥_{1} & 4𝑥_{1}\end{aligned}]+[\begin{aligned}3𝑥_{2} & 5𝑥_{2} \\ 2𝑥_{2} & −6𝑥_{2}\end{aligned}] & =[\begin{aligned}0 & 0 \\ 0 & 0\end{aligned}] \\ [\begin{aligned}𝑥_{1}+3𝑥_{2} & 5𝑥_{2} \\ −2𝑥_{1}+2𝑥_{2} & 4𝑥_{1}−6𝑥_{2}\end{aligned}] & =[\begin{aligned}0 & 0 \\ 0 & 0\end{aligned}].\end{aligned}


$$

Equating the corresponding entries, we obtain the following system of equations:

$$


\begin{aligned}𝑥_{1}+3𝑥_{2}=0 \\ 5𝑥_{2}=0 \\ −2𝑥_{1}+2𝑥_{2}=0 \\ 4𝑥_{1}−6𝑥_{2}=0.\end{aligned}


$$

Now, we consider the corresponding augmented matrix and reduce it to row echelon form using Gaussian elimination:

$$


\begin{aligned}𝑀 & =\begin{aligned}1 & 3 & 0 \\ 0 & 5 & 0 \\ −2 & 2 & 0 \\ 4 & −6 & 0\end{aligned} & & \begin{aligned}𝑅_{3}:=𝑅_{3}+2𝑅_{1} \\ 𝑅_{4}:=𝑅_{4}+(−4)𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}1 & 3 & 0 \\ 0 & 5 & 0 \\ 0 & 8 & 0 \\ 0 & −18 & 0\end{aligned} & & \begin{aligned}𝑅_{3}:=𝑅_{3}+(−\frac{8}{5})𝑅_{2} \\ 𝑅_{4}:=𝑅_{4}+\frac{18}{5}𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}1 & 3 & 0 \\ 0 & 5 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

The pivot columns are the $1$st and $2$nd columns. Therefore, we get the system

$$


\begin{aligned}𝑥_{1}+3𝑥_{2}=0 \\ 5𝑥_{2}=0,\end{aligned}


$$

which has only the zero solution $x_1=x_2=0.$

Consequently, $\big\{A, B \big\}$ is linearly independent.

### An Important Property of Linearly Dependent Sets

Note the following important property of linearly dependent sets.

*A set of vectors is linearly dependent if and only if it contains a vector that is a linear combination of **** vectors from that set.*

To see why this is true, let $\{\mathbf{v}_1, \mathbf{v}_2,\cdots, \mathbf{v}_n\}$ be a linearly dependent set of $n$ vectors. This means that the equation

$$


x_1\mathbf{v}_1 + x_2 \mathbf{v}_2 + \cdots + x_n\mathbf{v}_n = \mathbf{0}


$$

has a non-trivial solution, i.e. a solution in which at least one of the coefficients $x_1, x_2, \ldots, x_n$ is not zero. Without loss of generality, we may assume that $x_1 \ne 0,$ and we can rewrite the above equation as

$$


\mathbf{v}_1 = -\dfrac{x_2}{x_1} \mathbf{v}_2 - \dfrac{x_3}{x_1}\mathbf{v}_3 - \cdots - \dfrac{x_n}{x_1}\mathbf{v}_n.


$$

The above argument shows that the vector $\mathbf{v}_1$ can be written as a linear combination of the other vectors from the set.

### Example: Determining if a Given Set Is Linearly Independent Given Information on Its Elements

#### Question

Consider a vector space $V$ and vectors $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3 \in V.$ Given that $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is linearly independent, which of the following statements are true?

1. $\{4\mathbf{v}_1, 5\mathbf{v}_2, \mathbf{v}_3\}$ is linearly independent

2. $\{\mathbf{0}, \mathbf{v}_1, 2\mathbf{v}_2 \}$ is linearly independent

3. $\{\mathbf{v}_2, \mathbf{v}_3 \}$ is linearly independent

#### Explanation

Let's examine each of the given options in turn.

- Statement I is true. Suppose that which, in turn, gives Since $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is a linearly independent set, the final equation can be true only if The unique solution of the system is $x_1=x_2=x_3=0,$ which means that is linearly independent.

- Statement II is false. Indeed, notice that As a result, $x_1\mathbf{0}+x_2\mathbf{v}_1+x_3(2\mathbf{v}_2)=\mathbf{0}$ has a non-zero solution. This means that $\{\mathbf{0}, \mathbf{v}_1, 2\mathbf{v}_2 \}$ is linearly dependent. In general, any set containing the zero vector is linearly dependent.

- Statement III is true. Indeed, $x_1\mathbf{v}_2+x_2\mathbf{v}_3=\mathbf{0}$ must have only the zero solution $x_1=x_2=0.$ If this equation has a non-zero solution, $a \cdot \mathbf{v}_2 + b \cdot \mathbf{v}_3=\mathbf{0},$ then we obtain which would mean that $\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ is linearly dependent.

Therefore, the correct answer is "I and III only."
