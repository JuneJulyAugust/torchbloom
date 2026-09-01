# Finding Extrema of Functions Using a Graphing Calculator

Source: https://www.mathacademy.com/topics/3128?courseId=21
Topic ID: 3128

## Prerequisites

- [Global vs. Local Extrema and Critical Points](../ap-calculus-ab/313-global-vs-local-extrema-and-critical-points.md)
- [Evaluating Expressions Using a Graphing Calculator](../ap-calculus-ab/1832-evaluating-expressions-using-a-graphing-calculator.md)

## Lesson

### Introduction

In this lesson, we'll learn how to plot a function on a graphing calculator and then use our plot to find accurate approximations of the function's maxima and minima.

This lesson is designed to help prepare you for the parts of the AP Calculus exam where graphing calculators are needed.

**If you want to succeed on the AP Calculus exam, then you must acquire a physical graphing calculator and use it when completing this lesson.**

Do *not* use any other type of online tool, as you will not be allowed to use it during the exam. You need to practice with the specific calculator that you will use on the AP exam so that you can solve problems quickly without wasting any time troubleshooting your calculator.

A comprehensive list of calculators that are permitted in the AP Calculus exams can be found [here.](https://apcentral.collegeboard.org/exam-administration-ordering-scores/administering-exams/on-exam-day/calculator-policy#list)

Throughout this lesson, we will list buttons that feature on a TI-84 Plus CE-T graphing calculator.

Similar models will have the same or similar buttons, and even dissimilar models may have similar buttons.

If you have a different calculator model and cannot find the right buttons to press, the best way to resolve this is to either to

$\qquad$ (a) consult your calculator's manual, or

$\qquad$ (b) search online for a video that explains how to operate your calculator.

The best way to get familiar with your calculator is to consult its manual. Manuals can usually be found online. For example, a link to the manual for a TI-84 Plus CE-T can be found by entering the following query into a search engine.

$\qquad$ online manual TI-84 Plus CE-T

If you have a different model calculator, replace "TI-84 Plus CE-T" in the query above with your calculator's model.

Answers to common questions can be found by searching for online videos explaining how the calculator works. For example, to find a video that shows how to plot a function on a TI-84, you might type the following query into a search engine.

$\qquad$ video plot a function on a TI-84 graphing calculator

Again, replace "TI-84" in the query above with your calculator's model. Also, bear in mind that videos for similar models might also help.

### Plotting a Function

Our goal is to plot some functions on a graphing calculator and then use these to approximate the function's local maxima and minima.

Let's start by plotting the following function:

$$


f(x)=x^3-\sin x


$$

**Watch Out!** Since $f(x)$ involves a trigonometric function, we *must* put our calculator into radians mode!

To plot the function, we first press the $\boxed{\color{gray}\,y=\,}$ button, and then enter the function definition in the first available space (usually labeled $Y_1=$) using the following sequence of buttons:

$$


\boxed{\color{gray}X,T,\theta,n}\qquad \boxed{\color{gray}\,\land\,} \qquad \boxed{\color{gray}\,3\,} \qquad \boxed{\color{gray}\,\blacktriangleright\,} \qquad \boxed{\color{gray}\,-\,} \qquad \boxed{\color{gray}\,\sin\,} \qquad \boxed{\color{gray}X,T,\theta,n}\qquad \boxed{\color{gray}\,)\,}


$$

We then press $\boxed{\color{gray}\,\text{graph}\,}$ to graph the function.

To get a better view of our function, we can adjust the window settings using the $\boxed{\color{gray}\,\text{window}\,}$ button. Press this button, and then enter the following settings:

$$


\begin{aligned}Xmin & =−2 \\ Xmax & =2 \\ Ymin & =−1 \\ Ymax & =1\end{aligned}


$$

Remember to use the negative $\boxed{\color{gray}\,(-)\,}$ button when entering the negative numbers.

Once you've entered these settings, press $\boxed{\color{gray}\,\text{graph}\,}$ once more. Your calculator should then draw the following graph:

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/4483adca3963873b.png)

Notice that the $x$ and $y$-axes have been restricted as follows:

- For the horizontal axis, we have $x \in [-2,2].$

- For the vertical axis, we have $y \in [-1,1].$

Make sure you can replicate this graph on your graphing calculator before continuing. This includes adjusting the window settings, which will become important later in the lesson.

