# Introduction to Hypothesis Testing

Source: https://www.mathacademy.com/topics/2995?courseId=73
Topic ID: 2995

## Prerequisites

- [Modeling With the Binomial Distribution](./1395-modeling-with-the-binomial-distribution.md)
- [The CDF of the Binomial Distribution](./3270-the-cdf-of-the-binomial-distribution.md)
- [Sampling Distributions](./3864-sampling-distributions.md)

## Lesson

### Introduction

**Hypothesis testing** is a widely-used statistical technique used to make inferences about population parameters from sample data.

Suppose a factory makes a particular item where the probability that a randomly selected item is defective is $0.03$. After updating the software on the production line, the factory's manager suspects that the proportion of defective items has *increased*. They wish to design and conduct a statistical experiment to determine whether or not their suspicions are correct.

Loosely speaking, the manager should conduct a random sample of factory items and check the proportion of defective ones. If the proportion in the sample is much larger than $0.03,$ this may suggest that the proportion of defective items for the *entire population* has increased.

More formally, we can conduct a statistical hypothesis test to confirm or deny the manager's suspicion. The six steps of a hypothesis test are:

- **Step 1**: Determine the population parameter we're interested in. In this case, we're interested in the proportion of defective items produced by the factory. Let's state this formally. $\qquad$ *We define $p$ as "the probability that a randomly selected item is defective."*

- **Step 2**: Define our hypotheses. We always form two hypotheses when conducting hypothesis tests: We first form a **null hypothesis**. The null hypothesis states that the situation hasn't changed, i.e., the probability that a randomly selected item is defective is still $0.03.$ We write this as follows: Then, we form an **alternative hypothesis**. In this case, the alternative hypothesis states that the probability has *increased,* in line with our suspicions. We write this as follows:

- **Step 3**: Design a suitable experiment to test our hypotheses. A suitable experiment to test our hypotheses in this case is as follows: $\qquad$*We randomly select $100$ items and count the number of defective ones.* The sample size of $100$ here is arbitrary. The larger our experiment, the more likely our conclusion will be correct.

- **Step 4**: Set a **significance level.** The significance level is a small, positive number representing an unlikely (or very unlikely) probability. The significance level can be any small probability we like, but common values are $5\%$ (unlikely), and $1\%$ (very unlikely). We usually denote our chosen significance level as $\alpha.$ $\qquad$*Let's pick the significance level $\alpha = 5\%$ for this experiment.*

- **Step 5**: Define and calculate a **test statistic.** The test statistic is computed from experimental data and must provide evidence for or against the population parameter we wish to test. In our case, we might define a suitable test statistic as follows: $\qquad X=$"*the number of defective items in our sample*." We then run our experiment and compute the test statistic based on the results.

- **Step 6**: Draw a **conclusion.** Once the test statistic is calculated, one of two possible conclusions can be drawn: The result given by the test statistic is *unlikely* (or very unlikely) under the null hypothesis. In this case, we *reject* $H_0.$ The result given by the test statistic is *not unlikely* under the null hypothesis. In this case, we *do not reject* $H_0.$

We can summarize the process in the following flowchart.

![Instructional graphic](../../lesson-assets/probability-and-statistics/topic-2995/7250c910df52b329.png)

### Understanding Hypothesis Tests

To confirm the manager's suspicions about the proportion of defective items, they need to collect enough statistical evidence to *reject* the null hypothesis in favor of the alternative hypothesis.

In this example, the manager's experiment requires them to randomly pick $100$ items and compare the number of defective ones with that predicted by the null hypothesis. Let's run through some possible scenarios to build some intuition.

- Suppose we ran our experiment and found $20$ defective items out of $100.$ This is extremely unlikely if the null hypothesis is true. Thus, this experimental result suggests we should *reject the null hypothesis*.

- On the other hand, suppose we ran our experiment and found $4$ defective items out of $100.$ This result is not unusual if the null hypothesis is true. Thus, this experimental result suggests we should *not reject the null hypothesis*.

In general, when we conduct a hypothesis test and run an experiment, one of two things will happen:

