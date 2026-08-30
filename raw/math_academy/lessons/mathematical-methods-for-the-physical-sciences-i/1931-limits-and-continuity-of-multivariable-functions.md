# Limits and Continuity of Multivariable Functions

Source: https://www.mathacademy.com/topics/1931?courseId=154
Topic ID: 1931

## Prerequisites

- [Defining Continuity at a Point](../ap-calculus-ab/314-defining-continuity-at-a-point.md)
- [Calculating Limits of Radical Functions Using Conjugate Multiplication](../ap-calculus-ab/604-calculating-limits-of-radical-functions-using-conjugate-multiplication.md)
- [The Domain of a Multivariable Function](./1899-the-domain-of-a-multivariable-function.md)

## Lesson

### Introduction

We can extend our knowledge of limits to multivariable functions. We'll first consider the two-variable case.

We denote $\mathbf{x}=(x,y)$ and $\mathbf{x}_0 = (a,b)$ as a particular, fixed vector. Let the function $f(x,y)$ be defined in some neighborhood of $\mathbf x_0.$

Then, the notation

$$


\lim\limits_{\mathbf{x} \to \mathbf{x}_0} f (x,y) = L


$$

means that the value of $f$ can be made as close as we want to $L,$ provided that $\mathbf x$ is sufficiently close to $\mathbf{x}_0.$

A few things to note:

- This definition of a limit also extends to functions of more than two variables in the natural way.

- All of the rules set out by the algebra of limits are valid for functions of several variables.

We say that $f(x,y)$ is **continuous** at $(a,b)$ if

$$


\lim\limits_{\mathbf{x} \to (a,b)} f (x,y) = f(a,b).


$$

So, if a function is continuous at $(a,b),$ then the limit can be evaluated by simply plugging $(x,y) = (a,b)$ into the function.

To demonstrate, let's calculate the following limit:

$$


\displaystyle{\lim_{\mathbf{x}\to (2,1)}} \dfrac{xy}{x^2+y^2}


$$

This function is continuous for all $(x,y)$ with the exception of $(0,0)$ where the denominator vanishes. Since the point $(2,1)$ does not cause the denominator to vanish, we can calculate the limit by substituting $(x,y) = (2,1)$ into the function:

$$


\begin{aligned}\underset{𝐱→(2,1)}{lim}\frac{𝑥𝑦}{𝑥^{2}+𝑦^{2}} & =\frac{2⋅1}{2^{2}+1^{2}}=\frac{2}{5}\end{aligned}


$$

### Example: Calculating Limits of Multivariable Functions at Points of Continuity

#### Question

Find $\displaystyle{\lim_{\mathbf{x}\to (-1,2)}} \dfrac{xy^3}{x+y}.$

#### Explanation

The function

$$


f(x,y)= \dfrac{xy^3}{x+y}


$$

is continuous except when the denominator is zero. However, the point $(-1,2)$ does not cause the denominator to become zero, so we can calculate the limit by substituting $(-1,2)$ into the function:

$$


\begin{aligned}\underset{𝐱→(−1,2)}{lim}\frac{𝑥𝑦^{3}}{𝑥+𝑦} & =\frac{(−1)⋅2^{3}}{(−1)+2} \\ & =\frac{−8}{1} \\ & =−8\end{aligned}


$$

### Calculating Limits of Multivariable Rational Functions by Factoring

Sometimes, we may need to simplify a limit before we can evaluate it.

For example, let's consider the limit

$$


\displaystyle{\lim_{\mathbf{x}\to (2,-1)}} \dfrac{x^2+2xy}{xy+2y^2}.


$$

Direct substitution causes this limit to take the indeterminate form $\dfrac 00$ because the numerator and denominator both evaluate to zero at the given point.

$$


\displaystyle{\lim_{\mathbf{x}\to (2,-1)}} \dfrac{x^2+2xy}{xy+2y^2} = \dfrac{(2)^2 + 2(2)(-1)}{(2)(-1) + 2(-1)^2} = \dfrac{0}{0}


$$

However, we can simplify the limit by factoring the numerator and denominator and then canceling a common factor, as follows:

$$


\begin{aligned}\underset{𝐱→(2,−1)}{lim}\frac{𝑥^{2}+2𝑥𝑦}{𝑥𝑦+2𝑦^{2}} & =\underset{𝐱→(2,−1)}{lim}\frac{𝑥(𝑥+2𝑦)}{𝑦(𝑥+2𝑦)} \\ & =\underset{𝐱→(2,−1)}{lim}\frac{𝑥}{𝑦}\end{aligned}


$$

Now that the limit has been simplified, we can evaluate it:

$$


\begin{aligned}\underset{𝐱→(2,−1)}{lim}\frac{𝑥}{𝑦}=\frac{2}{−1}=−2\end{aligned}


$$

So, we conclude that

$$


\displaystyle{\lim_{\mathbf{x}\to (2,-1)}} \dfrac{x^2+2xy}{xy+2y^2} = -2.


$$

### Example: Calculating Limits of Multivariable Rational Functions by Factoring

#### Question

Find $\displaystyle{\lim_{\mathbf{x}\to (-1,1)}} \dfrac{x^2y+xy^2}{x^2-y^2}.$

#### Explanation

Attempting to evaluate the limit by direct substitution leads to the indeterminate form $\dfrac 0 0,$ as follows:

$$


\displaystyle{\lim_{\mathbf{x}\to (-1,1)}} \dfrac{x^2y+xy^2}{x^2-y^2} = \dfrac{(-1)^2(1) + (-1)(1)^2}{(-1)^2 - (1)^2} = \dfrac{0}{0}


$$

However, we can simplify the limit by canceling common factors in the numerator and denominator:

$$