### Finding a Local Maximum

So, we have the function $f(x),$ defined as

$$


f(x)=x^3-\sin x.


$$

Our plot of this function is shown again below.

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/be7f1e3368ee2b8a.png)

The graph shows that the function has a local maximum point inside the interval $x \in [-2,0].$ Our goal now is to find an accurate approximation for this point using our graphing calculator's $\boxed{\color{gray}\,\text{maximum}\,}$ command.

To access the $\boxed{\color{gray}\,\text{maximum}\,}$ command, we first make sure that our function $f(x)$ is plotted, and the point we want to find is clearly in view. Then, we press the $\boxed{\color{gray}\,\text{2nd}\,}$ button followed by $\boxed{\color{gray}\,\text{calc}\,}.$ We then select $\boxed{\color{gray}\,\text{maximum}\,}$ from the menu, followed by $\boxed{\color{gray}\,\text{enter}\,}.$

The calculator will now ask us to specify an interval containing the maximum and an initial guess. First, we select a "left bound," followed by a "right bound," followed by our "guess." To specify these values, we use the $\boxed{\color{gray}\,\blacktriangleleft\,}$ and $\boxed{\color{gray}\,\blacktriangleright\,}$ buttons to move the cursor along the curve, and press $\boxed{\color{gray}\,\text{enter}\,}$ to select.

In this particular case, we enter the following when prompted:

- The "left bound" should be an $x$-value close to the maximum on its left-hand side. Let's pick $-1.5.$

- The "right bound" should be an $x$-value close to the maximum on its right-hand side. Let's pick $0.$

- The "guess" could be any number from the interval $x\in [-1.5,0].$ Let's pick $-0.5.$

Our interval and guess are highlighted below.

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/2ab9ddde155615d9.png)

At the bottom of the display, the calculator will return the following value for the maximum:

$$


x = -0.535\,427, \qquad y = 0.356\,711


$$

And that's it! We've successfully used the calculator to approximate the $x$- and $y$-coordinates of the local maximum.

**Watch Out!**

- It's important to remember that the coordinates of the maximum point returned by the calculator are *approximations*.

- Moreover, different calculators use different algorithms to arrive at their approximations.

- For that reason, different calculators may give slightly different answers for these points.

- Despite this, the answers returned by different calculators will agree when the answer is rounded to two or three decimal places in most cases.

### Example: Finding a Local Maximum Inside the Standard Range

#### Question

Find the $x$-value that corresponds to the maximum of the function $f(x) =-2x^3 + 2^{x^2} +x$ on the interval $[0,1].$

#### Explanation

First, we plot $y=f(x)$ using a graphing calculator.

We need to find an interval that contains the maximum. To get a better view, we might need to either

- zoom out, or

- adjust the window ranges.

We can adjust the window settings using the $\boxed{\color{gray}\,\text{window}\,}$ button (or equivalent).

In our case, the appropriate window ranges could be the following:

- for the horizontal axis, $x \in [-1,2]$

- for the vertical axis, $y \in [-1,2]$

This gives us the following graph:

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/5404a7116ca9d42a.png)

We're told that the maximum lies inside the interval $x \in [0,1].$

To get a good approximation for the maximum, we use the $\boxed{\color{gray}\,\text{maximum}\,}$ command (or equivalent). This is usually accessed by pressing the $\boxed{\color{gray}\,\text{calc}\,}$ button (or equivalent). Note that we sometimes need to press the $\boxed{\color{gray}\,\text{2nd}\,}$ button first.

Then, we enter the following when prompted:

- The "left bound" should be an $x$-value close to the maximum on its left-hand side. Let's pick $0.$

- The "right bound" should be an $x$-value close to the maximum on its right-hand side. Let's pick $1.$

- The "guess" could be any number from $[0,1].$ Let's pick $0.5.$

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/d4c7d7ce9556f411.png)

The calculator returns the maximum

$$


x_{\max} \approx 0.579\,272, \qquad y_{\max} \approx 1.452\,379.


$$

Rounding to three decimal places, we obtain the following:

$$


x_{\max} \approx 0.579, \qquad y_{\max} \approx 1.452.


$$

Therefore, the maximum value of $f(x)$ is obtained at $x_{\max} \approx 0.579,$ rounded to $3$ decimal places.

