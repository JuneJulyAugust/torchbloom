# Linearity of Laplace Transforms

Source: https://www.mathacademy.com/topics/2537?courseId=61
Topic ID: 2537

## Prerequisites

- [The Hyperbolic Functions](../calculus-i/967-the-hyperbolic-functions.md)
- [Introduction to Laplace Transforms](./2529-introduction-to-laplace-transforms.md)

## Lesson

### Introduction

In the previous lesson, we learned how to compute Laplace transforms directly from the definition,

$$


\mathcal L\{f(t)\} = \int_0^\infty e^{-st}f(t)\,\textrm d t,


$$

where $s$ is a real number.

So far, the following basic transforms have been computed:

Of course, not every function will appear in a table. Fortunately, the Laplace transform has a **linearity** property, which lets us break complicated functions into simpler pieces.

For functions $f(t)$ and $g(t),$ the linearity property states that

$$


\mathcal L\{\alpha f(t) + \beta g(t)\} = \alpha\cdot \mathcal L\{f(t)\} + \beta\cdot \mathcal L\{g(t)\},


$$

where $\alpha$ and $\beta$ are constants.

**Watch out:** Laplace transforms do *not* distribute over products. In general,

$$


\mathcal{L}\left\{f(t)\,g(t) \right\} \ne \mathcal{L}\left\{ f(t) \right\}\,\mathcal{L}\left\{ g(t) \right\}.


$$

Finally, when we apply linearity, the Laplace transform of the overall function exists only where *every* piece exists. So the domain of

$$


\mathcal L\{\alpha f(t) + \beta g(t)\}


$$

is the *intersection* of the domains of $\mathcal L\{f(t)\}$ and $\mathcal L\{g(t)\}.$

In the next slide, we will apply the linearity property to a concrete example.

### Example: Finding Laplace Transforms of Sums of Exponentials

#### Question

Find the Laplace transform of $f(t) = e^{-3t}-e^{5t}$ for $s>5.$

#### Explanation

The linearity property of the Laplace transform states that for functions $f(t)$ and $g(t),$ we have

$$


\mathcal L\{\alpha f(t) + \beta g(t)\} = \alpha\cdot \mathcal L\{f(t)\} + \beta\cdot \mathcal L \{g(t)\},


$$

where $\alpha$ and $\beta$ are constants.

Taking the Laplace transform and applying the linearity properties, we have

$$


\begin{aligned}L{𝑒^{−3𝑡}−𝑒^{5𝑡}} & =L{𝑒^{−3𝑡}}+L{−𝑒^{5𝑡}} \\ & =L{𝑒^{−3𝑡}}−L{𝑒^{5𝑡}}.\end{aligned}


$$

Next, we recall the following result:

$$


\mathcal L\left\{e^{kt}\right\} = \dfrac{1}{s-k}, \qquad s > k


$$

Therefore, we have the following:

$$


\begin{aligned}L{𝑒^{−3𝑡}} & =\frac{1}{𝑠+3},\,𝑠>−3 \\ L{𝑒^{5𝑡}} & =\frac{1}{𝑠−5},\,𝑠>5\end{aligned}


$$

Therefore, the Laplace transform of $f(t)$ is

$$


\begin{aligned}L{𝑓(𝑡)} & =L{𝑒^{−3𝑡}}−L{𝑒^{5𝑡}} \\ & =\frac{1}{𝑠+3}−\frac{1}{𝑠−5} \\ & =\frac{(𝑠−5)−(𝑠+3)}{(𝑠+3)(𝑠−5)} \\ & =\frac{−8}{(𝑠+3)(𝑠−5)} \\ & =−\frac{8}{(𝑠+3)(𝑠−5)}.\end{aligned}


$$

Finally, since $\mathcal L\{e^{-3t}\}$ is defined for $s\in (-3,\infty)$ and $\mathcal L \{e^{5t}\}$ is defined for $s\in (5,\infty),$ we have that $\mathcal L\{f(t)\}$ is defined for

$$


(-3,\infty) \cap (5,\infty) = (5,\infty),


$$

that is, $s > 5.$

### Laplace Transforms of Hyperbolic and Trigonometric Functions

Linearity becomes especially useful when a function can be rewritten as a linear combination of exponentials.

In particular, we can rewrite hyperbolic and trigonometric functions using exponentials:

$$


