# Calculating the Dot Product Using Components

Source: https://www.mathacademy.com/topics/177?courseId=101
Topic ID: 177

## Prerequisites

- [Calculating the Dot Product Using Angle and Magnitude](./243-calculating-the-dot-product-using-angle-and-magnitude.md)
- [Three-Dimensional Vectors in Component Form](./1166-three-dimensional-vectors-in-component-form.md)

## Lesson

### Introduction

Given two vectors $\mathbf{a}$ and $\mathbf{b},$ we know that the dot product can be computed using the formula

$$


\mathbf{a} \cdot \mathbf{b} = |\,\mathbf{a}\,| \cdot |\,\mathbf{b}\,| \cdot \cos\theta,


$$

where $\theta$ is the angle formed between the vectors when their tails are placed at the same point.

However, there is another formula for the dot product that we can use if the two vectors are given in component form. If the components of our two vectors are

$$


\mathbf{a} = \langle {\color{red}a_x},{\color{blue}a_y}, a_z \rangle, \qquad \mathbf{b} = \langle {\color{red}b_x},{\color{blue}b_y}, b_z \rangle,


$$

then the dot product can be computed by summing up the products of corresponding components:

$$


\mathbf{a} \cdot \mathbf{b} = {\color{red}a_x} \cdot {\color{red}b_x} + {\color{blue}a_y} \cdot {\color{blue}b_y} + a_z \cdot b_z


$$

For example, if we have two vectors

$$


\mathbf{a} = \langle {\color{red}3},{\color{blue}-5},2 \rangle, \qquad \mathbf{b} = \langle {\color{red}4},{\color{blue}6},7 \rangle,


$$

Then we can find the dot product of $\mathbf{a}$ and $\mathbf{b}$ as follows:

$$


\begin{aligned}𝐚⋅𝐛 & =3⋅4+(−5)⋅6+2⋅7 \\ & =12−30+14 \\ & =−4\end{aligned}


$$

**Note:** The procedure for computing the dot product works for vectors of any number of components. For example,

$$


\begin{aligned}⟨3,−5⟩⋅⟨4,6⟩ & =3⋅4+(−5)⋅6 \\ & =12−30 \\ & =−18\end{aligned}


$$

and

$$


\begin{aligned}⟨3,−5,2,1⟩⋅⟨4,6,7,9⟩ & =3⋅4+(−5)⋅6+2⋅7+1⋅9 \\ & =12−30+14+9 \\ & =5.\end{aligned}


$$

### Example: Calculating the Dot Product Using the General Formula

#### Question

Let $\mathbf{a}=\langle 0,-0.4,11 \rangle$ and $\mathbf{b}=\langle 2,5,2 \rangle.$ Find $\mathbf{a} \cdot \mathbf{b}.$

#### Explanation

Summing up the products of corresponding components, we obtain:

$$


\begin{aligned}𝐚⋅𝐛 & =𝑎_{𝑥}⋅𝑏_{𝑥}+𝑎_{𝑦}⋅𝑏_{𝑦}+𝑎_{𝑧}⋅𝑏_{𝑧} \\ & =0⋅2+(−0.4)⋅5+11⋅2 \\ & =0−2+22 \\ & =20\end{aligned}


$$

### Example: Solving for an Unknown Given Two Perpendicular Vectors

#### Question

Let $\begin{aligned}4 \\ −2 \\ 1\end{aligned}$ and $\begin{aligned}−2 \\ 5 \\ 𝑡\end{aligned}$. Given that $\mathbf{a} \perp \mathbf{b}$, find the value of $t$.

#### Explanation

We know that $\mathbf{a} \perp \mathbf{b}$ ($\mathbf{a}$ and $\mathbf{b}$ are perpendicular) if and only if $\mathbf{a} \cdot \mathbf{b} = 0.$

Computing the dot product, we have

$$


\begin{aligned}𝐚⋅𝐛 & =𝑎_{𝑥}⋅𝑏_{𝑥}+𝑎_{𝑦}⋅𝑏_{𝑦}+𝑎_{𝑧}⋅𝑏_{𝑧} \\ & =4⋅(−2)+(−2)⋅5+1⋅𝑡 \\ & =−8−10+𝑡 \\ & =𝑡−18.\end{aligned}


$$

Setting the dot product equal to $0,$ we obtain:

$$


\begin{aligned}𝐚⋅𝐛 & =0 \\ 𝑡−18 & =0 \\ 𝑡 & =18\end{aligned}


$$

### Intuition Behind the Formula

To understand the reasoning behind the formula for the dot product of two vectors, it's helpful to write the two vectors in terms of their elementary unit vectors and carry out the computation the long way.

For example, suppose we want to find the dot product $\mathbf{a} \cdot \mathbf{b}$ for $\mathbf{a} = \langle 3,-5 \rangle$ and $\mathbf{b}=\langle 4,6 \rangle.$

Expressing the vectors in terms of their elementary unit vectors, we have

$$


\begin{aligned}𝐚=3𝐢−5𝐣,\,𝐛=4𝐢+6𝐣.\end{aligned}


$$

Now, using properties of the dot product we obtain

$$


\begin{aligned}𝐚⋅𝐛 & =(3𝐢+(−5)𝐣)⋅(4𝐢+6𝐣) \\ & =(3⋅4)𝐢⋅𝐢+(3⋅6)𝐢⋅𝐣+(−5⋅4)𝐣⋅𝐢+(−5⋅6)𝐣⋅𝐣.\end{aligned}


$$

Remember that $\mathbf{i},\mathbf{j}$ are perpendicular, meaning the angle between them is $\theta=90^\circ$ and consequently their dot product is zero:

$$


\begin{aligned}𝐢⋅𝐣 & =|\,𝐢\,|⋅|\,𝐣\,|⋅cos⁡90^{∘} \\ & =1⋅1⋅0 \\ & =0\end{aligned}


$$

On the other hand, since the angle between a vector and itself is $\theta=0,$ we have

$$


\begin{aligned}𝐢⋅𝐢 & =|\,𝐢\,|⋅|\,𝐢\,|⋅cos⁡0^{∘} \\ & =1⋅1⋅1 \\ & =1\end{aligned}


$$

and

$$


\begin{aligned}𝐣⋅𝐣 & =|\,𝐣\,|⋅|\,𝐣\,|⋅cos⁡0^{∘} \\ & =1⋅1⋅1 \\ & =1.\end{aligned}


$$

Therefore, we have

$$


\begin{aligned}𝐢⋅𝐣 & =𝐣⋅𝐢=0, \\ 𝐢⋅𝐢 & =𝐣⋅𝐣=1,\end{aligned}


$$

and our computation reduces to

$$


\begin{aligned}𝐚⋅𝐛 & =(3⋅4)\overset{𝐢⋅𝐢}{=1}+(3⋅6)\overset{𝐢⋅𝐣}{=0}+(−5⋅4)\overset{𝐣⋅𝐢}{=0}+(−5⋅6)\overset{𝐣⋅𝐣}{=1} \\ & =(3⋅4)⋅1+(3⋅6)⋅0+(−5⋅4)⋅0+(−5⋅6)⋅1 \\ & =(3⋅4)+(−5⋅6).\end{aligned}


$$

So, we have that

$$


\begin{aligned}𝐚⋅𝐛 & =⟨3,−5⟩⋅⟨4,6⟩ \\ & =(3⋅4)+(−5⋅6).\end{aligned}


$$
