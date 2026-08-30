# The Sample Covariance Matrix

Source: https://www.mathacademy.com/topics/3138?courseId=145
Topic ID: 3138

## Prerequisites

- [The Transpose of a Matrix](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/232-the-transpose-of-a-matrix.md)
- [Multiplying Matrices](../../../high-school/integrated-math-honors/lessons/integrated-math-iii-honors/1196-multiplying-matrices.md)
- [The Sample Variance](./3820-the-sample-variance.md)
- [Sums of Squares](../../../high-school/integrated-math-honors/lessons/integrated-math-ii-honors/5204-sums-of-squares.md)

## Lesson

### Introduction

The table below describes the number of classes taken per semester and the average final grade in a sample of four college students.

We can collect this data in a matrix so that each column reports the number of courses and the average grade of a single student:

$$


[\begin{aligned}4 & 3 & 5 & 4 \\ 80 & 85 & 75 & 72\end{aligned}]


$$

The matrix $X$ is called the **observation matrix.**

Suppose we want to determine the mean number of courses and the mean average grade of this sample. The **sample mean vector,** denoted $\mathbf m,$ is a vector containing these values. The sample mean vector is given by

$$


\mathbf{m} = \dfrac{1}{n} \sum_{i=1}^n \mathbf{x}_i,


$$

where $\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_n$ are the individual observations (columns of $X$).

From our matrix above, we have that

$$


[\begin{aligned}4 \\ 80\end{aligned}]


$$

Therefore, the sample mean vector is

$$


\begin{aligned}𝐦 & =\frac{1}{4}(𝐱_{1}+𝐱_{2}+𝐱_{3}+𝐱_{4}) \\ & =\frac{1}{4}([\begin{aligned}4 \\ 80\end{aligned}]+[\begin{aligned}3 \\ 85\end{aligned}]+[\begin{aligned}5 \\ 75\end{aligned}]+[\begin{aligned}4 \\ 72\end{aligned}]) \\ & =\frac{1}{4}[\begin{aligned}16 \\ 312\end{aligned}] \\ & =[\begin{aligned}4 \\ 78\end{aligned}].\end{aligned}


$$

So, the average number of courses is $4,$ and the average final grade is $78.$

### Example: Finding the Sample Mean of an Observation Matrix

#### Question

$$


[\begin{aligned}1 & 1 & 0 & 2 \\ 2 & 5 & 3 & 2\end{aligned}]


$$

Consider the observation matrix $X$ above, where the individual observations are given in columns. Find the sample mean vector of $X.$

#### Explanation

Recall that the sample mean vector is given by

$$


\mathbf{m} = \dfrac{1}{n} \sum_{i=1}^n \mathbf{x}_i,


$$

where $\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_n$ are the individual observations (columns of $X$).

From the matrix, we have that

$$


[\begin{aligned}1 \\ 2\end{aligned}]


$$

Therefore, the sample mean is

$$


\begin{aligned}𝐦 & =\frac{1}{4}(𝐱_{1}+𝐱_{2}+𝐱_{3}+𝐱_{4}) \\ & =\frac{1}{4}([\begin{aligned}1 \\ 2\end{aligned}]+[\begin{aligned}1 \\ 5\end{aligned}]+[\begin{aligned}0 \\ 3\end{aligned}]+[\begin{aligned}2 \\ 2\end{aligned}]) \\ & =\frac{1}{4}[\begin{aligned}4 \\ 12\end{aligned}] \\ & =[\begin{aligned}1 \\ 3\end{aligned}].\end{aligned}


$$

### Mean-Deviation Form

Earlier, we studied data that reported the number of courses selected and the average grades of a sample of four college students. The observation matrix for this data was

$$


[\begin{aligned}4 & 3 & 5 & 4 \\ 80 & 85 & 75 & 72\end{aligned}]


$$

The individual observations are

$$


[\begin{aligned}4 \\ 80\end{aligned}]


$$

We also found the sample mean vector

$$


[\begin{aligned}4 \\ 78\end{aligned}]


$$

One thing we can do with this data is to check how much each observation differs from the mean values. To do that, we compute the difference between each observation and the sample mean vector:

$$