- If the result of the experiment is **statistically significant,** meaning that it is unlikely to have happened purely by chance (the probability is smaller than the chosen *significance level*) under the assumptions laid out by the null hypothesis, then we *reject* the null hypothesis in favor of the alternative hypothesis.

- Otherwise, if there is insufficient statistical evidence to suggest that the percentage has increased, we *do not reject* the null hypothesis.

Hypothesis tests are often compared to a trial by jury. Suppose a defendant is accused of a crime. In the United States and many other countries, a defendant is presumed innocent at the beginning of the trial. It is down to the prosecution to present enough evidence to convince the jury that the defendant is guilty after all. Hypothesis tests are the same. We assume the null hypothesis is true unless we're presented with enough statistical evidence to reject it.

Finally, since the alternative hypothesis involves an inequality, we call this a **one-tailed** hypothesis test. We'll meet **two-tailed tests** in future lessons.

Let's get some practice at defining null and alternative hypotheses.

### Example: Identifying Null and Alternative Hypothesis

#### Question

The sports magazine editor estimates that $28\%$ of the articles he receives for review require corrections. After suggesting a new grammar checker to the reporters preparing the articles, he wants to know if the number of articles that require corrections has **. So, he decides to carry out a hypothesis test.

Let $p$ represent the proportion of articles that require corrections after the reporters start using the new grammar checker. State the null and alternative hypotheses for this test.

#### Explanation

A hypothesis is a statement about a population parameter we wish to test by collecting sample data.

In a statistical hypothesis test, we form two hypotheses:

- The null hypothesis $H_0,$ which we assume to be correct unless proven otherwise. It is our default assumption.

- The alternative hypothesis, $H_1,$ is what we conclude about the population parameter if statistical evidence suggests that $H_0$ is incorrect.

A hypothesis test is similar to a trial by jury. We assume the null hypothesis is true unless there is enough statistical evidence to reject it.

In this case, the population parameter we wish to test is $p,$ the proportion of articles that require corrections after the reporters start using the new grammar checker.

- The default assumption is that the proportion of articles that require corrections has not changed. Therefore, the null hypothesis is $H_0: \boxed{\color{blue}p = 0.28}.$

- The editor wishes to test the hypothesis that the proportion of articles that require corrections **. Therefore, the alternative hypothesis is $H_1: \boxed{\color{blue}p < 0.28}.$

### Carrying Out a Hypothesis Test

Suppose we have a coin that we suspect is biased *against* landing on heads (i.e., the coin is *less* likely to land on heads than tails). We wish to design a hypothesis test to determine whether or not our suspicions are correct.

We can use a so-called **left-tailed** hypothesis test for this purpose. To do that, we proceed as follows:

- **Step 1**: Determine the population parameter we're interested in. $\qquad$ *We define $p$ as "the probability that the coin lands on heads when tossed randomly."*

- **Step 2**: Define our hypotheses: *Since we want to check whether the coin is biased **** landing on heads, we have the following null and alternative hypotheses:* We use a "less than" symbol (the left tail of the probability distribution) for $H_1$ because if the coin is biased against heads, then the probability that the coin lands on heads must be less than one-half.

- **Step 3**: Design a suitable experiment to test our hypotheses. $\qquad$ *We toss our coin $10$ times and count the total number of heads.*

- **Step 4**: Set a significance level $\alpha.$ $\qquad$ *For our experiment, let's pick the significance level $\alpha = 5\%.$*

- **Step 5**: Define and calculate a test statistic. In our case, we might define a suitable test statistic as follows: $\qquad X=$ "*the number of times the coin lands on heads after $10$ random tosses*." Notice that under the conditions specified in the null hypothesis, the random variable $X$ must follow a binomial distribution: Suppose we toss the coin $10$ times and get only ${\color{red}{1}}$ head. If the null hypothesis is true, then

- **Step 6**: Draw a conclusion. The probability $P(X\leq {\color{red}{1}})$ is *smaller than* our significance level of $5\%.$ This means that our result *is* statistically significant. In other words, it is unlikely that this event could have occurred if the null hypothesis is true. Therefore, we should *reject* the null hypothesis and conclude that the coin is biased.

