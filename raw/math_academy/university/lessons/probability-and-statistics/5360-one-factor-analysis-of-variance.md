# One-Factor Analysis of Variance

Source: https://www.mathacademy.com/topics/5360?courseId=73
Topic ID: 5360

## Prerequisites

- [The F-Distribution](./3060-the-f-distribution.md)
- [Hypothesis Tests for Two Means: Equal But Unknown Population Variances](./3313-hypothesis-tests-for-two-means-equal-but-unknown-population-variances.md)
- [The Relationship Between SSW, SSB, SST](./5365-the-relationship-between-ssw-ssb-sst.md)

## Lesson

### Introduction

In a previous lesson, we saw how to conduct a hypothesis test to check whether two means are equal for populations with equal variance. In this lesson, we will learn how to perform a hypothesis test, called an **ANOVA** test, to determine if the population means of *three or more* groups are equal.

Suppose we have $K$ groups and $\mu_1, \mu_2, \ldots \mu_K$ are the population means of each group.

Then, we can formulate the following null and alternative hypotheses:

- $H_0{:}\: \mu_1 = \mu_2 = \ldots = \mu_K$

- $H_1{:}$ There is at least one population mean that differs from the others.

The test statistic we will use is

$$


W = \dfrac{\text{MSB}}{\text{MSW}},


$$

where

- $\text{MSW}$ is the mean sum of squares within groups,

- $\text{MSB}$ is the mean sum of squares between groups.

Intuitively, we can interpret $W$ as follows:

- If $W$ is large, then $\text{MSB}$ is much greater than $\text{MSW}.$ This means that the average variation between one group and another is larger than the average deviation within a group. If $W$ exceeds some threshold value, we reject $H_0.$

- If $W$ is small, then $\text{MSB}$ is much smaller than $\text{MSW}.$ This means that the average variation between groups is smaller than the average variation within groups. If $W$ is smaller than some threshold value, we don't reject $H_0.$

The statistic $W$ is called $F$-ratio because, as we will see, it follows a Fisher's $F$-distribution (provided certain assumptions hold).

### The One-Factor ANOVA Table

It will be convenient to collect all the relevant statistics for this problem in a **one-factor ANOVA table,** shown below.

Recall that:

- $\text{SSW}$ is the sum of squares within groups,

- $\text{SSB}$ is the sum of squares between groups,

- $\text{SST}$ is the total sum of squares, and $\text{SST}=\text{SSW}+\text{SSB},$

- $K$ is the number of groups,

- $n$ is the total number of sample elements.

For example, suppose a particular feature is being examined across $5$ groups of individuals to determine if the mean varies by group. A sample of size $n=80$ is conducted and it is found that

$$


\text{SSB} = 124, \qquad \text{SSW} = 262.5.


$$

Let's complete the one-factor ANOVA table for this sample.

- First, we are given $\text{SSB}$ and $\text{SSW},$ so we can compute $\text{SST}$ as follows:

- The degrees of freedom of $\text{SSB}$ are

- The degrees of freedom of $\text{SSW}$ are

- The degrees of freedom of $\text{SST}$ are

- The mean sum of squares between groups is

- The mean sum of squares within groups is

- Finally, the $F$ ratio is

Therefore, the completed table is as follows.

### Example: Completing a One-Factor ANOVA Table

#### Question

Fill in the missing entries in the following one-factor ANOVA table, which gives the statistics of a sample of $n=26$ individuals divided into $K=3$ groups. Round your answers to two decimal places where appropriate.

#### Explanation

Recall that the one-factor ANOVA table for comparing $K$ groups in a sample of size $n$ gives the following data.

where

- $\text{SSW}$ is the sum of squares within groups,

- $\text{SSB}$ is the sum of squares between groups,

- $\text{SST}$ is the total sum of squares, and $\text{SST}=\text{SSW}+\text{SSB}.$

Let's go through the missing entries in the given table.

- $\text{SSB}$ can be computed using the above relation:

- The degrees of freedom of $\text{SSB}$ are

- The degrees of freedom of $\text{SSW}$ are

- The mean sum of squares between groups is

- The mean sum of squares within groups is

- Finally, the $F$ ratio is

Therefore, the completed table is as follows.

### The Distribution of the F-Ratio

Suppose we have a sample of size $n,$ where the observations are divided into $K$ groups. We want to determine whether the population mean varies by group.

In other words, we want to test the following null and alternative hypotheses:

