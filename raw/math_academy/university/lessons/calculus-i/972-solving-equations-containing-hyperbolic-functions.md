# Solving Equations Containing Hyperbolic Functions

Source: https://www.mathacademy.com/topics/972?courseId=105
Topic ID: 972

## Prerequisites

- [The Quadratic Formula](../../../high-school/traditional/lessons/algebra-i/422-the-quadratic-formula.md)
- [Solving Equations Containing the Exponential Function](../../../high-school/traditional/lessons/algebra-ii/870-solving-equations-containing-the-exponential-function.md)
- [The Hyperbolic Functions](./967-the-hyperbolic-functions.md)
- [Solving Quadratic Equations with Leading Coefficients by Factoring](../../../high-school/traditional/lessons/algebra-i/1422-solving-quadratic-equations-with-leading-coefficients-by-factoring.md)

## Lesson

### Introduction

When solving equations containing hyperbolic functions, one strategy that often works is to rewrite any hyperbolic functions using their definitions. Doing this reduces the problem to solving an exponential equation.

For example, let's consider the following equation:

$$


2\cosh{x} = 3


$$

To find the real solutions to this equation, we first recall that the definition of $\cosh{x}$ is

$$


\cosh{x} = \dfrac12(e^x + e^{-x}).


$$

Substituting this definition into our equation, we get

$$


2\cdot \left( \dfrac12(e^x+e^{-x}) \right) = 3


$$

which simplifies to

$$


e^x + e^{-x} = 3.


$$

We can eliminate the $e^{-x}$ term by multiplying both sides of the equation by $e^x$ and simplifying by bringing all terms to one side.

$$


\begin{aligned}𝑒^{𝑥}⋅(𝑒^{𝑥}+𝑒^{−𝑥}) & =𝑒^{𝑥}⋅3 \\ 𝑒^{𝑥}⋅𝑒^{𝑥}+𝑒^{𝑥}⋅𝑒^{−𝑥} & =3𝑒^{𝑥} \\ 𝑒^{2𝑥}+1 & =3𝑒^{𝑥} \\ 𝑒^{2𝑥}−3𝑒^{𝑥}+1 & =0\end{aligned}


$$

Notice that this is a quadratic equation in $e^x.$ To see this, note that we can write our equation as

$$


\left(e^{x}\right)^2 - 3e^x + 1 = 0


$$

and if we let $y=e^x,$ we get

$$


y^2 - 3y + 1 = 0.


$$

We can solve this equation using the quadratic formula as follows:

$$


\begin{aligned}𝑦 & =\frac{−(−3)±\sqrt{√(−3)^{2}−4⋅1⋅1}}{2⋅1} \\ 𝑦 & =\frac{3±\sqrt{√9−4}}{2} \\ 𝑦 & =\frac{3±\sqrt{√5}}{2} \\ 𝑒^{𝑥} & =\frac{3±\sqrt{√5}}{2}\end{aligned}


$$

Finally, taking the natural logarithm of both sides, we have

$$


x = \ln{\left(\dfrac{3 \pm \sqrt{5}}{2}\right)}.


$$

Since we want real solutions only, we require that the argument of the logarithm is positive. However, since

$$


\dfrac{3 + \sqrt{5}}{2} > 0\qquad\text{and}\qquad \dfrac{3 - \sqrt{5}}{2} > 0,


$$

this means that *both* of our solutions are valid.

Therefore, we conclude that the solutions to our equation are $x=\ln{\left(\dfrac{3 \pm \sqrt{5}}{2}\right)}.$

When solving these equations, we often skip the intermediate step of setting $y=e^x.$ However, you can continue to do this if you wish.

### Example: Solving Equations Containing a Hyperbolic Sine or Cosine

#### Question

Find the real solutions to the equation $3\sinh{x}= 4.$

#### Explanation

The definition of $\sinh{x}$ is

$$


\sinh{x} = \dfrac12(e^x - e^{-x}).


$$

Substituting the above definition into the equation, we get

$$


\begin{aligned}3⋅(\frac{1}{2}(𝑒^{𝑥}−𝑒^{−𝑥})) & =4 \\ \frac{3}{2}(𝑒^{𝑥}−𝑒^{−𝑥}) & =4 \\ 3𝑒^{𝑥}−3𝑒^{−𝑥} & =8.\end{aligned}


$$

Next, we multiply both sides of the equation by $e^x,$ and simplify:

$$


\begin{aligned}𝑒^{𝑥}⋅(3𝑒^{𝑥}−3𝑒^{−𝑥}) & =𝑒^{𝑥}⋅8 \\ 3𝑒^{2𝑥}−3 & =8𝑒^{𝑥} \\ 3𝑒^{2𝑥}−8𝑒^{𝑥}−3 & =0\end{aligned}


$$

This is a quadratic equation in $e^x$ that we can factor as follows:

$$


\begin{aligned}(3𝑒^{𝑥}+1)(𝑒^{𝑥}−3) & =0\end{aligned}


$$

By the zero-product property, we have to solve two equations:

$$


3e^x + 1 = 0, \qquad e^x - 3 = 0


$$

Solving the two equations above for $x,$ we get the following:

$$


