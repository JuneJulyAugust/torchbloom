# The ABM2 Method

Source: https://www.mathacademy.com/topics/6397?courseId=61
Topic ID: 6397

## Prerequisites

- [The Modified Euler Method](./3247-the-modified-euler-method.md)
- [The RK4 Method](./3248-the-rk4-method.md)

## Lesson

### Introduction

For a first-order initial value problem, we have already seen ways to approximate the increment in $y$ over a step, including:

- the modified Euler method, which predicts using Euler's method and then corrects that prediction, and

- the RK4 method, which combines several slope evaluations within a single step.

Another group of methods, called the **Adams-Bashforth-Moulton methods**, takes a different approach. Rather than computing multiple slopes at new points, these methods reuse slopes from previous steps in a predictor-corrector framework, giving high accuracy with relatively little additional work.

In this lesson, we'll focus on one of the simplest: the $2$-step Adams-Bashforth-Moulton method. For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the predictor equation of the **$2$-step Adams-Bashforth-Moulton method** (**ABM $2$-step**) with step size $\Delta x$ is

$$


\Delta y_p = \dfrac12(3y' - y'_{-1}) \cdot \Delta x,


$$

where

- $y' = f(x,y)$ is the slope at the current point $(x,y),$ and

- $y'_{-1} = f(x_{-1}, y_{-1})$ is the slope at the previous point $(x_{-1}, y_{-1}),$ where $x_{-1} = x-\Delta x.$

The initially predicted new $y$-value is then given by $y_p = y + \Delta y_p.$

Since ABM $2$-step uses the slope from the previous step, it cannot be started from a single initial condition alone. Instead, we initialize the method by computing the first step with a one-step method, typically the RK4 method.

Once the prediction $y_p$ is computed, we apply a corrector equation to refine our approximation. We'll return to this step shortly. Before that, let's see an example of how to apply the predictor equation.

### A Worked Example

Consider the following initial value problem:

$$


y' = 4x - 2y, \qquad y(0) = 1


$$

Let's begin the process of applying the $2$-step Adams-Bashforth-Moulton method to approximate the value of $y(1).$

We know $y(0)$ and wish to estimate $y(1).$ Since the method takes $2$ steps (one to initialize, one to approximate), we will use a step size of

$$


\Delta x = \dfrac{1-0}2 = \dfrac12.


$$

We will use a table to keep track of known values. First, we add the initial condition data:

Next, we initialize the ABM $2$-step method by making a preliminary step with a one-step method.

Applying the RK4 method with step size $\Delta x = \dfrac12,$ we obtain the slope $y'=-2,$ increment $\Delta y = -\dfrac14,$ and approximation

$$


y\left(\dfrac12\right)\approx 1 + \left(-\dfrac14\right) = \dfrac34.


$$

We add the slope to the table, and the approximation in a new row.

Note that, since RK4 is not a predictor-corrector method, there is no increment $\Delta y_p$ or predictor $y_p$ for this step. So, we leave these entries in the first row blank.

Now, we continue from this point, using the ABM $2$-step method. First, we compute the value of $y'$ according to the given rule:

$$


\begin{aligned}𝑦^{′} & =4𝑥−2𝑦 \\ & =4⋅(\frac{1}{2})−2⋅(\frac{3}{4}) \\ & =\frac{1}{2}\end{aligned}


$$

So, we add this to our table.

From the table, we see that the slope at the previous point $(x_{-1}, y_{-1}) = \left(0, 1\right)$ is $y'_{-1} = -2.$

Next, we compute $\Delta y_p$ using the predictor equation:

$$


\begin{aligned}Δ𝑦_{𝑝} & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥 \\ & =\frac{1}{2}(3⋅(\frac{1}{2})−(−2))⋅\frac{1}{2} \\ & =\frac{1}{4}⋅\frac{7}{2} \\ & =\frac{7}{8}\end{aligned}


$$

