# Orthogonal Vectors in Euclidean Spaces

Source: https://www.mathacademy.com/topics/2099?courseId=145
Topic ID: 2099

## Prerequisites

- [The Dot Product in N-Dimensional Euclidean Space](./2094-the-dot-product-in-n-dimensional-euclidean-space.md)

## Lesson

### Introduction

Let $\mathbf{u}$ and $\mathbf{v}$ be vectors in $\mathbb{R}^n$. What do we mean when we say that the vectors $\mathbf{u}$ and $\mathbf{v}$ are orthogonal?

Two vectors $\mathbf{u}$ and $\mathbf{v}$ are **orthogonal** if their dot product equals zero:

$$


\mathbf{u}\cdot \mathbf{v}=0


$$

If two vectors are orthogonal, then we denote this by $\mathbf{u} \!\perp\! \mathbf{v}$. For instance, the vectors

$$


[\begin{aligned}1 \\ 0\end{aligned}]


$$

in $\mathbb{R^2}$ are orthogonal, since

$$


\begin{aligned}𝐞_{1}⋅𝐞_{2} & =[\begin{aligned}1 \\ 0\end{aligned}]⋅[\begin{aligned}0 \\ 1\end{aligned}] \\ & =1⋅0+0⋅1 \\ & =0+0 \\ & =0.\end{aligned}


$$

**Note:** The zero vector $\mathbf{0}$ is orthogonal to any vector $\mathbf{u}\in\mathbb{R}^n$ since $\mathbf{0}\cdot\mathbf{u}=0$.

### Example: Identifying Orthogonal Vectors

#### Question

Given the vector $\begin{aligned}−5 \\ −3 \\ 2 \\ 0\end{aligned}$, which of the following vectors are orthogonal to $\mathbf{u}$?

$$


\begin{aligned}1 \\ −3 \\ −4 \\ 9\end{aligned}


$$

#### Explanation

We compute the dot product between $\mathbf{u}$ and each of the listed vectors:

$$


\begin{aligned}𝐮⋅𝐯 & =𝑢_{1}⋅𝑣_{1}+𝑢_{2}⋅𝑣_{2}+𝑢_{3}⋅𝑣_{3}+𝑢_{4}⋅𝑣_{4} \\ & =(−5)⋅1+(−3)⋅(−3)+2⋅(−4)+0⋅9 \\ & =−5+9−8+0 \\ & =−4.\,×\end{aligned}


$$

$$


\begin{aligned}𝐮⋅𝐰 & =𝑢_{1}⋅𝑤_{1}+𝑢_{2}⋅𝑤_{2}+𝑢_{3}⋅𝑤_{3}+𝑢_{4}⋅𝑤_{4} \\ & =(−5)⋅2+(−3)⋅2+2⋅8+0⋅3 \\ & =−10−6+16+0 \\ & =0.\,✓\end{aligned}


$$

$$


\begin{aligned}𝐮⋅𝐱 & =𝑢_{1}⋅𝑥_{1}+𝑢_{2}⋅𝑥_{2}+𝑢_{3}⋅𝑥_{3}+𝑢_{4}⋅𝑥_{4} \\ & =(−5)⋅2+(−3)⋅(−4)+2⋅(−8)+0⋅6 \\ & =−10+12−16+0 \\ & =−14.\,×\end{aligned}


$$

Consequently, the correct answer is $\mathbf{w}$ only.

### Example: Determining Components in Orthogonal Vectors

#### Question

If $\begin{aligned}5 \\ −3 \\ 𝑘 \\ −2\end{aligned}$ and $\begin{aligned}−4 \\ 6 \\ −6 \\ 8\end{aligned}$ are orthogonal vectors, find the value of $k.$

#### Explanation

Since $\mathbf{u}$ and $\mathbf{v}$ are orthogonal vectors, we have that their dot product is equal to zero. First, let's calculate the dot product in terms of $k$:

$$


\begin{aligned}𝐮⋅𝐯 & =𝑢_{1}⋅𝑣_{1}+𝑢_{2}⋅𝑣_{2}+𝑢_{3}⋅𝑣_{3}+𝑢_{4}⋅𝑣_{4} \\ & =5⋅(−4)+(−3)⋅6+𝑘⋅(−6)+(−2)⋅8 \\ & =−20−18−6𝑘−16 \\ & =−6𝑘−54.\end{aligned}


