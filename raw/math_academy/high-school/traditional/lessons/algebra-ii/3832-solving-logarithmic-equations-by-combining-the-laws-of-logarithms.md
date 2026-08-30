# Solving Logarithmic Equations by Combining the Laws of Logarithms

Source: https://www.mathacademy.com/topics/3832?courseId=51
Topic ID: 3832

## Prerequisites

- [Combining the Laws of Logarithms](./30-combining-the-laws-of-logarithms.md)
- [Solving Equations With Even Exponents Using the Nth Root Method](../algebra-i/1587-solving-equations-with-even-exponents-using-the-nth-root-method.md)
- [Solving Logarithmic Equations Using the Laws of Logarithms](./1594-solving-logarithmic-equations-using-the-laws-of-logarithms.md)
- [Solving Equations With Odd Exponents Using the Nth Root Method](../algebra-i/3748-solving-equations-with-odd-exponents-using-the-nth-root-method.md)

## Lesson

### Introduction

Let's remind ourselves of the laws of logarithms:

**Product Rule**:

$\qquad$ $\log_b(xy) = \log_b(x) + \log_b(y)$

**Quotient Rule:**

$\qquad$ $\log_b\left(\dfrac x y\right) = \log_b(x) - \log_b(y)$

**Power Rule**:

$\qquad$ $\log_b\left(x^n\right) = n\log_b(x)$

Sometimes, we need to combine two or more of these laws to solve a logarithmic equation. Let's see an example.

### Example: Solving Equations Using the Power and Product Rules

#### Question

Solve the equation $\dfrac{1}{2}\log_2 \left(4x^4\right) + \log_2 x= 1.$

#### Explanation

Notice that the logarithms share the same base.

First, we apply the power rule to the ** term to make the coefficient in front of each logarithm the same:

$$



\begin{aligned}\frac{1}{2}log_{2}⁡(4𝑥^{4})+log_{2}⁡𝑥 & =1 \\ log_{2}⁡((4𝑥^{4})^{1/2})+log_{2}⁡𝑥 & =1 \\ log_{2}⁡(2𝑥^{2})+log_{2}⁡𝑥 & =1\end{aligned}



$$

Next, we combine the logarithms using the product rule. This gives

$$



\begin{aligned}log_{2}⁡(2𝑥^{2}⋅𝑥) & =1 \\ log_{2}⁡(2𝑥^{3}) & =1.\end{aligned}



$$

Writing this equation in its equivalent exponential form, we get

$$



\begin{aligned}2^{log_{2}⁡(2𝑥^{3})} & =2^{1} \\ 2𝑥^{3} & =2.\end{aligned}



$$

Now, we solve this equation for $x$ using the usual methods.

$$



\begin{aligned}𝑥^{3} & =1 \\ \sqrt[√𝑥^{3}]{3} & =\sqrt[√1]{3} \\ 𝑥 & =1\end{aligned}



$$

Let's now check for an extraneous solution by substituting back into the original equation:

Substituting $x=1$ back into the original equation, we get

$$



\begin{aligned}\frac{1}{2}log_{2}⁡(4⋅1^{4})+log_{2}⁡1 & \overset{=}{?}1 \\ \frac{1}{2}log_{2}⁡4+log_{2}⁡1 & \overset{=}{?}1 \\ \frac{1}{2}log_{2}⁡4+0 & \overset{=}{?}1 \\ log_{2}⁡(4^{1/2}) & \overset{=}{?}1 \\ log_{2}⁡(2) & \overset{=}{?}1 \\ 1 & =1.\,✓\end{aligned}



$$

Therefore, $x=1$ is a valid solution.

### Example: Solving Equations Using the Power and Quotient Rules

#### Question

Solve the equation $\log_2 (4x) - 2\log_2\left(x^2\right) = 1.$

#### Explanation

Notice that the logarithms share the same base.

First, we apply the power rule to the first term to make the coefficient in front of each logarithm the same:

$$



\begin{aligned}log_{2}⁡(4𝑥)−2log_{2}⁡(𝑥^{2})=1 & \\ log_{2}⁡(4𝑥)−log_{2}⁡((𝑥^{2})^{2})=1 & \\ log_{2}⁡(4𝑥)−log_{2}⁡(𝑥^{4}) & =1\end{aligned}



$$

Next, we combine the logarithms using the quotient rule. This gives

$$



