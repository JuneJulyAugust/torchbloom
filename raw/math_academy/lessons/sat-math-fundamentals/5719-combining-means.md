# Combining Means

Source: https://www.mathacademy.com/topics/5719?courseId=120
Topic ID: 5719

## Prerequisites

- [Solving Linear Equations by Clearing a Rational Expression](../grade-7/651-solving-linear-equations-by-clearing-a-rational-expression.md)
- [The Mean of a Data Set](../grade-6/2479-the-mean-of-a-data-set.md)

## Lesson

### Introduction

Suppose we have two data sets, $X$ and $Y$, each containing $8$ data points:

- the mean of data set $X$ is $44$, and

- the mean of data set $Y$ is $36.$

What is the mean of the combined data set?

Since both $X$ and $Y$ contain *the same number of data points,* the mean of the combined data set $Z$ is simply the average of the two means:

$$


\textrm{mean}(Z) =\dfrac{\textrm{mean}(X)+\textrm{mean}(Y)}{2}


$$

We'll prove this result at the end of the lesson.

Now, in our example, we have the following:

$$


\begin{aligned}mean(𝑍) & =\frac{44+36}{2} \\ & =\frac{80}{2} \\ & =40\end{aligned}


$$

**Watch out!** It's important that the two data sets have the *same number of data points*! When the sizes differ, this formula *no longer applies!* We'll see how to handle that situation later in the lesson.

### Example: Finding a Combined Mean When the Smaller Data Sets Have Equal Sizes

#### Question

Three delivery drivers, Dana, Eli, and Fiona, each drove for $10$ hours. The average speed of Dana was $55\,\dfrac{\textrm{mi}}{\textrm{h}}$, Eli’s was $65\,\dfrac{\textrm{mi}}{\textrm{h}}$, and Fiona’s was $75\,\dfrac{\textrm{mi}}{\textrm{h}}$. What was their average speed over the $30$ hours combined?

#### Explanation

Let the combined data set of all driving speeds be denoted by $S.$

Because each driver drove the same number of hours, we can compute the overall average by taking the mean of the three individual speeds:

$$


\begin{aligned}mean(𝑆) & =\frac{55+65+75}{3} \\ & =\frac{195}{3} \\ & =65\end{aligned}


$$

Therefore, the average score the $30$ hours is $65\,\dfrac{\textrm{mi}}{\textrm{h}}.$

### Finding a Combined Mean Using a Weighted Average

Now, let's consider the case where the data sets have different sizes.

Suppose we have data sets $X$ and $Y$ with the following information.

- $n_X = 6$ is the size of data set $X.$

- $\text{mean}(X) = 24$ is the mean of data set $X.$

- $n_Y = 14$ is the size of data set $Y.$

- $\text{mean}(Y) = 30$ is the mean of data set $Y.$

Let $Z$ be the data set that combines all the data points from data sets $X$ and $Y.$ What is the mean of the *combined* data set $Z?$

The total number of data points is

$$


n_X + n_Y = 6 + 14 = 20.


$$

We compute the combined mean using a so-called **weighted average:**

$$


\textrm{mean}(Z)= \dfrac{n_X \cdot \textrm{mean}(X) + n_Y \cdot \textrm{mean}(Y)}{n_X + n_Y}


$$

We'll explain why this formula gives the combined mean at the end of the lesson.

In our example, we have the following:

$$


\begin{aligned}mean(𝑍) & =\frac{6⋅24+14⋅30}{6+14} \\ & =\frac{144+420}{20} \\ & =\frac{564}{20} \\ & =28.2\end{aligned}


$$

Let's now use a weighted average to find the combined mean of three data sets.

### Example: Finding a Combined Mean When the Smaller Data Sets Have Unequal Sizes

#### Question

Suppose data set $A$ contains $5$ data points, data set $B$ contains $15$ data points, and data set $C$ contains $10$ data points. The mean of data set $A$ is $24$, the mean of data set $B$ is $42$, and the mean of data set $C$ is $36.$ What is the mean of the combined data set?

#### Explanation

Let $D$ be the data set that combines all the data points from data sets $A$, $B$, and $C.$

We introduce the following notation:

- $n_A = 5$ is the size of data set $A.$

- $\text{mean}(A) = 24$ is the mean of data set $A.$

- $n_B = 15$ is the size of data set $B.$

- $\text{mean}(B) = 42$ is the mean of data set $B.$

- $n_C = 10$ is the size of data set $C.$

- $\text{mean}(C) = 36$ is the mean of data set $C.$

The total number of data points is

$$


n_A + n_B + n_C = 5 + 15 + 10 = 30.


$$

We compute the combined mean using a weighted average:

$$


\begin{aligned}mean(𝐷) & =\frac{𝑛_{𝐴}⋅mean(𝐴)+𝑛_{𝐵}⋅mean(𝐵)+𝑛_{𝐶}⋅mean(𝐶)}{𝑛_{𝐴}+𝑛_{𝐵}+𝑛_{𝐶}} \\ & =\frac{5⋅24+15⋅42+10⋅36}{5+10+15} \\ & =\frac{120+630+360}{30} \\ & =\frac{1110}{30} \\ & =37\end{aligned}


$$

Therefore, the mean of the combined data set is $37.$

### Solving for an Unknown Smaller Mean

Suppose we have data sets $A$ and $B,$ and we create a new data set $C$ by combining all the elements from $A$ and $B.$ We're given the following information:

- $n_A = 4$ is the size of data set $A.$

- $n_B = 16$ is the size of data set $B.$

- $\text{mean}(B) = 40$ is the mean of data set $B.$