### Finding a Local Minimum

Let's now consider the function $f(x),$ defined as

$$


f(x)=x^3-x + \cos x.


$$

A plot of this function is shown below.

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/e397048009f04111.png)

The graph shows that the function has a local minimum point inside the interval $x \in [0,2].$ We wish to find an accurate approximation for this point using our graphing calculator's $\boxed{\color{gray}\,\text{minimum}\,}$ command.

To access the $\boxed{\color{gray}\,\text{minimum}\,}$ command, we first make sure that our function $f(x)$ is plotted, and the point we want to find is clearly in view. Then, we press the $\boxed{\color{gray}\,\text{2nd}\,}$ button followed by $\boxed{\color{gray}\,\text{calc}\,}.$ We then select $\boxed{\color{gray}\,\text{minimum}\,}$ from the menu, followed by $\boxed{\color{gray}\,\text{enter}\,}.$

The calculator will now ask us to specify an interval containing the minimum and an initial guess. First, we select a "left bound," followed by a "right bound," followed by our "guess." To specify these values, we use the $\boxed{\color{gray}\,\blacktriangleleft\,}$ and $\boxed{\color{gray}\,\blacktriangleright\,}$ buttons to move the cursor along the curve, and press $\boxed{\color{gray}\,\text{enter}\,}$ to select.

In this particular case, we enter the following when prompted:

- The "left bound" should be an $x$-value close to the minimum on its left-hand side. Let's pick $0.$

- The "right bound" should be an $x$-value close to the minimum on its right-hand side. Let's pick $2.$

- The "guess" could be any number from the interval $x\in [0,2].$ Let's pick $1.$

Our interval and guess are highlighted below.

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/83fb7ee889d44a92.png)

At the bottom of the display, the calculator will return the following value for the minimum:

$$


x = 0.748\,441\,6, \qquad y = 0.403\,559\,3


$$

And that's it! We've successfully used the calculator to approximate the $x$- and $y$-coordinates of the local minimum.

### Example: Finding a Local Minimum Inside the Standard Range

#### Question

Find the minimum value of the function $f(x) = x^{x-2}$ on the interval $[1,2].$

#### Explanation

First, we plot $y=f(x)$ using a graphing calculator.

We need to find an interval that contains the minimum. To get a better view, we might need to either

- zoom out, or

- adjust the window ranges.

We can adjust the window settings using the $\boxed{\color{gray}\,\text{window}\,}$ button (or equivalent).

In our case, the appropriate window ranges could be the following:

- for the horizontal axis, $x \in [0,2.5]$

- for the vertical axis, $y \in [0,3.5]$

This gives us the following graph:

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/72cea4b1ff6fc475.png)

We're told that the minimum lies inside the interval $x \in [1,2].$

To get a good approximation for the minimum, we use the $\boxed{\color{gray}\,\text{minimum}\,}$ command (or equivalent). This is usually accessed by pressing the $\boxed{\color{gray}\,\text{calc}\,}$ button (or equivalent). Note that we sometimes need to press the $\boxed{\color{gray}\,\text{2nd}\,}$ button first.

Then, we enter the following when prompted:

- The "left bound" should be an $x$-value close to the minimum on its left-hand side. Let's pick $1.$

- The "right bound" should be an $x$-value close to the minimum on its right-hand side. Let's pick $2.$

- The "guess" could be any number from $[1,2].$ Let's pick $1.5.$

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/aaf5619bdc97b3f4.png)

The calculator returns the minimum

$$


x_{\min} \approx 1.454\,731\,6, \qquad y_{\min} \approx 0.815\,154.


$$

Rounding to $3$ decimal places, we obtain the following:

$$


x_{\min} \approx 1.455, \qquad y_{\min} \approx 0.815.


$$

Therefore, the minimum value of $f(x)$ is $0.815,$ rounded to $3$ decimal places.

### Extrema Outside the Standard Range

The default view on most graphing calculators is $x\in [-10,10]$ and $y\in [-10,10].$ When a local extremum lies outside this range, we must adjust the window to see it.

Suppose we want to find the minimum value of the following function:

$$


f(x) = (x-1)^2-20 +\cos x


$$

Plotting $y=f(x)$ using the default view gives the following:

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/6c3257b7c745791f.png)

Notice that the minimum point is not visible in the standard view.

