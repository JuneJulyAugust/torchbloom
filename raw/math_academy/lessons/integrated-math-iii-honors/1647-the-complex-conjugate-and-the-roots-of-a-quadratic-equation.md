# The Complex Conjugate and the Roots of a Quadratic Equation

Source: https://www.mathacademy.com/topics/1647?courseId=101
Topic ID: 1647

## Prerequisites

- [Solving Quadratic Equations With Complex Roots](../algebra-ii/895-solving-quadratic-equations-with-complex-roots.md)
- [Special Properties of the Complex Conjugate](./905-special-properties-of-the-complex-conjugate.md)

## Lesson

### Introduction

If we know one complex root of a quadratic equation, we can find the other root by taking the complex conjugate. More precisely, we have the following theorem:

*If $z=a+\textrm{i}b$ is a root of a quadratic equation with real coefficients, then the complex conjugate $\overline{z}=a-\textrm{i}b$ is also a root of the quadratic equation.*

For example, suppose we know that $z = 1 + \textrm{i}$ is a root of the quadratic equation $z^2 -2z+2=0.$ Then we can conclude that $\overline{z} = 1-\textrm{i}$ is also a root of the equation!

We can check that this is true by substituting $\overline{z} = 1-\textrm{i}$ into the equation as follows:

$$


\begin{aligned}\overset{𝑧}{–}^{2}−2\overset{𝑧}{–}+2 & =0 \\ (1−i)^{2}−2(1−i)+2 & =0 \\ 1−2i+i^{2}−2+2i+2 & =0 \\ 1−2i−1−2+2i+2 & =0 \\ 0 & =0.\,✓\end{aligned}


$$

Furthermore, since a quadratic equation can have at most $2$ distinct roots, the number $z = 1+\textrm{i}$ and its complex conjugate $\overline{z}=1-\textrm{i}$ are the *only* roots of this quadratic equation.

**Caution:** The theorem only applies to a quadratic equation which has real coefficients. For example, the theorem does *not* apply to the quadratic equation $z^2 + z + \textrm i = 0$ because the coefficient $\textrm i$ is not a real coefficient.

**Note:** A proof of this theorem will be given at the end of the lesson. But for now, let's focus on applying the theorem.

### Example: Finding the Second Complex Root of a Quadratic Equation Given the First Root

#### Question

A quadratic equation with real coefficients has a root $x=5+4\textrm{i}.$ What is the other root?

#### Explanation

We're given that the quadratic equation has real coefficients and that $x=5+4\textrm{i}$ is a root. Therefore, its complex conjugate $x=5-4\textrm{i}$ is also a root.

### Example: Finding a Quadratic Equation Given an Imaginary Root and Its Leading Coefficient

#### Question

A quadratic equation in the variable $x$ with real coefficients has a root $x=-3\textrm{i}.$ Given that the coefficient of $x^2$ in the equation is $2,$ find the equation.

#### Explanation

Since the quadratic equation has real coefficients and $x=-3\textrm{i}$ is a root, its conjugate $x = 3\textrm{i}$ must also be a root. Therefore, using the zero product property, we can write a quadratic equation with the required roots as follows:

$$


(x-3\textrm{i})(x+3\textrm{i})= 0


$$

Multiplying out the parentheses and simplifying gives

$$


\begin{aligned}𝑥^{2}−(3i)^{2} & =0 \\ 𝑥^{2}−9(−1) & =0 \\ 𝑥^{2}+9 & =0.\end{aligned}


$$

This equation has roots $x=\pm 3\textrm{i},$ but the coefficient of $x^2$ is not $2.$ Therefore, to find the desired equation, we multiply the equation above by $2.$ This gives

$$


\begin{aligned}2(𝑥^{2}+9) & =0 \\ 2𝑥^{2}+18 & =0.\end{aligned}


$$

### Example: Finding a Quadratic Equation Given a Complex Root and Its Leading Coefficient

#### Question

A quadratic equation in the variable $x$ with real coefficients has a root $x=6-8\textrm{i}.$ Given that the coefficient of $x^2$ in the equation is $-1,$ find the equation.

#### Explanation

Since the quadratic equation has real coefficients and $x=6-8\textrm{i}$ is a root, its conjugate $x=6+8\textrm{i}$ must also be a root. Therefore, using the zero product property, we can write a quadratic equation with the required roots as follows:

$$


\Bigl(x-(6-8\textrm{i})\Bigr)\Bigl(x-(6+8\textrm{i})\Bigr) = 0


$$

By expanding the parentheses, we can write the equation in standard form as follows:

$$


\begin{aligned}𝑥^{2}−𝑥(6+8i)−𝑥(6−8i)+(6−8i)(6+8i) & =0 \\ 𝑥^{2}−6𝑥−8𝑥i−6𝑥+8𝑥i+36−64i^{2} & =0 \\ 𝑥^{2}−12𝑥+36+64 & =0 \\ 𝑥^{2}−12𝑥+100 & =0\end{aligned}


$$

This equation has roots $x= 6 \pm 8\textrm{i},$ but the coefficient of $x^2$ is not $-1.$ Therefore, to find the desired equation, we multiply the equation above by $-1.$ This gives

$$


\begin{aligned}−(𝑥^{2}−12𝑥+100) & =0 \\ −𝑥^{2}+12𝑥−100 & =0.\end{aligned}


$$

### A Proof of the Theorem

In this lesson, we have used the following theorem:

*If $z$ is a root of a quadratic equation with real coefficients, then the complex conjugate $\overline{z}$ is also a root of the quadratic equation.*

Now, let's prove the theorem. Suppose that $a,b,c$ are real numbers and that $z$ is a root of $ax^2 +bx +c = 0.$ Then, we have

$$


az^2 +bz +c = 0.


$$

If we take the complex conjugate of this equation, we get

$$


\overline{ az^2+ bz+c} = \overline{0}


$$

and since $\overline{0} = 0,$ we have

$$


\overline{ az^2+ bz+c} = 0.


$$

We can now take the complex conjugate of each term individually. This gives

$$


\overline{az^2} + \overline{bz} +\overline{c} = 0,


$$

and since $a,b,$ and $c$ are real, we have

$$


a\overline{z^2} + b\overline{z} +c = 0.


$$

Finally, we use the fact that $\overline{z^2} = (\overline{z})^2,$ so our equation becomes

$$


a(\overline{z})^2 + b\overline{z} +c = 0.


$$

This shows that $\overline{z}$ is also a root of $ax^2 +bx +c = 0.$
