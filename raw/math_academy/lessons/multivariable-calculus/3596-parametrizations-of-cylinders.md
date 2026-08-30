# Parametrizations of Cylinders

Source: https://www.mathacademy.com/topics/3596?courseId=54
Topic ID: 3596

## Prerequisites

- [Parametric Equations of Horizontal Hyperbolas](../integrated-math-iii-honors/873-parametric-equations-of-horizontal-hyperbolas.md)
- [Parametric Equations of Parabolas](../integrated-math-iii-honors/875-parametric-equations-of-parabolas.md)
- [Parametric Surfaces](./1789-parametric-surfaces.md)
- [Cylinders](./1895-cylinders.md)
- [Parametric Equations of Ellipses](../integrated-math-iii-honors/2746-parametric-equations-of-ellipses.md)
- [Parametric Equations of Vertical Hyperbolas](../integrated-math-iii-honors/2981-parametric-equations-of-vertical-hyperbolas.md)

## Lesson

### Introduction

In this lesson, we will explore strategies for parametrizing cylinders.

Parametrizing a cylinder is no more difficult than parametrizing its base curve. The only difference is that we need a *second* parameter to control the variation parallel to the cylinder's axis. This second parameter is usually allowed to vary arbitrarily.

For example, consider the parabolic cylinder defined in Cartesian coordinates as

$$


y = 8x^2.


$$

Notice that $y = y(x)$ is an explicit function of $x.$ Therefore, for any point $(x,y,z)$ on this surface, we have

$$


\begin{aligned}𝐟(𝑥,𝑧) & =⟨𝑥,𝑦,𝑧⟩ \\ & =⟨𝑥,\,8𝑥^{2},\,𝑧⟩.\end{aligned}


$$

And that's it! We have successfully found a parametrization of this cylinder.

Note that, under this parametrization

- the parameter $x \in (-\infty,\infty)$ controls the movement along the base curve, and

- the parameter $z \in (-\infty,\infty)$ controls the movement parallel to the $z$-axis.

Let's see some more examples.

### Example: Parametrizing a Parabolic Cylinder

#### Question

$$


\mathbf{f}(x,y) = \big\langle x, \: y, \: \boxed{\phantom{0}} \big\rangle


$$

The vector-valued function $\mathbf{f}(x,y)$ above parametrizes the parabolic cylinder defined in Cartesian coordinates as $2x^2=z.$ What is the third component of $\mathbf{f}?$

#### Explanation

For any point $(x,y,z)$ on our surface, we obtain the following:

$$


\begin{aligned}𝐟(𝑥,𝑦) & =⟨𝑥,𝑦,𝑧⟩ \\ & =⟨𝑥,\,𝑦,\,2𝑥^{2}⟩\end{aligned}


$$

where $x \in (-\infty,\infty)$ and $y \in (-\infty,\infty).$

Therefore, the third component of $\mathbf{f}$ is ${\color{blue} 2x^2}.$

### Elliptic Cylinders

Let's find a parametrization of the elliptic cylinder defined in Cartesian coordinates as

$$


\dfrac{x^2}{25}+\dfrac{z^2}{16}=1.


$$

The base curve in the $xz$-plane is an ellipse centered at $O$ with semi-axes of lengths $\sqrt{25} = 5$ and $\sqrt{16} = 4.$ Therefore, we can parametrize the base curve in the $xz$-plane as follows:

$$


\langle x,z \rangle = \big\langle 5\cos{t}, \: 4\sin{t} \big\rangle, \qquad t \in [0,2\pi).


$$

Now, for any point $(x,y,z)$ on our surface, we obtain the following parametrization:

$$


\begin{aligned}𝐟(𝑡,𝑦) & =⟨𝑥,𝑦,𝑧⟩ \\ & =⟨5cos⁡𝑡,\,𝑦,\,4sin⁡𝑡⟩\end{aligned}


$$

where $t \in [0,2\pi)$ and $y \in (-\infty,\infty).$

Note that the axis of the cylinder coincides with the $y$-axis. Therefore, the parameter $y$ is allowed to vary arbitrarily.

### Example: Parametrizing an Elliptic Cylinder

#### Question

$$


\mathbf{f}(t,z) = \big\langle \boxed{\phantom{0}}, \: 4\sin{t}, \: z \big\rangle


$$

The vector-valued function $\mathbf{f}(t,z)$ above parametrizes the elliptic cylinder defined in Cartesian coordinates as $\dfrac{x^2}{4}+\dfrac{y^2}{16}=1.$ What is the first component of $\mathbf{f}?$

#### Explanation

Recall that the ellipse $\dfrac{x^2}{4}+\dfrac{y^2}{16}=1$ in $xy$-plane has the parametrization

