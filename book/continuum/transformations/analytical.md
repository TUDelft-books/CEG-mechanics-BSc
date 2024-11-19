```{index} Transformations
```
```{index} Tensors
```
```{index} Principal
```

# Analytical
```{figure} ./analytical_data/image.png
:align: center
:width: 400

Figure 2.2 {cite:ts}`Hartsuijker2007con`
```

## Transformations
Define rotation matrix R as:
$$R=\begin{bmatrix}
\cos(\alpha) & \sin(\alpha) \\
-\sin(\alpha) & \cos(\alpha)
\end{bmatrix}$$

Rotating a vector $F$ by an angle $\alpha$ is defined in matrix notation as:

$$\bar{F} = R\cdot F$$

The transformation rule for a stiffness matrix $K$ is defined in matrix notation as:

$$\bar{K} = R \cdot K \cdot R^T$$

This is treated in chapter 2.1 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.

## Tensors
Tensor notation for stiffness matrix $K$ in 2D is defined as follows: 
$$k_{ij} \quad \text{with} \quad i, j = x, y$$

The principal values of a 2D stiffness matrix are defined by:

$$k_{1,2} = \frac{1}{2}\left(k_{xx} + k_{yy}\right) \pm \sqrt{\left(\frac{1}{2}\left(k_{xx} + k_{yy}\right)\right)^2 + k_{xy}^2}$$

The principal directions of a 2D stiffness matrix are defined by:

$$\tan{2\alpha_0} = \frac{k_{xy}}{\frac{1}{2}\left(k_{xx} - k_{yy}\right)}$$

This is treated in chapter 2.2 and 2.3 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.