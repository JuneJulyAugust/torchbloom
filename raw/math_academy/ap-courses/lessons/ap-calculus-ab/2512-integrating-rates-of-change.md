# Integrating Rates of Change

Source: https://www.mathacademy.com/topics/2512?courseId=24
Topic ID: 2512

## Prerequisites

- [The Second Fundamental Theorem of Calculus](./613-the-second-fundamental-theorem-of-calculus.md)
- [Using the First Derivative Test to Classify Local Extrema](./1360-using-the-first-derivative-test-to-classify-local-extrema.md)
- [Integrating Exponential Functions Using Substitution](./3770-integrating-exponential-functions-using-substitution.md)

## Lesson

### Introduction

Suppose that a tank is filling up with water, and the rate at which water flows into the tank is given by

$$


r(t) = 600e^{-3t},


$$

where $r(t)$ is measured in liters per hour, and $t > 0$ is the time (in hours) since the water flow started.

Suppose we want to know how much water enters the tank between $1$ and $2$ hours.

Let's take note of the following:

- We're interested in the amount of water that enters the tank between $t=1$ and $t=2.$ In other words, we want the **net change in volume** between these times. We're *not* finding the total volume of water in the tank.

- We're given the **rate of change of volume** $r(t).$

To find the net change in volume, we integrate $r(t)$ between the two limits. This gives:

$$


\begin{aligned}∫_{21}600𝑒^{−3𝑡}\,d𝑡 & =−\frac{600}{3}𝑒^{−3𝑡}_{21} \\ & =−200𝑒^{−3𝑡}_{21} \\ & =−200(𝑒^{−6}−𝑒^{−3}) \\ & =200(𝑒^{−3}−𝑒^{−6}) \\ & =200𝑒^{−6}(𝑒^{3}−1)\end{aligned}


$$

### Example: Finding the Net Change of a Function Given Its Rate of Change

#### Question

At a shopping mall, the rate at which people are entering the mall is given by

$$


r(t) = 300t^2+50,


$$

where $r(t)$ is measured in people per hour, and $t>0$ is the number of hours since the mall opened. In addition, people are leaving the mall at a steady rate of $25$ people per hour.

1. Calculate the number of people that entered the mall in the first two hours.

2. Calculate the net change in the number of people inside the mall in the first 2 hours.

#### Explanation

****

People are entering the mall at a rate of $r(t) = 300t^2+50.$ To find out how many people entered the mall between $t=0$ and $t=2,$ we integrate $r(t)$ between these two limits:

$$


\begin{aligned}∫_{20}𝑟(𝑡)\,d𝑡 & =∫_{20}300𝑡^{2}+50\,d𝑡 \\ & =100𝑡^{3}+50𝑡_{20} \\ & =(100⋅2^{3}+50(2))−(0) \\ & =(800+100) \\ & =900\end{aligned}


$$

****

People are entering the mall at a rate of $r(t) = 300t^2+50$ people per hour, and are leaving the mall at a rate of $25$ people per hour. Therefore, the **** in the number of people inside the mall, which we'll call $R(t),$ is given by:

$$


\begin{aligned}𝑅(𝑡) & =𝑟(𝑡)−25\end{aligned}


$$

To find the **** in the number of people, we integrate $R(t)$ between $t=0$ and $t=2$:

$$


\begin{aligned}∫_{20}𝑅(𝑡)\,d𝑡 & =∫_{20}𝑟(𝑡)−25\,d𝑡 \\ & =\underset{900}{\underset{}{∫_{20}𝑟(𝑡)\,d𝑡}}−∫_{20}25\,d𝑡 \\ & =900−[25𝑡]_{20} \\ & =900−50 \\ & =850\end{aligned}


$$

Therefore, over the first two hours, there was a net increase of $850$ people.

### Finding Total Amounts Given Rates of Change

If we're interested to find the **total number** or **total amount** of some quantity, we should use the fundamental theorem of calculus.

Let's go back to the earlier example with the shopping mall (Example 1). Suppose that there are $2\,000$ people inside the mall at the moment that it opened. How many people in total are inside the mall after $2$ hours?

We already know that the **rate of change** in the number of people is $R(t).$ Therefore, the **total number of people** in the mall at time $t$, which we'll call $T(t)$ is given by:

