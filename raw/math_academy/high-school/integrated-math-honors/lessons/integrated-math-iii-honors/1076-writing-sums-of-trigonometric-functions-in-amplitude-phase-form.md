# Writing Sums of Trigonometric Functions in Amplitude-Phase Form

Source: https://www.mathacademy.com/topics/1076?courseId=101
Topic ID: 1076

## Prerequisites

- [Simplifying Expressions Using the Pythagorean Identity](./207-simplifying-expressions-using-the-pythagorean-identity.md)
- [The Sum and Difference Formulas for Sine](./270-the-sum-and-difference-formulas-for-sine.md)
- [The Sum and Difference Formulas for Cosine](./274-the-sum-and-difference-formulas-for-cosine.md)
- [Solving Systems of Linear Equations Using Elimination: Two Transformations](../../../traditional/lessons/algebra-i/4236-solving-systems-of-linear-equations-using-elimination-two-transformations.md)

## Lesson

### Introduction

The trigonometric expression

$$


{\color{blue}R} \sin( x + {\color{red}\phi})


$$

is called the **amplitude-phase form** of sine. Here, ${\color{blue}R}$ is the **amplitude** and ${\color{red}\phi}$ is the **phase** of the sine function.

The sum or difference of a sine function and a cosine function with the same argument can always be written as a sine function in amplitude-phase form. That is to say, if $a$ and $b$ are positive real numbers, then the expression

$$


a \sin x \pm b \cos x


$$

can be written in the form

$$


R \sin(x \pm \phi).


$$

for some $R>0$ and $\phi \in \left(0, \dfrac{\pi}{2}\right).$

### Writing a Sum or Difference of Sine and Cosine Using Amplitude-Phase Form

Let's write the expression

$$


3\sin{x}+\sqrt{3}\cos{x}


$$

in amplitude-phase form. We start by expanding out the amplitude-phase form using the sum formula for sine:

$$


\begin{aligned}𝑅sin⁡(𝑥+𝜙) & =𝑅(sin⁡𝑥cos⁡𝜙+cos⁡𝑥sin⁡𝜙) \\ & =𝑅cos⁡𝜙sin⁡𝑥+𝑅sin⁡𝜙cos⁡𝑥\end{aligned}


$$

So, we obtain the following equation:

$$


\begin{aligned}3sin⁡𝑥+\sqrt{3}cos⁡𝑥 & =𝑅sin⁡(𝑥+𝜙) \\ 3sin⁡𝑥+\sqrt{3}cos⁡𝑥 & =(𝑅cos⁡𝜙)sin⁡𝑥+(𝑅sin⁡𝜙)cos⁡𝑥\end{aligned}


$$

First, we find the phase $\phi$. Equating the coefficients of $\sin x$ and $\cos x,$ we have the following system:

$$


\begin{aligned}𝑅cos⁡𝜙=3 \\ 𝑅sin⁡𝜙=\sqrt{3}\end{aligned}


$$

Dividing the second equation by the first one, we get

$$


\begin{aligned}\frac{𝑅sin⁡𝜙}{𝑅cos⁡𝜙} & =\frac{\sqrt{3}}{3} \\ tan⁡𝜙 & =\frac{\sqrt{3}}{3} \\ 𝜙 & =arctan⁡(\frac{\sqrt{3}}{3}) \\ & =\frac{𝜋}{6}.\end{aligned}


$$

Now, we find the amplitude $R.$ Squaring the first and the second equations of the system and adding the results together, we get

$$


\begin{aligned}(𝑅cos⁡𝜙)^{2}+(𝑅sin⁡𝜙)^{2} & =(3)^{2}+(\sqrt{3})^{2} \\ 𝑅^{2}(cos^{2}⁡𝜙+sin^{2}⁡𝜙) & =9+3 \\ 𝑅^{2} & =12 \\ 𝑅 & =\sqrt{12} \\ 𝑅 & =2\sqrt{3}.\end{aligned}


$$

