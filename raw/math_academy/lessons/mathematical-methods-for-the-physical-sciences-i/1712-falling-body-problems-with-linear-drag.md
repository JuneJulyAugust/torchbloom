# Falling Body Problems With Linear Drag

Source: https://www.mathacademy.com/topics/1712?courseId=154
Topic ID: 1712

## Prerequisites

- [Modeling With First-Order ODEs](./2023-modeling-with-first-order-odes.md)
- [Newton's Second Law](../calculus-i/2722-newton-s-second-law.md)
- [General Solutions of First-Order Linear ODEs](./6678-general-solutions-of-first-order-linear-odes.md)

## Lesson

### Introduction

Consider a body of mass falling vertically, influenced only by

- gravity, and

- air resistance (drag).

Assume that both and are constant, and choose the downward direction as the positive direction.

![Instructional graphic](../../lesson-assets/mathematical-methods-for-the-physical-sciences-i/topic-1712/daf3cd994575d8c7.png)

There are two forces acting on the body:

- The force due to gravity is the weight, which equals.

- The drag force is, since it acts upward (in the negative direction).

Hence, the net force on the body is

If drag is negligible, then, so the net force becomes

Applying Newton's second law,, where is the acceleration of the body, we get

Finally, since acceleration is the derivative of velocity,, we obtain

### A Worked Example

Suppose a supply drone of mass $3\,\textrm{kg}$ descends vertically. Let $v(t)$ be the drone's velocity, in meters per second, $t\geq 0$ seconds after the descent begins, with downward taken as the positive direction.

Assuming air resistance is negligible, and the only force acting on the drone is its weight due to gravity $g,$ let's find the differential equation that models the velocity.

Recall Newton's second law, which states that the resultant force $F$ acting on a body equals the product of its mass $m$ and acceleration $a{:}$

$$


F = ma


$$

Since air resistance is negligible, the only force acting on the drone is its weight due to gravity. The weight $w$ of the drone is given by

$$


\begin{aligned}𝐹 & =𝑤 \\ & =𝑚𝑔 \\ & =3𝑔.\end{aligned}


$$

Now, recall that acceleration is the derivative of velocity: $a=\dfrac{\mathrm{d}v}{\mathrm{d}t}.$ Substituting this into Newton's second law, along with our expression for the resultant force on the drone, we get

$$


3g = 3\,\dfrac{\mathrm{d}v}{\mathrm{d}t}


$$

Finally, simplifying and writing in standard form, we get

$$


\dfrac{\mathrm{d}v}{\mathrm{d}t} = g.


$$

### Example: Constructing and Solving a Falling Body Model With Negligible Drag

#### Question

A cryogenic sample container of mass $31\,\textrm{kg}$ is launched vertically downward with an initial velocity of $2.9\,\textrm{m/s}.$ Let $v(t)$ be the container's velocity, in meters per second, $t \geq 0$ seconds after release, with downward taken as the positive direction. The air resistance acting on the container is negligible, and the only other force acting on it is its weight due to gravity.

What is the velocity of the container after $7$ seconds? Assume that acceleration due to gravity is $g = 9.8\,\textrm{m/s}^2.$

#### Explanation

Recall Newton's second law, which states that the resultant force $F$ acting on a body equals the product of its mass $m$ and acceleration $a{:}$

$$


F = ma


$$

Since air resistance is negligible, the only force acting on the body is its weight due to gravity. The weight $w$ of the body is given by

$$


\begin{aligned}𝐹 & =𝑤 \\ & =𝑚𝑔 \\ & =31𝑔.\end{aligned}


$$

Now, recall that acceleration is the derivative of velocity: $a=\dfrac{\mathrm{d}v}{\mathrm{d}t}.$ Substituting this into Newton's second law, along with our expression for the resultant force on the container, we get

$$


31g = 31\,\dfrac{\mathrm{d}v}{\mathrm{d}t}.


$$

Simplifying and writing in standard form, we get

$$


\begin{aligned}\frac{d𝑣}{d𝑡} & =𝑔.\end{aligned}


$$

Next, we integrate to solve for $v(t),$ as follows:

$$


\begin{aligned}∫\frac{d𝑣}{d𝑡}\,d𝑡 & =𝑔∫d𝑡 \\ 𝑣(𝑡) & =𝑔𝑡+𝐶\end{aligned}


$$

Note that $C$ is a constant of integration. We're told that the initial velocity of the container is $2.9\,\textrm{m/s}.$ So, we apply the initial condition $v(0) = 2.9,$ and solve for $C{:}$

$$


\begin{aligned}𝑣(0)=𝑔⋅0+𝐶 \\ 2.9=0+𝐶 \\ 𝐶=2.9\end{aligned}


$$

Therefore, the velocity of the container $t$ seconds after release is

$$


v(t) = gt + 2.9.


$$

Finally, the velocity after $7$ seconds is

$$


v(7) = 9.8\cdot7 + 2.9 = 71.5 \,\textrm{m/s}.


$$

### Falling Body Problems With Linear Drag

Now, consider the case when drag is *not* negligible. At low speeds, drag is often approximately proportional to the body’s velocity. This model is called **linear drag**.

Defining the direction of motion (downwards) as positive, there are still two forces acting on the body:

- The force due to gravity is the weight, which equals $mg$.

- The drag force is where $k>0$ is a constant of proportionality (this force is negative because it acts upward, opposite the motion).

Hence, the net force on the body is

$$


F = mg - kv.


$$

Applying Newton's second law, $F=ma$, where $a$ is the acceleration of the body, we obtain

$$


\begin{aligned}𝐹 & =𝑚𝑔−𝑘𝑣 \\ 𝑚𝑎 & =𝑚𝑔−𝑘𝑣 \\ 𝑚\,\frac{d𝑣}{d𝑡} & =𝑚𝑔−𝑘𝑣\end{aligned}


$$

Finally, writing in standard form, we get

$$


m\,\dfrac{\mathrm{d}v}{\mathrm{d}t} + kv = mg \qquad\Longrightarrow\qquad \boxed{\dfrac{\mathrm{d}v}{\mathrm{d}t} + \dfrac{k}{m}v = g}.


$$

### Example: Constructing a Falling Body Model With Linear Drag

#### Question

A geological sampler of mass $15\,\textrm{kg}$ falls vertically downward. Let $v(t)$ be the sampler's velocity, in meters per second, $t \geq 0$ seconds after the descent began, with downward taken as the positive direction. The air resistance on the sampler is proportional to its velocity with a constant of proportionality $k > 0$ and acts in the direction opposite to motion. At a particular moment during the fall, the sampler’s velocity is $9\,\textrm{m/s}$ and instantaneous acceleration is $7.4\,\textrm{m/s}^2.$

Find the constant of proportionality $k,$ and the differential equation that best models the velocity. Assume the acceleration due to gravity is $g = 9.8\,\textrm{m/s}^2,$ and the only forces acting on the sampler are weight due to gravity and drag.

$\quad$ The constant of proportionality is $k=$ $(𝑞_{0},1,𝐿)$ $(𝑞_{0},1,𝐿)$

$\quad$ The differential equation that best models the velocity is $(𝑞_{0},2,𝐿,𝑚,𝑘,𝑙𝑜)$

#### Explanation

Recall Newton's second law, which states that the resultant force $F$ acting on a body equals the product of its mass $m$ and acceleration $a{:}$

$$


F = ma


$$

In our case, there are two forces acting on the body:

- The force due to gravity, given by the weight $w$ of the body, which equals

- The force due to drag (air resistance) $D,$ which is proportional to the velocity of the body (and negative since it acts in the negative direction): where $k>0$ is a constant of proportionality. Note that, since the drag, in $N=\text{kg}\cdot\text{m/s}^2,$ is the product of the constant $k$ and velocity, in $\text{m/s},$ the units of $k$ are

Summing the forces, the resultant force acting on the body is

$$


F = w + D = 15g - kv.


$$

Also, recall that acceleration is the derivative of velocity: $a=\dfrac{\mathrm{d}v}{\mathrm{d}t}.$ Substituting this into Newton's second law, along with our expression for the resultant force on the body, we have

$$


15g - kv = 15\,\dfrac{\mathrm{d}v}{\mathrm{d}t}.


$$

Writing in standard form, we get

$$


\begin{aligned}15\,\frac{d𝑣}{d𝑡}+𝑘𝑣 & =15𝑔 \\ \frac{d𝑣}{d𝑡}+\frac{𝑘}{15}𝑣 & =𝑔.\end{aligned}


$$

Now, we're given that, at a particular moment, the body's velocity is $9\,\textrm{m/s}$ and instantaneous acceleration is $7.4\,\textrm{m/s}^2.$ So, substituting $v=9, g = 9.8,$ and $\dfrac{\mathrm{d}v}{\mathrm{d}t} = 7.4$ into our model, we can solve for $k{:}$

$$


\begin{aligned}7.4+\frac{𝑘}{15}⋅9 & =9.8 \\ 7.4+\frac{3𝑘}{5} & =9.8 \\ \frac{3𝑘}{5} & =2.4 \\ 𝑘 & =4\,kg/s\end{aligned}


$$

Therefore, the differential equation that models the velocity is

$$


\dfrac{\mathrm{d}v}{\mathrm{d}t} + \dfrac4{15}v = g.


$$

### Example: Constructing and Solving a Falling Body Model With Linear Drag

#### Question

A supply container of mass $32\,\textrm{kg}$ is launched downward with an initial velocity of $7\,\textrm{m/s}$ and continues to fall vertically. Let $v(t)$ be the container's velocity, in meters per second, $t \geq 0$ seconds after launch, with downward taken as the positive direction. The air resistance on the container is proportional to its velocity and acts in the direction opposite to motion. At a particular moment during the fall, the container’s velocity is $8\,\textrm{m/s}$ and its instantaneous acceleration is $7.8\,\textrm{m/s}^2.$ Assume the acceleration due to gravity is $g = 9.8\,\textrm{m/s}^2,$ and the only forces acting on the container are the weight due to gravity and drag.

Find the equation for the velocity $v(t),$ expressing your answer in terms of $\bf t$ ****

#### Explanation

First, note that only two forces act on the body: the force due to gravity, given by the weight

$$


w = mg = 32\cdot9.8 = 313.6\,\textrm{N},


$$

and the force due to drag $D,$ which is proportional to the velocity (and negative since it acts in the negative direction),

$$


D=-kv,


$$

where $k>0$ is a constant of proportionality. Hence, the resultant force acting on the body is

$$


F = w + D = 313.6 - kv.


$$

Applying Newton's second law, we obtain an inhomogeneous first-order linear equation:

$$


\begin{aligned}𝐹 & =𝑚𝑎 \\ 313.6−𝑘𝑣 & =32\,\frac{d𝑣}{d𝑡} \\ \frac{d𝑣}{d𝑡}+\frac{𝑘}{32}𝑣 & =9.8\end{aligned}


$$

We're told that, at a particular moment, the body’s velocity is $8\,\textrm{m/s}$ and its instantaneous acceleration is $7.8\,\textrm{m/s}^2.$ Substituting these values into the ODE, we can solve for $k{:}$

$$


7.8 + \dfrac{k}{32}\cdot 8 = 9.8 \quad\Longrightarrow\quad k = 8\,\textrm{kg/s}


$$

Therefore, we have the following differential equation:

$$


\dfrac{\mathrm{d}v}{\mathrm{d}t} + \dfrac14v = 9.8


$$

This is a first-order linear equation with constant coefficients. So, to find the general solution, we must find the sum of the complementary and particular solutions.

- To find the complementary solution $v_c,$ we solve the corresponding homogeneous equation, given by Solving using an integration technique, such as separation of variables, we obtain the complementary solution where $A$ is a constant of integration.

- Next, we find the particular solution. Note that the right-hand side of the inhomogeneous equation is a polynomial of degree $0.$ So, we assume that the particular solution is also a polynomial of degree $0,$ i.e., To find the value of $\alpha,$ we substitute $v_p=\alpha$ and $\dfrac{\mathrm{d}v_p}{\mathrm{d}t} = (\alpha)' = 0$ into the inhomogeneous equation: Therefore, the particular solution is $v_p(t) = \dfrac{196}{5}.$

Now, since the general solution is given by the sum of the complementary solution and the particular solution, the general solution in our case is

$$


v(t) = v_c(t) + v_p(t) = Ae^{-t/4} + \dfrac{196}{5}.


$$

We're told that the body is launched downward with an initial velocity of $7\,\textrm{m/s}.$ So, we can apply the initial condition $v(0) = 7,$ and solve for $A{:}$

$$


\begin{aligned}𝑣(0) & =𝐴𝑒^{−0/4}+\frac{196}{5} \\ 7 & =𝐴+\frac{196}{5} \\ 𝐴 & =−\frac{161}{5}\end{aligned}


$$

Therefore, we have the following expression for $v(t){:}$

$$


\begin{aligned}𝑣(𝑡) & =−\frac{161}{5}𝑒^{−𝑡/4}+\frac{196}{5}\end{aligned}


$$

### Terminal Velocity

**Terminal velocity** is the constant speed a falling object approaches when the upward resistive force (such as drag) becomes large enough to exactly balance the downward gravitational force.

When drag is proportional to velocity, with a constant of proportionality $k>0,$ this balance occurs when

$$


mg - kv_\text{term} = 0.


$$

Solving for the terminal velocity, we get

$$


v_\text{term} = \dfrac{mg}{k}.


$$

For example, suppose a sealed electronics crate of mass $44\,\textrm{kg}$ falls vertically downward. Let $v$ be its velocity, with downward taken as the positive direction. The air resistance on the crate is proportional to its velocity with a constant of proportionality $k=8\,\textrm{kg/s}$ and acts opposite to the direction of motion.

Assuming that the acceleration due to gravity is $g = 9.8\,\textrm{m/s}^2,$ and the only forces acting on the crate are the weight due to gravity and drag, what is the terminal velocity $v_\text{term}$ of the crate?

Recall that at terminal velocity (a constant), acceleration is zero, so by $F=ma,$ the resultant force is zero.

First, note that only two forces act on the crate:

- the force due to gravity, given by the weight

- the force due to drag $D,$ which is proportional to the velocity (and negative since it acts in the negative direction),

Hence, the resultant force acting on the crate is

$$


F = w + D = 431.2 - 8v.


$$

When the crate reaches terminal velocity $v_\text{term},$ the resultant force is zero:

$$


431.2 - 8v_\text{term} = 0 \qquad\Longrightarrow\qquad v_\text{term} = \dfrac{431.2}{8} = 53.9


$$

Therefore, the terminal velocity of the crate is $v_\text{term} = 53.9\,\textrm{m/s}.$

### Example: Finding a Terminal Velocity

#### Question

A sensor pod of mass $20\,\textrm{kg}$ falls vertically downward. Let $v$ be its velocity, with downward taken as the positive direction. The air resistance on the pod is proportional to its velocity and acts in the opposite direction to the motion. At a particular moment during the fall, the pod’s velocity is $8\,\textrm{m/s}$ and its instantaneous acceleration is $6.3\,\textrm{m/s}^2.$

What is the terminal velocity $v_\text{term}$ of the pod? Assume the acceleration due to gravity is $g = 9.8\,\textrm{m/s}^2,$ and the only forces acting on the pod are the weight due to gravity and drag.

#### Explanation

Terminal velocity is the constant speed a falling object approaches as the upward resistive force (drag) grows to exactly balance the downward gravitational force. That is, at terminal velocity (a constant), acceleration is zero, so by $F=ma,$ the resultant force is zero.

First, note that only two forces act on the pod: the force due to gravity, given by the weight

$$


w = mg = 20\cdot9.8 = 196\,\textrm{N},


$$

and the force due to drag $D,$ which is proportional to the velocity (and negative since it acts in the negative direction),

$$


D=-kv,


$$

where $k>0$ is a constant of proportionality. Hence, the resultant force acting on the pod is

$$


F = w + D = 196 - kv.


$$

Applying Newton's second law, we obtain the following:

$$


\begin{aligned}𝐹 & =𝑚𝑎 \\ 196−𝑘𝑣 & =20𝑎\end{aligned}


$$

We're told that, at a particular moment, the pod’s velocity is $8\,\textrm{m/s}$ and its instantaneous acceleration is $6.3\,\textrm{m/s}^2.$ Substituting these values into the above, we can solve for $k{:}$

$$


\begin{aligned}196−8𝑘 & =20⋅6.3 \\ 196−8𝑘 & =126 \\ −8𝑘 & =−70 \\ 𝑘 & =8.75\,kg/s\end{aligned}


$$

Hence, the resultant force acting on the pod is

$$


F = 196 - 8.75v.


$$

When the pod reaches terminal velocity $v_\text{term},$ the resultant force is zero:

$$


196 - 8.75v_\text{term} = 0 \quad\Longrightarrow\quad v_\text{term} = \dfrac{196}{8.75} = 22.4


$$

Therefore, the terminal velocity of the pod is $v_\text{term} = 22.4\,\textrm{m/s}.$
