# The Least-Squares Solution of a Linear System (With Collinearity)

Source: https://www.mathacademy.com/topics/2167?courseId=155
Topic ID: 2167

## Prerequisites

- [The Least-Squares Solution of a Linear System (Without Collinearity)](./2166-the-least-squares-solution-of-a-linear-system-without-collinearity.md)

## Lesson

### Introduction

Let's consider the following inconsistent system of equations:

$$


[\begin{aligned}1 & −4 \\ −2 & 8\end{aligned}]


$$

Since the system is inconsistent, we cannot find an exact solution. However, as we've previously seen, we can attempt to find the so-called least-squares solution, which is a vector ${\hat{\mathbf{x}}}$ such that

$$


\| A{\hat{\mathbf{x}}} - \mathbf{b} \|


$$

is as small as possible.

As before, the least-squares solution can be found by solving the corresponding normal equation, given by

$$


\begin{aligned}𝐴^{𝑇}\,𝐴\overset{𝐱}{^} & =𝐴^{𝑇}𝐛.\end{aligned}


$$

Now, note the following:

- Previously, we solved the normal equation by left-multiplying the normal equation by $(A^T A)^{-1}.$

- However, in this case, the second column of $A$ is a multiple of the first.

- So, the columns of $A$ are linearly dependent.

- Therefore, $A^T A$ is not invertible.

To solve the normal equation in this case, we proceed as follows:

$$


\begin{aligned}𝐴^{𝑇}\,𝐴\overset{𝐱}{^} & =𝐴^{𝑇}𝐛 \\ [\begin{aligned}1 & −2 \\ −4 & 8\end{aligned}][\begin{aligned}1 & −4 \\ −2 & 8\end{aligned}][\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}1 & −2 \\ −4 & 8\end{aligned}][\begin{aligned}1 \\ 3\end{aligned}] \\ [\begin{aligned}5 & −20 \\ −20 & 80\end{aligned}][\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}−5 \\ 20\end{aligned}]\end{aligned}


$$

Solving the last equation by Gaussian elimination, we obtain the general solution

$$


[\begin{aligned}−1+4𝑥_{2} \\ 𝑥_{2}\end{aligned}]


$$

Notice that our solution is not unique! The second term of the least-squares solution (highlighted in blue) represents vectors from the null space of $A.$

In general, if a matrix $A$ has collinear columns, then the least-squares solution to $A\mathbf x = \mathbf b$ is not unique.

### Example: Constructing the Normal Equation Corresponding to a Linear System

#### Question

$$


\begin{aligned}4𝑥_{1}−3𝑥_{2}−𝑥_{3}=4 \\ 8𝑥_{1}−6𝑥_{2}−2𝑥_{3}=2\end{aligned}


$$

Consider the system of linear equations and its corresponding normal equation shown above. What is the value of $a-b+c?$

#### Explanation

First, we write our system in matrix form as

$$


[\begin{aligned}4 & −3 & −1 \\ 8 & −6 & −2\end{aligned}]


$$

The normal equation corresponding to $A\mathbf{x}=\mathbf{b}$ is given by

$$


\begin{aligned}𝐴^{𝑇}\,𝐴𝐱 & =𝐴^{𝑇}𝐛 \\ \begin{aligned}4 & 8 \\ −3 & −6 \\ −1 & −2\end{aligned}[\begin{aligned}4 & −3 & −1 \\ 8 & −6 & −2\end{aligned}]𝐱 & =\begin{aligned}4 & 8 \\ −3 & −6 \\ −1 & −2\end{aligned}[\begin{aligned}4 \\ 2\end{aligned}] \\ \begin{aligned}80 & −60 & −20 \\ −60 & 45 & 15 \\ −20 & 15 & 5\end{aligned}𝐱 & =\begin{aligned}32 \\ −24 \\ −8\end{aligned}.\end{aligned}


$$

Therefore, we have

$$


a-b+c=(-20)-(-24)+(-20) = -16.


$$

### Example: Finding the Least-Squares Solution of a Linear System Given in Matrix Form with Collinearity

#### Question

$$


\begin{aligned}1 & −3 \\ −1 & 3 \\ 2 & −6\end{aligned}


