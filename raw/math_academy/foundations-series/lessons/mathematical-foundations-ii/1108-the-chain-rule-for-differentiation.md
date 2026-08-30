# The Chain Rule for Differentiation

Source: https://www.mathacademy.com/topics/1108?courseId=111
Topic ID: 1108

## Prerequisites

- [Calculating the Equation of a Tangent Line Using Differentiation](./986-calculating-the-equation-of-a-tangent-line-using-differentiation.md)

## Lesson

### Introduction

The **chain rule** for differentiation states that the derivative of a composite function $f(g(x))$ is given by

$$


\dfrac {\textrm{d}f} {\textrm{d}x} = \dfrac {\textrm{d}f} {\textrm{d}g} \cdot \dfrac {\textrm{d}g} {\textrm{d}x}.


$$

There is some intuition behind this rule: if we think of the derivatives as fractions, the ${\textrm{d}g}$'s would appear to cancel out.

$$


\begin{aligned}\frac{d𝑓}{d𝑥}=\frac{d𝑓}{d𝑔}⋅\frac{d𝑔}{d𝑥}\end{aligned}


$$

To see how the chain rule can be used to differentiate a function like

$$


f(x) = (1+2x)^3,


$$

first, notice that the function can be written as a composite function

$$


f(g) = g^3, \qquad g(x) = 1+2x.


$$

We can use the chain rule to compute the derivative of this composite function:

$$


\begin{aligned}\frac{d𝑓}{d𝑥} & =\frac{d𝑓}{d𝑔}⋅\frac{d𝑔}{d𝑥} \\ & =\frac{d}{d𝑔}(𝑔^{3})⋅\frac{d}{d𝑥}(1+2𝑥) \\ & =3𝑔^{2}⋅2 \\ & =6𝑔^{2}\end{aligned}


$$

Substituting $g(x) = 1+2x$ for $g,$ we obtain the final result:

$$


\begin{aligned}\frac{d𝑓}{d𝑥} & =6(1+2𝑥)^{2}\end{aligned}


$$

**Note:** We'll provide a derivation of the chain rule at the end of the lesson.

### Example: Differentiating a Polynomial Raised to a Power Using the Chain Rule

#### Question

Given that $f(x) = (3x^4+x^3)^5,$ calculate $\dfrac {\textrm{d}f} {\textrm{d}x}.$

#### Explanation

First, we express $f(x)$ as a composite function:

$$


f = g^5, \qquad g = 3x^4+x^3


$$

The chain rule states that

$$


\dfrac {\textrm{d}f} {\textrm{d}x} = \dfrac {\textrm{d}f} {\textrm{d}g} \cdot \dfrac {\textrm{d}g} {\textrm{d}x}.


$$

Differentiating, we have

$$


\dfrac {\textrm{d}f} {\textrm{d}g} = 5g^4,


$$

and

$$


\dfrac {\textrm{d}g} {\textrm{d}x} = 12x^3 + 3x^2.


$$

Finally, multiplying the two together and substituting for $g$ gives

$$


\begin{aligned}\frac{d𝑓}{d𝑥} & =5𝑔^{4}⋅(12𝑥^{3}+3𝑥^{2}) \\ & =5(3𝑥^{4}+𝑥^{3})^{4}(12𝑥^{3}+3𝑥^{2}).\end{aligned}


$$

### Example: Differentiating a Radical Function Using the Chain Rule

#### Question

Given that $y = \sqrt{1-x^2},$ find $\dfrac{\textrm d y}{\textrm d x}.$

#### Explanation

We use the chain rule in the form

$$


\dfrac{\textrm d y}{\textrm d x} = \dfrac{\textrm d y}{\textrm d u}\cdot \dfrac{\textrm d u}{\textrm d x}.


$$

Here, we've used $u$ instead of $g$ for the intermediate variable.

Let $u=1-x^2.$ Then $y = \sqrt u = u^{1/2}.$ Differentiating, we have

$$


