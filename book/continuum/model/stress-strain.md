```{index} Poisson's ratio
```
```{index} Stress-Strain relations
```

# Stress-Strain relations
Poisson's ratio $\nu$ relates strains with stresses in perpendicular directions.

The complete stress strain relation in 3D is defined as:

$$\begin{bmatrix}
\epsilon_{xx} \\
\epsilon_{yy} \\
\epsilon_{zz} \\
2\epsilon_{xy} \\
2\epsilon_{yz} \\
2\epsilon_{zx}
\end{bmatrix} = 
\frac{1}{E}
\begin{bmatrix}
1 & -\nu & -\nu & 0 & 0 & 0 \\
-\nu & 1 & -\nu & 0 & 0 & 0 \\
-\nu & -\nu & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 2(1+\nu) & 0 & 0 \\
0 & 0 & 0 & 0 & 2(1+\nu) & 0 \\
0 & 0 & 0 & 0 & 0 & 2(1+\nu) \\
\end{bmatrix}
\begin{bmatrix}
\sigma_{xx} \\
\sigma_{yy} \\
\sigma_{zz} \\
\sigma_{xy} \\
\sigma_{yz} \\
\sigma_{zx}
\end{bmatrix}$$

This is treated in chapter 4 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.

## Instructions from lecture
This topic is presented in Dutch in a lecture available from 0:15:50 to 1:24:00 [here](https://collegeramavideoportal.tudelft.nl/catalogue/ctb2210/presentation/afa01c66a9434fae8e4a95c0b0a3348b1d?academicYear=2025-2026-ctb2210).

## Exercises
Problems 1-3 in chapter 5 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`. Instead of applying the circle of Mohr, apply the transformulation formulas. Answers are available in chapter 5 of the lecture notes.