```{index} Strains in 2D
```

# Strains in 2D
```{figure} ./strains-3D_data/image.png
:align: center
:width: 400

Figure 1.9 {cite:ts}`Hartsuijker2007con`
```
Strains in 2D can be represented in matrix notation as follows:
$$\begin{bmatrix}
\Delta u_x \\
\Delta u_y
\end{bmatrix}=
\begin{bmatrix}
\epsilon_{xx} & \epsilon_{xy} \\
\epsilon_{yx} & \epsilon_{yy}
\end{bmatrix}\begin{bmatrix}
\Delta x \\
\Delta y
\end{bmatrix}+
\begin{bmatrix}
0 & -\omega \\
\omega & 0
\end{bmatrix}\begin{bmatrix}
\Delta x \\
\Delta y
\end{bmatrix}$$

The first part is a deformation, the second part is a rigid body rotation.

This is treated in chapter 1.2 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.
