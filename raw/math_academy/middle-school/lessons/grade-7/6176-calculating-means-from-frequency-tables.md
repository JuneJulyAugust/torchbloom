# Calculating Means From Frequency Tables

Source: https://www.mathacademy.com/topics/6176?courseId=37
Topic ID: 6176

## Prerequisites

- [Solving Rational Equations Containing One Fractional Term](./1415-solving-rational-equations-containing-one-fractional-term.md)
- [The Mean of a Data Set](../prealgebra/2479-the-mean-of-a-data-set.md)
- [Frequency Tables](../prealgebra/2509-frequency-tables.md)

## Lesson

### Introduction

We've seen how it's often convenient to organize data in the form of a frequency table. We've also seen that the mean of a data set gives a measure of its centrality. In this lesson, we'll learn how to calculate the mean of a data set when presented as a frequency table.

To demonstrate, let's discuss how to compute the mean of the data set given by the frequency table below.

If we were to write the data set out in full, we'd get the following:

$$



0,\:\: 0, \:\: 1, \:\: 1, \:\: 1, \:\: 1, \:\: 2, \:\: 2, \:\: 3, \:\: 3, \:\: 3, \:\: 3, \:\: 3, \:\: 3



$$

Notice that we have $14$ data points in total. So, to calculate the mean, we must sum these values and then divide the result by $14.$

We can make the computation a little faster by taking advantage of the repetition in the data set. Since the value $0$ occurs twice, $1$ occurs four times, $2$ occurs twice, and $3$ occurs six times, we can calculate the mean as follows:

$$



\begin{aligned}Mean & =\frac{0⋅2+1⋅4+2⋅2+3⋅6}{14} \\ & =\frac{0+4+4+18}{14} \\ & =\frac{26}{14} \\ & ≈1.86.\end{aligned}



$$

Notice that this is the same as multiplying the value in each row by its respective frequency, summing the results for each row, and then dividing by the total number of data points.

### Computing the Mean in Stages

When calculating the mean, it's easy to make a mistake when the frequency table is large or contains big numbers. For that reason, it's useful to proceed in stages.

Let's consider the same data set once more, but this time we'll proceed in stages.

We begin by extending the table to include a third column for the product of each value and its frequency. We'll denote each possible value in the table by $x$ and the associated frequency $f_x,$ as shown below.

Next, we calculate the product $x\cdot f_x$ in each row.

We now calculate the mean by dividing the sum of these products by the total number of data points, given by the total sum of the frequencies:

$$



\begin{aligned}Mean & =\frac{0+4+4+18}{2+4+2+6} \\ & =\frac{26}{14} \\ & ≈1.86\end{aligned}



$$

### Example: Calculating the Mean From a Frequency Table

#### Question

Families were asked how many trays of cookies they baked during a holiday weekend. The table above summarizes the responses. What is the mean number of trays of cookies baked per family?

#### Explanation

To calculate the mean of a dataset given in a frequency table, we compute the sum of the products of each value $x$ and its corresponding frequency $f_x,$ and then divide that sum by the total number of data points.

We begin by extending the table to include a third column for the product of each value and its frequency:

We now calculate the mean by dividing the sum of these products by the total number of data points, given by the total sum of the frequencies:

$$



\begin{aligned}Mean & =\frac{27+24+110+15+64}{9+6+10+1+4} \\ & =\frac{240}{30} \\ & =8\end{aligned}



$$

Therefore, the mean number of trays of cookies baked per family is $8.$

### Calculating a Missing Frequency

Now that we've learned how to calculate the mean of a data set from a frequency table, let's consider how we'd calculate a missing frequency given the mean of a data set.

Consider the frequency table below, where the frequency associated with the value $x=9$ is unknown.

Suppose we're given that the mean of the dataset is $10.$ How can we use this to find the missing frequency?

To find the missing frequency, let's first extend the table to include a third column for the product of each value and its frequency, as before.

Notice that we've denoted the missing frequency as $f_9.$

Now, we find an expression for the mean by dividing the sum of these products by the total number of data points:

$$



