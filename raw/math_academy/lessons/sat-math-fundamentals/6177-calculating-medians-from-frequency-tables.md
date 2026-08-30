# Calculating Medians From Frequency Tables

Source: https://www.mathacademy.com/topics/6177?courseId=120
Topic ID: 6177

## Prerequisites

- [The Median of a Data Set](../grade-6/3749-the-median-of-a-data-set.md)
- [Cumulative Frequency](../grade-7/6187-cumulative-frequency.md)

## Lesson

### Introduction

It's often convenient to organize data in the form of a frequency table. We've also seen that the median of a data set gives a measure of its centrality. In this lesson, we'll learn how to calculate the median of a data set when presented as a frequency table.

To demonstrate, let's discuss how to compute the median of the data set given by the frequency table below.

If we were to write the data set out in full, we'd get the following:

$$


3, \qquad 3, \qquad 3, \qquad 3, \qquad 7, \qquad 10, \qquad 13,


$$

Notice that the data is ordered, and there are $7$ data points in total. Since $7$ is an odd number, the median is given by the $(7+1)/2 = 4$th element in the ordered list.

So, we count the elements from the left until we get to the $4$th element.

$$


3, \qquad 3, \qquad 3, \qquad {\color{blue}{\mathbf 3}}, \qquad 7, \qquad 10, \qquad 13,


$$

Since the $4$th element is $3,$ we conclude that

$$


\textrm{Median} = {\color{blue}\mathbf3}.


$$

The method of listing all the values in the data set becomes impractical when the frequencies are large. A more efficient way of doing this is to use *cumulative frequency.* We'll discuss this method next.

### Using Cumulative Frequency

Let's consider the same data set once more, but this time we'll use cumulative frequency to calculate the median.

We first need to construct the corresponding *cumulative frequency* table. So, let's start by adding another column to store our cumulative frequencies.

Recall that the cumulative frequency column shows the running total of the frequencies:

- For the first row, the cumulative frequency is simply equal to the frequency of that row.

- For each subsequent row, the cumulative frequency is found by adding the frequency of that row to the cumulative total from the previous row.

With that in mind, let's add the missing values in the cumulative frequency table.

Thus, the total number of values in the dataset is $7$ (the final cumulative frequency). Since our dataset has an odd number of data points, the median is the middle value in the following position:

$$


\begin{aligned}Median position & =\frac{7+1}{2} \\ & =\frac{8}{2} \\ & =4th\end{aligned}


$$

Now, let’s determine where the $4$th value falls. Looking at the cumulative frequency column in our table, we see that the first row of the table covers the first $4$ positions in total.

So, the $4$th position falls into the first row that corresponds to the value $3.$ Therefore, the median is

$$


\text{Median} = 3.


$$

In this example, the position we wanted (the $4$th position) coincided with a value in the cumulative frequency column. When this doesn't happen, we need to think a little more carefully about which value in the table to select as the median.

Let's see an example.

### Example: Calculating the Median With an Odd Number of Data Points

#### Question

A fitness coach records how many flights of stairs each participant climbs in a building. The cumulative frequency table below summarizes the data. Fill in the missing values in the table and determine the median number of stairs climbed.

#### Explanation

The cumulative frequency column shows the running total of the frequencies:

- For the first row, the cumulative frequency is simply equal to the frequency of that row.

- For each subsequent row, the cumulative frequency is found by adding the frequency of that row to the cumulative total from the previous row.

With that in mind, let's add the missing value in the cumulative frequency table.

Thus, the total number of values in the dataset is $11$ (the final cumulative frequency). Since our dataset has an odd number of data points, the median is the middle value in the following position:

$$


\begin{aligned}Median position & =\frac{11+1}{2} \\ & =\frac{12}{2} \\ & =6th\end{aligned}


$$

Now, let’s determine where the $6$th value falls. Looking at the cumulative frequency column in our table, we see the following:

- Up to the third row, the table covers $5$ positions in total.

- Up to the fourth row, the table covers $11$ positions in total.

So, the $6$th position falls into the fourth row that corresponds to the value $8$ (stairs climbed).

Therefore, the median number of stairs climbed is

$$


\text{Median} = \boxed{8}.


$$

### Even Number of Data Points

When a data set contains an even number of data points, the median is the mean of the two middle values.

To demonstrate how this works when the data are presented using a frequency table, consider the following cumulative frequency table.

The total number of values in the dataset is $10$ (the final cumulative frequency). Since $10$ is even, the median is the average of the two middle values in the following positions:

$$


\dfrac{10}{2} = 5\textrm{th} \qquad\text{and}\qquad 5+1 = 6\textrm{th}.


$$

Now, let’s determine where the $5$th and $6$th values fall. Looking at the cumulative frequency column in our table, we see the following:

