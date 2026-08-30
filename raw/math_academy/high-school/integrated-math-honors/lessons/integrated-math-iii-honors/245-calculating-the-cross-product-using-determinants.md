# Calculating the Cross Product Using Determinants

Source: https://www.mathacademy.com/topics/245?courseId=101
Topic ID: 245

## Prerequisites

- [Solving Radical Equations](../../../traditional/lessons/algebra-i/116-solving-radical-equations.md)
- [The Determinant of a 3x3 Matrix](./153-the-determinant-of-a-3x3-matrix.md)
- [Properties of the Cross Product](./4858-properties-of-the-cross-product.md)

## Lesson

### Introduction

Suppose we have two vectors $\mathbf{a}$ and $\mathbf{b},$ given by

$$


\begin{aligned}𝐚 & =𝑎_{1}𝐢+𝑎_{2}𝐣+𝑎_{3}𝐤 \\ 𝐛 & =𝑏_{1}𝐢+𝑏_{2}𝐣+𝑏_{3}𝐤.\end{aligned}


$$

The cross product $\mathbf{a}\times\mathbf b$ can be calculated using the following determinant:

$$


\begin{aligned}𝐢 & 𝐣 & 𝐤 \\ 𝑎_{1} & 𝑎_{2} & 𝑎_{3} \\ 𝑏_{1} & 𝑏_{2} & 𝑏_{3}\end{aligned}


$$

For instance, suppose that we have the two vectors $\mathbf{a} = \langle 2,-1,5 \rangle$, $\mathbf{b} = \langle -1,4,2 \rangle$. We can find the cross product of $\mathbf{a}$ and $\mathbf{b}$ as follows:

$$


\begin{aligned}𝐚×𝐛 & =\begin{aligned}𝐢 & 𝐣 & 𝐤 \\ 2 & −1 & 5 \\ −1 & 4 & 2\end{aligned} \\ & =\begin{aligned}−1 & 5 \\ 4 & 2\end{aligned}𝐢−\begin{aligned}2 & 5 \\ −1 & 2\end{aligned}𝐣+\begin{aligned}2 & −1 \\ −1 & 4\end{aligned}𝐤 \\ & =((−1)⋅2−5⋅4)𝐢−(2⋅2−5⋅(−1))𝐣+(2⋅4−(−1)⋅(−1))𝐤 \\ & =−22𝐢−9𝐣+7𝐤 \\ & =⟨−22,−9,7⟩\end{aligned}


$$

### Example: Calculating the Cross Product Using Determinants

#### Question

Let $\mathbf{a}=\langle 3,-4,1 \rangle$ and $\mathbf{b}=\langle -7,0,2 \rangle.$ Find $\mathbf{a} \times \mathbf{b}.$

#### Explanation

Using the determinant formula, we get

$$


\begin{aligned}𝐚×𝐛 & =\begin{aligned}𝐢 & 𝐣 & 𝐤 \\ 3 & −4 & 1 \\ −7 & 0 & 2\end{aligned} \\ & =\begin{aligned}−4 & 1 \\ 0 & 2\end{aligned}𝐢−\begin{aligned}3 & 1 \\ −7 & 2\end{aligned}𝐣+\begin{aligned}3 & −4 \\ −7 & 0\end{aligned}𝐤 \\ & =((−4)⋅2−1⋅0)𝐢−(3⋅2−1⋅(−7))𝐣+(3⋅0−(−4)⋅(−7))𝐤 \\ & =−8𝐢−13𝐣−28𝐤 \\ & =⟨−8,−13,−28⟩.\end{aligned}


$$

### Example: Solving for an Unknown in an Equation Involving the Cross Product

#### Question

Let $\mathbf{a}=\langle 3, 1, 2x \rangle,$ $\mathbf{b}=\langle 0,1,x \rangle,$ and $|\,\mathbf{a} \times \mathbf{b}\,| = \sqrt{19}.$ Find $x.$

#### Explanation

Using the determinant formula, we get

$$


\begin{aligned}𝐚×𝐛 & =\begin{aligned}𝐢 & 𝐣 & 𝐤 \\ 3 & 1 & 2𝑥 \\ 0 & 1 & 𝑥\end{aligned} \\ & =\begin{aligned}1 & 2𝑥 \\ 1 & 𝑥\end{aligned}𝐢−\begin{aligned}3 & 2𝑥 \\ 0 & 𝑥\end{aligned}𝐣+\begin{aligned}3 & 1 \\ 0 & 1\end{aligned}𝐤 \\ & =−𝑥𝐢−3𝑥𝐣+3𝐤 \\ & =⟨−𝑥,−3𝑥,3⟩.\end{aligned}


$$

Now, computing the magnitude, we get

$$


\begin{aligned}|\,𝐚×𝐛\,| & =\sqrt{√(−𝑥)^{2}+(−3𝑥)^{2}+3^{2}} \\ & =\sqrt{√10𝑥^{2}+9}.\end{aligned}


$$

Lastly, we solve for $x$ the following equation:

$$


