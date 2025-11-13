```{index} Strains in 2D
```

# Strains in 2D

Strains in 2D can be represented in a matrix (specifically a second-order tensor) as follows:

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

## Instructions from lecture
This topic is presented in Dutch in a lecture available from 0:58:10 to 1:12:10 [here](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/08600f8d8be64fd69111bd21b3cac6311d?academicYear=2025-2026-ctb2210).