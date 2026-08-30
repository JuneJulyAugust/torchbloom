# Range, Quartiles, and IQR

Source: https://www.mathacademy.com/topics/2480?courseId=120
Topic ID: 2480

## Prerequisites

- [The Median of a Data Set](../grade-6/3749-the-median-of-a-data-set.md)

## Lesson

### Introduction

The **range** of a data set is the difference between the greatest and smallest values in the data set.

To demonstrate, let's find the range of the following data set:

$$


2, \: 3, \: 3, \: 6, \: 7, \: 9


$$

Notice that our data set is already arranged from smallest to greatest.

The smallest value is $\color{red}2$ and the greatest is ${\color{blue}9}\mathbin{:}$

$$


{\color{red}\underline{2}}, \: 3, \: 3, \: 6, \: 7, \: {\color{blue}\underline{9}}


$$

Therefore, the range of the data set is:

$$


{\color{blue}\text{greatest}} - {\color{red}\text{smallest}} = {\color{blue}9} - {\color{red}2} = 7


$$

### Example: Finding the Range

#### Question

Suppose that the temperatures registered yesterday in the southwest of the United States were as follows:

$$


19^\circ\text{C}, \quad 29^\circ\text{C}, \quad 15^\circ\text{C}, \quad 12^\circ\text{C}, \quad 16^\circ\text{C}, \quad 26^\circ\text{C}, \quad 29^\circ\text{C}


$$

What is the range of temperatures?

#### Explanation

Our data set is not arranged from smallest to greatest. So, let's first order the numbers:

$$


12, \: 15, \: 16, \: 19, \: 26, \: 29, \: 29


$$

Now, we see that the smallest value is $\color{red}12$ and the greatest is ${\color{blue}29} \mathbin{:}$

$$


{\color{red}\underline{12}}, \: 15, \: 16, \: 19, \: 26, \: 29, \: {\color{blue}\underline{29}}


$$

Therefore, the range of the data set is:

$$


{\color{blue}\text{greatest}} - {\color{red}\text{smallest}} = {\color{blue}29} - {\color{red}12} = 17


$$

So, the range of temperatures is $17^{\circ}\text{C}.$

### Lower and Upper Quartiles

To compute the **lower quartile** and **upper quartile** of a data set, we first need to order the data set from smallest to greatest and then split the data set into two halves: the half below the median and the half above the median. Then,

- the **lower quartile** is the median of the lower half, and

- the **upper quartile** is the median of the upper half.

For example, consider the following data set:

$$


7, \: 13, \: 15, \: 21, \: 24, \: 29


$$

Notice that our data set is already arranged from smallest to greatest.

The lower half is what's below the median, and the upper half is what's above the median:

$$


\underbrace{7, \: 13, \: 15}_{\text{lower half}}, \: \underbrace{21, \: 24, \: 29}_{\text{upper half}}


$$

To find the lower quartile, we find the median of the lower half:

$$


7, \: {\color{blue}\underline{13}}, \: 15


$$

So, the lower quartile is ${\color{blue}{13}}.$

Now, to find the upper quartile, we find the median of the upper half:

$$


21, \: {\color{red}\underline{24}}, \: 29


$$

So, the upper quartile is ${\color{red}{24}}.$

### Example: Finding the Lower or Upper Quartile: Even Number of Elements

#### Question

Arthur recorded how many hours he worked per day each day over a period of $6$ days and got the following data:

$$


7, \: 5, \: 6, \: 7, \: 6, \: 8


$$

Find the lower quartile of this data set.

#### Explanation

Our data set is not arranged from smallest to greatest. So, let's first order the numbers:

$$


5, \: 6, \: 6, \: 7, \: 7, \: 8


$$

Now, we consider the lower half of the data:

$$


\underbrace{5, \: 6, \: 6,}_{\text{lower half}} \: 7, \: 7, \: 8


$$

Next, we find the median of the lower half. In this case, it's the middle number:

$$


5, \: {\color{blue}\underline{6}}, \:6


$$

So, the lower quartile is $\boxed{\color{blue}6}.$

### Example: Finding the Lower or Upper Quartile: Odd Number of Elements

#### Question

Marlon asked his friends about their weights and got the following data (in kilograms):

$$


63.2, \: 50, \: 48.4, \: 45.6, \: 45, \: 55, \: 58.9, \: 92.1, \: 88


$$

What is the lower quartile of the given data set?

#### Explanation

Our data set is not arranged from smallest to greatest. So, let's first order the numbers:

$$


45, \: 45.6, \: 48.4, \: 50, \: 55, \: 58.9, \: 63.2, \: 88, \: 92.1


$$

The median of the data set is the middle number ($\color{blue}55$).

Now, we consider the lower half of the data:

$$


\underbrace{45, \: 45.6, \: 48.4, \: 50,}_{\text{lower half}} \: {\color{blue}55}, \: 58.9, \: 63.2, \: 88, \: 92.1


$$

We want to find the lower quartile, so we need to find the median of the lower half. In this case, it's the mean of the two middle numbers:

$$


45, \: {\color{red}\underline{45.6}}, \: {\color{red}\underline{48.4}}, \: 50


$$

So, the lower quartile is:

$$


\dfrac{{\color{red}45.6}+{\color{red}48.4}}{2} = \dfrac{94}{2} = 47


$$

### Interquartile Range

The **interquartile range (IQR)** of a data set is the difference between its upper and lower quartiles.

For example, suppose that the lower and upper quartiles of a data set are $3.8$ and $6$, respectively.

Then to find the interquartile range, we take the difference:

$$


\text{IQR} = \text{upper quartile} - \text{lower quartile} = 6 - 3.8 = 2.2


$$

Therefore, the interquartile range is $2.2.$

### Example: Finding the Interquartile Range

#### Question

What is the interquartile range of the data set below?

$$


19, \: 21, \: 21, \: 25, \: 28, \: 33, \: 36


$$

#### Explanation

Notice that our data set is already arranged from smallest to greatest.

The median of the data set is the middle number ($\color{blue}25$), so the lower and upper halves of the data set are as follows:

$$


\underbrace{19, \: 21, \: 21,}_{\text{lower half}} \: {\color{blue}{25}}, \: \underbrace{28, \: 33, \: 36}_{\text{upper half}}


$$

The lower quartile is the median of the lower half:

$$


19, \: {\color{red}\underline{21}}, \: 21


$$

So, the lower quartile is $21.$

Likewise, the upper quartile is the median of the upper half:

$$


28, \: {\color{red}\underline{33}}, \: 36


$$

So, the upper quartile is $33.$

Finally, the interquartile range of the data set is:

$$


\text{IQR} = \text{upper quartile} - \text{lower quartile} = 33 - 21 =12


$$
