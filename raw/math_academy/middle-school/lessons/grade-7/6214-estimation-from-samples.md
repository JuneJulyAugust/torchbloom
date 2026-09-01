# Estimation From Samples

Source: https://www.mathacademy.com/topics/6214?courseId=37
Topic ID: 6214

## Prerequisites

- [Joint Frequency Tables](./1498-joint-frequency-tables.md)
- [Finding Part of a Number Given a Whole and a Percentage: Word Problems](../prealgebra/2454-finding-part-of-a-number-given-a-whole-and-a-percentage-word-problems.md)
- [The Median of a Data Set](../prealgebra/3749-the-median-of-a-data-set.md)
- [Sampling](./6216-sampling.md)

## Lesson

### Introduction

When we have data from a random sample, we can use this data to *estimate* (or **infer**) characteristics of the population from which the sample was drawn.

For example, suppose there are $500$ employees at a company. A random sample of employees was conducted, and each participant was asked if they planned to attend the upcoming industry conference. Of those surveyed, $62\%$ responded that they planned to attend.

From this sample, we can *estimate* how many employees in the *entire company* plan to attend by applying the sample percentage ($62\%$) to the total population ($500$):

$$



\begin{aligned}500⋅62\% & =500⋅0.62 \\ & =310\end{aligned}



$$

Therefore, our **best estimate** is that $310$ employees plan to attend the conference.

It's important to note that this is an *estimate* of the total number of employees who plan to attend the conference, and the exact number *may differ from this!* We'll discuss this at more length in a future lesson.

Finally, please note that, throughout this lesson, all samples will be carried out by *randomly selecting* units from the population to reduce sample bias.

### Example: Making Population Inferences From Sample Proportions

#### Question

A regional road race has $19{,}600$ registered runners. A random sample of runners was surveyed, and each participant was asked whether they plan to purchase official race merchandise. Of those surveyed, $47\%$ responded that they plan to purchase merchandise.

Based on this survey, which of the following is the best estimate of the total number of runners who plan to purchase merchandise? Round your answer to the nearest $500.$

#### Explanation

We are told that there are $19{,}600$ runners in total, and the sample suggests that $47\%$ plan to purchase merchandise. To estimate the total number who plan to purchase, we compute $47\%$ of $19{,}600$:

$$



\begin{aligned}19,600⋅47\% & =19,600⋅0.47 \\ & =9,212.\end{aligned}



$$

We must round to the nearest $500,$ which is $9{,}000$.

Therefore, the best estimate is $9{,}000$ runners.

### Example: Making Population Inferences From Sample Data

#### Question

A neighborhood has $320$ houses. A random sample of $40$ houses was taken, and among those surveyed, $25$ had a garden.

Based on the sample data, which of the following is the best estimate of the total number of houses in the neighborhood that have a garden?

#### Explanation

We are told there are $320$ houses in the neighborhood. In a sample of $40$ houses, $25$ had a garden.

First, we find the proportion of houses in the sample that have a garden. Since $25$ houses out of a sample of $40$ have a garden, the required proportion is

$$



\frac{25}{40} = 0.625 = 62.5\%.



$$

So, $62.5\%$ of the houses in our sample have a garden.

Finally, to estimate the number in the whole neighborhood that hava a garden, we multiply the total number of houses by $62.5\%$:

$$



320 \cdot 0.625 = 200.



$$

Therefore, the best estimate is that $200$ houses have a garden.

### Example: Making Inferences From Sample Data in Tabular Form

#### Question

A corporation randomly sampled $500$ employees about next year’s health insurance. The results were categorized by work arrangement and are shown below.

The corporation has $34{,}000$ employees in total. Based on the table, what is the best estimate of the number of employees who plan to choose Health Plan A?

#### Explanation

First, we total the number in the sample who plan to choose Plan A:

$$



110 + 140 = 250.



$$

Out of the $500$ people surveyed, the proportion who favor Plan A is

$$



\frac{250}{500} = 0.5 = 50\%.



$$

Therefore, $50\%$ of those sampled intend to choose Plan A.

To estimate how many of the $34{,}000$ employees favor Plan A, we scale the proportion by the population:

$$



\begin{aligned}34,000⋅50\% & =34,000⋅0.5 \\ & =17,000.\end{aligned}



$$

Therefore, the best estimate is that $17{,}000$ employees plan to choose Health Plan A.

### Inferring Results Using Centrality Measures

When estimating values for an entire population, we can use measures of centrality, such as the mean or median, from a random sample to make reasonable predictions about the population.

Let's explore this through a real-world scenario.

Suppose a botanical center has $420$ garden beds. To estimate the total number of flowering plants, a horticulturist randomly selects $5$ different beds and counts the number of flowering plants in each. The results are given below:

$$



34, \: 31, \: 29, \: 33, \: 32



$$

Based on the *mean* of the sample, we can find an *estimate* for the total number of flowering plants in the botanical center.

First, we find the mean number of flowering plants per bed in the sample. The total number in the $5$ sampled beds is

$$



34 + 31 + 29 + 33 + 32 = 159.



$$

Dividing by the $5$ beds gives a sample mean of

$$



\frac{159}{5} = 31.8.



$$

This suggests an average of $31.8$ flowering plants per bed.

Now, to estimate the total number of flowering plants in the center, we multiply the mean by the total number of flower beds:

$$



31.8 \cdot 420 = 13{,}356



$$

Therefore, our best estimate for the number of flower beds is $13{,}356.$

Since our best estimate is still an estimate, the number $13{,}356$ seems a little too precise. It's often more practical to bound this estimate between two reasonable wholes, say, the nearest multiples of $500.$

Since $13{,}356$ lies between $13{,}000$ and $13{,}500,$ we say that the best estimate of the number of flowering plants falls in the range $13{,}000$ to $13{,}500.$

Let's now take a look at a similar example where we use the *median* of the sample.

### Example: Making Inferences From Sample Data Using Centrality

#### Question

A coach wants to estimate the typical finish time of participants in a 10K race series. Over several years, $200$ races have been held. The coach randomly selects $7$ races and records the winning times (in minutes): $52$, $48$, $55$, $50$, $60$, $53$, and $58.$

Based on the **** of the sample, which of the following ranges contains the best estimate for the total combined finish time of all $200$ races?

1. $10{,}000$ to $10{,}500$

2. $10{,}500$ to $11{,}000$

3. $11{,}000$ to $11{,}500$

#### Explanation

First, we list the sample times in order from least to greatest:

$$



48,\ 50,\ 52,\ 53,\ 55,\ 58,\ 60



$$

Since there are $7$ values, the median is the middle value, which is the $4$th number in the list:

$$



\text{Median} = 53



$$

This suggests a typical race finish time of $53$ minutes.

To estimate the total combined finish time over all $200$ races, we multiply the median by the total number of races:

$$



53 \cdot 200 = 10{,}600



$$

The number $10{,}600$ lies between $10{,}500$ and $11{,}000.$ Therefore, the best estimate falls in the range $10{,}500$ to $11{,}000.$
