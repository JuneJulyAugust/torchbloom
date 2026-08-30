# Repeating Decimals as Infinite Geometric Series

Source: https://www.mathacademy.com/topics/689?courseId=106
Topic ID: 689

## Prerequisites

- [Writing an Infinite Geometric Series in Sigma Notation](./686-writing-an-infinite-geometric-series-in-sigma-notation.md)

## Lesson

### Introduction

A repeating decimal can be expressed as a geometric series whose common ratio is a power of $\dfrac 1 {10}.$

For example, the number $0.\overline{8}$ can be expressed as

$$


\begin{aligned}0.\overset{8}{–} & =0.8+0.08+0.008+… \\ & =\frac{8}{10}+\frac{8}{100}+\frac{8}{1\,000}+…\end{aligned}


$$

We have $a_1 = \dfrac{8}{10}$ and $r = \dfrac {0.08}{0.8} = \dfrac 1 {10}.$ Therefore,

$$


\begin{aligned}0.\overset{8}{–} & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{1}𝑟^{𝑛−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{8}{10}(\frac{1}{10})^{𝑛−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}8⋅\frac{1}{10}⋅(\frac{1}{10})^{𝑛}⋅(\frac{1}{10})^{−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}8⋅\frac{1}{10}⋅(\frac{1}{10})^{𝑛}⋅(\frac{1}{10})^{−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}8⋅\frac{1}{10}⋅(\frac{1}{10})^{𝑛}⋅10 \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}8(\frac{1}{10})^{𝑛}.\end{aligned}


$$

### Example: Expressing a Repeating Decimal as an Infinite Geometric Series

#### Question

Write $0.\overline{23}$ as geometric series.

#### Explanation

The given repeating decimal can be written as

$$


0.\overline{23} = 0.23 + 0.002\,3 + 0.000\,023 + \dots


$$

$$


0.\overline{23} = \dfrac{23}{100} + \dfrac{23}{10\,000} + \dfrac{23}{1\,000\,000}+\dots


$$

where the first term is $a_1 = \dfrac{23}{100}$ and the common ratio is $\dfrac{1}{100}.$ Therefore,

$$


\begin{aligned}0.\overset{23}{} & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{1}𝑟^{𝑛−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{23}{100}⋅(\frac{1}{100})^{𝑛−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}23⋅\frac{1}{100}⋅(\frac{1}{100})^{𝑛−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}23⋅\frac{1}{100}⋅(\frac{1}{100})^{𝑛}⋅(\frac{1}{100})^{−1} \\ & =\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}23(\frac{1}{100})^{𝑛}.\end{aligned}


$$

### Example: Expressing a Repeating Decimal as the Sum of a Number and a Geometric Series

#### Question

Write $0.1\overline{4}$ as geometric series.

#### Explanation

The given repeating decimal can be written as

$$


\begin{aligned}0.1\overset{4}{–} & =0.144\,4... \\ & =0.1+0.04+0.004+0.000\,4+… \\ & =\frac{1}{10}+(\frac{4}{100}+\frac{4}{1000}+\frac{4}{10\,000}+…).\end{aligned}


$$

The series in the parentheses is a geometric series with the first term $a_1 = \dfrac{4}{100}$ and the common ratio $r=\dfrac{1}{10}.$ Therefore,

$$


\begin{aligned}0.1\overset{4}{–} & =\frac{1}{10}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}𝑎_{1}𝑟^{𝑛−1} \\ & =\frac{1}{10}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{4}{100}(\frac{1}{10})^{𝑛−1} \\ & =\frac{1}{10}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{4⋅10}{100}(\frac{1}{10})^{𝑛} \\ & =\frac{1}{10}+\underset{\underset{𝑛=1}{∑}}{\overset{}{∞}}\frac{4}{10}(\frac{1}{10})^{𝑛}.\end{aligned}


$$
