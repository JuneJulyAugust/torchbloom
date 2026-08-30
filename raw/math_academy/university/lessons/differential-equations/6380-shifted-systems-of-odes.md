# Shifted Systems of ODEs

Source: https://www.mathacademy.com/topics/6380?courseId=61
Topic ID: 6380

## Prerequisites

- [Phase Portraits for Linear Systems With Complex Eigenvalues](./3241-phase-portraits-for-linear-systems-with-complex-eigenvalues.md)
- [Phase Portraits for Linear Systems With Zero Eigenvalues](./6379-phase-portraits-for-linear-systems-with-zero-eigenvalues.md)

## Lesson

### Introduction

Suppose we have a system of ODEs such as

$$


\mathbf{x}' = \mathbf{f}(x(t),y(t))


$$

with a nonzero equilibrium point $\mathbf{x}^\ast$ satisfying $\mathbf{f}(\mathbf{x}^\ast) = \mathbf{0}.$

Instead of analyzing the system near a *nonzero* equilibrium $\mathbf{x}^\ast,$ we can introduce *shifted coordinates* so that the equilibrium becomes the origin. We define the **deviation vector**

$$


\mathbf{u} = \mathbf{x} - \mathbf{x}^\ast,


$$

so that

$$


\mathbf{u} = \mathbf{0} \qquad\Leftrightarrow\qquad \mathbf{x} = \mathbf{x}^\ast.


$$

This transformed system has several advantages: shifting the equilibrium to the origin makes the system easier to analyze without altering its behavior.

To illustrate, let's consider the following system of ODEs:

$$


[\begin{aligned}3 & 2 \\ −5 & 1\end{aligned}]


$$

The equilibrium point of the system is $[1, \, -1]^T.$ What is the system obtained by shifting the equilibrium to the origin?

To shift the system's equilibrium from $\mathbf{x}^\ast$ to the origin, we define the deviation vector

$$


\mathbf{u} = \mathbf{x} - \mathbf{x}^\ast.


$$

In our case, we have

$$


[\begin{aligned}1 \\ −1\end{aligned}]


$$

Substituting $\mathbf{x}$ and $\mathbf{x}'$ into the given system, we obtain

$$


\begin{aligned}𝐱^{′} & =[\begin{aligned}3 & 2 \\ −5 & 1\end{aligned}]𝐱+[\begin{aligned}−1 \\ 6\end{aligned}] \\ 𝐮^{′} & =[\begin{aligned}3 & 2 \\ −5 & 1\end{aligned}](𝐮+[\begin{aligned}1 \\ −1\end{aligned}])+[\begin{aligned}−1 \\ 6\end{aligned}] \\ & =[\begin{aligned}3 & 2 \\ −5 & 1\end{aligned}]𝐮+[\begin{aligned}3 & 2 \\ −5 & 1\end{aligned}][\begin{aligned}1 \\ −1\end{aligned}]+[\begin{aligned}−1 \\ 6\end{aligned}] \\ & =[\begin{aligned}3 & 2 \\ −5 & 1\end{aligned}]𝐮+[\begin{aligned}1 \\ −6\end{aligned}]+[\begin{aligned}−1 \\ 6\end{aligned}] \\ & =[\begin{aligned}3 & 2 \\ −5 & 1\end{aligned}]𝐮.\end{aligned}


$$

Therefore, the shifted system is

$$


[\begin{aligned}3 & 2 \\ −5 & 1\end{aligned}]


$$

Notice that for linear systems, shifting the equilibrium to the origin just removes the constant term.

### Example: Shifting the Equilibrium to the Origin: Linear Systems

#### Question

$$


\begin{aligned}𝑥^{′}(𝑡)=3𝑥(𝑡)−2𝑦(𝑡)+1 \\ 𝑦^{′}(𝑡)=4𝑥(𝑡)+𝑦(𝑡)−6\end{aligned}


$$

Consider the system of ODEs above. The equilibrium point of the system is $[1, \, 2]^T.$ What is the system obtained by shifting the equilibrium to the origin?

#### Explanation

Writing our system in matrix form, we get

$$


[\begin{aligned}3 & −2 \\ 4 & 1\end{aligned}]


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$

To shift the system's equilibrium from $\mathbf{x}^\ast$ to the origin, we define the deviation vector

$$


\mathbf{u} = \mathbf{x} - \mathbf{x}^\ast,


$$

where $[\begin{aligned}𝑢(𝑡) \\ 𝑣(𝑡)\end{aligned}]$

In our case, we have

$$


[\begin{aligned}1 \\ 2\end{aligned}]


$$

Substituting $\mathbf{x}$ and $\mathbf{x}'$ into the given system, we obtain

$$


