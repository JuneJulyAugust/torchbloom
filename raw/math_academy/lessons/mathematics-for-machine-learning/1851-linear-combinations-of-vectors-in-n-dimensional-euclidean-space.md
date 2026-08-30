# Linear Combinations of Vectors in N-Dimensional Euclidean Space

Source: https://www.mathacademy.com/topics/1851?courseId=145
Topic ID: 1851

## Prerequisites

- [Solving 3x3 Singular Systems of Equations Using Gaussian Elimination](./1374-solving-3x3-singular-systems-of-equations-using-gaussian-elimination.md)
- [Vectors in N-Dimensional Euclidean Space](./1849-vectors-in-n-dimensional-euclidean-space.md)

## Lesson

### Introduction

Consider a vector $\mathbf{u}$ which is given in terms of the vectors $\mathbf{v_1}$ and $\mathbf{v_2}$ as follows:

$$


{\color{red}3}{\color{blue}\mathbf{v_1}}+({\color{red}-2}){\color{blue}\mathbf{v_2}} = \mathbf{u}


$$

Here, we say that $\mathbf{u}$ is a **linear combination** of the vectors ${\color{blue}\mathbf{v_1}}$ and ${\color{blue}\mathbf{v_2}}$ with coefficients ${\color{red}3}$ and ${\color{red}-2}$ respectively.

In general, a linear combination of $n$ vectors $\mathbf{v_1},\mathbf{v_2},\dots,\mathbf{v_n}$ is the *weighted sum*

$$


{\color{red}x_1}\mathbf{\color{blue}v_1}+{\color{red}x_2}\mathbf{\color{blue}v_2}+\cdots + {\color{red}x_n}\mathbf{\color{blue}v_n} = \mathbf{u},


$$

where ${\color{red}x_1},{\color{red}x_2},\dots,{\color{red}x_n}\in\mathbb{R}.$ We say that $\mathbf{u}$ is a linear combination of the vectors $\mathbf{\color{blue}v_1},\mathbf{\color{blue}v_2},\dots,\mathbf{\color{blue}v_n}$ with coefficients (or *weights*) ${\color{red}x_1},{\color{red}x_2},\dots,{\color{red}x_n},$ respectively.

For instance,

$$


[\begin{aligned}1 \\ −1\end{aligned}]


$$

is the linear combination of vectors $\mathbf{\color{blue}v_1},\mathbf{\color{blue}v_2},\mathbf{\color{blue}v_3}$ with coefficients ${\color{red}2}, {\color{red}0}, {\color{red}\dfrac{1}{2}},$ respectively.

### Example: Solving for One Coefficient in a Linear Combination

#### Question

Find $s,$ if $3\mathbf{a_1}+s\mathbf{a_2} = \mathbf{b}$ and

$$


\begin{aligned}−1 \\ 2 \\ 1\end{aligned}


$$

#### Explanation

Using the properties of addition/subtraction and scalar multiplication of vectors to isolate the $s$ term, we get

$$


\begin{aligned}3𝐚_{𝟏}+𝑠𝐚_{𝟐} & =𝐛 \\ 3\begin{aligned}−1 \\ 2 \\ 1\end{aligned}+𝑠\begin{aligned}4 \\ 0 \\ −2\end{aligned} & =\begin{aligned}13 \\ 6 \\ −5\end{aligned} \\ 𝑠\begin{aligned}4 \\ 0 \\ −2\end{aligned} & =\begin{aligned}13 \\ 6 \\ −5\end{aligned}−3\begin{aligned}−1 \\ 2 \\ 1\end{aligned} \\ 𝑠\begin{aligned}4 \\ 0 \\ −2\end{aligned} & =\begin{aligned}16 \\ 0 \\ −8\end{aligned}.\end{aligned}


$$

From the final equation above, we can tell that $s=4.$

### Example: Solving for a Vector in a Linear Combination

#### Question

Find $\mathbf{x},$ if $\mathbf{a}+2\mathbf{x} = \mathbf{b}$ and

$$


\begin{aligned}12 \\ −11 \\ −5\end{aligned}


$$

#### Explanation

Using the properties of addition/subtraction and scalar multiplication of vectors to isolate $\mathbf{x},$ we get

$$


\begin{aligned}𝐚+2𝐱 & =𝐛 \\ 2𝐱 & =𝐛−𝐚 \\ 𝐱 & =\frac{1}{2}(𝐛−𝐚) \\ 𝐱 & =\frac{1}{2}\begin{aligned}24 \\ −9 \\ 13\end{aligned}−\begin{aligned}12 \\ −11 \\ −5\end{aligned} \\ 𝐱 & =\frac{1}{2}\begin{aligned}12 \\ 2 \\ 18\end{aligned} \\ 𝐱 & =\begin{aligned}6 \\ 1 \\ 9\end{aligned}.\end{aligned}


$$

### Example: Solving for Two Coefficients in a Linear Combination

#### Question

Consider the vectors

$$


\begin{aligned}4 \\ −1 \\ 3\end{aligned}


$$

If $x_1 \mathbf{c}_1 + x_2\mathbf{c}_2 = \mathbf d,$ then what is $x_1+x_2?$

#### Explanation

If $x_1 \mathbf{c}_1 + x_2\mathbf{c}_2 = \mathbf d,$ then we have

$$