- $\text{mean}(C) = 37$ is the mean of the combined data set.

Notice that we do not know $\textrm{mean}(A).$ How can we find this using the information given above?

The total number of data points is

$$


n_A + n_B = 4 + 16 = 20.


$$

The combined mean is found using a weighted average:

$$


\textrm{mean}(C) = \dfrac{n_A \cdot \textrm{mean}(A) + n_B \cdot \textrm{mean}(B)}{n_A + n_B}


$$

Substituting the known numbers, we have

$$


\begin{aligned}mean(𝐶) & =\frac{𝑛_{𝐴}⋅mean(𝐴)+𝑛_{𝐵}⋅mean(𝐵)}{𝑛_{𝐴}+𝑛_{𝐵}} \\ 37 & =\frac{4⋅mean(𝐴)+16⋅40}{4+16} \\ 37 & =\frac{4⋅mean(𝐴)+640}{20}.\end{aligned}


$$

We wish to solve for $\textrm{mean}(A).$ To do this, we first multiply both sides by $20.$ This gives

$$


740 = 4 \cdot \textrm{mean}(A) + 640.


$$

Then, we subtract $640$ from both sides.

$$


100 = 4 \cdot \textrm{mean}(A)


$$

Finally, we divide both sides by $4{:}$

$$


\textrm{mean}(A) = 25


$$

Let's now consider a similar problem where one of the data sets contains an unknown number of elements.

### Example: Finding an Unknown Mean or Group Size Given the Combined Mean

#### Question

Suppose data set $D$ contains $n_D$ data points and data set $E$ contains $10$ data points. The mean of data set $D$ is $20$, and the mean of data set $E$ is $32.$ If the mean of the combined data set is $30$, what is the value of $n_D?$

#### Explanation

Let $F$ be the data set that combines all the data points from data sets $D$ and $E.$

We introduce the following notation:

- $n_D$ is the unknown size of data set $D.$

- $\text{mean}(D) = 20$ is the mean of data set $D.$

- $n_E = 10$ is the size of data set $E.$

- $\text{mean}(E) = 32$ is the mean of data set $E.$

- $\text{mean}(F) = 30$ is the mean of the combined data set.

The total number of data points is

$$


n_D + n_E = n_D + 10.


$$

We compute the combined mean using a weighted average:

$$


\begin{aligned}mean(𝐹) & =\frac{𝑛_{𝐷}⋅mean(𝐷)+𝑛_{𝐸}⋅mean(𝐸)}{𝑛_{𝐷}+𝑛_{𝐸}} \\ 30 & =\frac{𝑛_{𝐷}⋅20+10⋅32}{𝑛_{𝐷}+10} \\ 30 & =\frac{20𝑛_{𝐷}+320}{𝑛_{𝐷}+10}\end{aligned}


$$

We wish to solve for $n_D.$ To do this, we first multiply both sides by $(n_D + 10){:}$

$$


30(n_D + 10) = 20n_D + 320


$$

Next, we apply the distributive law to the left-hand side:

$$


30n_D + 300 = 20n_D + 320


$$

Then, we subtract $20n_D$ and $300$ from both sides. This gives

$$


10n_D = 20.


$$

Finally, divide both sides by $10$:

$$


n_D = 2


$$

### Proof of the Formula for Equally Sized Data Sets

Let $X = \{x_1, \dots, x_n\}$ and $Y = \{y_1, \dots, y_n\}$ each contain $n$ elements. Then, the means of $X$ and $Y$ are

$$


\textrm{mean}(X) = \dfrac{x_1 + x_2 + \cdots + x_n}{n}, \qquad \textrm{mean}(Y) = \dfrac{y_1 + y_2 + \cdots + y_n}{n}.


$$

The total sum of values in the combined set $Z$ is

$$


\text{sum}(Z) = (x_1 + \cdots + x_n) + (y_1 + \cdots + y_n) = n \cdot \textrm{mean}(X) + n \cdot \textrm{mean}(Y),


$$

and the total number of values is

$$


n + n = 2n.


$$

Therefore, the mean of the combined set is

$$


\begin{aligned}mean(𝑍) & =\frac{𝑛⋅mean(𝑋)+𝑛⋅mean(𝑌)}{2𝑛} \\ & =\frac{𝑛(mean(𝑋)+mean(𝑌))}{2𝑛} \\ & =\frac{mean(𝑋)+mean(𝑌)}{2}.\end{aligned}


$$

### Proof of the Formula With the Weighted Average

Let $X = \{x_1, \dots, x_{n_X}\}$ and $Y = \{y_1, \dots, y_{n_Y}\}$ contain $n_X$ and $n_Y$ elements, respectively. Then, the means of $X$ and $Y$ are

$$


\textrm{mean}(X) = \dfrac{x_1 + x_2 + \cdots + x_{n_X}}{n_X}, \qquad \textrm{mean}(Y) = \dfrac{y_1 + y_2 + \cdots + y_{n_Y}}{n_Y}.


$$

The total sum of values in the combined set $Z$ is

$$


\text{sum}(Z) = (x_1 + \cdots + x_{n_X}) + (y_1 + \cdots + y_{n_Y}) = n_X \cdot \textrm{mean}(X) + n_Y \cdot \textrm{mean}(Y),


$$

and the total number of values is $n_X + n_Y.$ Therefore, the mean of the combined set is the weighted average of the individual means:

$$


\begin{aligned}mean(𝑍) & =\frac{𝑛_{𝑋}⋅mean(𝑋)+𝑛_{𝑌}⋅mean(𝑌)}{𝑛_{𝑋}+𝑛_{𝑌}}\end{aligned}


$$
