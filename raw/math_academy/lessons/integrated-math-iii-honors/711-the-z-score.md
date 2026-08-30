# The Z-Score

Source: https://www.mathacademy.com/topics/711?courseId=101
Topic ID: 711

## Prerequisites

- [Systems of Linear Equations With Fractional Coefficients](../algebra-i/1045-systems-of-linear-equations-with-fractional-coefficients.md)
- [Systems of Linear Equations With Decimal Coefficients](../algebra-i/1081-systems-of-linear-equations-with-decimal-coefficients.md)
- [Variance and Standard Deviation](../integrated-math-ii-honors/1632-variance-and-standard-deviation.md)

## Lesson

### Introduction

Suppose that a student takes a test and gets a score of $x=82.$ If we know that the mean score for the class is $\overline{x} = 75$ and the standard deviation is $\sigma = 3.5,$ then how good is the student's score?

To determine how good the student's score is, we can calculate the **$z$-score**, which is defined by

$$


z = \frac{x-\overline{x}}{\sigma}.


$$

The $z$-score represents how many standard deviations the observed score is above or below the mean of the data set.

- A large positive $z$-score means the student's score is high compared to the class's mean score.

- A $z$-score close to $0$ means the student's score is close to the class's mean score.

- A large negative $z$-score means the student's score is low compared to the class's mean score.

In this particular example, the student's $z$-score is

$$


z = \dfrac{82 - 75}{3.5} = 2.


$$

So, the student's score is $2$ standard deviations above the mean. This suggests that the student obtained a much higher score than the average score for the entire class.

### Example: Calculating the Z-Score of a Given Observation

#### Question

A data set has mean $\overline{x}=15$ and variance $\sigma^2=3.25$. Find the $z$-score of an observation $x=17.3,$ giving your answer to $2$ decimal places.

#### Explanation

The $z$-score of an observation $x$ is defined by

$$


z = \frac{x-\overline{x}}{\sigma}.


$$

The $z$-score represents how many standard deviations an observation is above or below the mean of the data set.

Here, we're told that the mean is $\overline{x}=15,$ and we can calculate the standard deviation as

$$


\sigma = \sqrt{\sigma^2} = \sqrt{3.25}.


$$

So, the $z$-score of the observation $x=17.3$ is given by

$$


\begin{aligned}𝑧 & =\frac{𝑥−\overset{𝑥}{}}{𝜎} \\ & ≈\frac{17.3−15}{\sqrt{√3.25}} \\ & ≈1.28\end{aligned}


$$

to $2$ decimal places.

### Finding an Observation Corresponding to a Given Z-Score

So far, we have practiced converting an observation $x$ into a $z$-score. Other times, though, we may be given a $z$-score and want to find the corresponding observation $x.$

To accomplish this, we can take the formula for the $z$-score and solve for $x\mathbin{:}$

$$


\begin{aligned}𝑧 & =\frac{𝑥−\overset{𝑥}{}}{𝜎} \\ 𝑧⋅𝜎 & =𝑥−\overset{𝑥}{} \\ 𝑥 & =\overset{𝑥}{}+𝑧⋅𝜎\end{aligned}


$$

For example, suppose that a data set has a mean of $\overline{x}=15$ and a standard deviation of $\sigma = 1.5.$ If we're given a $z$-score of $z=2,$ then we can find the corresponding observation $x$ as follows:

$$


\begin{aligned}𝑥 & =\overset{𝑥}{}+𝑧⋅𝜎 \\ & =15+2⋅1.5 \\ & =15+3 \\ & =18\end{aligned}


$$

### Example: Finding the Value of an Observation, Standard Deviation, or Mean Given a Z-Score

#### Question

A data set has a standard deviation $\sigma=1.2$ and an unknown mean. An observation of the data set has the value $x=13.2$ and $z$-score $z=-1.5.$ Find the mean of the data set.

#### Explanation

To compute the value of an observation $x$ which yields a given $z$-score in a data set with mean $\overline{x}$ and standard deviation $\sigma,$ we can use the following formula:

$$


x = \overline{x} + z \cdot \sigma


$$

Substituting $x=13.2,$ $z=-1.5,$ and $\sigma=1.2$ into the formula and solving for $\overline{x}$, we get

$$


\begin{aligned}𝑥 & =\overset{𝑥}{}+𝑧⋅𝜎 \\ 13.2 & =\overset{𝑥}{}+(−1.5)⋅1.2 \\ 13.2 & =\overset{𝑥}{}−1.8 \\ \overset{𝑥}{} & =13.2+1.8 \\ \overset{𝑥}{} & =15\end{aligned}


$$

### Example: Solving a System of Equations to Compute an Unknown Mean or Standard Deviation

#### Question

A data set contains the observations $x_1=18, x_2=12$ with $z$-scores $z_1=2.8$ and $z_2=1.6,$ respectively. Find the mean of the data set.

#### Explanation

To compute the value of an observation $x$ which yields a given $z$-score in a data set with mean $\overline{x}$ and standard deviation $\sigma,$ we can use the following formula:

$$


x = \overline{x} + z \cdot \sigma


$$

From the first observation, we have

$$


\begin{aligned}18 & =\overset{𝑥}{¯}+2.8⋅𝜎.\end{aligned}


$$

From the second observation, we have

$$


\begin{aligned}12 & =\overset{𝑥}{¯}+1.6⋅𝜎.\end{aligned}


$$

Subtracting the second equation from the first and solving for $\sigma,$ we get

$$


\begin{aligned}(18−12) & =(\overset{𝑥}{¯}−\overset{𝑥}{¯})+(2.8−1.6)⋅𝜎 \\ 6 & =1.2⋅𝜎 \\ 𝜎 & =5.\end{aligned}


$$

Finally, substituting this value back into our first equation and solving for $\bar{x},$ we get

$$


\begin{aligned}18 & =\overset{𝑥}{¯}+2.8⋅𝜎 \\ 18 & =\overset{𝑥}{¯}+2.8⋅5 \\ \overset{𝑥}{¯} & =4.\end{aligned}


$$

### Example: Z-Score: Word Problems

#### Question

The mean height of a group of basketball players is $178\textrm{cm}$. A player in this group is $184\textrm{cm}$ tall and his $z$-score is $z = 1.5$. Find the standard deviation of the basketball players' heights.

#### Explanation

To compute the value of an observation $x$ which yields a given $z$-score in a data set with mean $\overline{x}$ and standard deviation $\sigma,$ we can use the following formula:

$$


x = \overline{x} + z \cdot \sigma


$$

Substituting $x=184,$ $\overline{x}=178,$ and $z=1.5$ into the formula and solving for $\sigma,$ we get

$$


\begin{aligned}𝑥 & =\overset{𝑥}{}+𝑧⋅𝜎 \\ 184 & =178+1.5⋅𝜎 \\ 6 & =1.5⋅𝜎 \\ 𝜎 & =\frac{6}{1.5} \\ 𝜎 & =4.\end{aligned}


$$

Therefore, the standard deviation of the players heights is $4\,\textrm{cm}.$
