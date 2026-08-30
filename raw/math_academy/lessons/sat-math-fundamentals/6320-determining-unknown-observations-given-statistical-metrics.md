# Determining Unknown Observations Given Statistical Metrics

Source: https://www.mathacademy.com/topics/6320?courseId=120
Topic ID: 6320

## Prerequisites

- [Solving Linear Equations With Fractional Coefficients](../grade-7/67-solving-linear-equations-with-fractional-coefficients.md)
- [Inequalities](../grade-7/178-inequalities.md)
- [The Mode of a Data Set](../grade-6/3579-the-mode-of-a-data-set.md)
- [The Median of a Data Set](../grade-6/3749-the-median-of-a-data-set.md)
- [Rational Numbers as Finite or Repeating Decimals](../grade-7/7011-rational-numbers-as-finite-or-repeating-decimals.md)

## Lesson

### Introduction

In real-world situations, we often don’t have access to every data point in a dataset. Instead, we might be given a statistical summary, such as the mean, median, or mode.

In previous lessons, we saw how to calculate the mean, median, or mode of a dataset. In this topic, we'll learn how to *reverse the process*: given one of these statistics, we'll determine some missing data values.

For example, suppose the mean of the data set below is $5.5{:}$

$$


3.3, \: 6.1, \: 4.4, \: 7.0, \: 5.2, \: x


$$

How can we determine the value of the missing data point $x?$

First, we let $\overline{x}$ represent the mean of the data set.

Now, let's write down an expression for the mean. Recall that the mean of a data set equals the sum of the data points divided by the number of data points. Since there are six data points in total, we can express the mean $\overline{x}$ as follows:

$$


\begin{aligned}\overset{𝑥}{} & =\frac{1}{6}(3.3+6.1+4.4+7.0+5.2+𝑥)\end{aligned}


$$

Simplifying the expression in the parentheses by adding the numerical values gives

$$


\begin{aligned}\overset{𝑥}{} & =\frac{1}{6}(𝑥+26).\end{aligned}


$$

Now, we equate it to $5.5$ and solve for $x{:}$

$$


\begin{aligned}\overset{𝑥}{} & =5.5 \\ \frac{1}{6}(𝑥+26) & =5.5 \\ 6⋅\frac{1}{6}(𝑥+26) & =6⋅5.5 \\ 𝑥+26 & =33 \\ 𝑥 & =33−26 \\ 𝑥 & =7\end{aligned}


$$

By the end of the topic, we’ll learn how to handle not only means, but also more subtle cases involving medians and modes.

Let's see some more examples.

### Example: Determining an Unknown Observation Given a Mean

#### Question

Ivy and Jack each attempted the math test five times, and their scores are represented in the table above. The mean score for Jack’s attempts was $0.2$ greater than the mean score for Ivy’s attempts. What is the value of $x?$

#### Explanation

Let $I$ and $J$ represent the means of Ivy’s and Jack’s scores, respectively.

First, we compute Ivy’s mean:

$$


\begin{aligned}𝐼 & =\frac{1}{5}(3.6+3.8+4.0+3.9+4.2) \\ & =\frac{19.5}{5} \\ & =3.9\end{aligned}


$$

Since Jack’s mean is $0.2$ greater than Ivy’s mean, Jack’s mean is

$$


\begin{aligned}𝐽 & =𝐼+0.2 \\ & =3.9+0.2 \\ & =4.1.\end{aligned}


$$

Now, we write down the expression for Jack’s mean:

$$


\begin{aligned}𝐽 & =\frac{1}{5}(4.4+4.2+4.0+3.8+𝑥) \\ & =\frac{1}{5}(16.4+𝑥)\end{aligned}


$$

Finally, we equate it to $4.1$ and solve for $x{:}$

$$


\begin{aligned}𝐽 & =4.1 \\ \frac{1}{5}(𝑥+16.4) & =4.1 \\ 5⋅\frac{1}{5}(𝑥+16.4) & =5⋅4.1 \\ 𝑥+16.4 & =20.5 \\ 𝑥 & =20.5−16.4 \\ 𝑥 & =4.1\end{aligned}


$$

### Example: Determining Possible Values of an an Unknown Given a Median

#### Question

$$


x,\: 5,\: 10,\: 4,\: 7,\: 12,\: 4,\: 5


$$

In the data set above, $x$ is an integer. If the median of the data set is $6$ and $x < 9,$ what are all possible values of $x?$

#### Explanation

Notice that our data set contains $8$ values. So, the median is the average of the values in the

$$


\dfrac{8}{2}=4 \text{th position} \qquad\text{and}\qquad \dfrac{8}{2}+1=5 \text{th position}.


$$

First, we write down the data in ascending order, ignoring $x{:}$

$$


4,\; 4,\; 5,\; 5,\; 7,\; 10,\; 12


$$

With this in mind, let's consider all possibilities for the value of $x.$

- If $x \leq 4,$ then we have the following ordered data: The $4$th and $5$th values are $5$ and $5,$ so the median is $\dfrac{5+5}{2}=5,$ not $6.$ $\color{red}\times$

- If $x = 5,$ then we have the following ordered data: The $4$th and $5$th values are $5$ and $5,$ so the median is $\dfrac{5+5}{2}=5,$ not $6.$ $\color{red}\times$

- If $x = 6,$ then we have the following ordered data: The $4$th and $5$th values are $5$ and $6,$ so the median is $\dfrac{5+6}{2}=5.5,$ not $6.$ $\color{red}\times$

- If $x = 7,$ then we have the following ordered data: The $4$th and $5$th values are $5$ and $7,$ respectively. So, the median is $\dfrac{5+7}{2}=6.$ $\color{darkgreen}\checkmark$

- If $x = 8,$ then we have the following ordered data: The $4$th and $5$th values are still $5$ and $7,$ so the median is $\dfrac{5+7}{2}=6.$ $\color{darkgreen}\checkmark$

Therefore, the possible values of $x$ are $7$ and $8.$

### Determining an Unknown Observation Given a Dataset's Mode

Next, consider the following data set, where $x$ is an integer.

$$


12,\; 15,\; 14,\; x,\; 13,\; 15,\; 12


$$

Suppose we know that the only mode of the data set is $15.$ Let's use this information to determine all possible values of $x.$

Recall that the mode of a data set is the value that occurs the most often.

Now, notice that $12$ and $15$ each occur twice, while all other values occur less than twice.

So, $12$ and $15$ are candidates for the mode. Now, for $15$ to be the only mode, it must occur more often than $12,$ i.e., at least three times.

Therefore, $x$ must be equal to $15.$

Let's see another, similar example.

### Example: Determining Possible Values of an an Unknown Given Modes

#### Question

$$


2, \: 5,\; x, \: 7,\; 9,\; 5,\; 7


$$

The rainfall amounts (in millimeters) measured over a week are shown above. The data set has at least two modes. Determine all possible values of $x.$

#### Explanation

The mode is the value that occurs the most often in the data set.

Notice that $5$ and $7$ each occur twice, while all other values occur less than twice. So, $5$ and $7$ are candidates for the modes.

Now, $x$ can't be equal to $5$ or $7.$ Otherwise, one of these values would occur three times in the data set, meaning that it's the only mode.

But $x$ could be either $2$ or $9.$ If so, one of these values would also occur twice in the data set, meaning that we would have three modes.

Therefore, $x$ could be any integer other than $5$ or $7.$
