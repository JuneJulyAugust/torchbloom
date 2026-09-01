# Finding Improper Integrals Using a Graphing Calculator

Source: https://www.mathacademy.com/topics/4084?courseId=21
Topic ID: 4084

## Prerequisites

- [Improper Integrals Over the Real Line](./1382-improper-integrals-over-the-real-line.md)
- [Finding Definite Integrals Using a Graphing Calculator](../ap-calculus-ab/4080-finding-definite-integrals-using-a-graphing-calculator.md)

## Lesson

### Introduction

We've seen how to approximate definite integrals using a graphing calculator. In this lesson, we'll apply the techniques we've learned to approximate improper integrals.

Suppose we wish to evaluate the following improper integral to three decimal places:

$$


\int_1^\infty \dfrac{\sqrt{\ln{x}}}{x^4}\,\textrm d x


$$

Your graphing calculator is unlikely to include an $\infty$ button, so we cannot directly enter this improper integral into our graphing calculator.

However, recall that, by definition

$$


\int_1^\infty \dfrac{\sqrt{\ln{x}}}{x^4}\,\textrm d x = \lim\limits_{a\to\infty} \int_1^a \dfrac{\sqrt{\ln{x}}}{x^4}\,\textrm d x.


$$

So instead, let's consider the definite integral

$$


\int_1^a \dfrac{\sqrt{\ln{x}}}{x^4}\,\textrm d x.


$$

We now use our graphing calculator to approximate the above integral for increasing values of $a{:}$

- Setting $a=9,$ we have rounded to $3$ decimal places.

- Setting $a=99,$ we have rounded to $3$ decimal places.

- Setting $a=999,$ we have rounded to $3$ decimal places.

Since the integrals with upper limits $99$ and $999$ both give $0.171$ to $3$ decimal places, we conclude that

$$


\int_1^\infty \dfrac{\sqrt{\ln{x}}}{x^4}\,\textrm d x \approx 0.171


$$

rounded to $3$ decimal places.

### Some Important Notes

Before we look at another example, you should note the following important points:

- In the previous example, you may wonder why we didn't approximate our improper integral by picking a very large value for $a$ right off the bat, e.g., If we were to try this, one of two things might happen: The first is that the calculator might report an error. This is likely due to a lack of physical memory available. The second is that the calculator might give an incorrect answer! Evaluating the above on a TI-84 Plus CE-T gives which is *incorrect!* Again, this incorrect answer is likely due to physical limitations that apply to all calculators. The critical takeaway is that the only safe way to approximate improper integrals is by using the method described earlier.

- In the last example, we increased the upper limit by appending an extra digit $9$ each time. If your calculator reports errors before you've reached a definite answer, consider increasing the upper limit more slowly. For example,

- Also, bear in mind that some integrals will converge faster than others. Integrals that converge slowly may require us to pick large values for $a$ before we can be sure of our final answer.

- Finally, throughout this lesson, you may assume that all improper integrals we'll encounter are convergent and that all of the functions we'll integrate decay to zero "rapidly enough" for this method to be suitable.

### Example: Approximating an Improper Integral With an Unbounded Upper Limit

#### Question

Approximate $\displaystyle \int_{1}^{\infty} \sqrt{2x}e^{-x^2} \, \text{d}x$ to three decimal places.

#### Explanation

We bring up the integral option on most calculators in one of the following ways:

- Press the $\boxed{\color{gray}\,2\text{nd}\,}$ (or $\boxed{\color{gray}\,\text{shift}\,}$) button, then the $\boxed{\displaystyle\color{gray}\,\int_{\boxed{\,\phantom{0}}}^{\boxed{\,\phantom{0}}} \boxed{\,\phantom{\big|0\big|}}\,}$ button.

- Press the $\boxed{\color{gray}\,\text{math}\,}$ (or $\boxed{\color{gray}\,\text{calc}\,}$) button and choose the integral option. Note that this might be called $\boxed{\color{gray}\,\text{fnInt}\,}$ or similar.

To calculate our improper integral, we insert ** numbers in place of $\infty$ until successive approximations are the same, as follows:

- Evaluating the integral with upper limit $9$ using a calculator, we get rounded to $3$ decimal places.

- Evaluating the integral with upper limit $99$ using a calculator, we obtain rounded to $3$ decimal places.

We can stop now since the last two approximations were $0.225$ to $3$ decimal places. Therefore,

$$


\int_{1}^{\infty} \sqrt{2x}e^{-x^2} \, \text{d}x \approx 0.225,


$$

rounded to $3$ decimal places.

### Unbounded Lower Limits

Suppose we have an improper integral with an unbounded lower limit, e.g.,

$$


\int_{-\infty}^{-1} \dfrac{e^{-x^2}}{x^2}.


$$

To approximate this integral, let's write

$$


\int_{a}^{-1} \dfrac{e^{-x^2}}{x^2}.


$$

Now, we use our graphing calculator to approximate the above integral for *decreasing* values of $a{:}$

- Setting $a=-9,$ we have rounded to $3$ decimal places.

