# Cauchy-Euler Equations: Characteristic Equations With Complex Roots

Source: https://www.mathacademy.com/topics/2545?courseId=61
Topic ID: 2545

## Prerequisites

- [Second-Order Homogeneous ODEs: Characteristic Equations With Complex Roots](./880-second-order-homogeneous-odes-characteristic-equations-with-complex-roots.md)
- [Cauchy-Euler Equations: Characteristic Equations With Distinct Real Roots](./2528-cauchy-euler-equations-characteristic-equations-with-distinct-real-roots.md)

## Lesson

### Introduction

When the characteristic equation of a Cauchy-Euler equation has the complex roots $\lambda = a \pm b \textrm{i},$ the general solution is

$$


y(t) = A t^{a + b \textrm{i}} + B t^{a - b \textrm{i}}.


$$

For example, if the complex roots are $\lambda = 2 \pm 3 \textrm{i},$ then the general solution is

$$


y(t) = A t^{2 + 3 \textrm{i}} + B t^{2 - 3 \textrm{i}}.


$$

However, we can simplify this form of the general solution even further using Euler's formula. To start, let's focus on $t^{2+3\textrm{i}}$ and separate it into a product:

$$


t^{2+3\textrm{i}} = t^{2} t^{3\textrm{i}}


$$

Now, using the rules of logarithms, we have that

$$


t^{3\textrm{i}} = e^{\ln t^{3\textrm{i}} } = e^{3\textrm{i} \ln t}.


$$

Then, using Euler's formula, we have

$$


e^{3\textrm{i} \ln t} = e^{\textrm{i} \cdot 3 \ln t} = \cos (3 \ln t) + \textrm{i} \sin (3 \ln t).


$$

So, we have that

$$


t^{2+3\textrm{i}} = t^2 \left( \cos (3 \ln t) + \textrm{i} \sin (3 \ln t) \right).


$$

By the same reasoning,

$$


\begin{aligned}𝑡^{2−3i} & =𝑡^{2}(cos⁡(−3ln⁡𝑡)+isin⁡(−3ln⁡𝑡)) \\ & =𝑡^{2}(cos⁡(3ln⁡𝑡)−isin⁡(3ln⁡𝑡)).\end{aligned}


$$

Therefore, the general solution can be expressed as

$$


\begin{aligned}𝑦(𝑡) & =𝐴𝑡^{2+3i}+𝐵𝑡^{2−3i} \\ & =𝐴𝑡^{2}(cos⁡(3ln⁡𝑡)+isin⁡(3ln⁡𝑡))+𝐵𝑡^{2}(cos⁡(3ln⁡𝑡)−isin⁡(3ln⁡𝑡)) \\ & =𝑡^{2}((𝐴+𝐵)cos⁡(3ln⁡𝑡)+i(𝐴−𝐵)sin⁡(3ln⁡𝑡)).\end{aligned}


$$

Finally, we can rewrite $y(t)$ as

$$


y(t) = t^{2} \left( c_1 \cos( 3 \ln{t} ) + c_2 \sin( 3 \ln{t} ) \right),


$$

where $c_1 = A+B$ and $c_2 = \textrm{i}(A-B).$

### The Shortcut for Cauchy-Euler Equations with Complex Roots

In general, if the characteristic equation of a Cauchy-Euler equation has imaginary roots $\lambda = a \pm b\textrm{i},$ then the general solution is

$$


y(x) = Ax^{a+b\textrm{i}} + B x^{a-b\textrm{i}}.


$$

Using Euler's formula, the above can be simplified to

$$


y(t) = x^a \left( c_1 \cos(b \ln x) + c_2 \sin(b \ln x) \right)


$$

where $c_1 = A+B$ and $c_2=\textrm{i} (A-B).$

### Example: Solving a Cauchy-Euler Equation with Imaginary Roots

#### Question

Find the general solution to the equation

$$


x^2 y'' + xy' + 4y = 0,\quad x > 0.


$$

#### Explanation

This is an instance of the Cauchy-Euler equation. So, we assume the solutions take the form $y=x^\lambda.$ Differentiating $y$ with respect to $x$ gives

$$


y' = \lambda x^{\lambda -1}, \qquad y'' = \lambda(\lambda-1)x^{\lambda-2}


$$

Substituting the above to our differential equation gives

$$