- Up to the second row, the table covers $3$ positions in total.

- Up to the third row, the table covers $7$ positions in total.

So, the $5$th and $6$th positions both fall in the third row and correspond to the value $8.$

Therefore, the median is

$$


\begin{aligned}Median & =\frac{8+8}{2} \\ & =\frac{16}{2} \\ & =8.\end{aligned}


$$

When dealing with an even number of data points, we sometimes need to find the mean of values that lie in two separate groups! Let's see an example.

### Example: Calculating the Median With an Even Number of Data Points

#### Question

A group of volunteers reported how many hours they spent helping out during a weekend event. The cumulative frequency table below summarizes the data. Fill in the missing values in the table and determine the median number of volunteer hours.

#### Explanation

The cumulative frequency column shows the running total of the frequencies:

- For the first row, the cumulative frequency is simply equal to the frequency of that row.

- For each subsequent row, the cumulative frequency is found by adding the frequency of that row to the cumulative total from the previous row.

With that in mind, let's add the missing value in the cumulative frequency table.

Thus, the total number of values in the dataset is $20$ (the final cumulative frequency). Since our dataset has an even number of data points, the median is the average of the two middle values in the following positions:

$$


\dfrac{20}{2} = 10\textrm{th} \qquad\text{and}\qquad 10+1 = 11\textrm{th}


$$

Now, let’s determine where the $10$th and $11$th values fall. Looking at the cumulative frequency column in our table, we see the following:

- Up to the third row, the table covers $10$ positions in total.

- Up to the fourth row, the table covers $20$ positions in total.

So, we have that

- The $10$th value falls in the third row corresponding to the value $5$ (volunteer hours), and

- The $11$th value falls in the fourth row corresponding to the value $9$ (volunteer hours).

Therefore, the median is

$$


\begin{aligned}Median & =\frac{5+9}{2} \\ & =\frac{14}{2} \\ & =7\end{aligned}


$$

volunteer hours.

### Grouped Data

When data values are too numerous to list individually, we can group them into intervals and record how many fall into each. This arrangement is called a frequency table.

To analyze such data, we often extend the table with a cumulative frequency column, which helps locate measures like the median and quartiles. Let’s see how this works in the following example.

The frequency table above shows the number of values in a dataset that fall into each group. In which group does the median of the dataset lie?

First, notice that the cumulative frequency column shows the running total of the frequencies:

- For the first row, the cumulative frequency is simply equal to the frequency of that row.

- For each subsequent row, the cumulative frequency is found by adding the frequency of that row to the cumulative total from the previous row.

With that in mind, let's add the missing value in the cumulative frequency table.

Thus, the total number of values is ${\color{blue}17}.$ Since this is an odd number, the median is the value in the following position:

$$


\dfrac{{\color{blue}17} + 1}{2} = \dfrac{18}{2} = {\color{red}9\textrm{th}}


$$

Now we determine where the $9$th value falls. Looking at the cumulative frequency column in our table, we see the following:

- Up to the third row, the table covers $8$ positions in total.

- Up to the fourth row, the table covers $12$ positions in total.

Therefore, the $9$th value falls in the **fourth** interval, which is

$$


{\color{red}84-88}.


$$

### Example: Determining the Location of the Median for Grouped Data

#### Question

The frequency table above shows how many values from a dataset fall into each group. Which of the following values could be the median of the dataset?

1. $25$

2. $31$

3. $34$

#### Explanation

The cumulative frequency column shows the running total of the frequencies:

- For the first row, the cumulative frequency is simply equal to the frequency of that row.

- For each subsequent row, the cumulative frequency is found by adding the frequency of that row to the cumulative total from the previous row.

With that in mind, let's add a cumulative frequency column and fill in the values.

There are $26$ total values in the dataset. Since this is an even number, the median is the average of the values in the following positions:

$$


\dfrac{26}{2} = 13\textrm{th} \qquad \text{and} \qquad 13 + 1 = 14\textrm{th}


$$

Now we determine where the $13$th and $14$th values fall. Looking at the cumulative frequency column in our table, we see the following:

- Up to the third row, the table covers $13$ positions in total.

- Up to the fourth row, the table covers $20$ positions in total.

So, we have that

- the $13$th value falls in the third row corresponding to the group $30-33,$ while

- the $14$th value falls in the fourth row corresponding to the group $33-36.$

The median could fall in either of these groups. Of the given options:

- Option I, $25,$ doesn't fall within either group $30-33$ or $33-36,$ so cannot be the median.

- Option II, $31,$ falls within the group $30-33,$ so could be the median.

- Option III, $34,$ falls within the group $33-36,$ so could be the median.

Therefore, the correct answer is "II and III only".