\begin{aligned} & |\,𝐚×𝐛\,|=\sqrt{√19} \\ & \sqrt{√10𝑥^{2}+9}=\sqrt{√19} \\ & 10𝑥^{2}+9=19 \\ & 10𝑥^{2}=10 \\ & 𝑥^{2}=1\end{aligned}


$$

Therefore, the solutions are $x= \pm 1.$

### Proof of the Formula for the Cross Product Using the Determinant

We have been using the following formula to compute the cross product of two vectors:

$$


\begin{aligned}𝐚×𝐛 & =\begin{aligned}𝐢 & 𝐣 & 𝐤 \\ 𝑎_{1} & 𝑎_{2} & 𝑎_{3} \\ 𝑏_{1} & 𝑏_{2} & 𝑏_{3}\end{aligned} \\ & =\begin{aligned}𝑎_{2} & 𝑎_{3} \\ 𝑏_{2} & 𝑏_{3}\end{aligned}𝐢−\begin{aligned}𝑎_{1} & 𝑎_{3} \\ 𝑏_{1} & 𝑏_{3}\end{aligned}𝐣+\begin{aligned}𝑎_{1} & 𝑎_{2} \\ 𝑏_{1} & 𝑏_{2}\end{aligned}𝐤 \\ & =(𝑎_{2}𝑏_{3}−𝑎_{3}𝑏_{2})𝐢−(𝑎_{1}𝑏_{3}−𝑎_{3}𝑏_{1})𝐣+(𝑎_{1}𝑏_{2}−𝑎_{2}𝑏_{1})𝐤\end{aligned}


$$

But where does this formula come from? Let's find out.

Suppose we want to find the cross product $\mathbf{a} \times \mathbf{b}$ for $\mathbf{a}=a_1\mathbf{i}+a_2\mathbf{j}+a_3\mathbf{k}$ and $\mathbf{b}=b_1\mathbf{i}+b_2\mathbf{j}+b_3\mathbf{k}.$ Using properties of the cross product, we obtain

$$


\begin{aligned}𝐚×𝐛 & =(𝑎_{1}𝐢+𝑎_{2}𝐣+𝑎_{3}𝐤)×(𝑏_{1}𝐢+𝑏_{2}𝐣+𝑏_{3}𝐤) \\ & =(𝑎_{1}⋅𝑏_{1})𝐢×𝐢+(𝑎_{1}⋅𝑏_{2})𝐢×𝐣+(𝑎_{1}⋅𝑏_{3})𝐢×𝐤 \\ & +(𝑎_{2}⋅𝑏_{1})𝐣×𝐢+(𝑎_{2}⋅𝑏_{2})𝐣×𝐣+(𝑎_{2}⋅𝑏_{3})𝐣×𝐤 \\ & +(𝑎_{3}⋅𝑏_{1})𝐤×𝐢+(𝑎_{3}⋅𝑏_{2})𝐤×𝐣+(𝑎_{3}⋅𝑏_{3})𝐤×𝐤.\end{aligned}


$$

Since the cross product of two parallel (collinear) vectors is equal to $\mathbf 0,$ we have

$$


\mathbf{i}\times\mathbf{i} = \mathbf{j}\times\mathbf{j} = \mathbf{k}\times\mathbf{k} = \mathbf 0.


$$

Also, using the definition of the cross product we obtain

$$


\begin{aligned}𝐢×𝐣=𝐤, & \,𝐣×𝐢=−𝐤, \\ 𝐣×𝐤=𝐢, & \,𝐤×𝐣=−𝐢, \\ 𝐤×𝐢=𝐣, & \,𝐢×𝐤=−𝐣.\end{aligned}


$$

Therefore,

$$


\begin{aligned}𝐚×𝐛 & =(𝑎_{1}⋅𝑏_{1})\underset{=𝟎}{\underset{}{𝐢×𝐢}}+(𝑎_{1}⋅𝑏_{2})\underset{=𝐤}{\underset{}{𝐢×𝐣}}+(𝑎_{1}⋅𝑏_{3})\underset{=−𝐣}{\underset{}{𝐢×𝐤}} \\ & +(𝑎_{2}⋅𝑏_{1})\underset{=−𝐤}{\underset{}{𝐣×𝐢}}+(𝑎_{2}⋅𝑏_{2})\underset{=𝟎}{\underset{}{𝐣×𝐣}}+(𝑎_{2}⋅𝑏_{3})\underset{=𝐢}{\underset{}{𝐣×𝐤}} \\ & +(𝑎_{3}⋅𝑏_{1})\underset{=𝐣}{\underset{}{𝐤×𝐢}}+(𝑎_{3}⋅𝑏_{2})\underset{=−𝐢}{\underset{}{𝐤×𝐣}}+(𝑎_{3}⋅𝑏_{3})\underset{=𝟎}{\underset{}{𝐤×𝐤}} \\ & =(𝑎_{2}𝑏_{3}−𝑎_{3}𝑏_{2})𝐢−(𝑎_{1}𝑏_{3}−𝑎_{3}𝑏_{1})𝐣+(𝑎_{1}𝑏_{2}−𝑎_{2}𝑏_{1})𝐤.\end{aligned}


$$

The expression above is equal to the formula given for the cross product of two general vectors using the determinant.
