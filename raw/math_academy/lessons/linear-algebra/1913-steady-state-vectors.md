# Steady-State Vectors

Source: https://www.mathacademy.com/topics/1913?courseId=55
Topic ID: 1913

## Prerequisites

- [Limits of Sequences](../ap-calculus-bc/1087-limits-of-sequences.md)
- [Solving 3x3 Singular Systems of Equations Using Gaussian Elimination](./1374-solving-3x3-singular-systems-of-equations-using-gaussian-elimination.md)
- [Markov Chains](./1911-markov-chains.md)

## Lesson

### Introduction

Suppose we have a population where people live either in the city or the countryside. A study carried out by the local authority shows that, each year,

- $6\%$ of the city population relocates to the countryside,

- $3\%$ of the countryside population relocates to the city, and

- everyone else remains where they are.

Additionally, $70\%$ of the population lived in the city and $30\%$ in the countryside at the time of the study.

We can represent this situation using a stochastic matrix $P$ and initial state vector $\mathbf x_0,$ as follows:

$$


[\begin{aligned}0.94 & 0.03 \\ 0.06 & 0.97\end{aligned}]


$$

As we've seen, to find the state vector $\mathbf x_{k+1}$ that corresponds to the $(k+1)$th year, we left-multiply the state vector corresponding to the $k$th year by $P.$ This gives rise to the following Markov chain:

$$


\begin{aligned}𝐱_{1} & =𝑃𝐱_{0}, \\ 𝐱_{2} & =𝑃𝐱_{1}, \\ 𝐱_{3} & =𝑃𝐱_{2}, \\ ⋮ & \,⋮ \\ 𝐱_{𝑘+1} & =𝑃𝐱_{𝑘} \\ ⋮ & \,⋮\end{aligned}


$$

The local authority wants to determine whether the state vectors settle down to a fixed state. With the aid of a computer, they compute the following states:

$$


\begin{aligned}𝐱_{1} & =𝑃𝐱_{0}=[\begin{aligned}0.667 \\ 0.333\end{aligned}] \\ 𝐱_{2} & =𝑃𝐱_{1}=[\begin{aligned}0.636\,97 \\ 0.363\,03\end{aligned}] \\ 𝐱_{3} & =𝑃𝐱_{2}=[\begin{aligned}0.609\,64 \\ 0.390\,36\end{aligned}] \\ & =⋮ \\ 𝐱_{100} & =𝑃𝐱_{99}=[\begin{aligned}0.333\,363 \\ 0.666\,637\end{aligned}]≈\begin{aligned}\frac{1}{3} \\ \frac{2}{3}\end{aligned} \\ 𝐱_{101} & =𝑃𝐱_{100}=[\begin{aligned}0.333\,36 \\ 0.666\,64\end{aligned}]≈\begin{aligned}\frac{1}{3} \\ \frac{2}{3}\end{aligned}\end{aligned}


$$

Looking at the data, we see that the vectors $\mathbf x_{100}$ and $\mathbf x_{101}$ are both approximately equal to the vector

$$


\begin{aligned}\frac{1}{3} \\ \frac{2}{3}\end{aligned}


$$

Furthermore, computing $\mathbf x_{102}, \mathbf{x}_{103}, \ldots$ all give vectors approximately equal to $\mathbf q.$ This suggests that the sequence $\mathbf x_k$ converges to $\mathbf q\mathbin{:}$

$$


x_k \rightarrow \mathbf q \quad\textrm{as}\quad k\to\infty.


$$

The vector $\mathbf q$ is called a **steady-state vector** of the matrix $P.$ Here, our steady-state vector suggests that after enough time has passed, one-third of the population will live in the city and two-thirds will live in the countryside.

Finally, notice that for large values of $k,$ we have

$$


P\mathbf x_k \approx \mathbf x_{k}.


$$

This observation indicates how to find $\mathbf q$ without resorting to computers.

### Steady-State Vectors

Suppose we have a stochastic matrix $P$ and a stochastic vector $\mathbf{q}.$ Then, $\mathbf{q}$ is a **steady-state vector** of $P$ if

$$


