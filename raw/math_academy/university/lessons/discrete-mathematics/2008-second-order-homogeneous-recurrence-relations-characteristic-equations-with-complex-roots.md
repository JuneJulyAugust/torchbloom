# Second-Order Homogeneous Recurrence Relations: Characteristic Equations with Complex Roots

Source: https://www.mathacademy.com/topics/2008?courseId=109
Topic ID: 2008

## Prerequisites

- [De Moivre's Theorem](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/925-de-moivre-s-theorem.md)
- [The Complex Conjugate and the Roots of a Quadratic Equation](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1647-the-complex-conjugate-and-the-roots-of-a-quadratic-equation.md)
- [Second-Order Homogeneous Recurrence Relations: Characteristic Equations with Distinct Real Roots](./2007-second-order-homogeneous-recurrence-relations-characteristic-equations-with-distinct-real-roots.md)

## Lesson

### Introduction

Recall that when the characteristic equation of a second-order linear homogeneous recurrence relation has two distinct real roots $\lambda_1$ and $\lambda_2,$ the general solution is

$$



a_n = A \cdot \lambda_1^n + B \cdot \lambda_2^n.



$$

As it turns out, this also works in cases where $\lambda_1$ and $\lambda_2$ are complex.

For example, suppose that we want to solve the following recurrence relation:

$$



a_{n} = 6a_{n-1} - 34a_{n-2}



$$

Assuming $a_n=\lambda^n,$ we obtain

$$



a_{n-1}= \lambda^{n-1},\qquad a_{n-2}= \lambda^{n-2}.



$$

Substituting the above into our recurrence relation gives

$$



\begin{aligned}𝜆^{𝑛} & =6𝜆^{𝑛−1}−34𝜆^{𝑛−2}\end{aligned}



$$

which can be written as follows:

$$



\begin{aligned}𝜆^{𝑛}−6𝜆^{𝑛−1}+34𝜆^{𝑛−2} & =0 \\ 𝜆^{𝑛−2}(𝜆^{2}−6𝜆+34) & =0\end{aligned}



$$

The characteristic equation is

$$



\lambda^2-6\lambda + 34 = 0.



$$

This equation can be solved by completing the square:

$$



\begin{aligned}𝜆^{2}−6𝜆+34 & =0 \\ (𝜆^{2}−6𝜆+9)−9+34 & =0 \\ (𝜆−3)^{2}+25 & =0 \\ (𝜆−3)^{2} & =−25 \\ 𝜆−3 & =±5i \\ 𝜆 & =3±5i\end{aligned}



$$

Therefore, the general solution is

$$



a_n = C \cdot (3 + 5\text{i})^n + D \cdot (3 - 5\text{i})^n,



$$

where $C$ and $D$ are complex conjugate arbitrary constants.

### Example: Finding and Solving a Characteristic Equation

#### Question

Consider the recurrence relation $a_{n} = -8a_{n-1} - 20a_{n-2}.$ If $a_n = \lambda^n$ is a nonzero solution, then what are the possible values of $\lambda?$

#### Explanation

Assuming $a_n=\lambda^n,$ we obtain

$$



a_{n-1}= \lambda^{n-1},\qquad a_{n-2}= \lambda^{n-2}.



$$

Substituting the above into our recurrence relation gives

$$



\begin{aligned}𝜆^{𝑛} & =−8𝜆^{𝑛−1}−20𝜆^{𝑛−2}\end{aligned}



$$

which can be written as follows:

$$



\begin{aligned}𝜆^{𝑛}+8𝜆^{𝑛−1}+20𝜆^{𝑛−2} & =0 \\ 𝜆^{𝑛−2}(𝜆^{2}+8𝜆+20) & =0\end{aligned}



$$

The characteristic equation is

$$



\lambda^2+8\lambda + 20 = 0.



$$

This equation can be solved by completing the square:

$$



\begin{aligned}𝜆^{2}+8𝜆+20 & =0 \\ (𝜆^{2}+8𝜆+16)−16+20 & =0 \\ (𝜆+4)^{2}+4 & =0 \\ (𝜆+4)^{2} & =−4 \\ 𝜆+4 & =±2i \\ 𝜆 & =−4±2i\end{aligned}



$$

Therefore, $\lambda = -4\pm 2\text{i}$ are the complex roots of the characteristic equation.

### Simplifying the General Solution Using Complex Numbers in Polar Form

Suppose that the characteristic equation of a second-order homogeneous recurrence relation has the complex roots

$$



\lambda_1 = a + \text{i}b, \qquad \lambda_2 = a - \text{i}b.



$$

Since the characteristic equation typically has real coefficients, the roots $\lambda_1$ and $\lambda_2$ are complex conjugates.

The general solution to the recurrence relation is

$$



\begin{aligned}𝑎_{𝑛} & =𝐶𝜆_{𝑛1}+𝐷𝜆_{𝑛2} \\ & =𝐶(𝑎+i𝑏)^{𝑛}+𝐷(𝑎−i𝑏)^{𝑛},\end{aligned}



$$

where the constants $C$ and $D$ are complex conjugates.

This solution might seem strange as recurrence relations usually involve real numbers only. Is it possible to express this general solution using only real numbers?

To answer this, suppose we express our solutions $\lambda_1$ and $\lambda_2$ in polar form:

$$



\begin{aligned}𝜆_{1}=𝑟(cos⁡𝜃+isin⁡𝜃),\,𝜆_{2}=𝑟(cos⁡𝜃−isin⁡𝜃)\end{aligned}



$$

where

$$



r = |\lambda_1|, \qquad \theta = \arg(\lambda_1).



$$

Therefore, using De Moivre's theorem, we can write the general solution to the recurrence relation as follows:

$$



\begin{aligned}𝑎_{𝑛} & =𝐶𝜆_{𝑛1}+𝐷𝜆_{𝑛2} \\ & =𝐶[𝑟(cos⁡𝜃+isin⁡𝜃)]^{𝑛}+𝐷[𝑟(cos⁡(𝜃)−isin⁡(𝜃))]^{𝑛} \\ & =𝐶[𝑟^{𝑛}(cos⁡(𝑛𝜃)+isin⁡(𝑛𝜃))]+𝐷[𝑟^{𝑛}(cos⁡(𝑛𝜃)−isin⁡(𝑛𝜃))] \\ & =𝑟^{𝑛}((𝐶+𝐷)cos⁡(𝑛𝜃)+i(𝐶−𝐷)sin⁡(𝑛𝜃))\end{aligned}



$$

Finally, if we define the real constants $A$ and $B$ as

$$



A = C+D, \qquad B = \textrm i(C-D),



$$

we obtain the general solution

$$



a_n = r^n \left( A \cos\left(n\theta\right) + B \sin\left(n\theta\right) \right).



$$

Thus, we have managed to write the general solution in terms of real numbers only.

### Example: Finding the General Solution to a Second-Order Recurrence Relation

#### Question

Find the general solution to the difference equation $a_n + 100a_{n-2} =0.$

#### Explanation

Let $a_n=\lambda^n.$ Then, we have

$$



a_{n-1} = \lambda^{n-1}, \qquad a_{n-2} = \lambda^{n-2}.



$$

Substituting the above into our difference equation gives

$$



\begin{aligned}𝜆^{𝑛}+100𝜆^{𝑛−2} & =0 \\ 𝜆^{𝑛−2}(𝜆^{2}+100) & =0.\end{aligned}



$$

The characteristic equation is

$$



\begin{aligned}𝜆^{2}+100 & =0 \\ 𝜆^{2} & =−100 \\ 𝜆 & =±10i.\end{aligned}



$$

So, we have $\lambda_1 = 10\textrm i$ and $\lambda_2 = -10\textrm i.$

Expressing our solutions in polar form, we get

$$



\begin{aligned}𝜆_{1} & =10(cos⁡(\frac{𝜋}{2})+isin⁡(\frac{𝜋}{2})), \\ 𝜆_{2} & =10(cos⁡(\frac{𝜋}{2})−isin⁡(\frac{𝜋}{2})).\end{aligned}



$$

Therefore, using De Moivre's theorem, we can write the general solution to the difference equation as

$$



\begin{aligned}𝑎_{𝑛} & =𝐶𝜆_{𝑛1}+𝐷𝜆_{𝑛2} \\ & =𝐶[10(cos⁡(\frac{𝜋}{2})+isin⁡(\frac{𝜋}{2}))]^{𝑛}+𝐷[10(cos⁡(\frac{𝜋}{2})−isin⁡(\frac{𝜋}{2}))]^{𝑛} \\ & =𝐶[10^{𝑛}(cos⁡(\frac{𝑛𝜋}{2})+isin⁡(\frac{𝑛𝜋}{2}))]+𝐷[10^{𝑛}(cos⁡(\frac{𝑛𝜋}{2})−isin⁡(\frac{𝑛𝜋}{2}))] \\ & =10^{𝑛}(𝐴cos⁡(\frac{𝑛𝜋}{2})+𝐵sin⁡(\frac{𝑛𝜋}{2})),\end{aligned}



$$

where

$$



A = C+D, \qquad B = \textrm i(C-D).



$$

### Example: Solving Second-Order Recurrence Relations With Initial Conditions Given the General Solution

#### Question

Consider the recurrence relation

$$



a_n = -6a_{n-1} - 12a_{n-2}, \quad a_0 = - 1, \quad a_1=3+\sqrt{3}.



$$

Given that the solution takes the form

$$



a_n = \big(2\sqrt{3}\big)^n \left( A\cos\left(\dfrac{5n\pi}{6}\right) + B\sin\left(\dfrac{5n\pi}{6}\right) \right),



$$

find the value of $A + B.$

#### Explanation

The general solution to the recurrence relation is

$$



a_n = \big(2\sqrt{3}\big)^n \left( A\cos\left(\dfrac{5n\pi}{6}\right) + B\sin\left(\dfrac{5n\pi}{6}\right) \right).



$$

We find the constants $A$ and $B$ using the initial conditions.

- Substituting $a_0 = -1$ into the general solution gives

- Substituting $a_1=3+\sqrt{3}$ and $A=-1$ into the general solution gives

Therefore,

$$



A + B = -1 + 1 = 0.



$$

Finally, the solution is

$$



\begin{aligned}𝑎_{𝑛} & =(2\sqrt{3})^{𝑛}(sin⁡(\frac{5𝑛𝜋}{6})−cos⁡(\frac{5𝑛𝜋}{6})).\end{aligned}



$$

### Example: Solving Second-Order Recurrence Relations With Initial Conditions

#### Question

Solve the recurrence relation

$$



a_n =2a_{n-1} - 2a_{n-2}, \quad a_0=2, \quad a_1=5.



$$

#### Explanation

Moving all terms of our recurrence relation to the left-hand side, we obtain

$$



a_n - 2a_{n-1} + 2a_{n-2} = 0.



$$

First, we find the roots of the characteristic equation:

$$



\lambda^2 - 2\lambda + 2 = 0



$$

This equation can be solved by completing the square:

$$



\begin{aligned}𝜆^{2}−2𝜆+2 & =0 \\ (𝜆^{2}−2𝜆+1)−1+2 & =0 \\ (𝜆−1)^{2}+1 & =0 \\ (𝜆−1)^{2} & =−1 \\ 𝜆−1 & =±i \\ 𝜆 & =1±i\end{aligned}



$$

So, we have

$$



\lambda_1 = 1 + \text{i}, \qquad \lambda_2 = 1 - \text{i}.



$$

Expressing our solutions in polar form, we get

$$



\begin{aligned}𝜆_{1} & =\sqrt{2}(cos⁡(\frac{𝜋}{4})+isin⁡(\frac{𝜋}{4})), \\ 𝜆_{2} & =\sqrt{2}(cos⁡(\frac{𝜋}{4})−isin⁡(\frac{𝜋}{4})).\end{aligned}



$$

So, the general solution to the recurrence relation is

$$



a_n = \big(\sqrt{2}\big)^n \left(A\cos\left(\dfrac{n\pi}{4}\right) + B\sin\left(\dfrac{n\pi}{4}\right)\right).



$$

We now find the constants $A$ and $B$ using the initial conditions:

- Substituting $a_0 = 2$ into the general solution gives

- Substituting $a_1=5$ and $A=2$ into the general solution gives

Therefore, the solution is

$$



a_n = \big(\sqrt{2}\big)^n \left(2\cos\left(\dfrac{n\pi}{4}\right) + 3\sin\left(\dfrac{n\pi}{4}\right)\right).



$$