- $H_0{:}\: \mu_1 = \mu_2 = \ldots = \mu_K$

- $H_1{:}$ There is at least one population mean that differs from the others,

where $\mu_1, \mu_2, \ldots, \mu_K$ are the population means of each group.

We've already introduced the $F$-ratio test statistic for this problem:

$$


W = \dfrac{\text{MSB}}{\text{MSW}}


$$

Now, we will discuss the distribution of $W.$

Let's assume that the data points are independent and follow a normal distribution with equal mean $\mu$ and variance $\sigma^2{:}$

$$


X_{jk} \sim N(\mu, \sigma^2), \qquad j=1, 2, \ldots, n_k, \quad k=1, 2, \ldots, K


$$

where $n_k$ is the size of the $k$th group.

Also, recall that

$$


\text{SST} = \sum_{k=1}^K\sum_{j=1}^{n_k} (X_{jk} - \overline{X})^2, \qquad \text{SSW} = \sum_{k=1}^K \sum_{j=1}^{n_k} (X_{jk} - \overline{X}_k)^2, \qquad \text{SSB} = \sum_{k=1}^K n_k (\overline{X}_k - \overline{X})^2.


$$

Given a sample of $n$ independent normal random variables with variance $\sigma^2$, for the sample variance $S^2,$ we have

$$


\dfrac{(n-1)S^2}{\sigma^2} \sim\chi^2(n-1).


$$

We can use this result to find the distribution of $\text{SST}/\sigma^2.$ Since

$$


\text{SST} = (n-1)S^2


$$

it follows that

$$


\dfrac{\text{SST}}{\sigma^2} = \dfrac{(n-1)S^2}{\sigma^2}\sim \chi^2(n-1).


$$

We can also apply this result to *each* group mean:

$$


\dfrac{1}{\sigma^2}\sum_{j=1}^{n_k}(X_{jk} - \overline{X}_k)^2 \sim \chi^2(n_k-1), \quad k = 1, \ldots, K


$$

Moreover, the above sums are independent. Since each group variance contributes $(n_k - 1)$ degrees of freedom, we have

$$


\dfrac{\text{SSW}}{\sigma^2} = \dfrac{1}{\sigma^2}\sum_{k=1}^K\sum_{j=1}^{n_k}(X_{jk} - \overline{X}_k)^2 \sim \chi^2(n - K).


$$

It can be shown that $\text{SSB}$ and $\text{SSW}$ are independent. Therefore, since $\text{SST} = \text{SSB} + \text{SSW},$ we have that $\text{SSB}/\sigma^2$ follows a chi-squared distribution with $n-1 - (n-K) = K-1$ degrees of freedom.

Notice that our test statistic $W$ is the ratio of two independent chi-squared random variables divided by their respective degrees of freedom:

$$


\begin{aligned}\frac{(\frac{SSB}{𝜎^{2}})}{𝜎^{2}}⋅\frac{𝑛−𝐾}{𝐾−1} & =\frac{(\frac{SSB}{𝜎^{2}})}{𝜎^{2}}⋅\frac{𝑛−𝐾}{𝐾−1} \\ & =\frac{(\frac{SSB}{𝐾−1})}{𝐾−1} \\ & =\frac{MSB}{MSW} \\ & =𝑊\end{aligned}


$$

Therefore, $W$ follows a Fisher's $F$-distribution with $\nu_1=K-1$ and $\nu_2=n-K$ degrees of freedom.

$$


W\sim F(K-1, n-K).


$$

### Conducting a One-Factor ANOVA Test

Let's return to the previous example in which we calculated the ANOVA table of a sample of $n=80$ data points distributed among $K=5$ groups:

We want to test the following null and alternative hypotheses on the above data set:

- $H_0{:}\: \mu_1 = \mu_2 = \mu_3= \mu_4 = \mu_5$

- $H_1{:}$ There is at least one population mean that differs from the others,

where $\mu_1, \mu_2, \ldots, \mu_5$ are the population means of each group.

We conduct the test as follows:

- The $F$ ratio statistic test is

- The numbers of degrees of freedom for this test are

- Since this is a hypothesis test, we must choose an appropriate significance level. So, let's choose

- Since we want to know whether the test statistic exceeds a certain threshold, the one factor ANOVA test is *always right-tailed*. Using a Fisher's $F$-distribution table, the critical value for $\nu_1=4,$ $\nu_2=75$ at a $5\%$ significance level is $f_{\text{critical}}=2.494,$ and the critical region is as shown below.

