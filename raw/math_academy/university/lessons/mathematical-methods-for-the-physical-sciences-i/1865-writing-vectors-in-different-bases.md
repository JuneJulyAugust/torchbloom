# Writing Vectors in Different Bases

Source: https://www.mathacademy.com/topics/1865?courseId=154
Topic ID: 1865

## Prerequisites

- [Expressing the Coordinates of a Vector in a Given Basis](./1864-expressing-the-coordinates-of-a-vector-in-a-given-basis.md)

## Lesson

### Introduction

Let's consider the basis $\mathcal{C}= \left\{\mathbf{c}_1, \mathbf{c}_2 \right\}$ of $\mathbb{R}^2$ and the vector

$$


[\begin{aligned}2 \\ −1\end{aligned}]


$$

Now, let $\mathcal{B}= \left\{\mathbf{b}_1, \mathbf{b}_2 \right\}$ be another basis of $\mathbb{R}^2,$ such that

$$


\mathbf{b}_1 = \mathbf{c}_2 \quad \textrm{and} \quad \mathbf{b}_2 = -2\mathbf{c}_1.


$$

How can we find the coordinates of $\mathbf{x}$ relative to the basis $\mathcal{B}?$

Since $[\begin{aligned}2 \\ −1\end{aligned}]$ we can write the vector $\mathbf{x}$ relative to the basis $\mathcal B$ as follows:

$$


\begin{aligned}𝐱 & =2𝐜_{1}−𝐜_{2} \\ & =−𝐜_{2}+2𝐜_{1} \\ & =−(𝐜_{2})−(−2𝐜_{1}) \\ & =−𝐛_{1}−𝐛_{2}\end{aligned}


$$

Therefore, $[\begin{aligned}−1 \\ −1\end{aligned}]$

### Example: Writing a Two-Dimensional Vector in a Different Basis

#### Question

Let $\mathcal{B}= \left\{\mathbf{b}_1, \mathbf{b}_2 \right\}$ be a basis of $\mathbb{R}^2$ and $[\begin{aligned}5 \\ −2\end{aligned}]$ What are the coordinates of $\mathbf{x}$ relative to the basis $\mathcal{C}= \left\{\mathbf{c}_1, \mathbf{c}_2 \right\},$ where $\mathbf{c}_1 = -\mathbf{b}_2$ and $\mathbf{c}_2 = -3\mathbf{b}_1?$

#### Explanation

Since $[\begin{aligned}5 \\ −2\end{aligned}]$ we can write $\mathbf{x}$ in terms of the vectors $\mathbf c_1$ and $\mathbf c_2,$ as follows:

$$


\begin{aligned}𝐱 & =5𝐛_{1}−2𝐛_{2} \\ & =−2𝐛_{2}+5𝐛_{1} \\ & =2(−𝐛_{2})−\frac{5}{3}(−3𝐛_{1}) \\ & =2𝐜_{1}−\frac{5}{3}𝐜_{2}\end{aligned}


$$

Therefore, $\begin{aligned}2 \\ −\frac{5}{3}\end{aligned}$

### Example: Writing a Three-Dimensional Vector in a Different Basis

#### Question

Let $\mathcal{B}= \left\{\mathbf{b}_1, \mathbf{b}_2,\mathbf{b}_3 \right\}$ be a basis of $\mathbb{R}^3$ and $\begin{aligned}−2 \\ −3 \\ 5\end{aligned}$ What are the coordinates of $\mathbf{x}$ relative to the basis $\mathcal{C}= \left\{\mathbf{c}_1, \mathbf{c}_2, \mathbf{c}_3 \right\},$ where $\mathbf{c}_1 = -3\mathbf{b}_2,$ $\mathbf{c}_2=-\mathbf{b}_3,$ and $\mathbf{c}_3 = -4\mathbf{b}_1?$

#### Explanation

Since $\begin{aligned}−2 \\ −3 \\ 5\end{aligned}$ we can write $\mathbf{x}$ in terms of the vectors $\mathbf c_1, \mathbf c_2,$ and $\mathbf c_3,$ as follows:

$$


