# Resonance in Vibrating Systems

Source: https://www.mathacademy.com/topics/6720?courseId=154
Topic ID: 6720

## Prerequisites

- [Forced Oscillators](./2526-forced-oscillators.md)

## Lesson

### Introduction

A standard vibrating system under an external force looks like where is the system's natural **internal frequency**.

The complementary solution describes the system's internal oscillation when there is no external force. It can be written as so the motion naturally oscillates at frequency

If the external force is periodic, then it has its own forcing frequency **Resonance** occurs when the forcing frequency matches the natural frequency:

Intuitively, resonance happens because the force repeatedly "pushes" the system at exactly the right rhythm each cycle. In the undamped model, these pushes continually add energy to the system at just the right phase, causing the oscillation amplitude to grow without bound.

For example, suppose the position measured in meters, of a particle oscillating with periodically forced harmonic motion without damping is governed by the equation where is the time, in seconds. Let's find the value of the parameter that causes the oscillator to resonate.

Notice that the complementary solution has frequency where Therefore,

The external force is which has forcing frequency

Resonance occurs when so

Let's see more examples.

### Example: Calculating the Value of a Parameter that Results in Resonance

#### Question

The position $y(t),$ measured in meters, of a particle oscillating with periodically forced harmonic motion without damping is governed by the equation

$$


y'' + 25y =2\sin^2{pt},


$$

where $t > 0$ is the time, in seconds. Which value of the parameter $p$ causes the oscillator to resonate?

#### Explanation

First, we find the general solution of the differential equation. The complementary solution $y_c$ here represents simple harmonic motion, and it can be written as

$$


y_c=A\cos{\omega t} + B\sin{\omega t}.


$$

In our case,

$$


\omega^2 = 25\qquad\Longrightarrow\qquad \omega = 5,


$$

so, we have

$$


y_c=A\cos{5 t} + B\sin{5 t}.


$$

The oscillator experiences resonance when the frequency of the external periodic force $2 \sin^2 pt$ is equal to the frequency of the complementary solution, which is $\omega = 5.$ Since

$$


f(t) = 2 \sin^2 pt = 1 - \cos 2pt,


$$

the frequency of the external periodic force is $2p.$ Therefore, the oscillator experiences resonance when

$$


2p = 5 \qquad\Longrightarrow\qquad p = \dfrac{5}{2}.


$$

### Example: Determining the Spring Constant Given an External Periodic Force

#### Question

A particle of mass $0.25\,\text{kg}$ is attached to a massless spring. An external periodic force $F(t) = 3\sin(6t)\,\text{N}$ is applied to the particle.

The position of the particle is $y(t)$ (measured in meters), and $t>0$ is the time in seconds. If the particle moves with forced harmonic motion without damping and the system experiences resonance, what is the spring constant $k?$

#### Explanation

The equation of motion for a particle of mass $m$ moving with forced harmonic motion without damping under the action of a spring with spring constant $k$ and external force $F(t)$ is given by

$$


my'' = -ky + F(t).


$$

Substituting our values for $m$ and $F(t)$ gives

$$


0.25y'' = - ky + 3\sin(6t).


$$

Simplifying and rearranging the above equation, we get

$$


y'' + 4ky = 12\sin(6t).


$$

The complementary solution $y_c$ here represents simple harmonic motion, and it can be written as

$$


y_c = A\cos \omega t + B\sin \omega t,


$$

where $A$ and $B$ are arbitrary constants of integration, and $\omega$ is the system's internal frequency.

In our case,

$$


\omega^2 = 4k \qquad\Longrightarrow\qquad k = \dfrac14\omega^2.


$$

The oscillator experiences resonance when the frequency of the external periodic force $f(t)=12\sin(6t),$ which is $6,$ is equal to the frequency of the complementary solution $\omega.$

Therefore,

$$


k = \dfrac14\omega^2 = \dfrac14\cdot6^2 = 9 \,\text{kg/s}^2.