Our test statistic $(8.857)$ lies inside the critical region. Therefore, there is $\boxed{\color{blue}\text{sufficient}}$ evidence to reject the null hypothesis.

In other words, the population means varies by group.

### Example: Testing a Hypothesis Using ANOVA

#### Question

The marketing team of an advertising agency evaluates the effectiveness of three different online advertising strategies: Strategy A, Strategy B, and Strategy C. The customer engagement times for each strategy are assumed to follow a normal distribution with respective means $\mu_1,$ $\mu_2,$ and $\mu_3,$ all having the same variance $\sigma^2.$ The team conducts a hypothesis test at a $10\%$ significance level to test the hypothesis $\mu_1=\mu_2=\mu_3,$ against the alternative hypothesis that at least one mean differs from the others.

Independent random samples are conducted with $15$ customers engaged by Strategy A, $20$ customers engaged by Strategy B, and $24$ customers engaged by Strategy C. It is found that $\text{SSB}=42\,\text{min}^2$ and $\text{SSW}=308\,\text{min}^2.$

The table below gives the values of $x$ that satisfy $P(X\gt x) = 10\%,$ where $X\sim F(\nu_1, \nu_2).$

Using this information, fill in the following missing entries.

- The $F$-ratio for this test is approximately $\boxed{\phantom{\mathrm{3.818}}}.$

- At the $10\%$ level of significance, there is $\boxed{\phantom{\mathrm{sufficient}}}$ evidence that at least one mean differs from the others.

#### Explanation

We are told that the three populations are normally distributed, independent, and have the same variance.

In cases like this, when the null hypothesis is true (i.e., all means are equal), the random variable

$$


W = \dfrac{\text{MSB}}{\text{MSW}}


$$

follows a $F$-distribution with $df_B = K-1$ and $df_W= n-K$ degrees of freedom, where

- $K$ is the number of groups,

- $n$ is the grand sample size,

- $\text{MSB}$ is the mean sum of squares between groups,

- $\text{MSW}$ is the mean sum of squares within groups.

Furthermore, recall that

$$


\text{MSB} = \dfrac{\text{SSB}}{df_B}, \qquad \text{MSW} = \dfrac{\text{SSW}}{df_W}


$$

where

- $\text{SSB}$ is the sum of squares between groups,

- $\text{SSW}$ is the sum of squares within groups.

In our example, the null and alternative hypotheses are:

- $H_0: \mu_1 = \mu_2 = \mu_3$

- $H_1:$ $\mu_i\neq \mu_j$ for at least one $i,j$ pair.

We have $K=3$ groups, and

$$


n = 15+20+24=59.


$$

For the degrees of freedom, we have

$$


\begin{aligned}𝑑𝑓_{𝐵} & =𝐾−1 \\ & =3−1 \\ & =2, \\ 𝑑𝑓_{𝑊} & =𝑛−𝐾 \\ & =59−3 \\ & =56.\end{aligned}


$$

Therefore, we have that $W\sim F(2,56),$ and

$$


\text{MSB} = \dfrac{42}{2} = 21, \qquad \text{MSW} = \dfrac{308}{56} = 5.5.


$$

Let's now examine our statements.

- We reject the null hypothesis when $\text{MSB}$ is large compared to $\text{MSW}.$ Therefore, we conduct a right-tailed test. Assuming the null hypothesis, we compute the test statistic: Therefore, the $F$-ratio for this test is approximately $\boxed{\color{blue}3.818}.$

- Our critical region is the set $W > a,$ where $P(W > a)=10\%.$ To find $a,$ we focus on the column of the table corresponding to $\nu_1=2$ and the row corresponding to $\nu_2=56.$ $\nu_2\setminus \nu_1$ $2$ $3$ $4$ $56$ $\,\boxed{\color{blue}2.400}\,$ $\,2.184\,$ $\,2.048\,$ $57$ $\,2.398\,$ $\,2.182\,$ $\,2.046\,$ $58$ $\,2.396\,$ $\,2.181\,$ $\,2.044\,$ $59$ $\,2.395\,$ $\,2.179\,$ $\,2.043\,$ The table shows that $a = 2.400$ is our critical value. So, the critical region is Our test statistic ($3.818$) lies in the critical region, as shown below. So, we reject the null hypothesis $H_0.$ As a result, we conclude the following:

**
