# Bayes' Theorem

Source: https://www.mathacademy.com/topics/3272?courseId=109
Topic ID: 3272

## Prerequisites

- [The Law of Total Probability](./773-the-law-of-total-probability.md)

## Lesson

### Introduction

For two events $A$ and $B,$ **Bayes’ theorem** states that

$$



P(A|B)=\dfrac{P(B|A)P(A)}{P(B)}.



$$

Deriving Bayes' theorem is straightforward. First, recall that the multiplication law states that

$$



P(A|B) = \dfrac{P(A\cap B)}{P(B)}.\qquad\qquad (\ast)



$$

Swapping $A$ and $B$ in the multiplication law and noting that $P(B\cap A) = P(A\cap B),$ we have

$$



P(B|A) = \dfrac{P(A\cap B)}{P(A)}



$$

which can be written as

$$



P(A\cap B) = P(B|A)P(A).



$$

Substituting the above expression for $P(A\cap B)$ into $(\ast)$ gives Bayes' theorem.

We'll discuss the significance of Bayes' theorem shortly. But for now, let's get some practice applying the formula.

### Example: Computing a Conditional Probability Using Bayes' Theorem

#### Question

Given that $P(K|L) = 0.15,$ $P(K) = 0. 6,$ and $P(L) = 0.4,$ compute $P(L|K).$

#### Explanation

Using Bayes' theorem, we have

$$



\begin{aligned}𝑃(𝐿|𝐾) & =\frac{𝑃(𝐾|𝐿)𝑃(𝐿)}{𝑃(𝐾)} \\ & =\frac{(0.15)(0.4)}{0.6} \\ & =\frac{0.06}{0.6} \\ & =0.1.\end{aligned}



$$

### The Significance of Bayes' Theorem

Bayes' theorem states that

$$



P(A|B)=\dfrac{P(B|A)P(A)}{P(B)}.



$$

For reasons that will become clear shortly, we'll rewrite Bayes' theorem in a slightly different (but equivalent) way, as follows:

$$



P(A|B)=P(A) \cdot \dfrac{P(B|A)}{P(B)}



$$

Bayes' theorem is significant because it allows us to update our belief that a particular hypothesis is true when new evidence comes to light. For this reason, it has numerous applications in science, computer science, and engineering.

For example, suppose a doctor wishes to assess the probability that a certain patient is infected with a particular disease. It is known that those aged $65$ or older have a higher chance of carrying the disease.

Let's define the events $A$ and $B$ as follows:

- $A=$ the event that a randomly selected patient has the disease

- $B=$ the event that a randomly selected patient is $65$ years old or more

Then, Bayes' theorem gives the following:

$$



{\color{blue}{P(\textrm{has disease} \,|\, \textrm{patient is } 65+)}} = {\color{purple}{P(\textrm{has disease})}} \cdot \dfrac{P(\textrm{patient is } 65+ \,|\, \textrm{has disease})}{P({\textrm{patient is } 65+})}



$$

Let's introduce some new terminology:

- ${\color{purple}{P(\textrm{has disease})}}$ is called the **prior.** It tells us the probability that a randomly selected patient has the disease *without considering any other factors*.

- ${\color{blue}{P(\textrm{has disease} \,|\, \textrm{patient is} 65+)}}$ is called the **posterior**. It tells us the probability that a randomly selected patient has the disease *taking into consideration* that they are $65$ or older.

- $P(\textrm{patient is} 65+ \,|\, \textrm{has disease})$ is called the **likelihood.** It tells us the proportion of infected people that are $65$ or older. This quantity could be established by taking a random sample from the population of infected people and computing the ratio of those that are $65$ or older.

Therefore, Bayes' theorem allows us to update the hypothesis (the patient has the disease), taking into account information about the patient (they are $65$ or older), making use of existing available evidence (an estimate of the proportion of infected people that are $65$ or older).

Furthermore, suppose the likelihood is updated at a later date (e.g., due to more evidence being available as more people become infected). In that case, this will further improve the accuracy of the posterior when future patients are assessed.

### Example: Applying Bayes’ Theorem to a Situation in Context

#### Question

A survey of Bulgarian citizens showed that $17\%$ of all females smoke. Overall, $27.3\%$ of the population smoke, and $51\%$ of the population are female. If a smoker from this population is selected at random, what is the probability of them being female? Express your answer as a percentage to the nearest percent.

#### Explanation

Let $S$ be the event that a randomly selected person smokes, and let $F$ be the event that they are female. Then, we require $P(F|S),$ which we can compute using Bayes' theorem.

$$



P(F|S) = \dfrac{P(S|F) P(F) }{P(S)}