\begin{aligned}𝐱 & =−2𝐛_{1}−3𝐛_{2}+5𝐛_{3} \\ & =−3𝐛_{2}+5𝐛_{3}−2𝐛_{1} \\ & =(−3𝐛_{2})−5(−𝐛_{3})+\frac{1}{2}(−4𝐛_{1}) \\ & =𝐜_{1}−5𝐜_{2}+\frac{1}{2}𝐜_{3}\end{aligned}


$$

Therefore, $\begin{aligned}1 \\ −5 \\ \frac{1}{2}\end{aligned}$

### Writing a Vector in a Different Basis Given a Linear Relationship Between Two Bases

Let $\mathcal{B}= \left\{\mathbf{b}_1, \mathbf{b}_2 \right\}$ be a basis of $\mathbb{R}^2$ and $[\begin{aligned}5 \\ −2\end{aligned}]$ What are the coordinates of $\mathbf{x}$ relative to the basis $\mathcal{C}= \left\{\mathbf{c}_1, \mathbf{c}_2 \right\},$ where $\mathbf{b}_1 = 2\mathbf{c}_1-\mathbf{c}_2$ and $\mathbf{b}_2 = \mathbf{c}_1+\mathbf{c}_2?$

Since $[\begin{aligned}5 \\ −2\end{aligned}]$ we can write the vector $\mathbf{x}$ in terms of the vectors $\mathbf c_1$ and $\mathbf c_2,$ as follows:

$$


\begin{aligned}𝐱 & =5𝐛_{𝟏}−2𝐛_{𝟐} \\ & =5(2𝐜_{1}−𝐜_{2})−2(𝐜_{1}+𝐜_{2}) \\ & =10𝐜_{1}−5𝐜_{2}−2𝐜_{1}−2𝐜_{2} \\ & =8𝐜_{1}−7𝐜_{2}\end{aligned}


$$

Therefore, $[\begin{aligned}8 \\ −7\end{aligned}]$

### Example: Writing a Vector in a Different Basis Given a Linear Relationship Between Two Bases

#### Question

Let $\mathcal{B}= \left\{\mathbf{b}_1, \mathbf{b}_2 \right\}$ be a basis of $\mathbb{R}^2$ and $[\begin{aligned}1 \\ −3\end{aligned}]$ What are the coordinates of $\mathbf{x}$ relative to the basis $\mathcal{C}= \left\{\mathbf{c}_1, \mathbf{c}_2 \right\},$ where $\mathbf{c}_1 = \mathbf{b}_2-\mathbf{b}_1$ and $\mathbf{c}_2 = 2\mathbf{b}_1 - 3\mathbf{b}_2?$

#### Explanation

We are given that

$$


\begin{aligned}𝐜_{1}=𝐛_{2}−𝐛_{1} \\ 𝐜_{2}=2𝐛_{1}−3𝐛_{2}.\end{aligned}


$$

First, we express the $\mathbf{b}$'s in terms of $\mathbf{c}$'s. Multiplying the first equation by $2$ and adding the equations, we get

$$


2\mathbf{c}_1+\mathbf{c}_2 = -\mathbf{b}_2 \qquad\Longrightarrow\qquad \mathbf{b}_2 = -2\mathbf{c}_1-\mathbf{c}_2.


$$

Substituting this into the first equation, we obtain

$$


\mathbf{c}_1 = \left( -2\mathbf{c}_1-\mathbf{c}_2 \right) - \mathbf{b}_1 \qquad\Longrightarrow\qquad \mathbf{b}_1 = -3\mathbf{c}_1-\mathbf{c}_2.


$$

Since $[\begin{aligned}1 \\ −3\end{aligned}]$ we can write the vector $\mathbf{x}$ in terms of the vectors $\mathbf c_1$ and $\mathbf c_2,$ as follows:

$$


\begin{aligned}𝐱 & =𝐛_{𝟏}−3𝐛_{𝟐} \\ & =(−3𝐜_{1}−𝐜_{2})−3(−2𝐜_{1}−𝐜_{2}) \\ & =−3𝐜_{1}−𝐜_{2}+6𝐜_{1}+3𝐜_{2} \\ & =3𝐜_{1}+2𝐜_{2}\end{aligned}


$$

Therefore, $[\begin{aligned}3 \\ 2\end{aligned}]$
