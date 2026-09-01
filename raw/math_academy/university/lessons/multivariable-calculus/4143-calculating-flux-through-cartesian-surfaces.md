# Calculating Flux Through Cartesian Surfaces

Source: https://www.mathacademy.com/topics/4143?courseId=54
Topic ID: 4143

## Prerequisites

- [Calculating Flux Through Parametric Surfaces](./4145-calculating-flux-through-parametric-surfaces.md)

## Lesson

### Introduction

Let's calculate the flux of the vector field

$$


\mathbf{F}(x,y,z)=\left\langle (x-y)^2, \:(x+y)^2, \: 12xy \right\rangle


$$

through the surface $S$ defined by the Cartesian equation

$$


z=2y-2x


$$

for $0 \leq x \leq 1$ and $0 \leq y \leq 1.$

For surfaces like this, substituting $x=u$ and $y=v,$ we obtain a parametrization

$$


\mathbf{r}(u,v) = \left\langle u,\: v,\: 2v-2u \right\rangle


$$

over the domain

$$


D = \big\{ (u,v) \: : \: 0 \leq u \leq 1, \: 0 \leq v \leq 1 \big\}.


$$

Recall that for a surface $S$ with parametrization $\mathbf{r}(u,v)$ for $(u,v) \in D,$ the flux of a vector field $\mathbf{F}$ over $S$ is given by

$$


\iint\limits_S \mathbf{F} \cdot \text{d}\mathbf{S} = \iint\limits_S \mathbf{F} \cdot \mathbf{n} \,\text{d}S = \iint\limits_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}'_u \times \mathbf{r}'_v) \,\text{d}A.


$$

We now compute the tangent vectors to the grid curves:

$$


\begin{aligned}𝐫_{′𝑢} & =⟨\frac{𝜕𝑥}{𝜕𝑢},\,\frac{𝜕𝑦}{𝜕𝑢},\,\frac{𝜕𝑧}{𝜕𝑢}⟩ \\ & =⟨\frac{𝜕}{𝜕𝑢}(𝑢),\,\frac{𝜕}{𝜕𝑢}(𝑣),\,\frac{𝜕}{𝜕𝑢}(2𝑣−2𝑢)⟩ \\ & =⟨1,\,0,\,−2⟩ \\ 𝐫_{′𝑣} & =⟨\frac{𝜕𝑥}{𝜕𝑣},\,\frac{𝜕𝑦}{𝜕𝑣},\,\frac{𝜕𝑧}{𝜕𝑣}⟩ \\ & =⟨\frac{𝜕}{𝜕𝑣}(𝑢),\,\frac{𝜕}{𝜕𝑣}(𝑣),\,\frac{𝜕}{𝜕𝑣}(2𝑣−2𝑢)⟩ \\ & =⟨0,\,1,\,2⟩\end{aligned}


$$

So, the fundamental vector product is

$$


\begin{aligned}𝐫_{′𝑢}×𝐫_{′𝑣} & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 1 & 0 & −2 \\ 0 & 1 & 2\end{matrix} \\ & =⟨\begin{matrix}0 & −2 \\ 1 & 2\end{matrix},\,−\begin{matrix}1 & −2 \\ 0 & 2\end{matrix},\,\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}⟩ \\ & =⟨2,\,−2,\,1⟩.\end{aligned}


$$

Next, we substitute the coordinate expressions of $\mathbf{r}(u,v)$ into $\mathbf{F}(x,y,z){:}$

$$


\begin{aligned}𝐅(𝐫(𝑢,𝑣)) & =⟨(𝑥−𝑦)^{2},\,(𝑥+𝑦)^{2},\,12𝑥𝑦⟩_{𝑥=𝑢,\,\,𝑦=𝑣,\,\,𝑧=2𝑣−2𝑢} \\ & =⟨(𝑢−𝑣)^{2},\,(𝑢+𝑣)^{2},\,12𝑢𝑣⟩\end{aligned}


$$

Then, we calculate the dot product of $\mathbf{F}$ and $\mathbf{r}'_u \times \mathbf{r}'_v{:}$

$$