$$

Equating the last line to zero, we have

$$


\begin{aligned}−6𝑘−54 & =0 \\ −6𝑘 & =54 \\ 𝑘 & =−9.\end{aligned}


$$

### Example: Calculating Dot Products Using Orthogonal Vectors

#### Question

Let $\begin{aligned}−1 \\ −2 \\ 5\end{aligned}$ and $\begin{aligned}−1 \\ 3 \\ 1\end{aligned}$ be vectors such that $\mathbf{u} \!\perp\! \mathbf{w}$. Find $(\mathbf{u}+\mathbf{v})\cdot \mathbf{w} + \mathbf{u}\cdot(\mathbf{v}+ \mathbf{w}).$

#### Explanation

Since $\mathbf{u}$ and $\mathbf{w}$ are orthogonal vectors, we have that $\mathbf{u}\cdot\mathbf{w}=0$. Therefore, using linearity of the dot product to expand the parentheses, we have

$$


\begin{aligned}(𝐮+𝐯)⋅𝐰+𝐮⋅(𝐯+𝐰) & =𝐮⋅𝐰+𝐯⋅𝐰+𝐮⋅𝐯+𝐮⋅𝐰 \\ & =0+𝐯⋅𝐰+𝐮⋅𝐯+0 \\ & =𝐯⋅𝐰+𝐮⋅𝐯 \\ & =(2⋅(−1)+(−3)⋅3+4⋅1) \\ & +((−1)⋅2+(−2)⋅(−3)+5⋅4)\, \\ & =(−2−9+4)+(−2+6+20) \\ & =−7+24 \\ & =17.\end{aligned}


$$

### Example: Determining Components of a Vector Orthogonal to Two Given Vectors

#### Question

Let $\begin{aligned}−8 \\ 𝑎 \\ 𝑏 \\ −10\end{aligned}$ and $\begin{aligned}4 \\ 2 \\ −5 \\ −3\end{aligned}$ be vectors such that $\mathbf{u}$ is orthogonal to $\mathbf{v}$ and $\mathbf{w}$. What is the value of $a+b?$

#### Explanation

Given that $\mathbf{u}$ is orthogonal to $\mathbf{v}$ and $\mathbf{w}$, we have

$$


\begin{aligned}𝐮⋅𝐯=0 \\ 𝐮⋅𝐰=0.\end{aligned}


$$

Let's consider the first equation $\mathbf{u}\cdot\mathbf{v}=0$. Calculating the dot product in terms of $a$ and $b$, we get

$$


\begin{aligned}𝐮⋅𝐯 & =0 \\ −8⋅6+𝑎⋅(−15)+𝑏⋅9+(−10)⋅(−12) & =0 \\ −48−15𝑎+9𝑏+120 & =0 \\ −15𝑎+9𝑏 & =−72 \\ −5𝑎+3𝑏 & =−24.\end{aligned}


$$

Similarly, for the second equation $\mathbf{u}\cdot\mathbf{w}=0$, we obtain

$$


\begin{aligned}𝐮⋅𝐰 & =0 \\ −8⋅4+𝑎⋅2+𝑏⋅(−5)+(−10)⋅(−3) & =0 \\ −32+2𝑎−5𝑏+30 & =0 \\ 2𝑎−5𝑏 & =2.\end{aligned}


$$

So, to find the values of $a$ and $b$, we need to solve the system

$$


\begin{aligned}\begin{aligned}−5𝑎+3𝑏=−24 \\ 2𝑎−5𝑏=2.\end{aligned}\end{aligned}


$$

Multiplying the first equation by $2$ and the second equation by $5$, we get

$$


\begin{aligned}−10𝑎+6𝑏=−48 \\ 10𝑎−25𝑏=10.\end{aligned}


$$

Now, adding the above equations, we obtain

$$


-19b = -38 \qquad\Longrightarrow\qquad b = 2.


$$

Substituting $b = 2$ into the second equation, we obtain

$$


\begin{aligned}2𝑎−5(2) & =2 \\ 2𝑎−10 & =2 \\ 2𝑎 & =12 \\ 𝑎 & =6.\end{aligned}


$$

Finally, we have that

$$


a+b = 6 + 2 = 8.


$$
