# The Relationship Between SSW, SSB, SST

Source: https://www.mathacademy.com/topics/5365?courseId=73
Topic ID: 5365

## Prerequisites

- [One-Factor Within Groups and Between Groups Variation](./3315-one-factor-within-groups-and-between-groups-variation.md)

## Lesson

### Introduction

Suppose that a particular feature is examined across $K$ groups to determine if the mean varies with each group. In an earlier lesson, we introduced the statistics $\text{SSW}$ (sum of squares within groups) and $\text{SSB}$ (sum of squares between groups) to address this problem.

Recall that

$$


\text{SSW} = \sum_{k=1}^K \sum_{j=1}^{n_k} \left(x_{jk} - \overline{x}_k\right)^2, \qquad \text{SSB} = \sum_{k=1}^K n_k \left(\overline{x}_k - \overline{x}\right)^2


$$

where

- the number of data points in the $k$th groups is $n_k,$

- $x_{jk}$ the $j$th data point from the $k$th group,

- $\overline{x}_{k}$ the sample mean of the $k$th group, and

- $\overline{x}$ the grand sample mean.

We will study the relationship between these statistics and the sample variance in this topic.

First, we need to define a new statistic: **The total sum of squares,** denotes $\text{SST},$ is the sum of squared deviations from the grand mean, measured over *all* observations:

$$


\text{SST} = \sum_{k=1}^K\sum_{j=1}^{n_k} (x_{jk} - \overline{x})^2


$$

Now, notice that $\text{SST}$ is simply the sum of squares in the formula for the sample variance measured over all groups:

$$


\text{SST} = (n-1)s^2,


$$

where $n = n_1+n_2+\cdots+ n_k$ (i.e., the total number of observations), and $s^2$ is our unbiased estimate of the population variance $\sigma^2$ (assumed to be the same for all groups).

It can be shown that

$$


\text{SST} = \text{SSW} + \text{SSB}


$$