$$


\begin{aligned}𝑇(𝑡) & =𝑇(0)+∫_{𝑡0}𝑅(𝑥)\,d𝑥 \\ & =𝑇(0)+∫_{𝑡0}𝑟(𝑥)−25\,d𝑥\end{aligned}


$$

**Important**: You'll notice that we changed the variable of integration from $t$ to $x.$ This is to ensure that $T$ comes out as a function of $t,$ and also so we don't get confused. When we have a definite integral, it does not matter which variable we use!

To work out how many people are inside the mall at $t=2,$ we substitute $t=2$ into the above:

$$


\begin{aligned}𝑇(2) & =𝑇(0)+∫_{20}𝑟(𝑥)−25\,d𝑥 \\ & =2\,000+\underset{850}{\underset{}{∫_{20}𝑟(𝑥)−25\,d𝑥}} \\ & =2\,000+850 \\ & =2\,850\end{aligned}


$$

### Example: Finding the Total Change of a Function Given Its Rate of Change

#### Question

The rate at which guests are arriving at a restaurant one evening is given by the function

$$


r(t) = 6t^2+2,


$$

where $r(t)$ is measured in guests per hour and $t > 0$ is the time in hours since the restaurant opened. Guests are also leaving at a steady rate of $6$ guests per hour. If there were $50$ guests in the restaurant when it opened, how many guests will be in the restaurant after $1$ hour?

#### Explanation

Guests are entering the restaurant at a rate of $6t^2+2$ guests per hour and are leaving at a rate of $6$ guests per hour. Therefore, the **** in the number of guests (call it $R(t)$) is

$$


\begin{aligned}𝑅(𝑡) & =𝑟(𝑡)−6 \\ & =6𝑡^{2}+2−6 \\ & =6𝑡^{2}−4\end{aligned}


$$

To find the **** after $t$ hours (call it $T(t)$), we apply the second fundamental theorem of calculus:

$$


\begin{aligned}𝑇(𝑡) & =𝑇(0)+∫_{𝑡0}𝑅(𝑥)\,d𝑥 \\ & =50+∫_{𝑡0}(6𝑥^{2}−4)\,d𝑥\end{aligned}


$$

To ensure that $T$ is a function of $t$ only, we use a different variable ($x$) for the integration.

To find out the number of guests after $1$ hour, we substitute $t=1$ into the above and evaluate.

$$


\begin{aligned}𝑇(1) & =50+∫_{10}(6𝑥^{2}−4)\,d𝑥 \\ & =50+[2𝑥^{3}−4𝑥]_{10} \\ & =50+[(2(1)^{3}−4(1))−(0)] \\ & =50−2 \\ & =48\end{aligned}


$$

### Example: Finding the Global Minimum or Maximum of a Function Given Its Rate of Change

#### Question

In example 2, we saw that the number of guests in a restaurant is given by

$$


T(t) = 50 + \int_0^t \left(6x^2-4\right)\,\textrm d x\,.


$$

Given that $T(t)$ has a local minimum for some $t>0,$ find the time when the number of guests is at its minimum value.

#### Explanation

To find the time when the number of guests is minimized, we need to solve $\dfrac{\textrm d T}{\textrm d t} = 0.$

Differentiating $T(t)$ with respect to $t$ gives:

$$


\begin{aligned}\frac{d𝑇}{d𝑡} & =\frac{d}{d𝑡}(50+∫_{𝑡0}(6𝑥^{2}−4)\,d𝑥) \\ & =\frac{d}{d𝑡}(50)+\frac{d}{d𝑡}∫_{𝑡0}(6𝑥^{2}−4)\,d𝑥 \\ & =\frac{d}{d𝑡}∫_{𝑡0}(6𝑥^{2}−4)\,d𝑥 \\ & =6𝑡^{2}−4\end{aligned}


$$

Solving $\dfrac{\textrm d T}{\textrm d t} = 0$ gives

$$


6t^2-4 = 0\qquad\Longrightarrow\qquad t = \sqrt{\dfrac{2}{3}}


$$

So we have $2$ critical points $t=\sqrt{\dfrac 2 3}$ and $t=0$ (the endpoint). But since the local minimum exists for $t>0,$ $t=\sqrt{\dfrac{2}{3}}$ must be the minimum value.
