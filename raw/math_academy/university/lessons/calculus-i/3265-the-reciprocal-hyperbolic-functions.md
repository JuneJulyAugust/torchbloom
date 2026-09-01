# The Reciprocal Hyperbolic Functions

Source: https://www.mathacademy.com/topics/3265?courseId=105
Topic ID: 3265

## Prerequisites

- [The Hyperbolic Functions](./967-the-hyperbolic-functions.md)

## Lesson

### Introduction

We can define the **reciprocal hyperbolic functions** similarly to how we define reciprocal trigonometric functions.

The **hyperbolic cosecant function** (pronounced "cosetch") is defined as The graph of is shown below.

![Instructional graphic](../../../lesson-assets/calculus-i/topic-3265/28fe98ece625b658.png)

Note the following properties of

- Its domain is

- Its range is

- It has a vertical asymptote

- It has a horizontal asymptote

- It is an odd function.

### Example: Evaluating Hyperbolic Cosecant

#### Question

$$

Evaluate $\operatorname{csch} (-9).$

#### Explanation

$$

The definition of $\operatorname{csch} x$ is

$$


\operatorname{csch} x = \dfrac{1}{\sinh x} = \dfrac {2}{e^{x} - e^{-x}}.


$$

Therefore,

$$


\operatorname{csch} (-9) =\dfrac{2}{e^{-9}-e^{-(-9)}}=\dfrac{2}{e^{-9}-e^{9}}.


$$

### Hyperbolic Secant

The **hyperbolic secant function** (pronounced "sesh") is defined as The graph of is shown below.

![Instructional graphic](../../../lesson-assets/calculus-i/topic-3265/a8daebeaefb60a4e.png)

Note the following properties of

- Its domain is

- Its range is

- It has a horizontal asymptote

- It is an even function.

### Example: Evaluating Hyperbolic Secant

#### Question

$$

Evaluate $\operatorname{sech} \left(-t \right).$

#### Explanation

$$

The definition of $\operatorname{sech}{x}$ is

$$


\operatorname{sech}{x} = \dfrac{1}{\cosh x} = \dfrac{2}{e^{x}+e^{-x}}.


$$

Therefore,

$$


\begin{aligned}sech⁡(−𝑡) & =\frac{2}{𝑒^{−𝑡}+𝑒^{−(−𝑡)}} \\ & =\frac{2}{𝑒^{−𝑡}+𝑒^{𝑡}}.\end{aligned}


$$

### Hyperbolic Cotangent

The **hyperbolic cotangent function** (pronounced "coth") is defined as The graph of is shown below.

![Instructional graphic](../../../lesson-assets/calculus-i/topic-3265/99fa94048bbc81ac.png)

Note the following properties of

- Its domain is

- Its range is

- It has a vertical asymptote

- It has horizontal asymptotes

- It is an odd function.

Using the alternative definitions of we can write down two more definitions for

### Example: Evaluating Hyperbolic Cotangent

#### Question

$$

Evaluate $\coth (-\ln 3).$

#### Explanation

$$

The definition of $\coth x$ is

$$


\begin{aligned}coth⁡𝑥 & =\frac{1}{tanh⁡𝑥} \\ & =\frac{𝑒^{𝑥}+𝑒^{−𝑥}}{𝑒^{𝑥}−𝑒^{−𝑥}} \\ & =\frac{𝑒^{2𝑥}+1}{𝑒^{2𝑥}−1} \\ & =\frac{1+𝑒^{−2𝑥}}{1−𝑒^{−2𝑥}}.\end{aligned}


$$

Using the fourth definition, we get

$$


\begin{aligned}coth⁡(−ln⁡3) & =\frac{1+𝑒^{−2(−ln⁡3)}}{1−𝑒^{−2(−ln⁡3)}} \\ & =\frac{1+𝑒^{2ln⁡3}}{1−𝑒^{2ln⁡3}} \\ & =\frac{1+𝑒^{ln⁡3^{2}}}{1−𝑒^{ln⁡3^{2}}} \\ & =\frac{1+3^{2}}{1−3^{2}} \\ & =\frac{1+9}{1−9} \\ & =\frac{10}{(−8)} \\ & =−\frac{5}{4}.\end{aligned}


$$
