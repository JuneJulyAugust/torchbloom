# Approximating Values Using the Binomial Theorem

Source: https://www.mathacademy.com/topics/1158?courseId=136
Topic ID: 1158

## Prerequisites

- [The Special Case of the Binomial Theorem](./3764-the-special-case-of-the-binomial-theorem.md)
- [Calculating Percentage Change](../grade-7/6666-calculating-percentage-change.md)

## Lesson

### Introduction

The binomial theorem can be used to find or approximate the value of a number raised to a positive integer power.

For example, suppose we want to approximate the numerical value of $(1.01)^{15}.$ A good place to start is the special case of the binomial formula:

$$


(1+x)^n = 1 + nx + \dfrac{1}{2!} n(n-1)x^2 + \cdots + x^n


$$

Notice that substituting $x={\color{blue}{0.01}}$ and $n={\color{red}{15}}$ gives

$$


(1 + {\color{blue}{0.01}})^{\color{red}{15}} = 1 + {\color{red}{15}}({\color{blue}{0.01}}) + \dfrac{1}{2!} {\color{red}{15}}({\color{red}{15}}-1)({\color{blue}{0.01}})^2 + \cdots + ({\color{blue}{0.01}})^{\color{red}{15}}


$$

which simplifies as

$$


(1.01)^{15} = 1 + 15(0.01) + \dfrac{1}{2!} 15(14)(0.01)^2 + \cdots + (0.01)^{15}. \qquad\left(\ast\right)


$$

So, we can find the exact value of $(1.01)^{15}$ by evaluating the right-hand side of $\left(\ast\right).$ However, the full binomial expansion on the right-hand side contains $16$ terms! In cases like this, a good alternative is to find an approximation.

Increasing powers of $x$ become progressively smaller when $x$ is small. In our case, this means

$$


(0.01) \quad\gg\quad (0.01)^2 \quad\gg\quad (0.01)^3 \quad\gg\quad\cdots \quad\gg \quad(0.01)^{15}


$$

where the symbol $\gg$ means "much greater than." Therefore, we can find a good approximation of $(1.01)^{15}$ by considering the first few terms of $(\ast)$ only.

If we drop everything but the first three terms of $\left(\ast\right),$ we arrive at the approximation

$$


(1.01)^{15} \approx 1 + 15(0.01) + \dfrac{1}{2!} 15(14)(0.01)^2 .


$$

Evaluating the right-hand side of the above, we get

$$


(1.01)^{15} \approx 1+0.15+0.0105 = 1.1605.


$$

Note that the exact value is

$$


(1.01)^{15} = 1.160\,968\ldots


$$

so our approximation is pretty good. However, if we want to improve our approximation, we must keep more terms from the original expansion.

### Example: Approximating Powers of Numbers Close to Unity

#### Question

Use the first four terms of the binomial expansion of $(1+x)^6$ in ascending powers of $x$ to approximate $(1.15)^6.$ Give your answer to three decimal places.

#### Explanation

Recall that when $n$ is a positive integer,

$$


(1+x)^n = 1 + nx + \dfrac{1}{2!} n(n-1)x^2 + \dfrac{1}{3!} n(n-1)(n-2)x^3 + \cdots + x^n.


$$

Therefore,

$$


\begin{aligned}(1+𝑥)^{6} & =1+6𝑥+\frac{1}{2}⋅6⋅5⋅𝑥^{2}+\frac{1}{6}⋅6⋅5⋅4⋅𝑥^{3}+⋯+𝑥^{𝑛} \\ & =1+6𝑥+15𝑥^{2}+20𝑥^{3}+⋯\,+𝑥^{𝑛}.\end{aligned}


$$

So, for small $x,$ we have

$$


\left( {1 + x} \right)^6 \approx 1 + 6x + 15x^2 + 20x^3.


$$

Finally, we substitute $x=0.15$ into the above approximation of $(1 + x)^6{:}$

$$


\begin{aligned}(1.15)^{6} & =(1+0.15)^{6} \\ & ≈1+6(0.15)^{1}+15(0.15)^{2}+20(0.15)^{3} \\ & =1+6(0.15)+15(0.022\,5)+20(0.003\,375) \\ & =1+0.9+0.337\,5+0.067\,5 \\ & =2.305,\end{aligned}


$$

to three decimal places.

### Example: Approximating Powers of Numbers Close to Unity: Case With Alternating Signs

#### Question

Use the first four terms of the binomial expansion of $(1+x)^8$ in ascending powers of $x$ to approximate $(0.89)^8.$ Give your answer to six decimal places.

#### Explanation

Recall that when $n$ is a positive integer,

$$


(1+x)^n = 1 + nx + \dfrac{1}{2!} n(n-1)x^2 + \dfrac{1}{3!} n(n-1)(n-2)x^3 + \cdots + x^n.


$$

Therefore,

$$