\begin{aligned}log_{2}⁡(\frac{4𝑥}{𝑥^{4}}) & =1 \\ log_{2}⁡(\frac{4}{𝑥^{3}}) & =1.\end{aligned}



$$

Writing this equation in its equivalent exponential form, we get

$$



\begin{aligned}\frac{4}{𝑥^{3}} & =2^{1} \\ \frac{4}{𝑥^{3}} & =2.\end{aligned}



$$

Now, we solve this rational equation for $x$ using the usual methods.

$$



\begin{aligned}\frac{4}{𝑥^{3}} & =2 \\ 𝑥^{3}⋅\frac{4}{𝑥^{3}} & =𝑥^{3}⋅2 \\ 𝑥^{3}⋅\frac{4}{𝑥^{3}} & =2𝑥^{3} \\ 2𝑥^{3} & =4 \\ 𝑥^{3} & =2 \\ 𝑥 & =\sqrt[√2]{3}\end{aligned}



$$

Let's now check for an extraneous solution by substituting back into the original equation:

Substituting $x=\sqrt[3]{2}$ back into the original equation, we get

$$



\begin{aligned}log_{2}⁡(4(\sqrt[√2]{3}))−2log_{2}⁡((\sqrt[√2]{3})^{2}) & \overset{=}{?}1 \\ log_{2}⁡(4(\sqrt[√2]{3}))−log_{2}⁡((\sqrt[√2]{3})^{2})^{2} & \overset{=}{?}1 \\ log_{2}⁡(4(\sqrt[√2]{3}))−log_{2}⁡((\sqrt[√2]{3})^{4}) & \overset{=}{?}1 \\ log_{2}⁡(4(\sqrt[√2]{3}))−log_{2}⁡(2(\sqrt[√2]{3})) & \overset{=}{?}1 \\ log_{2}⁡(\frac{4\sqrt[√2]{3}}{2\sqrt[√2]{3}}) & \overset{=}{?}1 \\ log_{2}⁡\frac{4\sqrt[√2]{3}}{2\sqrt[√2]{3}} & \overset{=}{?}1 \\ log_{2}⁡(\frac{4}{2}) & \overset{=}{?}1 \\ log_{2}⁡(2) & \overset{=}{?}1 \\ 1 & =1.\,✓\end{aligned}



$$

Therefore, $x=\sqrt[3]{2}$ is a valid solution.

### Example: Solving Equations Resulting in Rational Equations Using the Quotient Rule

#### Question

Solve the equation $2\log_3 (\sqrt 2x) - \log_3(x - 1) = \log_3 (3x).$

#### Explanation

Notice that the logarithms share the same base.

First, we apply the power rule to the ** term to make the coefficient in front of each logarithm the same:

$$



\begin{aligned}2log_{3}⁡(\sqrt{2}𝑥)−log_{3}⁡(𝑥−1) & =log_{3}⁡(3𝑥) \\ log_{3}⁡(\sqrt{2}𝑥)^{2}−log_{3}⁡(𝑥−1) & =log_{3}⁡(3𝑥) \\ log_{3}⁡(2𝑥^{2})−log_{3}⁡(𝑥−1) & =log_{3}⁡(3𝑥)\end{aligned}



$$

Next, we combine the logarithms on the left-hand side using the quotient rule:

$$



\begin{aligned}log_{3}⁡(\frac{2𝑥^{2}}{𝑥−1}) & =log_{3}⁡(3𝑥)\end{aligned}



$$

Now, we solve the equation for $x$ using the usual methods.

$$



\begin{aligned}\frac{2𝑥^{2}}{𝑥−1} & =3𝑥 \\ (𝑥−1)⋅\frac{2𝑥^{2}}{𝑥−1} & =(𝑥−1)⋅(3𝑥) \\ (𝑥−1)⋅\frac{2𝑥^{2}}{𝑥−1} & =(𝑥−1)⋅(3𝑥) \\ 2𝑥^{2} & =3𝑥^{2}−3𝑥 \\ 𝑥^{2}−3𝑥 & =0 \\ 𝑥(𝑥−3) & =0\end{aligned}



$$

So, $x = 0$ and $x =3.$

Let's now check for extraneous solutions by substituting them back into the original equation:

- Substituting $x=0$ back into the original equation, we get This statement is false because $\log_3 (0)$ and $\log_3 (-1)$ are undefined. Therefore, $x=0$ is not a valid solution.

- Substituting $x=3$ back into the original equation, we get Therefore, $x=3$ is a valid solution.

Therefore, the correct answer is "$x=3$ only".
