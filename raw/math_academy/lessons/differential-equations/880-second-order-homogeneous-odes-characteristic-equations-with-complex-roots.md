# Second-Order Homogeneous ODEs: Characteristic Equations With Complex Roots

Source: https://www.mathacademy.com/topics/880?courseId=61
Topic ID: 880

## Prerequisites

- [Second-Order Homogeneous ODEs: Characteristic Equations With Distinct Real Roots](./614-second-order-homogeneous-odes-characteristic-equations-with-distinct-real-roots.md)
- [Solving Quadratic Equations With Complex Roots](../algebra-ii/895-solving-quadratic-equations-with-complex-roots.md)
- [Euler's Formula](../integrated-math-iii-honors/898-euler-s-formula.md)

## Lesson

### Introduction

Sometimes, the characteristic equation of a second-order homogeneous ODE has **complex roots**. Let's see how to find the solution in this case.

We will solve the following differential equation:

$$


\frac{\textrm{d}^2 y}{\textrm{d} x^2} + 4y =0.


$$

**Step 1:** Find the characteristic equation.

Assuming a solution of the form $y=e^{\lambda x},$ we find the derivatives:

$$


\dfrac{\textrm{d}y}{\textrm{d}x} = \lambda e^{\lambda x}, \qquad \dfrac{\textrm{d}^2y}{\textrm{d}x^2} = \lambda^2 e^{\lambda x}.


$$

Substituting these into the ODE gives the **characteristic equation**:

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑥}+4𝑒^{𝜆𝑥} & =0 \\ 𝑒^{𝜆𝑥}(𝜆^{2}+4) & =0 \\ 𝜆^{2}+4 & =0\,(since 𝑒^{𝜆𝑥}≠0).\end{aligned}


$$

**Step 2:** Solve for the characteristic roots.

$$


\begin{aligned}𝜆^{2} & =−4 \\ 𝜆 & =±\sqrt{√−4} \\ 𝜆 & =±2i.\end{aligned}


$$

The roots are a *complex conjugate pair*. Since the roots are distinct, the general solution is a linear combination of the corresponding exponentials:

$$


y = Ae^{2\textrm{i}x} + Be^{-2\textrm{i}x}.


$$

On the next slide, we will use *Euler's formula* to convert this into a more useful real-valued form.

### Convert the Complex Solution to a Real-Valued Solution

Recall our solution from the previous slide:

$$


y = Ae^{2\textrm{i}x} + Be^{-2\textrm{i}x}.


$$

We use **Euler's formula**, which states

$$


e^{\textrm{i}\theta} = \cos\theta + \textrm{i}\sin\theta,


$$

to rewrite the exponentials:

$$


\begin{aligned}𝑦 & =𝐴(cos⁡2𝑥+isin⁡2𝑥)+𝐵(cos⁡2𝑥−isin⁡2𝑥) \\ & =(𝐴+𝐵)cos⁡2𝑥+i(𝐴−𝐵)sin⁡2𝑥.\end{aligned}


$$

Since we are typically solving for a real-world quantity, our final answer must be a real-valued function. For this to be true, the arbitrary constants $A$ and $B$ must be a complex conjugate pair ($B = \overline{A}$). This implies that the following definitions yield *real* constants $P$ and $Q$:

$$


P = A+B \quad \text{and} \quad Q = \textrm{i}(A-B).


$$

This gives the **general real-valued solution**:

$$


\boxed{y(x) = P\cos{2x} + Q\sin{2x}},


$$

where $P$ and $Q$ are arbitrary real constants determined by initial conditions.

So, for example,

$$


y(x) = \cos{2x} - 2\sin{2x},


$$

corresponding to $P=1$ and $Q=-2,$ is a solution of the given differential equation. On the other hand,

$$


y(x) = \cos{2x} + \sin{x}


$$

is *not* a solution because it contains a function $\sin{x},$ which is not included in the above form representing the general solution.

### A Shortcut When the Characteristic Equation Has Imaginary Roots

In general, if the characteristic equation of a second-order homogeneous ODE has **imaginary roots**

$$


\lambda = \pm b\textrm{i},


$$

then the *general solution* is

$$


y(x) = Ae^{\textrm{i} b x} + B e^{-\textrm{i} bx}.


$$

Using *Euler's formula*, the above can be simplified to

$$


y(x) = P \cos bx + Q \sin bx,


$$

where $P = A+B$ and $Q=\textrm{i} (A-B).$

Let's take a look at another example.

### Example: Finding the General Solution When the Characteristic Equation Has Imaginary Roots

#### Question

Find the general solution to the equation

$$


\frac{\textrm{d}^2 y}{\textrm{d} x^2} + 25y =0.


$$

#### Explanation

Assuming $y=e^{\lambda x}$ and differentiating $y$ with respect to $x$ gives

$$


\frac{\textrm{d} y}{\textrm{d} x} = \lambda e^{\lambda x}, \qquad \frac{\textrm{d}^2 y}{\textrm{d} x^2} = \lambda^2 e^{\lambda x} .


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑥}+25𝑒^{𝜆𝑥} & =0 \\ 𝑒^{𝜆𝑥}(𝜆^{2}+25) & =0.\end{aligned}