We add this value to our table.

Hence, according to the predictor equation, the initially predicted new $y$-value is

$$


\begin{aligned}𝑦_{𝑝} & =𝑦+Δ𝑦_{𝑝} \\ & =\frac{3}{4}+\frac{7}{8} \\ & =\frac{13}{8}.\end{aligned}


$$

Therefore, the completed table is as given below.

Therefore, our initial prediction for $y(1)$ is $y_p = \dfrac{13}8.$

### Example: Completing a Table Using the Predictor Equation of the ABM 2-Step Method

#### Question

Consider the following initial value problem:

$$


y' = 2x - 2y + 1, \qquad y(0) = 0


$$

We wish to approximate the solution using the $2$-step Adams-Bashforth-Moulton method. Given that the step size is $\Delta x = \dfrac14,$ and that the first step has already been computed using the Runge-Kutta method, fill the missing entries in the table below, where $y_p$ denotes the predictor at each step.

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the predictor equation of the $2$-step Adams-Bashforth-Moulton method (ABM2) with step size $\Delta x$ is given by

$$


\Delta y_p = \dfrac12(3y' - y'_{-1}) \cdot \Delta x,


$$

where

- $y' = f(x,y)$ is the estimated slope at the current point $(x,y),$ and

- $y'_{-1} = f(x_{-1}, y_{-1})$ is the estimated slope at the previous point $(x_{-1}, y_{-1}).$

The initially predicted new $y$-value is then given by $y_p = y + \Delta y_p.$

We're told that the first step is calculated using the Runge-Kutta Method, resulting in

$$


y\left(\dfrac{1}{4}\right) \approx \dfrac{1}{4}.


$$

Now, we'll continue from this point, using the ABM $2$-step method.

First, we compute the value of $y'$ according to the given rule:

$$


\begin{aligned}𝑦^{′} & =2𝑥−2𝑦+1 \\ & =2⋅(\frac{1}{4})−2⋅(\frac{1}{4})+1 \\ & =1\end{aligned}


$$

So, we add this to our table.

From the table, we see that the slope at the previous point $(x_{-1}, y_{-1}) = \left(0, 0\right)$ is $y'_{-1} = 1.$

Next, we compute $\Delta y_p$ using the predictor equation:

$$


\begin{aligned}Δ𝑦_{𝑝} & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥 \\ & =\frac{1}{2}(3⋅1−1)⋅\frac{1}{4} \\ & =\frac{1}{8}⋅2 \\ & =\frac{1}{4}\end{aligned}


$$

We add this value to our table.

Hence, according to the predictor equation, the initially predicted new $y$-value is

$$


\begin{aligned}𝑦_{𝑝} & =𝑦+Δ𝑦_{𝑝} \\ & =\frac{1}{4}+\frac{1}{4} \\ & =\frac{1}{2}.\end{aligned}


$$

Therefore, the completed table is as given below.

### The Two-Step Adams-Bashforth-Moulton Method

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the **$2$-Step Adams-Bashforth-Moulton** (**ABM $2$-step**) **Method** with step size $\Delta x$ is given by

$$


\begin{aligned}Predictor & : & Δ𝑦_{𝑝} & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥, \\ Corrector & : & Δ𝑦 & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥,\end{aligned}


$$

where

- $y' = f(x,y)$ is the estimated slope at the current point $(x,y),$

- $y'_{-1} = f(x_{-1}, y_{-1})$ is the estimated slope at the previous point $(x_{-1}, y_{-1}),$ and

- $y'_p = f(x_\text{new}, y_p)$ is the estimated slope at the predicted new point $(x_\text{new}, y_p) = (x + \Delta x, y + \Delta y_p).$

The final approximation for the new step is $y_\text{new} = y + \Delta y.$

So, the corrector of the ABM $2$-step combines the slope evaluated at the predicted point with the slope evaluated at the current point and the previous point. Let's demonstrate how to apply the corrector equation to our previous example.