$$

### General Solutions to Forced Harmonic Motion Equations With Resonance

Consider an undamped forced oscillator,

$$


y''+\omega^2y=f(t),


$$

where $\omega$ is the system's natural frequency. Its general solution is

$$


y=y_c+y_p,


$$

where $y_c$ solves the homogeneous equation $y''+\omega^2y=0$ and $y_p$ is any particular solution to the full equation.

Notice that the complementary solution can be written in any of the following equivalent forms:

1. $y_c = R\cos{(\omega t + \phi_1)}$

2. $y_c = R\sin{(\omega t + \phi_2)}$

3. $y_c =A\cos{\omega t} + B\sin{\omega t}$

Now, suppose the external force has the resonant form

$$


f(t)=a\cos(\omega t)+b\sin(\omega t),


$$

so that the forcing frequency equals the natural frequency $\omega.$

A sinusoidal trial at frequency $\omega$ would duplicate $y_c,$ so at resonance we multiply by $t$ and use a trial of the form

$$


y_p=t\bigl(C\cos(\omega t)+D\sin(\omega t)\bigr).


$$

To determine $C$ and $D,$ we first compute derivatives:

$$


\begin{aligned}𝑦_{′𝑝} & =𝐶cos⁡(𝜔𝑡)+𝐷sin⁡(𝜔𝑡)+𝑡(−𝐶𝜔sin⁡(𝜔𝑡)+𝐷𝜔cos⁡(𝜔𝑡)) \\ 𝑦_{″𝑝} & =2(−𝐶𝜔sin⁡(𝜔𝑡)+𝐷𝜔cos⁡(𝜔𝑡))−𝑡𝜔^{2}(𝐶cos⁡(𝜔𝑡)+𝐷sin⁡(𝜔𝑡))\end{aligned}


$$

Substituting into the equation, we have that the $t$-terms cancel out, and we obtain

$$


\begin{aligned}𝑦_{″𝑝}+𝜔^{2}𝑦_{𝑝}=2𝜔𝐷cos⁡(𝜔𝑡)−2𝜔𝐶sin⁡(𝜔𝑡).\end{aligned}


$$

Since we need $y_p''+\omega^2y_p=f(t)=a\cos(\omega t)+b\sin(\omega t),$ equating coefficients gives

$$


2\omega D=a, \qquad -2\omega C=b.


$$

Therefore,

$$


C=-\frac{b}{2\omega}, \qquad D=\frac{a}{2\omega},


$$

so a standard resonant particular solution is

$$


y_p =\frac{t}{2\omega}\bigl(-b\cos(\omega t)+a\sin(\omega t)\bigr).


$$

So, when $f(t)=a\cos(\omega t)+b\sin(\omega t)$ and resonance occurs, the general solution can be written as

$$


\boxed{y=A\cos(\omega t)+B\sin(\omega t)+\dfrac{t}{2\omega}\bigl(-b\cos(\omega t)+a\sin(\omega t)\bigr)}.


$$

### Example: Identifying Solutions to Forced Harmonic Motion Equations

#### Question

A particle is moving with forced harmonic motion without damping. The particle is acted on by an external periodic force $f(t) = 4\cos(4t)+12\sin(4t).$ Assuming the system experiences resonance, which of the following could be used to represent the general solution for the position $y(t)?$

1. $y = R\cos(4t+\phi) - \dfrac{3}{2}t\cos(4t) + \dfrac{1}{2}t\sin(4t)$

2. $y = R\sin(4t+\phi) - \dfrac{3}{2}t\cos(4t) + \dfrac{1}{2}t\sin(4t)$

3. $y = A\cos(4t) + B\sin(4t) - \dfrac{3}{2}t\cos(4t)$

Note that $A,$ $B,$ $R,$ and $\phi$ are constants.

#### Explanation

Because the motion is undamped and the system experiences resonance, the forcing frequency equals the natural frequency $\omega.$