\begin{aligned}𝐅(𝐫(𝑢,𝑣))⋅(𝐫_{′𝑢}×𝐫_{′𝑣}) & =⟨(𝑢−𝑣)^{2},\,(𝑢+𝑣)^{2},\,12𝑢𝑣⟩⋅⟨2,\,−2,\,1⟩ \\ & =(𝑢−𝑣)^{2}⋅2+(𝑢+𝑣)^{2}⋅(−2)+12𝑢𝑣⋅1 \\ & =4𝑢𝑣.\end{aligned}


$$

Therefore, the flux of $\mathbf F$ through $S$ is given by

$$


\begin{aligned}\underset{𝑆}{∬}⟨(𝑥−𝑦)^{2},\,(𝑥+𝑦)^{2},\,12𝑥𝑦⟩⋅d𝐒 & =\underset{𝐷}{∬}𝐅(𝐫(𝑢,𝑣))⋅(𝐫_{′𝑢}×𝐫_{′𝑣})\,d𝐴 \\ & =\underset{𝐷}{∬}4𝑢𝑣\,d𝐴 \\ & =∫_{10}∫_{10}4𝑢𝑣\,d𝑣\,d𝑢 \\ & =∫_{10}2𝑢\,d𝑢⋅∫_{10}2𝑣\,d𝑣 \\ & =[𝑢^{2}]_{10}⋅[𝑣^{2}]_{10} \\ & =(1^{2}−0^{2})⋅(1^{2}−0^{2}) \\ & =1.\end{aligned}


$$

### Example: Expressing Flux Over a Surface as a Repeated Integral

#### Question

Consider the vector field $\mathbf{F}(x,y,z)=\left\langle z+2y, \: 3y+z, \: x -z\right\rangle$ and the surface $S$ defined by $z=-3x+2y$ for $0 \leq x \leq 2$ and $0 \leq y \leq 1.$ Using the parametrization $x=u$ and $y=v,$ the flux of $\mathbf F$ through $S$ can be expressed as

$$


𝐴𝐴𝐴𝐴𝐴𝐴𝐴


$$

What is the missing expression?

#### Explanation

For a surface $S$ with parametrization $\mathbf{r}(u,v)$ for $(u,v) \in D,$ the flux of a vector field $\mathbf{F}$ over $S$ is given by

$$


\iint\limits_S \mathbf{F} \cdot \text{d}\mathbf{S} = \iint\limits_S \mathbf{F} \cdot \mathbf{n} \,\text{d}S = \iint\limits_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}'_u \times \mathbf{r}'_v) \,\text{d}A.


$$

Using the parametrization, where $x=u$ and $y=v,$ our surface can be parameterized as

$$


\mathbf{r}(u,v) = \left\langle u,\: v,\: -3u+2v \right\rangle


$$

over the domain

$$


D = \big\{ (u,v) \: : \: 0 \leq u \leq 2, \: 0 \leq v \leq 1 \big\}.


$$

We now compute the tangent vectors to the grid curves:

$$


\begin{aligned}𝐫_{′𝑢} & =⟨\frac{𝜕𝑥}{𝜕𝑢},\,\frac{𝜕𝑦}{𝜕𝑢},\,\frac{𝜕𝑧}{𝜕𝑢}⟩ \\ & =⟨\frac{𝜕}{𝜕𝑢}(𝑢),\,\frac{𝜕}{𝜕𝑢}(𝑣),\,\frac{𝜕}{𝜕𝑢}(−3𝑢+2𝑣)⟩ \\ & =⟨1,\,0,\,−3⟩ \\ 𝐫_{′𝑣} & =⟨\frac{𝜕𝑥}{𝜕𝑣},\,\frac{𝜕𝑦}{𝜕𝑣},\,\frac{𝜕𝑧}{𝜕𝑣}⟩ \\ & =⟨\frac{𝜕}{𝜕𝑣}(𝑢),\,\frac{𝜕}{𝜕𝑣}(𝑣),\,\frac{𝜕}{𝜕𝑣}(−3𝑢+2𝑣)⟩ \\ & =⟨0,\,1,\,2⟩\end{aligned}


$$

Now, the fundamental vector product is

$$


\begin{aligned}𝐫_{′𝑢}×𝐫_{′𝑣} & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 1 & 0 & −3 \\ 0 & 1 & 2\end{matrix} \\ & =⟨\begin{matrix}0 & −3 \\ 1 & 2\end{matrix},\,−\begin{matrix}1 & −3 \\ 0 & 2\end{matrix},\,\begin{matrix}1 & 0 \\ 0 & 1\end{matrix}⟩ \\ & =⟨3,\,−2,\,1⟩.\end{aligned}


