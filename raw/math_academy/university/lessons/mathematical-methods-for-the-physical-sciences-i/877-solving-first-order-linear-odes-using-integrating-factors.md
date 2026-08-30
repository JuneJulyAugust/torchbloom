# Solving First-Order Linear ODEs Using Integrating Factors

Source: https://www.mathacademy.com/topics/877?courseId=154
Topic ID: 877

## Prerequisites

- [Introduction to Integration by Parts](../../../ap-courses/lessons/ap-calculus-bc/317-introduction-to-integration-by-parts.md)
- [Introduction to First-Order Linear ODEs](./906-introduction-to-first-order-linear-odes.md)
- [Solving First-Order ODEs Using Direct Integration](../../../ap-courses/lessons/ap-calculus-ab/1061-solving-first-order-odes-using-direct-integration.md)

## Lesson

### Introduction

Recall that a first-order linear ODE can always be expressed in the standard form

$$


y'(x)+P(x)y(x) =Q(x).


$$

First-order linear ODEs are special because we can always find the general solution using an **integrating factor.**

An integrating factor is a function $I(x)$ that allows us to rewrite the left-hand side as an exact derivative after multiplying the equation by $I(x).$ The resulting equation can then be solved by integrating both sides.

To demonstrate, consider the following first-order linear ODE.

$$


\frac{\text{d}y}{\text{d}x} + \frac{2}{x}\, y = 3


$$

As it stands, this differential equation cannot be integrated directly. However, if we multiply both sides of the equation by $I(x) = x^2,$ we get

$$


x^2\cdot \frac{\text{d}y}{\text{d}x} + x^2\cdot \frac{2}{x}\, y = x^2\cdot 3


$$

which simplifies as follows:

$$


x^2 \frac{\text{d}y}{\text{d}x} + 2 x y = 3x^2 \qquad (\ast)


$$

Now, here's the neat part. Provided our integrating factor is correct, we can *always* write the left-hand side of the equation as the exact derivative

$$


\dfrac{\textrm d }{\textrm d x}\left(y\cdot I(x)\right)


$$

which in our case is

$$


\dfrac{\textrm d }{\textrm d x}\left(y \cdot x^2\right).


$$

So, our differential equation is

$$


\frac{\text{d}}{\text{d}x}( y \cdot x^2) = 3x^2.


$$

We can now find the general solution by integrating both sides with respect to $x{:}$

$$


\begin{aligned}\frac{d}{d𝑥}(𝑦⋅𝑥^{2}) & =3𝑥^{2} \\ ∫\frac{d}{d𝑥}(𝑦⋅𝑥^{2})\,d𝑥 & =∫3𝑥^{2}\,d𝑥 \\ 𝑦⋅𝑥^{2} & =𝑥^{3}+𝐶 \\ 𝑦=𝑥+\frac{𝐶}{𝑥^{2}} & \end{aligned}


$$

We can check that

$$


\frac{\text{d}}{\text{d}x}( y \cdot x^2) = 3x^2


$$

is indeed equivalent to the original equation $(\ast)$ using the product rule:

$$


\begin{aligned}\frac{d}{d𝑥}(𝑦⋅𝑥^{2}) & =3𝑥^{2} \\ \frac{d}{d𝑥}(𝑦)⋅𝑥^{2}+𝑦⋅\frac{d}{d𝑥}(𝑥^{2}) & =3𝑥^{2} \\ 𝑥^{2}\frac{d𝑦}{d𝑥}+𝑦⋅2𝑥 & =3𝑥^{2} \\ 𝑥^{2}\frac{d𝑦}{d𝑥}+2𝑥𝑦 & =3𝑥^{2}\,✓\end{aligned}


$$

By finding an appropriate integrating factor, we can solve any first-order linear ODE! So the question is, how do we find an integrating factor? Let's discuss this next.

### The Integrating Factor Method

Given a first-order linear ODE, we can find an integrating factor and use it to solve the equation using the following procedure.

- **Step 1**: Write the equation in standard form:

- **Step 2**: Compute an integrating factor $I(x)$ using the definition

- **Step 3**: Multiply both sides of the equation found in step 1 by $I(x)\mathbin{:}$

- **Step 4**: Rewrite the left side as If steps 1 through 3 are done correctly, then we can always do this, and we can check that it's correct by differentiating. Our new equation is

- **Step 5**: Integrate both sides of the equation with respect to $x$ and solve for $y\mathbin{:}$

You might be wondering where the formula for $I(x)$ comes from; we'll discuss this at the end of the lesson. First, let's apply this method to a concrete example in the next slide.

### Example: Transforming First-Order Linear ODEs Using Integrating Factors

#### Question

Consider the following first-order linear ODE for the function $y = y(x)\mathbin{:}$

$$


