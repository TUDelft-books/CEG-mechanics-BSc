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

## Exercises
Problems 1-3 in chapter 5 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`. Answers are available in chapter 5 of the lecture notes.