### A Worked Example

Let's return to the following initial value problem:

$$


y' = 4x-2y, \qquad y(0) = 1


$$

We will now complete our approximation of the value of $y(1)$ using the $2$-step Adams-Bashforth-Moulton method.

First, recall that we previously initialized with the RK4 method and completed the predictor step of the ABM $2$-step method, resulting in the following values:

Now, the slope at the point $(x_\text{new},y_p) = \left(\dfrac12+\dfrac12, \dfrac{13}8\right) = \left(1, \dfrac{13}8\right)$ estimated by the predictor is

$$


\begin{aligned}𝑦_{′𝑝}^{} & =4𝑥_{new}−2𝑦_{𝑝} \\ & =4⋅1−2⋅\frac{13}{8} \\ & =\frac{3}{4}.\end{aligned}


$$

We can add this to our table.

Looking at the partially filled table, we note the following:

- From the second row, the slope at the current point $(x, y) = \left(\dfrac12, \dfrac34\right)$ is $y' = \dfrac12.$

- From the first row, the slope at the previous point $(x_{-1}, y_{-1}) = \left(0, 1\right)$ is $y'_{-1} = -2.$

Finally, we compute $\Delta y$ using the corrector equation:

$$


\begin{aligned}Δ𝑦 & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥 \\ & =\frac{1}{12}(5⋅\frac{3}{4}+8⋅\frac{1}{2}−(−2))⋅\frac{1}{2} \\ & =\frac{1}{24}⋅\frac{39}{4} \\ & =\frac{13}{32}\end{aligned}


$$

Therefore, the completed row is as given below.

We know the value of $x$ in the next row is $x_\text{new}=1.$ To get the value of $y$ in the next row, we add $\Delta y$ to $y{:}$

$$


y_\text{new} = y + \Delta y = \dfrac34 + \dfrac{13}{32} = \dfrac{37}{32}


$$

Adding these results to our table gives the following:

Therefore, we conclude that $y(1) \approx \dfrac{37}{32}.$

### Example: Calculating the Corrector Term

#### Question

Consider the following initial value problem:

$$


y' = x + y + 1, \qquad y\left(-2\right) = 0


$$

We wish to approximate the solution using the $2$-step Adams-Bashforth-Moulton method. Given that the step size is $\Delta x = \dfrac14,$ and that one preliminary step has already been computed using the Runge-Kutta method, complete the second row of the table below.

**

$$


