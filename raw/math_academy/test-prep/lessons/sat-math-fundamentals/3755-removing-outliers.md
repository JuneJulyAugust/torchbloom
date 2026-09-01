# Removing Outliers

Source: https://www.mathacademy.com/topics/3755?courseId=120
Topic ID: 3755

## Prerequisites

- [Range, Quartiles, and IQR](../../../middle-school/lessons/grade-6/2480-range-quartiles-and-iqr.md)
- [Mean Absolute Deviation](../../../middle-school/lessons/grade-6/2481-mean-absolute-deviation.md)
- [Outliers](../../../middle-school/lessons/grade-6/2517-outliers.md)

## Lesson

### Introduction

Outliers can affect the mean in a way that sometimes distorts its interpretation. For this reason, we might consider removing outliers from a data set before computing the mean.

For example, consider the following data set, which gives the heights (in feet) of a group of saplings:

$$


5, \quad 5.5, \quad {\color{blue}\underline{1}}, \quad 4.5, \quad 5


$$

The value $\color{blue}1$ is an outlier because it is much smaller than all the other values:

Now, if we compute the data set's mean without removing the outlier, we get a result of $4.2$ feet:

$$


\begin{aligned}mean & =\frac{5+5.5+1+4.5+5}{5} \\ & =\frac{21}{5} \\ & =4.2\end{aligned}


$$

However, we can see by inspecting the data that most saplings are around $5$ feet tall. Thus, the outlier has caused some distortion, and the mean can no longer be considered truly representative of most of the data points in the sample.

So instead, let's remove the outlier from the data set:

$$


5, \quad 5.5, \quad 4.5, \quad 5


$$

Calculating the mean of the updated data set, we get

$$


\begin{aligned}mean & =\frac{5+5.5+4.5+5}{4} \\ & =\frac{20}{4} \\ & =5.\end{aligned}


$$

By computing the mean with the updated data set, we get a result of $5$ feet, which is more representative of the data overall.

In general:

- If we remove an outlier *smaller* than all other values, the center of the data will shift towards a bigger number, so the mean will *increase*.

- If we remove an outlier *greater* than all other values, the center of the data will shift towards a smaller number, so the mean will *decrease*.

### Example: Predicting the Effect of Removing Outliers on the Mean

#### Question

Consider the following data set:

$$


500, \quad 460, \quad 675, \quad 583, \quad 50, \quad 690, \quad 568


$$

Which of the following statements are true?

1. The value $50$ is an outlier of the data set.

2. There is one outlier, and it is much smaller than all the other values of the data set.

3. If the outlier were removed, the mean of the data would decrease.

#### Explanation

In general:

- If we remove an outlier ** than all other values, the center of the data will shift towards a bigger number, so the mean will **.

- If we remove an outlier ** than all other values, the center of the data will shift towards a smaller number, so the mean will **.

With that in mind, let's examine the statements one-by-one.

- Statements I and II are true. An outlier is a value that is much larger or smaller than all other values. The value $\color{blue}50$ is much smaller than all the other values. So, $\color{blue}50$ is an outlier.

- Statement III is false. If we remove an outlier that is much smaller than all other values in the data set, the center of the data will shift towards a bigger number. So, the mean will increase.

Therefore, the correct answer is "I and II only."

### The Effect of Outliers on the Range

Outliers can also affect our interpretation of a data set's range.

To demonstrate, let's go back to the sample data for the group of saplings:

$$


5, \quad 5.5, \quad {\color{blue}\underline{1}}, \quad 4.5, \quad 5


$$

Let's compute the range of this data set:

- Computing the range of the data set without removing the outlier, we get a result of $4.5$ feet:

- However, if we *remove* the outlier, we get a result of $1$ foot.

Outliers have a significant effect on the range. Therefore, removing outliers when computing the range is often a good idea.

In general, the range of a data set will always *decrease* if outliers are removed.

### The Effect of Outliers on the Mean Absolute Deviation

Outliers can also affect our interpretation of a data set's mean absolute deviation (MAD).

Let's reconsider the sample data for the group of saplings:

$$


5, \quad 5.5, \quad1, \quad 4.5, \quad 5


$$

Let's compute the MAD of this data set both with and without the outlier:

- As we saw earlier, the mean of the data set that includes the outlier is ${\color{blue}{4.2}}$ feet. Computing the MAD, we get

- The mean of the data set that excludes the outlier is ${\color{red}{5}}$ feet. Computing the MAD, we get

As with the range, outliers have a significant effect on the MAD. Therefore, removing outliers in such cases is often a good idea as doing so gives a result that better represents the spread of most of the data.

In general, the MAD of a data set will always *decrease* if outliers are removed.

### Example: Predicting the Effect of Removing Outliers on the Range and MAD

#### Question

Fred and Jill recorded the distances, in miles, from home to school for $12$ students in their class. The data is given below:

$$


4.2, \quad 4.5, \quad 4.2, \quad 4.3, \quad 4.3, \quad 5.4, \quad 5.8, \quad 0.2, \quad 5.6 , \quad 5.5, \quad 6.2, \quad 6.2


$$

Fred removed the outlier from the data and computed both the range and the mean absolute deviation (MAD). Jill did the same, except she kept the outlier.

Which of the following are true statements?

1. The value of $0.2$ miles is an outlier of the data set.

2. Fred's mean absolute deviation is smaller than Jill's.

3. Fred's range is larger than Jill's.

#### Explanation

Let's examine the statements one by one.

- Statement I is true. An outlier is a value that is much larger or smaller than all other data set values. The value $\color{blue}0.2$ is much smaller than all the other values in the data set. So $\color{blue}0.2$ is an outlier.

- Statement II is true, while statement III is false. Removing an outlier makes the spread of the remaining data smaller. So Fred's MAD should be smaller than Jill's. For the same reason, Fred's range should be smaller than Jill's.

Therefore, the correct answer is "I and II only."

### Final Remark

In this lesson, we've explored how the mean, range, and mean absolute deviation are affected when outliers are removed from a data set. As we've seen, outliers can significantly affect these measures of center and spread.

However, we haven't yet discussed how the median, quartiles, interquartile range, and mode are affected when we remove outliers.

As it turns out, the median, quartiles, interquartile range, and mode are **resistant to outliers**, which means that the presence of outliers does not drastically alter their values. For this reason, assessing the center and spread of a data set might be preferable using these measures when outliers are present.

There are other reasons we might prefer to use median, quartiles, interquartile range, and mode to assess a data set. We'll explore these ideas in more detail in a future lesson.
