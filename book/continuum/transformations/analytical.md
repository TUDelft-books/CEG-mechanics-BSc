```{index} Transformations
```
```{index} Tensors
```
```{index} Principal
```

# Analytical
```{figure} ./analytical_data/image.png
:align: center
:width: 600

Figure 2.2 {cite:ts}`Hartsuijker2007con`
```

## Transformations
The rotation matrix R is defined as:

$$\text{R}=\begin{bmatrix}
\cos(\alpha) & \sin(\alpha) \\
-\sin(\alpha) & \cos(\alpha)
\end{bmatrix}$$

Rotating a first-order tensor (for example force $F$) by an angle $\alpha$ is defined as:

$$\bar{F} = \text{R} \cdot F $$

The transformation rule for a second order tensor (for example stiffness matrix $K$) is defined in matrix notation as:

$$\bar{\text{K}} = \text{R} \cdot \text{K} \cdot \text{R}^T$$

This is treated in chapter 2.1 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.

The individual terms of $\bar{\text{K}}$ can be written out as:

- $k_{\bar x \bar x} = \cfrac{1}{2}\left(k_{xx} + k_{yy}\right) + \cfrac{1}{2}\left(k_{xx} - k_{yy}\right) \cos \left(2\alpha\right) + k_{xy} \sin \left(2 \alpha\right)$
- $k_{\bar y \bar y} = \cfrac{1}{2}\left(k_{xx} + k_{yy}\right) - \cfrac{1}{2}\left(k_{xx} - k_{yy}\right) \cos \left(2\alpha\right) - k_{xy} \sin \left(2 \alpha\right)$
- $k_{\bar x \bar y} = -\cfrac{1}{2}\left(k_{xx} - k_{yy}\right) \sin \left(2 \alpha \right) + k_{xy} \cos \left(2 \alpha\right)$

The principal values of the second order tensor $\bar{\text{K}}$ are defined by:

$$k_{1,2} = \frac{1}{2}\left(k_{xx} + k_{yy}\right) \pm \sqrt{\left(\frac{1}{2}\left(k_{xx} + k_{yy}\right)\right)^2 + k_{xy}^2}$$

The principal directions of the second order tensor $\bar{\text{K}}$ are defined by:

$$\tan{2\alpha_0} = \frac{k_{xy}}{\frac{1}{2}\left(k_{xx} - k_{yy}\right)}$$

This is treated in chapter 2.3 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.