- Setting $a=-99,$ we have rounded to $3$ decimal places.

Since the integrals with upper limits $9$ and $99$ both give $0.089$ to $3$ decimal places, we conclude that

$$


\int_{-\infty}^{-1} \dfrac{e^{-x^2}}{x^2} \approx 0.089


$$

rounded to $3$ decimal places.

### Example: Approximating an Improper Integral With an Unbounded Lower Limit

#### Question

Approximate $\displaystyle \int_{-\infty}^{0} \dfrac{|x|^3}{2^{-x} + x} \, \text{d}x$ to $2$ decimal places.

#### Explanation

We bring up the integral option on most calculators in one of the following ways:

- Press the $\boxed{\color{gray}\,2\text{nd}\,}$ (or $\boxed{\color{gray}\,\text{shift}\,}$) button, then the $\boxed{\displaystyle\color{gray}\,\int_{\boxed{\,\phantom{0}}}^{\boxed{\,\phantom{0}}} \boxed{\,\phantom{\big|0\big|}}\,}$ button.

- Press the $\boxed{\color{gray}\,\text{math}\,}$ (or $\boxed{\color{gray}\,\text{calc}\,}$) button and choose the integral option. Note that this might be called $\boxed{\color{gray}\,\text{fnInt}\,}$ or similar.

- To access the absolute value function, you can locate this function on your calculator (on some models, you can access this by typing $\boxed{\color{gray}\,\text{math}\,}$ and then selecting $\boxed{\color{gray}\,\text{abs}\,}$ under the $\boxed{\color{gray}\,\text{num}\,}$ submenu). Or, you can recall that $|x| = \sqrt{x^2}$ and rewrite the integral as

To calculate our improper integral, we insert ** numbers in place of $-\infty$ until successive approximations are the same, as follows:

- Evaluating the integral with lower limit $-10$ using a calculator, we have rounded to $3$ decimal places.

- Evaluating the integral with lower limit $-100$ using a calculator, we get rounded to $3$ decimal places.

- Evaluating the integral with lower limit $-200$ using a calculator, we obtain rounded to $3$ decimal places.

We can stop now since the last two approximations were $33.18$ to $2$ decimal places. Therefore,

$$


\int_{-\infty}^{0} \dfrac{|x|^3}{2^{-x} + x} \, \text{d}x \approx 33.18,


$$

rounded to $2$ decimal places.

### Improper Integrals Over the Real Line

Suppose we wish to evaluate the following improper integral to three decimal places:

$$


\displaystyle \int_{-\infty}^{\infty} e^{-x^2}\, \text{d}x\,.


$$

In this case, both the lower *and* upper limits of integration are unbounded.

To approximate our improper integral, we insert decreasingly small numbers in place of $-\infty$ and increasingly large numbers in place of $\infty$ until successive approximations are the same, as follows:

- Evaluating the integral with lower limit $-9$ and upper limit $9$ using a calculator, we have rounded to $3$ decimal places.

- Evaluating the integral with lower limit $-99$ and upper limit $99$ using a calculator, we have rounded to $3$ decimal places.

We can stop now since the last two approximations were $1.772$ to $3$ decimal places. Therefore,

$$


\int_{-\infty}^{\infty} e^{-x^2}\, \text{d}x \approx 1.772,


$$

rounded to $3$ decimal places.

### Example: Approximating an Improper Integral Over the Real Line

#### Question

Use a calculator to approximate $\displaystyle \int_{-\infty}^{\infty} \dfrac{\ln(x^2+1)}{x^4 + 2} \, \text{d}x$ rounded to $2$ decimal places.

#### Explanation

We bring up the integral option on most calculators in one of the following ways:

- Press the $\boxed{\color{gray}\,2\text{nd}\,}$ (or $\boxed{\color{gray}\,\text{shift}\,}$) button, then the $\boxed{\displaystyle\color{gray}\,\int_{\boxed{\,\phantom{0}}}^{\boxed{\,\phantom{0}}} \boxed{\,\phantom{\big|0\big|}}\,}$ button.

- Press the $\boxed{\color{gray}\,\text{math}\,}$ (or $\boxed{\color{gray}\,\text{calc}\,}$) button and choose the integral option. Note that this might be called $\boxed{\color{gray}\,\text{fnInt}\,}$ or similar.

To calculate our improper integral, we insert decreasingly small numbers in place of $-\infty$ and increasingly large numbers in place of $\infty$ until successive approximations are the same, as follows:

- Evaluating the integral with lower limit $-9$ and upper limit $9$ using a calculator, we get rounded to $2$ decimal places.

- Evaluating the integral with lower limit $-99$ and upper limit $99$ using a calculator, we obtain rounded to $2$ decimal places.

We can stop now since the last two approximations were $0.73,$ to $2$ decimal places.

Therefore,

$$


\int_{-\infty}^{\infty} \dfrac{\ln(x^2+1)}{x^4 + 2} \, \text{d}x \approx 0.73,


$$

rounded to $2$ decimal places.