\dfrac{\textrm d y}{\textrm d u} = \dfrac{1}{2}u^{-1/2} = \dfrac{1}{2\sqrt u}


$$

and

$$


\dfrac{\textrm d u}{\textrm d x} = -2x.


$$

Multiplying the two together gives

$$


\begin{aligned}\frac{d𝑦}{d𝑥} & =\frac{1}{2\sqrt{√𝑢}}⋅(−2𝑥) \\ & =−\frac{2𝑥}{2\sqrt{√𝑢}} \\ & =−\frac{𝑥}{\sqrt{√1−𝑥^{2}}}.\end{aligned}


$$

### Another Notation for the Chain Rule

The chain rule can also be expressed using primes instead of Leibniz notation.

The chain rule, in prime notation, states that

$$


(f(g(x)))' = f'(g(x)) \cdot g'(x).


$$

### Example: Differentiating a Function Using the Chain Rule and Prime Notation

#### Question

Given that $f(x) = \dfrac{1}{\sqrt{1-3x}},$ calculate $f'(x).$

#### Explanation

Let $g(x)=1-3x$ and $f(g(x)) = \dfrac{1}{\sqrt{g}} = g^{-1/2}.$

Differentiating, we have

$$


\begin{aligned}𝑓^{′}(𝑔(𝑥)) & =(𝑔^{−1/2})^{′}=−\frac{1}{2}𝑔^{−3/2}=−\frac{1}{2𝑔^{3/2}}, \\ 𝑔^{′}(𝑥) & =(1−3𝑥)^{′}=−3.\end{aligned}


$$

Then, using the chain rule,

$$


\begin{aligned}𝑓^{′}(𝑥) & =𝑓^{′}(𝑔(𝑥))⋅𝑔^{′}(𝑥) \\ & =−\frac{1}{2𝑔^{3/2}}⋅(−3) \\ & =\frac{3}{2𝑔^{3/2}} \\ & =\frac{3}{2(1−3𝑥)^{3/2}}\end{aligned}


$$

### Deriving the Chain Rule

Let's now prove the chain rule in the following form:

$$


(f \circ g)'(a) = f'(g(a)) \cdot g'(a)


$$

Let $f$ and $g$ be functions such that

- $g$ is differentiable at $a$,

- $f$ is differentiable at $g(a)$.

Then $f \circ g$ is differentiable at $a$, and we compute its derivative as follows.

We start with the definition of the derivative:

$$


(f \circ g)'(a) = \lim_{x \to a} \frac{f(g(x)) - f(g(a))}{x - a}


$$

Since $g$ is differentiable at $a$, it is also continuous there. Hence $g(x) \to g(a)$ as $x \to a$. For $x$ sufficiently close to $a$, we have $g(x) \ne g(a)$, so we may write

$$


\frac{f(g(x)) - f(g(a))}{x - a} = \frac{f(g(x)) - f(g(a))}{g(x) - g(a)} \cdot \frac{g(x) - g(a)}{x - a}.


$$

Taking the limit as $x \to a$, and using the product rule for limits (which applies since both limits exist), we obtain

$$


\begin{aligned}(𝑓∘𝑔)^{′}(𝑎) & =\underset{𝑥→𝑎}{lim}(\frac{𝑓(𝑔(𝑥))−𝑓(𝑔(𝑎))}{𝑔(𝑥)−𝑔(𝑎)}⋅\frac{𝑔(𝑥)−𝑔(𝑎)}{𝑥−𝑎}) \\ & =\underset{𝑥→𝑎}{lim}\frac{𝑓(𝑔(𝑥))−𝑓(𝑔(𝑎))}{𝑔(𝑥)−𝑔(𝑎)}⋅\underset{𝑥→𝑎}{lim}\frac{𝑔(𝑥)−𝑔(𝑎)}{𝑥−𝑎} \\ & =𝑓^{′}(𝑔(𝑎))⋅𝑔^{′}(𝑎)\end{aligned}


$$

as required.