\begin{aligned}\underset{𝐱→(−1,1)}{lim}\frac{𝑥^{2}𝑦+𝑥𝑦^{2}}{𝑥^{2}−𝑦^{2}} & =\underset{𝐱→(−1,1)}{lim}\frac{𝑥𝑦(𝑥+𝑦)}{(𝑥+𝑦)(𝑥−𝑦)} \\ & =\underset{𝐱→(−1,1)}{lim}\frac{𝑥𝑦}{(𝑥−𝑦)}\end{aligned}


$$

Now that the limit has been simplified, we can evaluate it:

$$


\begin{aligned}\underset{𝐱→(−1,1)}{lim}\frac{𝑥𝑦}{(𝑥−𝑦)} & =\frac{(−1)⋅1}{−1−1} \\ & =\frac{−1}{−2} \\ & =\frac{1}{2}\end{aligned}


$$

Therefore, the limit evaluates to $\dfrac{1}{2}.$

### Example: Calculating Limits of Multivariable Functions Using Conjugate Multiplication

#### Question

Find $\displaystyle{\lim_{\mathbf{x}\to (2,1)}} \dfrac{x^2-4y}{x-2\sqrt{y}}.$

#### Explanation

Attempting to evaluate the limit by direct substitution leads to the indeterminate form $\dfrac00,$ as follows:

$$


\displaystyle{\lim_{\mathbf{x}\to (2,1)}} \dfrac{2^2-4 \cdot 1}{2-2\sqrt{1}} = \dfrac{0}{0}


$$

However, we can simplify the limit by first multiplying the numerator and denominator by the conjugate of the denominator:

$$


\begin{aligned}\underset{𝐱→(2,1)}{lim}\frac{𝑥^{2}−4𝑦}{𝑥−2\sqrt{√𝑦}} & =\underset{𝐱→(2,1)}{lim}\frac{(𝑥^{2}−4𝑦)(𝑥+2\sqrt{√𝑦})}{(𝑥−2\sqrt{√𝑦})(𝑥+2\sqrt{√𝑦})} \\ & =\underset{𝐱→(2,1)}{lim}\frac{(𝑥^{2}−4𝑦)(𝑥+2\sqrt{√𝑦})}{𝑥^{2}−(2\sqrt{√𝑦})^{2}} \\ & =\underset{𝐱→(2,1)}{lim}\frac{(𝑥^{2}−4𝑦)(𝑥+2\sqrt{√𝑦})}{𝑥^{2}−4𝑦} \\ & =\underset{𝐱→(2,1)}{lim}(𝑥+2\sqrt{√𝑦})\end{aligned}


$$

Now that the limit has been simplified, we can evaluate it:

$$


\begin{aligned}\underset{𝐱→(2,1)}{lim}(𝑥+2\sqrt{√𝑦}) & =2+2\sqrt{√1} \\ & =2+2 \\ & =4\end{aligned}


$$

Therefore, the limit evaluates to $4.$

### The Definition of a Limit: Single Variable Functions vs. Multivariable Functions

Recall that for a function of a single variable $f(x),$ if the left and right limits both exist and are equal at some point $x=a$, then this is sufficient to conclude that the limit exists at $x=a.$

So, if we have

$$


\lim_{x\to a^-} f(x) = \lim_{x\to a^+} f(x) = L,


$$

then we may conclude that

$$


\lim_{x\to a} f(x) = L.


$$

For a multivariable function, the situation is not so straightforward. For a function of two variables $f(x,y),$ we may only conclude that

$$


\lim_{\mathbf{x} \to \mathbf{x}_0} f(x,y) = L,


$$

if we can show that the limit is the same *for all possible paths* on which $\mathbf x$ can approach $\mathbf{x}_0.$

### Proving That a Limit Does Not Exist by Evaluating It Along Different Paths

However, it is often easy to show that a limit does not exist for a multivariable function. All we have to do is find two paths on which the limit evaluates to different results.

As an example, let's consider the following limit:

$$


\lim\limits_{\mathbf{x} \to (0,0)} \dfrac{y}{x+y}


$$

Clearly, direct substitution leads to the indeterminate form $\dfrac00.$ Let's compute the limit along the paths $y=x$ and $y=x^2.$ We will see that the limit evaluates to different results on these two paths.

- Taking $\mathbf{x} \to (0,0)$ along the path $y=x,$ we have

- Taking $\mathbf{x} \to (0,0)$ along the path $y=x^2,$ we have

Because the limit evaluates to different results on these two paths, we conclude that the limit does not exist:

$$


\displaystyle{\lim_{\mathbf{x}\to (0,0)}} \dfrac{y}{x +y} = \text{DNE}


$$

### Example: Calculating Limits Along Different Paths for Multivariable Functions

#### Question

Find $\displaystyle{\lim_{\mathbf{x}\to (0,0)}} \dfrac{x(x + 2y)}{y^2}.$

#### Explanation

Direct substitution gives an indeterminate form, but the function cannot be simplified by canceling a common factor in the numerator and denominator:

$$


\displaystyle{\lim_{\mathbf{x}\to (0,0)}} \dfrac{x(x + 2y)}{y^2} = \dfrac{0 \cdot (0 + 2 \cdot 0)}{0^2} = \dfrac{0}{0}


$$

Let's evaluate the limit approaching $(0,0)$ from different paths.

- Taking $\mathbf{x} \to (0,0)$ along the path $y=x,$ we have

- Taking $\mathbf{x} \to (0,0)$ along the path $y=-x,$ we have

Because the limit evaluates to different results on these two paths, we conclude that the limit does not exist:

$$


\displaystyle{\lim_{\mathbf{x}\to (0,0)}} \dfrac{x(x + 2y)}{y^2} = \text{DNE}


$$
