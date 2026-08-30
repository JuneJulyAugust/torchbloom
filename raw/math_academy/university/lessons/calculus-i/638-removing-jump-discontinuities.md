# Removing Jump Discontinuities

Source: https://www.mathacademy.com/topics/638?courseId=105
Topic ID: 638

## Prerequisites

- [Removing Point Discontinuities](./341-removing-point-discontinuities.md)
- [Jump Discontinuities](./2003-jump-discontinuities.md)

## Lesson

### Introduction

Consider the function $f(x)$ below:

$$


\begin{aligned}3𝑥^{2}+𝑘𝑥, & 𝑥<−3, \\ 𝑥^{3}, & 𝑥≥−3\end{aligned}


$$

The function $f(x)$ seems to have a jump discontinuity at $x=-3.$ However, by selecting a particular value for $k$, we can remove the jump discontinuity and make the function continuous.

We can find this value of $k$ by forcing the left and right-sided limits of the function to be equal at $x=-3\mathbin{:}$

$$


\lim\limits_{x\to (-3)^-} f(x) = \lim\limits_{x\to (-3)^+} f(x)


$$

For the left limit, we have,

$$


\begin{aligned}\underset{𝑥→(−3)^{−}}{lim}𝑓(𝑥) & =\underset{𝑥→(−3)^{−}}{lim}(3𝑥^{2}+𝑘𝑥) \\ & =3(−3)^{2}+𝑘(−3) \\ & =27−3𝑘,\end{aligned}


$$

and for the right limit, we have

$$


\begin{aligned}\underset{𝑥→(−3)^{+}}{lim}𝑓(𝑥) & =\underset{𝑥→(−3)^{+}}{lim}𝑥^{3} \\ & =(−3)^{3} \\ & =−27.\end{aligned}


$$

Setting the left and right limits as equal, we have

$$


\begin{aligned}27−3𝑘 & =−27 \\ 3𝑘 & =54 \\ 𝑘 & =18.\end{aligned}


$$

Therefore, to make $f(x)$ continuous at $x=-3,$ we need to choose $k=18.$

### Example: Removing a Jump Discontinuity in a Piecewise Polynomial Function

#### Question

Find the value(s) of the constant $a$ that make the function $f(x)$ below continuous at $x=2.$

$$


\begin{aligned}(2𝑥+𝑎)^{2}, & 𝑥≤2 \\ 𝑥^{2}−3, & 𝑥>2\end{aligned}


$$

#### Explanation

At $x=2,$ the left-sided limit is

$$


\begin{aligned}\underset{𝑥→2^{−}}{lim}𝑓(𝑥) & =\underset{𝑥→2^{−}}{lim}(2𝑥+𝑎)^{2} \\ & =(2(2)+𝑎)^{2} \\ & =(4+𝑎)^{2},\end{aligned}


$$

and the right-sided limit is

$$


\begin{aligned}\underset{𝑥→2^{+}}{lim}𝑓(𝑥) & =\underset{𝑥→2^{+}}{lim}(𝑥^{2}−3) \\ & =(2)^{2}−3 \\ & =4−3 \\ & =1.\end{aligned}


$$

In order for $f(x)$ to be continuous at $x=2,$ we require that

$$


\begin{aligned}\underset{𝑥→2^{−}}{lim}𝑓(𝑥) & =\underset{𝑥→2^{+}}{lim}𝑓(𝑥) \\ (4+𝑎)^{2} & =1 \\ \sqrt{√(𝑎+4)^{2}} & =\sqrt{√1} \\ |𝑎+4| & =1 \\ 𝑎+4 & =±1 \\ 𝑎 & =−4±1 \\ 𝑎 & =−5,−3.\end{aligned}


$$

Therefore, $f(x)$ is continuous at $x=2$ for $a=-5$ or $a=-3.$

### Example: Removing a Jump Discontinuity in a Piecewise Radical Function

#### Question

Given that the function

$$


\begin{aligned}\sqrt{√2𝑏−3𝑥}, & 𝑥≤0 \\ −𝑥+2, & 𝑥>0\end{aligned}


