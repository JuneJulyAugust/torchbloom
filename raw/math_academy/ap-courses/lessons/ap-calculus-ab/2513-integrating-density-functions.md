# Integrating Density Functions

Source: https://www.mathacademy.com/topics/2513?courseId=24
Topic ID: 2513

## Prerequisites

- [The Second Fundamental Theorem of Calculus](./613-the-second-fundamental-theorem-of-calculus.md)
- [Definite Integrals of Piecewise Functions](./626-definite-integrals-of-piecewise-functions.md)
- [Integrating Exponential Functions Using Substitution](./3770-integrating-exponential-functions-using-substitution.md)

## Lesson

### Introduction

Suppose that a test-tube contains a solution of glucose and the concentration $c(x)$ of glucose in the tube depends upon its depth $x$ within the solution, as follows:

$$


c(x) = 0.2 + 0.05x


$$

Here, the units of $c(x)$ are grams per cubic centimeter.

Note that:

- The function $c(x)$ is called a **density function** for the glucose. It tells us the concentration of glucose at a particular depth $x.$

- In this particular case, the given concentration is linear with a positive slope ($0.05$).

- Therefore, $c(x)$ increases as $x$ increases.

- Intuitively, this means that as we move down through the tube, the concentration of glucose increases.

How can we find the total mass of glucose in the solution if the depth of the solution in the tube is $10$ centimeters, and it has a constant horizontal cross-section of $1$ square centimeter?

Since the cross-section of the tube is constant and equals $1\,\text{cm}^2,$ the total mass $M$ of the glucose will depend only on the depth $x$ and can be found as

$$


M = \int_{0}^{10} c(x) \, \text{d}x.


$$

We carry out the integration as follows:

$$


\begin{aligned}𝑀 & =∫_{100}^{}(0.2+0.05𝑥)\,d𝑥 \\ & =0.2𝑥\,_{100}^{}+0.05⋅\frac{𝑥^{2}}{2}\,_{100}^{} \\ & =0.2(10−0)+0.05(50−0) \\ & =2+2.5 \\ & =4.5\end{aligned}


$$

So, the total mass of glucose in the solution is $4.5$ grams.

### Example: Integrating a Density Function

#### Question

The function $F(h)=40 e^{-0.5h}$ gives the number of dust particles in the air, in millions per cubic foot, at a height of $h$ feet above the sea level in a particular region of the world. Consider a vertical column of air with a height of $100 \, \text{ft}$ and a constant horizontal cross-section of $5$ square feet. How many dust particles does the column contain?

#### Explanation

Here, $F(h)$ is a density function for the number of dust particles in the air, and its units are millions of particles per $1 \, \text{ft}^3.$

The mass of a single vertical column measuring

$$


\underbrace{1\,\textrm{ft}^2}_{\textrm{cross section}} \times \:\: \underbrace{100\, \textrm{ft}}_{\textrm{height}}


$$

is given by the integral

$$


\int_{0}^{100} F(h) \, \text{d}h.


$$

However, since we want the mass of $5$ vertical columns (since that will give a cross-section of $5\,\textrm{ft}^2),$ we need to multiply the above integral by $5.$ So the required mass is given by

$$


5 \int_{0}^{100} F(h) \, \text{d}h.


$$

Carrying out the integration, we obtain

$$


\begin{aligned}𝑀 & =5∫_{1000}^{}40𝑒^{−0.5𝑑}\,dℎ \\ & =200∫_{1000}^{}𝑒^{−0.5𝑑}\,dℎ \\ & =200[−\frac{1}{0.5}⋅𝑒^{−0.5𝑑}]_{1000}^{} \\ & =−400\,𝑒^{−0.5𝑑}\,_{1000}^{} \\ & =−400(𝑒^{−50}−1) \\ & =400(1−𝑒^{−50}).\end{aligned}


$$

So, the column contains $400 \left(1-e^{-50} \right)$ million particles.

