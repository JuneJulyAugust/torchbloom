# The Power-Reducing Formulas for Sine and Cosine

Source: https://www.mathacademy.com/topics/928?courseId=43
Topic ID: 928

## Prerequisites

- [De Moivre's Theorem](./925-de-moivre-s-theorem.md)
- [The Special Case of the Binomial Theorem](./3764-the-special-case-of-the-binomial-theorem.md)

## Lesson

### Introduction

Using De Moivre's theorem, it's possible to express any integer power of $\cos\theta$ or $\sin\theta$ in terms of single powers of $\cos\theta, \cos2\theta, \ldots$ for cosine, or $\sin\theta, \sin2\theta, \ldots$ for sine. The key is to use the so-called **power-reducing formulas**.

Let $z=\cos\theta + \text{i}\sin\theta.$ Then, we have the following:

- The **power-reducing formula for cosine** is

- The **power-reducing formula for sine** is

At the end of this lesson, we will walk through how to derive the formulas from De Moivre's theorem. But for now, let's focus on using the formulas.

### Reducing the Power of a Single-Angle Expression

Let's use the power-reduction formula for cosine to express $\cos^4\theta$ in terms of $\cos\theta, \cos2\theta,\ldots,$ etc.

Let $z = \cos\theta + \text{i}\sin\theta.$ We start with the power-reducing formulas for cosine:

$$



\begin{aligned}𝑧+\frac{1}{𝑧}=2cos⁡𝜃,\,𝑧^{𝑛}+\frac{1}{𝑧^{𝑛}}=2cos⁡𝑛𝜃\end{aligned}



$$

To get a $\cos^4 \theta$ term, we raise both sides of the first identity to the power of $4,$ and we get

$$



\begin{aligned}(𝑧+\frac{1}{𝑧})^{4} & =(2cos⁡𝜃)^{4} \\ & =16cos^{4}⁡𝜃.\end{aligned}



$$

Now, we expand the binomial on the left-hand side and simplify the result using the power-reducing formula for cosine:

$$



\begin{aligned}(𝑧+\frac{1}{𝑧})^{4} & =𝑧^{4}+4𝑧^{3}(\frac{1}{𝑧})+6𝑧^{2}(\frac{1}{𝑧})^{2}+4𝑧(\frac{1}{𝑧})^{3}+(\frac{1}{𝑧})^{4} \\ & =𝑧^{4}+4𝑧^{2}+6+\frac{4}{𝑧^{2}}+\frac{1}{𝑧^{4}} \\ & =(𝑧^{4}+\frac{1}{𝑧^{4}})+4(𝑧^{2}+\frac{1}{𝑧^{2}})+6 \\ & =2cos⁡4𝜃+4(2cos⁡2𝜃)+6 \\ & =2cos⁡4𝜃+8cos⁡2𝜃+6\end{aligned}



$$

By equating $16\cos^4\theta$ with the above, we have

$$



16\cos^4\theta = 2\cos4\theta + 8\cos2\theta+6,



$$

and therefore

$$



\cos^4\theta= \dfrac{1}{8}\cos4\theta + \dfrac{1}{2}\cos2\theta+\dfrac{3}{8}\,.



$$

### Example: Writing a Power of Cosine as a Sum of Cosines of Multiple Angles

#### Question

Find the value of the constant $B$ in the trigonometric identity $\cos^3\theta = A\cos3\theta + B\cos\theta.$

#### Explanation

Let $z = \cos\theta + \text{i}\sin\theta.$ We start with the following identities:

$$



\begin{aligned}𝑧+\frac{1}{𝑧}=2cos⁡𝜃,\,𝑧^{𝑛}+\frac{1}{𝑧^{𝑛}}=2cos⁡𝑛𝜃\end{aligned}



$$

Raising both sides to the power $3$ in the first identity, we get

$$



\left(z + \dfrac{1}{z}\right)^3 = (2\cos\theta)^3 =8\cos^3\theta.



$$

Now, we expand the binomial using the binomial theorem and simplify the result using our identities, as follows:

$$



\begin{aligned}(𝑧+\frac{1}{𝑧})^{3} & =𝑧^{3}+3𝑧^{2}(\frac{1}{𝑧})+3𝑧(\frac{1}{𝑧})^{2}+(\frac{1}{𝑧})^{3} \\ & =𝑧^{3}+3𝑧+3(\frac{1}{𝑧})+\frac{1}{𝑧^{3}} \\ & =\underset{2cos⁡3𝜃}{\underset{}{(𝑧^{3}+\frac{1}{𝑧^{3}})}}+3\underset{2cos⁡𝜃}{\underset{}{(𝑧+\frac{1}{𝑧})}} \\ & =2cos⁡3𝜃+3(2cos⁡𝜃) \\ & =2cos⁡3𝜃+6cos⁡𝜃\end{aligned}



$$

So, by equating $8\cos^3\theta$ with the above, we get

$$



8\cos^3\theta = 2\cos3\theta + 6\cos\theta.



$$

Finally, we divide both sides of the equation by $8,$ which gives

$$



\cos^3\theta = \frac{1}{4}\cos3\theta + \frac{3}{4}\cos\theta.



$$

Therefore, $B=\dfrac{3}{4}.$

### Example: Writing an Odd Power of Sine as a Sum of Sines of Multiple Angles

#### Question

Find the value of the constant $A$ in the trigonometric identity $\sin^5\theta = A\sin5\theta + B\sin3\theta + C\sin\theta.$

#### Explanation

Let $z = \cos\theta + \text{i}\sin\theta.$ We start with the following identities:

$$



\begin{aligned}(𝑧−\frac{1}{𝑧})=2isin⁡𝜃\,(𝑧^{𝑛}−\frac{1}{𝑧^{𝑛}})=2isin⁡𝑛𝜃\end{aligned}



$$

Raising both sides to the power $5$ in the first identity, we get

$$



\left(z - \dfrac{1}{z}\right)^5 = (2\text{i}\sin\theta)^5 \%=32\text{i}^5\sin^5\theta =32\text{i}\sin^5\theta \,.



$$

Now, we expand the binomial using the binomial theorem and simplify the result using our identities, as follows:

$$



\begin{aligned}(𝑧−\frac{1}{𝑧})^{5} & =𝑧^{5}−5𝑧^{4}(\frac{1}{𝑧})+10𝑧^{3}(\frac{1}{𝑧})^{2}−10𝑧^{2}(\frac{1}{𝑧})^{3}+5𝑧(\frac{1}{𝑧})^{4}−(\frac{1}{𝑧})^{5} \\ & =𝑧^{5}−5𝑧^{3}+10𝑧−\frac{10}{𝑧}+\frac{5}{𝑧^{3}}−\frac{1}{𝑧^{5}} \\ & =\underset{2isin⁡5𝜃}{\underset{}{(𝑧^{5}−\frac{1}{𝑧^{5}})}}−5\underset{2isin⁡3𝜃}{\underset{}{(𝑧^{3}−\frac{1}{𝑧^{3}})}}+10\underset{2isin⁡𝜃}{\underset{}{(𝑧−\frac{1}{𝑧})}} \\ & =2isin⁡5𝜃−5(2isin⁡3𝜃)+10(2isin⁡𝜃) \\ & =2isin⁡5𝜃−10isin⁡3𝜃+20isin⁡𝜃\end{aligned}



$$

By equating $32\text{i} \sin^5 \theta$ with the above, we get

$$



32\text{i}\sin^5\theta = 2\text{i}\sin5\theta - 10\text{i}\sin3\theta + 20\text{i}\sin\theta.



$$

Finally, we divide both sides of the equation by $32\text{i},$ which gives

$$



\sin^5\theta = \dfrac{1}{16}\sin5\theta - \dfrac{5}{16}\sin3\theta+\dfrac{5}{8}\sin\theta.



$$

Therefore, $A=\dfrac{1}{16}.$

### Example: Writing an Even Power of Sine as a Sum of Cosines of Multiple Angles

#### Question

Given the trigonometric identity

$$



\sin^4\theta=A\cos4\theta + B\cos2\theta+C



$$

where $A, B$ and $C$ are constants, find the value of $A.$

#### Explanation

Let $z = \cos\theta + \text{i}\sin\theta.$ We start with the following identities:

$$



\begin{aligned}(𝑧−\frac{1}{𝑧})=2isin⁡𝜃\,(𝑧^{𝑛}+\frac{1}{𝑧^{𝑛}})=2cos⁡𝑛𝜃\end{aligned}



$$

Raising both sides to the power $4$ in the first identity, we get

$$



\left(z - \frac{1}{z}\right)^4 = (2\text{i}\sin\theta)^4 \%=16\text{i}^4\sin^4\theta =16\sin^4\theta .



$$

Now, we expand the binomial using the binomial theorem and simplify the result using our identities, as follows:

$$



\begin{aligned}(𝑧−\frac{1}{𝑧})^{4} & =𝑧^{4}−4𝑧^{3}(\frac{1}{𝑧})+6𝑧^{2}(\frac{1}{𝑧})^{2}−4𝑧(\frac{1}{𝑧})^{3}+(\frac{1}{𝑧})^{4} \\ & =𝑧^{4}−4𝑧^{2}+6−\frac{4}{𝑧^{2}}+\frac{1}{𝑧^{4}} \\ & =\underset{2cos⁡4𝜃}{\underset{}{(𝑧^{4}+\frac{1}{𝑧^{4}})}}−4\underset{2cos⁡2𝜃}{\underset{}{(𝑧^{2}+\frac{1}{𝑧^{2}})}}+6 \\ & =2cos⁡4𝜃−4(2cos⁡2𝜃)+6 \\ & =2cos⁡4𝜃−8cos⁡2𝜃+6\end{aligned}



$$

By equating $16 \sin^4 \theta$ with the above, we get

$$



16\sin^4\theta = 2\cos4\theta - 8\cos2\theta+6.



$$

Finally, we divide both sides of the equation by $16,$ which gives

$$



\sin^4\theta = \frac{1}{8}\cos4\theta - \frac{1}{2}\cos2\theta+\frac{3}{8}.



$$

Therefore, $A=\dfrac{1}{8}.$

### Justification for the Power-Reducing Formulas

Now that we've had some practice using the power-reducing formulas, let's see where they come from.

First, let $z = \cos \theta + \text{i} \sin \theta.$ Using De Moivre's theorem, we have

$$



\begin{aligned}𝑧^{𝑛} & =(cos⁡𝜃+isin⁡𝜃)^{𝑛} \\ & =cos⁡(𝑛𝜃)+isin⁡(𝑛𝜃).\end{aligned}



$$

Now, let's simplify the expression for $\dfrac{1}{z^n},$ as follows:

$$



\begin{aligned}\frac{1}{𝑧^{𝑛}} & =\frac{1}{cos⁡(𝑛𝜃)+isin⁡(𝑛𝜃)} \\ & =\frac{1}{cos⁡(𝑛𝜃)+isin⁡(𝑛𝜃)}⋅\frac{cos⁡(𝑛𝜃)−isin⁡(𝑛𝜃)}{cos⁡(𝑛𝜃)−isin⁡(𝑛𝜃)} \\ & =\frac{cos⁡(𝑛𝜃)−isin⁡(𝑛𝜃)}{cos^{2}⁡(𝑛𝜃)+sin^{2}⁡(𝑛𝜃)} \\ & =\frac{cos⁡(𝑛𝜃)−isin⁡(𝑛𝜃)}{1} \\ & =cos⁡(𝑛𝜃)−isin⁡(𝑛𝜃)\end{aligned}



$$

Finally, we can write down the power-reducing formulas. The power-reducing formula for cosine is

$$



\begin{aligned}(𝑧^{𝑛}+\frac{1}{𝑧^{𝑛}}) & =\overset{[cos⁡(𝑛𝜃)+isin⁡(𝑛𝜃)]}{𝑧^{𝑛}}+\overset{[cos⁡(𝑛𝜃)−isin⁡(𝑛𝜃)]}{\frac{1}{𝑧^{𝑛}}} \\ & =2cos⁡(𝑛𝜃),\end{aligned}



$$

and the power-reducing formula for sine is

$$



\begin{aligned}(𝑧^{𝑛}−\frac{1}{𝑧^{𝑛}}) & =\overset{[cos⁡(𝑛𝜃)+isin⁡(𝑛𝜃)]}{𝑧^{𝑛}}−\overset{[cos⁡(𝑛𝜃)−isin⁡(𝑛𝜃)]}{\frac{1}{𝑧^{𝑛}}} \\ & =2isin⁡(𝑛𝜃).\end{aligned}



$$