$$

The corresponding characteristic equation is

$$


\begin{aligned}𝜆^{2}+25 & =0 \\ 𝜆^{2}+25 & =0 \\ 𝜆^{2} & =−25 \\ 𝜆 & =±5i.\end{aligned}


$$

Therefore, the general solution to the differential equation is

$$


y = P\cos{5x} + Q\sin{5x}.


$$

### Second-Order Homogeneous ODEs: Characteristic Equation Has Complex Roots

Sometimes, the characteristic equation of a second-order homogeneous ODE may have complex solutions. In such cases, the general solution will initially involve complex exponentials.

For example, suppose that we want to solve the following differential equation:

$$


\frac{\textrm{d}^2 y}{\textrm{d} x^2} - 6 \frac{\textrm{d} y}{\textrm{d} x} + 18y =0.


$$

Assuming a solution of the form $y=e^{\lambda x}$, we get the **characteristic equation**:

$$


\lambda^2 - 6\lambda + 18 =0.


$$

We can solve this by *completing the square*:

$$


\begin{aligned}𝜆^{2}−6𝜆+18 & =0 \\ (𝜆^{2}−6𝜆+9)−9+18 & =0 \\ (𝜆−3)^{2}+9 & =0 \\ (𝜆−3)^{2} & =−9 \\ 𝜆−3 & =±3i \\ 𝜆 & =3±3i\end{aligned}


$$

The two complex roots are $\lambda_1 = 3 + 3\textrm{i}$ and $\lambda_2 = 3 - 3\textrm{i}.$

The general solution is therefore

$$


y = Ae^{(3 + 3 \textrm{i})x} + Be^{(3 - 3 \textrm{i})x}.


$$

Next, we will use *Euler's formula* to rewrite this solution in a form that does not involve complex numbers.

### Convert the Complex Solution to a Real-Valued Solution

Recall that our general solution is

$$


y = Ae^{(3 + 3 \textrm{i})x} + Be^{(3 - 3 \textrm{i})x}.


$$

Our goal is to simplify this to find the **real-valued general solution**. We can do this using **Euler's formula**, which states that

$$


e^{\textrm{i}\theta} = \cos{\theta} + \textrm{i}\sin{\theta}.


$$

First, we use the law of exponents to separate the real and imaginary parts in the exponential:

$$


\begin{aligned}𝑦 & =𝐴𝑒^{3𝑥}𝑒^{3i𝑥}+𝐵𝑒^{3𝑥}𝑒^{−3i𝑥} \\ & =𝑒^{3𝑥}(𝐴𝑒^{3i𝑥}+𝐵𝑒^{−3i𝑥}).\end{aligned}


$$

Now, we apply Euler's formula with $\theta = 3x$:

$$


\begin{aligned}𝑦 & =𝑒^{3𝑥}(𝐴(cos⁡3𝑥+isin⁡3𝑥)+𝐵(cos⁡3𝑥−isin⁡3𝑥)) \\ & =𝑒^{3𝑥}((𝐴+𝐵)cos⁡3𝑥+i(𝐴−𝐵)sin⁡3𝑥).\end{aligned}


$$

Since $A$ and $B$ are arbitrary constants, we can define new arbitrary constants $P=A+B$ and $Q=\textrm{i}(A-B).$ The general solution becomes:

$$


\boxed{y = e^{3x}(P\cos{3 x} + Q\sin{3 x}).}


$$

This is the final form of the solution, written entirely with real-valued functions.

So, for example,

$$


y(x) = e^{3x}(5\cos{3 x} - \sin{3 x}),


$$

corresponding to $P=5$ and $Q=-1,$ is a solution of the given differential equation. On the other hand,

$$


y(x) = e^{3x}(\cos{5 x} - \sin{3 x})


$$

is *not* a solution because it contains a function $e^{3x}\cos{5x},$ which is not included in the above form representing the general solution.

### A Shortcut When the Characteristic Equation Has Complex Roots

In general, if the characteristic equation of a second-order homogeneous ODE has **complex conjugate roots**

$$


\lambda = a \pm b\textrm{i},


$$

then the *general solution* is

$$


y(x) = Ae^{(a+b\textrm{i})x} + B e^{(a-b\textrm{i})x}.


$$

Using *Euler's formula*, we can expand and group the terms:

$$


y(x) = e^{ax} \left[ (A+B)\cos bx + \textrm{i}(A-B)\sin bx \right].


$$

This simplifies to

$$


y(x) = e^{ax} \left( P \cos bx + Q \sin bx \right)


$$

where $P = A+B$ and $Q=\textrm{i} (A-B).$

Let's take a look at another example

### Example: Finding the Complex Solutions of a Characteristic Equation

#### Question

Consider the equation $y'' + 10y' + 34y = 0,$ where $y = y(t).$ If $y = e^{\lambda t}$ is a solution, then what is $\lambda?$