The external force is $f(t)=4\cos(4t)+12\sin(4t),$ which is sinusoidal with frequency $4.$ Therefore, $\omega = 4.$

The complementary solution for the associated simple harmonic motion equation can be written in three different forms:

1. $y_c = R\cos{(\omega t + \phi)} = R\cos{(4t + \phi)}$

2. $y_c = R\sin{(\omega t + \phi)} = R\sin{(4t + \phi)}$

3. $y_c =A\cos{\omega t} + B\sin{\omega t} = A\cos(4t) + B\sin(4t)$

At resonance, a sinusoidal trial at frequency $\omega$ duplicates the complementary solution, so we multiply by $t$ and take a resonant particular solution of the form

$$


y_p(t)=t(C\cos(4t)+D\sin(4t)).


$$

By substituting the particular solution and $\omega=4$ into the differential equation, $y'' + \omega^2y = f(t),$ we get

$$


\begin{aligned}[8(𝐷−2𝐶𝑡)cos⁡(4𝑡)−8(𝐶+2𝐷𝑡)sin⁡(4𝑡)]+16𝑡(𝐶cos⁡(4𝑡)+𝐷sin⁡(4𝑡)) & =4cos⁡(4𝑡)+12sin⁡(4𝑡) \\ 8𝐷cos⁡(4𝑡)−8𝐶sin⁡(4𝑡) & =4cos⁡(4𝑡)+12sin⁡(4𝑡)\end{aligned}


$$

Equating coefficients, $C=-\dfrac{3}{2}$ and $D=\dfrac{1}{2}.$

So, the particular solution is

$$


y_p(t) = -\dfrac{3}{2}t\cos(4t) + \dfrac{1}{2}t\sin(4t).


$$

Finally, then, the general solution is given by the sum of the complementary and particular solutions. So, it can be written in any of the following forms:

1. $y = R\cos{(4t + \phi)} - \dfrac{3}{2}t\cos(4t) + \dfrac{1}{2}t\sin(4t)$

2. $y = R\sin{(4t + \phi)} - \dfrac{3}{2}t\cos(4t) + \dfrac{1}{2}t\sin(4t)$

3. $y = A\cos(4t) + B\sin(4t) - \dfrac{3}{2}t\cos(4t) + \dfrac{1}{2}t\sin(4t)$

Only solutions I and II match the forms above. Therefore, the correct answer is "I and II only".

### Practical Resonance

Recall that resonance is the phenomenon where an external periodic force drives a vibrating system at exactly the system's natural frequency. In the undamped model, this causes the oscillations to grow larger and larger over time.

In the ideal undamped model, resonance produces a particular solution that grows in magnitude with time (due to the extra factor of $t$). This is why the model predicts that the amplitude increases *without bound*.

For example, consider the undamped forced oscillator

$$


y'' + 9y = \sin(3t).


$$

The complementary solution is of the form $y_c = A\cos(3t) + B\sin(3t),$ the natural frequency of the system is $\omega = 3,$ and the forcing frequency is also $3.$ Because these frequencies match, resonance occurs.

Since the forcing term $\sin(3t)$ duplicates a term in the homogeneous solution, we must multiply our guess by $t.$ We try a solution of the form $y_p = t(C\cos(3t) + D\sin(3t)).$

Calculating the derivatives of $y_p,$ substituting them into the equation, and equating coefficients of $\sin(3t)$ and $\cos(3t)$ yields $C=-\dfrac16$ and $D=0.$ So, the particular solution is of the form

$$


y_p = -\dfrac{t}{6}\cos(3t).


$$

Notice that this solution grows larger as $t$ increases. This time-dependent growth illustrates how resonance leads to an increase in oscillation amplitude in the undamped model.

In real systems, perfectly *unbounded growth* does not occur because physical effects, such as damping and energy loss, eventually limit the amplitude. Even so, forcing near the natural frequency can still produce very large oscillations, which is why resonance is important in engineering design.
