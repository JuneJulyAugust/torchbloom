# Evaluating Special Limits Involving Sine Using a Substitution

Source: https://www.mathacademy.com/topics/3678?courseId=105
Topic ID: 3678

## Prerequisites

- [Special Limits Involving Sine](./606-special-limits-involving-sine.md)

## Lesson

### Introduction

Recall the following special limit for sine:

$$


\lim\limits_{\theta \to 0}\: \dfrac{\sin \theta}{\theta} = 1


$$

We can use this special limit to evaluate other limits, such as

$$


\lim\limits_{x \to 0}\: \dfrac{\sin 2x}{x}.


$$

For this limit, notice that as $x\to0,$ both the numerator and denominator approach $0.$ So, if we attempt to evaluate the limit directly, we get $\%\lim\limits_{x \to 0} \: \dfrac{\sin 2x}{x} = \dfrac00,$ which is an indeterminate form.

Instead, we rewrite the limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑥→0}{lim}\,\frac{sin⁡2𝑥}{𝑥} & =\underset{𝑥→0}{lim}(2⋅\frac{sin⁡2𝑥}{2𝑥}) \\ & =2⋅\underset{𝑥→0}{lim}\,\frac{sin⁡2𝑥}{2𝑥}\end{aligned}


$$

Now, this limit looks very similar to our special limit for sine. So, if we make the substitution $\theta = 2x,$ then, since $\theta \to 0$ as $x \to 0,$ we have

$$


\lim\limits_{x \to 0} \: \dfrac{\sin {\color{blue}2x}}{\color{blue}2x} = \lim\limits_{\theta \to 0} \: \dfrac{\sin {\color{blue}\theta}}{\color{blue}\theta} = 1.


$$

Therefore,

$$


\begin{aligned}\underset{𝑥→0}{lim}\,\frac{sin⁡2𝑥}{𝑥} & =2⋅\underset{𝑥→0}{lim}\,\frac{sin⁡2𝑥}{2𝑥} \\ & =2⋅1 \\ & =2.\end{aligned}


$$

### Example: Using the Special Limit With Sine and Substitution to Evaluate a Limit

#### Question

Find $\lim\limits_{x \to 5} \:\dfrac{\sin (x-5)}{15-3x}.$

#### Explanation

Notice that as $x \to 5,$ both numerator and denominator approach $0.$

So, if we attempt to evaluate the limit directly, we get

$$


\lim_{x \to5} \:\dfrac{\sin(x-5)}{15-3x} = \dfrac00,


$$

which is an indeterminate form.

Instead, let's recall the following special limit:

$$


\lim_{\theta \to 0} \: \dfrac{\sin\theta}{\theta} = 1


$$

We rewrite the given limit using the algebra of limits, as follows:

$$


\begin{aligned}\underset{𝑥→5}{lim}\,\frac{sin⁡(𝑥−5)}{15−3𝑥} & =\underset{𝑥→5}{lim}\,\frac{sin⁡(𝑥−5)}{(−3)(𝑥−5)} \\ & =−\frac{1}{3}⋅\underset{𝑥→5}{lim}\,\frac{sin⁡(𝑥−5)}{𝑥−5}\end{aligned}


$$

Let $\theta =x-5.$ Then, $\theta \to 0$ as $x \to 5,$ we have

$$


\lim\limits_{x \to 5} \:\dfrac{\sin({\color{blue}x-5})}{\color{blue}x-5} = \lim\limits_{\theta \to 0} \:\dfrac{\sin{\color{blue}\theta}}{\color{blue}\theta} =1.


$$

Therefore,

$$


\begin{aligned}−\frac{1}{3}⋅\underset{𝑥→5}{lim}\,\frac{sin⁡(𝑥−5)}{𝑥−5} & =−\frac{1}{3}⋅1 \\ & =−\frac{1}{3}.\end{aligned}


$$

### Example: Using the Special Limit With Sine and Substitution to Evaluate a Limit: Advanced Cases

#### Question

Calculate $\lim\limits_{\theta \to 0} \:\dfrac{\tan 2\theta}{\theta}.$

#### Explanation

First, we can simplify the limit using trigonometric identities, as follows:

$$


\begin{aligned}\underset{𝜃→0}{lim}\frac{tan⁡2𝜃}{𝜃} & =\underset{𝜃→0}{lim}\frac{(\frac{sin⁡2𝜃}{cos⁡2𝜃})}{cos⁡2𝜃} \\ & =\underset{𝜃→0}{lim}(\frac{sin⁡2𝜃}{𝜃}⋅\frac{1}{cos⁡2𝜃}) \\ & =\underset{𝜃→0}{lim}\,\frac{sin⁡2𝜃}{𝜃}⋅\underset{𝜃→0}{lim}\,\frac{1}{cos⁡2𝜃}\end{aligned}


$$

Let's now evaluate the limits separately:

- Consider the first limit. Notice that as $\theta \to 0,$ both numerator and denominator approach $0.$ So, if we attempt to evaluate the limit directly, we get which is an indeterminate form. Instead, let's recall the following special limit: We rewrite the given limit using the algebra of limits, as follows: Let $x = 2\theta.$ Then, since $x\to0$ as $\theta \to 0,$ we have

- Consider the second limit. Evaluating it directly, we get

Therefore, we have

$$


\begin{aligned}\underset{𝜃→0}{lim}\,\frac{sin⁡2𝜃}{𝜃}⋅\underset{𝜃→0}{lim}\,\frac{1}{cos⁡2𝜃}=2⋅1=2.\end{aligned}


$$