\begin{aligned}𝐛_{1} & =𝐱_{1}−𝐦=[\begin{aligned}4 \\ 80\end{aligned}]−[\begin{aligned}4 \\ 78\end{aligned}]=[\begin{aligned}0 \\ 2\end{aligned}] \\ 𝐛_{2} & =𝐱_{2}−𝐦=[\begin{aligned}3 \\ 85\end{aligned}]−[\begin{aligned}4 \\ 78\end{aligned}]=[\begin{aligned}−1 \\ 7\end{aligned}] \\ 𝐛_{3} & =𝐱_{3}−𝐦=[\begin{aligned}5 \\ 75\end{aligned}]−[\begin{aligned}4 \\ 78\end{aligned}]=[\begin{aligned}1 \\ −3\end{aligned}] \\ 𝐛_{4} & =𝐱_{4}−𝐦=[\begin{aligned}4 \\ 72\end{aligned}]−[\begin{aligned}4 \\ 78\end{aligned}]=[\begin{aligned}0 \\ −6\end{aligned}]\end{aligned}


$$

We collect these differences in a new matrix, as follows:

$$


[\begin{aligned}0 & −1 & 1 & 0 \\ 2 & 7 & −3 & −6\end{aligned}]


$$

The matrix $B$ is the **mean-deviation form** of $X.$ It's often easier to work with the mean-deviation form, especially if the original data contains large numbers.

Notice that the mean of a mean-deviation form equals the zero vector:

$$


\begin{aligned}𝐦_{𝐵} & =\frac{1}{4}([\begin{aligned}0 \\ 2\end{aligned}]+[\begin{aligned}−1 \\ 7\end{aligned}]+[\begin{aligned}1 \\ −3\end{aligned}]+[\begin{aligned}0 \\ −6\end{aligned}]) \\ & =\frac{1}{4}([\begin{aligned}0 \\ 0\end{aligned}]) \\ & =[\begin{aligned}0 \\ 0\end{aligned}]\end{aligned}


$$

### Example: Finding the Mean-Deviation Form of an Observation Matrix

#### Question

$$


[\begin{aligned}5 & 9 & 4 \\ 15 & −7 & 1\end{aligned}]


$$

Consider the observation matrix $X$ above, where the individual observations are given in columns. Find the mean-deviation form of $X.$

#### Explanation

Recall that the mean-deviation form of the observation matrix

$$


\begin{aligned}| & | & & | \\ 𝐱_{1} & 𝐱_{2} & ⋯ & 𝐱_{𝑛} \\ | & | & & |\end{aligned}


$$

is given by

$$


\begin{aligned}| & | & & | \\ 𝐛_{1} & 𝐛_{2} & ⋯ & 𝐛_{𝑛} \\ | & | & & |\end{aligned}


$$

where $\mathbf{b}_i = \mathbf{x}_i - \mathbf{m}$ for $i = 1,2, \ldots, n,$ and $\mathbf{m}$ is sample mean vector.

From the matrix, we have that

$$


[\begin{aligned}5 \\ 15\end{aligned}]


$$

As a result, the sample mean is

$$


\begin{aligned}𝐦 & =\frac{1}{3}(𝐱_{1}+𝐱_{2}+𝐱_{3}) \\ & =\frac{1}{3}([\begin{aligned}5 \\ 15\end{aligned}]+[\begin{aligned}9 \\ −7\end{aligned}]+[\begin{aligned}4 \\ 1\end{aligned}]) \\ & =\frac{1}{3}[\begin{aligned}18 \\ 9\end{aligned}] \\ & =[\begin{aligned}6 \\ 3\end{aligned}].\end{aligned}


$$

Now, we have the following:

$$


\begin{aligned}𝐛_{1} & =𝐱_{1}−𝐦=[\begin{aligned}5 \\ 15\end{aligned}]−[\begin{aligned}6 \\ 3\end{aligned}]=[\begin{aligned}−1 \\ 12\end{aligned}] \\ 𝐛_{2} & =𝐱_{2}−𝐦=[\begin{aligned}9 \\ −7\end{aligned}]−[\begin{aligned}6 \\ 3\end{aligned}]=[\begin{aligned}3 \\ −10\end{aligned}] \\ 𝐛_{3} & =𝐱_{3}−𝐦=[\begin{aligned}4 \\ 1\end{aligned}]−[\begin{aligned}6 \\ 3\end{aligned}]=[\begin{aligned}−2 \\ −2\end{aligned}]\end{aligned}


$$

