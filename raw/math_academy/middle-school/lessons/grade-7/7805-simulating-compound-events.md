# Simulating Compound Events

Source: https://www.mathacademy.com/topics/7805?courseId=37
Topic ID: 7805

## Prerequisites

- [Experimental Probability for Compound Events](./7223-experimental-probability-for-compound-events.md)
- [Computing Probabilities of Compound Events](./7804-computing-probabilities-of-compound-events.md)

## Lesson

### Introduction

A **simulation** is a method of using a random process to model a real-world situation.

For a simulation to be valid, the probability of each outcome in the model must match the probability in the real situation.

For example, suppose a quality inspector finds that $1$ out of every $6$ products is defective.

This means the probability that a randomly selected product is defective is $\dfrac{1}{6}.$

To simulate this situation, we need a random process with $6$ equally likely outcomes, where $1$ outcome represents a defective product.

One way to do this is to roll a fair $6$-sided die and record whether a $1$ is rolled.

A fair $6$-sided die has $6$ possible outcomes, and exactly $1$ outcome is considered a success. So, the probability of rolling a $1$ is $\dfrac{1}{6},$ which matches the probability of selecting a defective product.

This makes the simulation valid.

### Alternative Simulations

There are multiple ways to simulate a single event.

Recall our previous example where we needed to simulate a probability of $\dfrac{1}{6}.$ As long as our model has $6$ equally likely outcomes, the simulation is valid.

Instead of rolling a single $6$-sided die, another valid method is to combine two distinct random processes. For example, we could:

- Flip a fair coin ($2$ possible outcomes)

- Spin a spinner with $3$ equal sections ($3$ possible outcomes)

Combining these creates $2 \times 3 = 6$ equally likely outcomes.

If exactly one of these combined outcomes (such as flipping Heads and spinning a $1$) is designated as "defective," then the probability of a defective outcome is $\dfrac{1}{6}.$

This matches the real situation perfectly, making our coin-and-spinner method a valid simulation.

### Example: Designing a Simulation for a Compound Event

#### Question

A streaming service finds that $1$ out of every $8$ users cancel their subscription each month. A data analyst wants to simulate $60$ users to estimate how many cancellations might occur. Which of the following would be a valid way to simulate whether a user cancels their subscription?

1. Rolling a fair $8$-sided die and recording whether a $1$ is rolled.

2. Flipping three fair coins and recording whether all three land on Heads.

3. Using a spinner with $4$ equal sections and recording whether it lands on one particular section.

#### Explanation

A simulation uses a random process to model a real situation. For the simulation to be valid, the probability of success in the model must match the probability in the real situation.

We are told that $1$ out of every $8$ users cancel their subscription. So, the probability that a randomly selected user cancels is $\dfrac{1}{8}.$

Now, let's see which of the potential simulations has the same probability.

- Simulation I ** valid. A fair $8$-sided die has $8$ outcomes, and $1$ outcome is considered a success. So, the probability is $\dfrac{1}{8}.$

- Simulation II ** valid. Flipping three coins has $8$ possible outcomes: Of these, $1$ outcome represents success: $\big\{(\text{H},\text{H},\text{H})\big\}.$ So, the probability is $\dfrac{1}{8}.$

- Simulation III is ** valid. A spinner with $4$ equal sections has $4$ outcomes, and $1$ outcome is considered a success. So, the probability is $\dfrac{1}{4}.$

In conclusion, the valid simulations are I and II.

### Example: Evaluating Frequencies With a Compound-Event Simulation

#### Question

A student is practicing free throws and makes a shot with probability $\dfrac{1}{3}.$ To simulate a set of $3$ shots, the student uses a spinner with $3$ equal sections, where landing on the "Star" section represents a made shot. The student repeats this for $36$ trials and records how many shots were made in each $3$-shot set.

In how many of the simulated sets did the student make at least $2$ shots?

#### Explanation

A simulation models a real situation using a random process.

In this simulation, spins are used to model outcomes of shots. Each spin represents one shot, and landing on a Star represents a made shot. Spinning the spinner $3$ times represents the outcomes of $3$ shots in one set.

The table shows the results of $36$ simulated sets. We are asked for the number of times the student made at least $2$ shots.

From the table, we see:

- The student obtained $2$ stars $8$ times, meaning $2$ shots were made in $8$ of the simulated sets.

- The student obtained $3$ stars $2$ times, meaning $3$ shots were made in $2$ of the simulated sets.

So, the student made at least $2$ shots in

$$



8 + 2 = \boxed{10}



$$

of the simulated sets.

### Probability From a Simulation

The probability of an event can be estimated using the results of a simulation. This estimated probability is given by

$$



P(\text{Event}) = \frac{\text{Number of successful trials}}{\text{Total number of trials}}.



$$

In a simulation, each trial represents one outcome of the situation being modeled.

For example, suppose a basketball player makes a shot with probability $\dfrac{1}{4}.$ To simulate two shots, a coach rolls two $4$-sided dice, where rolling a $1$ represents a made shot.

The coach performs $40$ simulated trials and records the number of made shots in each trial.

Suppose we want the probability that exactly $2$ shots are made.

From the table, there are $6$ trials in which exactly $2$ shots are made.

There are $40$ total trials, so the estimated probability is

$$



2



$$

The result is an estimate of the true probability based on the simulation data.

### Example: Estimating Compound Probabilities From Simulations

#### Question

A video game character has a $\dfrac{1}{4}$ chance of landing a "Power Strike" on any attack. To simulate a sequence of $2$ attacks, a tester rolls two $4$-sided dice, where rolling a $1$ represents a Power Strike. The tester repeats this simulation $40$ times and records the number of Power Strikes in each $2$-attack sequence.

Based on the simulation, what is the estimated probability that the character lands two Power Strikes?

#### Explanation

A simulation models a real situation using a random process. To find the estimated probability from a trial, we use

$$



P(\text{Event}) = \frac{\text{Number of successful trials}}{\text{Total number of trials}}.



$$

In this simulation, die rolls are used to model outcomes of attacks. Each die roll represents one attack, and rolling a $1$ represents a Power Strike. Rolling the dice twice represents the outcomes of $2$ attacks in one sequence.

The table shows the results of $40$ simulated sequences. We are asked how many times the character lands two Power Strikes.

From the table, we see that the tester obtained $2$ ones $6$ times, meaning two Power Strikes occurred in $6$ of the simulated sequences.

So, two Power Strikes occurred in $6$ of the simulated sequences.

Since there were $40$ simulations in total, the estimated probability is

$$



P(\text{Two Power Strikes}) = \dfrac{6}{40} = \dfrac{3}{20}.



$$