\cos(\omega t) = \dfrac{e^{\textrm i \omega t} + e^{-\textrm i \omega t}}{2}, \qquad \sin(\omega t) = \dfrac{e^{\textrm i \omega t} - e^{-\textrm i \omega t}}{2\textrm i},


$$

$$


\cosh(\omega t) = \dfrac{e^{\omega t} + e^{-\omega t}}{2}, \qquad \sinh(\omega t) = \dfrac{e^{\omega t} - e^{-\omega t}}{2}.


$$

Then we take the Laplace transform of *both sides* and apply linearity term-by-term.

To do this, we use the transforms we already know:

$$


\mathcal L\{e^{kt}\} = \dfrac{1}{s-k},\qquad s > k, \qquad\qquad \mathcal L\{e^{\textrm i \omega t}\} = \dfrac{1}{s-\textrm i \omega},\qquad s > 0.


$$

**Note.** Even though complex exponentials appear in these identities, we are still treating $s$ as a real variable in this lesson.

Let's take a look at an example.

### Finding the Laplace Transform of Cosine Using Linearity

We will find the Laplace transform of $\cos(t)$ by rewriting it using complex exponentials and applying linearity.

First, we recall the identity

$$


\cos(t) = \dfrac{e^{\mathrm{i} t} + e^{-\mathrm{i} t}}{2}.


$$

Now, we take the Laplace transform of *both sides*:

$$


\mathcal L\{\cos(t)\} = \mathcal L\left\{\dfrac{e^{\mathrm{i} t} + e^{-\mathrm{i} t}}{2}\right\}.


$$

Next, we apply linearity:

$$


\begin{aligned}L{cos⁡(𝑡)} & =\frac{1}{2}\,L{𝑒^{i𝑡}+𝑒^{−i𝑡}} \\ & =\frac{1}{2}(L{𝑒^{i𝑡}}+L{𝑒^{−i𝑡}}).\end{aligned}


$$

From the previous lesson, we know that for $s>0,$

$$


\mathcal L\{e^{\mathrm{i} \omega t}\} = \dfrac{1}{s-\mathrm{i} \omega}.


$$

So for $\omega=1,$ we have

$$


\mathcal L\{e^{\mathrm{i} t}\} = \dfrac{1}{s-\mathrm{i}}, \qquad \mathcal L\{e^{-\mathrm{i} t}\} = \dfrac{1}{s+\mathrm{i}}.


$$

Substituting these into our expression gives

$$


\begin{aligned}L{cos⁡(𝑡)} & =\frac{1}{2}(\frac{1}{𝑠−i}+\frac{1}{𝑠+i}) \\ & =\frac{1}{2}(\frac{(𝑠+i)+(𝑠−i)}{(𝑠−i)(𝑠+i)}) \\ & =\frac{1}{2}(\frac{2𝑠}{𝑠^{2}−i^{2}}) \\ & =\frac{1}{2}(\frac{2𝑠}{𝑠^{2}+1}) \\ & =\frac{𝑠}{𝑠^{2}+1}.\end{aligned}


$$

Therefore,

$$


\mathcal L\{\cos(t)\} = \dfrac{s}{s^2+1}, \qquad s>0.


$$

### Example: Finding Laplace Transforms of Trigonometric and Hyperbolic Functions

#### Question

Use the Laplace transform of $f(t) = e^{kt}$ to find the Laplace transform of $\sinh(3t).$

#### Explanation

The linearity property of the Laplace transform states that for functions $f(t)$ and $g(t),$ we have

$$


\mathcal L\{\alpha f(t) + \beta g(t)\} = \alpha\cdot \mathcal L\{f(t)\} + \beta\cdot \mathcal L \{g(t)\},


$$

where $\alpha$ and $\beta$ are constants.

First, recall that, by definition

$$


\sinh(3t) = \dfrac{e^{3t} - e^{-3t}}{2}.


$$

Taking the Laplace transform and applying the linearity property, we have

$$


\begin{aligned}L{sinh⁡(3𝑡)} & =L{\frac{𝑒^{3𝑡}−𝑒^{−3𝑡}}{2}} \\ & =L{\frac{𝑒^{3𝑡}}{2}−\frac{𝑒^{−3𝑡}}{2}} \\ & =L{\frac{𝑒^{3𝑡}}{2}}−L{\frac{𝑒^{−3𝑡}}{2}} \\ & =\frac{1}{2}L{𝑒^{3𝑡}}−\frac{1}{2}L{𝑒^{−3𝑡}}.\end{aligned}