To get a better view, we might start by zooming out. For this, we press $\boxed{\color{gray}\text{zoom}}$ and select "zoom out." Then, we press $\boxed{\color{gray}\text{enter}}$ followed by $\boxed{\color{gray}\text{enter}}$ once more.

This gives the following plot.

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/ae6f279676fd8b4b.png)

By pressing the $\boxed{\color{gray}\text{window}}$ button, we see that this view is $x\in [-40,40], y\in [-40,40].$

The minimum is now clearly visible, and we can apply our usual procedure to approximate the minimum point.

### Problems With Using Zoom

Although zoom is *sometimes* handy for identifying the approximate location of a maximum or minimum, it has drawbacks. In particular, we can encounter problems when a function varies rapidly and the extremum lies far from the origin.

For example, suppose we want to locate the local minimum point that lies to the left of the $y$-axis for the following function:

$$


f(x) = 2x^4 + 5x^3 - 9x^2 + 3


$$

Plotting the function in the default view gives the following.

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/5792cf499b8a5c58.png)

The local minimum that we want cannot be seen. However, if we zoom out twice, we get the following:

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/562747114ec6ef8a.png)

The problem here is that the $x$ and $y$-axes are so long that it's difficult to get an approximate location for the minimum.

To get around this issue, instead of using zoom, we should adjust the window settings to increase the range for $y$ while keeping the range for $x$ very small.

Since the minimum lies well below the $x$-axis, let's press the $\boxed{\color{gray}\,\text{window}\,}$ button and enter the following settings:

- for the horizontal axis, $x \in [-5, 5]$

- for the vertical axis, $y \in [-40,5]$

Pressing $\boxed{\color{gray}\,\text{graph}\,}$ gives the following.

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/0a435b164a5e6362.png)

We now have a much clearer picture of the function's behavior.

We still haven't located the root, so let's extend the $y$-axis even further down while keeping the range for $x$ the same as before.

- for the horizontal axis, $x \in [-5, 5]$

- for the vertical axis, $y \in [-60,5]$

This gives the following graph.

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/7d8dd930d9c40bb0.png)

We have now managed to locate the minimum, and we can apply our usual minimization procedures.

### Example: Finding a Local Extremum Outside the Standard Range

#### Question

Consider the function $f(x) =2^{x/2} - x^2.$ Determine the value of $x$ for $x\in [10,15]$ for which $f'(x) = 0.$

#### Explanation

The derivative $f'(x) = 0$ at the stationary points of a function.

First, we plot $y=f(x)$ using a graphing calculator.

We need to find an interval that contains the stationary point. To get a better view, we might need to either

- zoom out, or

- adjust the window ranges.

We can adjust the window settings using the $\boxed{\color{gray}\,\text{window}\,}$ button (or equivalent).

In our case, the appropriate window ranges could be the following:

- for the horizontal axis, $x \in [-5,18]$

- for the vertical axis, $y \in [-100,50]$

This gives us the following graph:

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/112d10a7779f3f5b.png)

The graph shows that the stationary point is the minimum that lies inside the interval $x \in [10,15].$

To get a good approximation for the minimum, we use the $\boxed{\color{gray}\,\text{minimum}\,}$ command (or equivalent). This is usually accessed by pressing the $\boxed{\color{gray}\,\text{calc}\,}$ button (or equivalent). Note that we sometimes need to press the $\boxed{\color{gray}\,\text{2nd}\,}$ button first.

Then, we enter the following when prompted:

- The "left bound" should be an $x$-value close to the minimum on its left-hand side. Let's pick $10.$

- The "right bound" should be an $x$-value close to the minimum on its right-hand side. Let's pick $15.$

- The "guess" could be any number from $[10,15].$ Let's pick $12.5.$

![Instructional graphic](../../../lesson-assets/ap-calculus-bc/topic-3128/1092712934d1fbfe.png)

The calculator returns the minimum

$$


x_{\min} \approx 12.298\,31, \qquad y_{\min} \approx -80.277\,56.


$$

Rounding to three decimal places, we obtain the following:

$$


x_{\min} \approx 12.298, \qquad y_{\min} \approx -80.278.


$$

Therefore, the value of $x$ for which $f'(x)=0$ is $x_{\min} \approx 12.298,$ rounded to $3$ decimal places.