Note that we only considered the positive root, since $R>0.$

Finally, we can write the initial expression in amplitude-phase form as follows:

$$


3\sin{x}+\sqrt{3}\cos{x} = {\color{blue}2\sqrt{3}} \sin \left(x + {\color{red}\dfrac{\pi}{6}} \right)


$$

### Example: Finding the Amplitude for the Amplitude-Phase Form for Sine

#### Question

Given that the expression $\sqrt{2}\sin x + \sqrt{7}\cos x$ can be written as $R\sin(x+\phi)$ with $R>0,$ what is the value of $R?$

#### Explanation

The sum formula for sine gives

$$


\begin{aligned}𝑅sin⁡(𝑥+𝜙) & =𝑅(sin⁡𝑥cos⁡𝜙+cos⁡𝑥sin⁡𝜙) \\ & =𝑅cos⁡𝜙sin⁡𝑥+𝑅sin⁡𝜙cos⁡𝑥.\end{aligned}


$$

Therefore, by writing the given expression in the amplitude-phase form

$$


\sqrt{2}\sin x + \sqrt{7}\cos x = R\sin(x+\phi),


$$

we get the following identity:

$$


\sqrt{2}\sin x + \sqrt{7}\cos x = (R \cos \phi ) \sin x + (R \sin \phi ) \cos x


$$

Equating the coefficients of $\sin x$ and $\cos x,$ we have the following system:

$$


\begin{aligned}𝑅cos⁡𝜙=\sqrt{2} \\ 𝑅sin⁡𝜙=\sqrt{7}\end{aligned}


$$

Squaring the first and the second equations of the system and adding the results together, we get

$$


\begin{aligned}(𝑅cos⁡𝜙)^{2}+(𝑅sin⁡𝜙)^{2} & =\sqrt{2}^{2}+\sqrt{7}^{2} \\ 𝑅^{2}(cos^{2}⁡𝜙+sin^{2}⁡𝜙) & =2+7 \\ 𝑅^{2} & =9 \\ 𝑅 & =3.\end{aligned}


$$

Note that we only consider the positive root since $R>0.$

### Example: Finding the Phase for the Amplitude-Phase Form for Sine

#### Question

Given that the expression $2\sin{x}-2\cos{x}$ can be written as $R\sin(x-\phi)$ with $0^\circ < \phi < 90^\circ$ and $R>0,$ what is the value of $\phi?$

#### Explanation

The difference formula for sine gives

$$


\begin{aligned}𝑅sin⁡(𝑥−𝜙) & =𝑅(sin⁡𝑥cos⁡𝜙−cos⁡𝑥sin⁡𝜙) \\ & =𝑅cos⁡𝜙sin⁡𝑥−𝑅sin⁡𝜙cos⁡𝑥.\end{aligned}


$$

Therefore, by writing the given expression in the amplitude-phase form

$$


2 \sin x - 2 \cos x = R\sin(x-\phi),


$$

we get the following identity:

$$


2 \sin x - 2 \cos x = (R \cos \phi ) \sin x - (R \sin \phi ) \cos x


$$

Equating the coefficients of $\sin x$ and $\cos x,$ we get the following system of equations:

$$


\begin{aligned}𝑅cos⁡𝜙=2 \\ 𝑅sin⁡𝜙=2\end{aligned}


$$

Dividing the second equation by the first, we get

$$


\begin{aligned}\frac{𝑅sin⁡𝜙}{𝑅cos⁡𝜙} & =\frac{2}{2} \\ tan⁡𝜙 & =1 \\ 𝜙 & =arctan⁡(1) \\ & =45^{∘}.\end{aligned}


$$

### Example: Finding the Amplitude-Phase Form for Sine

#### Question

Write $3\sin x-2\cos x$ in the form $R\sin(x-\phi)$ with $\phi \in \left(0, \dfrac{\pi}{2} \right)$. Round $\phi$ to $3$ decimal places.

#### Explanation

The difference formula for sine gives