$$


\langle x,y \rangle = \big\langle 2\cos{t}, \: 4\sin{t} \big\rangle, \qquad t \in [0,2\pi),


$$

since

$$


\begin{aligned}\frac{𝑥^{2}}{4}+\frac{𝑦^{2}}{16} & =\frac{(2cos⁡𝑡)^{2}}{4}+\frac{(4sin⁡𝑡)^{2}}{16} \\ & =\frac{4cos^{2}⁡𝑡}{4}+\frac{16sin^{2}⁡𝑡}{16} \\ & =cos^{2}⁡𝑡+sin^{2}⁡𝑡 \\ & =1.\end{aligned}


$$

Now, for any point $(x,y,z)$ on our surface, we obtain the following:

$$


\begin{aligned}𝐟(𝑡,𝑧) & =⟨𝑥,𝑦,𝑧⟩ \\ & =⟨2cos⁡𝑡,\,4sin⁡𝑡,\,𝑧⟩\end{aligned}


$$

where $t \in [0,2\pi)$ and $z \in (-\infty,\infty).$

Therefore, the first component of $\mathbf{f}$ is ${\color{blue}2\cos{t}}.$

### Hyperbolic Cylinders

To find a parametrization of one sheet of the hyperbolic cylinder defined in Cartesian coordinates as

$$


\dfrac{x^2}{25}-\dfrac{y^2}{16}=1


$$

for $x \geq 5,$ recall that the corresponding hyperbola in $xy$-plane has the parametrization

$$


\langle x,y \rangle = \big\langle 5 \sec{t}, \: 4 \tan{t} \big\rangle, \qquad t\in\left(-\dfrac\pi2,\dfrac\pi2\right)


$$

We can check that this indeed parametrizes our base hyperbola by substituting the parametric equations into the equation of the base curve:

$$


\begin{aligned}\frac{𝑥^{2}}{25}−\frac{𝑦^{2}}{16} & =\frac{(5sec⁡𝑡)^{2}}{25}−\frac{(4tan⁡𝑡)^{2}}{16} \\ & =sec^{2}⁡𝑡−tan^{2}⁡𝑡 \\ & =1\end{aligned}


$$

Now, for any point $(x,y,z)$ on our surface, we obtain the following:

$$


\begin{aligned}𝐟(𝑡,𝑧) & =⟨𝑥,𝑦,𝑧⟩ \\ & =⟨5sec⁡𝑡,\,4tan⁡𝑡,\,𝑧⟩\end{aligned}


$$

where $t\in\left(-\dfrac\pi2,\dfrac\pi2\right)$ and $z \in (-\infty,\infty).$

### Example: Parametrizing a Hyperbolic Cylinder

#### Question

$$


\mathbf{f}(t,y) = \big \langle 4\tan{t}, \, y, \, \boxed{\phantom{0}} \big\rangle, \qquad t\in\left(-\dfrac\pi2,\dfrac\pi2\right)


$$

The vector-valued function $\mathbf{f}(t,y)$ above parametrizes one sheet of the hyperbolic cylinder defined in Cartesian coordinates as $\dfrac{z^2}{4} - \dfrac{x^2}{16} = 1$ for $z \geq 2.$ What is the third component of $\mathbf{f}?$

#### Explanation

Recall that the hyperbola $\dfrac{z^2}{4} - \dfrac{x^2}{16} = 1$ for $z \geq 2$ in $xz$-plane has the parametrization

$$


\langle x , z \rangle = \big \langle 4\tan{t}, \, 2\sec{t} \big\rangle, \qquad t \in \left(-\dfrac{\pi}{2},\dfrac{\pi}{2}\right)


$$

since

$$


\begin{aligned}\frac{𝑧^{2}}{4}−\frac{𝑥^{2}}{16} & =\frac{(2sec⁡𝑡)^{2}}{4}−\frac{(4tan⁡𝑡)^{2}}{16} \\ & =\frac{4sec^{2}⁡𝑡}{4}−\frac{16tan^{2}⁡𝑡}{16} \\ & =sec^{2}⁡𝑡−tan^{2}⁡𝑡 \\ & =1.\end{aligned}


$$

Now, for any point $(x,y,z)$ on our surface, we obtain the following:

$$


\begin{aligned}𝐟(𝑡,𝑦) & =⟨𝑥,𝑦,𝑧⟩ \\ & =⟨4tan⁡𝑡,\,𝑦,\,2sec⁡𝑡⟩\end{aligned}


$$

where $t \in \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$ and $y \in (-\infty, \infty).$

Therefore, the third component of $\mathbf{f}$ is ${\color{blue}2\sec{t}}.$
