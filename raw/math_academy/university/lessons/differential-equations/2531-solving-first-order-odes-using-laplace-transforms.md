# Solving First-Order ODEs Using Laplace Transforms

Source: https://www.mathacademy.com/topics/2531?courseId=61
Topic ID: 2531

## Prerequisites

- [Introduction to First-Order Linear ODEs](./906-introduction-to-first-order-linear-odes.md)
- [Expressing Rational Functions with Irreducible Quadratic Factors as Sums of Partial Fractions](../../../ap-courses/lessons/ap-calculus-bc/1063-expressing-rational-functions-with-irreducible-quadratic-factors-as-sums-of-partial-fractions.md)
- [Inverse Laplace Transforms](./2530-inverse-laplace-transforms.md)
- [Laplace Transforms of Derivatives](./2538-laplace-transforms-of-derivatives.md)

## Lesson

### Introduction

In this lesson, we will solve first-order *initial value problems* using Laplace transforms.

The key idea is that the Laplace transform converts derivatives into algebraic expressions involving the transform of the unknown function. If we write

$$


Y(s) = \mathcal L\{y(t)\},


$$

then the initial condition appears automatically through the **derivative rule**

$$


\mathcal L\{y'\} = sY(s) - y(0).


$$

So, when we take the Laplace transform of a differential equation like

$$


y' + ay = f(t),


$$

we get an algebraic equation in $Y(s),$ which we can solve using standard algebra.

In the first few problems, our goal will be to find an explicit formula for $Y(s).$ Later, we will finish the process by taking the inverse Laplace transform to recover $y(t).$

### Using Laplace Transforms to Solve First-Order IVPs

The **Laplace transform method** is a powerful tool that converts a differential equation (a calculus problem) into an algebraic equation, which is often much easier to solve.

To solve a first-order initial value problem (IVP) of the form

$$


y' + ay = f(t), \quad y(0)=y_0,


$$

we follow a standard workflow.

- First, we take the Laplace transform of both sides of the equation to obtain an algebraic equation in $Y(s)=\mathcal L\{y(t)\}.$ Using linearity and the derivative formula we convert the IVP into an algebraic equation for the unknown transform, $Y(s).$

- After substituting the initial condition $y(0)=y_0$ and finding the transform of $f(t),$ we solve the resulting algebraic equation for $Y(s).$ The calculus portion of the problem is now complete.

- Before applying the inverse transform, we rewrite $Y(s)$ as a sum of simpler expressions found in a standard table of Laplace transforms. This step often requires techniques like **partial fraction decomposition**.

- Finally, we take the inverse Laplace transform, $\mathcal L^{-1},$ of each term in $Y(s)$ to find the solution $y(t)$ to the original initial value problem.

Next, we consider the example of finding $Y(s)$ for the concrete initial value problem.

### Finding the Laplace Transform of the Unknown Function Satisfying the IVP

Consider the following initial value problem.

$$


\dfrac{\textrm{d}y}{\textrm{d}t} + 4y = 2t-1, \qquad y(0)=0.


$$

To find $Y(s) = \mathcal L \{y(t)\},$ we first take the Laplace transform of both sides of the differential equation. Using the linearity property, we have

$$


\mathcal{L}\{y'\} + 4\mathcal{L}\{y\} = 2\mathcal{L}\{t\}-\mathcal{L}\{1\}.


$$

To calculate $\mathcal L\left\{y' \right\},$ we use the formula for the Laplace transform of a derivative and the initial condition $y(0)=0{:}$

$$


\mathcal{L}\left\{y'\right\} = sY(s) - y(0) = sY(s).


$$

So, the differential equation transforms to

$$


sY(s) + 4Y(s) = 2\mathcal{L}\{t\}-\mathcal{L}\{1\}.


$$

Now, we make use of the following result:

$$


\mathcal L\{t^n\} = \dfrac{n!}{s^{n+1}}, \qquad s > 0, \quad n\in \mathbb{N}_0.


$$

This gives

$$


\begin{aligned}L{𝑡} & =\frac{1!}{𝑠^{1+1}}=\frac{1}{𝑠^{2}}, \\ L{1} & =\frac{0!}{𝑠^{0+1}}=\frac{1}{𝑠}.\end{aligned}


$$

Substituting these results into the transformed equation, we get

$$


\begin{aligned}𝑠𝑌(𝑠)+4𝑌(𝑠) & =2⋅\frac{1}{𝑠^{2}}−\frac{1}{𝑠} \\ (𝑠+4)𝑌(𝑠) & =\frac{2}{𝑠^{2}}−\frac{1}{𝑠} \\ (𝑠+4)𝑌(𝑠) & =\frac{2−𝑠}{𝑠^{2}}.\end{aligned}


$$

Finally, dividing by $(s+4),$ we obtain

$$


Y(s) =\dfrac{2-s}{s^2(s + 4)}.


$$

### Example: Laplace Transforms of First-Order Linear IVPs

#### Question

Find the Laplace transform $Y(s) = \mathcal L\{y(t)\}$ for $s > 1$ if

$$


y' + y = 2e^t, \qquad y(0)=-1.


$$

#### Explanation

First, we take the Laplace transform of both sides and use the addition and scalar multiplication properties of the Laplace transform:

$$


\begin{aligned}L{𝑦^{′}+𝑦} & =L{2𝑒^{𝑡}} \\ L{𝑦^{′}}+L{𝑦} & =2L{𝑒^{𝑡}}\end{aligned}


$$

To calculate $\mathcal L\left\{y' \right\},$ we use the formula for the Laplace transform of a derivative and the initial condition $y(0)=-1\mathbin{:}$

$$


\mathcal{L}\left\{y'\right\} = sY(s) - y(0) = sY(s) + 1


$$

From the table of Laplace transforms:

$$


\mathcal L \{e^{at}\} = \dfrac{1}{s-a}, \qquad s > a


$$

Therefore, we have the following result:

$$


\mathcal{L} \{ e^t \} = \dfrac{1}{s-1}


$$

Therefore, we get the following:

$$


\begin{aligned}L{𝑦^{′}}+L{𝑦} & =2L{𝑒^{𝑡}} \\ (𝑠𝑌(𝑠)+1)+𝑌(𝑠) & =\frac{2}{𝑠−1} \\ (𝑠+1)𝑌(𝑠) & =\frac{2}{𝑠−1}−1 \\ (𝑠+1)𝑌(𝑠) & =\frac{2−(𝑠−1)}{𝑠−1} \\ 𝑌(𝑠) & =\frac{3−𝑠}{𝑠^{2}−1}\end{aligned}


$$

### Getting Ready for the Inverse Laplace Transform

Once we have solved for $Y(s)$, the final step is to compute the solution.

The main idea is to rewrite $Y(s)$ as a sum of simpler terms whose inverse transforms are known from a table.

**Step 1:** Look for standard inverse-transform patterns.

The goal is to match terms in $Y(s)$ to known transform pairs. Common forms include:

- $\mathcal{L}^{-1}\left\{\dfrac{1}{s-a}\right\} = e^{at}$

- $\mathcal{L}^{-1}\left\{\dfrac{1}{(s-a)^n}\right\} = \dfrac{t^{n-1}e^{at}}{(n-1)!}$ for integer $n \ge 1$

- $\mathcal{L}^{-1}\left\{\dfrac{s}{s^2+\omega^2}\right\} = \cos(\omega t)$

- $\mathcal{L}^{-1}\left\{\dfrac{\omega}{s^2+\omega^2}\right\} = \sin(\omega t)$

**Step 2:** If $Y(s)$ is a rational function, use **partial fraction decomposition**.

If the denominator has distinct linear factors, we write:

$$


\dfrac{P(s)}{(s-a)(s-b)} = \dfrac{A}{s-a} + \dfrac{B}{s-b}


$$

where $P(s)$ is a polynomial with $\deg (P) < 2$.

If there is a repeated linear factor, we include a term for each power:

$$


\dfrac{P(s)}{(s-a)^2} = \dfrac{A}{s-a} + \dfrac{B}{(s-a)^2}


$$

where $P(s)$ is a polynomial with $\deg (P) < 2$.

**Step 3:** Apply the inverse transform term-by-term.

Because the inverse Laplace transform is **linear**, we can apply it to each term in the sum separately to find the final solution $y(t)$.

Next, we will apply this method to a specific example.

### Example: Solving First-Order Initial Value Problems Using Laplace Transforms

#### Question

Consider the following initial value problem.

$$


\dfrac{\textrm{d}y}{\textrm{d}t} + 4y = 3e^{-t}, \qquad y(0)=2


$$

Select the correct options in the reasoning below to find the solution using Laplace transforms.

Let $Y(s) = \mathcal L \{y(t)\}.$ Taking the Laplace transform of both sides of the equation and solving for $Y,$ we have

$$


𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}^{}


$$

The partial fraction decomposition of $Y$ is

$$


𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}^{}


$$

Therefore, the solution to the initial value problem is

$$


𝐴𝐴𝐴𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}^{}


$$

#### Explanation

First, we take the Laplace transform of both sides of the differential equation. Using the linearity property, we have

$$


\mathcal{L}\{y'\} + 4\mathcal{L}\{y\} = 3\mathcal{L}\{e^{-t}\}.


$$

Using the formula for the transform of a derivative, $\mathcal{L}\{y'\} = sY(s) - y(0),$ and the standard transform

$$


\mathcal{L}\{e^{at}\} = \frac{1}{s-a}, \qquad s > a,


$$

we substitute the known values. Note that $y(0)=2{:}$

$$


\begin{aligned}(𝑠𝑌(𝑠)−2)+4𝑌(𝑠) & =3⋅\frac{1}{𝑠+1} \\ (𝑠+4)𝑌(𝑠)−2 & =\frac{3}{𝑠+1}\end{aligned}


$$

We rearrange to solve for $Y(s).$ First, add $2$ to the right-hand side and find a common denominator:

$$


\begin{aligned}(𝑠+4)𝑌(𝑠) & =2+\frac{3}{𝑠+1} \\ (𝑠+4)𝑌(𝑠) & =\frac{2(𝑠+1)}{𝑠+1}+\frac{3}{𝑠+1} \\ (𝑠+4)𝑌(𝑠) & =\frac{2𝑠+5}{𝑠+1}\end{aligned}


$$

Dividing by $(s+4),$ we obtain

$$


Y(s) =\dfrac{2s+5}{(s + 4)(s+1)}.


$$

Next, we perform a partial fraction decomposition. We write $Y(s)$ in the form

$$


\dfrac{2s+5}{(s+4)(s+1)} = \dfrac{A}{s+4} + \dfrac{B}{s+1}.


$$

To find the constants $A$ and $B,$ we first clear the denominators:

$$


2s+5 = A(s+1) + B(s+4)


$$

Now, we find the constants $A$ and $B.$

- Setting $s = -4,$ we have

- Setting $s = -1,$ we have

Thus, the decomposition is

$$


Y(s) = \dfrac{1}{s+4} + \dfrac{1}{s+1}.


$$

From the table of Laplace transforms, we have:

$$


\begin{aligned}L^{−1}{\frac{1}{𝑠+4}} & =𝑒^{−4𝑡} \\ L^{−1}{\frac{1}{𝑠+1}} & =𝑒^{−𝑡}\end{aligned}


$$

Finally, taking the inverse Laplace transform of $Y(s),$ we get

$$


\begin{aligned}𝑦(𝑡) & =L^{−1}{\frac{1}{𝑠+4}}+L^{−1}{\frac{1}{𝑠+1}} \\ 𝑦(𝑡) & =𝑒^{−4𝑡}+𝑒^{−𝑡}.\end{aligned}


$$

### Partial Fractions With Irreducible Quadratic Factors

When $Y(s)$ is a rational function, we often use partial fractions to rewrite it in a form where we can apply $\mathcal L^{-1}.$

Sometimes the denominator contains an *irreducible quadratic factor*, such as $s^2+\omega^2.$ In that case, the partial fraction term must have a linear numerator.

**Step 1:** Write the correct decomposition form.

For example, if

$$


Y(s)=\dfrac{P(s)}{(s-a)(s^2+\omega^2)},


$$

then we decompose it as

$$


\dfrac{P(s)}{(s-a)(s^2+\omega^2)} = \dfrac{A}{s-a} + \dfrac{Bs+C}{s^2+\omega^2}.


$$

**Step 2:** Multiply both sides by the denominator.

Clearing denominators gives an identity in $s{:}$

$$


P(s)=A(s^2+\omega^2) + (Bs+C)(s-a).


$$

**Step 3:** Solve for the constants.

We can find $A,$ $B,$ and $C$ by expanding the right-hand side and matching coefficients of powers of $s.$

**Step 4:** Take the inverse Laplace transform.

We split the quadratic term to match the standard forms:

$$


\dfrac{Bs+C}{s^2+\omega^2} = B\left(\dfrac{s}{s^2+\omega^2}\right) + \dfrac{C}{\omega}\left(\dfrac{\omega}{s^2+\omega^2}\right).


$$

Then we apply the inverse transforms:

$$


\mathcal L^{-1}\left\{\dfrac{s}{s^2+\omega^2}\right\}=\cos(\omega t), \qquad \mathcal L^{-1}\left\{\dfrac{\omega}{s^2+\omega^2}\right\}=\sin(\omega t).


$$

Let's see an example.

### Example: Solving First-Order Initial Value Problems With Sinusoidal Forcing

#### Question

Consider the following initial value problem.

$$


\dfrac{\textrm{d}y}{\textrm{d}t} - 2y = -5\sin t, \qquad y(0)=1


$$

Select the correct options in the reasoning below to find the solution using Laplace transforms. You may make use of the following results:

$$


\mathcal L\{\sin\omega t\} = \dfrac{\omega}{s^2+\omega^2}, \qquad \mathcal L\{\cos\omega t\} = \dfrac{s}{s^2+\omega^2}, \qquad s > 0.


$$

Let $Y(s) = \mathcal L \{y(t)\}.$ Taking the Laplace transform of both sides of the equation and solving for $Y,$ we have

$$


𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}^{}𝐴𝐴


$$

The partial fraction decomposition of $Y$ is

$$


𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}^{}𝐴𝐴


$$

Therefore, the solution to the initial value problem is

$$


𝐴𝐴𝐴𝐴𝐴_{𝐴𝐴}^{}𝐴𝐴


$$

#### Explanation

First, we take the Laplace transform of both sides of the differential equation. Using the linearity property, we have

$$


\mathcal{L}\{y'\} - 2\mathcal{L}\{y\} = -5\mathcal{L}\{\sin t\}.


$$

Using the formula for the transform of a derivative $\mathcal{L}\{y'\} = sY(s) - y(0)$ and the standard trigonometric transform

$$


\mathcal{L}\{\sin t\} = \dfrac{1}{s^2+1},


$$

we substitute the known values. Note that $y(0)=1{:}$

$$


\begin{aligned}(𝑠𝑌(𝑠)−1)−2𝑌(𝑠) & =−5⋅\frac{1}{𝑠^{2}+1} \\ (𝑠−2)𝑌(𝑠)−1 & =−\frac{5}{𝑠^{2}+1}\end{aligned}


$$

We rearrange to solve for $Y(s).$ First, add $1$ to the right-hand side and find a common denominator:

$$


\begin{aligned}(𝑠−2)𝑌(𝑠) & =1−\frac{5}{𝑠^{2}+1} \\ (𝑠−2)𝑌(𝑠) & =\frac{𝑠^{2}+1}{𝑠^{2}+1}−\frac{5}{𝑠^{2}+1} \\ (𝑠−2)𝑌(𝑠) & =\frac{𝑠^{2}−4}{𝑠^{2}+1}\end{aligned}


$$

Dividing by $(s-2),$ we obtain

$$


Y(s) =\dfrac{s^2 - 4}{(s - 2)(s^2 + 1)} = \dfrac{(s-2)(s+2)}{(s - 2)(s^2 + 1)} = \dfrac{s+2}{s^2 + 1}.


$$

From the table of Laplace transforms, we have:

$$


\begin{aligned}L^{−1}{\frac{𝑠}{𝑠^{2}+1}} & =cos⁡𝑡 \\ L^{−1}{\frac{1}{𝑠^{2}+1}} & =sin⁡𝑡\end{aligned}


$$

Finally, taking the inverse Laplace transform of $Y(s),$ we get

$$


\begin{aligned}𝑦(𝑡) & =L^{−1}{\frac{𝑠}{𝑠^{2}+1}}+2L^{−1}{\frac{1}{𝑠^{2}+1}} \\ 𝑦(𝑡) & =cos⁡𝑡+2sin⁡𝑡.\end{aligned}


$$