$$


\begin{aligned}𝑅sin⁡(𝑥−𝜙) & =𝑅(sin⁡𝑥cos⁡𝜙−cos⁡𝑥sin⁡𝜙) \\ & =𝑅cos⁡𝜙sin⁡𝑥−𝑅sin⁡𝜙cos⁡𝑥.\end{aligned}


$$

Therefore, by writing the given expression in the amplitude-phase form

$$


3 \sin x - 2 \cos x = R\sin(x-\phi) ,


$$

we get the following identity:

$$


3 \sin x - 2 \cos x = (R \cos \phi ) \sin x - (R \sin \phi )\cos x


$$

Equating the coefficients of $\sin x$ and $\cos x,$ we get the following system of equations:

$$


\begin{aligned}𝑅cos⁡𝜙=3 \\ 𝑅sin⁡𝜙=2\end{aligned}


$$

Dividing the second equation by the first, we get

$$


\begin{aligned}\frac{𝑅sin⁡𝜙}{𝑅cos⁡𝜙} & =\frac{2}{3} \\ tan⁡𝜙 & =\frac{2}{3} \\ 𝜙 & =arctan⁡(\frac{2}{3}) \\ & ≈0.588\,rad\end{aligned}


$$

rounded to three decimal places.

Now, we find the amplitude $R.$ Squaring the first and the second equations of the system and adding the results together, we get

$$


\begin{aligned}(𝑅cos⁡𝜙)^{2}+(𝑅sin⁡𝜙)^{2} & =(3)^{2}+(2)^{2} \\ 𝑅^{2}(cos^{2}⁡𝜙+sin^{2}⁡𝜙) & =9+4 \\ 𝑅^{2} & =13 \\ 𝑅 & =\sqrt{13}.\end{aligned}


$$

Note that we only considered the positive root, since $R>0.$

Finally, we can write the initial expression in amplitude-phase form as follows:

$$


3\sin(x)-2\cos(x) \approx \sqrt{13} \sin \left(x - 0.588 \right)


$$

### The Amplitude-Phase Form For Cosine

We've been using the amplitude-phase form for sine, but there is also an amplitude-phase form for cosine. If $a$ and $b$ are positive real numbers, then the expression

$$


a \cos x \pm b \sin x


$$

can be written in the form

$$


{\color{blue}R} \cos(x \mp {\color{red}\phi} )


$$

for some ${\color{blue}R}>0$ and ${\color{red}\phi} \in \left(0, \dfrac{\pi}{2}\right).$

Note that the sign in the last formula flips due to the identity $\cos(x \mp \phi) = \cos x \cos \phi \pm \sin x \sin \phi,$ which reverses the sign when expanding.

Writing this more explicitly, we have

$$


\begin{aligned}𝑎cos⁡𝑥+𝑏sin⁡𝑥 & =𝑅cos⁡(𝑥−𝜙) \\ 𝑎cos⁡𝑥−𝑏sin⁡𝑥 & =𝑅cos⁡(𝑥+𝜙).\end{aligned}


$$

For example, let's write the expression

$$


4\sin{x}+\cos{x}


$$

in amplitude-phase form with cosine. We start by expanding out the amplitude-phase form using the difference formula for cosine:

$$


\begin{aligned}𝑅cos⁡(𝑥−𝜙) & =𝑅(cos⁡𝑥cos⁡𝜙+sin⁡𝑥sin⁡𝜙) \\ & =𝑅cos⁡𝜙cos⁡𝑥+𝑅sin⁡𝜙sin⁡𝑥\end{aligned}


$$

So, we obtain the following equation:

$$


\begin{aligned}4sin⁡𝑥+cos⁡𝑥 & =𝑅cos⁡(𝑥−𝜙) \\ 4sin⁡𝑥+cos⁡𝑥 & =(𝑅sin⁡𝜙)sin⁡𝑥+(𝑅cos⁡𝜙)cos⁡𝑥\end{aligned}