P\mathbf{q} = \mathbf{q}.


$$

For example, to show that the stochastic vector

$$


\begin{aligned}\frac{1}{3} \\ \frac{2}{3}\end{aligned}


$$

is a steady-state vector for the stochastic matrix

$$


[\begin{aligned}0.94 & 0.03 \\ 0.06 & 0.97\end{aligned}]


$$

we compute the matrix product $P\mathbf q\mathbin:$

$$


\begin{aligned}𝑃𝐪 & =[\begin{aligned}0.94 & 0.03 \\ 0.06 & 0.97\end{aligned}]⋅\begin{aligned}\frac{1}{3} \\ \frac{2}{3}\end{aligned} \\ & =\frac{1}{3}⋅[\begin{aligned}0.94 & 0.03 \\ 0.06 & 0.97\end{aligned}]⋅[\begin{aligned}1 \\ 2\end{aligned}] \\ & =\frac{1}{3}⋅[\begin{aligned}0.94+2⋅0.03 \\ 0.06+2⋅0.97\end{aligned}] \\ & =\frac{1}{3}⋅[\begin{aligned}1 \\ 2\end{aligned}] \\ & =\begin{aligned}\frac{1}{3} \\ \frac{2}{3}\end{aligned} \\ & =𝐪\,✓\end{aligned}


$$

Since $P\mathbf q = \mathbf q,$ the vector $\mathbf q$ is a steady-state vector of $P.$

### Example: Identifying Steady-State Vectors of Stochastic Matrices

#### Question

$$


[\begin{aligned}0.4 & 0.2 \\ 0.6 & 0.8\end{aligned}]


$$

Consider the stochastic matrix $P$ and vector $\mathbf{q}$ shown above. Which of the following statements are true?

1. $\mathbf{q}$ is a stochastic vector

2. $P\mathbf{q} = \mathbf{q}$

3. $\mathbf{q}$ is a steady-state vector of $P$

#### Explanation

Recall that a steady-state vector of a stochastic matrix $P$ is a stochastic vector $\mathbf{q}$ such that $P\mathbf{q} = \mathbf{q}.$

With that in mind, let's examine our statements.

- Statement I is true. Indeed, $\mathbf{q}$ is a stochastic vector since its entries are non-negative and add up to $1.$

- Statement II is true. Indeed, we have

- Statement III is true. Indeed, $\mathbf{q}$ is a stochastic vector such that $P\mathbf{q}=\mathbf{q}.$ So, it's a steady-state vector of $P.$

Therefore, the correct answer is "I, II, and III."

### Finding the Steady-State Vector of a Stochastic Matrix

To find a steady-state vector of a stochastic matrix $P,$ we seek a stochastic vector $\mathbf{q}$ such that

$$


P\mathbf{q} = \mathbf{q}.


$$

Let's begin by writing this equation in a slightly different form:

$$


\begin{aligned}𝑃𝐪 & =𝐪 \\ 𝑃𝐪−𝐪 & =𝟎 \\ 𝑃𝐪−𝐼𝐪 & =𝟎 \\ (𝑃−𝐼)𝐪 & =𝟎\end{aligned}


$$

Therefore, the vector we seek is a solution to the matrix equation $(P-I)\mathbf{q} = \mathbf{0}.$

Let's use this idea to find a steady-state vector for the matrix

$$


[\begin{aligned}0.25 & 0.5 \\ 0.75 & 0.5\end{aligned}]


$$

First, we compute $(P-I):$

$$


[\begin{aligned}0.25 & 0.5 \\ 0.75 & 0.5\end{aligned}]


$$

Then, to solve $(P-I)\mathbf{q} = \mathbf{0},$ we reduce the augmented matrix $M$ to row echelon form using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{aligned}−0.75 & 0.5 & 0 \\ 0.75 & −0.5 & 0\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+𝑅_{1} \\ & ∼[\begin{aligned}−0.75 & 0.5 & 0 \\ 0 & 0 & 0\end{aligned}] & & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). Thus, $x_2$ is a free variable. From the first equation, we obtain

$$


x_1= \dfrac 23 x_2.


$$

Hence, the general solution is