$$

Next, we substitute the coordinate expressions of $\mathbf{r}(u,v)$ into $\mathbf{F}(x,y,z){:}$

$$


\begin{aligned}𝐅(𝐫(𝑢,𝑣)) & =⟨𝑧+2𝑦,\,3𝑦+𝑧,\,𝑥−𝑧⟩_{𝑥=𝑢,\,\,𝑦=𝑣,\,\,𝑧=−3𝑢+2𝑣} \\ & =⟨(−3𝑢+2𝑣)+2𝑣,\,3𝑣+(−3𝑢+2𝑣),\,𝑢−(−3𝑢+2𝑣)⟩ \\ & =⟨−3𝑢+4𝑣,\,−3𝑢+5𝑣,\,4𝑢−2𝑣⟩\end{aligned}


$$

Then, we calculate the dot product of $\mathbf{F}$ and $\mathbf{r}'_u \times \mathbf{r}'_v{:}$

$$


\begin{aligned}𝐅(𝐫(𝑢,𝑣))⋅(𝐫_{′𝑢}×𝐫_{′𝑣}) & =⟨−3𝑢+4𝑣,\,−3𝑢+5𝑣,\,4𝑢−2𝑣⟩⋅⟨3,\,−2,\,1⟩ \\ & =(−3𝑢+4𝑣)⋅(3)+(−3𝑢+5𝑣)⋅(−2)+(4𝑢−2𝑣)⋅1 \\ & =−9𝑢+12𝑣+6𝑢−10𝑣+4𝑢−2𝑣 \\ & =𝑢\end{aligned}


$$

Therefore, the surface integral can be written as

$$


\begin{aligned}\underset{𝑆}{∬}⟨𝑧+2𝑦,\,3𝑦+𝑧,\,𝑥−𝑧⟩⋅d𝐒 & =\underset{𝐷}{∬}𝐅(𝐫(𝑢,𝑣))⋅(𝐫_{′𝑢}×𝐫_{′𝑣})\,d𝐴 \\ & =\underset{𝐷}{∬}𝑢\,d𝐴 \\ & =∫_{20}∫_{10}𝑢\,d𝑣\,d𝑢.\end{aligned}


$$

So, the missing expression is ${\color{blue}u}.$

### Formulas for Flux Over Cartesian Surfaces

Let's now derive a general formula for the flux through an *upward-oriented* Cartesian surface.

For a surface $S$ with parametrization $\mathbf{r}(u,v)$ for $(u,v) \in D,$ the flux of a vector field $\mathbf{F}$ over $S$ is given by

$$


\iint\limits_S \mathbf{F} \cdot \text{d}\mathbf{S} = \iint\limits_S \mathbf{F} \cdot \mathbf{n} \,\text{d}S = \iint\limits_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}'_u \times \mathbf{r}'_v) \,\text{d}A.


$$

Consider a surface $S$ given by the equation $z=g(x,y).$ The canonical parameterization of the surface is

$$


\mathbf{r}(x,y) = \left\langle x,\: y,\: g(x,y) \right\rangle.


$$

Computing the tangent vectors to the grid curves, we get

$$


\begin{aligned}𝐫_{′𝑥} & =⟨1,\,0,\,\frac{𝜕𝑔}{𝜕𝑥}⟩ \\ 𝐫_{′𝑦} & =⟨0,\,1,\,\frac{𝜕𝑔}{𝜕𝑦}⟩\end{aligned}


$$

Next, the fundamental vector product is

$$


\begin{aligned}𝐫_{′𝑥}×𝐫_{′𝑦} & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 1 & 0 & \frac{𝜕𝑔}{𝜕𝑥} \\ 0 & 1 & \frac{𝜕𝑔}{𝜕𝑦}\end{matrix}=⟨−\frac{𝜕𝑔}{𝜕𝑥},\,−\frac{𝜕𝑔}{𝜕𝑦},\,1⟩.\end{aligned}


$$

Notice that the $\mathbf k$-component is positive, which indicates that our surface is upward-oriented.

Therefore, the surface integral can be written as

$$