$$

Consider the matrix $A$ and vector $\mathbf{b}$ shown above. Find the general least-squares solution of the system $A\mathbf{x}=\mathbf{b}.$

#### Explanation

The least-squares solution of $A\mathbf{x}=\mathbf{b}$ satisfies the corresponding normal equation:

$$


A^T \! A\mathbf{x} = A^T\mathbf{b}


$$

Notice that the columns of $A$ are linearly dependent. So first, let's write down the normal equation in matrix form:

$$


\begin{aligned}[\begin{aligned}1 & −1 & 2 \\ −3 & 3 & −6\end{aligned}]\begin{aligned}1 & −3 \\ −1 & 3 \\ 2 & −6\end{aligned}[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}1 & −1 & 2 \\ −3 & 3 & −6\end{aligned}]\begin{aligned}1 \\ 3 \\ −1\end{aligned} \\ [\begin{aligned}6 & −18 \\ −18 & 54\end{aligned}][\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}−4 \\ 12\end{aligned}]\end{aligned}


$$

Now, we solve the system corresponding to the above matrix equation using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{aligned}6 & −18 & −4 \\ −18 & 54 & 12\end{aligned}] & 𝑅_{2}:=𝑅_{2}+3𝑅_{1} \\ & ∼[\begin{aligned}6 & −18 & −4 \\ 0 & 0 & 0\end{aligned}] & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). Thus, $x_2$ is a free variable. From the first equation, we have

$$


x_1=-\dfrac{2}{3}+3x_2.


$$

Hence, the general solution is

$$


\begin{aligned}−\frac{2}{3}+3𝑥_{2} \\ 𝑥_{2}\end{aligned}


$$

### Example: Finding the Least-Squares Solution of a Linear System With Collinearity

#### Question

$$


\begin{aligned}−𝑥_{1}+4𝑥_{2}=1 \\ 2𝑥_{1}−8𝑥_{2}=1 \\ −2𝑥_{1}+8𝑥_{2}=−1\end{aligned}


$$

Consider the system of linear equations shown above. Find the general least-squares solution of the system $A \mathbf x = \mathbf b.$

#### Explanation

First, we write our system in matrix form as $A\mathbf{x}=\mathbf{b},$ where

$$


\begin{aligned}−1 & 4 \\ 2 & −8 \\ −2 & 8\end{aligned}


$$

The least-squares solution of $A\mathbf{x}=\mathbf{b}$ satisfies the corresponding normal equation:

$$


A^T \! A\mathbf{x} = A^T\mathbf{b}


$$

Notice that the columns of $A$ are linearly dependent. So first, let's write down the normal equation in matrix form:

$$


\begin{aligned}[\begin{aligned}−1 & 2 & −2 \\ 4 & −8 & 8\end{aligned}]\begin{aligned}−1 & 4 \\ 2 & −8 \\ −2 & 8\end{aligned}[\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}−1 & 2 & −2 \\ 4 & −8 & 8\end{aligned}]\begin{aligned}1 \\ 1 \\ −1\end{aligned} \\ [\begin{aligned}9 & −36 \\ −36 & 144\end{aligned}][\begin{aligned}𝑥_{1} \\ 𝑥_{2}\end{aligned}] & =[\begin{aligned}3 \\ −12\end{aligned}]\end{aligned}


$$

Now, we solve the system corresponding to the final matrix equation using Gaussian elimination, as follows:

$$


\begin{aligned}𝑀 & =[\begin{aligned}9 & −36 & 3 \\ −36 & 144 & −12\end{aligned}] & & \begin{aligned}𝑅_{2}:=𝑅_{2}+4𝑅_{1}\end{aligned} \\ & ∼[\begin{aligned}9 & −36 & 3 \\ 0 & 0 & 0\end{aligned}] & & \end{aligned}


$$

The reduced matrix above has one pivot column (the $1$st one). Thus, $x_2$ is a free variable. From the first equation, we have

$$


x_1=\dfrac{1}{3}+ 4x_2.


$$

Hence, the general solution is

$$


\begin{aligned}\frac{1}{3}+4𝑥_{2} \\ 𝑥_{2}\end{aligned}


$$
