# Introduction to Integration by Parts

Source: https://www.mathacademy.com/topics/317?courseId=136
Topic ID: 317

## Prerequisites

- [Integrating Trigonometric Functions Using Substitution](./478-integrating-trigonometric-functions-using-substitution.md)
- [Integrating Exponential Functions Using Substitution](./3770-integrating-exponential-functions-using-substitution.md)

## Lesson

### Introduction

In this lesson, we introduce a method of integration that can be used in cases where integration by substitution fails. The method is known as **integration by parts**. The so-called **by-parts formula** is

$$


\int u\dfrac{\textrm{d}v}{\textrm{d}x}\,\textrm{d}x= uv- \int v\dfrac{\textrm{d}u}{\textrm{d}x}\,\textrm{d}x


$$

or simply

$$


\int uv'\,\textrm{d}x= uv- \int vu'\,\textrm{d}x.


$$

This method is handy for integrating products of functions where one factor can be easily integrated, and the other factor can easily be differentiated.

Let's see how to apply it to evaluate the integral

$$


\int xe^{2x} \textrm{d}x\,.


$$

The idea is to call one of the factors $u,$ the other factor $v',$ and then apply the by-parts formula. We'll choose the following:

$$


\int \underbrace{\color{blue}x}_{\large\color{blue}u}\cdot \underbrace{\color{red}e^{2x}}_{\large\color{red}v'} \textrm{d}x


$$

Now, if ${\color{blue}u} = {\color{blue}x}$ then we differentiate to get ${\color{blue}u'} = {\color{blue}1}.$ And if ${\color{red}v'} = {\color{red}e^{2x}}$ then we integrate to get ${\color{red}v} = {\color{red}\dfrac{1}{2}e^{2x}}.$ Note that we don't bother with the constant of integration here.

We now have everything we need, so we can substitute into the "by-parts" formula, as follows:

$$


\begin{aligned}∫\underset{𝑢𝑣^{′}}{\underset{}{𝑥⋅𝑒^{2𝑥}}}\,d𝑥 & =\underset{𝑢𝑣}{\underset{}{𝑥⋅\frac{1}{2}𝑒^{2𝑥}}}−∫\underset{𝑣𝑢^{′}}{\underset{}{\frac{1}{2}𝑒^{2𝑥}⋅1}}\,d𝑥\end{aligned}


$$

Now, we compute the integral:

$$


\begin{aligned}∫𝑥𝑒^{2𝑥}\,d𝑥 & =\frac{1}{2}𝑥𝑒^{2𝑥}−\frac{1}{2}∫𝑒^{2𝑥}\,d𝑥 \\ & =\frac{1}{2}𝑥𝑒^{2𝑥}−\frac{1}{2}⋅\frac{1}{2}𝑒^{2𝑥}+𝐶 \\ & =\frac{1}{2}𝑥𝑒^{2𝑥}−\frac{1}{4}𝑒^{2𝑥}+𝐶 \\ & =\frac{1}{4}𝑒^{2𝑥}(2𝑥−1)+𝐶\end{aligned}


$$

And we're done! Notice that integration by parts allows us to take a complicated integral $\displaystyle \int xe^{2x}\,\textrm{d}x$ and replace it with the simpler $\displaystyle \int e^{2x}\,\textrm{d}x$ plus some additional terms.

### Example: Using Integration by Parts to Compute an Indefinite Integral Containing an Exponential Expression

#### Question

Calculate $\displaystyle \int xe^{7x} \textrm{d}x.$

#### Explanation

To solve this integral, we use the by-parts formula, given by

$$


\int uv' \, \textrm{d}x= uv - \int vu' \, \textrm{d}x.


$$

We need to express $\displaystyle \int xe^{7x} \textrm{d}x$ as $\displaystyle \int uv'\,\textrm{d}x.$ Therefore, we set

$$


\begin{aligned}𝑢=𝑥\, & ⟹\,𝑢^{′}=1 \\ 𝑣^{′}=𝑒^{7𝑥}\, & ⟹\,𝑣=\frac{1}{7}𝑒^{7𝑥}.\end{aligned}


$$

We substitute the above into the integration by parts formula, and we get the following:

$$


\begin{aligned}∫𝑢𝑣^{′}\,d𝑥 & =𝑢𝑣−∫𝑣𝑢^{′}\,d𝑥 \\ ∫𝑥⋅𝑒^{7𝑥}\,d𝑥 & =𝑥⋅\frac{1}{7}𝑒^{7𝑥}−∫\frac{1}{7}𝑒^{7𝑥}⋅1\,d𝑥\end{aligned}


$$

Finally, we calculate the integral:

$$


\begin{aligned}∫𝑥𝑒^{7𝑥}\,d𝑥 & =\frac{1}{7}𝑥𝑒^{7𝑥}−\frac{1}{7}∫𝑒^{7𝑥}\,d𝑥 \\ & =\frac{1}{7}𝑥𝑒^{7𝑥}−\frac{1}{7}(\frac{𝑒^{7𝑥}}{7})+𝐶 \\ & =\frac{1}{7}𝑥𝑒^{7𝑥}−\frac{1}{49}𝑒^{7𝑥}+𝐶\end{aligned}


$$

### Example: Using Integration by Parts to Compute an Indefinite Integral Containing a Trigonometric Expression

#### Question

Calculate $\displaystyle\int x \cos{2x}\,\textrm d x.$

#### Explanation

To solve this integral, we use the by-parts formula, given by

$$


\int uv'\,\textrm{d}x= uv- \int vu'\,\textrm{d}x.


$$

We need to express $\displaystyle \int x \cos{2x} \textrm{d}x$ as $\displaystyle \int uv'\,\textrm{d}x.$ Therefore, we set

$$


\begin{aligned}𝑢=𝑥\, & ⟹\,𝑢^{′}=1 \\ 𝑣^{′}=cos⁡2𝑥\, & ⟹\,𝑣=\frac{1}{2}sin⁡2𝑥.\end{aligned}


$$

We substitute the above into the integration by parts formula, and we get

$$


\begin{aligned}∫𝑢𝑣^{′}\,d𝑥 & =𝑢𝑣−∫𝑣𝑢^{′}\,d𝑥 \\ ∫𝑥cos⁡2𝑥\,d𝑥 & =𝑥⋅\frac{1}{2}sin⁡2𝑥−∫\frac{1}{2}sin⁡2𝑥⋅1\,d𝑥.\end{aligned}


$$

Finally, we calculate the integral, as follows:

$$


\begin{aligned}∫𝑥cos⁡2𝑥\,d𝑥 & =\frac{1}{2}𝑥sin⁡2𝑥−\frac{1}{2}∫sin⁡2𝑥\,d𝑥 \\ & =\frac{1}{2}𝑥sin⁡2𝑥−\frac{1}{2}(−\frac{1}{2}cos⁡2𝑥)+𝐶 \\ & =\frac{1}{2}𝑥sin⁡2𝑥+\frac{1}{4}cos⁡2𝑥+𝐶\end{aligned}


$$

### Example: Computing a Definite Integral Using Integration by Parts

#### Question

Evaluate $\displaystyle \int_0^{\pi/5} x\sin(5x) \, \textrm{d}x.$

#### Explanation

Let's use integration by parts. We set

$$


\begin{aligned}𝑢=𝑥\, & ⟹\,𝑢^{′}=1 \\ 𝑣^{′}=sin⁡(5𝑥) & ⟹\,𝑣=−\frac{1}{5}cos⁡(5𝑥).\end{aligned}


$$

Substituting the above into the integration by parts formula, we get

$$


\begin{aligned}∫𝑢𝑣^{′}\,d𝑥 & =𝑢𝑣−∫𝑣𝑢^{′}\,d𝑥 \\ ∫𝑥⋅sin⁡(5𝑥)\,d𝑥 & =−𝑥⋅\frac{1}{5}cos⁡(5𝑥)−∫(−\frac{1}{5}cos⁡(5𝑥))⋅1\,d𝑥.\end{aligned}


$$

Finally, we evaluate the integral and get

$$


\begin{aligned}∫_{𝜋/50}^{}𝑥sin⁡(5𝑥)\,d𝑥 & =−\frac{1}{5}𝑥cos⁡(5𝑥)_{𝜋/50}^{}+\frac{1}{5}∫_{𝜋/50}^{}cos⁡(5𝑥)\,d𝑥 \\ & =−\frac{1}{5}𝑥cos⁡(5𝑥)_{𝜋/50}^{}+\frac{1}{5}(\frac{sin⁡(5𝑥)}{5})_{𝜋/50}^{} \\ & =[−\frac{1}{5}⋅\frac{𝜋}{5}cos⁡(𝜋)+\frac{1}{5}⋅0⋅cos⁡(0)]+[\frac{1}{25}sin⁡(𝜋)−\frac{1}{25}sin⁡(0)] \\ & =[−\frac{𝜋}{25}⋅(−1)+0]+[0−0] \\ & =\frac{𝜋}{25}.\end{aligned}


$$

### Deriving the By Parts Formula From the Product Rule

If you thought the by-parts formula looked similar to the product rule for differentiation, then you'd be right. In fact, that's precisely where it comes from!

To work out the formula, we recall the product rule for differentiation,

$$


\dfrac{\textrm{d}}{\textrm{d}x}(uv)=u\dfrac{\textrm{d}v}{\textrm{d}x}+ v\dfrac{\textrm{d}u}{\textrm{d}x},


$$

where $u$ and $v$ are functions of $x.$

If we rearrange this formula a bit, we get

$$


u\dfrac{\textrm{d}v}{\textrm{d}x}=\dfrac{\textrm{d}}{\textrm{d}x}(uv)- v\dfrac{\textrm{d}u}{\textrm{d}x}.


$$

Let's now integrate both sides of the equation:

$$


\int u\dfrac{\textrm{d}v}{\textrm{d}x}\,\textrm{d}x=\int\dfrac{\textrm{d}}{\textrm{d}x}(uv)\,\textrm{d}x- \int v\dfrac{\textrm{d}u}{\textrm{d}x}\,\textrm{d}x


$$

Using the fundamental theorem of calculus, we can use the fact that $\displaystyle\int\dfrac{\textrm{d}}{\textrm{d}x}(uv)\,\textrm{d}x=uv,$ and we arrive at the by-parts formula:

$$


\int u\dfrac{\textrm{d}v}{\textrm{d}x}\,\textrm{d}x= uv- \int v\dfrac{\textrm{d}u}{\textrm{d}x}\,\textrm{d}x


$$

### Final Remark

Let's go back to our first example,

$$


\int xe^{2x} \textrm{d}x\,.


$$

Note that when we selected our $u$ and $v',$ we could have picked them the other way around. So instead, we could have said

$$


\begin{aligned}𝑢=𝑒^{2𝑥}\, & ⟹\,𝑢^{′}=2𝑒^{2𝑥} \\ 𝑣^{′}=𝑥\, & ⟹\,𝑣=\frac{1}{2}𝑥^{2}.\end{aligned}


$$

Applying the by-parts formula using this selection, we get

$$


\begin{aligned}∫𝑥𝑒^{2𝑥}d𝑥 & =\frac{1}{2}𝑥^{2}𝑒^{2𝑥}−∫𝑥^{2}𝑒^{2𝑥}\,d𝑥.\end{aligned}


$$

Now, while the above is a mathematically correct statement, the integral on the right-hand side is *more* complicated than the integral we started with. Ouch!

Therefore, it's crucial that we select our $u$ and $v'$ in such a way that the problem is simplified, not made more complicated.