You might be wondering why our test statistic was $P(X\leq {\color{red}{1}})$ rather than $P(X={\color{red}{1}}).$ When conducting hypothesis tests, we consider not just the observed outcome, but all outcomes that are *at least as extreme*—meaning outcomes that point even more strongly toward the alternative hypothesis. Since our alternative hypothesis is $p < \dfrac{1}{2},$ lower values of $X$ provide stronger evidence for it. The cumulative probability $P(X\leq 1)$ accounts for $X = 1$ and the even more extreme outcome $X = 0.$

**Right-tailed** hypothesis tests are similar. The difference is the alternative hypothesis involves a "greater than" sign. Let's see an example.

### Example: Identifying the Significance Level and Test Statistic

#### Question

Companies A and B manufacture batteries for cell phones. It is known that $4\%$ of all batteries produced by Company A are defective. Company A's general manager claims that Company B's production has a higher percentage of defective batteries. They decide to test the following hypotheses at the $10\%$ significance level.

- $H_0: \quad p = 0.04$

- $H_1: \quad p > 0.04$

Here, $p$ is the proportion of defective batteries produced by Company B.

The manager of Company A samples $60$ of Company B's batteries and finds that only $2$ of them are defective.

Let $X$ be the number of defective batteries in a random sample produced by Company B. State the distribution of $X$ under $H_0,$ the value of $\alpha,$ and specify a suitable test statistic for this hypothesis test.

#### Explanation

A hypothesis is a statement about a population parameter we wish to test by collecting sample data.

In a statistical hypothesis test, we form two hypotheses:

- The null hypothesis $H_0,$ which we assume to be correct unless proven otherwise. It is our default assumption.

- The alternative hypothesis, $H_1,$ is what we conclude about the population parameter if statistical evidence suggests that $H_0$ is incorrect.

A hypothesis test is similar to a trial by jury. We assume the null hypothesis is true unless there is enough statistical evidence to reject it.

The significance level $\alpha$ is a threshold probability that we consider unlikely (or very unlikely) under the null hypothesis.

In this case, the population parameter we wish to test is $p,$ the proportion of defective batteries produced by Company B.

- Under the null hypothesis, the probability of getting $x$ defective batteries out of $60$ produced is equivalent to $x$ "successes" over $60$ Bernoulli trials, where the probability of success on each trial is $p=0.04.$ Therefore,

- The manager collected the data and found that only $2$ batteries out of $60$ were defective. Therefore, a suitable test statistic is $P(\boxed{\color{blue}X\geq 2}).$ Note that: Since we wish to test $p > 0.04,$ this is a **. We're interested in $X\geq 2,$ not just $X=2.$ This is because we want to include ** events in the right tail at least as extreme or more extreme than $X=2.$

- For this test, the significance level is $\alpha = 10\% = \boxed{\color{blue}0.1}.$

### Example: Conducting Left-Tailed Tests

#### Question

In a textile factory, the manager estimated that $10\%$ of the T-shirts produced by a faulty machine are defective. After repairing the machine, the manager wants to know if the proportion of defective T-shirts has decreased. They decide to conduct a hypothesis test at the $5\%$ significance level.

The manager samples a batch of $120$ T-shirts produced by the repaired machine and notices that only $4$ of them are defective. The manager compares this experimental evidence against a null hypothesis, making use of the following cumulative distribution table for $X\sim B(120,0.1).$

Fill in the missing information from the following statements.

If $X$ represents the number of defective T-shirts in a random sample of $120$ T-shirts produced by the new machine, then a suitable test statistic is

$$


P\big(\boxed{\phantom{\textrm{X \leq 4}}} \big)= \boxed{\phantom{\textrm{0.0000}}}.


$$

Since $P\big(\boxed{\phantom{\textrm{X \leq 4}}}\big)$ $\boxed{\phantom{\textrm{<}}}$ $5\%,$ there is $\boxed{\phantom{\textrm{sufficient}}}$ evidence to reject $H_0.$

Therefore, we $\boxed{\phantom{\textrm{can conclude}}}$ that the proportion of defective T-shirts has decreased since the machine was replaced.

#### Explanation