$$

Now, we recall that

$$


\mathcal L\left\{e^{kt}\right\} = \dfrac{1}{s-k}, \qquad s > k.


$$

Therefore, we have the following:

$$


\begin{aligned}L{𝑒^{3𝑡}} & =\frac{1}{𝑠−3},\,𝑠>3 \\ L{𝑒^{−3𝑡}} & =\frac{1}{𝑠+3},\,𝑠>−3\end{aligned}


$$

Therefore, the Laplace transform of $\sinh(3t)$ is

$$


\begin{aligned}L{sinh⁡(3𝑡)} & =\frac{1}{2}L{𝑒^{3𝑡}}−\frac{1}{2}L{𝑒^{−3𝑡}} \\ & =\frac{1}{2}⋅\frac{1}{𝑠−3}−\frac{1}{2}⋅\frac{1}{𝑠+3} \\ & =\frac{1}{2}(\frac{1}{𝑠−3}−\frac{1}{𝑠+3}) \\ & =\frac{1}{2}(\frac{(𝑠+3)−(𝑠−3)}{(𝑠−3)(𝑠+3)}) \\ & =\frac{1}{2}(\frac{6}{𝑠^{2}−9}) \\ & =\frac{3}{𝑠^{2}−9}.\end{aligned}


$$

Finally, since $\mathcal L\{e^{3t}\}$ is defined for $s\in (3,\infty)$ and $\mathcal L \{e^{-3t}\}$ is defined for $s\in (-3,\infty),$ we have that $\mathcal L\{\sinh(3t)\}$ is defined for

$$


(3,\infty) \cap (-3,\infty) = (3,\infty),


$$

that is, $s > 3.$

### Example: Finding Laplace Transforms of Combined Functions

#### Question

Given that for $s > 0,$

$$


\begin{aligned}L{sin⁡𝜔𝑡}=\frac{𝜔}{𝑠^{2}+𝜔^{2}},\,L{cos⁡𝜔𝑡}=\frac{𝑠}{𝑠^{2}+𝜔^{2}},\end{aligned}


$$

find the Laplace transform of $f(t) = 3\cos{9t} - 2\sin{9t}$ for $s > 0.$

#### Explanation

The linearity property of the Laplace transform states that for functions $f(t)$ and $g(t),$ we have

$$


\mathcal L\{\alpha f(t) + \beta g(t)\} = \alpha\cdot \mathcal L\{f(t)\} + \beta\cdot \mathcal L \{g(t)\},


$$

where $\alpha$ and $\beta$ are constants.

Taking the Laplace transform and applying the linearity property, we have

$$


\begin{aligned}L{3cos⁡9𝑡−2sin⁡9𝑡} & =L{3cos⁡9𝑡}+L{−2sin⁡9𝑡} \\ & =3L{cos⁡9𝑡}−2L{sin⁡9𝑡}.\end{aligned}


$$

We are given that

$$


\begin{aligned}L{sin⁡𝜔𝑡} & =\frac{𝜔}{𝑠^{2}+𝜔^{2}}, & & 𝑠>0, \\ L{cos⁡𝜔𝑡} & =\frac{𝑠}{𝑠^{2}+𝜔^{2}}, & & 𝑠>0.\end{aligned}


$$

Therefore, we have the following:

$$


\begin{aligned}L{cos⁡9𝑡} & =\frac{𝑠}{𝑠^{2}+81},\,𝑠>0 \\ L{sin⁡9𝑡} & =\frac{9}{𝑠^{2}+81},\,𝑠>0\end{aligned}


$$

Therefore, the Laplace transform of $f(t)$ is

$$


\begin{aligned}L{𝑓(𝑡)} & =3L{cos⁡9𝑡}−2L{sin⁡9𝑡} \\ & =3⋅\frac{𝑠}{𝑠^{2}+81}−2⋅\frac{9}{𝑠^{2}+81} \\ & =\frac{3𝑠}{𝑠^{2}+81}−\frac{18}{𝑠^{2}+81} \\ & =\frac{3𝑠−18}{𝑠^{2}+81}.\end{aligned}


$$

### An Updated Table of Laplace Transforms

Using linearity, we can build new Laplace transforms from old ones.

The following Laplace transforms have been established so far:

As we make progress, we will continue using properties of Laplace transforms (like linearity) to expand this table.
