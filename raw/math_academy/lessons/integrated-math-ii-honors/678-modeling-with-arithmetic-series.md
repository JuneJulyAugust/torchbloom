# Modeling With Arithmetic Series

Source: https://www.mathacademy.com/topics/678?courseId=128
Topic ID: 678

## Prerequisites

- [Calculating the Number of Terms in an Arithmetic Series](./676-calculating-the-number-of-terms-in-an-arithmetic-series.md)
- [Modeling With Arithmetic Sequences](../algebra-i/2223-modeling-with-arithmetic-sequences.md)

## Lesson

### Introduction

We can use arithmetic series to model real-world problems and make predictions.

For example, suppose that Giorgia saves for a family holiday, depositing money into a savings account every month. She deposits $200$ at the beginning of January, $210$ at the beginning of February, $220$ at the beginning of March, and so on. If this trend continues, how much money will she have in the account at the end of July, assuming that the account earns no interest?

Giorgia's initial deposit was $200,$ and her monthly deposits increase by $10$ per month. Therefore, the amount of money she deposits in month $n$ can be modeled as an arithmetic sequence, as follows:

- The first term is $a_1=200.$

- The common difference is $d=10.$

- The total number of terms is $N=7$ (since Giorgia made the last payment in July, the $7$th month of the year).

To find the total amount of money in the account at the end of July, we have to calculate the sum of an arithmetic series. To do that, we use the formula

$$


S_N = \dfrac N 2 (2a_1 + (N-1)d).


$$

Substituting our values into the above, we get

$$


\begin{aligned}𝑆_{7} & =\frac{7}{2}(2(200)+(7−1)⋅10) \\ & =\frac{7}{2}(400+6⋅10) \\ & =\frac{7}{2}(460) \\ & =1\,610.\end{aligned}


$$

Therefore, Giorgia will have $1\,610$ in the account by the end of July.

### Example: Finding the Sum of an Arithmetic Series

#### Question

In an elementary school, there are $240$ students in the first grade, $210$ students in the second grade, $180$ students in the third grade, etc. Assuming this trend continues, what is the total number of students if the school has $6$ grades?

#### Explanation

The number of students ** by a fixed amount of $30$ students per grade. Therefore, the number of students in the $n$th grade can be modeled as an arithmetic sequence as follows:

- The first term is $a_1=240.$

- The common difference is $d=-30.$

- The total number of terms is $N=6.$

To find the total number of students in the school, we have to calculate the sum of an arithmetic series. To do that, we use the formula

$$


S_N = \dfrac N 2 \big(2a_1 + (N-1) d \big).


$$

Substituting our values into the above, we get

$$


\begin{aligned}𝑆_{6} & =\frac{6}{2}(2⋅240+(6−1)⋅(−30)) \\ & =3⋅(480+5⋅(−30)) \\ & =3⋅(480−150) \\ & =3⋅330 \\ & =990.\end{aligned}


$$

Therefore, there are $990$ students in total.

### Example: Calculating the Number of Terms in Arithmetic Series

#### Question

Mary decides to start saving some money each month. She saves $3$ in the first month, an additional $9$ in the second month, an additional $15$ in the third month, and so on. Assuming this trend continues, how long does it take her to save $243$ in total?

#### Explanation

The amount Mary saves each month increases by a fixed amount of $6$ per month. Therefore, the amount she saves in the $n$th month can be modeled as an arithmetic sequence, as follows:

- The first term is $a_{1}=3$

- The common difference is $d=6$

- The sum of the series is $S_N=243.$

The sum of an arithmetic series is given by the formula

$$


S_N = \dfrac N 2 \big(2a_1 + (N-1) d \big).


$$

Substituting our values into the above and solving for $N,$ we get

$$


\begin{aligned}243 & =\frac{𝑁}{2}(2(3)+(𝑁−1)(6)) \\ 243 & =\frac{𝑁}{2}(6+6𝑁−6) \\ 243 & =\frac{𝑁}{2}⋅6𝑁 \\ 243 & =3𝑁^{2} \\ 81 & =𝑁^{2} \\ 𝑁 & =9.\end{aligned}


$$

Notice that we take the positive square root because $N$ can't be negative.

Therefore, it will take Mary $9$ months to save $243.$

### Example: Finding the Value of a Term of an Arithmetic Series

#### Question

Sandy is building a tower using $144$ blocks. She plans to have a single block in the top row, $3$ blocks in the second row down, $5$ blocks in the third row down, and so on. If this trend continues, how many blocks will she place in the bottom row?

#### Explanation

Sandy plans to have $1$ block in the top row, increasing by a fixed amount of $2$ blocks per row. Sandy uses $144$ blocks in total, and she will have $N$ rows. Therefore, we have an arithmetic series with the following values:

- The first term is $a_1 = 1.$

- The common difference is $d=2.$

- The sum of the series is $S_N = 144.$

The sum of an arithmetic series is given by the formula

$$


S_N = \dfrac N 2 \big(2a_1 + (N-1) d \big).


$$

Substituting our values into the above and solving for $N,$ we get

$$


\begin{aligned}144 & =\frac{𝑁}{2}(2⋅1+(𝑁−1)⋅2) \\ 144 & =\frac{𝑁}{2}(2+2𝑁−2) \\ 144 & =𝑁^{2} \\ 𝑁 & =12.\end{aligned}


$$

Notice that we take the positive square root because $N$ can't be negative.

Therefore, the tower will have $12$ rows, and the number of blocks in the bottom row is given by $a_{12}.$

Substituting our values into the formula for the $N$th term of an arithmetic sequence to find $a_{12},$ we conclude that

$$


\begin{aligned}𝑎_{𝑁} & =𝑎_{1}+(𝑁−1)𝑑 \\ 𝑎_{12} & =1+(12−1)⋅2 \\ & =1+11⋅2 \\ & =1+22 \\ & =23.\end{aligned}


$$

Therefore, Sandy will place $23$ blocks in the bottom row.