#### Explanation

Assuming $y = e^{\lambda t}$ and differentiating $y$ with respect to $t$ gives

$$


y' = \lambda e^{\lambda t}, \qquad y'' = \lambda^2 e^{\lambda t} .


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑡}+10𝜆𝑒^{𝜆𝑡}+34𝑒^{𝜆𝑡} & =0 \\ 𝑒^{𝜆𝑡}(𝜆^{2}+10𝜆+34) & =0.\end{aligned}


$$

The corresponding characteristic equation is

$$


\lambda^2 + 10\lambda + 34 = 0,


$$

and we can solve it by completing the square:

$$


\begin{aligned}𝜆^{2}+10𝜆+34 & =0 \\ (𝜆^{2}+10𝜆+25)−25+34 & =0 \\ (𝜆+5)^{2}+9 & =0 \\ (𝜆+5)^{2} & =−9 \\ 𝜆+5 & =±3i \\ 𝜆 & =−5±3i\end{aligned}


$$

Therefore, $\lambda = - 5 \pm 3\textrm{i}$ are the complex roots of the auxiliary equation.

### Example: Finding the General Solution When the Characteristic Equation Has Complex Roots

#### Question

Find the general solution to the equation

$$


\frac{\textrm{d}^2 y}{\textrm{d} x^2} - 4 \frac{\textrm{d} y}{\textrm{d} x} + 20y =0.


$$

#### Explanation

Assuming $y=e^{\lambda x}$ and differentiating $y$ with respect to $x$ gives

$$


\frac{\textrm{d} y}{\textrm{d} x} = \lambda e^{\lambda x}, \qquad \frac{\textrm{d}^2 y}{\textrm{d} x^2} = \lambda^2 e^{\lambda x} .


$$

Substituting the above into our ODE gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑥}−4𝜆𝑒^{𝜆𝑥}+20𝑒^{𝜆𝑥} & =0 \\ 𝑒^{𝜆𝑥}(𝜆^{2}−4𝜆+20) & =0.\end{aligned}


$$

The corresponding characteristic equation is

$$


\begin{aligned}𝜆^{2}−4𝜆+20 & =0,\end{aligned}


$$

and we can solve it by completing the square:

$$


\begin{aligned}𝜆^{2}−4𝜆+20 & =0 \\ (𝜆^{2}−4𝜆+4)−4+20 & =0 \\ (𝜆−2)^{2}+16 & =0 \\ (𝜆−2)^{2} & =−16 \\ 𝜆−2 & =±4i \\ 𝜆 & =2±4i.\end{aligned}


$$

Therefore, the general solution is

$$


\begin{aligned}𝑦 & =𝑒^{2𝑥}(𝑃cos⁡4𝑥+𝑄sin⁡4𝑥).\end{aligned}


$$

### Example: Identifying Non-Solutions of a Second-Order Homogeneous ODEs

#### Question

Given that $y = y(t)$ satisfies the equation $y'' - 4y' + 85y = 0,$ which of the following is **** a solution to this equation?

1. $-2e^{2t}\cos{9t} + 7e^{2t}\sin{9t}$

2. $e^{2t}\cos{9t}+3e^{2t}\sin{3t}$

3. $-6e^{2t}\sin{9t}$

#### Explanation

Assuming $y = e^{\lambda x}$ and differentiating $y$ with respect to $t$ gives

$$


y' = \lambda e^{\lambda t}, \qquad y'' = \lambda^2 e^{\lambda t} .


$$

Substituting the above into our differential equation gives

$$


\begin{aligned}𝜆^{2}𝑒^{𝜆𝑡}−4𝜆𝑒^{𝜆𝑡}+85𝑒^{𝜆𝑡} & =0 \\ 𝑒^{𝜆𝑡}(𝜆^{2}−4𝜆+85) & =0.\end{aligned}


$$

The corresponding characteristic equation is

$$


\lambda^2 - 4\lambda + 85 = 0,


$$

and we can solve it by completing the square:

$$


\begin{aligned}𝜆^{2}−4𝜆+85 & =0 \\ (𝜆^{2}−4𝜆+4)−4+85 & =0 \\ (𝜆−2)^{2}+81 & =0 \\ (𝜆−2)^{2} & =−81 \\ 𝜆−2 & =±9i \\ 𝜆 & =2±9i\end{aligned}


$$

Since $\lambda = 2 \pm 9 \textrm{i}$ are the complex roots of the characteristic equation, the general solution takes the form

$$


y = e^{2t} \left( P \cos 9t + Q \sin 9t \right).


$$

Finally, we need to determine whether each of the given functions takes the form shown above.

- Function I takes the above form with $P=-2$ and $Q=7.$ So, it is a solution to the given ODE.

- Function II does ** take the above form. It contains $\sin 3t,$ which is not included in the above form. So, it is ** a solution to the given ODE.

- Function III takes the above form with $P=0$ and $Q=-6.$ So, it is a solution to the given ODE.

Therefore, the correct answer is "II only".