\begin{aligned}3𝑒^{𝑥}+1 & =0 & & \, & 𝑒^{𝑥}−3 & =0 \\ 3𝑒^{𝑥} & =−1 & & \, & 𝑒^{𝑥} & =3 \\ 𝑒^{𝑥} & =−\frac{1}{3} & & \, & 𝑥 & =ln⁡3\end{aligned}


$$

There are no real values of $x$ for which $e^x = -\dfrac13.$ Therefore, $x=\ln{3}$ is the only real solution to the equation.

### Example: Solving Equations Containing a Hyperbolic Tangent

#### Question

Find the real solution to the equation $41\tanh{x} = 40.$

#### Explanation

The definition of $\tanh{x}$ is

$$


\tanh{x} = \dfrac{e^x - e^{-x}}{e^x + e^{-x}}.


$$

Substituting the above definition into the equation $41\tanh{x} = 40,$ we get

$$


\begin{aligned}41⋅(\frac{𝑒^{𝑥}−𝑒^{−𝑥}}{𝑒^{𝑥}+𝑒^{−𝑥}}) & =40 \\ 41(𝑒^{𝑥}−𝑒^{−𝑥}) & =40(𝑒^{𝑥}+𝑒^{−𝑥}) \\ 41𝑒^{𝑥}−41𝑒^{−𝑥} & =40𝑒^{𝑥}+40𝑒^{−𝑥} \\ 𝑒^{𝑥} & =81𝑒^{−𝑥}.\end{aligned}


$$

Next, we multiply both sides of the equation by $e^x$ and solve the equation as follows:

$$


\begin{aligned}𝑒^{𝑥}⋅𝑒^{𝑥} & =𝑒^{𝑥}⋅81𝑒^{−𝑥} \\ 𝑒^{2𝑥} & =81 \\ ln⁡(𝑒^{2𝑥}) & =ln⁡81 \\ 2𝑥 & =ln⁡81 \\ 𝑥 & =\frac{1}{2}ln⁡81 \\ 𝑥 & =\frac{1}{2}ln⁡(9^{2}) \\ 𝑥 & =\frac{1}{2}⋅2ln⁡9 \\ 𝑥 & =ln⁡9\end{aligned}


$$

Therefore, the only real solution is $x=\ln{9}.$

### Example: Solving Equations Containing Multiple Hyperbolic Functions

#### Question

Find the real solutions to the equation $2\cosh{x} + \sinh{x} = 2.$

#### Explanation

The definitions of $\cosh{x}$ and $\sinh{x}$ are

$$


\cosh{x} = \dfrac12(e^x + e^{-x}),\qquad \sinh{x} = \dfrac12(e^x - e^{-x}).


$$

Substituting the above definitions into the equation $2\cosh{x} + \sinh{x} = 2,$ we get

$$


\begin{aligned}2⋅(\frac{1}{2}(𝑒^{𝑥}+𝑒^{−𝑥}))+\frac{1}{2}(𝑒^{𝑥}−𝑒^{−𝑥}) & =2 \\ 𝑒^{𝑥}+𝑒^{−𝑥}+\frac{1}{2}(𝑒^{𝑥}−𝑒^{−𝑥}) & =2 \\ 𝑒^{𝑥}+𝑒^{−𝑥}+\frac{1}{2}𝑒^{𝑥}−\frac{1}{2}𝑒^{−𝑥} & =2 \\ \frac{3}{2}𝑒^{𝑥}+\frac{1}{2}𝑒^{−𝑥} & =2.\end{aligned}


$$

Multiplying the above equation by $2,$ we get

$$


\begin{aligned}2⋅(\frac{3}{2}𝑒^{𝑥}+\frac{1}{2}𝑒^{−𝑥}) & =2⋅2 \\ 3𝑒^{𝑥}+𝑒^{−𝑥} & =4.\end{aligned}


$$

Next, we multiply both sides of the equation by $e^x,$ and simplify:

$$


\begin{aligned}𝑒^{𝑥}⋅(3𝑒^{𝑥}+𝑒^{−𝑥}) & =𝑒^{𝑥}⋅4 \\ 3𝑒^{2𝑥}+1 & =4𝑒^{𝑥} \\ 3𝑒^{2𝑥}−4𝑒^{𝑥}+1 & =0\end{aligned}


$$

This is a quadratic equation in $e^x$ that we can factor as follows:

$$


\begin{aligned}(3𝑒^{𝑥}−1)(𝑒^{𝑥}−1) & =0\end{aligned}


$$

By the zero-product property, we have to solve two equations:

$$


3e^x - 1 = 0, \qquad e^x - 1 = 0


$$

Solving the two equations above for $x,$ we get the following:

$$


\begin{aligned}3𝑒^{𝑥}−1 & =0 & & \, & 𝑒^{𝑥}−1 & =0 \\ 3𝑒^{𝑥} & =\frac{1}{3} & & \, & 𝑒^{𝑥} & =1 \\ 𝑒^{𝑥} & =ln⁡(\frac{1}{3}) & & \, & 𝑥 & =ln⁡1=0\end{aligned}


$$

Therefore, $x=0$ and $x=\ln\left(\dfrac 13\right)$ are the real solutions to the equation.
