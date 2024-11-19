```{index} Isotropic stress component
```
```{index} Deviatoric stress component
```

# Isotropic and deviatoric components
$$\sigma=
\begin{bmatrix}
\sigma_{xx} & \sigma_{xy} & \sigma_{xz}\\
\sigma_{yx} & \sigma_{yy} & \sigma_{yz}\\
\sigma_{zx} & \sigma_{zy} & \sigma_{zz}
\end{bmatrix}=
\begin{bmatrix}
\sigma_{0} & 0 & 0\\
0 & \sigma_{0} & 0\\
0 & 0 & \sigma_{0}
\end{bmatrix}+
\begin{bmatrix}
\sigma_{xx}-\sigma_0 & \sigma_{xy} & \sigma_{xz}\\
\sigma_{yx} & \sigma_{yy}-\sigma_0 & \sigma_{yz}\\
\sigma_{zx} & \sigma_{zy} & \sigma_{zz}-\sigma_0
\end{bmatrix}
$$

$$\sigma_0 = \frac{1}{3}(\sigma_{xx}+\sigma_{yy}+\sigma_{zz})$$
The isotropic stress component (diagonal matrix) will only cause a change in volume, the deviatoric stress component is responsible for a distortion.

This is treated in chapter 1.1.2 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.