\dfrac {\text{d}y} {\text{d}x} + 2y = 2e^{-2x}


$$

Write the equation in the form $\dfrac{\text{d}}{\text{d}x}\left(y I(x) \right) = I(x)Q(x),$ where $I(x)$ is an integrating factor.

#### Explanation

This equation is in the standard form

$$


\frac{\text{d}y}{\text{d}x} + P(x)y = Q(x)


$$

with $P(x) = 2$ and $Q(x) = 2e^{-2x}.$ We proceed to find an integrating factor $I(x)$ using the definition:

$$


\begin{aligned}𝐼(𝑥) & =𝑒^{∫𝑃(𝑥)\,d𝑥} \\ & =𝑒^{∫2\,d𝑥} \\ & =𝑒^{2𝑥}\end{aligned}


$$

Now, we multiply our differential equation through by $I(x) = e^{2x}$ as follows:

$$


\begin{aligned}𝑒^{2𝑥}⋅(\frac{d𝑦}{d𝑥}+2𝑦) & =𝑒^{2𝑥}⋅2𝑒^{−2𝑥} \\ 𝑒^{2𝑥}⋅\frac{d𝑦}{d𝑥}+2𝑒^{2𝑥}⋅𝑦 & =𝑒^{2𝑥}⋅2𝑒^{−2𝑥}\end{aligned}


$$

Finally, we rewrite the left hand side as $\dfrac{\text{d}}{\text{d}x}\left(y I(x)\right){:}$

$$


\begin{aligned}\frac{d}{d𝑥}(𝑦𝑒^{2𝑥}) & =𝑒^{2𝑥}⋅2𝑒^{−2𝑥}\end{aligned}


$$

### Example: Solving First-Order Linear ODEs Using Integrating Factors

#### Question

Find the general solution of the following differential equation using the method of integrating factors.

$$


\dfrac {\text{d}y} {\text{d}x} + \dfrac {3} {x} y = \dfrac{\cos x}{x^2}, \qquad x \gt 0.


$$

#### Explanation

This equation is in the standard form

$$


\dfrac{\text{d}y}{\text{d}x} + P(x)y = Q(x)


$$

with $P(x) = \dfrac{3}{x}$ and $Q(x) = \dfrac{\cos x}{x^2}.$ We proceed to find an integrating factor $I(x)$ using the definition:

$$


\begin{aligned}𝐼(𝑥) & =𝑒^{∫𝑃(𝑥)\,d𝑥} \\ & =𝑒^{∫(3/𝑥)\,d𝑥} \\ & =𝑒^{3ln⁡𝑥} \\ & =𝑒^{ln⁡(𝑥^{3})} \\ & =𝑥^{3}\end{aligned}


$$

Now, we multiply our differential equation through by $I(x) = x^3$ as follows:

$$


\begin{aligned}𝑥^{3}⋅(\frac{d𝑦}{d𝑥}+\frac{3}{𝑥}𝑦) & =𝑥^{3}⋅\frac{cos⁡𝑥}{𝑥^{2}} \\ 𝑥^{3}⋅\frac{d𝑦}{d𝑥}+3𝑥^{2}⋅𝑦 & =𝑥cos⁡𝑥\end{aligned}


$$

Finally, we rewrite the left hand side as $\dfrac{\text{d}}{\text{d}x}\left(y\cdot I(x)\right)$ and carry out the integration:

$$


\begin{aligned}\frac{d}{d𝑥}(𝑦𝑥^{3}) & =𝑥cos⁡𝑥 \\ ∫\frac{d}{d𝑥}(𝑦𝑥^{3})d𝑥 & =∫𝑥cos⁡𝑥\,d𝑥 \\ 𝑦𝑥^{3} & =∫𝑥cos⁡𝑥\,d𝑥\end{aligned}


$$

To solve this integral, we integrate by parts.

$$


\int uv'\,\textrm d x = uv - \int u' v\,\textrm d x


$$

Let $u = x, u' = 1, v' = \cos x,$ and $v = \sin x.$ Then, we have

$$


\begin{aligned}𝑦𝑥^{3} & =∫𝑥cos⁡𝑥\,d𝑥 \\ 𝑦𝑥^{3} & =𝑥sin⁡𝑥−∫sin⁡𝑥\,d𝑥 \\ 𝑦𝑥^{3} & =𝑥sin⁡𝑥+cos⁡𝑥+𝐶 \\ 𝑦 & =\frac{𝑥sin⁡𝑥+cos⁡𝑥}{𝑥^{3}}+\frac{𝐶}{𝑥^{3}}.\end{aligned}


$$

### Example: Solving First-Order Initial Value Problems Using Integrating Factors

#### Question

Solve the following initial value problem using the method of integrating factors.

$$


\dfrac {\text{d}y} {\text{d}x} + 3x^2y = 9x^2, \qquad y(0) = 1


