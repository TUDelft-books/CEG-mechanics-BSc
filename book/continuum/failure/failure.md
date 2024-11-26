```{index} Von Mises
```
```{index} Tresca
```

# Failure
```{figure} ./failure_data/image.png
:align: center
:width: 400

Figure 6.14b {cite:ts}`Hartsuijker2007con`
```

## Von Mises failure model
Von Mises assumed failure if the deviatoric stress exceeds a limit value $s_{max}$:

$$\frac{1}{3}\left((\sigma_1-\sigma_2)^2 + (\sigma_2-\sigma_3)^2 + (\sigma_3-\sigma_1)^2\right) \leq s_{max}^2$$

This is treated in chapter 6.1, 6.2 and 6.4 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.

## Tresca's failure model
Tresca assumed failure if the shear stress exceeds a certain limit value $c$:

- $|\sigma_1 - \sigma_2| \leq 2c$
- $|\sigma_2 - \sigma_3| \leq 2c$
- $|\sigma_3 - \sigma_1| \leq 2c$

This is treated in chapter 6.3 and 6.4 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`.

## Exercises
- Additional question Problems 3 in chapter 5.3 of the lecture notes Introduction to Continuum Mechanics {cite:p}`Hartsuijker2007con`. Answers are available in chapter 5 of the lecture notes.