$$

is continuous at $x=0,$ find the value of the constant $b.$

#### Explanation

At $x=0,$ the left-sided limit is

$$


\begin{aligned}\underset{𝑥→0^{−}}{lim}𝑓(𝑥) & =\underset{𝑥→0^{−}}{lim}\sqrt{√2𝑏−3𝑥} \\ & =\sqrt{√2𝑏−3(0)} \\ & =\sqrt{√2𝑏},\end{aligned}


$$

and the right-sided limit is

$$


\begin{aligned}\underset{𝑥→0^{+}}{lim}𝑓(𝑥) & =\underset{𝑥→0^{+}}{lim}(−𝑥+2) \\ & =−(0)+2 \\ & =2.\end{aligned}


$$

In order for $f(x)$ to be continuous at $x=0,$ we require that

$$


\begin{aligned}\underset{𝑥→0^{−}}{lim}𝑓(𝑥) & =\underset{𝑥→0^{+}}{lim}𝑓(𝑥) \\ 2 & =\sqrt{√2𝑏} \\ 4 & =2𝑏 \\ 𝑏 & =2.\end{aligned}


$$

### Example: Removing a Jump Discontinuity in a Piecewise Exponential Function

#### Question

Find the value of the constant $c$ that makes the function $h(x)$ below continuous at $x=4.$

$$


\begin{aligned}4^{𝑐𝑥+1}, & 𝑥≤4 \\ 4𝑥, & 𝑥>4\end{aligned}


$$

#### Explanation

At $x=4,$ the left-sided limit is

$$


\begin{aligned}\underset{𝑥→4^{−}}{lim}ℎ(𝑥) & =ℎ(4) \\ & =4^{𝑐(4)+1} \\ & =4^{4𝑐+1},\end{aligned}


$$

and the right-sided limit is

$$


\begin{aligned}\underset{𝑥→4^{+}}{lim}ℎ(𝑥) & =\underset{𝑥→4^{+}}{lim}(4𝑥) \\ & =4(4) \\ & =16.\end{aligned}


$$

In order for $h(x)$ to be continuous at $x=4,$ we require that

$$


\begin{aligned}4^{4𝑐+1} & =16 \\ 4^{4𝑐+1} & =4^{2} \\ 4𝑐+1 & =2 \\ 4𝑐 & =1 \\ 𝑐 & =\frac{1}{4}.\end{aligned}


$$

Therefore, $h(x)$ is continuous at $x=4$ for $c = \dfrac{1}{4}.$

### Example: Removing a Jump Discontinuity in a Piecewise Logarithmic Function

#### Question

Given that the function

$$


\begin{aligned}log_{2}⁡(𝑎𝑥+1), & 0≤𝑥≤1 \\ log_{3}⁡(2𝑥+1), & 𝑥>1\end{aligned}


$$

is continuous at $x=1$, find the value of $a.$

#### Explanation

At $x=1,$ the left-sided limit is

$$


\begin{aligned}\underset{𝑥→1^{−}}{lim}𝑔(𝑥) & =\underset{𝑥→1^{−}}{lim}log_{2}⁡(𝑎𝑥+1) \\ & =log_{2}⁡(𝑎(1)+1) \\ & =log_{2}⁡(𝑎+1),\end{aligned}


$$

and the right-sided limit is

$$


\begin{aligned}\underset{𝑥→1^{+}}{lim}𝑔(𝑥) & =\underset{𝑥→1^{+}}{lim}(log_{3}⁡(2𝑥+1)) \\ & =log_{3}⁡(2(1)+1) \\ & =log_{3}⁡(3) \\ & =1.\end{aligned}


$$

In order for $g(x)$ to be continuous at $x=1,$ we require that

$$


\begin{aligned}\underset{𝑥→1^{−}}{lim}𝑔(𝑥) & =\underset{𝑥→1^{+}}{lim}𝑔(𝑥) \\ log_{2}⁡(𝑎+1) & =1 \\ 𝑎+1 & =2^{1} \\ 𝑎 & =1.\end{aligned}


$$