$$

#### Explanation

This equation is in the standard form

$$


\frac{\text{d}y}{\text{d}x} + P(x)y = Q(x),


$$

with $P(x) = 3x^2$ and $Q(x) = 9x^2.$

We compute an integrating factor using the definition:

$$


\begin{aligned}𝐼(𝑥) & =𝑒^{∫𝑃(𝑥)\,d𝑥} \\ & =𝑒^{∫3𝑥^{2}\,d𝑥} \\ & =𝑒^{𝑥^{3}}\end{aligned}


$$

Multiplying both sides of the equation in standard form by $I(x) = e^{x^3}$ yields

$$


\begin{aligned}𝑒^{𝑥^{3}}⋅(\frac{d𝑦}{d𝑥}+3𝑥^{2}𝑦) & =𝑒^{𝑥^{3}}⋅9𝑥^{2} \\ 𝑒^{𝑥^{3}}⋅\frac{d𝑦}{d𝑥}+3𝑥^{2}𝑒^{𝑥^{3}}⋅𝑦 & =9𝑥^{2}𝑒^{𝑥^{3}} \\ \frac{d}{d𝑥}(𝑦𝑒^{𝑥^{3}}) & =9𝑥^{2}𝑒^{𝑥^{3}}.\end{aligned}


$$

Now, we integrate with respect to $x,$ making use of the substitution $u = x^3{:}$

$$


\begin{aligned}∫\frac{d}{d𝑥}(𝑦𝑒^{𝑥^{3}})d𝑥 & =∫9𝑥^{2}𝑒^{𝑥^{3}}\,d𝑥 \\ 𝑦𝑒^{𝑥^{3}} & =∫3𝑒^{𝑢}\,d𝑢 \\ 𝑦𝑒^{𝑥^{3}} & =3𝑒^{𝑢}+𝐶 \\ 𝑦𝑒^{𝑥^{3}} & =3𝑒^{𝑥^{3}}+𝐶 \\ 𝑦 & =3+𝐶𝑒^{−𝑥^{3}}\end{aligned}


$$

This is the general solution. To find the value of $C$ corresponding to the specific solution, we apply the initial condition $y(0) = 1$ as follows:

$$


\begin{aligned}𝑦(0) & =3+𝐶𝑒^{−0^{3}} \\ 1 & =3+𝐶 \\ 𝐶 & =−2\end{aligned}


$$

Therefore, the solution to the initial value problem is

$$


y = 3 - 2e^{-x^3}.


$$

### Deriving the Integrating Factor

We will now derive the formula for the integrating factor.

Consider the first-order linear equation in standard form

$$


\frac{\text{d}y}{\text{d}x} + P(x)y = Q(x).


$$

Our goal is to rewrite the left-hand side as the derivative of a product.

To do that, we multiply both sides of the equation by some function $I(x)$ that we wish to determine.

$$


{\color{blue}I(x)\frac{\text{d}y}{\text{d}x} + {\color{purple}I(x)P(x)}y} = I(x)Q(x)


$$

We want the left-hand side to match the derivative of $y\cdot I(x)$. But by the product rule,

$$


\frac{\text{d}}{\text{d}x}\Bigl(y\cdot I(x)\Bigr) = {\color{blue}I(x)\frac{\text{d}y}{\text{d}x} + {\color{purple}I'(x)}y}.


$$

So, if we choose $I(x)$ so that

$$


I'(x) = I(x)P(x),


$$

then the left-hand side becomes $\dfrac{\text{d}}{\text{d}x}\Bigl(y\cdot I(x)\Bigr).$

Dividing both sides of $I'(x) = I(x)P(x)$ by $I(x)$ gives

$$


\frac{I'(x)}{I(x)} = P(x).


$$

Next, integrating both sides with respect to $x$ yields

$$


\begin{aligned}∫\frac{𝐼^{′}(𝑥)}{𝐼(𝑥)}\,d𝑥 & =∫𝑃(𝑥)\,d𝑥 \\ ∫\frac{d}{d𝑥}(ln⁡(𝐼(𝑥)))\,d𝑥 & =∫𝑃(𝑥)\,d𝑥 \\ ln⁡(𝐼(𝑥)) & =∫𝑃(𝑥)\,d𝑥+𝐶 \\ 𝐼(𝑥) & =𝑒^{∫𝑃(𝑥)\,d𝑥+𝐶} \\ & =𝑒^{𝐶}⋅𝑒^{∫𝑃(𝑥)\,d𝑥}.\end{aligned}


$$

Finally, because multiplying $I(x)$ by a nonzero constant does not change the method, we can choose $e^C = 1$ and define an integrating factor as

$$


I(x) = e^{\int P(x)\,\text{d}x}.


$$
