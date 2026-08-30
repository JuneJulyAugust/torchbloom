# Trigonometric Equations Containing Transformed Cosine Functions

Source: https://www.mathacademy.com/topics/921?courseId=101
Topic ID: 921

## Prerequisites

- [General Solutions of Trigonometric Equations With Transformed Functions](./1259-general-solutions-of-trigonometric-equations-with-transformed-functions.md)

## Lesson

### Introduction

Suppose we want to find all of the solutions to

$$


\cos\left(x+\dfrac{\pi}{3}\right) = \dfrac{1}{2}, \qquad -\pi \leq x < \pi.


$$

Notice that the equation contains a transformed cosine function.

We know that the general solution to the elementary equation $\cos{X} = \dfrac{1}{2}$ is given by

$$


\begin{aligned}𝑋 & =\frac{𝜋}{3}+2𝑛𝜋, & \, & \, & 𝑋 & =\frac{5𝜋}{3}+2𝑛𝜋,\end{aligned}


$$

where $n$ is assumed to be any integer.

To find the general solution of the transformed cosine equation, we replace $X$ with the input of the cosine function, which is $x + \dfrac{\pi}{3}$ in this case. This gives the general solution

$$


x+\dfrac{\pi}{3} = \dfrac{\pi}{3} + 2n\pi, \qquad\qquad x+\dfrac{\pi}{3} = \dfrac{5\pi}{3}+ 2n\pi.


$$

We now solve the above two equations for $x,$ as follows:

$$


\begin{aligned}𝑥 & =2𝑛𝜋 & \, & \, & 𝑥 & =\frac{4𝜋}{3}+2𝑛𝜋 \\ & & \, & \, & 𝑥 & =\frac{4𝜋}{3}+\frac{6𝑛𝜋}{3} \\ & & \, & \, & 𝑥 & =\frac{2𝜋(2+3𝑛)}{3}\end{aligned}


$$

Now, we set $n = 0, \pm1, \pm2, \ldots$ until we have generated all solutions in the domain $-\pi \leq x < \pi.$

- Setting $n=0$ gives $x=0$ and $x=\dfrac{4\pi}{3}.$ We reject the solution $\dfrac{4\pi}{3}$ since it lies outside the domain of interest.

- Setting $n=-1$ gives $x=-2\pi$ and $x=-\dfrac{2\pi}{3}.$ We reject the solution $-2\pi$ since it lies outside the domain of interest.

All other values of $n$ generate solutions outside the domain $-\pi \leq x < \pi.$ So, the solutions $x_1$ and $x_2$ (written in ascending order) are

$$


x_1 = -\dfrac{2\pi}{3},\qquad x_2 = 0.


$$

### Example: Solving a Trigonometric Equation Containing the Cosine Function Transformed by One Operation

#### Question

Consider the equation $\cos{2x} = \dfrac{\sqrt{2}}{2}$ for $0\leq x < 2\pi.$ If the solutions $x_1, x_2, x_3$ and $x_4$ are written in ascending order, what is the value of $x_2\cdot x_3?$

#### Explanation

We will find the general solution to the equation, and then generate all of the solutions in the required domain.

The general solution to our equation is given by

$$


\begin{aligned}2𝑥 & =\frac{𝜋}{4}+2𝑛𝜋, & \, & \, & 2𝑥 & =\frac{7𝜋}{4}+2𝑛𝜋.\end{aligned}


$$

Solving our two equations for $x$ gives the following:

$$


\begin{aligned}𝑥 & =\frac{𝜋}{8}+𝑛𝜋 & \, & \, & 𝑥 & =\frac{7𝜋}{8}+𝑛𝜋 \\ 𝑥 & =\frac{𝜋}{8}+\frac{8𝑛𝜋}{8} & \, & \, & 𝑥 & =\frac{7𝜋}{8}+\frac{8𝑛𝜋}{8} \\ 𝑥 & =\frac{(8𝑛+1)𝜋}{8} & \, & \, & 𝑥 & =\frac{(8𝑛+7)𝜋}{8}\end{aligned}


$$

We set $n=0, \pm 1, \pm 2,\ldots,$ until we have generated all solutions in the domain $0 \leq x \lt 2\pi.$

- Setting $n=0$ gives $x=\dfrac{\pi}{8}$ and $x=\dfrac{7\pi}{8}.$

- Setting $n=1$ gives $x=\dfrac{9\pi}{8}$ and $x=\dfrac{15\pi}{8}.$

All other values of $n$ generate solutions outside the domain $0 \leq x \lt 2\pi.$ So, the solutions $x_1, x_2, x_3$ and $x_4$ (written in ascending order) are

$$


x = \dfrac{\pi}{8}, \, \dfrac{7\pi}{8}, \, \dfrac{9\pi}{8}, \, \dfrac{15\pi}{8}.


$$

Finally,

$$


x_2\cdot x_3 = \dfrac{7\pi}{8} \cdot \dfrac{9\pi}{8} = \dfrac{63\pi^2}{64}.