\begin{aligned}𝐱^{′} & =[\begin{aligned}3 & −2 \\ 4 & 1\end{aligned}]𝐱+[\begin{aligned}1 \\ −6\end{aligned}] \\ 𝐮^{′} & =[\begin{aligned}3 & −2 \\ 4 & 1\end{aligned}](𝐮+[\begin{aligned}1 \\ 2\end{aligned}])+[\begin{aligned}1 \\ −6\end{aligned}] \\ & =[\begin{aligned}3 & −2 \\ 4 & 1\end{aligned}]𝐮+[\begin{aligned}3 & −2 \\ 4 & 1\end{aligned}][\begin{aligned}1 \\ 2\end{aligned}]+[\begin{aligned}1 \\ −6\end{aligned}] \\ & =[\begin{aligned}3 & −2 \\ 4 & 1\end{aligned}]𝐮+[\begin{aligned}−1 \\ 6\end{aligned}]+[\begin{aligned}1 \\ −6\end{aligned}] \\ & =[\begin{aligned}3 & −2 \\ 4 & 1\end{aligned}]𝐮.\end{aligned}


$$

Therefore, the shifted system is the following:

$$


\begin{aligned}𝑢^{′}(𝑡)=3𝑢(𝑡)−2𝑣(𝑡) \\ 𝑣^{′}(𝑡)=4𝑢(𝑡)+𝑣(𝑡)\end{aligned}


$$

### Example: Shifting the Equilibrium to the Origin: Non-Linear Systems

#### Question

$$


\begin{aligned}𝑥^{′}(𝑡)=𝑥^{2}(𝑡)+𝑥(𝑡)+𝑦(𝑡)+2 \\ 𝑦^{′}(𝑡)=5𝑥(𝑡)−𝑦^{2}(𝑡)+3𝑦(𝑡)+10\end{aligned}


$$

Consider the system of ODEs above. An equilibrium point of the system is $[0, \, -2]^T.$ What system is obtained by shifting this equilibrium to the origin?

#### Explanation

To shift the system's equilibrium from $\mathbf{x}^\ast$ to the origin, we define the deviation vector

$$


\mathbf{u} = \mathbf{x} - \mathbf{x}^\ast,


$$

where $[\begin{aligned}𝑥(𝑡) \\ 𝑦(𝑡)\end{aligned}]$ and $[\begin{aligned}𝑢(𝑡) \\ 𝑣(𝑡)\end{aligned}]$

In our case, we have

$$


[\begin{aligned}0 \\ −2\end{aligned}]


$$

In coordinate form, this can be written as follows:

$$


x(t) = u(t), \qquad y(t) = v(t) - 2, \qquad x'(t) = u'(t), \qquad v'(t) = y'(t).


$$

Let's now substitute these into the given system.

- Substituting into the first equation, we obtain

- Substituting into the second equation, we obtain

Therefore, the shifted system is the following:

$$


\begin{aligned}𝑢^{′}(𝑡)=𝑢^{2}(𝑡)+𝑢(𝑡)+𝑣(𝑡) \\ 𝑣^{′}(𝑡)=5𝑢(𝑡)−𝑣^{2}(𝑡)+7𝑣(𝑡)\end{aligned}


$$

### Properties of Shifted Systems

Recall that when we shift coordinates by defining

$$


u = x - x^\ast,\qquad v = y - y^\ast,


$$

we translate the coordinate system so that the equilibrium $(x^\ast, y^\ast)$ becomes $(0,0).$

This translation preserves several important properties of the system. Shifting coordinates does not change the dynamics of the system, it only changes where the equilibrium appears in the coordinate plane. In particular:

1. *Eigenvalues do not change:* After shifting a linear system, the eigenvalues and the corresponding eigenvectors are unchanged.

2. *Stability type is preserved:* The equilibrium retains its original classification (saddle, node, spiral, center, etc.). Shifting does not alter the local behavior near the equilibrium.

3. *Trajectory shapes are unchanged up to translation:* Trajectories in the $(u,v)$-plane have the same shapes as those in the $(x,y)$-plane. Only their location changes.

4. *Equilibria correspond one-to-one:* The target equilibrium $(x^\ast, y^\ast)$ maps to $(u,v) = (0,0).$ The shift does not create or remove equilibria.

5. *Nullclines translate but retain the same shape:* The geometric structure of the vector field is preserved under translation.

Let's proceed to some examples.

### Example: Identifying Properties of a Shifted System

#### Question

A linear system of ODEs has an equilibrium at $\mathbf{x}^\ast.$ One of the nullclines of the system has the equation $y=3x-1$ in the corresponding phase space. The system is then shifted using $\mathbf{u} = \mathbf{x} - \mathbf{x}^\ast.$ Which of the following is **** to be a nullcline of the shifted system?

1. $y=3x+3$

2. $y=-x$

3. $y=3x$

4. $y=-3x$

#### Explanation

After shifting a system, the geometric structure of the vector field is preserved. In particular, each nullcline is translated but retains its orientation, meaning its slope does not change.

Because the equilibrium is moved to the origin by the shift, the translated nullclines must pass through the origin in the shifted coordinates.

Thus, the nullclines of the shifted system pass through the origin and have the same slopes as the corresponding nullclines of the original system.

Among the given options, the only line that satisfied the above conditions is $y=3x.$
