# Pascal's Triangle and the Binomial Coefficients

Source: https://www.mathacademy.com/topics/3404?courseId=136
Topic ID: 3404

## Prerequisites

- [Factorials](../../../high-school/traditional/lessons/geometry/774-factorials.md)
- [Expanding Binomials Using Pascal's Triangle](../../../high-school/traditional/lessons/algebra-i/1157-expanding-binomials-using-pascal-s-triangle.md)

## Lesson

### Introduction

Remember that when counting the rows and positions in Pascal's triangle, we always start counting from zero!

- The top row of Pascal's triangle is row $0.$

- The first position of each row (on the left) is position number $0.$

We can write a value in Pascal's triangle as $\displaystyle{\color{red}{a} \choose {\color{blue}b}},$ where the value is located in row $\color{red}a$ and position ${\color{blue}b}.$ This is known as a **binomial coefficient**. In words, we say $\displaystyle{\color{red}{a} \choose {\color{blue}b}}$ as "$\color{red}{a}$ choose ${\color{blue}b}$".

For example, the value located in row $\color{red}4$ and position $\color{blue}2$ is highlighted below.

$$


\begin{aligned} & & & & & 1 & & & & & \\ & & & & 1 & & 1 & & & & \\ & & & 1 & & 2 & & 1 & & & \\ & & 1 & & 3 & & 3 & & 1 & & \\ & 1 & & 4 & & 6 & & 4 & & 1 & \\ ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮\end{aligned}


$$

Therefore, $\displaystyle{{\color{red}4} \choose \color{blue}{2}} = 6.$ Remember, we start counting from zero.

### Example: Determining the Value of a Binomial Coefficient

#### Question

Use Pascal's triangle to determine the value of $\displaystyle{3 \choose 2}.$

#### Explanation

To find the value of $\displaystyle{\color{red}{3} \choose {\color{blue}2}},$ we need to find the number that is located in row $\color{red}3$ and position $\color{blue}2$ of Pascal's triangle.

**** Remember that when counting the rows and positions in Pascal's triangle, we always start counting from zero!

- The top row of Pascal's triangle is row $0.$

- The first position of each row (the one of the left) is position number $0.$

The value located in row $\color{red}3$ and position $\color{blue}2$ is highlighted below.

$$


\begin{aligned} & & & & 1 & & & & \\ & & & 1 & & 1 & & & \\ & & 1 & & 2 & & 1 & & \\ & 1 & & 3 & & 3 & & 1 & \\ ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮\end{aligned}


$$

Therefore, $\displaystyle{3 \choose 2} = 3.$

### Example: Expressing the Relationship Between the Rows of Pascal's Triangle in Terms of Binomial Coefficients

#### Question

Which expression is missing in the following equation?

$$


\displaystyle{4 \choose 3} = \displaystyle{3 \choose 2} + \displaystyle{\left[ \phantom{3 \choose 3}\right]}


$$

#### Explanation

To find $\displaystyle{\color{red}{4} \choose {\color{blue}3}},$ we need to find the number that is located in row $\color{red}4$ and position $\color{blue}3$ of Pascal's triangle.

**** Remember that when counting the rows and positions in Pascal's triangle, we always start counting from zero!

- The top row of Pascal's triangle is row $0.$

- The first position of each row (the one of the left) is position number $0.$

The location of $\displaystyle{4 \choose 3}$ in Pascal's triangle is highlighted below.

$$


\begin{aligned} & & & & & & & (\frac{0}{0}) & & & & & \\ & & & & & & (\frac{1}{0}) & & (\frac{1}{1}) & & & & \\ & & & & & (\frac{2}{0}) & & (\frac{2}{1}) & & (\frac{2}{2}) & & & \\ & & & & (\frac{3}{0}) & & (\frac{3}{1}) & & (\frac{3}{2}) & & (\frac{3}{3}) & & \\ & & & (\frac{4}{0}) & & (\frac{4}{1}) & & (\frac{4}{2}) & & (\frac{4}{3}) & & (\frac{4}{4}) & \\ & & ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮ & & ⋮\end{aligned}


$$

Now, $\displaystyle{4 \choose 3}$ is the sum of the two closest numbers located in the previous row. So

$$


\displaystyle{4 \choose 3} = \displaystyle{3 \choose 2} + \displaystyle{3 \choose 3}.


$$

Therefore, the missing expression is $\displaystyle{3 \choose 3}.$

### A Formula for the Binomial Coefficients

Suppose that we wanted to calculate the value of $\displaystyle{30 \choose 3}.$ If we were to use Pascal's triangle, we'd have to write out $31$ rows, which would take a long time. Thankfully, there is a formula for calculating binomial coefficients.

The binomial coefficient $\displaystyle{n \choose r}$ is given by the formula

$$


\displaystyle{n \choose r} = \dfrac{n!}{(n-r)!\, r!}.


$$

### Example: Calculating Binomial Coefficients Using the Formula

#### Question

Determine the value of $\displaystyle{5 \choose 4}.$

#### Explanation

The binomial coefficient $\displaystyle{n \choose r}$ is given by the formula

$$


\displaystyle{n \choose r} = \dfrac{n!}{(n-r)!\, r!}.


$$

In this case, we have $n = 5$ and $r = 4.$ Therefore,

$$


\begin{aligned}(\frac{5}{4}) & =\frac{5!}{(5−4)!⋅4!} \\ & =\frac{5⋅4!}{1!⋅4!} \\ & =\frac{5⋅4!}{1⋅4!} \\ & =5.\end{aligned}


$$