$$


\begin{aligned}\frac{2}{3}𝑥_{2} \\ 𝑥_{2}\end{aligned}


$$

Since the steady-state vector must be stochastic, its entries should add up to $1.$ Therefore, we have

$$


\begin{aligned}\frac{2}{3}𝑥_{2}+𝑥_{2} & =1 \\ \frac{5}{3}𝑥_{2} & =1 \\ 𝑥_{2} & =\frac{3}{5}.\end{aligned}


$$

Finally, our steady-state vector is

$$


\begin{aligned}\frac{2}{5} \\ \frac{3}{5}\end{aligned}


$$

### Regular Stochastic Matrices

A stochastic matrix $P$ is **regular** if there exists a positive integer $n$ such that $P^n$ has all positive elements.

Let's consider some examples:

- The stochastic matrix $P,$ given by has all positive elements. Therefore, it is a regular stochastic matrix.

- The stochastic matrix $Q,$ given by contains a zero element. However, if we compute its square, we get which has all positive elements. Therefore, $Q$ is a regular stochastic matrix.

Regular stochastic matrices have the following important property:

*Any regular stochastic matrix has a **** steady-state vector $\mathbf q.$ Moreover, the Markov chain converges to $\mathbf q$ for **** initial state $\mathbf x_0.$*

### Example: Finding the Steady-State Vector of a Stochastic 2x2 Matrix

#### Question

The table below describes how the customers of a particular electronics store feel about their next computer purchase.

It is found that $10 \%$ of customers who currently use a laptop would choose a desktop on their next purchase, while $80 \%$ of customers who currently use a desktop would choose a laptop on their next purchase.

Given that the store has $5\,400$ customers, all of whom purchase a new computer every two years, how many customers would eventually own a desktop computer if the given probabilities remain constant over many two-year periods?

#### Explanation

From the table, we get the corresponding stochastic matrix

$$


[\begin{aligned}0.9 & 0.8 \\ 0.1 & 0.2\end{aligned}]


$$

Notice that $P$ contains only positive entries. So, the matrix $P$ is regular. As a result, after many two-year periods, the distribution will eventually converge to the unique steady-state vector of $P,$ and this convergence does not depend on the initial state.

Recall that a steady-state vector of a stochastic matrix $P$ is a stochastic vector $\mathbf{q}$ such that

$$


\begin{aligned}𝑃𝐪=𝐪\,⟹\,(𝑃−𝐼)𝐪=𝟎.\end{aligned}


$$

Computing $P-I,$ we get

$$


[\begin{aligned}0.9 & 0.8 \\ 0.1 & 0.2\end{aligned}]


$$

So, the matrix equation $(P-I)\mathbf{q} = \mathbf{0}$ is equivalent to the system of linear equations with the augmented matrix $M,$ which we reduce to row echelon form using Gaussian elimination as follows:

$$


\begin{aligned}𝑀 & =[\begin{aligned}−0.1 & 0.8 & 0 \\ 0.1 & −0.8 & 0\end{aligned}] & 𝑅_{2} & :=𝑅_{2}+𝑅_{1} \\ & ∼[\begin{aligned}−0.1 & 0.8 & 0 \\ 0 & 0 & 0\end{aligned}] & & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). Thus, $x_2$ is a free variable. From the first equation, we obtain

$$


\begin{aligned}𝑥_{1}=8𝑥_{2}.\end{aligned}


$$

Hence, the general solution is

$$


[\begin{aligned}8𝑥_{2} \\ 𝑥_{2}\end{aligned}]


$$

Since the steady-state vector must be stochastic, its entries should add up to $1.$ Therefore, we have

$$


\begin{aligned}8𝑥_{2}+𝑥_{2} & =1 \\ 9𝑥_{2} & =1 \\ 𝑥_{2} & =\frac{1}{9}.\end{aligned}


$$

Our steady-state vector is

$$


\begin{aligned}\frac{8}{9} \\ \frac{1}{9}\end{aligned}


$$

So, ${\color{blue}{\dfrac{1}{9}}}$ of the $5\,400$ customers would eventually own a desktop computer. Therefore, the total number of people who would eventually own a desktop computer is

