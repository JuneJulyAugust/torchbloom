# Time-Shifting Exponential Models

Source: https://www.mathacademy.com/topics/6220?courseId=120
Topic ID: 6220

## Prerequisites

- [Interpreting Exponential Decay](../../../high-school/traditional/lessons/algebra-i/1629-interpreting-exponential-decay.md)
- [Interpreting Exponential Growth](../../../high-school/traditional/lessons/algebra-i/2465-interpreting-exponential-growth.md)
- [Describing Function Composition](../../../high-school/traditional/lessons/algebra-i/3817-describing-function-composition.md)
- [Unit Conversions Using Units of Time](../../../high-school/traditional/lessons/algebra-i/3870-unit-conversions-using-units-of-time.md)

## Lesson

### Introduction

One of the advantages of exponential models is their adaptability. If we change the time unit, say, from years to months, or shift the point from which we start counting time, the model can be rewritten without altering its fundamental behavior.

When we change the time unit, the growth factor stays the same. What changes is the exponent, since it’s just keeping track of how many time periods have passed.

Let's illustrate how this works with an example.

Suppose the function

$$


N(t) = 5{,}150 \cdot (1.05)^t


$$

models the number of users of a subscription service $t$ *years* after its launch. How can we rewrite this function so that it models the number of users after $m$ *months* since the service was launched?

Our goal is to rewrite this model in terms of months rather than years.

Note the following:

- Since there are $12$ months in a year, we substitute $t=\dfrac{m}{12}$ into the original equation.

- We *divide* by $12$ (not multiply) because we want $m=12$ months to correspond to $t=1$ year.

Substituting this into our model, we get a new model, given by

$$


n(m) = N\left(\dfrac{m}{12}\right) = 5{,}150 \cdot (1.05)^{m/12}.


$$

This new function $n(m)$ models the number of users as a function of time in *months* after the service’s launch.

### Avoiding Common Pitfalls

When rewriting an exponential model in different time units, a common mistake is mixing up whether to *multiply* or *divide* by the conversion factor.

- When going from longer units to shorter units, we *divide*. For example, suppose models a bacterial culture $t$ days after it is placed in a dish. Let's assume we want to express this in terms of hours instead of days. Since there are $24$ hours in a day, we substitute We *divide* by $24$ so that $h=24$ hours corresponds to $t=1$ day.

- When going from shorter units to longer units, we *multiply*. For example, suppose models the number of video views $t$ seconds after upload. Let's assume we want to express this in terms of minutes instead of seconds. Since there are $60$ seconds in a minute, we substitute We *multiply* by $60$ so that $m=1$ minute corresponds to $t=60$ seconds.

### Example: Converting a Model to Different Time Units

#### Question

The function

$$


v(t) = 2,250 \cdot (1.09)^{(1/6)t}


$$

models the number of video views $t$ seconds after a clip is uploaded. What function models the number of video views $m$ minutes after the clip is uploaded?

#### Explanation

We are given the exponential model

$$


v(t) = 2,250 \cdot (1.09)^{(1/6)t},


$$

where $t$ represents the number of seconds after upload. We want to rewrite this model in terms of minutes rather than seconds.

Note the following:

- Since there are $60$ seconds in a minute, we substitute $t=60m$ into the original equation.

- We ** by $60$ (not divide) because we want $m=1$ minute to correspond to $t=60$ seconds.

Substituting, we get the model

$$


\begin{aligned}𝑉(𝑚)=𝑣(60𝑚) & =2,250⋅(1.09)^{(1/6)⋅(60𝑚)} \\ & =2,250⋅(1.09)^{10𝑚}.\end{aligned}


$$

This models the number of video views as a function of time in minutes after the clip is uploaded.

### Interpreting Exponential Models Using Different Time Units

Suppose the function

$$


D(t) = 1,250 \cdot (1.05)^{(3/4)t}


$$

models the value, in thousands of dollars, of an investment $t$ years after it is made.

Note that some exponential models adjust the measurement of time by including a rescaling coefficient in the exponent, such as $3/4$ in this example.

The investors ask their investment manager the following question:

*By what percentage is the investment predicted to increase by every $4$ months?*

Let's start by rewriting this model in terms of months instead of years.

- Since there are $12$ months in a year, we substitute $t=\dfrac{m}{12}$ into the original equation.

- We *divide* by $12$ (not multiply) because we want $m=12$ months to correspond to $t=1$ year.

Substituting, we get a model $d(m)$ for the value of the investment as a function of time in months $m$.

$$


\begin{aligned}𝑑(𝑚)=𝐷(\frac{𝑚}{12}) & =1,250⋅(1.05)^{(3/4)⋅(𝑚/12)} \\ & =1,250⋅(1.05)^{𝑚/16}\end{aligned}


$$

Now, we want to find the percentage increase over $4$ months. Inspecting the model in terms of months $d(m),$ the growth factor over $m$ months is

$$


(1.05)^{m/16}.


$$

So, the growth factor over $4$ months is

$$


(1.05)^{4/16} = (1.05)^{1/4} \approx 1.012272.


$$

This corresponds to an increase of approximately

