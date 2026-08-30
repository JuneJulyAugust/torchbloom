# Dividing Complex Numbers

Source: https://www.mathacademy.com/topics/227?courseId=136
Topic ID: 227

## Prerequisites

- [Special Properties of the Complex Conjugate](./905-special-properties-of-the-complex-conjugate.md)

## Lesson

### Introduction

To divide one complex number by another, we set up a fraction and then multiply both the numerator and the denominator by the complex conjugate of the denominator.

For example, to divide $2 - \textrm{i}$ by $1 + 3\textrm{i},$ we start by setting up a fraction:

$$


\dfrac {2 - \textrm{i}} {1 + 3\textrm{i}}


$$

The denominator is $1 + 3\textrm{i}$ and its conjugate is $1 - 3\textrm{i}.$

We multiply both the numerator and denominator by $1 - 3\textrm{i},$ so that the denominator turns into a real number:

$$


\begin{aligned} \dfrac {2 - \textrm{i}} {1 + 3\textrm{i}} \cdot \dfrac {1 - 3\textrm{i}} {1 - 3\textrm{i}} &= \dfrac {2 - 6\textrm{i} -\textrm{i} + 3\textrm{i}^2} {1 - 3\textrm{i} + 3\textrm{i} - 9\textrm{i}^2} \\\[5pt] &= \dfrac {2 - 7\textrm{i} + 3(-1)} {1 - 9(-1)} \\\[5pt] &= \dfrac {2 - 7\textrm{i} - 3} {1 + 9} \\\[5pt] &= \dfrac {-1 - 7\textrm{i}} {10} \end{aligned}


$$

Now that the denominator is a real number, we can write the complex number in the form $a+b \textrm{i}\mathbin{:}$

$$


\begin{aligned} \dfrac {-1 - 7\textrm{i}} {10} = -\dfrac{1} {10} - \dfrac {7} {10} \textrm{i} \end{aligned}


$$

### Example: Dividing Two Complex Numbers

#### Question

Express $\dfrac {4 + \textrm{i}} {1 - \textrm{i}}$ in the form $a+\textrm{i}b.$

#### Explanation

The denominator is $1-\textrm{i}$ and its conjugate is $1+\textrm{i}.$ We multiply both the numerator and the denominator by $1+\textrm{i},$ so that the denominator turns into a real number:

$$


\begin{aligned} \dfrac {4 + \textrm{i}} {1 - \textrm{i}} &=\dfrac {4 + \textrm{i}} {1 - \textrm{i}} \cdot \dfrac {1 + \textrm{i}} {1 + \textrm{i}} \\\[5pt] &= \dfrac {4 + 4\textrm{i} + \textrm{i} + \textrm{i}^2} {1^2 - \textrm{i}^2} \\\[5pt] &= \dfrac {4 + 5\textrm{i} + (-1)} {1 - (-1)} \\\[5pt] &= \dfrac {3 + 5\textrm{i}} {2} \end{aligned}


$$

Now that the denominator is a real number, we can write the complex number in the form $a+\textrm{i} b \mathbin{:}$

$$


\begin{aligned} \dfrac {3 + 5\textrm{i}} {2} = \dfrac{3} {2} + \dfrac {5} {2} \textrm{i} \end{aligned}


$$

### Example: Dividing an Imaginary Number by a Complex Number

#### Question

If $z_1=3\textrm{i}$ and $z_2 = 2+5\textrm{i},$ then what is $z_1$ divided by $z_2?$

#### Explanation

First, we set up the fraction:

$$


\dfrac{3\textrm{i}}{2+5\textrm i}


$$

The denominator is $2+5\textrm{i}$ and its conjugate is $2-5\textrm{i}.$ We multiply both the numerator and the denominator by $2-5\textrm{i},$ so that the denominator turns into a real number:

$$