\begin{aligned}Mean & =\frac{4+12+9𝑓_{9}+117}{2+2+𝑓_{9}+9} \\ & =\frac{133+9𝑓_{9}}{13+𝑓_{9}}\end{aligned}



$$

We are told that the mean of the dataset is $10.$ So, we must have

$$



\dfrac{133 + 9f_{9}}{13 + f_{9}} = 10.



$$

To compute the missing frequency, we must solve this rational equation.

First, we eliminate the denominator by multiplying both sides by $(13 + f_{9})$ before solving for $f_{9}{:}$

$$



\begin{aligned}133+9𝑓_{9} & =10(13+𝑓_{9}) \\ 133+9𝑓_{9} & =130+10𝑓_{9} \\ 9𝑓_{9}−10𝑓_{9} & =130−133 \\ −𝑓_{9} & =−3 \\ 𝑓_{9} & =3\end{aligned}



$$

Now that we know the missing frequency, we can complete the table.

### Example: Calculating a Missing Frequency Given the Mean

#### Question

The incomplete frequency table below shows how many days guests stayed at a mountain lodge.

If the mean number of days stayed was $12,$ how many guests stayed for $14$ days?

#### Explanation

To find the missing frequency, we can find an expression for the mean in terms of the missing frequency.

We first extend the table to include a third column for the product of each value and its frequency:

Now, we find an expression for the mean by dividing the sum of these products by the total number of data points:

$$



\begin{aligned}Mean & =\frac{2+4+12+14𝑓_{14}}{2+2+2+𝑓_{14}} \\ & =\frac{18+14𝑓_{14}}{6+𝑓_{14}}\end{aligned}



$$

We are told that the mean of the dataset is $12.$ So, we must have

$$



\dfrac{18 + 14f_{14}}{6 + f_{14}} = 12.



$$

Then, we eliminate the denominator by multiplying both sides by $(6 + f_{14}),$ before solving for $f_{14}\mathbin{:}$

$$



\begin{aligned}18+14𝑓_{14} & =12(6+𝑓_{14}) \\ 18+14𝑓_{14} & =72+12𝑓_{14} \\ 14𝑓_{14}−12𝑓_{14} & =72−18 \\ 2𝑓_{14} & =54 \\ 𝑓_{14} & =27\end{aligned}



$$

Therefore, a total of $27$ guests stayed for $14$ days.

### Estimating Means From Grouped Data

When a frequency table contains grouped data, we cannot get an exact value for the mean because we don't have access to the full data set. However, we can *estimate* the mean using a similar method to what we saw before.

To demonstrate, let's estimate the mean of the data set represented by the frequency table below.

Since the data is grouped, we start by introducing $x_{\text{mid}},$ the middle value of $x$ for each group.

To calculate $x_{\text{mid}}$ for each group, we simply calculate the mean of the values on the boundary of each group.

For example, the first group is $60-62.$ The boundary values are $60$ and $62,$ and so finding the mean of these values, we get

$$



x_{\text{mid}} = \dfrac{60+62}{2} = 61



$$

and we add this to our table.

If we calculate $x_{\text{mid}}$ for all groups, we get the following:

Then, we introduce a new column $f\cdot x_{\text{mid}},$ and calculate this quantity for each row.

Therefore, our estimate of the mean is

$$



\begin{aligned}Mean & =\frac{183+441+130+402+414}{3+7+2+6+6} \\ & =\frac{1570}{24} \\ & =65.4.\end{aligned}



$$

### Example: Calculating the Mean From a Frequency Table Containing Grouped Data

#### Question

The table below shows the distribution of **** recorded at a track meet. Estimate the mean lap time.

#### Explanation

To estimate the mean from grouped data, we first use the frequency table.

Since the data is grouped, we record $x_{\text{mid}},$ the middle value of $x$ for each group. Then, we calculate $f\cdot x_{\text{mid}}$ for each row.

Therefore, our estimate of the mean is

$$



\begin{aligned}Mean & =\frac{36+55+78+45+34}{4+5+6+3+2} \\ & =\frac{248}{20} \\ & =12.4.\end{aligned}



$$

Therefore, the mean lap time is approximately $12.4$ minutes.