$$


1.012272 - 1 = 0.012272 \approx 1.23\%,


$$

rounded to $2$ decimal places.

Therefore, the investment is predicted to increase by $1.23\%$ every $4$ months.

### Example: Determining a Percentage Increase

#### Question

The function

$$


k(t) = 650 \cdot (1.04)^{(2/5)t}


$$

models the number of messages sent $t$ seconds after a chat stream begins. According to the model, what percentage are messages predicted to increase by every $1$ minute? Round your answer to two decimal places.

#### Explanation

We are given the exponential model

$$


k(t) = 650 \cdot (1.04)^{(2/5)t},


$$

which represents messages $t$ seconds after the stream begins. We want to rewrite this model in terms of minutes instead of seconds.

Note the following:

- Since there are $60$ seconds in a minute, we substitute $t=60m$ into the original equation.

- We ** by $60$ (not divide) because we want $m=1$ minute to correspond to $t=60$ seconds.

Substituting, we get a model $K(m)$ for messages as a function of time in minutes $m$.

$$


\begin{aligned}𝐾(𝑚)=𝑘(60𝑚) & =650⋅(1.04)^{(2/5)⋅(60𝑚)} \\ & =650⋅(1.04)^{24𝑚}\end{aligned}


$$

Now, we want to find the percentage increase over $1$ minute. Inspecting the model in terms of minutes $K(m),$ we see that the growth factor over $m$ minutes is

$$


(1.04)^{24m}.


$$

So, the growth factor over $1$ minute is

$$


(1.04)^{24} \approx 2.563\,304.


$$

This corresponds to an increase of approximately

$$


2.563\,304 - 1 = 1.563\,304 \approx 156.33\%,


$$

rounded to $2$ decimal places.

Therefore, messages are predicted to increase by $156.33\%$ every $1$ minute.

### Example: Determining a Percentage Decrease

#### Question

The function

$$


P(t) = 775 \cdot (0.95)^{(3/4)t}


$$

models the population of bacteria in a sealed container $t$ weeks after a chemical is introduced. According to the model, what percentage is the population predicted to decrease by every $2$ days? Round your answer to two decimal places.

#### Explanation

#### Explanation:

We are given the exponential model

$$


P(t) = 775 \cdot (0.95)^{(3/4)t},


$$

which represents the population $t$ weeks after the chemical is introduced. We want to rewrite this model in terms of days instead of weeks.

Note the following:

- Since there are $7$ days in a week, we substitute $t=\dfrac{d}{7}$ into the original equation.

- We ** by $7$ (not multiply) because we want $d=7$ days to correspond to $t=1$ week.

Substituting, we get a model $p(d)$ for the population as a function of time in days $d$ after the chemical is introduced:

$$


\begin{aligned}𝑝(𝑑)=𝑃\,(\frac{𝑑}{7}) & =775⋅(0.95)^{(3/4)⋅(𝑑/7)} \\ & =775⋅(0.95)^{3𝑑/28}\end{aligned}


$$

Now, we want to find the percentage decrease over $2$ days. Inspecting the model in terms of days $p(d),$ we see that the decay factor over $d$ days is

$$


(0.95)^{3d/28}.


$$

So, the decay factor over $2$ days is

$$


(0.95)^{3\cdot 2/28} = (0.95)^{3/14} \approx 0.989\,069.


$$

This corresponds to a decrease of approximately

$$


1 - 0.989\,069 = 0.010\,931 \approx 1.09\%,


$$

rounded to $2$ decimal places.

Therefore, the population is predicted to decrease by $1.09\%$ every $2$ days.

### Example: Determining the Time Period Required to Yield a Percentage Change

#### Question

The function

$$


C(t) = 95 \cdot (1.05)^{(5/2)t}


$$

models the number of data packets processed, in thousands, by a server $t$ minutes after a throughput upgrade. According to the model, in how many seconds is the number of packets expected to increase by $5\%?$

#### Explanation

We are given the exponential model

$$


C(t) = 95 \cdot (1.05)^{(5/2)t},


$$

which represents the number of data packets processed, in thousands, $t$ minutes after the upgrade. We want to rewrite this model in terms of seconds rather than minutes.

Note the following:

- Since there are $60$ seconds in a minute, we substitute $t=\dfrac{s}{60}$ into the original equation.

- We ** by $60$ (not multiply) because we want $s=60$ seconds to correspond to $t=1$ minute.

Substituting, we get a model $c(s)$ for the number of packets as a function of time in seconds $s$ after the upgrade:

$$


\begin{aligned}𝑐(𝑠)=𝐶(\frac{𝑠}{60}) & =95⋅(1.05)^{(5/2)⋅(𝑠/60)} \\ & =95⋅(1.05)^{𝑠/24}\end{aligned}


$$

The base $1.05$ means that the number of packets grows by $5\%$ each time the exponent increases by $1,$ i.e., once every growth period.

The exponent $\dfrac{s}{24}$ shows that for every increase in $s=24$ seconds, the exponent increases by $1.$

Therefore, the number of packets is expected to increase by $5\%$ every ${24}$ seconds.
