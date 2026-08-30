# The Poisson Approximation of the Binomial Distribution

Source: https://www.mathacademy.com/topics/2840?courseId=73
Topic ID: 2840

## Prerequisites

- [Mean and Variance of the Binomial Distribution](./2149-mean-and-variance-of-the-binomial-distribution.md)
- [Mean and Variance of the Poisson Distribution](./2991-mean-and-variance-of-the-poisson-distribution.md)

## Lesson

### Introduction

When the number of observations $n$ of a binomial random variable is large, it can be difficult to calculate binomial probabilities due to the extremely large numbers involved. However, provided that some constraints are satisfied, we can closely approximate a binomial distribution as a Poisson distribution.

For example, suppose that at a lightbulb factory, $0.5\%$ of lightbulbs are defective. If a company manufactures $1\,000$ lightbulbs, what is the probability that $10$ of them will be defective?

Let $X$ be the number of defective lightbulbs. If there are $n=1\,000$ lightbulbs and the probability of any single lightbulb being defective is $p=0.5\% = 0.005,$ then we can calculate $P(X=10)$ using the probability mass function for the binomial distribution, as follows:

$$


\begin{aligned}𝑃(𝑋=10)=(\frac{1\,000}{10})(0.005)^{10}(0.995)^{990}\end{aligned}


$$

However, this product is difficult to compute because

- the binomial coefficient is huge:

- the power $(0.005)^{10}$ is extremely small:

Thankfully, it turns out that when $n$ is large, and $p$ is small, we can approximate a binomial distribution using a Poisson distribution with rate $\lambda = np.$ In our case, we have

$$


\lambda = np = (1\,000)(0.005) = 5.


$$

Using the Poisson approximation, the calculation becomes much more tractable. We get

$$


\begin{aligned}𝑃(𝑋=10) & ≈\frac{5^{10}𝑒^{−5}}{10!} \\ & ≈\frac{9\,765\,625𝑒^{−5}}{3\,628\,800} \\ & ≈0.018133\end{aligned}


$$

rounded to $6$ decimal places.

This is indeed very close to the binomial probability, which is

$$


\begin{aligned}𝑃(𝑋=10) & =(\frac{1\,000}{10})(0.005)^{10}(0.995)^{990} \\ & ≈0.017996\end{aligned}


$$

rounded to $6$ decimal places.

**Note:** There's not a single broadly accepted rule of thumb for using the Poisson approximation to the binomial distribution. Here, we will use the rule of thumb to use the Poisson approximation when $n>20$ and $p<0.05.$

### Example: Identifying Situations Where the Poisson Approximation is Appropriate

#### Question

Which of the following probabilities could be approximated using the Poisson approximation of the binomial distribution?

1. The probability that a student gets $3$ correct answers in a true/false test with $10$ questions if the student answers all questions at random.

2. The probability that $5$ people out of a random sample of $50$ people have a certain disease, present in $2\%$ of the population.

3. The probability of getting a defective electronic component in a random sample of $40$ components if $6\%$ of the components are defective.

#### Explanation

A rule of thumb is that we can approximate a binomial random variable using the Poisson distribution when $n>20$ and $p< 0.05.$

With that in mind, let's consider each of the given probability scenarios.

- Probability I ** be approximated using the Poisson distribution. $n$ is ** large enough: $n=10 \ngtr 20 \quad \color{red}\times$

- Probability II can be approximated using the Poisson distribution. $n$ is large enough: $n=50 > 20 \quad \color{green}\checkmark$ $p$ is small enough: $p = 2\% = 0.02 < 0.05 \quad \color{green}\checkmark$

- Probability III ** be approximated using the Poisson distribution. $n$ is large enough: $n=40 > 20 \quad \color{green}\checkmark$ $p$ is ** small enough: $p = 6\% = 0.06 \nless 0.05 \quad \color{red}\times$

Therefore, the correct answer is "II only."

### Example: Using the Poisson Approximation to Compute a Probability

#### Question

The probability that an expert typist mistypes a single letter is $0.003.$ Using the Poisson approximation to the binomial distribution, estimate the probability that the typist will mistype at most $4$ letters on a page containing $2\,000$ letters.

#### Explanation

Let the random variable $X$ be equal to the number of mistyped letters on the page. Then, $X$ follows a binomial distribution, where $X\sim B(2\,000, 0.003).$

As a general rule of thumb, we can approximate a binomial random variable using the Poisson distribution when $n > 20$ and $p < 0.05.$

There are $n=2\,000>20$ letters and the probability that an individual letter is mistyped is $p = 0.003 < 0.05,$ so we can use a Poisson approximation.

The Poisson approximation will use the rate

$$


\lambda = np = (2\,000)(0.003) = 6.


$$

Substituting $\lambda = 6$ into the Poisson probability mass function, we get

$$


\begin{aligned}𝑓(𝑥) & =\frac{𝜆^{𝑥}𝑒^{−𝜆}}{𝑥!} \\ & =\frac{6^{𝑥}𝑒^{−6}}{𝑥!}.\end{aligned}


$$

The probability of having $4$ or fewer mistyped letters is

$$


\begin{aligned}𝑃(𝑋≤4) & =𝑃(0)+𝑃(1)+𝑃(2)+𝑃(3)+𝑃(4) \\ & ≈𝑓(0)+𝑓(1)+𝑓(2)+𝑓(3)+𝑓(4) \\ & ≈\frac{6^{0}𝑒^{−6}}{0!}+\frac{6^{1}𝑒^{−6}}{1!}+\frac{6^{2}𝑒^{−6}}{2!}+\frac{6^{3}𝑒^{−6}}{3!}+\frac{6^{4}𝑒^{−6}}{4!} \\ & ≈0.285,\end{aligned}


$$

rounded to three decimal places.