\begin{aligned}\underset{𝑆}{∬}𝐅⋅d𝐒 & =\underset{𝐷}{∬}𝐅(𝐫(𝑥,𝑦))⋅(𝐫_{′𝑥}×𝐫_{′𝑦})\,d𝐴 \\ & =\underset{𝐷}{∬}⟨𝑃,\,𝑄,\,𝑅⟩⋅⟨−\frac{𝜕𝑔}{𝜕𝑥},\,−\frac{𝜕𝑔}{𝜕𝑦},\,1⟩\,d𝐴 \\ & =\underset{𝐷}{∬}(−𝑃\frac{𝜕𝑔}{𝜕𝑥}−𝑄\frac{𝜕𝑔}{𝜕𝑦}+𝑅)\,d𝐴.\end{aligned}


$$

We summarize as follows:

- *For a surface $S$ given by $z = g(x,y)$ for $(x,y) \in D,$ the flux of a vector field $\mathbf{F}(x,y,z) = \left\langle P,\: Q,\: R \right\rangle$ over $S$ is given by*

We have analogous results for surfaces of the form $y = h(x,z)$ and $x=k(y,z){:}$

- *For a surface $S$ given by $y = h(x,z)$ for $(x,z) \in D,$ the flux of a vector field $\mathbf{F}(x,y,z) = \left\langle P,\: Q,\: R \right\rangle$ over $S$ is given by* *where the unit normal to the surface is chosen such that the $\mathbf j$-component is positive.*

- *For a surface $S$ given $x = k(y,z)$ for $(y,z) \in D,$ the flux of a vector field $\mathbf{F}(x,y,z) = \left\langle P,\: Q,\: R \right\rangle$ over $S$ is given by* *where the unit normal to the surface is chosen such that the $\mathbf i$-component is positive.*

### Example: Expressing Flux Over a Surface as a Repeated Integral Using a Formula

#### Question

For a surface $S$ given by $y = h(x,z)$ for $(x,z) \in D,$ the flux of the vector field $\mathbf{F}(x,y,z) = \left\langle P,\: Q,\: R \right\rangle$ over $S$ is given by

$$


\iint\limits_S \mathbf{F} \cdot \text{d}\mathbf{S} = \iint\limits_D \Bigg( \boxed{\phantom{A}} \dfrac{\partial h}{\partial x} + Q - \boxed{\phantom{A}} \dfrac{\partial h}{\partial z} \Bigg) \: \text{d}A,


$$

From left to right, what are the missing parts of the formula?

**

#### Explanation

For a surface $S$ with parametrization $\mathbf{r}(u,v)$ for $(u,v) \in D,$ the flux of a vector field $\mathbf{F}$ over $S$ is given by

$$


\iint\limits_S \mathbf{F} \cdot \text{d}\mathbf{S} = \iint\limits_S \mathbf{F} \cdot \mathbf{n} \,\text{d}S = \iint\limits_D \mathbf{F}(\mathbf{r}(u,v)) \cdot (\mathbf{r}'_u \times \mathbf{r}'_v) \,\text{d}A.


$$

Since our surface $S$ is of the form $y = h(x,z),$ it can be parameterized as

$$


\mathbf{r}(x,z) = \left\langle x, \: h(x,z),\: z \right\rangle.


$$

We now compute the tangent vectors to the grid curves:

$$


\begin{aligned}𝐫_{′𝑥} & =⟨1,\,\frac{𝜕ℎ}{𝜕𝑥},\,0⟩ \\ 𝐫_{′𝑧} & =⟨0,\frac{𝜕ℎ}{𝜕𝑧},\,1⟩\end{aligned}


$$

Now, the fundamental vector product is

$$


\begin{aligned}𝐫_{′𝑥}×𝐫_{′𝑧} & =\begin{matrix}𝐢 & 𝐣 & 𝐤 \\ 1 & \frac{𝜕ℎ}{𝜕𝑥} & 0 \\ 0 & \frac{𝜕ℎ}{𝜕𝑧} & 1\end{matrix}=⟨\frac{𝜕ℎ}{𝜕𝑥},\,−1,\,\frac{𝜕ℎ}{𝜕𝑧}⟩.\end{aligned}


$$

However, notice that the $\mathbf j$-component is negative. Therefore, we select the normal vector that points in the ** direction:

$$


\mathbf{r}'_z \times \mathbf{r}'_x = - \mathbf{r}'_x \times \mathbf{r}'_z = \left \langle -\dfrac{\partial h}{\partial x}, \: 1, \: -\dfrac{\partial h}{\partial z} \right \rangle


