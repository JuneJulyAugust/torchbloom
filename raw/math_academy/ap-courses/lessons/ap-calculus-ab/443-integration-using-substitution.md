# Integration Using Substitution

Source: https://www.mathacademy.com/topics/443?courseId=24
Topic ID: 443

## Prerequisites

- [Integrating Linear Rational Functions Using Substitution](./331-integrating-linear-rational-functions-using-substitution.md)

## Lesson

### Introduction

How can we solve an integral like

$$


\int 2x(x^2+1)^3\,\textrm{d}x \,?


$$

Notice that if we let $u=x^2+1$, then the derivative is $u' = 2x,$ and both $u$ and $u'$ are present in the integrand:

$$


\int \underbrace{2x}_{u'}(\overbrace{x^2+1}^{u})^3\,\textrm{d}x


$$

Integrals like this can always be solved using substitution. So, let's proceed. If we let ${\color{red}{u=x^2+1}},$ then differentiating with respect to $x$ gives

$$


\dfrac{\textrm d u}{\textrm d x} = 2x\quad\Longrightarrow\quad\color{blue}\textrm{d}u=2x \, \textrm{d}x.


$$

We can now see that the change of variables from $x$ to $u$ is convenient because if we substitute, we get

$$


\int {\color{blue}{2x}}({\color{red}{x^2+1}})^3\,{\color{blue}{\textrm{d}x}} = \int \color{red}(x^2+1)^{\color{black}3}\, \color{blue}{2x\,\textrm{d}x} \color{black}= \int {\color{red}u}^{\color{black}3}\, {\color{blue}{\,\textrm{d}u}} .


$$

Now, we can solve the integral on the right since it's the integral of a power function:

$$


\begin{aligned}∫𝑢^{3}\,\,d𝑢 & =\frac{𝑢^{4}}{4}+𝐶.\end{aligned}


$$

For the last step, we change the variable back to $x$ by replacing $u=x^2+1.$ So the final result is

$$


\displaystyle\int 2x(x^2+1)^3\,\textrm{d}x =\dfrac{(x^2+1)^4}{4}+C.


$$

**Note:** After solving an integral using substitution, we should always double-check that our result is correct. If we differentiate the result, then it should come out to the original integrand:

$$


\begin{aligned}\frac{d}{d𝑥}[\frac{(𝑥^{2}+1)^{4}}{4}+𝐶] & =\frac{1}{4}⋅\frac{d}{d𝑥}[(𝑥^{2}+1)^{4}]+\frac{d}{d𝑥}(𝐶) \\ & =\frac{1}{4}⋅4(𝑥^{2}+1)^{3}⋅\frac{d}{d𝑥}(𝑥^{2}+1)+0 \\ & =(𝑥^{2}+1)^{3}⋅(2𝑥) \\ & =2𝑥(𝑥^{2}+1)^{3}\,✓\end{aligned}


$$

### Example: Integrating an Expression Involving a Power Function Multiplied by Its Derivative

#### Question

Calculate $\displaystyle\int 6x^2(2x^3+3)^6\,\textrm{d}x.$

#### Explanation

We note that $6x^2$ is the derivative of the quantity in the parentheses. So we make a substitution

$$


u=2x^3+3.


$$

Its derivative is given by

$$


\begin{aligned}\frac{d𝑢}{d𝑥} & =6𝑥^{2}\,⟹\,d𝑢=6𝑥^{2}\,d𝑥,\end{aligned}


$$

and rewriting our integral, we get

$$


\begin{aligned}∫6𝑥^{2}(2𝑥^{3}+3)^{6}\,d𝑥 & =∫(2𝑥^{3}+3)^{6}\,6𝑥^{2}\,d𝑥 \\ & =∫𝑢^{6}\,d𝑢.\end{aligned}


$$

We can now solve the integral using the power rule:

$$


\begin{aligned}∫𝑢^{6}\,d𝑢 & =\frac{𝑢^{7}}{7}+𝐶\end{aligned}


$$

Lastly, we substitute $u=2x^3+3$ back in the expression. So the final result is

$$


\displaystyle\int 6x^2(2x^3+3)^6\,\textrm{d}x =\dfrac{(2x^3+3)^7}{7}+C.


$$

### Example: Integrating an Expression Involving a Power Function Multiplied by a Constant Multiple of Its Derivative

#### Question

Calculate $\displaystyle\int x\left(1+2x^2\right)^6\,\textrm{d}x.$

#### Explanation

The $x$ that's outside the parentheses isn't quite the derivative of $(1+2x^2).$ The derivative of $(1+2x^2)$ is $4x,$ so we're out by a constant factor of $4$. However, since we're out only by a constant factor, substitution will still work!

So we make the substitution

$$


u=1+2x^2.


$$

Its derivative is given by

$$


\begin{aligned}\frac{d𝑢}{d𝑥} & =4𝑥\,⟹\,\frac{1}{4}d𝑢=𝑥\,d𝑥,\end{aligned}


$$

and we can now write our integral in terms of $u,$ as follows:

$$


\begin{aligned}∫𝑥(1+2𝑥^{2})^{6}\,d𝑥 & =∫(1+2𝑥^{2})^{6}⋅𝑥\,d𝑥 \\ & =∫𝑢^{6}⋅\frac{1}{4}d𝑢 \\ & =\frac{1}{4}∫𝑢^{6}d𝑢\end{aligned}


$$

Finally, we can solve the integral in terms of $u$ and then write the final result in terms of $x.$ We get

$$


\begin{aligned}\frac{1}{4}∫𝑢^{6}d𝑢 & =\frac{1}{4}⋅\frac{𝑢^{7}}{7}+𝐶 \\ & =\frac{1}{28}𝑢^{7}+𝐶 \\ & =\frac{1}{28}(1+2𝑥^{2})^{7}+𝐶.\end{aligned}


$$

### Integrating Rational Functions Using Substitution

How do we calculate $\displaystyle\int \dfrac{2x}{1+x^2}\,\textrm d x?$

In this case, the numerator is the derivative of the denominator! Again, integrals like this are always solvable by substitution. So, we let

$$


\color{red}u = x^2+1.


$$

Differentiating the above with respect to $x$ gives

$$


\dfrac{\textrm d u}{\textrm d x} = 2x\quad\Longrightarrow\quad {\color{blue}{\textrm d u = 2x \, \textrm d x}},


$$

and we can now rewrite the integral in terms of $u$ as

$$


\begin{aligned}∫\frac{2𝑥}{1+𝑥^{2}}\,d𝑥 & =∫\frac{1}{1+𝑥^{2}}⋅2𝑥\,d𝑥 \\ & =∫\frac{1}{𝑢}⋅\,d𝑢.\end{aligned}


$$

Finally, we can solve the integral in terms of $u$ and then write the final result in terms of $x.$ We get

$$


\begin{aligned}∫\frac{1}{𝑢}\,d𝑢 & =ln⁡|𝑢|+𝐶 \\ & =ln⁡|1+𝑥^{2}|+𝐶 \\ & =ln⁡(1+𝑥^{2})+𝐶.\end{aligned}


$$

Therefore, we conclude that

$$


\displaystyle\int \dfrac{2x}{1+x^2}\,\textrm{d}x = \ln(1+x^2)+C.


$$

Notice that we removed the absolute value bars because the function $1+x^2$ is always positive.

### Example: Integrating a Rational Function Using Natural Logarithms

#### Question

Calculate $\displaystyle \int \dfrac{x^2}{x^3+1}\,\textrm d x.$

#### Explanation

Let $u=x^3+1.$ Then

$$


\dfrac{\textrm d u}{\textrm d x} = 3x^2\quad\Longrightarrow\quad \dfrac 1 3 \textrm d u= x^2 \, \textrm d x,


$$

and we can solve the resulting integral as follows:

$$


\begin{aligned}∫\frac{𝑥^{2}}{𝑥^{3}+1}\,d𝑥 & =∫\frac{1}{𝑥^{3}+1}⋅𝑥^{2}\,d𝑥 \\ & =∫\frac{1}{𝑢}⋅\frac{1}{3}\,d𝑢 \\ & =\frac{1}{3}∫\frac{1}{𝑢}\,d𝑢 \\ & =\frac{1}{3}ln⁡|𝑢|+𝐶 \\ & =\frac{1}{3}ln⁡|𝑥^{3}+1|+𝐶\end{aligned}


$$

### Example: Integrating Other Fractional Expressions

#### Question

$\displaystyle \int \dfrac{x^2}{\sqrt{1-x^3}} \, \textrm{d}x=$

#### Explanation

Let $u = 1 - x^3.$ Then

$$


\dfrac{\textrm d u}{\textrm d x} = -3x^2 \quad \Longrightarrow\quad -\dfrac{1}{3} \textrm d u= x^2 \, \textrm d x,


$$

and we can solve the resulting integral as follows:

$$


\begin{aligned}∫\frac{𝑥^{2}}{\sqrt{√1−𝑥^{3}}}\,d𝑥 & =∫\frac{1}{\sqrt{√1−𝑥^{3}}}⋅𝑥^{2}\,d𝑥 \\ & =∫\frac{1}{\sqrt{√𝑢}}⋅(−\frac{1}{3})d𝑢 \\ & =−\frac{1}{3}∫\frac{1}{\sqrt{√𝑢}}\,d𝑢 \\ & =−\frac{1}{3}(2\sqrt{√𝑢})+𝐶 \\ & =−\frac{2}{3}\sqrt{√𝑢}+𝐶 \\ & =−\frac{2}{3}\sqrt{√1−𝑥^{3}}+𝐶\end{aligned}


$$
