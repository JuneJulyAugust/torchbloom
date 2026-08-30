# Working With Equivalent Forms of Exponential Functions

Source: https://www.mathacademy.com/topics/6268?courseId=120
Topic ID: 6268

## Prerequisites

- [The Product Rule for Exponents With Algebraic Expressions](../algebra-i/71-the-product-rule-for-exponents-with-algebraic-expressions.md)
- [Extrema of Exponential Functions](./6328-extrema-of-exponential-functions.md)

## Lesson

### Introduction

It's possible to write exponential functions in many different, equivalent forms. Depending on the situation, we may prefer one form over another if it displays characteristics we're interested in more clearly.

For example, consider the following exponential function:

$$


f(x)=35\cdot(1.4)^{x+1}


$$

It's possible to express this function in a variety of different forms using the laws of exponents. Let's go through some of the most common:

- We can write the function $f$ in an equivalent form with $x$ only in the exponent using the product rule in reverse.

- Similarly, we can write the function $f$ in an equivalent form with $(x-1)$ in the exponent as follows:

Therefore, our function $f$ has the following equivalent forms:

- $f(x) = 35\cdot(1.4)^{x+1}$

- $f(x) = 49 \cdot (1.4)^x$

- $f(x) = 68.6 \cdot (1.4)^{x-1}$

Please note that exponential functions have *many* equivalent forms. For the function $f$ here, this is only three of them.

### Identifying a Form Displaying the Y-Intercept

As we saw, the function $f$ defined earlier has the following equivalent forms:

- $f(x) = 35\cdot(1.4)^{x+1}$

- $f(x) = 49 \cdot (1.4)^x$

- $f(x) = 68.6 \cdot (1.4)^{x-1}$

The coefficients $35, 49,$ and $68.6$ all correspond to certain characteristics of the function. We can identify which characteristic a coefficient corresponds to by evaluating the function at certain points.

For example, the $y$-intercept is a characteristic of the curve $y=f(x),$ and its value corresponds to $f(0).$ We can determine the $y$-intercept by finding $f(0)$ using *any* of the forms given above.

Evaluating $f(0)$ using the first form, we get

$$


\begin{aligned}𝑓(0) & =35⋅(1.4)^{𝑥+1} \\ & =35⋅(1.4)^{0+1} \\ & =35⋅(1.4)^{1} \\ & =35⋅1.4 \\ & =49.\end{aligned}


$$

Notice that this number $49$ appears as a coefficient in the *second* form.

Therefore, we say that *the equivalent form $f(x) = 49 \cdot (1.4)^x$ displays the $y$-intercept as a coefficient*.

### Identifying a Form Displaying a Function Value

Let's go back to our three equivalent forms:

- $f(x) = 35\cdot(1.4)^{x+1}$

- $f(x) = 49 \cdot (1.4)^x$

- $f(x) = 68.6 \cdot (1.4)^{x-1}$

Which of these forms displays, as a coefficient, the value of $f(1)?$

First, let's determine $f(1).$ Evaluating $f(1)$ using the first form, we get

$$


\begin{aligned}𝑓(0) & =35⋅(1.4)^{1+1} \\ & =35⋅(1.4)^{2} \\ & =35⋅1.96 \\ & =68.6.\end{aligned}


$$

Notice that this number $68.6$ appears as a coefficient in the *third* form.

Therefore, we say that *the equivalent form $f(x) = 68.6 \cdot (1.4)^{x-1}$ displays $f(1)$ as a coefficient*.

### Example: Identifying Function Values In Equivalent Exponential Forms

#### Question

For the exponential function $f,$ the value of $f(1)$ is $k,$ where $k$ is a constant. Which of the following equivalent forms of the function $f$ shows the value of $k$ as the coefficient or the base?

1. $f(x)=15\cdot 2^{x+1}$

2. $f(x)=30\cdot 2^{x}$

3. $f(x)=120\cdot 2^{x-2}$

4. $f(x)=60\cdot 2^{x-1}$

#### Explanation

The value $f(1)$ is found by evaluating the function at $x=1.$ Using the convenient equivalent form $f(x)=30\cdot 2^x$ given in option II, we have

$$


\begin{aligned}𝑓(1) & =30⋅2^{1} \\ & =30⋅2 \\ & =60.\end{aligned}


$$

Thus, $k=60.$

Of the given options, only the form $f(x)=60\cdot 2^{x-1}$ displays this value of $k$ as a coefficient or base.

Therefore, the correct answer is "IV only".

### Restricting a Function's Domain to All Nonnegative Reals

Exponential functions are usually defined for all real $x.$ However, in certain contexts, we may decide to restrict the domain of an exponential function to (say) the non-negative real numbers.

Suppose we have the exponential function $y = f(x),$ where

$$


f(x) = a \cdot b^x + c


$$

on the restricted domain $x \geq 0,$ and $a > 0.$ Then, we have the following:

- If $b > 1,$ then the function has a minimum at $x=0,$ and no maximum.

- If $0 < b < 1,$ then the function has a maximum at $x=0,$ and no minimum.

Sometimes, exponential functions are written in such a way to display its extremum. Let's see an example.

### A Worked Example

Consider the following functions, each defined on $x \geq 0.$

- $f(x) = 2\cdot(0.5)^x$

- $g(x) = 4\cdot(2.5)^x$

- $h(x) = 4\cdot(2.5)^x+1$

On the domain $x\ge 0$ and $a> 0,$ an exponential $a\cdot b^x+ c$ is

- *decreasing* when $0 < b < 1,$ and has **no** minimum, and

- *increasing* when $b>1,$ with its minimum at $x=0.$

Now, consider each function in turn.

- For the function the base is $0.5\in(0,1).$ So, the function is decreasing on $x\ge 0$ and has *no minimum*. Hence, the equation of $f$ does *not* display a minimum value.

- For the function $g(x)=4\cdot(2.5)^x,$ the base is $2.5>1.$ So, the minimum occurs at $x=0,$ and is equal to Thus, the minimum value is $4,$ which is exactly the coefficient shown. Hence, the equation of $g$ *does* display the minimum as a coefficient.

- For the function the base is $2.5>1.$ So, the minimum occurs at $x=0,$ and is equal to The minimum value is $5,$ which is *not* equal to the coefficient ($4$) or the constant term ($1$). Hence, the equation of $h$ does *not* display the minimum as a constant term or a coefficient.

### Example: Identifying Characteristics in Exponential Functions : Domain Is All Nonnegative Reals

#### Question

Which of the following functions' equations displays, as a constant term or as a coefficient, the maximum value of the function, each defined on $x\ge 0?$

1. $f(x)=18\cdot(1.2)^x$

2. $g(x)=27\cdot(0.75)^x$

3. $h(x)=9\cdot(0.75)^x+4$

#### Explanation

On the domain $x\ge 0$ and $a > 0,$ an exponential $a\cdot b^x+ c$ is

- ** when $0 < b < 1,$ with its maximum at $x=0,$ and

- ** when $b>1,$ and has no maximum.

Now, consider each function in turn.

- For the function the base is $1.2>1.$ So, the function has no maximum. Hence, the equation of $f$ does ** display the maximum as a constant term or a coefficient.

- For the function the base is $0.75\in(0,1).$ So, the maximum occurs at $x=0,$ and is equal to Thus, the maximum value is $27,$ which is exactly the ** shown. Hence, the equation of $g$ ** display the maximum as a coefficient.

- For the function the base is $0.75\in(0,1).$ So, the maximum occurs at $x=0,$ and is equal to Thus, the maximum value is $13.$ However, neither the constant term ($4$) nor the coefficient ($9$) equals $13.$ Hence, the equation of $h$ does ** display the maximum as a constant term or a coefficient.

Therefore, the correct answer is "II only".

### Other Domains

In other contexts, we may use another starting value for the domain, other than $0.$ Instead of restricting exponential functions to $x \geq 0,$ we could use any domain, such as $x \geq 1.$

On the domain $x \geq 1$ with $a > 0,$ an exponential $a \cdot b^x + c$ always has either a minimum or a maximum:

- The function is *decreasing* when $0 < b < 1,$ so has no minimum, and a maximum at $x=1.$

- The function is *increasing* when $b > 1,$ so has a minimum at $x=1,$ and no maximum.

Let's see how to apply this in the next example.

### Example: Identifying Characteristics in Exponential Functions on Other Domains

#### Question

Which of the following functions' equations displays, as a constant term or as a coefficient, the **** value of the function, each defined on $x\ge 1?$

1. $f(x)=8\cdot(0.7)^x+2$

2. $g(x)=12\cdot(1.4)^x-3$

3. $h(x)=15\cdot(1.5)^x-7.5$

#### Explanation

On the domain $x\ge 1$ and $a > 0,$ an exponential $a\cdot b^x+ c$ is

- ** when $0 < b < 1,$ and has **** minimum, and

- ** when $b>1,$ with its **** at $x=1.$

Now, consider each function in turn.

- For the function the base is $0.7\in(0,1).$ So, the function is decreasing on $x\ge 1$ and has **** minimum. Hence, the equation of $f$ does ** display a minimum value.

- For the function the base is $1.4>1.$ So, the minimum occurs at $x=1,$ and is equal to The minimum value is $13.8,$ which is **** equal to the coefficient ($12$) or the constant term $(-3).$ Hence, the equation of $g$ does ** display the minimum.

- For the function the base is $1.5>1.$ So, the minimum occurs at $x=1,$ and is equal to Thus, the minimum value is $15,$ which is exactly the ** shown. Hence, the equation of $h$ ** display the minimum as a coefficient.

Therefore, the correct answer is "III only".