\Delta y = \dfrac1{12}(5y'_p + 8y' - y'_{-1}) \cdot \Delta x


$$

**

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the $2$-step Adams-Bashforth-Moulton (ABM2) method with step size $\Delta x$ is given by

$$


\begin{aligned}Predictor & : & Δ𝑦_{𝑝} & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥, \\ Corrector & : & Δ𝑦 & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥,\end{aligned}


$$

where

- $y' = f(x,y)$ is the estimated slope at the current point $(x,y),$

- $y'_{-1} = f(x_{-1}, y_{-1})$ is the estimated slope at the previous point ($x_{-1}, y_{-1}),$ and

- $y'_p = f(x_\text{new}, y_p)$ is the estimated slope at the predicted new point $(x_\text{new}, y_p) = (x + \Delta x, y + \Delta y_p).$

Looking at the partially filled table, we note the following:

- From the second row, the slope at the current point $(x, y) = \left(-\dfrac74, -\dfrac{1}{4}\right)$ is $y' = -1.$

- From the first row, the slope at the previous point $(x_{-1}, y_{-1}) = \left(-2, 0\right)$ is $y'_{-1} = -1.$

- From the second row, the slope at the predicted new point $(x_\text{new}, y_p)$ is $y'_p = -1.$

Now, we compute $\Delta y$ using the corrector equation:

$$


\begin{aligned}Δ𝑦 & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥 \\ & =\frac{1}{12}(5⋅(−1)+8⋅(−1)−(−1))⋅\frac{1}{4} \\ & =\frac{1}{48}⋅(−12) \\ & =−\frac{1}{4}\end{aligned}


$$

Therefore, the completed row is as given below.

### Example: Completing a Row of a Table Using the ABM 2-Step Method

#### Question

Consider the following initial value problem:

$$


y' = -x - y, \qquad y\left(-1\right) = 0


$$

We wish to approximate the solution using the $2$-step Adams-Bashforth-Moulton method. Given that the step size is $\Delta x = 1,$ and that one preliminary step has already been computed using the Runge-Kutta method, complete the next rows of the table below.

**

$$


\Delta y = \dfrac1{12}(5y'_p + 8y' - y'_{-1}) \cdot \Delta x


$$

**

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the $2$-Step Adams-Bashforth-Moulton (ABM2) method with step size $\Delta x$ is given by

$$


\begin{aligned}Predictor & : & Δ𝑦_{𝑝} & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥, \\ Corrector & : & Δ𝑦 & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥,\end{aligned}


$$

where

- $y' = f(x,y)$ is the estimated slope at the current point $(x,y),$

- $y'_{-1} = f(x_{-1}, y_{-1})$ is the estimated slope at the previous point ($x_{-1}, y_{-1}),$ and

- $y'_p = f(x_\text{new}, y_p)$ is the estimated slope at the predicted new point $(x_\text{new}, y_p) = (x + \Delta x, y + \Delta y_p).$

We're told that the first step is calculated using the Runge-Kutta Method, resulting in

$$


y\left(0\right) \approx \dfrac{1}{4}.


$$

Now, we'll continue from this point, using the $2$-step ABM method.

First, we compute the value of $y'$ according to the given rule:

$$


\begin{aligned}𝑦^{′} & =−𝑥−𝑦 \\ & =−0−\frac{1}{4} \\ & =−\frac{1}{4}\end{aligned}


$$

So, we add this to our table.

From the first row of the table, we see that the slope at the previous point $(x_{-1}, y_{-1}) = \left(-1, 0\right)$ is $y'_{-1} = 1.$

Next, we compute $\Delta y_p$ using the predictor equation:

$$


\begin{aligned}Δ𝑦_{𝑝} & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥 \\ & =\frac{1}{2}(3⋅(−\frac{1}{4})−1)⋅1 \\ & =−\frac{7}{8}\end{aligned}


$$

We add this to our table.

So, the coordinates of the predicted new point are

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥=0+1=1, \\ 𝑦_{𝑝} & =𝑦+Δ𝑦_{𝑝}=\frac{1}{4}+(−\frac{7}{8})=−\frac{5}{8}.\end{aligned}


$$

Let's add the second value to the table.

Hence, the slope at this predicted point is

$$


\begin{aligned}𝑦_{′𝑝}^{} & =−𝑥_{new}−𝑦_{𝑝} \\ & =−1−(−\frac{5}{8}) \\ & =−\frac{3}{8}.\end{aligned}


$$

We can add this to our table.

Finally, we compute $\Delta y$ using the corrector equation:

$$


\begin{aligned}Δ𝑦 & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥 \\ & =\frac{1}{12}(5⋅(−\frac{3}{8})+8⋅(−\frac{1}{4})−1)⋅1 \\ & =\frac{1}{12}⋅(−\frac{39}{8}) \\ & =−\frac{13}{32}\end{aligned}


$$

Therefore, the completed row is as given below.

The value of $x$ in the next row is $x_\text{new} = 1.$ To get the value of $y$ in the next row, we add $\Delta y$ to $y{:}$

$$


y_\text{new} = y + \Delta y = \dfrac{1}{4} + \left(-\dfrac{13}{32}\right) = -\dfrac{5}{32}


$$

Adding these results to our table gives the following:

Therefore, we conclude that $y(1) \approx \boxed{-\dfrac{5}{32}}.$

### Example: Approximating the Solution to an Initial Value Problem Using The ABM 2-Step Method

#### Question

Consider the following initial value problem:

$$


y' = x - 2y + 6, \qquad y(0) = 2


$$

To approximate the solution, one step of the Runge-Kutta method has already been computed, resulting in the following estimate:

$$


y(1) \approx 3


$$

Use the $2$-Step Adams-Bashforth-Moulton Method with one step to approximate $y(2).$

**

$$


\Delta y = \dfrac1{12}(5y'_p + 8y' - y'_{-1}) \cdot \Delta x


$$

**

#### Explanation

For an initial value problem

$$


y' = f(x,y), \qquad y(a) = c,


$$

the $2$-Step Adams-Bashforth-Moulton (ABM $2$-step) Method with step size $\Delta x$ is given by

$$


\begin{aligned}Predictor & : & Δ𝑦_{𝑝} & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥, \\ Corrector & : & Δ𝑦 & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥,\end{aligned}


$$

where

- $y' = f(x,y)$ is the estimated slope at the current point $(x,y),$

- $y'_{-1} = f(x_{-1}, y_{-1})$ is the estimated slope at the previous point ($x_{-1}, y_{-1}),$ and

- $y'_p = f(x_\text{new}, y_p)$ is the estimated slope at the predicted new point $(x_\text{new}, y_p) = (x + \Delta x, y + \Delta y_p).$

Before we start, let's add the initial condition data and Runge-Kutta step data to a table.

Now, since we want to find the value of $y$ at $x=2,$ we will use a step size of

$$


\Delta x = 2 - 1 = 1.


$$

First, we compute the values of $y'$ at each point according to the given rule:

- The slope at the previous point $(x_{-1}, y_{-1}) = (0,2)$ is

- The slope at the current point $(x, y) = (1,3)$ is

We add these values to our table.

Next, we compute $\Delta y_p$ using the predictor equation:

$$


\begin{aligned}Δ𝑦_{𝑝} & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥 \\ & =\frac{1}{2}(3⋅1−2)⋅1 \\ & =\frac{1}{2}.\end{aligned}


$$

We add this to our table.

So, the coordinates of the predicted new point are

$$


\begin{aligned}𝑥_{new} & =𝑥+Δ𝑥=1+1=2, \\ 𝑦_{𝑝} & =𝑦+Δ𝑦_{𝑝}=3+\frac{1}{2}=\frac{7}{2}.\end{aligned}


$$

Let's add the second value to the table.

Hence, the slope at this predicted point is

$$


\begin{aligned}𝑦_{′𝑝}^{} & =𝑥_{new}−2𝑦_{𝑝}+6 \\ & =2−2⋅\frac{7}{2}+6 \\ & =1.\end{aligned}


$$

We can add this to our table.

Finally, we compute $\Delta y$ using the corrector equation:

$$


\begin{aligned}Δ𝑦 & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥 \\ & =\frac{1}{12}(5⋅1+8⋅1−2)⋅1 \\ & =\frac{1}{12}⋅11 \\ & =\frac{11}{12}.\end{aligned}


$$

We add this to our table.

The value of $x$ in the next row is $x_\text{new}=2.$ To get the value of $y$ in the next row, we add $\Delta y$ to $y{:}$

$$


\begin{aligned}𝑦_{new} & =𝑦+Δ𝑦 \\ & =3+\frac{11}{12} \\ & =\frac{47}{12}.\end{aligned}


$$

Adding these results to our table gives the following:

Therefore, we conclude that $y(2)\approx\dfrac{47}{12}.$

### Derivation of the AB2 Predictor

Where do the predictor and corrector equations of the two-step Adams–Bashforth–Moulton method come from?

The method consists of two parts: the **Adams-Bashforth** (**AB2**) **predictor**, and **Adams-Moulton** (**AM2**) **corrector**. We'll begin by deriving the AB2 predictor.

Consider an initial value problem:

$$


y' = f(x,y), \qquad y(a)=c


$$

Writing the differential equation in integral form, we have

$$


y_\text{new} = y + \int_{x}^{x_\text{new}} f(t, y(t))\,\mathrm{d}t \quad\Longrightarrow\quad \Delta y = \int_{x}^{x_\text{new}} f(t, y(t))\,\mathrm{d}t.


$$

Let $\Delta x = x_\text{new} - x$ be the step size, and define the change of variables

$$


\theta = \dfrac{t - x}{\Delta x}.


$$

Then, $t = x + \theta\cdot\Delta x$ and $\mathrm{d}t = \mathrm{d}\theta\cdot\Delta x,$ so the integral becomes

$$


\Delta y = \int_0^1 f(x + \theta\cdot\Delta x, y(x + \theta\cdot\Delta x))\,\mathrm{d}\theta\cdot\Delta x.


$$

Now, define a new function $g$ of $\theta$ as the integrand:

$$


g(\theta) = f(x + \theta\cdot\Delta x, y(x + \theta\cdot\Delta x))


$$

The Adams formulas result from approximating $g(\theta)$ by a simple function that agrees with its known values, and then integrating that approximation from $0$ to $1.$ We now determine some known values.

- Evaluating $g$ at $\theta = 0,$ we have

- Similarly, evaluating $g$ at $\theta=-1$, we get where $x_{-1}$ is the previous $x$-value and $y'_{-1}$ is the slope at the previous point $(x_{-1}, y(x_{-1})).$

Since we have two known values, the simplest reasonable approximation to $g(\theta)$ is a *straight line* passing through these two points: $(0,y')$ and $(-1,y'_{-1}).$ This straight line is given by

$$


\begin{aligned}𝑝(𝜃) & =𝑦^{′}+\frac{𝑦^{′}−𝑦_{′−1}^{}}{0−(−1)}(𝜃−0) \\ & =𝑦^{′}+(𝑦^{′}−𝑦_{′−1}^{})𝜃.\end{aligned}


$$

Finally, by integrating this approximation, we obtain

$$


\begin{aligned}∫_{10}^{}𝑝(𝜃)\,d𝜃 & =∫_{10}^{}(𝑦^{′}+(𝑦^{′}−𝑦_{′−1}^{})𝜃)\,d𝜃 \\ & =(𝑦^{′}𝜃+\frac{1}{2}(𝑦^{′}−𝑦_{′−1}^{})𝜃^{2})_{𝜃\,=\,1𝜃\,=\,0}^{} \\ & =𝑦^{′}+\frac{1}{2}(𝑦^{′}−𝑦_{′−1}^{})−0 \\ & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{}).\end{aligned}


$$

Therefore, the approximation of the increment in $y$ is

$$


\begin{aligned}Δ𝑦=∫_{10}^{}𝑔(𝜃)\,d𝜃⋅Δ𝑥≈∫_{10}^{}𝑝(𝜃)\,d𝜃⋅Δ𝑥=\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥.\end{aligned}


$$

It is this approximation that we define as the AB2 predictor:

$$


\Delta y_p = \dfrac12(3y' - y'_{-1})\cdot\Delta x.


$$

### Derivation of the AM2 Corrector

So far, we have derived the AB2 predictor. We are left to derive the AM2 corrector.

Recall that we wrote the differential equation in integral form as

$$


y_\text{new} = y + \int_x^{x_\text{new}} f(t,y(t))\,\mathrm{d}t \quad\Longrightarrow\quad \Delta y = \int_x^{x_\text{new}} f(t,y(t))\,\mathrm{d}t.


$$

With the change of variables

$$


\theta = \dfrac{t-x}{\Delta x},


$$

we had $t = x + \theta\cdot\Delta x$ and $\mathrm{d}t = \mathrm{d}\theta\cdot\Delta x,$ so

$$


\Delta y = \int_0^1 f(x+\theta\Delta x,y(x+\theta\Delta x))\,\mathrm{d}\theta\cdot\Delta x,


$$

and we defined

$$


g(\theta) = f(x+\theta\Delta x,y(x+\theta\Delta x)).


$$

For the predictor, we considered two known values of $g(\theta){:}$

- For $\theta = 0,$ we have $g(0) = y'.$

- For $\theta = -1,$ we have $g(-1) = y'_{-1}.$

Then, we approximated $g$ with a linear function passing through these two points.

Now, for the corrector, we use *three* known values, and approximate $g(\theta)$ by a *quadratic* passing through these three points.

To obtain a third value, we also want the slope at the *new* $x$-value $x_\text{new} = x + \Delta x.$ But, the true value $y_\text{new}$ is not yet known.

Instead, we evaluate the slope at the new point estimated by the AB2 predictor! This corresponds to $\theta = 1{:}$

$$


g(1) = f(x + \Delta x, y(x + \Delta x)) \approx f(x_\text{new}, y_p) = y'_p,


$$

where $y_p$ is the new $y$-value predicted by AB2, and $y'_p$ is the slope evaluated at $(x_\text{new}, y_p).$ So, our three points are

$$


(-1,y'_{-1}), \quad (0,y'), \quad (1,y'_p).


$$

Let $q(\theta)$ be the quadratic that passes through these three points. After simplifying, this quadratic can be written as

$$


\begin{aligned}𝑞(𝜃) & =\frac{1}{2}𝜃(𝜃+1)𝑦_{′𝑝}^{}−(𝜃−1)(𝜃+1)𝑦^{′}+\frac{1}{2}𝜃(𝜃−1)𝑦_{′−1}^{} \\ & =\frac{1}{2}(𝜃^{2}+𝜃)𝑦_{′𝑝}^{}−(𝜃^{2}−1)𝑦^{′}+\frac{1}{2}(𝜃^{2}−𝜃)𝑦_{′−1}^{}.\end{aligned}


$$

Now, we integrate this approximation from $0$ to $1{:}$

$$


\begin{aligned}∫_{10}^{}𝑞(𝜃)\,d𝜃 & =∫_{10}^{}(\frac{1}{2}(𝜃^{2}+𝜃)𝑦_{′𝑝}^{}−(𝜃^{2}−1)𝑦^{′}+\frac{1}{2}(𝜃^{2}−𝜃)𝑦_{′−1}^{})\,d𝜃 \\ & =\frac{1}{2}(\frac{1}{3}+\frac{1}{2})𝑦_{′𝑝}^{}−(\frac{1}{3}−1)𝑦^{′}+\frac{1}{2}(\frac{1}{3}−\frac{1}{2})𝑦_{′−1}^{}−0 \\ & =\frac{5}{12}𝑦_{′𝑝}^{}+\frac{2}{3}𝑦^{′}−\frac{1}{12}𝑦_{′−1}^{} \\ & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})\end{aligned}


$$

Therefore, the approximation of the increment in $y$ is

$$


\Delta y = \int_0^1 g(\theta) \,\mathrm{d}\theta\cdot\Delta x \approx \int_0^1 q(\theta) \,\mathrm{d}\theta\cdot\Delta x = \dfrac1{12}(5y'_p + 8y' - y'_{-1})\cdot\Delta x.


$$

It is this approximation that we use as the AM2 corrector. Putting it together, the $2$-step Adams-Bashforth-Moulton method is as follows:

$$


\begin{aligned}Predictor & : & Δ𝑦_{𝑝} & =\frac{1}{2}(3𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥 \\ Corrector & : & Δ𝑦 & =\frac{1}{12}(5𝑦_{′𝑝}^{}+8𝑦^{′}−𝑦_{′−1}^{})⋅Δ𝑥\end{aligned}


$$
