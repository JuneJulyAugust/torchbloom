# Using Probability to Make Predictions

Source: https://www.mathacademy.com/topics/7222?courseId=126
Topic ID: 7222

## Prerequisites

- [Single Events in Probability](./709-single-events-in-probability.md)

## Lesson

### Introduction

We can use probability to predict how many times an event is likely to happen over many trials.

In particular, the estimated number of times an event occurs is the product of the total number of trials and the probability of the event occurring:

$$


\text{estimated number of event occurrences} = \text{total number of trials} \cdot P(\text{Event})


$$

For example, suppose a fair six-sided die is rolled $60$ times. The probability of rolling a $3$ is

$$


P(3) = \dfrac{1}{6}.


$$

So, the estimated number of times a $3$ will be rolled is

$$


60 \cdot \dfrac{1}{6} = 10.


$$

This tells us we expect about $10$ rolls to be a $3.$

However, this is only a prediction. The actual number of times a $3$ appears will probably be close to, but may be slightly more or slightly less than $10.$

In general, probability helps us estimate what will happen in the long run, but it does not guarantee an exact result.

### Example: Using Probability to Make Predictions

#### Question

A bag contains $4$ red marbles, $5$ blue marbles, and $3$ yellow marbles. A marble is drawn at random $92$ times and replaced each time. What is the expected number of times a red or blue marble will be drawn?

#### Explanation

The estimated number of times an event occurs is the product of the total number of trials and the probability of the event occurring:

$$


\text{estimated number of event occurrences} = \text{total number of trials} \cdot P(\text{Event})


$$

The probability of drawing a red or blue marble is

$$


P(\text{red or blue}) = \dfrac{4+5}{4+5+3} = \dfrac{9}{12} = \dfrac{3}{4}.


$$

Substituting into the formula, the expected number of times a red or blue marble will be drawn in $92$ draws is

$$


92 \cdot \dfrac{3}{4} = 69.


$$

### Example: Using Probability to Make Predictions of Overlapping Events

#### Question

A spinner has $12$ equal sections labeled with the numbers $1$ through $12.$ The spinner is spun $60$ times. What is the expected number of times the spinner lands on a number greater than $4$ or a multiple of $2?$

#### Explanation

The estimated number of times an event occurs is the product of the total number of trials and the probability of the event occurring:

$$


\text{estimated number of event occurrences} = \text{total number of trials} \cdot P(\text{Event})


$$

There are $12$ possible outcomes:

$$


\{1,2,3,4,5,6,7,8,9,10,11,12\}


$$

Of these outcomes, $10$ of them are greater than $4$ or a multiple of $2{:}$

$$


\{2,4,5,6,7,8,9,10,11,12\}


$$

So, the probability of landing on a number greater than $4$ or a multiple of $2$ is

$$


P(\text{greater than 4 or multiple of 2}) = \dfrac{10}{12} = \dfrac{5}{6}.


$$

Substituting into the formula, the expected number of times the spinner lands on a number greater than $4$ or a multiple of $2$ is

$$


60 \cdot \dfrac{5}{6} = 50.


$$

### Example: Interpreting Predictions Using Probability

#### Question

A school cafeteria tracks students’ lunch choices. Out of $200$ students, $120$ choose pizza, $50$ choose sandwiches, and $30$ choose salads. A student is selected at random $400$ times, with replacement. Complete the statements below.

$\qquad$The probability of selecting a student who chooses a sandwich or a salad is $\boxed{\phantom{\dfrac{2}{5}}}.$

$\qquad$The estimated number of times a sandwich or salad is chosen in $400$ selections is $\boxed{\phantom{160}}.$

$\qquad$We expect that the actual number of sandwich or salad selections will be $\boxed{\phantom{\mathrm{close to}}}$ $\boxed{\phantom{160}}.$

#### Explanation

The estimated number of times an event occurs is the product of the total number of trials and the probability of the event occurring:

$$


\text{estimated number of event occurrences} = \text{total number of trials} \cdot P(\text{Event})


$$

The probability of selecting a student who chooses a sandwich or a salad is

$$


P(\text{sandwich or salad}) = \dfrac{50+30}{120+50+30} = \dfrac{80}{200} = \boxed{\dfrac{2}{5}}.


$$

Substituting into the formula, the estimated number of times a sandwich or salad is chosen in $400$ selections is

$$


400 \cdot \dfrac{2}{5} = \boxed{160}.


$$

However, probability gives an estimate, not an exact result. The actual number of times may be slightly more or slightly less than $160.$

Therefore, we expect that the actual number of sandwich or salad selections will be $\boxed{\text{close to}}$ $\boxed{160}.$

### Reliability of Experiments

When we use probability to make predictions, the number of trials affects the reliability of the estimate.

In general, predictions based on a larger number of trials tend to be more reliable, because they are based on more data. Predictions based on fewer trials are less reliable because they may be more susceptible to random variation.

If two estimates are based on the same number of trials, then they are equally reliable.

For example, suppose two students, Amy and Betty, are estimating how often a spinner lands on blue.

- Amy spins the spinner $25$ times and gets blue $10$ times.

- Betty spins the spinner $100$ times and gets blue $48$ times.

Their experimental probabilities, respectively, are

$$


P(\text{blue}) = \dfrac{10}{25} = \dfrac{2}{5} \qquad \text{and} \qquad P(\text{blue}) = \dfrac{48}{100} = \dfrac{12}{25}.


$$

Here, we have two potential experimental probabilities from which we can estimate how often a spinner lands on blue. However, Betty's estimate would be more reliable because it is based on more trials.

In general, predictions based on larger amounts of data are more dependable.

### Example: Comparing the Reliability of Experiments

#### Question

Two students, Ava and Noah, each conduct the same experiment. They roll a die and record how many times it lands on an even number.

- Ava rolls the die $30$ times and gets an even number $18$ times.

- Noah rolls the die $150$ times and gets an even number $84$ times.

Based on their experimental probabilities, complete the statements below.

$\qquad$Out of $240$ rolls, Ava expects to get an even number about $\boxed{\phantom{144}}$ times.

$\qquad$Out of $240$ rolls, Noah expects to get an even number about $\boxed{\phantom{134.4}}$ times.

$\qquad$ Ava's estimate for the number of even numbers in $240$ rolls is $\boxed{\phantom{\mathrm{less reliable than}}}$ Noah's estimate.

#### Explanation

The estimated number of times an event occurs is the product of the total number of trials and the probability of the event occurring:

$$


\text{estimated number of event occurrences} = \text{total number of trials} \cdot P(\text{Event})


$$

In general, the greater the number of trials, the closer the experimental probability is to the true probability, and the more reliable the estimate becomes.

First, let's find each student’s experimental probability.

- For Ava, the experimental probability of rolling an even number is Substituting into the formula, the expected number of even numbers in $240$ rolls is

- For Noah, the experimental probability of rolling an even number is Substituting into the formula, the expected number of even numbers in $240$ rolls is

Finally, since Ava's estimate for the number of even numbers in $240$ rolls is based on ** trials than Noah's estimate $(30 < 150),$ Ava's estimate is $\boxed{\text{less reliable than}}$ Noah's estimate.