\begin{aligned} \dfrac {3 \textrm{i}} {2 +5\textrm{i}} &= \dfrac {3 \textrm{i}} {2 +5 \textrm{i}} \cdot \dfrac {2 -5 \textrm{i}} {2-5\textrm{i}} \\\[5pt] &=\dfrac {6 \textrm{i} - 15 \textrm{i}^2 } {2^2 - (5\textrm{i})^2} \\\[5pt] &=\dfrac {6 \textrm{i} - 15\textrm{i}^2 } {4 - 25\textrm{i}^2} \\\[5pt] &= \dfrac {6 \textrm{i} - 15(-1) } {4 - 25(-1)} \\\[5pt] &=\dfrac {6 \textrm{i} + 15 } {29} \end{aligned}


$$

Now that the denominator is a real number, we can write the complex number in the form $a+b \textrm{i}\mathbin{:}$

$$


\begin{aligned} \dfrac {6 \textrm{i} + 15 } {29}= \dfrac{15} {29} + \dfrac {6} {29} \textrm{i} \end{aligned}


$$

### Example: Dividing a Real Number by a Complex Number

#### Question

Express $\dfrac{4}{-1+2\textrm{i}}$ in the form $a+\textrm{i}b.$

#### Explanation

The denominator is $-1+2\textrm{i}$ and its conjugate is $-1-2\textrm{i}.$ We multiply both the numerator and the denominator by $-1-2\textrm{i},$ so that the denominator turns into a real number:

$$


\begin{aligned} \dfrac {4} {-1 +2\textrm{i}} &=\dfrac {4} {-1 +2 \textrm{i}} \cdot \dfrac {-1 -2 \textrm{i}} {-1-2\textrm{i}} \\\[5pt] &= \dfrac {-4 - 8 \textrm{i} } {(-1)^2 - (2\textrm{i})^2} \\\[5pt] &= \dfrac {-4 - 8 \textrm{i} } {1 - 4\textrm{i}^2} \\\[5pt] &= \dfrac {-4 - 8 \textrm{i} } {1 - 4(-1)} \\\[5pt] &= \dfrac {-4 - 8 \textrm{i} } {5} \end{aligned}


$$

Now that the denominator is a real number, we can write the complex number in the form $a+b \textrm{i}\mathbin{:}$

$$


\begin{aligned} \dfrac {-4 - 8 \textrm{i} } {5} = -\dfrac{4} {5} - \dfrac {8} {5} \textrm{i} \end{aligned}


$$

### Example: Dividing a Complex Number by an Imaginary Number

#### Question

If $z_1 = -8-3\textrm{i}$ and $z_2 = 2\textrm{i},$ then what is $z_1$ divided by $z_2?$

#### Explanation

First, we set up the fraction:

$$


\dfrac {-8 - 3\textrm{i}} {2\textrm{i}}


$$

The denominator is the imaginary number $2\textrm{i}.$ Note that this can be written as $0+2\textrm{i},$ so the conjugate is $0-2\textrm{i},$ or simply $-2\textrm{i}.$

So, we multiply both the numerator and the denominator by $-2\textrm{i},$ so that the denominator turns into a real number:

$$


\begin{aligned} \dfrac {-8 - 3\textrm{i}} {2\textrm{i}} &= \dfrac {-8 - 3\textrm{i}} {2\textrm{i}} \cdot \dfrac {-2\textrm{i}} {-2\textrm{i}} \\\[5pt] &= \dfrac {16\textrm{i} + 6\textrm{i}^2} {-4\textrm{i}^2} \\\[5pt] &= \dfrac {16\textrm{i} + 6(-1)} {-4(-1)} \\\[5pt] &= \dfrac {-6 + 16\textrm{i}} {4} \end{aligned}


$$

Now that the denominator is a real number, we can write the complex number in the form $a+b \textrm{i}\mathbin{:}$

$$


\begin{aligned} \dfrac {-6 + 16\textrm{i}} {4} &= - \dfrac{6}{4} + \dfrac{16}{4} \textrm{i} \\\[5pt] &= -\dfrac{3} {2} + 4\textrm{i} \end{aligned}


$$