$$

### Example: Solving a Trigonometric Equation Containing the Cosine Function Transformed by Multiple Operations

#### Question

Solve the equation $-2\sqrt{3}\cos\left(2x+60^\circ\right) - 3 = 0$ for $0^\circ\leq x < 360^\circ.$

#### Explanation

First, we rearrange the equation, as follows:

$$


\begin{aligned}−2\sqrt{√3}cos⁡(2𝑥+60^{∘})−3 & =0 \\ −2\sqrt{√3}cos⁡(2𝑥+60^{∘}) & =3 \\ cos⁡(2𝑥+60^{∘}) & =−\frac{3}{2\sqrt{√3}} \\ cos⁡(2𝑥+60^{∘}) & =−\frac{\sqrt{√3}}{2}\end{aligned}


$$

We will find the general solution to the equation and then generate all of the solutions in the required domain.

The general solution to our equation is

$$


\begin{aligned}2𝑥+60^{∘} & =150^{∘}+𝑛⋅360^{∘}, & \, & \, & 2𝑥+60^{∘} & =210^{∘}+𝑛⋅360^{∘}.\end{aligned}


$$

Solving the two equations above for $x$ gives the following:

$$


\begin{aligned}2𝑥 & =150^{∘}−60^{∘}+𝑛⋅360^{∘} & \, & \, & 2𝑥 & =210^{∘}−60^{∘}+𝑛⋅360^{∘} \\ 2𝑥 & =90^{∘}+𝑛⋅360^{∘} & \, & \, & 2𝑥 & =150^{∘}+𝑛⋅360^{∘} \\ 𝑥 & =45^{∘}+𝑛⋅180^{∘} & \, & \, & 𝑥 & =75^{∘}+𝑛⋅180^{∘}\end{aligned}


$$

We set $n=0, \pm 1, \pm 2,\ldots$ until we have generated all solutions in the domain $0^\circ \leq x \lt 360^\circ.$

- Setting $n=0$ gives $x=45^\circ$ and $x=75^\circ.$

- Setting $n=1$ gives $x=225^\circ$ and $x=255^\circ.$

All other values of $n$ generate solutions outside the domain $0^\circ \leq x \lt 360^\circ.$ So, the solutions $x_1,x_2,x_3,x_4$ (written in ascending order) are

$$


x_1 = 45^\circ,\quad x_2 = 75^\circ,\quad x_3 = 225^\circ,\quad x_4= 255^\circ .


$$

### Example: Solving a Trigonometric Equation Containing a Transformed Cosine Function Under a Modified Domain

#### Question

Solve the equation $\cos\left(2x+\dfrac{\pi}{4}\right) = -\dfrac{1}{2}$ for $-2\pi < x \leq 0.$

#### Explanation

We will find the general solution to the equation and then generate all of the solutions in the required domain.

The general solution to our equation is

$$


\begin{aligned}2𝑥+\frac{𝜋}{4} & =−\frac{2𝜋}{3}+2𝑛𝜋, & \, & \, & 2𝑥+\frac{𝜋}{4} & =\frac{2𝜋}{3}+2𝑛𝜋.\end{aligned}


$$

Solving the two equations above for $x$ gives the following:

$$


\begin{aligned}2𝑥 & =−\frac{11𝜋}{12}+2𝑛𝜋 & \, & \, & 2𝑥 & =\frac{5𝜋}{12}+2𝑛𝜋 \\ 𝑥 & =−\frac{11𝜋}{24}+𝑛𝜋 & \, & \, & 𝑥 & =\frac{5𝜋}{24}+𝑛𝜋 \\ 𝑥 & =\frac{(24𝑛−11)𝜋}{24} & \, & \, & 𝑥 & =\frac{(24𝑛+5)𝜋}{24}\end{aligned}


$$

We set $n=0, \pm 1, \pm 2,\ldots$ until we have generated all solutions in the domain $-2\pi < x \leq 0.$

- Setting $n=-2$ gives $x=-\dfrac{59\pi}{24}$ and $x=-\dfrac{43\pi}{24}.$ We reject the solution $-\dfrac{59\pi}{24}$ since it lies outside the domain of interest.

- Setting $n=-1$ gives $x=-\dfrac{35\pi}{24}$ and $x=-\dfrac{19\pi}{24}.$

- Setting $n=0$ gives $x=-\dfrac{11\pi}{24}$ and $x=\dfrac{5\pi}{24}.$ We reject the solution $\dfrac{5\pi}{24}$ since it lies outside the domain of interest.

All other values of $n$ generate solutions outside the domain $-2\pi < x \leq 0.$ So, the solutions $x_1,x_2,x_3,x_4$ (written in ascending order) are

$$


x_1 = -\dfrac{43\pi}{24}, \quad x_2=-\dfrac{35\pi}{24}, \quad x_3 = -\dfrac{19\pi}{24}, \quad x_4 = -\dfrac{11\pi}{24}.


$$