Therefore, the mean-deviation form is

$$


[\begin{aligned}−1 & 3 & −2 \\ 12 & −10 & −2\end{aligned}]


$$

### The Covariance Matrix

Let's consider again the mean-deviation matrix for the students' data we found previously:

$$


[\begin{aligned}0 & −1 & 1 & 0 \\ 2 & 7 & −3 & −6\end{aligned}]


$$

Calculating the product $B B^T,$ we obtain

$$


\begin{aligned}[\begin{aligned}0 & −1 & 1 & 0 \\ 2 & 7 & −3 & −6\end{aligned}]\begin{aligned}0 & 2 \\ −1 & 7 \\ 1 & −3 \\ 0 & −6\end{aligned} & =[\begin{aligned}2 & −10 \\ −10 & 98\end{aligned}].\end{aligned}


$$

Let's analyze what we've obtained:

- The entry in the first row and first column (${\color{red}2}$) is the sum of the squares of the mean deviations of the number of courses.

- The entry in the second row and second column (${\color{blue}98}$) is the sum of the squares of the mean deviations of the final grades.

- The off-diagonal entries (${\color{purple}-10}$) are the sum of the products of the mean deviations.

Since there were $4$ observations in total, if we divide each entry by $4-1=3,$ we will get a matrix $C$ with the *sample variances* in the diagonal and the *sample covariance* in the off-diagonal positions:

$$


[\begin{aligned}2 & −10 \\ −10 & 98\end{aligned}]


$$

This matrix is called the **covariance matrix** of the data.

In general, the sample covariance matrix is given by

$$


C = \dfrac{1}{n-1} B B^T,


$$

where $B$ is the observation matrix in the mean-deviation form, and $n$ is the number of observations.

### Example: Finding the Covariance Matrix

#### Question

$$


[\begin{aligned}2 & 6 & 4 \\ −4 & 1 & 6\end{aligned}]


$$

Consider the observation matrix $X$ above, where the individual observations are given in columns. Find the sample covariance matrix of the data.

#### Explanation

Recall that the sample covariance matrix is given by

$$


C = \dfrac{1}{n-1} B B^T,


$$

where $B$ is the observation matrix in the mean-deviation form, and $n$ is the number of observations.

So, we first need to compute the mean-deviation form of our observation matrix.

The sample mean is

$$


\begin{aligned}𝐦 & =\frac{1}{3}(𝐱_{1}+𝐱_{2}+𝐱_{3}) \\ & =\frac{1}{3}([\begin{aligned}2 \\ −4\end{aligned}]+[\begin{aligned}6 \\ 1\end{aligned}]+[\begin{aligned}4 \\ 6\end{aligned}]) \\ & =\frac{1}{3}[\begin{aligned}12 \\ 3\end{aligned}] \\ & =[\begin{aligned}4 \\ 1\end{aligned}].\end{aligned}


$$

Now, we have the following:

$$


\begin{aligned}𝐛_{1} & =𝐱_{1}−𝐦=[\begin{aligned}2 \\ −4\end{aligned}]−[\begin{aligned}4 \\ 1\end{aligned}]=[\begin{aligned}−2 \\ −5\end{aligned}] \\ 𝐛_{2} & =𝐱_{2}−𝐦=[\begin{aligned}6 \\ 1\end{aligned}]−[\begin{aligned}4 \\ 1\end{aligned}]=[\begin{aligned}2 \\ 0\end{aligned}] \\ 𝐛_{3} & =𝐱_{3}−𝐦=[\begin{aligned}4 \\ 6\end{aligned}]−[\begin{aligned}4 \\ 1\end{aligned}]=[\begin{aligned}0 \\ 5\end{aligned}]\end{aligned}


$$

Therefore, the mean-deviation form is

$$


[\begin{aligned}−2 & 2 & 0 \\ −5 & 0 & 5\end{aligned}]


$$

Finally, the sample covariance matrix is

$$


\begin{aligned}𝐶 & =\frac{1}{3−1}[\begin{aligned}−2 & 2 & 0 \\ −5 & 0 & 5\end{aligned}]\begin{aligned}−2 & −5 \\ 2 & 0 \\ 0 & 5\end{aligned} \\ & =\frac{1}{2}[\begin{aligned}8 & 10 \\ 10 & 50\end{aligned}].\end{aligned}


$$