Let $p$ be the proportion of defective T-shirts. Then, we have the following null and alternative hypotheses:

- $H_0: \quad p = 0.1$

- $H_1: \quad p < 0.1$

The significance level is $\alpha =5\% = 0.05.$

Under the null hypothesis, the probability of finding $x$ defective T-shirts in a sample of $120$ is equivalent to $x$ "successes" over $120$ Bernoulli trials, where the probability of success on each trial is $p=0.1.$ Therefore,

$$


X\sim B(120, 0.1).


$$

The manager collected the data and found that only $4$ T-shirts out of $120$ were defective. Therefore, a suitable test statistic is $P(X\leq 4).$

Assuming the null hypothesis, the value of our test statistic is

$$


\begin{aligned}𝑃(𝑋≤4) & =0.0056.\end{aligned}


$$

Let's interpret this result:

- Since $P(\boxed{\color{blue}X\leq 4}) \boxed{\color{blue}<} 5\%,$ the experimental results are unlikely under the null hypothesis.

- In other words, there is $\boxed{\color{blue}\textrm{sufficient}}$ evidence to reject $H_0.$

- Therefore, we $\boxed{\color{blue}\textrm{can conclude}}$ that the proportion of defective T-shirts has decreased since the machine was repaired.

****: In hypothesis testing, the so-called **** is the probability of observing a test statistic as extreme as, or more extreme than, the observed one, assuming that the null hypothesis is true. In this case, the p-value is $0.0056.$ We won't use the p-value terminology very often, but you should know it exists.

### Example: Conducting Right-Tailed Tests

#### Question

A telecommunications company believes that $50\%$ of its customers must wait at least $3$ minutes for their call to be answered. The director of the customer service office claims that the true percentage is even higher. They conduct a hypothesis test at the $1 \%$ significance level to test this claim.

After randomly sampling $20$ customers, the director determined that $15$ of them waited for at least $3$ minutes. The director compares this experimental evidence against a null hypothesis, making use of the following cumulative distribution table for $X\sim B(20,0.5).$

Fill in the missing information from the following statements.

If $X$ represents the number of randomly selected customers who waited at least $3$ minutes, then an appropriate test statistic is $P\big(\boxed{\phantom{\textrm{0.0000}}}\big) = \boxed{\phantom{\textrm{0.0000}}}.$

Since $P\big(\boxed{\phantom{\textrm{0.0000}}}\big)\, \boxed{\phantom{\textrm{0}}}\, 1\%,$ there is $\boxed{\phantom{\textrm{0.000000}}}$ evidence to reject $H_0.$

Therefore, we $\boxed{\phantom{\textrm{cannot conclude}}}$ that the percentage of customers who must wait at least $3$ minutes is higher than expected.

#### Explanation

Let $p$ be the probability that a randomly selected customer waited at least $3$ minutes. Then, we have the following null and alternative hypotheses.

- $H_0: \quad p = 0.5$

- $H_1: \quad p > 0.5$

The significance level $\alpha = 1\% = 0.01.$

Under the null hypothesis, the probability that $x$ customers waited at least $3$ minutes in a sample of $20$ is equivalent to $x$ "successes" over $20$ Bernoulli trials, where the probability of success in each trial is $p = 0.5.$ Therefore,

$$


X \sim B(20, 0.5).


$$

The director conducted an experiment and found that $15$ of the $20$ customers waited at least $3$ minutes to be served. Therefore, a suitable test statistic is $P(X \geq 15).$

Under the null hypothesis, the value of our test statistic is

$$


\begin{aligned}𝑃(𝑋≥15) & =1−𝑃(𝑋≤14) \\ & =1−0.9793 \\ & =0.0207.\end{aligned}


$$

Let's interpret this result:

- Since $P(\boxed{\color{blue}X \geq 15}) \boxed{\color{blue}\gt} 1\%,$ this experimental result is likely under the null hypothesis.

- In other words, there is $\boxed{\color{blue}\textrm{insufficient}}$ evidence to reject $H_0.$

- Therefore, we $\boxed{\color{blue}\textrm{cannot conclude}}$ that the percentage of customers who must wait at least $3$ minutes is higher than expected.