\begin{aligned}(1+𝑥)^{8} & =1+8𝑥+\frac{1}{2}⋅8⋅7⋅𝑥^{2}+\frac{1}{6}⋅8⋅7⋅6⋅𝑥^{3}+⋯+𝑥^{𝑛} \\ & =1+8𝑥+28𝑥^{2}+56𝑥^{3}+⋯\,+𝑥^{𝑛}.\end{aligned}


$$

So, for small $x,$ we have

$$


\left( {1 + x} \right)^8 \approx 1 + 8x + 28x^2 + 56x^3.


$$

Finally, we substitute $x=-0.11$ into the above approximation of $(1 + x)^8{:}$

$$


\begin{aligned}(0.89)^{8} & =(1+(−0.11))^{8} \\ & ≈1+8(−0.11)^{1}+28(−0.11)^{2}+56(−0.11)^{3} \\ & =1−8(0.11)+28(0.012\,1)−56(0.001\,331) \\ & =1−0.88+0.338\,8−0.074\,536 \\ & =0.384\,264,\end{aligned}


$$

to six decimal places.

### Approximating Powers of Numbers Using the Binomial Theorem

Up to now, we've seen how to approximate numbers of the form $(1+x)^n,$ where $x$ is small.

To approximate numbers of the form $(a+b)^n$ where $a$ is any number, and $b$ is small, we need to apply the more general binomial theorem:

$$


{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \cdots + {n \choose n}{a^0}{b^n}


$$

Let's see an example.

### Example: Approximating Powers of Numbers Using the Binomial Theorem

#### Question

Use the first $3$ terms of the binomial expansion of ${\left(2+x \right)^{4}}$ in ascending powers of $x$ to approximate $(1.97)^{4}.$

#### Explanation

The binomial theorem for positive integer $n$ states that

$$


{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \cdots + {n \choose n}{a^0}{b^n}.


$$

By substituting $a=2,$ $b=x,$ and $n=4,$ we obtain

$$


\begin{aligned}(2+𝑥)^{4}= & (\frac{4}{0})(2)^{4}(𝑥)^{0}+(\frac{4}{1})(2)^{4−1}(𝑥)^{1}+(\frac{4}{2})(2)^{4−2}(𝑥)^{2}+⋯ \\ & =1⋅(2)^{4}(𝑥)^{0}+4(2)^{3}(𝑥)^{1}+6(2)^{2}(𝑥)^{2}+⋯ \\ & =16+4(8)(𝑥)+6(4)(𝑥^{2})+⋯ \\ & =16+32𝑥+24𝑥^{2}+⋯.\end{aligned}


$$

So, for small $x,$ we have

$$


\left( {2 + x} \right)^{4} \approx 16 + 32x + 24{x^2}.


$$

Finally, we substitute $x=-0.03$ into the expansion of $(2+x)^4{:}$

$$


\begin{aligned}(1.97)^{4} & =(2−0.03)^{4} \\ & ≈16+32(−0.03)+24(−0.03)^{2} \\ & =16−0.96+0.021\,6 \\ & =15.0616\end{aligned}


$$

### Example: Calculating the Percentage Error of an Approximation

#### Question

Calculate the percentage error obtained when approximating the value of $(1.08)^{5}$ using the first three terms of the binomial expansion of $(1+x)^5$ in ascending powers of $x.$ Round your final percentage error to two decimal places.

#### Explanation

The binomial theorem for positive integer $n$ states that

$$


{(a + b)^n} = {n \choose 0}{a^n}{b^0} + {n \choose 1}{a^{n - 1}}{b^1} + {n \choose 2}{a^{n - 2}}{b^2} + \ldots + {n \choose n}{a^0}{b^n}.


$$

By substituting $a = 1,$ $b = x,$ and $n = 5,$ we obtain

$$


\begin{aligned}(1+𝑥)^{5} & =(\frac{5}{0})(1)^{5}(𝑥)^{0}+(\frac{5}{1})(1)^{5−1}(𝑥)^{1}+(\frac{5}{2})(1)^{5−2}(𝑥)^{2}+⋯ \\ & =1(1)^{5}+5(1)^{4}(𝑥)^{1}+10(1)^{3}(𝑥)^{2}+⋯ \\ & =1+5(1)(𝑥)+10(1)(𝑥^{2})+⋯ \\ & =1+5𝑥+10𝑥^{2}+⋯\,.\end{aligned}


$$

So, for small $x,$ we have

$$


{\left( {1 + x} \right)^{5}} \approx 1 + 5x + 10x^2.


$$

Now, we substitute $x = 0.08$ into the above approximation of $(1 + x)^5{:}$

$$


\begin{aligned}(1.08)^{5} & =(1+0.08)^{5} \\ & ≈1+5(0.08)+10(0.08)^{2} \\ & =1+5(0.08)+10(0.006\,4) \\ & =1+0.4+0.064 \\ & =1.464\end{aligned}


$$

Finally, using a calculator, we can compute the percentage error, as follows:

$$


\begin{aligned}\%\,error & =\frac{amount of error}{exact value}×100 \\ & =\frac{|(1.08)^{5}−1.464|}{(1.08)^{5}}×100 \\ & ≈0.36\%\end{aligned}


$$

rounded to two decimal places.