\begin{aligned}𝑥^{2}⋅𝜆(𝜆−1)𝑥^{𝜆−2}+𝑥⋅𝜆𝑥^{𝜆−1}+4𝑥^{𝜆} & =0 \\ 𝜆(𝜆−1)𝑥^{𝜆}+𝜆𝑥^{𝜆}+4𝑥^{𝜆} & =0 \\ 𝑥^{𝜆}[𝜆(𝜆−1)+𝜆+4] & =0.\end{aligned}


$$

So, we have the following characteristic equation:

$$


\begin{aligned}𝜆(𝜆−1)+𝜆+4 & =0 \\ 𝜆^{2}+4 & =0 \\ 𝜆^{2} & =−4 \\ 𝜆 & =±2i\end{aligned}


$$

Therefore, the general solution is

$$


y(x)=c_1 \cos( 2 \ln{x} ) + c_2\sin( 2 \ln{x} ).


$$

### Example: Solving a Cauchy-Euler Equation with Complex Roots

#### Question

Determine the general solution to the equation

$$


t^2 y'' +5ty'+8y = 0,\quad t\gt 0.


$$

#### Explanation

This is an instance of the Cauchy-Euler equation. So, we assume the solutions take the form $y=t^\lambda.$ Differentiating $y$ with respect to $t$ gives

$$


y' = \lambda t^{\lambda -1}, \qquad y'' = \lambda(\lambda-1)t^{\lambda-2}.


$$

Substituting the above to our differential equation gives

$$


\begin{aligned}𝑡^{2}⋅𝜆(𝜆−1)𝑡^{𝜆−2}+5𝑡⋅𝜆𝑡^{𝜆−1}+8𝑡^{𝜆} & =0 \\ 𝜆(𝜆−1)𝑡^{𝜆}+5𝜆𝑡^{𝜆}+8𝑡^{𝜆} & =0 \\ 𝑡^{𝜆}[𝜆(𝜆−1)+5𝜆+8] & =0.\end{aligned}


$$

So, we have the following characteristic equation:

$$


\begin{aligned}𝜆(𝜆−1)+5𝜆+8 & =0 \\ 𝜆^{2}+4𝜆+8 & =0\end{aligned}


$$

We solve the auxiliary equation by completing the square:

$$


\begin{aligned}𝜆^{2}+4𝜆+8 & =0 \\ (𝜆^{2}+4𝜆+4)−4+8 & =0 \\ (𝜆+2)^{2} & =−4 \\ 𝜆+2 & =±2i \\ 𝜆 & =−2±2i\end{aligned}


$$

Therefore, the general solution is

$$


y(t) = t^{-2} \left( c_1 \cos( 2 \ln{t} ) + c_2 \sin( 2 \ln{t} ) \right).


$$

### Example: Solving an Initial Value Problem Involving a Cauchy-Euler Equation with Imaginary Roots

#### Question

Given that the differential equation

$$


x^2 y'' + xy' + 49 y = 0


$$

has the general solution

$$


y(x)= c_1 \cos(7 \ln{x} ) + c_2\sin(7 \ln{x} ),


$$

solve the initial value problem

$$


x^2 y'' + xy' + 49 y = 0, \quad y(1) = 0, \quad y'(1) = -7, \quad x > 0.


$$

#### Explanation

We find the constants $c_1$ and $c_2$ using the initial conditions.

- Substituting $y(1) = 0$ into the general solution gives

- To apply the condition $y'(1) = -7,$ we first differentiate $y$ to get Then, we substitute $y'(1) = -7$ and $c_1 = 0$ into the above to get

Therefore, the solution to the initial value problem is

$$


y(x) = -\sin(7 \ln{x} ).


$$

### Example: Solving an Initial Value Problem Involving a Cauchy-Euler Equation with Complex Roots

#### Question

Given that the differential equation

$$


2t^2 y'' -2ty' +20 y= 0


$$

has the general solution

$$


y = t(c_1 \cos( 3 \ln{t} ) + c_2\sin( 3 \ln{t}) ),


$$

solve the initial value problem

$$


2t^2 y'' -2ty' +20 y= 0, \quad y(1)= 0, \quad y'(1) = -1, \quad t\gt 0.


$$

#### Explanation

We find the constants $c_1$ and $c_2$ using the initial conditions.

- Substituting $y(1) = 0$ into the general solution gives

- To apply the condition $y'(1) = -1,$ we first differentiate $y$ to get Then, we substitute $y'(1) = -1$ and $c_1=0$ into the above to get

Therefore, the solution to the initial value problem is

$$


y(t) = -\dfrac{ t\sin( 3 \ln{t}) )}{3}.


$$
