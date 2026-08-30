# Type I and Type II Errors

Source: https://www.mathacademy.com/topics/3012?courseId=73
Topic ID: 3012

## Prerequisites

- [Two-Tailed Hypothesis Tests](./4120-two-tailed-hypothesis-tests.md)

## Lesson

### Introduction

In statistical hypothesis testing, we have two types of error that can occur:

- A **type I error** occurs if we reject the null hypothesis even though it's true. Type I errors are also known as **false-positives.**

- A **type II error** occurs if we do not reject the null hypothesis even though it's false. Type II errors are also known as **false-negatives.**

We summarise the possible situations in the following table:

Suppose, for example, we have the following null and alternative hypotheses regarding a population mean $\mu$:

$$


H_0: \mu =2.5, \qquad H_1: \mu \neq 2.5


$$

In this case,

- a type I error would occur if we reject $H_0$ when $\mu=2.5$, while

- a type II error would occur if we do not reject $H_0$ when $\mu\neq 2.5.$

### Example: Identifying Type I Errors

#### Question

Given the following null and alternative hypotheses, which of the following would be type I errors?

$$


H_0: \mu =3.5, \quad H_1: \mu < 3.5


$$

1. Do not reject $H_0$ when $\mu < 3.5$

2. Do not reject $H_0$ when $\mu = 3.5$

3. Reject $H_0$ when $\mu =3.5$

#### Explanation

A type I error occurs when we reject the null hypothesis $H_0$ even though it is true.

With that in mind, let's go through each case in turn:

- Case I is not a type I error. Here, we do not reject the null hypothesis $H_0,$ but the null hypothesis is false since $\mu < 3.5.$ This is an example of a type II error.

- Case II is not an error. Here, we do not reject the null hypothesis $H_0,$ and the null hypothesis is true since $\mu=3.5.$ So, in this case, we reach the correct conclusion.

- Case III is a type I error. Here, we reject the null hypothesis $H_0,$ but the null hypothesis is true since $\mu=3.5.$

Therefore, the correct answer is "III only."

### Example: Type I Errors in Modeling Contexts

#### Question

An engineer wants to test whether a new solar panel is more effective than the older model. What would be an example of a type I error in this context? For the null hypothesis, you should assume that the new solar panel is as effective as the older one.

#### Explanation

A type I error occurs when we reject the null hypothesis $H_0$ even though it is true.

In this case, the null hypothesis is that the new solar panel is as effective as the older one.

So, a type I error would consist of the engineer concluding that the new solar panel is more effective when it is as effective as the older model.

### Example: Identifying Type II Errors

#### Question

Given the following null and alternative hypotheses, which of the following would be type II errors?

$$


H_0: \mu =100, \quad H_1: \mu < 100


$$

1. Do not reject $H_0$ when $\mu < 100$

2. Reject $H_0$ when $\mu <100$

3. Reject $H_0$ when $\mu =100$

#### Explanation

A type II error occurs when we do not reject the null hypothesis $H_0$ even though it is false.

With that in mind, let's go through each case in turn:

- Case I is a type II error. Here, we do not reject the null hypothesis $H_0,$ but the null hypothesis is false since $\mu < 100.$

- Case II is not an error. Here, we reject the null hypothesis $H_0,$ and the null hypothesis is false since $\mu < 100.$ So, in this case, we reach the correct conclusion.

- Case III is not a type II error. Here, we reject the null hypothesis $H_0,$ but the null hypothesis is true since $\mu=100.$ This is an example of a type I error.

Therefore, the correct answer is "I only."

### Example: Type II Errors in Modeling Contexts

#### Question

An exam administrator wants to test whether students score higher under a new exam format than under the existing one. What would be an example of a type II error in this context? For the null hypothesis, you should assume that students score the same under the new format as the existing one.

#### Explanation

A type II error occurs when we do not reject the null hypothesis $H_0$ even though it is false.

In this case, the null hypothesis is that students score the same under both formats.

So, a type II error would consist of the administrator concluding that the students score the same under the new format when they, in fact, score higher.