\begin{aligned}𝑥_{1}\begin{aligned}4 \\ −1 \\ 3\end{aligned}+𝑥_{2}\begin{aligned}1 \\ 0 \\ 1\end{aligned} & =\begin{aligned}5 \\ −5 \\ 0\end{aligned} \\ \begin{aligned}4𝑥_{1}+𝑥_{2} \\ −𝑥_{1} \\ 3𝑥_{1}+𝑥_{2}\end{aligned} & =\begin{aligned}5 \\ −5 \\ 0\end{aligned}.\end{aligned}


$$

Equating the corresponding components, we get the following system:

$$


\begin{aligned}4𝑥_{1}+𝑥_{2}=5 \\ −𝑥_{1}=−5 \\ 3𝑥_{1}+𝑥_{2}=0\end{aligned}


$$

From the second equation, we obtain $x_1=5,$ which we substitute into the first equation to get

$$


\begin{aligned}4𝑥_{1}+𝑥_{2} & =5 \\ 4(5)+𝑥_{2} & =5 \\ 𝑥_{2} & =−15.\end{aligned}


$$

Finally, we substitute $x_1=5$ and $x_2=-15$ into the third equation to get

$$


\begin{aligned}3𝑥_{1}+𝑥_{2} & =0 \\ 3(5)+(−15) & =0 \\ 0 & =0,\end{aligned}


$$

which gives a true statement.

So the solution of the system is $x_1=5$ and $x_2=-15,$ which means

$$


5 \mathbf{c_1}-15 \mathbf{c_2} = \mathbf{d}.


$$

Consequently,

$$


x_1+x_2=5-15=-10.


$$

### Example: Solving for Three Coefficients in a Linear Combination

#### Question

Consider the vectors

$$


\begin{aligned}0 \\ 1 \\ 0\end{aligned}


$$

If $x_1 \mathbf{a}_1 + x_2\mathbf{a}_2 + x_3\mathbf{a}_3 = \mathbf b,$ then what is $x_1+x_2+x_3?$

#### Explanation

Since $\mathbf{b}$ is a linear combination of vectors $\mathbf{a_1}, \,\mathbf{a_2}$ and $\mathbf{a_3}$ with coefficients $x_1,\, x_2$ and $x_3,$ respectively, we have

$$


\begin{aligned}𝑥_{1}𝐚_{𝟏}+𝑥_{2}𝐚_{𝟐}+𝑥_{3}𝐚_{𝟑} & =𝐛 \\ 𝑥_{1}\begin{aligned}0 \\ 1 \\ 0\end{aligned}+𝑥_{2}\begin{aligned}1 \\ 0 \\ −1\end{aligned}+𝑥_{3}\begin{aligned}1 \\ 2 \\ 3\end{aligned} & =\begin{aligned}1 \\ 1 \\ 7\end{aligned} \\ \begin{aligned}0 \\ 𝑥_{1} \\ 0\end{aligned}+\begin{aligned}𝑥_{2} \\ 0 \\ −𝑥_{2}\end{aligned}+\begin{aligned}𝑥_{3} \\ 2𝑥_{3} \\ 3𝑥_{3}\end{aligned} & =\begin{aligned}1 \\ 1 \\ 7\end{aligned} \\ \begin{aligned}𝑥_{2}+𝑥_{3} \\ 𝑥_{1}+2𝑥_{3} \\ −𝑥_{2}+3𝑥_{3}\end{aligned} & =\begin{aligned}1 \\ 1 \\ 7\end{aligned}.\end{aligned}


$$

Equating the corresponding components, we get the following system:

$$


\begin{aligned}𝑥_{2}+𝑥_{3}=1 \\ 𝑥_{1}+2𝑥_{3}=1 \\ −𝑥_{2}+3𝑥_{3}=7\end{aligned}


$$

We will solve this system using Gaussian elimination. First, we write the augmented matrix for this system:

$$


\begin{aligned}0 & 1 & 1 & 1 \\ 1 & 0 & 2 & 1 \\ 0 & −1 & 3 & 7\end{aligned}


$$

Row-reducing the augmented matrix, we get

$$


\begin{aligned}𝑀 & =\begin{aligned}0 & 1 & 1 & 1 \\ 1 & 0 & 2 & 1 \\ 0 & −1 & 3 & 7\end{aligned} & 𝑅_{1} & ↔𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 2 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & −1 & 3 & 7\end{aligned} & 𝑅_{3} & :=𝑅_{3}+𝑅_{2} \\ & ∼\begin{aligned}1 & 0 & 2 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 4 & 8\end{aligned} & 𝑅_{3} & :=\frac{1}{4}𝑅_{3} \\ & ∼\begin{aligned}1 & 0 & 2 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 2\end{aligned}. & & \end{aligned}


$$

The system is now

$$


\begin{aligned}𝑥_{1}+2𝑥_{3}=1 \\ 𝑥_{2}+𝑥_{3}=1 \\ 𝑥_{3}=2.\end{aligned}


$$

From the third equation, we get $x_3 = 2.$ Substituting this into the second equation, we get

$$


x_2+(2) = 1 \quad\Rightarrow\quad x_2 = -1,


$$

and substituting $x_3=2$ into the first equation, we get

$$


x_1+2(2) = 1 \quad\Rightarrow\quad x_1 = -3.


$$

So the solution of the system is $x_1=-3, x_2=-1, x_3=2,$ which means

$$


-3 \mathbf{a_1}- \mathbf{a_2} +2 \mathbf{a_3}= \mathbf{b}.


$$

Consequently,

$$


x_1+x_2+x_3=-3-1+2=-2.


$$