$$

From the problem statement, we have the following:

- $P(S|F) = 0.17,$ since $17\%$ of all females smoke.

- $P(F) = 0.51$, since $51\%$ of the population are female.

- $P(S) = 0.273,$ since $27.3\%$ of the population smoke.

Therefore, using Bayes' theorem, we have

$$



\begin{aligned}𝑃(𝐹|𝑆) & =\frac{𝑃(𝑆|𝐹)𝑃(𝐹)}{𝑃(𝑆)} \\ & =\frac{(0.17)(0.51)}{0.273} \\ & ≈32\%\end{aligned}



$$

rounded to the nearest percent.

### Formulating Bayes' Theorem From the Law of Total Probability

It's possible to express Bayes' theorem in an alternative form using the law of total probability.

First, let's restate Bayes' theorem:

$$



P(A|B)=\dfrac{P(B|A)P(A)}{P(B)}



$$

Now, the law of total probability tells us that

$$



P(B) = P(B|A)P(A) + P(B|A')P(A').



$$

Substituting this into Bayes' theorem, we get

$$



P(A|B)=\dfrac{P(B|A)P(A)}{P(B|A)P(A) + P(B|A')P(A')}.



$$

### Example: Applying Bayes' Theorem With the Law of Total Probability

#### Question

A bin contains $2$ blue chips and $4$ yellow chips. A second bin has $2$ blue chips and $2$ yellow chips. A bin is chosen at random, and a chip is selected from the chosen bin, also at random. Given that the selected chip is yellow, what is the probability that it came from the second bin?

#### Explanation

Let $Y$ be the event that the selected chip is yellow, and let $S$ be the event that the second bin is chosen. Then, we require $P(S|Y),$ which we can compute using Bayes' theorem.

$$



\begin{aligned}𝑃(𝑆|𝑌) & =\frac{𝑃(𝑌|𝑆)𝑃(𝑆)}{𝑃(𝑌)}=\frac{𝑃(𝑌|𝑆)𝑃(𝑆)}{𝑃(𝑌|𝑆)𝑃(𝑆)+𝑃(𝑌|𝑆^{′})𝑃(𝑆^{′})}\end{aligned}



$$

From the problem statement, we have the following:

- Since the first bin contains $4$ yellow chips and $2$ blue chips, we have

- Since the second bin contains $2$ yellow chips and $2$ blue chips, we have

- Since the bins are selected at random, we have

Therefore, using Bayes' theorem, we have

$$



\begin{aligned}𝑃(𝑆|𝑌) & =\frac{𝑃(𝑌|𝑆)𝑃(𝑆)}{𝑃(𝑌|𝑆)𝑃(𝑆)+𝑃(𝑌|𝑆^{′})𝑃(𝑆^{′})} \\ & =\frac{(\frac{1}{2})(\frac{1}{2})}{2} \\ & =\frac{(\frac{1}{4})}{4} \\ & =\frac{3}{7}.\end{aligned}



$$

### Example: Determining the Accuracy of Medical Tests

#### Question

A laboratory test for a particular disease is conducted on some patients. Of the patients tested, $94\%$ of those infected and $2\%$ of those not infected tested positive for the disease. Only $5\%$ of the entire population is infected with the disease. What is the probability that a randomly chosen patient who tested positive is not infected? Round your answer to the nearest percent.

#### Explanation

Let $D$ be the event that a randomly chosen patient is infected with the disease, and let $T$ be the event that they tested positive. Then, we require $P(D'|T),$ which we can compute using Bayes' theorem.

$$



P(D'|T) = \dfrac{P(T|D')P(D')}{P(T)}= \dfrac{P(T|D')P(D')}{P(T|D) P(D) + P(T | D') P(D')}



$$

From the problem statement, we have the following:

- Since the probability that an infected person tests positive is $94\%,$ and the probability that a non-infected person tests positive is $2\%,$ we have

- Since only $5\%$ of the population has the disease, we have

Therefore, using Bayes' theorem, we have

$$



\begin{aligned}𝑃(𝐷^{′}|𝑇) & =\frac{𝑃(𝑇|𝐷^{′})𝑃(𝐷^{′})}{𝑃(𝑇|𝐷)𝑃(𝐷)+𝑃(𝑇|𝐷^{′})𝑃(𝐷^{′})} \\ & =\frac{(0.02)(0.95)}{(0.94)(0.05)+(0.02)(0.95)} \\ & ≈0.288 \\ & ≈29\%\end{aligned}



$$

rounded to the nearest percent.

Note the following:

- When a non-infected patient tests positive for a disease, we call this a ****

- When an infected patient tests negative for a disease, we call this a ****