**** We can say that the number of particles is around $400$ million since the number $e^{-50}$ inside the parenthesis is extremely small (it's almost zero).

### Example: Integrating a Piecewise Density Function

#### Question

Suppose that the density of a certain substance in the ocean, in milligrams per cubic meter, at a depth of $h$ meters can be modeled by the function

$$


\begin{aligned}30−ℎ, & 0≤ℎ≤20 \\ 10\,𝑒^{2−0.1ℎ}, & ℎ>20.\end{aligned}


$$

Which integral expression gives the number of milligrams of the substance in a vertical column of water that has a height of $30 \, \text{m}$ and a constant horizontal cross-section of $4$ square meters?

#### Explanation

Here, the function $c(h)$ is a density function for the mass of the substance, and its units are $\text{mg}/\text{m}^3.$

The mass of a single vertical column measuring

$$


\underbrace{1\,\textrm{m}^2}_{\textrm{cross section}} \times \:\: \underbrace{30\, \textrm{m}}_{\textrm{height}}


$$

is given by the integral

$$


\int_{0}^{30} c(h) \, \text{d}h.


$$

However, since we want the mass of $4$ vertical columns (since that will give a cross-section of $4\,\textrm{m}^2),$ we need to multiply the above integral by $4.$ So the required mass is given by

$$


M = 4 \int_{0}^{30} c(h) \, \text{d}h.


$$

Therefore, we obtain

$$


\begin{aligned}𝑀 & =4∫_{300}^{}𝑐(ℎ)\,dℎ \\ & =4(∫_{200}^{}𝑐(ℎ)\,dℎ+∫_{3020}^{}𝑐(ℎ)\,dℎ) \\ & =4[∫_{200}^{}(30−ℎ)dℎ+∫_{3020}^{}10\,𝑒^{2−0.1ℎ}\,dℎ] \\ & =4∫_{200}^{}(30−ℎ)dℎ+40∫_{3020}^{}𝑒^{2−0.1ℎ}\,dℎ.\end{aligned}


$$

### Integrating Areas of Cross-Sections

A solid has a total height of $10$ centimeters. The area of its horizontal cross-section at height $h$ centimeters is modeled by the function

$$


A(h)= 2+2h,


$$

where $A(h)$ is measured in square centimeters. How can we find the total volume of the solid?

Here, $A(h)$ is the density function for the volume of the solid because the accumulation of area results in volume. Therefore, the volume $V$ of the solid can be found by integrating $A(h)$ from $h=0$ to $h=10,$ as follows:

$$


\begin{aligned}𝑉 & =∫_{100}^{}𝐴(ℎ)\,dℎ \\ & =∫_{100}^{}(2+2ℎ)\,dℎ \\ & =(2ℎ+ℎ^{2})_{100}^{} \\ & =(2(10)+(10)^{2})−0 \\ & =120\,cm^{3}\end{aligned}


$$

### Example: Finding a Volume by Integrating Areas of Cross-Sections

#### Question

A grain storage tank has a total height of $15$ feet. The area of its horizontal cross-section at height $h$ feet is modeled by the function

$$


A(h)= 3e^{-0.2h},


$$

where $A(h)$ is measured in square feet. What is the total volume of the tank?

#### Explanation

Here, $A(h)$ is the density function for the volume of the tank because the accumulation of area results in volume. Therefore, the volume $V$ of the tank can be found by integrating $A(h)$ from $h=0$ to $h=15{:}$

$$


\begin{aligned}𝑉 & =∫_{150}^{}𝐴(ℎ)\,dℎ \\ & =∫_{150}^{}3𝑒^{−0.2ℎ}\,dℎ \\ & =3⋅−\frac{1}{0.2}⋅[𝑒^{−0.2ℎ}]_{150}^{} \\ & =−15\,𝑒^{−0.2ℎ}_{150}^{} \\ & =15(1−𝑒^{−3}).\end{aligned}


$$

So, the volume of the tank is $15 \left(1 - e^{-3} \right)$ cubic feet.

### Example: Finding the Rate of Change of a Volume Given the Areas of Its Cross Sections

#### Question

The area, in square meters, of a horizontal cross-section of a water storage tank at height $h$ meters is modeled by the function

$$


A(h)=\dfrac{20}{1+0.25h^2}.


$$

Water is pumped into the tank. When the height of the water is $2$ meters, the height is increasing at the rate of $3$ meters per hour. Find the rate at which the volume of water in the tank is changing with respect to time when the height of the water is $2\,\text{m}.$

#### Explanation

The function $A(h)$ is a density function for the volume of the tank because an accumulation of area results in volume. Therefore, the volume $V(h)$ of the tank at height $h$ is given by the following:

$$


V(h) = \int_{0}^{h} A(x) \, \text{d}x


$$

****: Notice that we use a different variable ($x$) for the integration. This is to ensure that $V(h)$ is a function of $h$ only, and so we don't get confused. When calculating a definite integral, it does not matter which variable we use!

Our task is to find $\dfrac{\textrm d V}{\textrm d t},$ so we differentiate the above with respect to $t{:}$

$$


\dfrac{\textrm d V}{\textrm d t} = \dfrac{\textrm d }{\textrm d t}\int_{0}^{h} A(x) \, \text{d}x


$$

Using the chain rule, we have

$$


\dfrac{\textrm d V}{\textrm d t} = \dfrac{\textrm d h}{\textrm d t}\cdot\dfrac{\textrm d }{\textrm d h}\int_{0}^{h} A(x) \, \text{d}x.


$$

Using the second fundamental theorem of calculus, the derivative of the integral simplifies to $A(h),$ and we have

$$


\dfrac{\text{d}V}{\text{d}t} = \dfrac{\text{d}h}{\text{d}t}\cdot A(h) .


$$

Now, we use the given information:

- $\dfrac{\text{d}h}{\text{d}t} = 3 \, \text{m/h}$

- $A(2) = \dfrac{20}{1+0.25(2)^2} =10 \, \text{m}^2$

Finally,

$$


\begin{aligned}\frac{d𝑉}{d𝑡}_{ℎ=2} & =\frac{dℎ}{d𝑡}⋅𝐴(ℎ)_{ℎ=2} \\ & =3\,m/h⋅10\,m^{2} \\ & =30\,m^{3}/h.\end{aligned}


$$

Therefore, the volume of water is changing at a rate of $30$ cubic meters per hour.