$$

Therefore, the surface integral can be written as

$$


\begin{aligned}\underset{𝑆}{∬}𝐅⋅d𝐒 & =\underset{𝐷}{∬}𝐅(𝐫(𝑥,𝑧))⋅(𝐫_{′𝑥}×𝐫_{′𝑧})\,d𝐴 \\ & =\underset{𝐷}{∬}⟨𝑃,\,𝑄,\,𝑅⟩⋅⟨−\frac{𝜕ℎ}{𝜕𝑥},\,1,\,−\frac{𝜕ℎ}{𝜕𝑧}⟩\,d𝐴 \\ & =\underset{𝐷}{∬}(−𝑃\frac{𝜕ℎ}{𝜕𝑥}+𝑄−𝑅\frac{𝜕ℎ}{𝜕𝑧})\,d𝐴.\end{aligned}


$$

### Example: Evaluating Flux Over a Surface

#### Question

Calculate the flux of the vector field

$$


\mathbf F(x, y, z) = \left\langle -y, \: x, \: z+2 \right\rangle,


$$

where the surface $S$ is defined by $z=x^2+y^2$ for $0 \leq x \leq 1$ and $0 \leq y \leq 1.$

#### Explanation

For a surface $S$ given by $z = g(x,y)$ for $(x,y) \in D,$ the flux of a vector field $\mathbf{F}(x,y,z) = \left\langle P,\: Q,\: R \right\rangle$ over $S$ is given by

$$


\iint\limits_S \mathbf{F} \cdot \text{d}\mathbf{S} = \iint\limits_D \left( -P\dfrac{\partial g}{\partial x} - Q\dfrac{\partial g}{\partial y} + R \right) \text{d}A.


$$

We first compute the partial derivatives of the graph $z=g(x,y){:}$

$$


\begin{aligned}\frac{𝜕𝑔}{𝜕𝑥} & =\frac{𝜕}{𝜕𝑥}(𝑥^{2}+𝑦^{2})=2𝑥 \\ \frac{𝜕𝑔}{𝜕𝑦} & =\frac{𝜕}{𝜕𝑦}(𝑥^{2}+𝑦^{2})=2𝑦\end{aligned}


$$

Next, we substitute the equation $z=g(x,y)$ into $\mathbf F(x,y,z){:}$

$$


\begin{aligned}𝐅(𝑥,𝑦,𝑔(𝑥,𝑦)) & =⟨−𝑦,\,𝑥,\,𝑧+2⟩_{𝑧=𝑥^{2}+𝑦^{2}} \\ & =⟨\underset{𝑃}{\underset{}{−𝑦}},\,\underset{𝑄}{\underset{}{𝑥}},\,\underset{𝑅}{\underset{}{𝑥^{2}+𝑦^{2}+2}}⟩\end{aligned}


$$

Therefore, we can evaluate our surface integral as follows:

$$


\begin{aligned}\underset{𝑆}{∬}⟨−𝑦,\,𝑥,\,𝑧+2⟩⋅d𝐒 & =\underset{𝐷}{∬}(−𝑃\frac{𝜕𝑔}{𝜕𝑥}−𝑄\frac{𝜕𝑔}{𝜕𝑦}+𝑅)d𝐴 \\ & =\underset{𝐷}{∬}(−(−𝑦)⋅(2𝑥)−(𝑥)⋅(2𝑦)+𝑥^{2}+𝑦^{2}+2)\,d𝐴 \\ & =\underset{𝐷}{∬}(2𝑥𝑦−2𝑥𝑦+𝑥^{2}+𝑦^{2}+2)\,d𝐴 \\ & =∫_{10}∫_{10}(𝑥^{2}+𝑦^{2}+2)\,d𝑦\,d𝑥 \\ & =∫_{10}[𝑥^{2}𝑦+\frac{𝑦^{3}}{3}+2𝑦]_{10}\,d𝑥 \\ & =∫_{10}(𝑥^{2}+\frac{1}{3}+2)\,d𝑥 \\ & =∫_{10}(𝑥^{2}+\frac{7}{3})\,d𝑥 \\ & =[\frac{𝑥^{3}}{3}+\frac{7𝑥}{3}]_{10} \\ & =\frac{1}{3}+\frac{7}{3} \\ & =\frac{8}{3}\end{aligned}


$$