(we'll derive this result at the end of the lesson). Therefore,

$$


\text{SSW} + \text{SSB} = (n-1)s^2.


$$

The formula above indicates that the total variance of the sample can be decomposed into two components: the variation within groups and the variation between groups.

### Example: Using the Relation Between SSW, SSB, and SST

#### Question

A particular feature is being examined across $3$ groups of individuals to determine if the mean varies by group.

In a sample of $76$ individuals, there are $23$ individuals from Group 1, $25$ from Group 2, and $28$ from Group 3. The sum of squares within groups (SSW) is $27.5,$ and the sum of squares between groups (SSB) is $32.5.$ Find an unbiased estimate $s^2$ for the population variance $\sigma^2.$

#### Explanation

Recall the following relationship between SSW, SSB, and SST:

$$


\text{SSW} + \text{SSB} = \text{SST},


$$

where

- $\text{SSW}$ is the sum of squares within groups,

- $\text{SSB}$ is the sum of squares between groups,

- $\text{SST}$ is the total sum of squares.

Moreover, since

$$


s^2 = \dfrac{1}{n-1}\cdot \text{SST}\qquad\Longrightarrow\qquad (n-1)s^2 = \text{SST}


$$

we have

$$


\text{SSW} + \text{SSB} = (n-1)s^2,


$$

where

- $n$ is the size of the entire sample,

- $s^2$ is an unbiased estimate of the population variance $\sigma^2.$

In our case, we have $\text{SSW}=27.5,$ $\text{SSB}=32.5,$ and

$$


n=23+25+28 = 76.


$$

Therefore,

$$


\begin{aligned}SSW+SSB & =(𝑛−1)𝑠^{2} \\ 27.5+32.5 & =(76−1)𝑠^{2} \\ 60 & =75𝑠^{2} \\ 𝑠^{2} & =0.8\end{aligned}


$$

### Interpreting the Results

Suppose a team of researchers wants to evaluate the effectiveness of three different medications for hypertension. To determine if there is a significant difference in their outcomes, they collected data from three groups of patients, with each group receiving a different medication. They found the following statistics:

$$


\text{SSB} = 102, \qquad \text{SSW}=878, \qquad \text{SST}=980


$$

Let's calculate the ratios of $\text{SSW}$ and $\text{SSB}$ to $\text{SST}{:}$

$$


\dfrac{\text{SSW}}{\text{SST}} \approx 0.896, \qquad \dfrac{\text{SSB}}{\text{SST}} = 1- \dfrac{\text{SSW}}{\text{SST}} \approx 0.104


$$

Note the following:

- The relatively large value of the ratio $\text{SSW}/\text{SST}$ indicates that a large portion ($89.6\%$) of the total variability in hypertension reduction is due to individual differences *within* each treatment group, *rather than differences between the group means*.

- On the other hand, the low value of $\text{SSB}/\text{SST}$ suggests that the group means may not differ significantly. So, the treatment groups' effects on hypertension reduction may be similar, as most variability arises from individual differences within the groups rather than from the treatments themselves

To confirm this, we would typically conduct a so-called **ANOVA test.** However, based on this high $\text{SSW}/\text{SST}$ ratio alone, it is likely that there *is not* a significant difference between the mean effects of the three treatments.

In general, as a rule of thumb:

- If $\dfrac{\text{SSB}}{\text{SST}} \geq 40\%,$ this suggests there may be *high* between-group variability.

- If $\dfrac{\text{SSB}}{\text{SST}} < 40\%,$ this suggests there may be *low* between-group variability.

Remember, this is just a rule of thumb. We can precisely characterize this using an ANOVA test, which we'll study in a future lesson.

### Example: Calculating SSW and SSB In Context

#### Question

A botanist wants to determine if there is a significant difference in the effectiveness of three fertilizers on plant growth. The following table gives the summary statistics of plant growth, in centimeters, of three groups of plants, each receiving a different fertilizer, where $n_k$ is the size of each sample, and $s_k$ is the (sample) standard deviation of each group measured in $\mathrm{cm}^2.$ You're given that the grand (sample) variance is $s^2=15\,\mathrm{cm}^2.$

Select the correct options to make the following statements true.

$\qquad$ The ratio $\dfrac{\text{SSW}}{\text{SST}}$ is approximately $\boxed{\phantom{10kkk}}.$

$\qquad$ This suggests the between-group variability is $\boxed{\phantom{10KKKKKK}}.$

#### Explanation

The sum of squares within groups $(\text{SSW})$ and sum of squares between groups $(\text{SSB})$ are given by

$$


\text{SSW} = \sum_{k=1}^K \sum_{j=1}^{n_k} \left(x_{jk} - \overline{x}_k\right)^2, \qquad \text{SSB} = \sum_{k=1}^K n_k \left(\overline{x}_k - \overline{x}\right)^2,


$$

where

- $K$ is the number of groups,

- $n_k$ is the number of individuals in the $k$th group,

- $x_{jk}$ is the $j$th data point from the $k$th group,

- $\overline{x}_{k}$ is the sample mean of the $k$th group,

- $\overline{x}$ is the grand mean.

Now, if $s_k^2$ is the unbiased estimate of the population variance $\sigma^2$ obtained from the data in group $k$ only, then

$$


s_k^2 = \dfrac{1}{n_k-1}\sum_{j=1}^{n_k}\left(x_{jk} - \overline{x}_k\right)^2 \quad\Longrightarrow\quad (n_k-1)s_k^2 = \sum_{j=1}^{n_k}\left(x_{jk} - \overline{x}_k\right)^2.


$$

This means we can express $\text{SSW}$ in the following simplified form:

$$


\text{SSW} = \sum_{k=1}^K (n_k - 1)s_k^2


$$

Moreover, the total sum of squares is

$$


\text{SST} = (n-1)s^2,


$$

where

- $n$ is the grand sample size,

- $s^2$ is the grand (unbiased) estimate of the population variance $\sigma^2.$

In our case, since there are $3$ groups, we have $K=3,$ and we can compute SSW as follows:

$$


\begin{aligned}SSW & =(20−1)(3.2)^{2}+(24−1)(3.4)^{2}+(20−1)(3.8)^{2} \\ & =194.56+265.88+274.36 \\ & =734.8\end{aligned}


$$

Next, we have

$$


n = 20+24+20 = 64


$$

and therefore

$$


\text{SST} = (64-1)\cdot (15)=945.


$$

Now, let's now examine our statements:

- Computing the given ratio, we have

- We're interested in determining the between-group variability. First, recall that and therefore Therefore, Since a low proportion of the variability is ** groups, relatively high variability is attributable to differences ** the group means. In other words, this suggests the between-group variability is $\boxed{\color{blue}\text{low}}.$

### Degrees of Freedom

We now introduce the concept of **degrees of freedom** associated with our sums of squares statistics.

The degrees of freedom of a statistic is the number of independent data points used in its calculation, which is equal to the total number of data points appearing in its formula minus the number of constraints (or relationships) imposed on the data.

Let's discuss the number of degrees of freedom of our statistics $\text{SST},$ $\text{SSB},$ and $\text{SSW}{:}$

- The formula for $\text{SST}$ involves $n$ data points: However, the sample mean $\overline{x}$ introduces a constraint on the data. If all but one data point and the sample mean are known, the final data point can be determined. So, only $n-1$ data points are independent. Therefore, for the total sum of squares $(\text{SST}),$ the number of degrees of freedom is given by

- The formula for $\text{SSB}$ involves $K$ data points (the groups' sample means): However, as for $\text{SST},$ the sample mean $\overline{x}$ introduces a constraint on the data. If all but one group mean and the grand sample mean are known, the missing group mean can be determined. So, only $K-1$ group means are independent. Therefore, for the total sum of squares between the groups $(\text{SSB}),$ the number of degrees of freedom is given by

- The formula for $\text{SSW}$ involves $n$ data points: However, each group mean $\overline{x}_k$ introduces a constraint on the data. If all but one data point and the group mean are known within a single group, the missing data point can be determined. This happens for all groups. So, only $n-K$ data points are independent. Therefore, for the total sum of squares within the groups $(\text{SSW}),$ the number of degrees of freedom is given by

Finally, note that

$$


df_{T} = df_{B} + df_{W}.


$$

### Example: Degrees of Freedom

#### Question

Consider a sample containing $n=100$ elements partitioned into $K = 8$ groups. Determine the number of degrees of freedom $\text{SST}, \text{SSB},$ and $\text{SSW}.$

#### Explanation

We have a sample with the following information:

- The sample size is $n = 100$

- The number of groups is $K = 8$

Let's calculate the degrees of freedom for each of the sums of squares:

- For the total sum of squares $(\text{SST}),$ the number of degrees of freedom is given by

- For the total sum of squares between the groups $(\text{SSB}),$ the number of degrees of freedom is given by

- For the total sum of squares within the groups $(\text{SSW}),$ the number of degrees of freedom is given by

Note that $df_T = df_B + df_W.$

### MSB and MSW

We now define the following statistics:

- The **mean sum of squares between groups** $(\text{MSB})$ is given by

- The **mean sum of squares within groups** $(\text{MSW})$ is given by

By dividing our statistics $\text{SSB}$ and $\text{SSW}$ by their respective degrees of freedom, we obtain two measures of the average variation per independent data point.

### Example: Calculating MSW and MSB

#### Question

An environmental analyst wants to determine if there is a significant difference in the monthly water consumption of three residential areas. The following table gives the summary statistics of water consumption, in gallons, of households, each from a different area, where $n_k$ is the size of each sample, and $s_k$ is the (sample) standard deviation of each group.

What is the mean sum of squares within groups (MSW) for this sample?

#### Explanation

The sum of squares within groups $(\text{SSW})$ is given by

$$


\text{SSW} = \sum_{k=1}^K \sum_{j=1}^{n_k} \left(x_{jk} - \overline{x}_k\right)^2,


$$

where

- $K$ is the number of groups,

- $n_k$ is the number of individuals in the $k$th group,

- $x_{jk}$ is the $j$th data point from the $k$th group,

- $\overline{x}_{k}$ is the sample mean of the $k$th group,

Now, if $s_k^2$ is the unbiased estimate of the population variance $\sigma^2$ obtained from the data in group $k$ only, then

$$


s_k^2 = \dfrac{1}{n_k-1}\sum_{j=1}^{n_k}\left(x_{jk} - \overline{x}_k\right)^2 \quad\Longrightarrow\quad (n_k-1)s_k^2 = \sum_{j=1}^{n_k}\left(x_{jk} - \overline{x}_k\right)^2.


$$

This means we can express $\text{SSW}$ in the following simplified form:

$$


\text{SSW} = \sum_{k=1}^K (n_k - 1)s_k^2


$$

The mean sum of squares within the groups $(\text{MSW})$ is given by

$$


\text{MSW} = \dfrac{\text{SSW}}{df_W} = \dfrac{\text{SSW}}{n-K},


$$

where $df_W = n-K$ is the number of degrees of freedom for $\text{SSW},$ and $n$ is the total number of elements in our sample.

Since there are $3$ groups, we have $K=3,$ and we can compute SSW as follows:

$$


\begin{aligned}SSW & =(42−1)(3.3)^{2}+(52−1)(3.1)^{2}+(46−1)(3.2)^{2} \\ & =446.49+490.11+460.8 \\ & =1397.4\end{aligned}


$$

Also, we have

$$


n = 42+52+46 = 140.


$$

Therefore,

$$


\text{MSW} = \dfrac{1397.4}{140-3} = 10.2\,\text{gallons}^2.


$$

### Deriving the Relation Between SSW, SSB, SST

We now prove that

$$


\text{SSB} + \text{SSW} = \text{SST}.


$$

Let's consider $\text{SST}{:}$

$$


\text{SST} = \sum_{k=1}^K\sum_{j=1}^{n_k} (x_{jk} - \overline{x})^2


$$

First, we rewrite each term of $\text{SST}$ in a more convenient form by adding and subtracting $\overline{x}_k$ and expanding the square:

$$


\begin{aligned}(𝑥_{𝑗𝑘}−\overset{𝑥}{})^{2} & =(𝑥_{𝑗𝑘}−\overset{𝑥}{}_{𝑘}+\overset{𝑥}{}_{𝑘}−\overset{𝑥}{})^{2} \\ & =(𝑥_{𝑗𝑘}−\overset{𝑥}{}_{𝑘})^{2}+(\overset{𝑥}{}_{𝑘}−\overset{𝑥}{})^{2}+2(𝑥_{𝑗𝑘}−\overset{𝑥}{}_{𝑘})(\overset{𝑥}{}_{𝑘}−\overset{𝑥}{})\end{aligned}


$$

Now, we apply the summations to the three terms we've just obtained. Notice that the inner summation in the second term is constant, so this term can be simplified as follows:

$$


\begin{aligned}\underset{\underset{𝑘=1}{∑}}{\overset{}{𝐾}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛_{𝑘}}}(\overset{𝑥}{}_{𝑘}−\overset{𝑥}{})^{2} & =\underset{\underset{𝑘=1}{∑}}{\overset{}{𝐾}}𝑛_{𝑘}(\overset{𝑥}{}_{𝑘}−\overset{𝑥}{})^{2}\end{aligned}


$$

In the third term, we can move the constant $2$ outside the summations and the factor $(\overline{x}_k - \overline{x})$ outside the inner summation (it doesn't depend on $j$):

$$


\begin{aligned}2\underset{\underset{𝑘=1}{∑}}{\overset{}{𝐾}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛_{𝑘}}}(𝑥_{𝑗𝑘}−\overset{𝑥}{}_{𝑘})(\overset{𝑥}{}_{𝑘}−\overset{𝑥}{}) & =2\underset{\underset{𝑘=1}{∑}}{\overset{}{𝐾}}(\overset{𝑥}{}_{𝑘}−\overset{𝑥}{})\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛_{𝑘}}}(𝑥_{𝑗𝑘}−\overset{𝑥}{}_{𝑘})\end{aligned}


$$

Notice that the inner summation of the last expression

$$


\sum_{j=1}^{n_k} (x_{jk} - \overline{x}_k)


$$

equals zero, being a sum of the deviations from the sample mean.

Finally, we have

$$


\begin{aligned}SST & =\underset{\underset{𝑘=1}{∑}}{\overset{}{𝐾}}\underset{\underset{𝑗=1}{∑}}{\overset{}{𝑛_{𝑘}}}(𝑥_{𝑗𝑘}−\overset{𝑥}{}_{𝑘})^{2}+\underset{\underset{𝑘=1}{∑}}{\overset{}{𝐾}}𝑛_{𝑘}(\overset{𝑥}{}_{𝑘}−\overset{𝑥}{})^{2} \\ SST & =SSW+SSB.\end{aligned}


$$

as required.
