# Multi-Digit by Two-Digit Multiplication

Source: https://www.mathacademy.com/topics/2288?courseId=30
Topic ID: 2288

## Prerequisites

- [Two-Digit by Two-Digit Multiplication](./258-two-digit-by-two-digit-multiplication.md)

## Lesson

### Introduction

We can use the standard algorithm when we want to multiply a three-digit number by a two-digit number.

As an example, let's find $706 \times 25.$ As always, we write the problem down in the following way:

$$
\begin{aligned} & \begin{aligned} & & & & & \\ & & & \,\,\,\,7\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,6\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,5\,\,\,\, \\ & & & & & \end{aligned} & \,\, & \begin{aligned}3,530+14,120=17,650\end{aligned} \\ & & & \end{aligned}
$$

First, we multiply the top number ($706$) by the ones digit of the second ($\bbox[2px, lightgray]{5}$).

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}3[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,7\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,6\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,\,5\,\,\,\, \\ & & \,\,\,\,3\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,0\,\,\,\,\end{aligned} & \,\, & \begin{aligned}706×5=3,530000000,\end{aligned}\end{aligned}
$$

Next, we multiply top number ($706$) by $\bbox[2px, lightgray]{2}0.$ Let's do this in steps:

**Step 1**: We add a zero underneath the result of the first calculation, in the ones place:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}3[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,7\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,6\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,\,2\,\,\,\, & \,\,\,\,5\,\,\,\, \\ & & \,\,\,\,3\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,0\,\,\,\, \\ & \,\,\,\,1\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,0\,\,\,\,\end{aligned} & \,\, & \begin{aligned}706×20=14,1200000,\end{aligned}\end{aligned}
$$

**Step 2**: We continue to work out $706\times \bbox[2px, lightgray]{2}0,$ proceeding as usual:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}\phantom{0}[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}3[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,7\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,6\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,\,2\,\,\,\, & \,\,\,\,5\,\,\,\, \\ & & \,\,\,\,3\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,0\,\,\,\, \\ & \,\,\,\,1\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,0\,\,\,\,\end{aligned} & \,\, & \begin{aligned}706×20=14,1200000,\end{aligned}\end{aligned}
$$

Finally, we add the results:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}\phantom{0}[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}3[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,7\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,6\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,5\,\,\,\, \\ & & \,\,\,\,3\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,0\,\,\,\, \\ \,\,\,\,+\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,0\,\,\,\, \\ & \,\,\,\,1\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,0\,\,\,\,\end{aligned} & \,\, & \begin{aligned}3,530+14,120=17,650\end{aligned} \\ & & & \end{aligned}
$$

Therefore, $706 \times 25 = 17, 650.$

### Example: Multiplying Three-Digit Numbers by Two-Digit Numbers

#### Question

What is $268$ multiplied by $54?$

#### Explanation

We write it this way:

$$
\begin{aligned} & \begin{aligned} & & & & & \\ & & & \,\,\,\,2\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,8\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,4\,\,\,\, \\ & & & & & \end{aligned} & \,\, & \,1,072+13,400=14,472\end{aligned}
$$

First, we multiply the ones:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}2[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}3[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,2\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,8\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,4\,\,\,\, \\ & & \,\,\,\,1\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,2\,\,\,\,\end{aligned} & \,\, & \begin{aligned}268×4=1,0720000000\end{aligned}\end{aligned}
$$

Next, we multiply the tens:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}3[/math] \\ [math]\color{blue}2[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}4[/math] \\ [math]\color{blue}3[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,2\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,8\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,4\,\,\,\, \\ & & \,\,\,\,1\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,2\,\,\,\, \\ & \,\,\,\,1\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\,\end{aligned} & \,\, & \begin{aligned}268×50=13,4000000,\end{aligned}\end{aligned}
$$

Finally, we add the results:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}3[/math] \\ [math]\color{blue}2[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}4[/math] \\ [math]\color{blue}3[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,2\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,8\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,4\,\,\,\, \\ & & \,\,\,\,1\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,2\,\,\,\, \\ \,\,\,\,+\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, \\ & \,\,\,\,1\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,2\,\,\,\,\end{aligned} & \,\, & \begin{aligned}1,072+13,400=14,472\end{aligned} \\ & & & \end{aligned}
$$

Therefore, $268 \times 54 = 14, 472.$

### Multiplying Larger Numbers by Two-Digit Numbers

There is no limit to the size of the numbers that we can multiply using the standard algorithm.

For example, to calculate $6,132 \times 54$, we write it this way:

$$
\begin{aligned} & \begin{aligned} & & & & & & \\ & & & \,\,\,\,6\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,2\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,4\,\,\,\, \\ & & & & & & \end{aligned} & \,\, & \,4,859+97,180=102,039\end{aligned}
$$

First, we multiply the ones:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,6\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,2\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,\,4\,\,\,\, \\ & & \,\,\,\,2\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,8\,\,\,\,\end{aligned} & \,\, & \begin{aligned}6,132×4=24,528\,0000000\end{aligned}\end{aligned}
$$

Next, we multiply the tens:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}\phantom{0}[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,6\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,2\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,\,5\,\,\,\, & \,\,\,\,4\,\,\,\, \\ & & \,\,\,\,2\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,8\,\,\,\, \\ & \,\,\,\,3\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\,\end{aligned} & \,\, & \begin{aligned}6,132×50=306,6000\,0000\end{aligned}\end{aligned}
$$

Finally, we add the results:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}\phantom{0}[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,6\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,2\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,\,5\,\,\,\, & \,\,\,\,4\,\,\,\, \\ & & \,\,\,\,2\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,8\,\,\,\, \\ & \,\,\,\,3\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, \\ & \,\,\,\,3\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,8\,\,\,\,\end{aligned} & \,\, & \begin{aligned}24,528+306,600=331,128\end{aligned} \\ & & & \end{aligned}
$$

Therefore, $6,132 \times 54 = 331, 128.$

### Example: Multiplying Four-Digit Numbers by Two-Digit Numbers

#### Question

Find the value of $2,324\times 46.$

#### Explanation

We write it this way:

$$
\begin{aligned} & \begin{aligned} & & & & & & \\ & & & \,\,\,\,2\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,4\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,6\,\,\,\, \\ & & & & & & \end{aligned}\end{aligned}
$$

First, we multiply the ones:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\begin{aligned} \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\begin{aligned} \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\begin{aligned} \\ [math]\color{blue}2[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,2\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,4\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,6\,\,\,\, \\ & & \,\,\,\,1\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,4\,\,\,\,\end{aligned} & \,\, & \begin{aligned}2,324×6=13,944\end{aligned}\end{aligned}
$$

Next, we multiply the tens:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\begin{aligned}[math]\color{blue}\phantom{0}[/math] \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}2[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,2\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,4\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,6\,\,\,\, \\ & & \,\,\,\,1\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,4\,\,\,\, \\ & \,\,\,\,\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,0\,\,\,\,\end{aligned} & \,\, & \begin{aligned}2,324×40=92,960\end{aligned}\end{aligned}
$$

Finally, we add the results:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\begin{aligned}[math]\color{blue}\phantom{0}[/math] \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}2[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,2\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,4\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,6\,\,\,\, \\ & & \,\,\,\,1\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,4\,\,\,\, \\ \,\,\,\,+\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,0\,\,\,\, \\ & \,\,\,\,1\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,4\,\,\,\,\end{aligned} & \,\, & \begin{aligned}13,944+92,960=106,904\end{aligned} \\ & & & \end{aligned}
$$

Therefore, $2,324 \times 46 = 106, 904.$

### Example: Multiplying Four-Digit Numbers by Two-Digit Numbers: Word Problems

#### Question

A hospital orders $21$ shipments of syringes. Each shipment contains $4,859$ syringes. How many syringes has the hospital ordered in total?

#### Explanation

To calculate the total number of syringes the hospital ordered, we need to multiply $4,859$ by $21.$

We write it this way:

$$
\begin{aligned} & \begin{aligned} & & & & & & \\ & & & \,\,\,\,4\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,1\,\,\,\, \\ & & & & & & \end{aligned} & \,\, & \,4,859+97,180=102,039\end{aligned}
$$

First, we multiply the ones:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,4\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,\,1\,\,\,\, \\ & & \,\,\,\,\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,9\,\,\,\,\end{aligned} & \,\, & \begin{aligned}4,859×1=4,859\,0000000\end{aligned}\end{aligned}
$$

Next, we multiply the tens:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,4\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,\,2\,\,\,\, & \,\,\,\,1\,\,\,\, \\ & & \,\,\,\,\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,9\,\,\,\, \\ & \,\,\,\,\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,0\,\,\,\,\end{aligned} & \,\, & \begin{aligned}4,859×20=97,1800\,0000\end{aligned}\end{aligned}
$$

Finally, we add the results:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}\phantom{0}[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,4\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,1\,\,\,\, \\ & & \,\,\,\,\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,+\,\,\,\, & \,\,\,\,\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,0\,\,\,\, \\ & \,\,\,\,1\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,9\,\,\,\,\end{aligned} & \,\, & \begin{aligned}4,859+97,180=102,039\end{aligned} \\ & & & \end{aligned}
$$

So, $4,859 \times 21 = 102, 039.$

Therefore, the hospital ordered $102,039$ syringes in total.

### Example: Multiplying Five-Digit Numbers by Two-Digit Numbers

#### Question

From left to right, what are the missing digits in the following multiplication problem?

$$
\begin{aligned} & & & \,\,\,\,4\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,7\,\,\,\, \\ & \,\,\,\,2\,\,\,\, & \,\,\,\,\,[math]\phantom{i}[/math]\,\,\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,\,[math]\phantom{i}[/math]\,\,\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,\,[math]\phantom{i}[/math]\,\,\,\,\,\, & \,\,\,\,3\,\,\,\,\end{aligned}
$$

#### Explanation

We write it this way:

$$
\begin{aligned} & \begin{aligned} & & & & & & & \\ & & & \,\,\,\,4\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,7\,\,\,\, \\ & & & & & & & \end{aligned} & \,\, & \,42,689×40=1,707,560\end{aligned}
$$

First, we multiply the ones:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}4[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}6[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned} \\ [math]\color{blue}6[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,4\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,\,7\,\,\,\, \\ & & \,\,\,\,2\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,3\,\,\,\,\end{aligned} & \,\, & \begin{aligned}42,689×7=298,82300,\end{aligned}\end{aligned}
$$

Next, we multiply the tens:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}2[/math] \\ [math]\color{blue}4[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}3[/math] \\ [math]\color{blue}6[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}3[/math] \\ [math]\color{blue}6[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,4\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,\,4\,\,\,\, & \,\,\,\,7\,\,\,\, \\ & & \,\,\,\,2\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,3\,\,\,\, \\ & \,\,\,\,1\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,0\,\,\,\,\end{aligned} & \,\, & \begin{aligned}42,689×40=1,707,560\end{aligned}\end{aligned}
$$

Finally, we add the results:

$$
\begin{aligned} & \begin{aligned} & & & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}1[/math] \\ [math]\color{blue}1[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}2[/math] \\ [math]\color{blue}4[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}3[/math] \\ [math]\color{blue}6[/math]\end{aligned}\,\,\,\, & \,\,\,\,\,\,\begin{aligned}[math]\color{blue}3[/math] \\ [math]\color{blue}6[/math]\end{aligned}\,\,\,\, & \\ & & & \,\,\,\,4\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,9\,\,\,\, \\ \,\,\,\,×\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,4\,\,\,\, & \,\,\,\,7\,\,\,\, \\ & & \,\,\,\,2\,\,\,\, & \,\,\,\,9\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,8\,\,\,\, & \,\,\,\,2\,\,\,\, & \,\,\,\,3\,\,\,\, \\ \,\,\,\,+\,\,\,\, & \,\,\,\,1\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,7\,\,\,\, & \,\,\,\,5\,\,\,\, & \,\,\,\,6\,\,\,\, & \,\,\,\,0\,\,\,\, \\ & \,\,\,\,2\,\,\,\, & \,\,\,\,\,\,[math]0[/math]\,\,\,\, & \,\,\,\,0\,\,\,\, & \,\,\,\,\,\,[math]6[/math]\,\,\,\, & \,\,\,\,3\,\,\,\, & \,\,\,\,\,\,[math]8[/math]\,\,\,\,\,\, & \,\,\,\,3\,\,\,\,\end{aligned} & \,\, & \begin{aligned}298,823+1,707,560=0,, \\ \,=2,006,383\end{aligned} \\ & & & \end{aligned}
$$

Therefore, the missing digits are $0,6$ and $8.$