$$


\dfrac{1}{9} \cdot 5\,400 = 600.


$$

### Example: Finding the Steady-State Vector of a Stochastic 3x3 Matrix

#### Question

$$


\begin{aligned}0.1 & 0.3 & 0.5 \\ 0.2 & 0.3 & 0.1 \\ 0.7 & 0.4 & 0.4\end{aligned}


$$

Find the steady-state vector $\mathbf q$ of the stochastic matrix $P$ shown above.

#### Explanation

Recall that a steady-state vector of a stochastic matrix $P$ is a stochastic vector $\mathbf{q}$ such that

$$


\begin{aligned}𝑃𝐪 & =𝐪 \\ 𝑃𝐪−𝐪 & =𝟎 \\ 𝑃𝐪−𝐼𝐪 & =𝟎 \\ (𝑃−𝐼)𝐪 & =𝟎.\end{aligned}


$$

Computing $P-I,$ we get

$$


\begin{aligned}0.1 & 0.3 & 0.5 \\ 0.2 & 0.3 & 0.1 \\ 0.7 & 0.4 & 0.4\end{aligned}


$$

The matrix equation $(P-I)\mathbf{q} = \mathbf{0}$ is equivalent to the system of linear equations with the augmented matrix $M,$ which we reduce to row echelon form using Gaussian elimination as follows:

$$


\begin{aligned}𝑀 & =\begin{aligned}−0.9 & 0.3 & 0.5 & 0 \\ 0.2 & −0.7 & 0.1 & 0 \\ 0.7 & 0.4 & −0.6 & 0\end{aligned} & & \begin{aligned}𝑅_{1}:=20𝑅_{1} \\ 𝑅_{2}:=10𝑅_{2} \\ 𝑅_{3}:=20𝑅_{3}\end{aligned} \\ & ∼\begin{aligned}−18 & 6 & 10 & 0 \\ 2 & −7 & 1 & 0 \\ 14 & 8 & −12 & 0\end{aligned} & & \begin{aligned}𝑅_{2}↔𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}2 & −7 & 1 & 0 \\ −18 & 6 & 10 & 0 \\ 14 & 8 & −12 & 0\end{aligned} & & \begin{aligned}𝑅_{2}:=𝑅_{2}+9𝑅_{1} \\ 𝑅_{3}:=𝑅_{3}−7𝑅_{1}\end{aligned} \\ & ∼\begin{aligned}2 & −7 & 1 & 0 \\ 0 & −57 & 19 & 0 \\ 0 & 57 & −19 & 0\end{aligned} & & \begin{aligned}𝑅_{3}:=𝑅_{3}+𝑅_{2}\end{aligned} \\ & ∼\begin{aligned}2 & −7 & 1 & 0 \\ 0 & −57 & 19 & 0 \\ 0 & 0 & 0 & 0\end{aligned} & & \end{aligned}


$$

The reduced matrix above has two pivot columns (the $1$st and $2$nd). Thus, $x_3$ is a free variable. From the second equation, we obtain

$$


x_2=\dfrac{1}{3}x_3.


$$

Substituting this into the first equation, we obtain

$$


2x_1 -7\left(\dfrac{1}{3}x_3\right) + x_3 = 0 \qquad \Longrightarrow\qquad x_1 = \dfrac{2}{3}x_3.


$$

Hence, the general solution is

$$


\begin{aligned}\frac{2}{3}𝑥_{3} \\ \frac{1}{3}𝑥_{3} \\ 𝑥_{3}\end{aligned}


$$

Since the steady-state vector must be stochastic, its entries should add up to $1.$ Therefore, we have

$$


\begin{aligned}\frac{2}{3}𝑥_{3}+\frac{1}{3}𝑥_{3}+𝑥_{3} & =1 \\ 2𝑥_{3} & =1 \\ 𝑥_{3} & =\frac{1}{2}.\end{aligned}


$$

Finally, our steady-state vector is

$$


\begin{aligned}\frac{1}{3} \\ \frac{1}{6} \\ \frac{1}{2}\end{aligned}


$$