$$

First, we find the phase $\phi.$ Equating the coefficients of $\sin x$ and $\cos x,$ we have the following system:

$$


\begin{aligned}𝑅sin⁡𝜙=4 \\ 𝑅cos⁡𝜙=1\end{aligned}


$$

Dividing the first equation by the second one, we get

$$


\begin{aligned}\frac{𝑅sin⁡𝜙}{𝑅cos⁡𝜙} & =\frac{4}{1} \\ tan⁡𝜙 & =4 \\ 𝜙 & =arctan⁡(4) \\ & ≈1.326\,rad\end{aligned}


$$

rounded to three decimal places.

Now, we find the amplitude $R.$ Squaring the first and the second equations of the system and adding the results together, we get

$$


\begin{aligned}(𝑅sin⁡𝜙)^{2}+(𝑅cos⁡𝜙)^{2} & =4^{2}+1^{2} \\ 𝑅^{2}(sin^{2}⁡𝜙+cos^{2}⁡𝜙) & =16+1 \\ 𝑅^{2} & =17 \\ 𝑅 & =\sqrt{17}\end{aligned}


$$

Note that we only considered the positive root, since $R>0.$

Finally, we can write the initial expression in amplitude-phase form as follows:

$$


\begin{aligned}4sin⁡𝑥+cos⁡𝑥 & =\sqrt{17}cos⁡(𝑥−arctan⁡(4)) \\ & ≈\sqrt{17}cos⁡(𝑥−1.326)\end{aligned}


$$

### Example: Finding the Amplitude-Phase Form for Cosine

#### Question

Write $3\cos x - \sqrt{3}\sin x$ in the form $R\cos(x+\phi)$ with $\phi \in \left(0, \dfrac{\pi}{2} \right).$

#### Explanation

The difference formula for cosine gives

$$


\begin{aligned}𝑅cos⁡(𝑥+𝜙) & =𝑅(cos⁡𝑥cos⁡𝜙−sin⁡𝑥sin⁡𝜙) \\ & =𝑅cos⁡𝜙cos⁡𝑥−𝑅sin⁡𝜙sin⁡𝑥.\end{aligned}


$$

Therefore, by writing the given expression in the amplitude-phase form

$$


3\cos x - \sqrt{3}\sin x = R\cos(x+\phi)


$$

we get the following identity:

$$


3\cos x - \sqrt{3}\sin x = (R \cos \phi) \cos x -( R \sin \phi )\sin x


$$

Equating the coefficients of $\sin x$ and $\cos x,$ we get the following system of equations:

$$


\begin{aligned}𝑅cos⁡𝜙=3 \\ 𝑅sin⁡𝜙=\sqrt{3}\end{aligned}


$$

Dividing the second equation by the first, we get

$$


\begin{aligned}\frac{𝑅sin⁡𝜙}{𝑅cos⁡𝜙} & =\frac{\sqrt{3}}{3} \\ tan⁡𝜙 & =\frac{\sqrt{3}}{3} \\ 𝜙 & =arctan⁡(\frac{\sqrt{3}}{3}) \\ & =\frac{𝜋}{6}.\end{aligned}


$$

Now, we find the amplitude $R.$ Squaring the first and the second equations of the system and adding the results together, we get

$$


\begin{aligned}(𝑅sin⁡𝜙)^{2}+(𝑅cos⁡𝜙)^{2} & =3^{2}+(\sqrt{3})^{2} \\ 𝑅^{2}(sin^{2}⁡𝜙+cos^{2}⁡𝜙) & =9+3 \\ 𝑅^{2} & =12 \\ 𝑅 & =\sqrt{12} \\ & =2\sqrt{3}.\end{aligned}


$$

Note that we only consider the positive root since $R>0.$

Finally, we can write the initial expression in amplitude-phase form as follows:

$$


3\cos x - \sqrt{3}\sin x = 2\sqrt{3}\cos\left(x + \dfrac{\pi}{6}\right)


$$
